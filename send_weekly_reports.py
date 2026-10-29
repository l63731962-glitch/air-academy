"""Send last week's progress emails to confirmed parents, and a class summary to each class owner.

Run it once a week, early on Monday (Lagos time). On Render you can make a Cron Job that runs:   python send_weekly_reports.py
It needs the same environment variables as the web service (DATABASE_URL, RESEND_API_KEY, RESEND_FROM) plus PUBLIC_URL, so the
"stop these emails" links point at your site. It is safe to run twice: an email is never sent twice for the same week.
"""
import os
import sys

if not os.getenv("PUBLIC_URL"):
    sys.exit("Set PUBLIC_URL (for example https://air-academy.onrender.com) so the links in the emails work.")

import app   # noqa: E402  importing it connects to DATABASE_URL

with app.app.app_context():
    print(app.send_weekly_reports())