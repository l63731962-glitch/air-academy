# Air Academy (HTML + Python)

Flask backend + plain HTML/CSS/JS frontend. Passwordless sign-in (6-digit email code), 8 tracks, 3,500 NGN per course through Flutterwave.

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
- `SMTP_*`: your email provider. Leave `SMTP_HOST` empty in development and the 6-digit code prints in the terminal instead.
- `FLW_WEBHOOK_HASH`: any random string; put the same value as "Secret hash" in Flutterwave > Settings > Webhooks, with URL `https://YOUR-DOMAIN/api/flutterwave/webhook`. Optional locally.

## Test a payment
Sign in, open a locked course, tap **Unlock**, and use a Flutterwave test card from their docs (test keys only). The blur lifts without a reload.

## Deploy
`gunicorn app:app` (Linux) or `waitress-serve app:app` (Windows). Set `APP_ENV=production`, a real `SECRET_KEY`, SMTP, and serve over HTTPS. SQLite needs a persistent disk/volume for `DATABASE_PATH`.

## Files
- `app.py`: API, OTP auth, payment init/verify/webhook, SQLite schema
- `courses_seed.py`: courses and lesson titles (edit freely; lessons are only sent to buyers)
- `static/index.html`, `style.css`, `app.js`: the whole UI
