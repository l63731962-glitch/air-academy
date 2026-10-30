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
- `OPENAI_API_KEY`: powers every AI feature (project generator, Air Omega, picture maker). `OPENAI_MODEL` (default `gpt-4o-mini`) is the model for Air Omega's chat, practice questions, assignments and marking.
- **Making Air Omega smarter.** `OPENAI_MODEL` (default `gpt-4o-mini`) is the cheap, quick model used for safety checks, practice questions and project ideas. `OPENAI_SMART_MODEL` is the clever one used for Air Omega's chat and voice conversations, the lesson mentor, assignment writing and marking, the Prompt Lab and the Agent Lab. Leave it empty and everything uses `OPENAI_MODEL`. Set it to a stronger model from OpenAI's models page (platform.openai.com/docs/models) and all of those get smarter at once. The app already handles the newer "thinking" models, which reject the old `temperature` and `max_tokens` settings. For snappier voice answers with a thinking model, also set `OPENAI_REASONING_EFFORT=low`.
- Voice (all optional): `OPENAI_TTS_MODEL` (Air Omega's voice, default `gpt-4o-mini-tts`), `OPENAI_STT_MODEL` (turns speech into text, default `gpt-4o-transcribe`).
- Daily limits per student (all optional, they keep the cost predictable): `TALK_DAILY_LIMIT` (messages to Air Omega, default 40), `VOICE_REPLY_DAILY_LIMIT` (spoken replies, default 60), `VOICE_LISTEN_DAILY_LIMIT` (voice messages, default 60), `PLAYGROUND_AI_DAILY_LIMIT` (Prompt Lab and Agent Lab runs, default 30).
- Air Omega limits (all optional): `MENTOR_DAILY_LIMIT` (questions per student per day, default 20), `PRACTICE_DAILY_LIMIT` (weak-spot practice sets per day, default 5), `ASSIGNMENT_ATTEMPTS` (tries per assignment, default 2; the best counts), `ASSIGNMENT_WEIGHT` (how many of the 40 CA points come from assignments, default 15, the other 25 from lesson quizzes; set `0` to go back to quizzes only).
- Picture maker (all optional): `OPENAI_IMAGE_MODEL` (default `gpt-image-2`), `IMAGE_QUALITY` (`low`, `medium` or `high`, default `medium`; this is the main cost setting), `LESSON_IMAGE_LIMIT` (pictures per student per lesson page, default 3), `IMAGE_BLOCK_MINUTES` (pause after an off-topic prompt, default 30), `IMAGE_MAX_PARALLEL` (pictures being made at once across all students, default 4).
  To lift a block early, delete that student's row from the `image_blocks` table in Supabase.
- `PUBLIC_URL`: your site address, for example `https://air-academy.onrender.com`. Used for the links in parent and teacher emails.
- `CRON_SECRET`: any long random string. It protects the weekly-email trigger (see "Weekly emails" below).
- `FLW_WEBHOOK_HASH`: any random string; put the same value as "Secret hash" in Flutterwave > Settings > Webhooks, with URL `https://YOUR-DOMAIN/api/flutterwave/webhook`. Optional locally.

## Air Omega (the AI assistant)
Every AI feature speaks as **Air Omega, Open Air Tech Space AI assistant**. All of it runs on the server, a failure never uses up a student's turn, and nothing is shown until the server has checked it.
- **Ask Air Omega** on each lesson: a small chat that answers only from that lesson, with "Normal", "Like I'm 12" and "With football" styles. It never gives quiz, exam or assignment answers. English only. Daily limit per student.
- **Listen to this lesson**: the browser's own free English voice. Nothing is sent to OpenAI.
- **Practice my weak spots**: quizzes and exams record which questions were missed. Air Omega writes fresh questions on exactly those. A right answer clears that weak spot. Practice does not change the CA.
- **Assignments**: Air Omega writes one assignment per student per lesson, the student answers in the app, and Air Omega marks it against a rubric out of 20. The server adds up the points itself, so the AI can never award more than the rubric allows. The score feeds the CA record.
- **XP and weekly leaderboard**: lessons (10), quizzes (up to 20), assignments (up to 30), exams (up to 50), practice (2 per right answer, up to 30 a day). The leaderboard is inside a class group, weekly (Monday to Sunday, Lagos time) and opt-in. On the teacher page the winner of last week can be given one free track, once per group per week.
- **Parent updates**: a student adds a parent or guardian email, the parent confirms from their own inbox, and then gets a short progress email every Monday with a link to stop. The class owner gets a weekly class summary.

## Talk to Air Omega, voice and playgrounds
- **Talk to Air Omega** (button on the dashboard): an open conversation about tech, coding, homework, study skills and careers. Type, or tap the microphone and talk, and Air Omega can answer out loud. It is available to students who have unlocked at least one track.
- **Voice.** 11 Air Omega voices (OpenAI), a speed setting, and the free voices already on the student's phone or computer as a fallback. Speech is turned into words by OpenAI, so it works in Chrome, Edge, Firefox, Safari and on phones. **Conversation mode** is hands-free: Air Omega notices when you stop talking, answers, then listens again. The browser asks for the microphone, and that only works on https, which Render provides. The lesson mentor has the same microphone and speak switch.
- **Playgrounds** (button on every unlocked course): Prompt Engineering has the **Prompt Lab** (runs a real prompt, Air Omega scores it), Web Development has the **Code Studio** (live HTML, CSS and JavaScript), Animation has the **Keyframe Studio**, Cloud Computing has the **Traffic Surge Simulator**, App Development has the **Screen Builder**, Full Stack has the **API Lab** (a pretend backend in the browser), Agentic AI has the **Agent Lab** (a real agent with tools the student chooses) and Game Development has the **Game Tuner**. In every playground, Air Omega can see what the student has built and helps with it.
- Only the Prompt Lab and Agent Lab, voice and chat use OpenAI. The other six run entirely in the browser and cost nothing.

## Weekly emails
Emails go out when something calls the trigger. Two ways, pick one:
1. **Free scheduler (cron-job.org).** Create a job that sends a `POST` to `https://YOUR-DOMAIN/api/internal/weekly-reports` every Monday morning, with the header `X-Cron-Secret: <your CRON_SECRET>`. It answers at once and sends the emails in the background.
2. **Render Cron Job.** Create a Cron Job service from the same repo with command `python send_weekly_reports.py`, schedule `0 6 * * 1` (that is 07:00 in Lagos on Mondays, as Render uses UTC) and the same environment variables as the web service.

Running it twice is safe: an email is never sent twice for the same week. It needs `RESEND_API_KEY` and `RESEND_FROM` (already used for sign-in codes) and `PUBLIC_URL`.

## Test a payment
Sign in, open a locked course, tap **Unlock**, and use a Flutterwave test card from their docs (test keys only). The blur lifts without a reload.

## Deploy
`gunicorn app:app` (Linux) or `waitress-serve app:app` (Windows). Set `APP_ENV=production`, a real `SECRET_KEY`, SMTP, and serve over HTTPS. SQLite needs a persistent disk/volume for `DATABASE_PATH`.

## Files
- `app.py`: API, OTP auth, payment init/verify/webhook, SQLite schema
- `playgrounds.js`: voice, the Talk screen and the eight playgrounds
- `omega.py`: Air Omega's prompts, checks on AI answers, week maths and email text (no database in it)
- `send_weekly_reports.py`: run once a week to send the progress emails
- `courses_seed.py`: courses and lesson titles (edit freely; lessons are only sent to buyers)
- `static/index.html`, `style.css`, `app.js`: the whole UI
