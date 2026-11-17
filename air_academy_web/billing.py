"""Stripe helpers for Open Air Tech Space.

Pure functions only: no Flask and no database in here, so all of it can be tested on its own.

How a payment works (Stripe's hosted Checkout page, so no card details ever touch this server):
  1. The server creates a Checkout Session and sends the student to the page Stripe hosts.
  2. The student pays there and comes back to the app.
  3. The server asks Stripe what really happened (and Stripe also calls our signed webhook), checks the amount, the
     currency, the reference and the owner, and only then unlocks the track.
"""
import hashlib
import hmac
import time
from decimal import Decimal, InvalidOperation

API = "https://api.stripe.com/v1"
API_VERSION = "2024-06-20"   # pinned, so Stripe changing its defaults later cannot change what these requests return

# Currencies the app can be priced in. Every one of these is a two-decimal currency in Stripe, so amounts go to Stripe in the
# smallest unit (kobo, cents, pence): 4000 naira is 400000.
CURRENCIES = {"ngn": "₦", "usd": "$", "gbp": "£", "eur": "€", "ghs": "GH₵", "kes": "KSh ", "zar": "R", "cad": "CA$", "aud": "A$"}


def price_minor(amount, currency):
    """'4000' or '2.99' in a currency -> the smallest-unit integer Stripe wants. Raises ValueError for anything odd."""
    cur = str(currency or "").strip().lower()
    if cur not in CURRENCIES:
        raise ValueError(f"unsupported currency {currency!r}")
    try:
        d = Decimal(str(amount).replace(",", "").strip())
    except InvalidOperation:
        raise ValueError(f"not a number: {amount!r}") from None
    if not d.is_finite() or d <= 0 or d > 10_000_000:
        raise ValueError(f"amount out of range: {amount!r}")
    return int((d * 100).to_integral_value())


def money_text(minor, currency):
    """400000, 'ngn' -> '₦4,000'.  300, 'usd' -> '$3'.  299, 'usd' -> '$2.99'."""
    cur = str(currency or "").lower()
    sym = CURRENCIES.get(cur, cur.upper() + " ")
    major = Decimal(int(minor or 0)) / 100
    return f"{sym}{major:,.0f}" if major == major.to_integral_value() else f"{sym}{major:,.2f}"


def key_mode(secret_key):
    """'test', 'live' or '' from the look of a secret (or restricted) key."""
    k = str(secret_key or "")
    return "test" if k.startswith(("sk_test_", "rk_test_")) else "live" if k.startswith(("sk_live_", "rk_live_")) else ""


def flw_key_mode(key):
    """'test', 'live' or '' from the look of a Flutterwave key (public FLWPUBK..., secret FLWSECK..., either one)."""
    k = str(key or "").strip().upper()
    if k.startswith(("FLWPUBK_TEST", "FLWSECK_TEST")):
        return "test"
    return "live" if k.startswith(("FLWPUBK", "FLWSECK")) else ""


def whole_dollars(raw, lo=1, hi=200):
    """FLW_USD_AMOUNT from the environment: a whole number of dollars between lo and hi, else 0 (meaning: no dollar option)."""
    try:
        n = int(str(raw or "").strip().lstrip("$"))
    except ValueError:
        return 0
    return n if lo <= n <= hi else 0


def checkout_form(*, tx_ref, uid, course_id, course_title, email, currency, amount_minor, success_url, cancel_url):
    """The form fields for POST /v1/checkout/sessions. The payment methods shown are decided in the Stripe Dashboard
    (Settings > Payment methods), so turning on a new one never needs a code change."""
    desc = f"Open Air Tech Space: {course_title}"[:250]
    return {
        "mode": "payment",
        "client_reference_id": tx_ref,
        "customer_email": email,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "line_items[0][quantity]": "1",
        "line_items[0][price_data][currency]": str(currency).lower(),
        "line_items[0][price_data][unit_amount]": str(int(amount_minor)),
        "line_items[0][price_data][product_data][name]": str(course_title)[:120],
        "line_items[0][price_data][product_data][description]": "One-time payment. Lifetime access to this track."[:300],
        "metadata[tx_ref]": tx_ref, "metadata[uid]": uid, "metadata[course_id]": course_id,
        "payment_intent_data[description]": desc,
        "payment_intent_data[metadata][tx_ref]": tx_ref,
        "payment_intent_data[metadata][uid]": uid,
        "payment_intent_data[metadata][course_id]": course_id,
    }


def sign_payload(secret, payload, timestamp=None):
    """A Stripe-Signature header value for `payload` (bytes). The server only verifies; tests use this to play Stripe."""
    t = int(timestamp if timestamp is not None else time.time())
    mac = hmac.new(secret.encode(), str(t).encode() + b"." + payload, hashlib.sha256).hexdigest()
    return f"t={t},v1={mac}"


def verify_signature(secret, header, payload, now=None, tolerance=300):
    """True only for an untampered body, signed with our webhook secret, no older than `tolerance` seconds."""
    if not secret or not header or not isinstance(payload, (bytes, bytearray)):
        return False
    stamp, sigs = None, []
    for item in str(header).split(","):
        k, _, v = item.strip().partition("=")
        if k == "t":
            stamp = v
        elif k == "v1":
            sigs.append(v)
    try:
        t = int(stamp)
    except (TypeError, ValueError):
        return False
    if not sigs or abs((time.time() if now is None else now) - t) > tolerance:
        return False
    want = hmac.new(secret.encode(), stamp.encode() + b"." + bytes(payload), hashlib.sha256).hexdigest().encode()
    return any(hmac.compare_digest(want, s.encode()) for s in sigs)


def judge_session(s, pay):
    """Decide what a Stripe Checkout Session means for one of our payment rows.

    Returns (state, why): 'paid' (safe to unlock), 'pending' (not paid yet: bank transfers can take a while),
    'failed' (expired or abandoned) or 'mismatch' (something does not add up, never unlock).
    `s` is the session object from Stripe, `pay` is our payments row (anything with these keys)."""
    if not isinstance(s, dict) or s.get("object") not in (None, "checkout.session"):
        return "mismatch", "not a checkout session"
    meta = s.get("metadata") or {}
    if (s.get("client_reference_id") or meta.get("tx_ref")) != pay["tx_ref"]:
        return "mismatch", "reference does not match"
    if meta.get("uid") not in (None, pay["uid"]) or meta.get("course_id") not in (None, pay["course_id"]):
        return "mismatch", "student or course does not match"
    if pay.get("stripe_session_id") and s.get("id") != pay["stripe_session_id"]:
        return "mismatch", "session id does not match"
    if s.get("mode") != "payment":
        return "mismatch", "not a one-time payment"
    if str(s.get("currency") or "").lower() != str(pay["currency"]).lower():
        return "mismatch", "currency does not match"
    if pay.get("amount_minor") is None or s.get("amount_total") != pay["amount_minor"]:
        return "mismatch", "amount does not match"
    if s.get("payment_status") == "paid":
        return "paid", ""
    if s.get("status") == "expired":
        return "failed", "expired"
    return "pending", str(s.get("payment_status") or "unpaid")
