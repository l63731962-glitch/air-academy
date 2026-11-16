# Air Academy (HTML + Python)

Flask backend + plain HTML/CSS/JS frontend. Passwordless sign-in (6-digit email code), 11 tracks, 4,000 NGN per course, paid through Stripe (or Flutterwave until Stripe is switched on).

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
- `STRIPE_SECRET_KEY`: Stripe dashboard > Developers > API keys. Starts `sk_test_` for testing and `sk_live_` for real money. When this is set (and the price below is valid) Stripe is the payment provider.
- `STRIPE_WEBHOOK_SECRET`: starts `whsec_`, from the webhook endpoint you create in Stripe (see "Stripe payments" below).
- `STRIPE_CURRENCY` (default `ngn`) and `STRIPE_AMOUNT` (the price in that currency, for example `4000` for NGN or `2.99` for USD). If you leave `STRIPE_AMOUNT` empty and the currency is `ngn`, it uses `PRICE_NGN` (4,000).
- `OWNER_EMAILS`: your own email address (comma-separated if more than one). Only these accounts see the live-user counter and the Control Room. It is read on the server, so no one else can open it. Keep your address here on Render, not in the code.
- `FLW_PUBLIC_KEY` / `FLW_SECRET_KEY`: Flutterwave, only used while `STRIPE_SECRET_KEY` is not set. Safe to remove once Stripe is live.
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

## Stripe payments
**How it works.** Tapping Unlock creates a Stripe Checkout Session on the server and sends the student to Stripe's own payment page, so card details never touch this app. Stripe sends the student back, and the server asks Stripe what really happened. Stripe also calls the webhook. The track unlocks only when the amount, the currency, the reference, the student and the track all match what the server asked for. The price is always decided by the server.

**Before you can take real money.** Stripe does not support businesses registered in Nigeria directly, and Naira card and bank-transfer payments are an invite-only Stripe preview for accounts outside Nigeria (money is paid out in dollars). Check your account at dashboard.stripe.com. The code works with any currency Stripe gives your account (`STRIPE_CURRENCY` and `STRIPE_AMOUNT`). Until Stripe is switched on, payments keep running on Flutterwave. Remember that Stripe also keeps a fixed 30 cents on every sale, which is a big share of a ₦4,000 sale (about $2.4), so check the numbers in the Control Room.

**Set it up (test mode first).**
1. In Stripe, turn on **Test mode**. Copy the secret key (`sk_test_...`) into Render as `STRIPE_SECRET_KEY`. Set `STRIPE_CURRENCY` and `STRIPE_AMOUNT`.
2. Stripe > Developers > Webhooks > **Add endpoint**. URL: `https://YOUR-DOMAIN/api/stripe/webhook`. Events to send: `checkout.session.completed`, `checkout.session.async_payment_succeeded`, `checkout.session.async_payment_failed`, `checkout.session.expired`, `charge.refunded`, `charge.dispute.created`.
3. Copy the signing secret (`whsec_...`) into Render as `STRIPE_WEBHOOK_SECRET`. Render restarts by itself.
4. Pay with the Stripe test card `4242 4242 4242 4242`, any future date, any CVC. The track unlocks when you come back. Open the Control Room > Setup check to see the webhook arrive.
5. When it all works, swap in the live key (`sk_live_...`) and a new live webhook secret. The Control Room warns you if a test key is left on a live site.

**Which payment methods show** (cards, bank transfer, and so on) is set in Stripe > Settings > Payment methods, with no code change.
**Refunds.** Refund in the Stripe dashboard. A full refund takes the track back automatically. A dispute flags the payment and emails you, and the student keeps access until you decide.
**Old Flutterwave payments** stay valid and are counted in revenue.

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
Sign in, open a locked course, tap **Unlock**. With Stripe on, you land on Stripe's page (test card `4242 4242 4242 4242`); with Flutterwave, use one of their test cards (test keys only). The track unlocks without a reload.

## Deploy
On Render: **Root Directory** `air_academy_web`, build command `pip install -r requirements.txt`, and start command `gunicorn app:app --workers 2 --threads 4 --timeout 120` (one plain worker would stop answering everyone while it waits for OpenAI). Set `APP_ENV=production`, a real `SECRET_KEY`, `DATABASE_URL` (Supabase), `RESEND_API_KEY` / `RESEND_FROM`, and serve over HTTPS. Never set `DEMO_UNLOCK` there. On Windows use `waitress-serve app:app`.

## Files
- `app.py`: API, OTP auth, payments (Stripe and Flutterwave), live users, owner routes, database schema
- `billing.py`: Stripe helpers with no database in them (price in minor units, checkout form, webhook signature check, what a session means)
- `control.py`: the Control Room's maths with no database in it (price lists, plans, projections, warnings, what-if)
- `static/live.js` (the ping) and `static/owner.js` (the Control Room, loaded only for the owner)
- `assistant.js`: Air Omega everywhere: the floating panel, quick commands, the actions it can run, and the memory panel
- `playgrounds.js`: voice, the Talk screen and the eleven playgrounds
- `omega.py`: Air Omega's prompts, checks on AI answers, week maths and email text (no database in it)
- `send_weekly_reports.py`: run once a week to send the progress emails
- `courses_seed.py`: courses and lesson titles (edit freely; lessons are only sent to buyers)
- `static/index.html`, `style.css`, `app.js`: the whole UI

## Free lessons, the paywall and the animation tracks
- **Price.** `PRICE_NGN = 4000` in `app.py` is the only price the server charges. `PRICE` in `static/app.js` is only a fallback: the screen shows whatever price the server reports (Stripe's price when Stripe is on). `ACCEPTED_PRICES` also accepts the old 3,500 so a payment that was started before the price change still verifies.
- **Free lessons.** `FREE_LESSONS = {"prompt-engineering": 2}` in `app.py`. Signed-in students can read and take the quiz for those lessons without paying. Everything else stays locked, and the server enforces it: locked lesson text is never sent. The AI helpers (mentor, pictures, assignments, playgrounds, exam, CA) stay for people who bought the course because they cost money. To change the free lessons, edit that one line.
- **New tracks.** `2d-animation` (2D Animation Fundamentals), `3d-animation` (3D Animation Mastery) and `ai-animation` (AI Animation and Storytelling), five lessons each (`lessons_2d_animation.py`, `lessons_3d_animation.py`, `lessons_ai_animation.py`). They are added to the database automatically at start-up. The Animation Masterclass is unchanged. Existing class numbers do not change: the new tracks are classes 9, 10 and 11.
- **Dashboard.** Topic tabs (All, 2D Animation, 3D Animation, AI Animation) sit under the search box. The lesson page has a syllabus sidebar that marks lessons Free, Locked or Done. Tapping a locked lesson, or "Continue to Lesson 3", opens the unlock pop-up.
- **Demo Unlock Pro (testing only).** Add `DEMO_UNLOCK=1` to your local `.env` and a "Demo Unlock Pro" button appears. It opens every course for your own session so you can look at the paid screens. It writes nothing to the database, and the server ignores it when `APP_ENV=production` or when running on Render. Never set `DEMO_UNLOCK` on Render.
