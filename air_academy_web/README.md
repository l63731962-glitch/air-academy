# Air Academy (HTML + Python)

Flask backend + plain HTML/CSS/JS frontend. Passwordless sign-in (6-digit email code), 11 tracks, 4,000 NGN per course, paid through Paystack (card, bank transfer and USSD; students abroad can pay with an international card once you switch that on in Paystack).

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
- `PAYSTACK_SECRET_KEY`: Paystack dashboard > Settings > API Keys & Webhooks > Secret Key. Test keys start with `sk_test_`, live keys with `sk_live_`. Use the SECRET key, not the public one (`pk_...`): a public key cannot confirm payments, so the app treats it as not set up. The same key signs Paystack's webhook calls, so there is no separate webhook password. The Control Room warns if a test key is left on a live site, because real cards would not work and no money would reach you.
- Webhook (safety net so a payment unlocks even if the student closes the page right after paying): Paystack > Settings > API Keys & Webhooks > **Live Webhook URL** = `https://YOUR-DOMAIN/api/paystack/webhook`. Nothing to add on Render for it.
- `PUBLIC_URL` (optional): your site's address, for example `https://YOUR-SITE.onrender.com`. Paystack sends students back here after paying. When it is not set the app uses the address the student is visiting, which is correct on Render.
- `OWNER_EMAILS`: your own email address (comma-separated if more than one). Only these accounts see the live-user counter and the Control Room. It is read on the server, so no one else can open it. Keep your address here on Render, not in the code.
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
- Only the Prompt Lab and Agent Lab, voice and chat use OpenAI. The Scene and Storyline Playground (AI Animation) also uses OpenAI. The other eight run entirely in the browser and cost nothing.

## Air Omega knows the app and can open anything
Air Omega is the round button at the bottom right of every screen (and the "Talk to Air Omega" button on the dashboard). It stays on screen while the app changes behind it.
- **It knows the whole app.** Every message carries a manual that is built from the app's own settings (price, grading weights, limits, tracks, playgrounds), so it cannot go out of date. It also knows the student: their tracks and progress, quiz and weak-spot counts, assignments, exam and certificate status, XP, class group and what to do next. And it knows which screen they are on, including the lesson text and whatever they built in a playground.
- **It can open and set up anything.** Say or type "open Prompt Engineering", "go to lesson 3 of Animation", "open my CA", "show locked tracks", "open the leaderboard", "read this lesson", "change your voice to Nova", or "set up the traffic simulator for a viral spike with 4 medium servers". Simple commands like these are understood in the browser, instantly, with no AI call. Anything more complicated goes to the AI, which answers with actions.
- **Every action is checked.** The AI only proposes actions as JSON. The server checks each one against a fixed list (known track ids, lessons 1 to 8 (5 in the three animation tracks), whitelisted playground settings) and drops anything else. It can never pay, unlock a track, or sign anyone out by itself: signing out is only offered as a button the student taps and confirms.
- **Suggestions.** Air Omega can offer buttons for the best next steps, and the student taps one to do it.
- **Memory.** Air Omega can keep up to 20 short facts about a student's goals and interests, so it helps better next time. It never keeps contact details, links, passwords or addresses. The brain button in the panel shows every fact, and the student can delete one or all of them.
- On a phone the panel steps aside after it opens something, so the student can see it. Tap the button to bring it back.

## Weekly emails
Emails go out when something calls the trigger. Two ways, pick one:
1. **Free scheduler (cron-job.org).** Create a job that sends a `POST` to `https://YOUR-DOMAIN/api/internal/weekly-reports` every Monday morning, with the header `X-Cron-Secret: <your CRON_SECRET>`. It answers at once and sends the emails in the background.
2. **Render Cron Job.** Create a Cron Job service from the same repo with command `python send_weekly_reports.py`, schedule `0 6 * * 1` (that is 07:00 in Lagos on Mondays, as Render uses UTC) and the same environment variables as the web service.

Running it twice is safe: an email is never sent twice for the same week. It needs `RESEND_API_KEY` and `RESEND_FROM` (already used for sign-in codes) and `PUBLIC_URL`.

## Paystack payments
**How it works.** Tapping Unlock asks the server to start a payment (the server always decides the price: ₦4,000, sent to Paystack in kobo) and sends the student to Paystack's own secure page. Card, bank transfer and USSD are offered there. Paystack then returns the student to the site with a reference, and the server asks Paystack what really happened (`/transaction/verify/{reference}`). The track unlocks only if the status, reference, currency, amount and the student's email all match. Paystack also calls the webhook (`/api/paystack/webhook`, signed with HMAC-SHA512 using your secret key) as a safety net. A bank transfer can take a few minutes to clear: the page keeps checking and the webhook finishes it if the student leaves.
**Students outside Nigeria.** They pay the same ₦4,000 with an international card and their own bank converts it. Paystack does not switch international cards on by default: in the Paystack dashboard go to Settings > Preferences and request international payments (it can take a couple of working days). Until then foreign cards are declined.
**Money that was paid but not confirmed.** If Paystack says a payment was successful but something did not match (wrong amount, wrong email, and so on) the Control Room shows a warning with the reason for 3 days. Check the payment in your Paystack dashboard and use **Give a track** if it is real. If Paystack refuses to start a payment at all (a wrong key, for example) the same warning appears.
**Fees.** The Control Room estimates Paystack's fee for a local card: 1.5% plus ₦100 (the ₦100 is not charged on sales under ₦2,500), never more than ₦2,000. On a ₦4,000 sale that is about ₦160. Foreign cards cost more (about 3.9% plus ₦100). The numbers are editable under Plans; your Paystack dashboard shows the real fee.
**Refunds** are made in the Paystack dashboard. The app does not take a track back automatically on a refund.
**Older payments.** Payments made before Paystack was switched on keep their original label and still count as sales in the Control Room.

## Welcome video
`static/intro.js` (loaded in `<head>` of `index.html`) plays `static/intro.mp4` full screen the moment the app opens, then pops up an **EXPLORE** button; tapping it opens the app. It starts muted when the browser forbids sound (with a "Tap for sound" button), has a Skip button from the first second, and plays once per session (`SHOW` at the top of the file: `session`, `day` or `always`). It steps aside by itself when the video is missing or broken, has not started after 7 seconds, on Data Saver or 2G, with reduced motion, on `/?nointro`, off the front page, and when a student returns from Paystack (`?reference=` / `?trxref=`). The video is served with a one-week cache header; after replacing `intro.mp4`, add 1 to `VERSION` in `intro.js`. The service worker does not touch video files. Use H.264 + AAC, about 2 MB or less, about 10 seconds or less (`-movflags +faststart`); a vertical 9:16 video fills phone screens best.

## Live users and the Control Room (owner only)
Set `OWNER_EMAILS` to your email. Sign in with it and the dashboard shows a green **N live · Control Room** button.
- **Live users.** Every open tab sends a tiny ping every 30 seconds. Someone counts as online for 75 seconds after their last ping, so one person is one, two people are two, and a student with three tabs open is still one. A tab that is hidden, or a phone that was put down, drops off within about a minute. Signed-in students and visitors on the sign-in page are counted separately. You are not counted unless you tap "Count me too" (handy for testing: or open a private window without signing in).
- **The meter.** Every AI call, picture, voice and email is logged with its cost the moment it happens. The Control Room shows OpenAI spend against your monthly budget with a projection for the whole month, where the money goes (chat, pictures, voice and so on), who uses the most, emails against your Resend limits, database size against your Supabase plan, and the most students online together against what your Render plan handles. Bars turn amber at 80% and red at 100%.
- **Alerts.** When something needs attention you also get an email (a red problem at most once every 12 hours, an amber one every 2 days). Switch this off under Plans. "Send a test alert" checks the email reaches you.
- **Plans.** Pick your Render, Supabase and Resend plans (or type your own numbers) so the bill, the projections and the warnings match what you really pay. OpenAI amounts are estimates from token counts at the public price list, so compare with platform.openai.com now and then.
- **What if.** Slide to 1,000 or 25,000 students and see the monthly bill, which plans you would need, and what is left over after sales. It uses what your real students cost once 10 are active, and typical numbers before that.
- **Sales, students and tools.** Revenue, fees, refunds, daily sales, sign-ups, daily and monthly active students, and the sign-up-to-paying funnel. **Give a student a track** by email for a giveaway or a payment that did not unlock. Every change is written to a log.
- It is private on the server: everyone else gets a "not found" answer from every owner address, and the page's code is only downloaded when you tap the button. The only thing a student's device keeps is a random id per tab for the ping.

## Test a payment
Sign in, open a locked course, tap **Unlock**. Use your Paystack test key (`sk_test_...`) and one of Paystack's test cards (never on the live site: see the warning above). Paystack's test mode needs the webhook URL in the **Test Webhook URL** box. The track unlocks without a reload.

## Deploy
On Render: **Root Directory** `air_academy_web`, build command `pip install -r requirements.txt`, and start command `gunicorn app:app --workers 2 --threads 4 --timeout 120` (one plain worker would stop answering everyone while it waits for OpenAI). Set `APP_ENV=production`, a real `SECRET_KEY`, `DATABASE_URL` (Supabase), `RESEND_API_KEY` / `RESEND_FROM`, and serve over HTTPS. Never set `DEMO_UNLOCK` there. On Windows use `waitress-serve app:app`.

## Files
- `app.py`: API, OTP auth, payments (Paystack), live users, owner routes, database schema
- `billing.py`: small payment helpers with no database in them (price text, Paystack key mode, webhook signature check, what a payment confirmation must match)
- `control.py`: the Control Room's maths with no database in it (price lists, plans, projections, warnings, what-if)
- `static/live.js` (the ping) and `static/owner.js` (the Control Room, loaded only for the owner)
- `assistant.js`: Air Omega everywhere: the floating panel, quick commands, the actions it can run, and the memory panel
- `playgrounds.js`: voice, the Talk screen and the eleven playgrounds
- `omega.py`: Air Omega's prompts, checks on AI answers, week maths and email text (no database in it)
- `send_weekly_reports.py`: run once a week to send the progress emails
- `courses_seed.py`: courses and lesson titles (edit freely; lessons are only sent to buyers)
- `static/index.html`, `style.css`, `app.js`: the whole UI

## Free lessons, the paywall and the animation tracks
- **Price.** `PRICE_NGN = 4000` in `app.py` is the only price the server charges. `PRICE` in `static/app.js` is only a fallback: the screen shows whatever price the server reports. `ACCEPTED_PRICES` also accepts the old 3,500 so a payment that was started before the price change still verifies.
- **Free lessons.** `FREE_LESSONS = {"prompt-engineering": 2}` in `app.py`. Signed-in students can read and take the quiz for those lessons without paying. Everything else stays locked, and the server enforces it: locked lesson text is never sent. The AI helpers (mentor, pictures, assignments, playgrounds, exam, CA) stay for people who bought the course because they cost money. To change the free lessons, edit that one line.
- **New tracks.** `2d-animation` (2D Animation Fundamentals), `3d-animation` (3D Animation Mastery) and `ai-animation` (AI Animation and Storytelling), five lessons each (`lessons_2d_animation.py`, `lessons_3d_animation.py`, `lessons_ai_animation.py`). They are added to the database automatically at start-up. The Animation Masterclass is unchanged. Existing class numbers do not change: the new tracks are classes 9, 10 and 11.
- **Dashboard.** Topic tabs (All, 2D Animation, 3D Animation, AI Animation) sit under the search box. The lesson page has a syllabus sidebar that marks lessons Free, Locked or Done. Tapping a locked lesson, or "Continue to Lesson 3", opens the unlock pop-up.
- **Demo Unlock Pro (testing only).** Add `DEMO_UNLOCK=1` to your local `.env` and a "Demo Unlock Pro" button appears. It opens every course for your own session so you can look at the paid screens. It writes nothing to the database, and the server ignores it when `APP_ENV=production` or when running on Render. Never set `DEMO_UNLOCK` on Render.
