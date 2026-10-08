"""Open Air Tech Space: Flask backend. Accounts (name, date of birth, gender, password) verified by email code (sent through Resend), progress, quizzes, CA record, exams, certificates, project studio + Flutterwave paywall (3,500 NGN per course)."""
import hashlib, hmac, json, logging, os, random, re, secrets, sqlite3, time, uuid
from datetime import date, datetime, timezone
from functools import wraps

import requests
from dotenv import load_dotenv
from flask import Flask, g, jsonify, request, send_from_directory, session
from markupsafe import escape
from werkzeug.security import check_password_hash, generate_password_hash

from course_content import CONTENT, KINDS, RUBRIC, STEPS
from courses_seed import COURSES, LESSONS, NOTES

load_dotenv()

ENV = os.getenv("APP_ENV", "development")
DB_PATH = os.getenv("DATABASE_PATH", "academy.db")
FLW_PUBLIC = os.getenv("FLW_PUBLIC_KEY", "")
FLW_SECRET = os.getenv("FLW_SECRET_KEY", "")
FLW_HASH = os.getenv("FLW_WEBHOOK_HASH", "")

PRICE_NGN = 3500          # flat, non-negotiable, enforced server-side only
CURRENCY = "NGN"
OTP_TTL, OTP_MAX_ATTEMPTS, RESEND_SECONDS = 600, 5, 60

log = logging.getLogger("academy")
logging.basicConfig(level=logging.INFO)

app = Flask(__name__, static_folder="static", static_url_path="/static")
_secret = os.getenv("SECRET_KEY")
if not _secret:
    if ENV == "production":
        raise RuntimeError("SECRET_KEY must be set in production")
    _secret = secrets.token_hex(32)
    log.warning("SECRET_KEY not set: using a temporary one (sessions reset on restart).")
app.config.update(
    SECRET_KEY=_secret,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=(ENV == "production"),
    PERMANENT_SESSION_LIFETIME=60 * 60 * 24 * 30,
    MAX_CONTENT_LENGTH=64 * 1024,
)

# ───────────────────────── Database (SQLite) ─────────────────────────
SCHEMA = """
CREATE TABLE IF NOT EXISTS users(
  uid TEXT PRIMARY KEY, email TEXT NOT NULL UNIQUE, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS courses(
  id TEXT PRIMARY KEY, title TEXT NOT NULL, description TEXT NOT NULL,
  cover_image TEXT NOT NULL DEFAULT '', lessons_count INTEGER NOT NULL);
-- enrolledCourses (List<String>) is stored relationally and returned as an array by the API.
CREATE TABLE IF NOT EXISTS enrollments(
  uid TEXT NOT NULL REFERENCES users(uid), course_id TEXT NOT NULL REFERENCES courses(id),
  created_at TEXT NOT NULL, PRIMARY KEY(uid, course_id));
CREATE TABLE IF NOT EXISTS otp_codes(
  email TEXT PRIMARY KEY, code_hash TEXT NOT NULL, expires_at INTEGER NOT NULL,
  attempts INTEGER NOT NULL DEFAULT 0, sent_at INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS payments(
  tx_ref TEXT PRIMARY KEY, uid TEXT NOT NULL, course_id TEXT NOT NULL,
  amount INTEGER NOT NULL, currency TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'pending',
  flw_transaction_id TEXT UNIQUE, created_at TEXT NOT NULL, verified_at TEXT);
"""

EXTRA_SCHEMA = """
CREATE TABLE IF NOT EXISTS pending_signups(
  email TEXT PRIMARY KEY, full_name TEXT NOT NULL, dob TEXT NOT NULL, gender TEXT NOT NULL, pw_hash TEXT NOT NULL, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS progress(
  uid TEXT NOT NULL, course_id TEXT NOT NULL, lesson_n INTEGER NOT NULL, done_at TEXT NOT NULL, PRIMARY KEY(uid, course_id, lesson_n));
CREATE TABLE IF NOT EXISTS scores(
  id INTEGER PRIMARY KEY AUTOINCREMENT, uid TEXT NOT NULL, course_id TEXT NOT NULL, kind TEXT NOT NULL,
  ref INTEGER NOT NULL DEFAULT 0, score INTEGER NOT NULL, max_score INTEGER NOT NULL, taken_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS certificates(
  cert_id TEXT PRIMARY KEY, uid TEXT NOT NULL, course_id TEXT NOT NULL, full_name TEXT NOT NULL,
  score INTEGER NOT NULL, issued_at TEXT NOT NULL, UNIQUE(uid, course_id));
"""

GROUP_SCHEMA = """
CREATE TABLE IF NOT EXISTS class_groups(
  id TEXT PRIMARY KEY, name TEXT NOT NULL, owner_uid TEXT NOT NULL, join_code TEXT NOT NULL UNIQUE,
  admin_token TEXT NOT NULL UNIQUE, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS class_group_courses(
  group_id TEXT NOT NULL, position INTEGER NOT NULL, course_id TEXT NOT NULL, PRIMARY KEY(group_id, position));
CREATE TABLE IF NOT EXISTS class_group_members(
  uid TEXT PRIMARY KEY, group_id TEXT NOT NULL, joined_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS purchase_requests(
  id INTEGER PRIMARY KEY AUTOINCREMENT, group_id TEXT NOT NULL, uid TEXT NOT NULL, course_id TEXT NOT NULL,
  status TEXT NOT NULL, created_at TEXT NOT NULL, decided_at TEXT, UNIQUE(uid, course_id));
"""


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def init_db():
    con = sqlite3.connect(DB_PATH)
    if os.getenv("SQLITE_WAL", "1") == "1":   # set SQLITE_WAL=0 on hosts where WAL misbehaves (one worker is fine without it)
        con.execute("PRAGMA journal_mode=WAL")
    con.executescript(SCHEMA)
    con.executescript(EXTRA_SCHEMA)
    con.executescript(GROUP_SCHEMA)
    have = {r[1] for r in con.execute("PRAGMA table_info(users)")}
    for col in ("full_name", "dob", "gender", "pw_hash"):   # older databases get the new account columns
        if col not in have:
            con.execute(f"ALTER TABLE users ADD COLUMN {col} TEXT NOT NULL DEFAULT ''")
    for c in COURSES:
        con.execute(
            """INSERT INTO courses(id,title,description,lessons_count) VALUES(?,?,?,?)
               ON CONFLICT(id) DO UPDATE SET title=excluded.title, description=excluded.description,
               lessons_count=excluded.lessons_count""",
            (c["id"], c["title"], c["description"], len(c["lessons"])),
        )
    con.commit()
    con.close()


def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH, timeout=10)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys=ON")
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    d = g.pop("db", None)
    if d is not None:
        d.close()


init_db()

# ───────────────────────── Helpers ─────────────────────────
EMAIL_RX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def err(message, status=400):
    return jsonify(error=message), status


def norm_email(v):
    v = (v or "").strip().lower() if isinstance(v, str) else ""
    return v if EMAIL_RX.match(v) and len(v) <= 254 else None


def current_user():
    uid = session.get("uid")
    if not uid:
        return None
    return db().execute("SELECT * FROM users WHERE uid=?", (uid,)).fetchone()


def login_required(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        u = current_user()
        if u is None:
            session.clear()
            return err("Please sign in.", 401)
        g.user = u
        return fn(*a, **kw)
    return wrapper


def enrolled_ids(uid):
    rows = db().execute("SELECT course_id FROM enrollments WHERE uid=? ORDER BY created_at", (uid,))
    return [r["course_id"] for r in rows]


def user_json(u):
    return {"uid": u["uid"], "email": u["email"], "fullName": u["full_name"], "dob": u["dob"], "gender": u["gender"],
            "enrolledCourses": enrolled_ids(u["uid"]), "createdAt": u["created_at"]}


def course_json(r):
    return {"id": r["id"], "title": r["title"], "description": r["description"],
            "coverImage": r["cover_image"], "lessonsCount": r["lessons_count"]}


def lesson_json(cid, i, title):
    notes = NOTES.get(cid, [])
    goal, pts, act = ((notes[i] if i < len(notes) else "").split("|") + ["", "", ""])[:3]
    return {"n": i + 1, "title": title, "goal": goal.strip(), "points": [p.strip() for p in pts.split(";") if p.strip()],
            "activity": act.strip(), "deep": (i + 1) in CONTENT.get(cid, {})}


@app.before_request
def json_only_posts():
    # Cross-site forms can't send application/json without a CORS preflight, which blocks CSRF.
    if request.method == "POST" and request.endpoint != "flutterwave_webhook" and not request.is_json:
        return err("Content-Type must be application/json.", 415)


@app.after_request
def secure_headers(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["Referrer-Policy"] = "same-origin"
    if request.path.startswith("/api/"):
        resp.headers["Cache-Control"] = "no-store"
    return resp

# ───────────────────────── Passwordless auth (email OTP) ─────────────────────────


def hash_code(email, code):
    return hmac.new(app.config["SECRET_KEY"].encode(), f"{email}:{code}".encode(), hashlib.sha256).hexdigest()


APP_NAME = "Open Air Tech Space"
EMAIL_TIMEOUT = 10   # seconds Resend gets to answer


def resend_ready():
    return bool(os.getenv("RESEND_API_KEY") and os.getenv("RESEND_FROM"))


def send_resend(to, subject, text, html):
    """Resend HTTP API. RESEND_FROM must be on a domain verified in Resend, e.g. 'Open Air Tech Space <no-reply@yourdomain.com>'."""
    r = requests.post("https://api.resend.com/emails",
                      headers={"Authorization": f"Bearer {os.getenv('RESEND_API_KEY')}", "User-Agent": "open-air-tech-space/1.0"},
                      json={"from": os.getenv("RESEND_FROM", ""), "to": [to], "subject": subject, "text": text, "html": html},
                      timeout=EMAIL_TIMEOUT)
    if not r.ok:
        log.error("Resend rejected the email (HTTP %s): %s", r.status_code, r.text[:300])
        r.raise_for_status()


def send_code_email(email, code):
    if not resend_ready():
        if ENV == "production":
            raise RuntimeError("RESEND_API_KEY and RESEND_FROM must be set in production")
        print(f"\n{'=' * 44}\n  {APP_NAME.upper()} LOGIN CODE for {email}: {code}\n{'=' * 44}\n", flush=True)
        return
    subject = f"{code} is your {APP_NAME} sign-in code"
    text = f"Your {APP_NAME} sign-in code is {code}\n\nIt expires in 10 minutes. If you didn't ask for it, ignore this email."
    html = f"""<div style="background:#0D0E15;padding:32px 16px;font-family:Arial,Helvetica,sans-serif">
      <div style="max-width:440px;margin:0 auto;background:#151830;border:1px solid #2a2f55;border-radius:20px;padding:32px;text-align:center;color:#E8ECF5">
        <div style="font-size:20px;font-weight:700;color:#00F0FF">{APP_NAME}</div>
        <p style="color:#8A93AD;margin:18px 0 8px">Your sign-in code</p>
        <div style="font-size:40px;font-weight:700;letter-spacing:10px;color:#fff;padding:14px 0 14px 10px;background:#0D0E15;border:1px solid #00F0FF;border-radius:14px">{code}</div>
        <p style="color:#8A93AD;font-size:13px;margin:20px 0 0">Expires in 10 minutes. If you didn't request it, you can ignore this email.</p>
      </div></div>"""
    send_resend(email, subject, text, html)


@app.post("/api/auth/request-code")
def request_code():
    email = norm_email((request.get_json(silent=True) or {}).get("email"))
    if not email:
        return err("Enter a valid email address.")
    now = int(time.time())
    row = db().execute("SELECT sent_at FROM otp_codes WHERE email=?", (email,)).fetchone()
    if row and now - row["sent_at"] < RESEND_SECONDS:
        return err(f"Please wait {RESEND_SECONDS - (now - row['sent_at'])}s before requesting another code.", 429)
    code = f"{secrets.randbelow(10 ** 6):06d}"
    db().execute("INSERT OR REPLACE INTO otp_codes(email,code_hash,expires_at,attempts,sent_at) VALUES(?,?,?,?,?)",
                 (email, hash_code(email, code), now + OTP_TTL, 0, now))
    db().commit()
    try:
        send_code_email(email, code)
    except Exception:
        log.exception("failed to send OTP email")
        db().execute("DELETE FROM otp_codes WHERE email=?", (email,))
        db().commit()
        return err("We couldn't send the email. Please try again shortly.", 503)
    return jsonify(ok=True, resendIn=RESEND_SECONDS)


def consume_code(email, code):
    """Check a 6-digit code and use it up. Returns an error response, or None when the code is right."""
    if not email or not re.fullmatch(r"\d{6}", code):
        return err("Enter the 6-digit code.")
    now = int(time.time())
    row = db().execute("SELECT * FROM otp_codes WHERE email=?", (email,)).fetchone()
    if not row or row["expires_at"] < now:
        return err("That code has expired. Request a new one.")
    if row["attempts"] >= OTP_MAX_ATTEMPTS:
        db().execute("DELETE FROM otp_codes WHERE email=?", (email,))
        db().commit()
        return err("Too many attempts. Request a new code.", 429)
    db().execute("UPDATE otp_codes SET attempts=attempts+1 WHERE email=?", (email,))
    db().commit()
    if not hmac.compare_digest(row["code_hash"], hash_code(email, code)):
        return err("Incorrect code.")
    db().execute("DELETE FROM otp_codes WHERE email=?", (email,))
    db().commit()
    return None


def start_session(u):
    session.clear()
    session["uid"] = u["uid"]
    session.permanent = True
    return jsonify(user=user_json(u))


GENDERS = {"female", "male", "other"}
FAILS = {}   # email -> (failed attempts, window start): stops password guessing


def password_problem(pw):
    if not isinstance(pw, str) or not 8 <= len(pw) <= 128:
        return "Your password must be 8 to 128 characters."
    if not (re.search(r"[A-Za-z]", pw) and re.search(r"\d", pw)):
        return "Use letters and at least one number in your password."
    return None


@app.post("/api/auth/register")
def register():
    b = request.get_json(silent=True) or {}
    email, name, pw = norm_email(b.get("email")), " ".join(str(b.get("fullName", "")).split()), b.get("password")
    if not email:
        return err("Enter a valid email address.")
    if " " not in name or not 3 <= len(name) <= 80:
        return err("Enter your full name (first and last name).")
    try:
        dob = date.fromisoformat(str(b.get("dob", "")))
    except ValueError:
        return err("Enter your date of birth.")
    if not 5 <= (date.today() - dob).days / 365.25 <= 110:
        return err("Check your date of birth.")
    if b.get("gender") not in GENDERS:
        return err("Choose a gender option.")
    if password_problem(pw):
        return err(password_problem(pw))
    u = db().execute("SELECT pw_hash FROM users WHERE email=?", (email,)).fetchone()
    if u and u["pw_hash"]:
        return err("An account with this email already exists. Sign in instead.", 409)
    # Details wait here until the email code proves the address is theirs; only then do they touch a real account.
    db().execute("INSERT OR REPLACE INTO pending_signups VALUES(?,?,?,?,?,?)",
                 (email, name, dob.isoformat(), b["gender"], generate_password_hash(pw), now_iso()))
    db().commit()
    return request_code()


@app.post("/api/auth/verify-code")
def verify_code():
    body = request.get_json(silent=True) or {}
    email, code = norm_email(body.get("email")), str(body.get("code", "")).strip()
    p = db().execute("SELECT * FROM pending_signups WHERE email=?", (email,)).fetchone() if email else None
    if p is None:
        return err("Start by creating your account.", 404)
    bad = consume_code(email, code)
    if bad:
        return bad
    u = db().execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    if u is None:
        db().execute("INSERT INTO users(uid,email,created_at,full_name,dob,gender,pw_hash) VALUES(?,?,?,?,?,?,?)",
                     (uuid.uuid4().hex, email, now_iso(), p["full_name"], p["dob"], p["gender"], p["pw_hash"]))
    else:   # an older passwordless account keeps its courses and gains a profile and password
        db().execute("UPDATE users SET full_name=?, dob=?, gender=?, pw_hash=? WHERE uid=?",
                     (p["full_name"], p["dob"], p["gender"], p["pw_hash"], u["uid"]))
    db().execute("DELETE FROM pending_signups WHERE email=?", (email,))
    db().commit()
    return start_session(db().execute("SELECT * FROM users WHERE email=?", (email,)).fetchone())


@app.post("/api/auth/login")
def login():
    b = request.get_json(silent=True) or {}
    email, pw = norm_email(b.get("email")), b.get("password")
    if not email or not isinstance(pw, str):
        return err("Enter your email and password.")
    n, t0 = FAILS.get(email, (0, 0))
    if time.time() - t0 > 900:
        n, t0 = 0, time.time()
    if n >= 5:
        return err("Too many attempts. Try again in a few minutes.", 429)
    u = db().execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    if not u or not u["pw_hash"] or not check_password_hash(u["pw_hash"], pw):
        FAILS[email] = (n + 1, t0 or time.time())
        return err("Email or password is incorrect.", 401)
    FAILS.pop(email, None)
    return start_session(u)


@app.post("/api/auth/reset")
def reset_password():
    b = request.get_json(silent=True) or {}
    email, pw = norm_email(b.get("email")), b.get("password")
    if password_problem(pw):
        return err(password_problem(pw))
    bad = consume_code(email, str(b.get("code", "")).strip())
    if bad:
        return bad
    u = db().execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    if u is None:
        return err("No account found for that email. Create one instead.", 404)
    db().execute("UPDATE users SET pw_hash=? WHERE uid=?", (generate_password_hash(pw), u["uid"]))
    db().commit()
    FAILS.pop(email, None)
    return start_session(u)


@app.post("/api/auth/logout")
def logout():
    session.clear()
    return jsonify(ok=True)


@app.get("/api/me")
@login_required
def me():
    return jsonify(user=user_json(g.user))

# ───────────────────────── Courses ─────────────────────────


@app.get("/api/courses")
@login_required
def courses():
    uid = g.user["uid"]
    rows = db().execute("SELECT * FROM courses ORDER BY title").fetchall()
    num = {r["id"]: i + 1 for i, r in enumerate(rows)}   # Class 1, Class 2... follow the dashboard order
    counts = {r["course_id"]: r["c"] for r in db().execute(
        "SELECT course_id, COUNT(*) c FROM progress WHERE uid=? GROUP BY course_id", (uid,))}
    grp, owned = group_of(uid), enrolled_ids(uid)
    scheme = scheme_of(grp["id"]) if grp else []
    if grp:   # a class group only sees its own classes, in the teacher's order (plus anything already bought)
        by = {r["id"]: r for r in rows}
        rows = [by[c] for c in scheme if c in by] + [r for r in rows if r["id"] in owned and r["id"] not in scheme]
    out = []
    for r in rows:
        item = course_json(r) | {"doneCount": counts.get(r["id"], 0), "classNo": num[r["id"]], "access": purchase_access(uid, r["id"], grp, owned)}
        if r["id"] in scheme:
            item["step"] = scheme.index(r["id"]) + 1
        out.append(item)
    pending = db().execute("""SELECT COUNT(*) c FROM purchase_requests p JOIN class_groups c ON c.id=p.group_id
                              WHERE c.owner_uid=? AND p.status='pending'""", (uid,)).fetchone()["c"]
    return jsonify(courses=out, group=group_summary(grp) if grp else None, pending=pending,
                   canCreate=not GROUP_CREATORS or g.user["email"] in GROUP_CREATORS)


@app.get("/api/courses/<cid>")
@login_required
def course_detail(cid):
    r = db().execute("SELECT * FROM courses WHERE id=?", (cid,)).fetchone()
    if r is None:
        return err("Course not found.", 404)
    unlocked = cid in enrolled_ids(g.user["uid"])
    out = course_json(r) | {"unlocked": unlocked, "lessons": None}
    if unlocked:   # real content is never sent to locked users
        out["lessons"] = [lesson_json(cid, i, t) for i, t in enumerate(LESSONS.get(cid, []))]
        out["done"] = done_list(g.user["uid"], cid)
    return jsonify(out)

# ───────────────────────── Flutterwave payments ─────────────────────────


def flw_verify(transaction_id):
    r = requests.get(f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify",
                     headers={"Authorization": f"Bearer {FLW_SECRET}"}, timeout=20)
    return r.json() if r.content else {}


def fulfil(tx_ref, transaction_id):
    """Verify with Flutterwave, then enroll. Idempotent. Returns (ok, message, http_status)."""
    con = db()
    pay = con.execute("SELECT * FROM payments WHERE tx_ref=?", (tx_ref,)).fetchone()
    if pay is None:
        return False, "Unknown payment reference.", 404
    if pay["status"] == "verified":
        return True, "Already verified.", 200
    try:
        body = flw_verify(transaction_id)
    except requests.RequestException:
        log.exception("flutterwave verify failed")
        return False, "Could not reach the payment provider. Try again in a moment.", 502
    d = (body or {}).get("data") or {}
    owner = con.execute("SELECT email FROM users WHERE uid=?", (pay["uid"],)).fetchone()
    valid = (
        body.get("status") == "success"
        and d.get("status") == "successful"
        and d.get("tx_ref") == tx_ref
        and d.get("currency") == pay["currency"] == CURRENCY
        and float(d.get("amount") or 0) >= pay["amount"] == PRICE_NGN
        and owner is not None
        and str((d.get("customer") or {}).get("email", "")).lower() == owner["email"]
    )
    if not valid:
        log.warning("payment rejected tx_ref=%s flw_status=%s", tx_ref, d.get("status"))
        return False, "Payment could not be verified.", 402
    try:
        with con:   # atomic
            con.execute("UPDATE payments SET status='verified', flw_transaction_id=?, verified_at=? "
                        "WHERE tx_ref=? AND status='pending'", (str(d["id"]), now_iso(), tx_ref))
            con.execute("INSERT OR IGNORE INTO enrollments(uid,course_id,created_at) VALUES(?,?,?)",
                        (pay["uid"], pay["course_id"], now_iso()))
    except sqlite3.IntegrityError:   # this Flutterwave transaction already paid for another reference
        return False, "This transaction was already used.", 409
    return True, "Verified.", 200


@app.post("/api/payments/init")
@login_required
def payment_init():
    cid = (request.get_json(silent=True) or {}).get("courseId")
    if not isinstance(cid, str) or db().execute("SELECT 1 FROM courses WHERE id=?", (cid,)).fetchone() is None:
        return err("Course not found.", 404)
    if cid in enrolled_ids(g.user["uid"]):
        return err("You already own this course.", 409)
    gate = purchase_access(g.user["uid"], cid)
    if gate["state"] != "open":
        return err(GATE_MESSAGES.get(gate["state"], "You cannot buy this class right now."), 403)
    if not FLW_PUBLIC:
        return err("Payments are not configured yet.", 503)
    tx_ref = f"OATS-{uuid.uuid4().hex}"   # unique per attempt
    db().execute("INSERT INTO payments(tx_ref,uid,course_id,amount,currency,created_at) VALUES(?,?,?,?,?,?)",
                 (tx_ref, g.user["uid"], cid, PRICE_NGN, CURRENCY, now_iso()))
    db().commit()
    return jsonify(txRef=tx_ref, amount=PRICE_NGN, currency=CURRENCY, publicKey=FLW_PUBLIC,
                   email=g.user["email"], courseId=cid)


@app.post("/api/payments/verify")
@login_required
def payment_verify():
    body = request.get_json(silent=True) or {}
    tx_ref, tid = body.get("txRef"), body.get("transactionId")
    if not isinstance(tx_ref, str) or not re.fullmatch(r"\d{1,20}", str(tid or "")):
        return err("txRef and transactionId are required.")
    pay = db().execute("SELECT uid FROM payments WHERE tx_ref=?", (tx_ref,)).fetchone()
    if pay is None or pay["uid"] != g.user["uid"]:
        return err("Unknown payment reference.", 404)
    ok, msg, status = fulfil(tx_ref, str(tid))
    if not ok:
        return err(msg, status)
    return jsonify(ok=True, user=user_json(g.user))


@app.post("/api/flutterwave/webhook")
def flutterwave_webhook():
    """Safety net if the browser closes mid-payment. Set the URL + secret hash in the Flutterwave dashboard."""
    sent = request.headers.get("verif-hash", "")
    if not FLW_HASH or not hmac.compare_digest(sent, FLW_HASH):
        return "", 401
    d = (request.get_json(silent=True) or {}).get("data") or {}
    if d.get("tx_ref") and d.get("id"):
        fulfil(d["tx_ref"], str(d["id"]))
    return "", 200

# ───────────────────────── Progress, quizzes, CA record, exams, certificates ─────────────────────────
W_CA, W_EXAM, PASS_MARK, EXAM_SIZE = 40, 60, 50, 10     # CA 40% + exam 60%, pass at 50%


def done_list(uid, cid):
    rows = db().execute("SELECT lesson_n FROM progress WHERE uid=? AND course_id=? ORDER BY lesson_n", (uid, cid))
    return [r["lesson_n"] for r in rows]


def locked_error(cid):
    return None if cid in enrolled_ids(g.user["uid"]) else err("Unlock this course first.", 403)


@app.post("/api/progress")
@login_required
def set_progress():
    b = request.get_json(silent=True) or {}
    cid, n = b.get("courseId"), b.get("n")
    bad = locked_error(cid)
    if bad:
        return bad
    if not isinstance(n, int) or not 1 <= n <= len(LESSONS.get(cid, [])):
        return err("Lesson not found.", 404)
    if b.get("done"):
        db().execute("INSERT OR IGNORE INTO progress VALUES(?,?,?,?)", (g.user["uid"], cid, n, now_iso()))
    else:
        db().execute("DELETE FROM progress WHERE uid=? AND course_id=? AND lesson_n=?", (g.user["uid"], cid, n))
    db().commit()
    return jsonify(done=done_list(g.user["uid"], cid))


def quiz_of(cid, n):
    return (CONTENT.get(cid, {}).get(n) or {}).get("quiz", [])


def best_quiz(uid, cid, n):
    return db().execute("SELECT MAX(score) m FROM scores WHERE uid=? AND course_id=? AND kind='quiz' AND ref=?", (uid, cid, n)).fetchone()["m"]


@app.get("/api/courses/<cid>/lessons/<int:n>")
@login_required
def lesson_page(cid, n):
    bad = locked_error(cid)
    if bad:
        return bad
    c = CONTENT.get(cid, {}).get(n)
    if not c:
        return err("This lesson page is being prepared.", 404)
    out = {k: c[k] for k in ("minutes", "hook", "sections", "diagram", "caption", "terms", "mistakes")}
    return jsonify(out | {"n": n, "title": LESSONS[cid][n - 1], "activity": lesson_json(cid, n - 1, "")["activity"], "quiz": [{"q": q["q"], "o": q["o"]} for q in c["quiz"]],
                          "best": best_quiz(g.user["uid"], cid, n), "next": (n + 1) in CONTENT[cid]})


def grade(qs, answers):
    """Answers never leave the server before grading: the client only ever receives questions and options."""
    if not qs or not isinstance(answers, list) or len(answers) != len(qs):
        return None
    return [{"ok": a == q["a"], "answer": q["a"], "why": q["why"]} for q, a in zip(qs, answers)]


def record(kind, cid, ref, res):
    score = sum(r["ok"] for r in res)
    db().execute("INSERT INTO scores(uid,course_id,kind,ref,score,max_score,taken_at) VALUES(?,?,?,?,?,?,?)",
                 (g.user["uid"], cid, kind, ref, score, len(res), now_iso()))
    db().commit()
    return score


@app.post("/api/quiz/<cid>/<int:n>")
@login_required
def submit_quiz(cid, n):
    bad = locked_error(cid)
    if bad:
        return bad
    res = grade(quiz_of(cid, n), (request.get_json(silent=True) or {}).get("answers"))
    if not res:
        return err("Answer every question first.")
    return jsonify(score=record("quiz", cid, n, res), max=len(res), results=res)


def exam_pool(cid):
    return [(n, i) for n, c in sorted(CONTENT.get(cid, {}).items()) for i in range(len(c["quiz"]))]


@app.get("/api/exam/<cid>")
@login_required
def exam_start(cid):
    bad = locked_error(cid)
    if bad:
        return bad
    pool = exam_pool(cid)
    if len(pool) < 4:
        return err("The exam for this course is being prepared.", 404)
    todo = [n for n in CONTENT[cid] if best_quiz(g.user["uid"], cid, n) is None]
    if todo:
        return err("Finish the lesson quizzes first (lesson " + ", ".join(map(str, todo)) + ").", 403)
    refs = random.sample(pool, min(EXAM_SIZE, len(pool)))
    session["exam"] = {"cid": cid, "refs": refs}
    return jsonify(questions=[{"q": CONTENT[cid][n]["quiz"][i]["q"], "o": CONTENT[cid][n]["quiz"][i]["o"]} for n, i in refs])


@app.post("/api/exam/<cid>")
@login_required
def exam_submit(cid):
    bad = locked_error(cid)
    if bad:
        return bad
    ex = session.get("exam")
    if not ex or ex["cid"] != cid:
        return err("Start the exam again.", 409)
    res = grade([CONTENT[cid][n]["quiz"][i] for n, i in ex["refs"]], (request.get_json(silent=True) or {}).get("answers"))
    if not res:
        return err("Answer every question first.")
    session.pop("exam")
    return jsonify(score=record("exam", cid, 0, res), max=len(res), results=res, ca=ca_record(g.user["uid"], cid))


def ca_record(uid, cid):
    """Continuous assessment: best score per lesson quiz (40%) + best exam (60%). Pass mark 50%."""
    rows = db().execute("""SELECT kind, ref, MAX(CAST(score AS REAL) / max_score) pct, COUNT(*) tries FROM scores
                           WHERE uid=? AND course_id=? GROUP BY kind, ref""", (uid, cid)).fetchall()
    quiz = {r["ref"]: r for r in rows if r["kind"] == "quiz"}
    exam = next((r for r in rows if r["kind"] == "exam"), None)
    lessons = [{"n": n, "title": LESSONS[cid][n - 1], "pct": round(quiz[n]["pct"] * 100) if n in quiz else None,
                "tries": quiz[n]["tries"] if n in quiz else 0} for n in sorted(CONTENT.get(cid, {}))]
    ca = round(sum(l["pct"] or 0 for l in lessons) / len(lessons)) if lessons else 0
    ex = round(exam["pct"] * 100) if exam else None
    total = round(ca * W_CA / 100 + (ex or 0) * W_EXAM / 100)
    cert = db().execute("SELECT cert_id FROM certificates WHERE uid=? AND course_id=?", (uid, cid)).fetchone()
    return {"lessons": lessons, "ca": ca, "exam": ex, "examTries": exam["tries"] if exam else 0, "total": total,
            "passed": ex is not None and total >= PASS_MARK, "cert": cert["cert_id"] if cert else None,
            "weights": {"ca": W_CA, "exam": W_EXAM, "pass": PASS_MARK},
            "examReady": len(exam_pool(cid)) >= 4 and all(l["pct"] is not None for l in lessons)}


@app.get("/api/ca/<cid>")
@login_required
def ca_get(cid):
    return locked_error(cid) or jsonify(ca_record(g.user["uid"], cid))


def cert_row(cert_id):
    return db().execute("SELECT c.*, k.title FROM certificates c JOIN courses k ON k.id=c.course_id WHERE c.cert_id=?",
                        (str(cert_id).upper(),)).fetchone()


def cert_json(r):
    base = (os.getenv("PUBLIC_URL") or request.host_url).rstrip("/")
    return {"certId": r["cert_id"], "fullName": r["full_name"], "course": r["title"], "score": r["score"],
            "issuedAt": r["issued_at"][:10], "verifyUrl": f"{base}/verify/{r['cert_id']}"}


@app.post("/api/certificate/<cid>")
@login_required
def certificate_issue(cid):
    bad = locked_error(cid)
    if bad:
        return bad
    rec = ca_record(g.user["uid"], cid)
    if not rec["passed"]:
        return err(f"Pass the final exam with an overall score of {PASS_MARK}% or more to earn your certificate.", 403)
    if not g.user["full_name"]:
        return err("Your account has no full name yet. Create your account again with your full name to earn certificates.", 409)
    db().execute("INSERT OR IGNORE INTO certificates VALUES(?,?,?,?,?,?)",
                 (f"OATS-{datetime.now().year}-{secrets.token_hex(4).upper()}", g.user["uid"], cid, g.user["full_name"], rec["total"], now_iso()))
    db().commit()
    cid_ = db().execute("SELECT cert_id FROM certificates WHERE uid=? AND course_id=?", (g.user["uid"], cid)).fetchone()["cert_id"]
    return jsonify(cert_json(cert_row(cid_)))


@app.get("/api/verify/<cert_id>")
def verify_api(cert_id):
    r = cert_row(cert_id)
    return jsonify(valid=True, **{k: cert_json(r)[k] for k in ("certId", "fullName", "course", "score", "issuedAt")}) if r else err("No certificate with that ID.", 404)


@app.get("/verify/<cert_id>")
def verify_page(cert_id):
    r = cert_row(cert_id)
    body = (f"<h1>Certificate verified</h1><p><b>{escape(r['full_name'])}</b> completed <b>{escape(r['title'])}</b> on {r['issued_at'][:10]} "
            f"with an overall score of {r['score']}%.</p><p>Certificate ID: {escape(r['cert_id'])}</p>") if r else \
           "<h1>Certificate not found</h1><p>Check the ID and try again.</p>"
    return (f'<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Certificate check</title>'
            f'<body style="font:16px/1.6 system-ui,sans-serif;background:#0D0E15;color:#E8ECF5;max-width:560px;margin:12vh auto;padding:0 20px">'
            f'<div style="border:1px solid #00F0FF;border-radius:20px;padding:28px">{body}<p style="color:#8A93AD">{APP_NAME}</p></div>')


# ───────────────────────── Project studio ─────────────────────────


def make_project(cid, theme, level):
    k, n = KINDS[cid], {"beginner": 3, "intermediate": 5, "advanced": 7}[level]
    return {"title": f"{theme}: {k['name']}",
            "scenario": f"A {theme.lower()} in Nigeria needs {k['need']}. You have been hired to deliver it, and the people who will use it are real.",
            "objective": f"Plan, build, test and present a {k['name'].lower()} that solves the {theme.lower()}'s problem.",
            "requirements": k["req"][:n], "steps": STEPS, "deliverables": k["out"],
            "stretch": k["req"][n:n + 2] or ["Present it live to a real user and write down their feedback."],
            "hours": {"beginner": 4, "intermediate": 8, "advanced": 15}[level], "ai": False}


def ai_project(cid, theme, level, base):
    """Optional: with OPENAI_API_KEY set, the AI tailors the project. Any failure falls back to the template."""
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return None
    try:
        title = db().execute("SELECT title FROM courses WHERE id=?", (cid,)).fetchone()["title"]
        r = requests.post("https://api.openai.com/v1/chat/completions", headers={"Authorization": f"Bearer {key}"}, timeout=40, json={
            "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"), "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": "You design practical class projects for beginners in Nigeria. Reply with one JSON object only."},
                         {"role": "user", "content": f"Course: {title}. Theme: {theme}. Level: {level}. Design one realistic project a student can finish. "
                          f"JSON keys: title, scenario, objective (strings), requirements (list of {len(base['requirements'])} strings), steps (list), "
                          "deliverables (list), stretch (list of 2 strings), hours (number). Plain English a beginner can follow."}]})
        r.raise_for_status()
        d = json.loads(r.json()["choices"][0]["message"]["content"])
        out = {k: str(d[k])[:400] for k in ("title", "scenario", "objective")}
        for k in ("requirements", "steps", "deliverables", "stretch"):
            out[k] = [str(x)[:300] for x in d[k]][:10]
        return base | out | {"hours": int(d["hours"]), "ai": True}
    except Exception:
        log.exception("AI project generation failed, using the template")
        return None


@app.post("/api/projects/generate")
@login_required
def project_generate():
    b = request.get_json(silent=True) or {}
    cid, level = b.get("courseId"), b.get("level")
    bad = locked_error(cid)
    if bad:
        return bad
    if cid not in KINDS:
        return err("Projects for this course are coming soon.", 404)
    if level not in ("beginner", "intermediate", "advanced"):
        return err("Choose a level.")
    theme = re.sub(r"[^\w\s&'-]", "", str(b.get("theme", "")))[:40].strip() or "School"
    base = make_project(cid, theme, level)
    return jsonify(project=ai_project(cid, theme, level, base) or base, rubric=[{"item": i, "points": p} for i, p in RUBRIC])


# ───────────────────────── Class groups ─────────────────────────
# A teacher makes a group and picks the classes in order. Students join with the join link. Inside a group a student
# can only buy the next class in the scheme, and every class after the first needs the teacher to say yes.
GROUP_CREATORS = {e.strip().lower() for e in os.getenv("GROUP_CREATOR_EMAILS", "").split(",") if e.strip()}   # empty = any signed-in user
GATE_MESSAGES = {
    "outside": "This class is not part of your class group.",
    "later": "Finish your earlier class first. Classes unlock one at a time.",
    "needs_request": "Ask your teacher to allow this class first.",
    "pending": "Your teacher has not decided yet. You will be able to unlock this class once it is allowed.",
    "denied": "Your teacher has not allowed this class yet.",
}


def group_of(uid):
    return db().execute("SELECT c.* FROM class_groups c JOIN class_group_members m ON m.group_id=c.id WHERE m.uid=?", (uid,)).fetchone()


def scheme_of(gid):
    return [r["course_id"] for r in db().execute("SELECT course_id FROM class_group_courses WHERE group_id=? ORDER BY position", (gid,))]


def group_summary(grp):
    titles = {r["id"]: r["title"] for r in db().execute("SELECT id, title FROM courses")}
    return {"id": grp["id"], "name": grp["name"], "steps": [{"id": c, "title": titles.get(c, c)} for c in scheme_of(grp["id"])]}


def group_links(grp):
    base = (os.getenv("PUBLIC_URL") or request.host_url).rstrip("/")
    return {"joinUrl": f"{base}/join/{grp['join_code']}", "adminUrl": f"{base}/admin/{grp['admin_token']}"}


def purchase_access(uid, cid, grp=None, owned=None):
    """Where a student stands on buying one class. People outside any group buy freely."""
    grp = grp if grp is not None else group_of(uid)
    if grp is None:
        return {"state": "open"}
    owned = owned if owned is not None else enrolled_ids(uid)
    scheme = scheme_of(grp["id"])
    if cid in owned:
        return {"state": "owned"}
    if cid not in scheme:
        return {"state": "outside"}
    todo = [c for c in scheme if c not in owned]
    if todo[0] != cid:
        return {"state": "later", "next": todo[0]}
    if scheme[0] == cid:
        return {"state": "open"}          # the first class needs no approval
    r = db().execute("SELECT status FROM purchase_requests WHERE uid=? AND course_id=?", (uid, cid)).fetchone()
    return {"state": {"allowed": "open", "pending": "pending", "denied": "denied"}.get(r["status"] if r else None, "needs_request")}


def send_plain_email(to, subject, text, html):
    """Best-effort notices. A failure here must never break the student's request."""
    if not resend_ready():
        print(f"\n[email to {to}] {subject}\n{text}\n", flush=True)
        return
    send_resend(to, subject, text, html)


def notify_admin(grp, student, course_id):
    owner = db().execute("SELECT email FROM users WHERE uid=?", (grp["owner_uid"],)).fetchone()
    course = db().execute("SELECT title FROM courses WHERE id=?", (course_id,)).fetchone()
    if not owner or not course:
        return
    who, link = student["full_name"] or student["email"], group_links(grp)["adminUrl"]
    subject = f"{who} wants to unlock {course['title']}"
    text = f"{who} ({student['email']}) in your group \"{grp['name']}\" asked to unlock {course['title']}.\n\nAllow or do not allow here:\n{link}"
    html = (f'<div style="font-family:Arial,sans-serif;max-width:480px;margin:auto;padding:24px;border:1px solid #2a2f55;border-radius:16px">'
            f'<h2 style="margin:0 0 8px">{escape(who)} wants to unlock {escape(course["title"])}</h2>'
            f'<p>Group: <b>{escape(grp["name"])}</b>. Student email: {escape(student["email"])}.</p>'
            f'<p><a href="{escape(link)}" style="display:inline-block;padding:12px 22px;border-radius:12px;background:#00F0FF;color:#04121a;text-decoration:none;font-weight:700">Allow or do not allow</a></p></div>')
    try:
        send_plain_email(owner["email"], subject, text, html)
    except Exception:
        log.exception("could not email the class admin")


@app.get("/api/groups/catalog")
@login_required
def group_catalog():
    rows = db().execute("SELECT id, title FROM courses ORDER BY title").fetchall()
    return jsonify(courses=[{"id": r["id"], "title": r["title"], "classNo": i + 1} for i, r in enumerate(rows)],
                   canCreate=not GROUP_CREATORS or g.user["email"] in GROUP_CREATORS)


@app.post("/api/groups")
@login_required
def group_create():
    b = request.get_json(silent=True) or {}
    name, ids = " ".join(str(b.get("name", "")).split()), b.get("courses")
    if GROUP_CREATORS and g.user["email"] not in GROUP_CREATORS:
        return err("Only approved teachers can create class groups.", 403)
    if not 3 <= len(name) <= 60:
        return err("Give the group a name of 3 to 60 characters.")
    valid = {r["id"] for r in db().execute("SELECT id FROM courses")}
    if not (isinstance(ids, list) and ids and all(isinstance(i, str) and i in valid for i in ids) and len(set(ids)) == len(ids)):
        return err("Pick at least one class, each only once.")
    gid = uuid.uuid4().hex
    db().execute("INSERT INTO class_groups VALUES(?,?,?,?,?,?)", (gid, name, g.user["uid"], secrets.token_urlsafe(8), secrets.token_urlsafe(24), now_iso()))
    for pos, cid in enumerate(ids):
        db().execute("INSERT INTO class_group_courses VALUES(?,?,?)", (gid, pos, cid))
    db().commit()
    grp = db().execute("SELECT * FROM class_groups WHERE id=?", (gid,)).fetchone()
    return jsonify(group=group_summary(grp) | group_links(grp))


@app.get("/api/groups/mine")
@login_required
def group_mine():
    out = []
    for grp in db().execute("SELECT * FROM class_groups WHERE owner_uid=? ORDER BY created_at DESC", (g.user["uid"],)).fetchall():
        n = db().execute("SELECT COUNT(*) c FROM class_group_members WHERE group_id=?", (grp["id"],)).fetchone()["c"]
        p = db().execute("SELECT COUNT(*) c FROM purchase_requests WHERE group_id=? AND status='pending'", (grp["id"],)).fetchone()["c"]
        out.append(group_summary(grp) | group_links(grp) | {"students": n, "pending": p})
    return jsonify(groups=out)


@app.get("/api/groups/join/<code>")
def group_invite(code):
    grp = db().execute("SELECT * FROM class_groups WHERE join_code=?", (code,)).fetchone()
    return jsonify(group=group_summary(grp)) if grp else err("This invite link is not valid.", 404)


@app.post("/api/groups/join/<code>")
@login_required
def group_join(code):
    grp = db().execute("SELECT * FROM class_groups WHERE join_code=?", (code,)).fetchone()
    if not grp:
        return err("This invite link is not valid.", 404)
    cur = group_of(g.user["uid"])
    if cur and cur["id"] != grp["id"]:
        return err("You are already in a class group. Ask your teacher if you need to move.", 409)
    if not cur:
        db().execute("INSERT INTO class_group_members VALUES(?,?,?)", (g.user["uid"], grp["id"], now_iso()))
        db().commit()
    return jsonify(group=group_summary(grp))


@app.post("/api/groups/request")
@login_required
def group_request():
    cid, uid = (request.get_json(silent=True) or {}).get("courseId"), g.user["uid"]
    grp = group_of(uid)
    if not grp:
        return err("You are not in a class group.", 403)
    if not isinstance(cid, str):
        return err("Class not found.", 404)
    state = purchase_access(uid, cid, grp)["state"]
    if state not in ("needs_request", "denied", "pending"):
        return err(GATE_MESSAGES.get(state, "You cannot ask for this class right now."), 403)
    if state != "pending":    # asking again while waiting does not email the teacher twice
        db().execute("""INSERT INTO purchase_requests(group_id,uid,course_id,status,created_at) VALUES(?,?,?,'pending',?)
                        ON CONFLICT(uid, course_id) DO UPDATE SET status='pending', created_at=excluded.created_at, decided_at=NULL""",
                     (grp["id"], uid, cid, now_iso()))
        db().commit()
        notify_admin(grp, g.user, cid)
    return jsonify(access=purchase_access(uid, cid, grp))


def admin_group(token):
    return db().execute("SELECT * FROM class_groups WHERE admin_token=?", (token,)).fetchone()


@app.get("/api/groups/admin/<token>")
def admin_view(token):
    grp = admin_group(token)
    if not grp:
        return err("This admin link is not valid.", 404)
    steps, titles = scheme_of(grp["id"]), {r["id"]: r["title"] for r in db().execute("SELECT id, title FROM courses")}
    reqs = db().execute("""SELECT r.id, r.status, r.created_at, r.decided_at, r.course_id, u.full_name, u.email FROM purchase_requests r
                           JOIN users u ON u.uid=r.uid WHERE r.group_id=? ORDER BY (r.status='pending') DESC, r.created_at DESC""", (grp["id"],)).fetchall()
    students = []
    for m in db().execute("""SELECT u.uid, u.full_name, u.email, m.joined_at FROM class_group_members m JOIN users u ON u.uid=m.uid
                             WHERE m.group_id=? ORDER BY m.joined_at""", (grp["id"],)).fetchall():
        owned, classes = enrolled_ids(m["uid"]), []
        for cid in steps:
            if cid not in owned:
                classes.append({"id": cid, "owned": False})
                continue
            rec = ca_record(m["uid"], cid) if CONTENT.get(cid) else None
            classes.append({"id": cid, "owned": True, "done": len(done_list(m["uid"], cid)), "total": len(LESSONS.get(cid, [])),
                            "score": {k: rec[k] for k in ("ca", "exam", "total", "passed")} if rec else None})
        students.append({"uid": m["uid"], "name": m["full_name"] or m["email"], "email": m["email"], "joinedAt": m["joined_at"][:10], "classes": classes})
    return jsonify(group=group_summary(grp) | group_links(grp), students=students,
                   requests=[{"id": r["id"], "status": r["status"], "student": r["full_name"] or r["email"], "email": r["email"],
                              "course": titles.get(r["course_id"], r["course_id"]), "at": r["created_at"][:16].replace("T", " ")} for r in reqs])


@app.post("/api/groups/admin/<token>/requests/<int:rid>")
def admin_decide(token, rid):
    grp = admin_group(token)
    if not grp:
        return err("This admin link is not valid.", 404)
    allow = (request.get_json(silent=True) or {}).get("allow")
    if not isinstance(allow, bool):
        return err("Choose allow or do not allow.")
    cur = db().execute("UPDATE purchase_requests SET status=?, decided_at=? WHERE id=? AND group_id=?",
                       ("allowed" if allow else "denied", now_iso(), rid, grp["id"]))
    db().commit()
    return jsonify(ok=True) if cur.rowcount else err("Request not found.", 404)


@app.post("/api/groups/admin/<token>/students/<uid>/remove")
def admin_remove(token, uid):
    grp = admin_group(token)
    if not grp:
        return err("This admin link is not valid.", 404)
    db().execute("DELETE FROM class_group_members WHERE uid=? AND group_id=?", (uid, grp["id"]))
    db().execute("DELETE FROM purchase_requests WHERE uid=? AND group_id=?", (uid, grp["id"]))
    db().commit()
    return jsonify(ok=True)


# ───────────────────────── Frontend ─────────────────────────


@app.get("/")
@app.get("/join/<code>")
@app.get("/admin/<token>")
def index(**_):
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=(ENV != "production"))
