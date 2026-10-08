# Open Air Tech Space (HTML + Python)

Flask backend + plain HTML/CSS/JS frontend. Accounts with full name, date of birth, gender and password (email verified with a 6-digit code), 8 tracks, 3,500 NGN per course through Flutterwave. Full lesson pages with diagrams, quizzes, a CA record, final exams, verifiable certificates and a project studio.

## Run it (PowerShell)

```powershell
cd air_academy_web
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # if blocked: Set-ExecutionPolicy -Scope Process Bypass
pip install -r requirements.txt
copy .env.example .env                # then edit .env (see below)
python app.py
```
Open http://127.0.0.1:5000

## .env
- `SECRET_KEY`: any long random string (`python -c "import secrets;print(secrets.token_hex(32))"`).
- `FLW_PUBLIC_KEY` / `FLW_SECRET_KEY`: Flutterwave dashboard > Settings > API keys. Use the TEST keys first.
- Sign-in emails: **Mailjet first, Resend as backup**. If Mailjet errors or doesn't answer within 10 seconds, the same code is sent through Resend automatically.
  - Mailjet (SMTP): `SMTP_HOST=in-v3.mailjet.com`, `SMTP_PORT=587`, `SMTP_USER=<API key>`, `SMTP_PASS=<secret key>`, `SMTP_FROM=<sender verified in Mailjet>`
  - Resend: `RESEND_API_KEY=re_...`, `RESEND_FROM=Open Air Tech Space <no-reply@yourdomain.com>` (domain must be verified in Resend)
  - Optional: `EMAIL_ORDER=smtp,resend` (default). Use `resend,smtp` to flip the order.
  - Leave both unset in development and the 6-digit code prints in the terminal instead.
- `SQLITE_WAL`: leave unset normally. Set `SQLITE_WAL=0` on PythonAnywhere, which is safer for SQLite on their file system.
- `PUBLIC_URL`: your site address (for example `https://openairtech.space`). It is printed on certificates as the verification link.
- `OPENAI_API_KEY` (optional): lets the Project Studio tailor each project with AI. `OPENAI_MODEL` (optional) picks the model. Without a key it uses the built-in project templates.
- `FLW_WEBHOOK_HASH`: any random string; put the same value as "Secret hash" in Flutterwave > Settings > Webhooks, with URL `https://YOUR-DOMAIN/api/flutterwave/webhook`. Optional locally.

## How marks work
CA (continuous assessment) is the average of a student's best lesson-quiz scores and counts for 40%. The final exam (up to 10 questions drawn from the lesson quizzes) counts for 60%. Pass mark is 50%. Passing unlocks the certificate, which has a unique ID and a public check page at `/verify/<ID>`. Change the weights in `W_CA`, `W_EXAM` and `PASS_MARK` in `app.py`.

## Free hosting: PythonAnywhere + Gmail (no money, no domain)
1. Create a free Beginner account. Your username becomes your address, `https://USERNAME.pythonanywhere.com`.
2. Open a Bash console and run: `git clone <your GitHub repo> open-air`, then `cd open-air && pip install --user -r requirements.txt`.
3. In the project folder create a `.env` file from `.env.example` (see the values in that file). `DATABASE_PATH` must be the full path, for example `/home/USERNAME/open-air/academy.db`.
4. Web tab > Add a new web app > Manual configuration > pick Python 3.12. Set the source code folder to `/home/USERNAME/open-air`.
5. Open the WSGI configuration file from the Web tab, replace its contents with the three lines below, save, then press Reload:
```python
import sys
sys.path.insert(0, "/home/USERNAME/open-air")
from app import app as application
```
6. In Flutterwave, set the webhook URL to `https://USERNAME.pythonanywhere.com/api/flutterwave/webhook`.
7. Free web apps expire. Log in and press the extend button on the Web tab before it runs out.
8. Back up by downloading `academy.db` from the Files tab now and then.

## Existing users
Accounts made before passwords existed keep their courses. They choose Create account with the same email, finish the email code, and the profile and password are added to the same account.

## Test a payment
Sign in, open a locked course, tap **Unlock**, and use a Flutterwave test card from their docs (test keys only). The blur lifts without a reload.

## Deploy
`gunicorn app:app` (Linux) or `waitress-serve app:app` (Windows). Set `APP_ENV=production`, a real `SECRET_KEY`, SMTP, and serve over HTTPS. SQLite needs a persistent disk/volume for `DATABASE_PATH`.

## Files
- `app.py`: API, OTP auth, payment init/verify/webhook, SQLite schema
- `course_content.py`: full lesson pages (text, diagram, key terms, mistakes, quiz) and the Project Studio templates. **Add a lesson here and it appears in the app automatically.** Quiz answers never leave the server before grading.
- `lessons_prompt_engineering.py`: lessons 3 to 8 of AI Prompt Engineering (lessons 1 and 2 are in `course_content.py`). Write each new course the same way, in its own file, then add two lines at the bottom of `course_content.py` to load it.
- `diagrams.py`: small helpers that draw the lesson diagrams (flow boxes, format cards)
- `static/learn.js`: sign-in and sign-up, lesson reader, quizzes, CA record, exam, certificate and project studio screens
- `courses_seed.py`: courses, lesson titles and lesson notes (`NOTES`). Edit freely; lessons and notes are only sent to buyers. `teachers.html` has its own copy of the same notes, so update both when you change them.
- `static/index.html`, `style.css`, `app.js`: the whole UI
- `teachers.html`: standalone teachers' page (not served by the app, no login, no paywall). Open it directly in a browser.
