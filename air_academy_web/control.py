"""Owner Control Room maths: what each service costs, where the month is heading, and when to worry.

Pure functions only (no Flask and no database in here), so all of it can be tested on its own.
Every price below is an ESTIMATE in US dollars taken from the provider's public price list. They are all in this one file,
so when a provider changes a price you only edit it here.
"""
import calendar
import math
from datetime import datetime, timedelta, timezone

LAGOS = timezone(timedelta(hours=1))

# ───────────────────────── Prices ─────────────────────────
# OpenAI text models, US dollars per 1 million tokens: (input, output, cached input). Longest matching name wins.
CHAT_PRICES = {
    "gpt-5.6-sol": (4.00, 20.00, 0.40), "gpt-5.6-terra": (2.00, 12.00, 0.20), "gpt-5.6-luna": (0.20, 1.20, 0.02),
    "gpt-5.5-pro": (30.00, 180.00, 30.00), "gpt-5.5": (5.00, 30.00, 0.50),
    "gpt-5.4-pro": (30.00, 180.00, 30.00), "gpt-5.4-mini": (0.75, 4.50, 0.075), "gpt-5.4-nano": (0.20, 1.25, 0.02), "gpt-5.4": (2.50, 15.00, 0.25),
    "gpt-5.3": (1.75, 14.00, 0.175), "gpt-5.2-pro": (21.00, 168.00, 21.00), "gpt-5.2": (1.75, 14.00, 0.175),
    "gpt-5.1": (1.25, 10.00, 0.125), "gpt-5-pro": (15.00, 120.00, 15.00), "gpt-5-mini": (0.25, 2.00, 0.025),
    "gpt-5-nano": (0.05, 0.40, 0.005), "gpt-5": (1.25, 10.00, 0.125),
    "gpt-4.1-nano": (0.10, 0.40, 0.025), "gpt-4.1-mini": (0.40, 1.60, 0.10), "gpt-4.1": (2.00, 8.00, 0.50),
    "gpt-4o-mini": (0.15, 0.60, 0.075), "gpt-4o": (2.50, 10.00, 1.25),
    "o4-mini": (1.10, 4.40, 0.275), "o3-mini": (1.10, 4.40, 0.55), "o3": (2.00, 8.00, 0.50), "o1": (15.00, 60.00, 7.50),
}
DEFAULT_CHAT = (1.00, 4.00, 0.25)   # a model not in the list above: a middle-of-the-road guess, shown as "estimated"
# Image models, dollars per 1M tokens: (text in, image in, image out).
IMAGE_PRICES = {"gpt-image-2": (5.0, 8.0, 30.0), "gpt-image-1-mini": (2.0, 2.5, 8.0), "gpt-image-1": (5.0, 10.0, 40.0)}
# When the image API does not report tokens: dollars per picture by quality, (square, wide or tall), output only.
IMAGE_FLAT = {"low": (0.006, 0.005), "medium": (0.053, 0.041), "high": (0.211, 0.165)}

# Plans, as they appear in the Control Room's drop-downs.
RENDER_TIERS = [("Free", 0, 15), ("Starter", 7, 40), ("Standard", 25, 150), ("Pro", 85, 400)]       # name, $/month, live students it handles comfortably (a rough guide)
SUPABASE_TIERS = [("Free", 0, 500), ("Pro", 25, 8192)]                                              # name, $/month, database MB included
RESEND_TIERS = [("Free", 0, 3000, 100), ("Pro 50k", 20, 50000, 0), ("Pro 100k", 35, 100000, 0)]     # name, $/month, emails a month, emails a day (0 = no daily cap)
SUPABASE_EXTRA_PER_GB = 0.125
RESEND_EXTRA_PER_1000 = 0.90

FEATURE_LABELS = {
    "talk_send": "Air Omega chat", "mentor_ask": "Lesson mentor", "practice_make": "Weak-spot practice", "practice_submit": "Weak-spot practice",
    "assignment_create": "Assignments (writing them)", "assignment_submit": "Assignments (marking)", "play_scene": "Scene playground",
    "play_agent": "Agent Lab", "play_prompt": "Prompt Lab", "project_generate": "Project Studio", "lesson_image_make": "Lesson pictures",
    "voice_speak": "Air Omega's voice", "voice_transcribe": "Voice messages", "background": "Background jobs",
}


def feature_label(kind):
    return FEATURE_LABELS.get(kind) or str(kind).replace("_", " ").capitalize()


def email_kind(subject):
    s = str(subject).lower()
    return ("owner alerts" if s.startswith("control room:") else "sign-in codes" if "sign-in code" in s else "parent confirmations" if "confirm weekly" in s else "parent reports" if "'s week at" in s
            else "teacher reports" if "class week" in s else "class notices" if "wants to unlock" in s else "other emails")


# ───────────────────────── Costs of one call ─────────────────────────
def chat_price(model):
    """((input, output, cached), known). `known` is False when the model is not in the list and a guess is used."""
    m = str(model or "").lower()
    for name in sorted(CHAT_PRICES, key=len, reverse=True):
        if m.startswith(name):
            return CHAT_PRICES[name], True
    return DEFAULT_CHAT, False


def chat_cost(model, prompt_tokens, completion_tokens, cached_tokens=0):
    (pin, pout, pcache), _ = chat_price(model)
    p, c = max(0, int(prompt_tokens or 0)), max(0, int(completion_tokens or 0))
    cached = min(p, max(0, int(cached_tokens or 0)))
    return ((p - cached) * pin + cached * pcache + c * pout) / 1e6


def image_cost(model, quality, size, usage=None):
    """Dollars for one picture. Uses the token counts the API reports; falls back to the typical price for that quality and size."""
    m = str(model or "").lower()
    pt = next((p for name, p in sorted(IMAGE_PRICES.items(), key=lambda kv: -len(kv[0])) if m.startswith(name)), IMAGE_PRICES["gpt-image-2"])
    if isinstance(usage, dict) and usage.get("output_tokens"):
        d = usage.get("input_tokens_details") or {}
        text = d.get("text_tokens")
        text = usage.get("input_tokens", 0) if text is None else text
        return (text * pt[0] + (d.get("image_tokens") or 0) * pt[1] + usage["output_tokens"] * pt[2]) / 1e6
    sq, wide = IMAGE_FLAT.get(quality) or IMAGE_FLAT["medium"]
    return sq if str(size) in ("1024x1024", "auto") else wide


def tts_cost(model, chars):
    m, chars = str(model or "").lower(), max(0, int(chars or 0))
    if m.startswith("tts-1-hd"):
        return chars * 30 / 1e6
    if m.startswith("tts-1"):
        return chars * 15 / 1e6
    return chars / 900 * 0.015   # gpt-4o-mini-tts: about $0.015 a minute of speech, and about 900 characters make a minute


def stt_cost(model, usage=None, size_bytes=0):
    """Dollars for one voice message turned into text."""
    m = str(model or "").lower()
    mini = "mini" in m
    if isinstance(usage, dict) and usage.get("type") == "duration" and usage.get("seconds"):
        return usage["seconds"] / 60 * (0.003 if mini else 0.006)
    if isinstance(usage, dict) and usage.get("type") == "tokens":
        d = usage.get("input_token_details") or {}
        audio, text = d.get("audio_tokens"), d.get("text_tokens") or 0
        if audio is not None:
            a, t, o = (3.0, 1.25, 5.0) if mini else (6.0, 2.5, 10.0)
            return (audio * a + text * t + (usage.get("output_tokens") or 0) * o) / 1e6
    minutes = min(300, max(1, int(size_bytes or 0) / 4000)) / 60   # a phone recording is roughly 4 KB a second
    return minutes * (0.003 if mini else 0.006)


# ───────────────────────── The month ─────────────────────────
def _utc(dt):
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


def month_window(now=None):
    """The current calendar month in Lagos time. `start` and `end` are UTC ISO strings that compare correctly with the app's timestamps."""
    n = (now or datetime.now(timezone.utc)).astimezone(LAGOS)
    start = n.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    days = calendar.monthrange(n.year, n.month)[1]
    return {"start": _utc(start), "end": _utc(start + timedelta(days=days)), "days": days, "elapsed": (n - start).total_seconds() / 86400,
            "label": n.strftime("%B %Y"), "key": n.strftime("%Y-%m"), "today": n.strftime("%Y-%m-%d"), "dayOfMonth": n.day}


def project(so_far, elapsed_days, days_in_month):
    """Where a running total will end the month if the pace holds. The first day counts as a full day, so one busy hour cannot predict a huge bill."""
    return so_far / max(elapsed_days, 1.0) * days_in_month


def gauge(used, limit):
    """(percent used, level). A limit of 0 means there is no limit."""
    if not limit:
        return 0.0, "ok"
    pct = used / limit * 100
    return round(pct, 1), ("bad" if pct >= 100 else "warn" if pct >= 80 else "ok")


# ───────────────────────── Settings the owner can change ─────────────────────────
SETTINGS = {   # key: (kind, lowest, highest, default)
    "usd_ngn": ("num", 100, 10000, 1500),           # naira per US dollar, to show costs in naira
    "openai_budget_usd": ("num", 0, 1000000, 20),   # the most you want to spend on OpenAI in a month
    "render_usd": ("num", 0, 5000, 7),
    "render_live_capacity": ("int", 5, 100000, 40),
    "supabase_usd": ("num", 0, 5000, 0),
    "supabase_db_mb": ("int", 50, 10000000, 500),
    "resend_usd": ("num", 0, 5000, 0),
    "resend_month_limit": ("int", 0, 100000000, 3000),
    "resend_day_limit": ("int", 0, 100000000, 100),
    "flw_fee_pct": ("num", 0, 20, 1.4),             # Flutterwave's cut of a naira sale, in percent (check your dashboard for your own rate)
    "flw_fee_cap_ngn": ("int", 0, 1000000, 2000),   # ...which Flutterwave caps at this many naira per sale
    "flw_intl_fee_pct": ("num", 0, 20, 3.8),        # Flutterwave's cut of a dollar (international card) sale, in percent
    "stripe_fee_pct": ("num", 0, 20, 2.9),
    "stripe_fee_fixed_usd": ("num", 0, 5, 0.30),
    "alert_emails": ("int", 0, 1, 1),               # 1 = email me when something needs attention
    "count_owner": ("int", 0, 1, 0),                # 1 = count the owner's own visits in the live number (handy for testing)
}


def _num(v, kind, lo, hi):
    if isinstance(v, bool) or v is None:
        raise ValueError
    f = float(str(v).replace(",", "").strip()) if isinstance(v, str) else float(v)
    if not math.isfinite(f) or not lo <= f <= hi:
        raise ValueError
    return int(round(f)) if kind == "int" else round(f, 4)


def settings_from(stored):
    """Typed settings: what is stored (text) where it is valid, the default everywhere else."""
    out = {}
    for k, (kind, lo, hi, default) in SETTINGS.items():
        try:
            out[k] = _num(stored[k], kind, lo, hi) if k in (stored or {}) else default
        except (ValueError, TypeError):
            out[k] = default
    return out


def clean_settings(raw):
    """(good, bad): the known settings that are valid numbers in range, and the names of those that are not. Unknown names are ignored."""
    good, bad = {}, []
    for k, v in (raw if isinstance(raw, dict) else {}).items():
        if k not in SETTINGS:
            continue
        kind, lo, hi, _ = SETTINGS[k]
        try:
            good[k] = _num(v, kind, lo, hi)
        except (ValueError, TypeError):
            bad.append(k)
    return good, bad


def presets():
    return {"render": [{"name": n, "usd": u, "live": c} for n, u, c in RENDER_TIERS],
            "supabase": [{"name": n, "usd": u, "mb": mb} for n, u, mb in SUPABASE_TIERS],
            "resend": [{"name": n, "usd": u, "month": mo, "day": d} for n, u, mo, d in RESEND_TIERS]}


# ───────────────────────── Money in, in dollars ─────────────────────────
def to_usd(minor, currency, usd_ngn):
    """A payment's smallest-unit amount in US dollars, or None for a currency this meter has no rate for (it is then listed on its own)."""
    cur, minor = str(currency or "").lower(), float(minor or 0)
    if cur == "usd":
        return minor / 100
    if cur == "ngn":
        return minor / 100 / usd_ngn if usd_ngn else None
    return None


def stripe_fee_usd(price_usd, s):
    """What Stripe keeps from one sale: a percentage plus a fixed amount."""
    return price_usd * s["stripe_fee_pct"] / 100 + s["stripe_fee_fixed_usd"]


def flw_fee_usd(amount_usd, currency, s):
    """What Flutterwave keeps from one sale, as an estimate. Naira sales pay a small percentage with a cap; sales in another currency
    (international cards) pay a higher percentage."""
    if str(currency or "").lower() == "ngn":
        rate = s["usd_ngn"] or 1
        pct = amount_usd * s["flw_fee_pct"] / 100
        return min(pct, s["flw_fee_cap_ngn"] / rate) if s["flw_fee_cap_ngn"] else pct
    return amount_usd * s["flw_intl_fee_pct"] / 100


def payment_fee_usd(provider, currency, amount_usd, s):
    """The provider's cut of one sale, in dollars. `provider` is 'stripe' or 'flutterwave'."""
    return stripe_fee_usd(amount_usd, s) if provider == "stripe" else flw_fee_usd(amount_usd, currency, s)


# ───────────────────────── "What if I had N students?" ─────────────────────────
ASSUMED = {"openai_usd": 0.30, "emails": 3.0, "db_mb": 2.0, "live_ratio": 0.08}   # used until there are enough real students to measure
MEASURE_MIN = 10   # active students needed before the real averages are trusted


def per_student(active, users, openai_30d, emails_30d, app_mb, base_mb, peak_live_7d):
    """What one active student costs a month, measured from real use when there are at least MEASURE_MIN of them, assumed otherwise.

    active: students who used the app in the last 30 days. users: everyone signed up. openai_30d, emails_30d: what the last 30 days used.
    app_mb: size of the app's own data. base_mb: what the database weighs apart from that. peak_live_7d: most students online together this week."""
    measured = active >= MEASURE_MIN
    if measured:
        per = {"openai_usd": openai_30d / active, "emails": emails_30d / active, "db_mb": app_mb / max(users, 1),
               "live_ratio": min(1.0, max(0.02, peak_live_7d / active))}
    else:
        per = dict(ASSUMED)
    per["base_mb"] = max(0.0, base_mb)
    per["measured"] = measured
    return per


def pick_tier(tiers, need, cap_index):
    """The cheapest tier whose capacity (the item at `cap_index`) covers `need`. Returns (tier, over) where over is True when even the top tier is too small."""
    for t in tiers:
        if need <= t[cap_index]:
            return t, False
    return tiers[-1], True


def whatif(students, per, s, price_usd, buy_rate, provider="flutterwave", currency="ngn"):
    """Monthly running costs for `students` active students a month.

    per: openai_usd (per student), emails (per student), db_mb (per student), base_mb (what the database weighs with no students),
         live_ratio (the share of a month's students online at the same time, at the busiest moment).
    s: the settings. price_usd: what one track sells for, in dollars. buy_rate: share of students who buy a track in a month (0 to 1).
    provider, currency: who takes the payment and in which currency, which decide the fee."""
    n = max(0, int(students))
    openai = n * per["openai_usd"]
    emails = n * per["emails"]
    rtier, rover = pick_tier(RESEND_TIERS, emails, 2)
    resend = rtier[1] + (max(0.0, emails - rtier[2]) / 1000 * RESEND_EXTRA_PER_1000 if rover else 0)
    mb = per["base_mb"] + n * per["db_mb"]
    stier, sover = pick_tier(SUPABASE_TIERS, mb, 2)
    supabase = stier[1] + (max(0.0, mb - stier[2]) / 1024 * SUPABASE_EXTRA_PER_GB if sover else 0)
    live = n * per["live_ratio"]
    ptier, pover = pick_tier(RENDER_TIERS[1:], live, 2)   # never suggest the Free plan for a paid app: it goes to sleep when idle
    sales = n * buy_rate
    fee = payment_fee_usd(provider, currency, price_usd, s)
    fees = sales * fee
    total = openai + resend + supabase + ptier[1] + fees
    net_per_sale = max(price_usd - fee, 0.01)
    fixed = resend + supabase + ptier[1]
    return {"students": n, "live": round(live, 1), "sales": round(sales, 1),
            "openai": round(openai, 2), "resend": {"usd": round(resend, 2), "plan": rtier[0], "emails": round(emails), "tooSmall": rover},
            "supabase": {"usd": round(supabase, 2), "plan": stier[0], "mb": round(mb), "tooSmall": sover},
            "render": {"usd": ptier[1], "plan": ptier[0], "tooSmall": pover}, "fees": round(fees, 2),
            "totalUsd": round(total, 2), "perStudentUsd": round(total / n, 3) if n else 0,
            "revenueUsd": round(sales * price_usd, 2), "profitUsd": round(sales * price_usd - total, 2),
            "breakEvenSales": math.ceil((openai + fixed) / net_per_sale) if (openai + fixed) > 0 else 0}


# ───────────────────────── Warnings ─────────────────────────
_ORDER = {"bad": 0, "warn": 1, "info": 2}


def _usd(x):
    return f"${x:,.2f}"


def evaluate(m, s):
    """Plain-English warnings for the owner, worst first. Each is {key, level, title, detail}.

    m: openai{mtd, projected, on}, resend{month, day, on}, supabase{db_bytes, images_bytes, images_n},
       render{peak_live, paid_students}, stripe{provider, mode, webhook_seen, stripe_sales, production},
       flw{mode, webhook_hash, webhook_seen, sales, recent_error, production},
       money{cost_projected, revenue_projected, day_of_month}."""
    out = []

    def add(key, level, title, detail):
        out.append({"key": key, "level": level, "title": title, "detail": detail})

    o = m.get("openai") or {}
    budget = s["openai_budget_usd"]
    if o.get("on") and budget:
        pct, lvl = gauge(o.get("mtd", 0), budget)
        if lvl == "bad":
            add("openai_budget", "bad", "OpenAI budget used up", f"About {_usd(o['mtd'])} spent this month against your {_usd(budget)} budget. Add credit at platform.openai.com or lower the daily AI limits, or Air Omega stops answering.")
        elif lvl == "warn":
            add("openai_budget", "warn", "OpenAI is close to your budget", f"{pct:.0f}% of your {_usd(budget)} monthly budget is used ({_usd(o['mtd'])}). Make sure your OpenAI balance has credit.")
        elif o.get("projected", 0) > budget:
            add("openai_pace", "warn", "OpenAI is on pace to go over budget", f"At this pace the month ends near {_usd(o['projected'])}, above your {_usd(budget)} budget.")
    elif not o.get("on"):
        add("openai_off", "info", "OpenAI is not switched on", "OPENAI_API_KEY is not set, so Air Omega, pictures and voice are off.")

    r = m.get("resend") or {}
    if r.get("on"):
        dpct, dlvl = gauge(r.get("day", 0), s["resend_day_limit"])
        mpct, mlvl = gauge(r.get("month", 0), s["resend_month_limit"])
        if dlvl == "bad":
            add("resend_day", "bad", "Daily email limit reached", f"{r['day']} emails sent today and your plan allows {s['resend_day_limit']} a day. New students cannot get their sign-in code until tomorrow. Upgrade Resend to remove the daily cap.")
        elif dlvl == "warn":
            add("resend_day", "warn", "Close to the daily email limit", f"{r['day']} of {s['resend_day_limit']} emails used today. Sign-in codes stop when it runs out.")
        if mlvl == "bad":
            add("resend_month", "bad", "Monthly email limit reached", f"{r['month']} of {s['resend_month_limit']:,} emails used this month. Upgrade Resend so sign-in codes keep arriving.")
        elif mlvl == "warn":
            add("resend_month", "warn", "Close to the monthly email limit", f"{mpct:.0f}% of this month's {s['resend_month_limit']:,} emails are used.")
    else:
        add("resend_off", "info", "Email sending is not set up", "RESEND_API_KEY / RESEND_FROM are not set, so sign-in codes cannot be emailed.")

    sb = m.get("supabase") or {}
    limit_bytes = s["supabase_db_mb"] * 1024 * 1024
    pct, lvl = gauge(sb.get("db_bytes", 0), limit_bytes)
    if lvl in ("warn", "bad"):
        pics = f" Lesson pictures take {sb.get('images_bytes', 0) / 1048576:,.0f} MB of it ({sb.get('images_n', 0)} pictures)." if sb.get("images_bytes", 0) > 0.2 * sb.get("db_bytes", 1) else ""
        add("supabase_size", lvl, "Database is almost full" if lvl == "warn" else "Database is full",
            f"{sb['db_bytes'] / 1048576:,.0f} MB of {s['supabase_db_mb']:,} MB used ({pct:.0f}%).{pics} A full free database can stop saving anything new. Upgrade Supabase to Pro ($25/month) or lower LESSON_IMAGE_LIMIT.")

    rd = m.get("render") or {}
    cap = s["render_live_capacity"]
    peak = rd.get("peak_live", 0)
    if cap and peak > cap:
        add("render_capacity", "bad", "More students online than your server plan handles", f"At the busiest moment this week {peak} students were online and your Render plan is rated for about {cap}. Pages will slow down. Move up a Render plan.")
    elif cap and peak >= 0.7 * cap:
        add("render_capacity", "warn", "Your server is getting busy", f"{peak} students were online together this week, and your Render plan is rated for about {cap}. Plan an upgrade before it fills.")
    if s["render_usd"] == 0 and rd.get("paid_students", 0) > 0:
        add("render_free", "warn", "Free Render plan with paying students", "Free Render services go to sleep when idle, so the first student of the day waits a long time. Starter ($7/month) stays awake.")

    st, fw = m.get("stripe") or {}, m.get("flw") or {}
    prov = st.get("provider")
    if prov is None:
        add("pay_none", "bad", "Students cannot pay", "No payment provider is set up. Add FLW_PUBLIC_KEY, FLW_SECRET_KEY and FLW_WEBHOOK_HASH on Render (Flutterwave > Settings > API keys).")
    elif prov == "flutterwave":
        if fw.get("production") and fw.get("mode") == "test":
            add("flw_test", "bad", "Flutterwave is in TEST mode", "The keys on Render are Flutterwave test keys. Anyone can pay with Flutterwave's test card and get a track free, and real cards will not work. Swap in your live keys (FLWPUBK-... and FLWSECK-...).")
        elif fw.get("mode") == "mixed":
            add("flw_mixed", "bad", "Your two Flutterwave keys do not match", "One key is a test key and the other is live. A student could be charged and the app would not be able to confirm it. Copy both keys from the same mode in Flutterwave > Settings > API keys.")
        if not fw.get("webhook_hash"):
            add("flw_hash", "warn", "Flutterwave webhook is not set up", "Without it, a student who closes the page right after paying may not get the track. In Flutterwave > Settings > Webhooks, add your site's /api/flutterwave/webhook address and a secret hash, then put the same hash in FLW_WEBHOOK_HASH on Render.")
        elif not fw.get("webhook_seen"):
            add("flw_webhook", "warn" if fw.get("sales", 0) else "info", "Flutterwave has not called your webhook yet",
                "Nothing received yet. Check the webhook address and that the secret hash in Flutterwave is the same as FLW_WEBHOOK_HASH on Render.")
        if fw.get("recent_error"):
            add("flw_rejected", "warn", "A Flutterwave payment could not be confirmed", f"{fw['recent_error']} If the student really paid, check the payment in your Flutterwave dashboard and use Give a track in this Control Room.")
    elif prov == "stripe":
        if st.get("production") and st.get("mode") == "test":
            add("stripe_test", "bad", "Stripe is in TEST mode", "The key on Render is a test key. Anyone can pay with Stripe's test card and get a track free, and real cards will not work. Swap in the live key (it starts with sk_live_).")
        if not st.get("webhook_seen"):
            add("stripe_webhook", "warn" if st.get("stripe_sales", 0) else "info", "Stripe webhook not heard yet",
                "Stripe has not called the webhook yet. Add the endpoint in Stripe and copy its signing secret into STRIPE_WEBHOOK_SECRET, so bank-transfer payments unlock even if the student closes the page.")

    mo = m.get("money") or {}
    if mo.get("day_of_month", 0) >= 10 and mo.get("cost_projected", 0) > mo.get("revenue_projected", 0) > 0:
        add("loss", "warn", "Costs are higher than sales this month", f"On pace for about {_usd(mo['cost_projected'])} of costs against {_usd(mo['revenue_projected'])} of sales.")

    out.sort(key=lambda w: _ORDER[w["level"]])
    return out
