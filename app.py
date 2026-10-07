"""Air Academy: Flask backend. Passwordless email-OTP auth + Flutterwave paywall (3,500 NGN per course)."""
import hashlib, hmac, logging, os, re, secrets, smtplib, sqlite3, time, uuid
from datetime import datetime, timezone
from email.message import EmailMessage
from functools import wraps

import requests
from dotenv import load_dotenv
from flask import Flask, g, jsonify, request, send_from_directory, session

from courses_seed import COURSES, LESSONS

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


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def init_db():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA journal_mode=WAL")
    con.executescript(SCHEMA)
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
    return {"uid": u["uid"], "email": u["email"], "enrolledCourses": enrolled_ids(u["uid"]), "createdAt": u["created_at"]}


def course_json(r):
    return {"id": r["id"], "title": r["title"], "description": r["description"],
            "coverImage": r["cover_image"], "lessonsCount": r["lessons_count"]}


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


def send_code_email(email, code):
    host = os.getenv("SMTP_HOST", "")
    if not host:
        if ENV == "production":
            raise RuntimeError("SMTP is not configured")
        print(f"\n{'=' * 44}\n  AIR ACADEMY LOGIN CODE for {email}: {code}\n{'=' * 44}\n", flush=True)
        return
    msg = EmailMessage()
    msg["Subject"] = f"{code} is your Air Academy sign-in code"
    msg["From"] = os.getenv("SMTP_FROM", os.getenv("SMTP_USER", "no-reply@localhost"))
    msg["To"] = email
    msg.set_content(f"Your Air Academy sign-in code is {code}\n\nIt expires in 10 minutes. If you didn't ask for it, ignore this email.")
    msg.add_alternative(
        f"""<div style="font-family:system-ui;background:#0D0E15;color:#E8ECF5;padding:32px;text-align:center">
        <h2 style="color:#00F0FF;letter-spacing:3px">AIR ACADEMY</h2><p>Your sign-in code</p>
        <p style="font-size:38px;letter-spacing:10px;font-weight:700;color:#fff">{code}</p>
        <p style="color:#8A93AD">Expires in 10 minutes. If you didn't request it, ignore this email.</p></div>""",
        subtype="html")
    port = int(os.getenv("SMTP_PORT", "587"))
    if port == 465:
        s = smtplib.SMTP_SSL(host, port, timeout=15)
    else:
        s = smtplib.SMTP(host, port, timeout=15)
        s.starttls()
    with s:
        if os.getenv("SMTP_USER"):
            s.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS", ""))
        s.send_message(msg)


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


@app.post("/api/auth/verify-code")
def verify_code():
    body = request.get_json(silent=True) or {}
    email, code = norm_email(body.get("email")), str(body.get("code", "")).strip()
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
    u = db().execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    if u is None:   # first sign-in creates the account: no separate sign-up, no password
        db().execute("INSERT INTO users(uid,email,created_at) VALUES(?,?,?)", (uuid.uuid4().hex, email, now_iso()))
        u = db().execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    db().commit()
    session.clear()
    session["uid"] = u["uid"]
    session.permanent = True
    return jsonify(user=user_json(u))


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
    rows = db().execute("SELECT * FROM courses ORDER BY title").fetchall()
    return jsonify(courses=[course_json(r) for r in rows])


@app.get("/api/courses/<cid>")
@login_required
def course_detail(cid):
    r = db().execute("SELECT * FROM courses WHERE id=?", (cid,)).fetchone()
    if r is None:
        return err("Course not found.", 404)
    unlocked = cid in enrolled_ids(g.user["uid"])
    out = course_json(r) | {"unlocked": unlocked, "lessons": None}
    if unlocked:   # real content is never sent to locked users
        out["lessons"] = [{"n": i + 1, "title": t} for i, t in enumerate(LESSONS.get(cid, []))]
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
    if not FLW_PUBLIC:
        return err("Payments are not configured yet.", 503)
    tx_ref = f"AIR-{uuid.uuid4().hex}"   # unique per attempt
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

# ───────────────────────── Frontend ─────────────────────────


@app.get("/")
def index():
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=(ENV != "production"))
