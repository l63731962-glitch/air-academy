"""Payment helpers for Open Air Tech Space (Paystack).

Pure functions only: no Flask and no database in here, so all of it can be tested on its own.
"""
import hashlib
import hmac
from decimal import Decimal

# Money symbols. A currency that is not listed here is shown with its three-letter code.
CURRENCIES = {"ngn": "₦", "usd": "$"}


def money_text(minor, currency):
    """400000, 'ngn' -> '₦4,000'.  300, 'usd' -> '$3'.  299, 'usd' -> '$2.99'."""
    cur = str(currency or "").lower()
    sym = CURRENCIES.get(cur, cur.upper() + " ")
    major = Decimal(int(minor or 0)) / 100
    return f"{sym}{major:,.0f}" if major == major.to_integral_value() else f"{sym}{major:,.2f}"


def paystack_key_mode(key):
    """What a Paystack key looks like: 'test' (sk_test_...), 'live' (sk_live_...), 'public' (pk_..., which cannot confirm a payment
    and is the key people copy by mistake) or '' for anything else."""
    k = str(key or "").strip().lower()
    if k.startswith("sk_test_"):
        return "test"
    if k.startswith("sk_live_"):
        return "live"
    return "public" if k.startswith(("pk_test_", "pk_live_")) else ""


def signature_ok(raw_body, header, secret):
    """Paystack signs every webhook: the header x-paystack-signature is the HMAC-SHA512 of the raw request body, made with your
    secret key, written in hex. Anything else is not from Paystack."""
    if not secret or not header or not isinstance(raw_body, (bytes, bytearray)):
        return False
    want = hmac.new(secret.encode("utf-8"), bytes(raw_body), hashlib.sha512).hexdigest()
    return hmac.compare_digest(want.encode(), str(header).strip().lower().encode("utf-8", "replace"))


def initialize_url(body):
    """The payment page address from Paystack's answer to 'initialize', or '' when Paystack did not accept the payment."""
    if not isinstance(body, dict) or body.get("status") is not True or not isinstance(body.get("data"), dict):
        return ""
    url = body["data"].get("authorization_url")
    return url if isinstance(url, str) and url.startswith("https://") else ""


# What Paystack calls a payment that has started but not finished (a bank transfer can take a few minutes to clear).
WAITING = {"ongoing", "pending", "processing", "queued"}


def judge_verification(body, tx_ref, currency, charged_minor, accepted_minor, email):
    """Decide what Paystack's answer to 'verify' means. Returns (state, problems):

      'paid'     money arrived and every check passed (problems is empty)
      'waiting'  the payment is still in progress: ask again in a few seconds
      'unpaid'   not paid (failed, abandoned, unknown reference, garbage answer): nothing to worry about
      'mismatch' Paystack says it was paid but something does not fit; problems says what, so the owner can look into it

    charged_minor: what this app asked for, in kobo. accepted_minor: the set of prices (in kobo) this app sells or ever sold, so a
    payment started just before a price change still counts but a tampered amount never does. email: the student's address."""
    body = body if isinstance(body, dict) else {}
    d = body.get("data") if isinstance(body.get("data"), dict) else {}
    status = str(d.get("status") or "").lower()
    answered = body.get("status") is True
    if answered and status in WAITING:
        return "waiting", []
    if not (answered and status == "success"):
        return "unpaid", []
    try:
        paid = int(d.get("amount"))
    except (TypeError, ValueError):
        paid = 0
    who = str((d.get("customer") or {}).get("email", "") if isinstance(d.get("customer"), dict) else "").strip().lower()
    checks = (   # (what is wrong if this fails, did it pass)
        ("the reference does not match", d.get("reference") == tx_ref),
        ("the currency does not match", str(d.get("currency") or "").upper() == str(currency or "").upper()),
        ("the price is not one this app sells", charged_minor in accepted_minor),
        ("the amount paid is too low", paid >= charged_minor),
        ("the email on the payment is not the student's", bool(email) and who == str(email).strip().lower()),
    )
    problems = [why for why, ok in checks if not ok]
    return ("mismatch", problems) if problems else ("paid", [])
