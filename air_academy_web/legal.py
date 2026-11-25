"""Legal pages and the site footer for Open Air Tech Space (Paystack / Visa / Mastercard website disclosures).

Pure functions only: no Flask and no database in here, so all of it can be tested on its own.

Who is shown to the public is decided by settings on Render, never by this file (the code is on public GitHub):

    BUSINESS_NAME       optional. Defaults to "Open Air Tech Space". This is the name people see. No personal name is needed.
    SUPPORT_EMAIL       needed on a live site. Students write here for help and refunds. Use an address made for the app.
    SUPPORT_PHONE       optional.
    BUSINESS_LOCATION   optional, a town or city only (for example "Lagos"). Without it the site says "Based in Nigeria".
    BUSINESS_ADDRESS    optional. A street address is shown only if you set this. Card companies need ONE contact way
                        (email, phone or address), not all three.
    BUSINESS_REG_NO     optional. For example a CAC number. Shown in the footer if set.

Every promise the policies make (refund days, reply times and so on) is a number in the block below. Change a number and every page
that mentions it changes with it, so the pages can never disagree with each other. Only promise what you will really do.
"""
import html
import os
import re
from datetime import datetime, timezone

UPDATED = "19 November 2026"   # change this whenever you change the wording of a policy

REFUND_DAYS = 7           # change-of-mind refund window after payment
REPORT_DAYS = 30          # how long a student has to report a double charge or a wrong amount
REPLY_DAYS = 2            # business days to answer an email
FIX_DAYS = 1              # business days to fix a course that did not open
REFUND_START_DAYS = 3     # business days from "approved" to the refund being sent
RESOLVE_DAYS = 14         # days we aim to settle any complaint in
PRIVACY_DAYS = 30         # days to answer a data request
NOTICE_DAYS = 30          # warning before a paid course is ever withdrawn
LATE_MINUTES = 30         # how long after a payment before a student should write to us

PAYSTACK = "Paystack Payments Limited"
E = html.escape
EMAIL_RX = re.compile(r"^[^@\s<>\"'()]+@[^@\s<>\"'()]+\.[^@\s<>\"'()]+$")

PAGES = (
    ("terms", "/terms", "Terms of Service", "What you are buying, prices, payment, support and disputes."),
    ("refund-policy", "/refund-policy", "Refund Policy", "When you get your money back, how to ask, and how long it takes."),
    ("delivery-policy", "/delivery-policy", "Delivery Policy", "How and when your course opens after a successful payment."),
    ("privacy-policy", "/privacy-policy", "Privacy Policy", "What data we collect, why, who gets it (including Paystack) and your rights."),
)
ALIASES = {   # other addresses a reviewer might try: they all lead to the real page
    "/terms-of-service": "/terms", "/terms-and-conditions": "/terms", "/tos": "/terms",
    "/refunds": "/refund-policy", "/refund": "/refund-policy", "/return-policy": "/refund-policy",
    "/delivery": "/delivery-policy", "/privacy": "/privacy-policy",
}


# ───────────────────────── who we are (from Render settings) ─────────────────────────
def business(env=None):
    """The public business details, cleaned. env is a mapping (os.environ by default)."""
    e = os.environ if env is None else env

    def get(key):
        return " ".join(str(e.get(key, "") or "").split())[:200]
    return {"name": get("BUSINESS_NAME") or "Open Air Tech Space", "country": get("BUSINESS_COUNTRY") or "Nigeria",
            "place": get("BUSINESS_LOCATION"), "address": get("BUSINESS_ADDRESS"), "email": get("SUPPORT_EMAIL"),
            "phone": get("SUPPORT_PHONE"), "reg": get("BUSINESS_REG_NO")}


def contact_state(b, owner_emails=()):
    """For the Control Room: ('ok'|'warn'|'bad', what to tell the owner). A contact way is a must on a live site."""
    mail = b.get("email", "")
    if not mail:
        have = [w for w in ("phone", "address") if b.get(w)]
        if have:
            return "warn", "Add SUPPORT_EMAIL on Render too. The refund policy tells students to write to a support email."
        return "bad", "Add SUPPORT_EMAIL on Render (an address made for the app, not your personal one). Paystack and the card companies want a way for customers to reach you."
    if not EMAIL_RX.match(mail):
        return "bad", "SUPPORT_EMAIL on Render does not look like an email address."
    if mail.lower() in {str(o).strip().lower() for o in owner_emails}:
        return "warn", "SUPPORT_EMAIL is the same as your owner sign-in email, so everyone can see the address you sign in with. Make a separate one for support."
    return "ok", ""


def where(b):
    return ", ".join(x for x in (b.get("place"), b.get("country")) if x)


def mail_link(b, fallback="our support email (shown at the bottom of every page)"):
    m = b.get("email", "")
    return f'<a href="mailto:{E(m, quote=True)}">{E(m)}</a>' if m and EMAIL_RX.match(m) else (E(m) if m else fallback)


def phone_link(b):
    p = b.get("phone", "")
    digits = re.sub(r"[^\d+]", "", p)
    return f'<a href="tel:{E(digits, quote=True)}">{E(p)}</a>' if p and len(digits) >= 6 else E(p)


def contact_block(b):
    rows = [f"<strong>{E(b['name'])}</strong>", E(where(b))]
    if b.get("address"):
        rows.append(E(b["address"]))
    if b.get("email"):
        rows.append("Email: " + mail_link(b))
    if b.get("phone"):
        rows.append("Phone: " + phone_link(b))
    if b.get("reg"):
        rows.append("Registration number: " + E(b["reg"]))
    return '<address class="lg-contact">' + "<br>".join(rows) + "</address>"


# ───────────────────────── small writing helpers ─────────────────────────
def P(*parts):
    return "<p>" + "".join(parts) + "</p>"


def UL(items, cls=""):
    return (f'<ul class="{cls}">' if cls else "<ul>") + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def OL(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def L(slug, text=None):
    path, title = next((p[1], p[2]) for p in PAGES if p[0] == slug)
    return f'<a href="{path}">{E(text or title)}</a>'


def days(n, word="business day"):
    return f"{n} {word}{'' if n == 1 else 's'}"


def _ctx(c):
    c = dict(c or {})
    c.setdefault("price", "₦4,000")
    c.setdefault("courses", [])
    c.setdefault("free", "the first two lessons of AI Prompt Engineering")
    return c


def _reply_line():
    return f"We answer within {days(REPLY_DAYS)} (Monday to Friday, Lagos time, not counting public holidays)."


# ───────────────────────── Terms of Service ─────────────────────────
def terms(b, c):
    price, mail = E(c["price"]), mail_link(b)
    titles = [E(t) for t in c["courses"]]
    summary = (f"You are buying lifetime access to an online course for a one-time price of <b>{price}</b> (Nigerian naira). "
               f"There is <b>no subscription</b> and nothing renews by itself. Payment is handled by {PAYSTACK}, and we never see your card details. "
               f"If anything goes wrong, write to {mail}. Your money-back rights are in the {L('refund-policy')}.")
    s = []
    s.append(("about", "About these Terms", P(
        f"{E(b['name'])} (“we”, “us”, “our”) runs this website and installable app, where people learn technology skills through online courses. "
        f"On some phones the app is shown as “Air Academy”. We are based in {E(where(b))}.") + P(
        f"By creating an account, paying for a course or otherwise using the service, you agree to these Terms, our {L('privacy-policy')}, our {L('refund-policy')} "
        f"and our {L('delivery-policy')}. If you do not agree, please do not use the service.")))
    s.append(("who", "Who can use the service", UL([
        "You must be 18 or older, <b>or</b> have a parent or legal guardian who agrees to these Terms for you and allows you to use the service. A parent or guardian who allows or pays for a child’s account is responsible for how that account is used.",
        "Give true details when you sign up. Your full name is printed on your certificate, so use your real name.",
        "An account is for one person. Keep your password private, and tell us quickly if you think someone else is using your account."])))
    what = [P("Each course is a <b>digital product</b>. When you buy a course you get, for that course:"), UL([
        "self-paced online lessons you can read and practise in the app;",
        "quizzes that count towards your continuous assessment (CA) record;",
        "a project brief for the course (Project Studio);",
        "AI helpers: a lesson mentor and practice playgrounds (see “AI features” below);",
        "a final exam and, when you pass, a certificate."])]
    if titles:
        what.append(P("Courses currently on offer:") + UL(titles, "cols"))
    if c["free"]:
        what.append(P(f"<b>Free preview:</b> {E(c['free'])} can be read without paying."))
    what.append(P("Nothing is posted to you; there are no physical goods. Courses are self-paced, and we do not promise a job, a grade or any particular result. What you get out of a course depends on your own effort. We improve and update course content from time to time."))
    s.append(("what", "What you are buying", "".join(what)))
    s.append(("price", "Prices and payment", (
        '<div class="lg-tablewrap"><table><caption class="sr">Course price</caption><thead><tr><th scope="col">Item</th><th scope="col">Price</th></tr></thead><tbody>'
        f'<tr><td>One course: lifetime access, paid once</td><td><b>{price}</b> (NGN)</td></tr></tbody></table></div>')
        + UL([
        "Prices are in <b>Nigerian naira (NGN, ₦)</b>. The price is for one course and is paid once.",
        "<b>No subscription, no monthly fee, no automatic renewal.</b> Because nothing renews, there is nothing to cancel later.",
        "The price you see before you pay is the price you pay. We add no hidden fees. If you pay from an account or card in another currency, your bank may convert the naira amount and may charge its own fees. We cannot see or control those.",
        f"Payments are processed by <b>{PAYSTACK}</b> (“Paystack”), a Nigerian payment company. You type your card or bank details on Paystack’s secure page, not on ours. <b>We never see, receive or store your full card number, expiry date, CVV or PIN.</b> Paystack tells us only whether the payment worked, with the amount, a reference and your email address. Paystack’s own terms and privacy notice apply to the payment itself.",
        "We may change the price of a course for future purchases. A price change never affects a course you have already paid for."])))
    s.append(("access", "Your access, and what “lifetime” means", UL([
        f"When a payment succeeds the course opens in your account (see the {L('delivery-policy')}).",
        "“Lifetime access” means access with no time limit and no extra fee, for as long as we offer that course and your account follows these Terms.",
        f"If we ever permanently stop offering a course you have paid for, we will email you at least {NOTICE_DAYS} days before, so you can finish it, and we will agree a fair fix with you, such as an equivalent course or a refund.",
        "Access is personal. You may not share it, sell it or let other people use your account."])))
    s.append(("refunds", "Refunds and delivery", P(
        f"Our {L('refund-policy')} and {L('delivery-policy')} are part of these Terms. In short: your course opens right after payment; if a payment problem is our fault you get your money back; "
        f"and for a change of mind you have {REFUND_DAYS} days, as long as you have not taken the final exam or received a certificate for that course.")))
    s.append(("support", "Customer support and disputes", P(
        f"<b>We are responsible for supporting you.</b> {E(b['name'])} is the seller of the courses. We are responsible for customer support, for fixing access problems, and for refunds and payment disputes about your purchase. "
        "Paystack only processes the payment. It does not provide or support the courses.") + P(f"Contact us at {mail}"
        + (f" or {phone_link(b)}" if b.get("phone") else "") + f". {_reply_line()}") + P("If you have a problem:") + OL([
        "Write to us with your account email, the course, the date and amount, and what went wrong.",
        f"We will answer within {days(REPLY_DAYS)} and aim to settle the matter within {RESOLVE_DAYS} days.",
        "If you are still not happy, you may take the matter to your bank or card issuer, to Paystack, or to the Federal Competition and Consumer Protection Commission (FCCPC). For a data-protection complaint, see the " + L("privacy-policy") + "."]) + P(
        "Please talk to us before you ask your bank for a chargeback, because most problems are solved faster that way. This does not take away your right to dispute a payment with your bank.")))
    s.append(("rules", "Acceptable use", P("Please do not:") + UL([
        "share your account, or sell, copy, record or republish course content;",
        "use bots, scripts or tricks to cheat quizzes or exams, or to get around the free-lesson and payment rules;",
        "attack, overload or try to break into the service or other people’s accounts;",
        "use the AI helpers to produce harmful, illegal or abusive material, or to harass anyone;",
        "put someone else’s email address in your account or in a parent-update request without their permission."]) + P(
        "If you break these rules we may warn you, limit your access or close your account. A closed account for serious misuse is not refundable.")))
    s.append(("ip", "Our content and your work", P(
        "The lessons, quizzes, projects, designs, pictures and software of this service belong to us or to the people who license them to us. "
        "You may use them for your own learning. You keep ownership of the work you create (for example project submissions and assignments). "
        "You allow us to store, process and display that work as needed to run the service for you, such as marking it and showing it to your teacher if you are in a class group.")))
    s.append(("ai", "AI features", P(
        "Some features use artificial intelligence (the lesson mentor, the practice playgrounds, picture and voice tools, and the marking of practice assignments). AI can be wrong or out of date. "
        "Treat its answers as study help, check important facts, and do not rely on it for legal, medical, financial or safety decisions. "
        "Do not type passwords, card numbers or other sensitive personal details into any AI box. What you type or say to an AI feature is sent to our AI provider to produce the answer (see the "
        + L("privacy-policy") + "). Daily limits apply so the service stays fair and affordable. If you think an AI mark is unfair, email us and a person will look at it.")))
    s.append(("certs", "Certificates and CA records", P(
        "A certificate is issued when you complete the course requirements and pass the final exam. It shows your full name, the course, the date and your score, and carries a certificate number. "
        "Anyone who has the certificate link or number can open a public page that confirms it is genuine and shows those details. Share it only if you are happy for that to be seen. "
        "A certificate shows what you completed on this service; it is not an official academic degree or a government licence.")))
    s.append(("groups", "Class groups and teachers", P(
        "A teacher can create a class group and invite students with a link. Teachers can see the names, email addresses and course progress of students in their group. "
        "In some groups the teacher must approve each new course before a student can pay for it. The student still pays for each course and the same " + L("refund-policy") + " applies. Teachers are not our employees unless we say so, and we are not responsible for what a teacher says outside the service.")))
    s.append(("world", "Using the service from other countries", P(
        "The service is open to people in any country, subject to Nigerian law and to any laws or sanctions that apply to you or to us. You are responsible for following the laws where you live, including any local taxes. "
        "We do not sell to anyone who is not allowed to receive our services under applicable sanctions. Payments from outside Nigeria depend on your bank allowing international online payments and on Paystack accepting the card; "
        "prices stay in naira.")))
    s.append(("liability", "Availability and our responsibility", P(
        "We work to keep the service available and accurate, but we cannot promise it will never be interrupted or error-free. We may change or pause parts of it, for example for maintenance. "
        "Nothing in these Terms removes any right you have under Nigerian consumer-protection law, including the Federal Competition and Consumer Protection Act 2018, or excludes liability that the law does not allow us to exclude "
        "(for example for fraud, or for death or personal injury caused by negligence). Subject to that, our total responsibility for any claim about a course is limited to the price you paid for that course, and we are not liable for indirect losses such as lost profit or lost opportunity.")))
    s.append(("end", "Ending your account", P(
        f"You can stop using the service at any time and can ask us to close your account and delete your data by writing to us (see the {L('privacy-policy')}). "
        "We may suspend or close an account that breaks these Terms. When an account is closed, the access that came with it ends, except where the law or our " + L("refund-policy") + " says otherwise.")))
    s.append(("changes", "Changes to these Terms", P(
        f"We may update these Terms. The “last updated” date at the top shows when. If a change is important we will tell you in the app or by email before it starts. "
        "If you keep using the service after a change starts, you accept the new Terms. A change never reduces what you have already paid for.")))
    s.append(("law", "Governing law", P(
        "These Terms are governed by the laws of the Federal Republic of Nigeria. We hope to settle any disagreement by talking first. If that fails, the courts of Nigeria can decide it, "
        "without limiting any right you have to go to a consumer or data-protection authority.")))
    s.append(("contact", "Contact us", contact_block(b) + P(_reply_line())))
    return summary, s


# ───────────────────────── Refund Policy ─────────────────────────
def refunds(b, c):
    price, mail = E(c["price"]), mail_link(b)
    summary = (f"If a payment problem is our fault, you get your money back. For a change of mind you have <b>{REFUND_DAYS} days</b> from payment, as long as you have not taken the final exam "
               f"or received a certificate for that course. Email {mail} and we reply within {days(REPLY_DAYS)}. Courses are {price} each, paid once, with no subscription.")
    s = []
    s.append(("eligible", "When we give a refund", UL([
        f"<b>The course did not open.</b> You paid, and we could not open the course within {days(FIX_DAYS)} of you telling us. Full refund.",
        f"<b>Double payment.</b> You were charged more than once for the same course. We refund the extra payment. Please tell us within {REPORT_DAYS} days.",
        f"<b>Wrong amount.</b> You were charged a different amount from the price shown when you paid. We refund the difference. Please tell us within {REPORT_DAYS} days.",
        f"<b>Change of mind.</b> You ask within <b>{REFUND_DAYS} days</b> of paying, and you have not taken the final exam or received a certificate for that course. Full refund.",
        "<b>Not as described.</b> The course is clearly different from how we described it, or a serious fault that we cannot fix stops you from using it."])))
    s.append(("not", "When we do not give a refund", UL([
        f"The request comes after {REFUND_DAYS} days and is only a change of mind.",
        "You have already taken the final exam or received a certificate for the course (unless the problem was our fault).",
        "Your account was closed for breaking the Terms, for example sharing the account or copying course content.",
        "The difference is only your bank’s fees or exchange rate. We cannot control those."])))
    s.append(("how", "How to ask for a refund", P(f"Send an email to {mail}" + (f" (or call {phone_link(b)})" if b.get("phone") else "") + ' with the subject “Refund request” and tell us:') + UL([
        "the email address you use for your account;",
        "which course, the date and the amount;",
        "the payment reference, if you have it (it starts with OATS- and is on your Paystack receipt);",
        "a short reason."]) + P("<b>Never send us your card number, PIN, CVV or password.</b> We will never ask for them.")))
    s.append(("time", "How long it takes", OL([
        f"We reply within {days(REPLY_DAYS)}.",
        f"If the refund is approved, we start it within {days(REFUND_START_DAYS)} through Paystack and email you when we do.",
        "Your bank or card company then takes time to show the money. This is usually <b>5 to 10 business days</b>, and sometimes longer, depending on your bank."])))
    s.append(("where", "Where the money goes", UL([
        "Back to the same card or bank account you paid with, through Paystack. We cannot pay a refund in cash or to a different person’s account.",
        f"You get back the same naira amount you paid ({price} for a course). If you paid with a card in another currency, your bank’s exchange rate may make the amount look a little different on your statement. We cannot control that."])))
    s.append(("access", "What happens to your access", P(
        "When a refund is approved, your access to that course ends. Free lessons stay free, and your other courses are not affected.")))
    s.append(("failed", "Money taken but no course, or a failed payment", P(
        "If Paystack or your bank says a payment failed, banks normally return the money to you automatically. This can take a few business days. "
        f"If it has not come back after 5 business days, please ask your bank, and write to us if you want us to check our records. If a payment <i>succeeded</i> but the course did not open, see the {L('delivery-policy')}.")))
    s.append(("nosub", "Cancelling", P(
        "There is no subscription and nothing renews by itself, so there is nothing to cancel. You pay once for each course. You may stop using the service, or ask us to close your account, at any time.")))
    s.append(("disputes", "Disputes and chargebacks", P(
        f"We are responsible for refunds and payment disputes about your purchase (see the {L('terms')}). Please write to us first. We settle most problems within {RESOLVE_DAYS} days. "
        "You may still raise a dispute with your bank or card issuer at any time.")))
    s.append(("contact", "Contact us", contact_block(b) + P(_reply_line())))
    return summary, s


# ───────────────────────── Delivery Policy ─────────────────────────
def delivery(b, c):
    price, mail = E(c["price"]), mail_link(b)
    summary = ("Courses are digital. After a successful payment your course opens in your account straight away, usually within a few seconds (a bank transfer can take a few minutes). "
               "Nothing is posted, so there is no delivery fee and no parcel to wait for.")
    s = []
    s.append(("what", "What you receive", P(
        "Access to the course you paid for, inside your account on this website and app: all of its lessons, quizzes, the project brief, the AI helpers for that course, the final exam and the certificate. "
        "The lessons are used online; they are not sent as downloads or by post.")))
    s.append(("when", "When it opens", UL([
        f"Card payments: almost at once. When Paystack confirms the payment you are brought back to the app and the course opens by itself ({price} per course).",
        "Bank transfer or USSD: this can take a few minutes while your bank confirms the money. The app keeps checking for you.",
        f"If you closed the page after paying, nothing is lost. Paystack tells our server directly. Sign in with the same email and your course will be open.",
        "The free lessons need no payment and open at once."])))
    s.append(("how", "How you get to it", OL([
        "Choose a course and tap Unlock.",
        "Pay on Paystack’s secure page.",
        "You return to the app and the course opens. If you are not returned automatically, open the app, sign in with the same email you paid with, and open your courses."])))
    s.append(("receipt", "Your receipt", P(
        "Paystack may email you a receipt for the payment to the email address you used. Keep it: it shows the payment reference (it starts with OATS-), which helps us find your payment fast if you ever need help. "
        "Your course purchase also appears in your account as an open course.")))
    s.append(("problem", "If your course has not opened", OL([
        f"Wait {LATE_MINUTES} minutes after paying (a bank can be slow), then refresh the page or close and reopen the app.",
        "Check that you are signed in with the same email address you used to pay.",
        f"Still locked? Email {mail} with your account email, the date, the amount and the payment reference if you have it. We fix it within <b>{days(FIX_DAYS)}</b>.",
        f"If we cannot open it, you get a full refund (see the {L('refund-policy')})."])))
    s.append(("groups", "Class groups", P(
        "If you joined a class group, your teacher may need to approve a course before you can pay for it, and classes may open one step at a time. "
        "Once a payment succeeds, the course you paid for opens straight away.")))
    s.append(("needs", "What you need", UL([
        "a phone, tablet or computer with an internet connection and a recent browser (the app can also be installed on your device);",
        "an email address that works, because sign-in codes and some notices are sent there. If the code does not arrive, check your spam or junk folder."])))
    s.append(("where", "Where we deliver", P(
        "Anywhere there is an internet connection. There is no shipping, no customs and no delivery charge. Foreign cards need to be allowed for international online payments by your bank, and prices stay in Nigerian naira.")))
    s.append(("contact", "Contact us", contact_block(b) + P(_reply_line())))
    return summary, s


# ───────────────────────── Privacy Policy ─────────────────────────
def privacy(b, c):
    mail = mail_link(b)
    summary = (f"We collect only what we need to run your account and your courses: your <b>name, email address, date of birth and gender</b>, and your learning activity. "
               f"When you pay, we share the data needed to process the payment with <b>{PAYSTACK}</b>. "
               "<b>We do not store your card number, expiry date, CVV or PIN.</b> We do not sell your data and we show no advertising. "
               f"You can ask to see, fix or delete your data at any time by writing to {mail}.")
    s = []
    s.append(("who", "Who we are", P(
        f"{E(b['name'])} is the “data controller” for personal data collected through this website and app: we decide why and how it is used. "
        f"This policy follows the Nigeria Data Protection Act 2023 (NDPA), the Nigeria Data Protection Regulation 2019 (NDPR) and the implementation directive issued by the Nigeria Data Protection Commission (NDPC). "
        f"We are based in {E(where(b))}. Contact for anything about your data: {mail}.")))
    rows = [
        ("Your account", "Full name, email address, date of birth, gender, and your password (kept only as a one-way scrambled hash, so nobody can read it).", "To create your account, put your name on your certificate, and keep the service suitable for your age."),
        ("Signing in", "One-time sign-in codes (kept scrambled, valid for 10 minutes) and a secure sign-in cookie.", "To prove the email is yours and keep you signed in."),
        ("Your learning", "Lessons you finish, quiz and exam scores, CA record, assignments and projects you submit, and certificates.", "To run your courses, mark your work and issue certificates."),
        ("AI chats and voice", "Messages you send to the AI helpers, short notes the mentor keeps so it can remember your goals, and daily-use counters. Voice recordings are sent for transcription and are not saved by us.", "To answer you and keep AI use fair."),
        ("Payments", f"Your email, the course, the amount, the currency, the payment status and reference, Paystack’s transaction number and the date. <b>Not</b> your card number, expiry date, CVV or PIN: you type those only on Paystack’s page.", "To confirm your payment, open your course, give refunds, and keep records the law requires."),
        ("Class groups", "Which group you joined, which courses the teacher approved, and your course progress.", "So a teacher can run a class."),
        ("Parent or teacher updates", "Email addresses you add for a parent, guardian or teacher, and a record of the weekly progress emails sent.", "To send progress updates you asked for."),
        ("Live activity", "A random id for your open tab, the part of the app you are in, the time you were last active, and (if signed in) your name and account id. We also keep the dates on which you used the app.", "So the owner can see how many people are online now, and how many students are active each day or month, and keep the service running."),
        ("Technical", "Your IP address and browser type in our host’s server logs, and the request your browser makes to Google Fonts to show text.", "Security, preventing abuse and keeping the service working."),
        ("When you contact us", "Your name, email address, phone number (if you call or message us) and what you tell us.", "To help you and keep a record of what we agreed."),
    ]
    table = ('<div class="lg-tablewrap"><table><caption class="sr">Data we collect</caption><thead><tr><th scope="col">What</th><th scope="col">Details</th><th scope="col">Why</th></tr></thead><tbody>'
             + "".join(f'<tr><th scope="row">{E(a)}</th><td>{d}</td><td>{w}</td></tr>' for a, d, w in rows) + "</tbody></table></div>")
    s.append(("collect", "What we collect and why", table + P(
        "<b>Phone number.</b> We do not ask for your phone number when you sign up. If you contact us by phone, we keep the number you called from. Paystack may ask for a phone number or other details on its own payment page; those are collected by Paystack under its own privacy notice.")))
    s.append(("paystack", "Payments and Paystack", P(
        f"When you pay, we share the data needed to process the payment with <b>{PAYSTACK}</b>: your email address, the amount and currency, a payment reference and the address we want you returned to. "
        "You then enter your card or bank details on Paystack’s secure page. <b>Those details go to Paystack only. We never see them and we do not store them.</b> "
        "Paystack sends us back the result: whether the payment worked, the amount, the reference and your email. Paystack is responsible for the card data it collects and has its own privacy notice and security controls.")))
    s.append(("basis", "Why we may use your data (legal reasons)", UL([
        "<b>To provide the service you asked for</b> (a contract): your account, courses, payments, exams, certificates and support.",
        "<b>Our legitimate interests</b>: keeping the service secure, stopping fraud and abuse, counting live users, controlling costs, and improving the courses. We balance this against your rights.",
        "<b>The law</b>: keeping payment and tax records and answering lawful requests.",
        "<b>Your consent</b>: for example when you add a parent’s email, or when a parent or guardian agrees for a child. You can withdraw consent at any time."])))
    s.append(("share", "Who we share data with", P("We do not sell your data and we do not use it for advertising. We share it only with:") + UL([
        f"<b>{PAYSTACK}</b>: to process payments.",
        "<b>Supabase</b>: stores our database.",
        "<b>Render</b>: hosts the website and app.",
        "<b>Resend</b>: sends emails (sign-in codes, parent and teacher updates, notices).",
        "<b>OpenAI</b>: powers the AI helpers, voice and picture tools. What you type or say to them is sent to OpenAI to produce the answer.",
        "<b>Google Fonts</b>: your browser asks Google for the text fonts, which shows your IP address to Google.",
        "<b>Your teacher</b>, if you join a class group: your name, email and progress in that group.",
        "<b>Parents or guardians you add</b>: your weekly progress.",
        "<b>The public</b>, only for certificates: the certificate page shows your name, course, date and score to anyone with the link or number.",
        "<b>Authorities</b>, when the law requires it."]) + P("These companies act on our instructions to provide their service, and each has its own privacy terms.")))
    s.append(("abroad", "Sending data outside Nigeria", P(
        "Some of the companies above (for example our database, hosting, email and AI providers) store or process data in other countries. "
        "When we send personal data abroad we do it only where the NDPA allows it: to providers that protect it to a suitable standard, under their contracts with us, or where it is needed to give you the service you asked for.")))
    s.append(("keep", "How long we keep data", UL([
        "<b>Account and learning data:</b> for as long as your account exists. When you ask us to delete your account we delete or anonymise it within " + f"{PRIVACY_DAYS} days.",
        "<b>Payment records:</b> for as long as Nigerian tax and accounting rules require (generally up to six years), even if the account is deleted.",
        "<b>Sign-in details you typed but never confirmed with the email code:</b> deleted within 24 hours.",
        "<b>Sign-in codes:</b> valid 10 minutes, then cleared.",
        "<b>Live-activity records:</b> the who-is-online records are deleted within about an hour. The dates you were active are kept while your account exists.",
        "<b>Records of AI and email use</b> (kept to control costs) are deleted after about 100 days.",
        "<b>Certificates:</b> a certificate stays verifiable for as long as it exists. Ask us if you want yours removed."])))
    s.append(("security", "How we protect your data", UL([
        "Everything travels over HTTPS (an encrypted connection).",
        "Passwords and sign-in codes are stored scrambled, never in plain text.",
        "Card details never reach our servers, because you enter them on Paystack’s page.",
        "Payments are checked with Paystack on our server before a course opens, so they cannot be faked from a browser.",
        "Owner and admin areas are locked to the right accounts, and access to our systems is limited to what is needed."]) + P(
        "No system is perfectly safe. If a breach puts your rights at risk, we will tell the NDPC and the people affected within the time the law requires.")))
    s.append(("cookies", "Cookies and storage on your device", P(
        "We use <b>one essential cookie</b>: the secure sign-in cookie that keeps you signed in. We use no advertising or tracking cookies. "
        "Your browser’s own storage keeps small things to make the app work: a random id for the open tab, your private lesson notes (these stay on your device), your last lesson, your voice settings, a high score, the welcome-video flag, and install prompts. "
        "Paystack’s page may set its own cookies. You can clear this storage in your browser at any time.")))
    s.append(("children", "Children", P(
        "Children can learn here, but the law says a parent or legal guardian must agree to the use of a child’s personal data. <b>If you are under 18, you may use this service only with your parent’s or guardian’s permission,</b> "
        "and a parent or guardian is welcome to ask us what we hold about the child, or to ask us to delete it, at any time. We use children’s data only to run their account and courses. We never use it for advertising.")))
    s.append(("rights", "Your rights", P("Under the NDPA you can ask us to:") + UL([
        "tell you what personal data we hold about you and give you a copy;",
        "correct data that is wrong or out of date;",
        "delete your data, or restrict how we use it, where the law allows;",
        "stop using your data for a purpose you object to, and withdraw any consent you gave;",
        "give your data to you in a format you can reuse (data portability);",
        "review an automated mark, such as an AI-marked assignment, with a person."]) + P(
        f"To use any right, email {mail} from the email address on your account. We may ask you to confirm who you are. We answer within {PRIVACY_DAYS} days. "
        "There is no self-service delete button yet, so deletion is done by request.")))
    s.append(("complain", "Complaints", P(
        f"Please tell us first at {mail}, and we will try to put it right. You also have the right to complain to the <b>Nigeria Data Protection Commission (NDPC)</b> "
        "at <a href=\"https://ndpc.gov.ng\" target=\"_blank\" rel=\"noopener\">ndpc.gov.ng</a>.")))
    s.append(("changes", "Changes to this policy", P(
        "We may update this policy. The “last updated” date at the top shows when. If a change matters to your rights we will tell you in the app or by email.")))
    s.append(("contact", "Contact us", contact_block(b) + P(_reply_line())))
    return summary, s


BUILDERS = {"terms": terms, "refund-policy": refunds, "delivery-policy": delivery, "privacy-policy": privacy}
LEAD = {
    "terms": "Please read these Terms before you create an account or pay for a course.",
    "refund-policy": "A plain explanation of when we refund, how to ask, and how long it takes.",
    "delivery-policy": "How and when your course reaches you after you pay.",
    "privacy-policy": "What we collect, why we collect it, who we share it with, and the rights you have.",
}


# ───────────────────────── the footer and the page ─────────────────────────
LOGO = ('<svg class="lg-logo" viewBox="0 0 32 32" width="26" height="26" aria-hidden="true" focusable="false">'
        '<path d="M16 2l12 7v14l-12 7L4 23V9z" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<path d="M9.5 21a6.5 6.5 0 0 1 13 0M7 21h18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>')


def footer_html(b, c=None, current=None):
    """The site-wide footer: business name, where we are, how to reach us, links to every policy. Rendered on the server so
    a reviewer (or a crawler that does not run scripts) sees it on every page, including the home page."""
    c = _ctx(c)
    price = E(c["price"])
    contact = [f"<span><b>{E(b['name'])}</b></span>", f"<span>Based in {E(where(b))}</span>"]
    if b.get("address"):
        contact.append(f"<span>{E(b['address'])}</span>")
    if b.get("email"):
        contact.append(f"<span>Email: {mail_link(b)}</span>")
    if b.get("phone"):
        contact.append(f"<span>Phone: {phone_link(b)}</span>")
    if b.get("reg"):
        contact.append(f"<span>Reg. no. {E(b['reg'])}</span>")
    links = "".join(f'<a href="{p}"{" aria-current=page" if current == s else ""}>{E(t)}</a>' for s, p, t, _ in PAGES)
    year = datetime.now(timezone.utc).year
    return (
        '<footer class="sf" id="site-footer" aria-labelledby="sf-h"><div class="sf-in">'
        f'<div class="sf-col sf-about"><h2 id="sf-h" class="sf-title">{E(b["name"])}</h2>'
        f'<p>Online tech courses: web, apps, cloud, AI, game development and animation. <b>{price} per course</b>, paid once, lifetime access, no subscription. '
        f'Prices are in Nigerian naira (₦).</p>'
        f'<p class="sf-pay"><span aria-hidden="true">🔒</span> Payments are processed securely by {PAYSTACK}. We never see or store your card details.</p></div>'
        f'<address class="sf-col sf-contact"><h3 class="sf-sub">Contact us</h3>{"".join(contact)}</address>'
        f'<nav class="sf-col sf-links" aria-label="Legal and policies"><h3 class="sf-sub">Policies</h3>{links}</nav>'
        f'</div><p class="sf-copy">© {year} {E(b["name"])}. All rights reserved.</p></footer>')


def mini_links():
    """The one-line version for the sign-in page, so the policies are visible without scrolling."""
    return '<p class="legal-mini">' + " · ".join(f'<a href="{p}">{E(t.replace(" of Service", "").replace(" Policy", ""))}</a>' for _, p, t, _ in PAGES) + "</p>"


def page_html(slug, b, c=None, base=""):
    c = _ctx(c)
    _, path, title, desc = next(p for p in PAGES if p[0] == slug)
    summary, sections = BUILDERS[slug](b, c)
    toc = "".join(f'<li><a href="#{i}">{E(t)}</a></li>' for i, t, _ in sections)
    body = "".join(f'<section id="{i}" aria-labelledby="{i}-h"><h2 id="{i}-h">{E(t)}</h2>{h}</section>' for i, t, h in sections)
    nav = "".join(f'<a href="{p}"{" aria-current=page" if s == slug else ""}>{E(t)}</a>' for s, p, t, _ in PAGES)
    canon = f'<link rel="canonical" href="{E(base.rstrip("/") + path, quote=True)}">' if base else ""
    name = E(b["name"])
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
        '<meta name="theme-color" content="#0D0E15">'
        f'<title>{E(title)} | {name}</title><meta name="description" content="{E(desc, quote=True)}">'
        f'<meta name="robots" content="index, follow">{canon}'
        '<link rel="icon" href="/static/icons/icon-192.png"><link rel="apple-touch-icon" href="/static/icons/apple-touch-icon.png">'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&family=Sora:wght@400;600&display=swap" rel="stylesheet">'
        '<link rel="stylesheet" href="/static/style.css"><link rel="stylesheet" href="/static/legal.css"></head>'
        '<body class="lg-body"><a class="skip" href="#main">Skip to main content</a><div class="bg" aria-hidden="true"></div>'
        f'<header class="lg-head"><div class="lg-head-in"><a class="lg-brand" href="/" aria-label="{name}, home">{LOGO}<span>{name}</span></a>'
        '<a class="lg-back" href="/">Back to the app</a></div>'
        f'<nav class="lg-nav" aria-label="Legal pages">{nav}</nav></header>'
        f'<main id="main" class="lg"><article class="glass lg-card"><h1>{E(title)}</h1>'
        f'<p class="lg-updated">Last updated: <time>{E(UPDATED)}</time></p><p class="lg-lead">{E(LEAD[slug])}</p>'
        f'<div class="lg-summary" role="note"><strong>In short</strong><p>{summary}</p></div>'
        f'<nav class="lg-toc" aria-label="On this page"><strong>On this page</strong><ol>{toc}</ol></nav>'
        f'{body}</article></main>{footer_html(b, c, slug)}</body></html>')
