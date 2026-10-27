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
- `FREE_ACCESS_EMAILS`: optional, comma-separated full email addresses that get every course free (enrolled automatically at sign-in, including courses added later).
- `OPENAI_API_KEY`: powers the project generator and the picture maker on lesson pages. `OPENAI_MODEL` (default `gpt-4o-mini`) is used to check that a picture prompt is connected to the lesson.
- Picture maker (all optional): `OPENAI_IMAGE_MODEL` (default `gpt-image-2`), `IMAGE_QUALITY` (`low`, `medium` or `high`, default `medium`; this is the main cost setting), `LESSON_IMAGE_LIMIT` (pictures per student per lesson page, default 3), `IMAGE_BLOCK_MINUTES` (pause after an off-topic prompt, default 30), `IMAGE_MAX_PARALLEL` (pictures being made at once across all students, default 4).
  To lift a block early, delete that student's row from the `image_blocks` table in Supabase.
- `FLW_WEBHOOK_HASH`: any random string; put the same value as "Secret hash" in Flutterwave > Settings > Webhooks, with URL `https://YOUR-DOMAIN/api/flutterwave/webhook`. Optional locally.

## Test a payment
Sign in, open a locked course, tap **Unlock**, and use a Flutterwave test card from their docs (test keys only). The blur lifts without a reload.

## Deploy
`gunicorn app:app` (Linux) or `waitress-serve app:app` (Windows). Set `APP_ENV=production`, a real `SECRET_KEY`, SMTP, and serve over HTTPS. SQLite needs a persistent disk/volume for `DATABASE_PATH`.

## Files
- `app.py`: API, OTP auth, payment init/verify/webhook, SQLite schema
- `courses_seed.py`: courses and lesson titles (edit freely; lessons are only sent to buyers)
- `static/index.html`, `style.css`, `app.js`: the whole UI
