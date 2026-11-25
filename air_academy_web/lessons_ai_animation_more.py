"""AI Animation track: lessons 6 to 15, added when the track grew from 5 to 15 lessons (course_plan.py says where each one sits on screen).
Same format as lessons_ai_animation.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option.
AI tools change very fast. Lessons describe kinds of tools and habits that last, and tell learners to check each tool's current features, prices, payment options, terms and licences."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[6] = dict(   # Choosing and testing AI tools: what each one is good at
    minutes=15,
    hook="New AI tools appear every week, each with a dramatic demo and a promise of a whole film in one click. For a young creator, this is both exciting and confusing. Which tool should you use for the story, the pictures, the motion, the voices and the music? Which are free, which need a bank card that works in Nigeria, which allow you to use the result in a commercial project? A smart creator does not chase every new tool. Instead, you learn the kinds of tools, you test a few of them on your own project using the same fair test, and you keep a short list of tools you trust. In this lesson you will learn the main categories of AI tools for animation and what each is good and bad at, a simple scorecard for testing, how to read prices, free limits and terms, how to protect your accounts and data, and how to build a small, reliable toolkit that does not break when one company changes its rules.",
    sections=[
        ("The kinds of tools", """You do not need to memorise product names, because those change. Learn the **categories:**

- **Text assistants (chatbots):** brainstorm ideas, outline stories, draft and polish scripts, write prompts and organise your plan. Good at options and structure, and weak at facts, local culture and your personal voice.
- **Image generators:** create characters, backgrounds, props and storyboards from text, and sometimes from a reference picture. Good at speed and variety, and weak at **consistency,** hands, small text and exact details.
- **Image-to-video and video generators:** turn a still image or a text prompt into a short moving clip, usually a few seconds. Good at atmosphere and camera moves, and weak at long action, complex physics and keeping a character the same.
- **Voice tools:** text-to-speech and voice conversion. Good for narration and rough dialogue, and weak at emotional acting and correct pronunciation of African names and languages.
- **Music and sound tools:** create background music and effects. Good for mood beds, and weak at exact timing and cultural authenticity.
- **Lip-sync and motion tools:** match mouths to audio, or copy movement from a phone video.
- **Editing, upscaling and clean-up tools:** cut, colour, remove noise, raise resolution, add subtitles.

Many companies offer several of these in one site. **Mixing tools from different makers** is normal, and often gives the best result."""),
        ("A fair test with a scorecard", """Do not judge a tool from its advertising. Test it on **your own project** with the **same inputs:**

1. **Choose a standard test:** for images, the same character description and the same setting. For video, the same still image and the same simple motion, such as a slow camera push. For voice, the same 30-word script with a hard name in it, like “Chukwuemeka.”
2. **Run each tool three times,** because results vary.
3. **Score each tool from 1 to 5** on these points:
   - **Quality:** does it look good?
   - **Consistency:** does the character stay the same across tries?
   - **Control:** can you steer it with prompts and references?
   - **Speed:** how long does each result take?
   - **Cost:** what does one usable result really cost?
   - **Ease:** can you learn it quickly on your device?
   - **Rights:** are commercial uses allowed?
   - **Privacy:** what happens to your uploads?
4. **Add up the scores** and write one sentence of notes.

Keep the scorecard in a simple table. When a new tool arrives, you can test it in an hour and compare."""),
        ("Prices, free limits and payment", """Most tools have a **free tier** with limits, and **paid plans** for more. Read these carefully:

- **Credits:** many video and image tools use credits. A short video clip may cost many credits, and failed attempts still use them. Estimate how many tries you will need.
- **Watermarks and resolution:** free results may carry a watermark or be low resolution, which limits use in a finished film.
- **Commercial use:** some tools allow commercial use only on paid plans. If you plan to sell, take payment from a client or monetise a video channel, check this **before** you make the work.
- **Speed and queue limits:** free users may wait in line.
- **Payment methods:** some services accept only international cards. Naira cards may or may not work, and rules change. **Never share card numbers, PINs or one-time codes with anyone,** and use only the tool's official payment page. Be careful with sites that ask you to pay through unusual methods.
- **Subscriptions:** note the renewal date, and cancel when you finish, or you may keep paying.
- **Data costs:** video tools need large uploads and downloads. Plan your bundles, and download results on a good connection.

A good rule is to **start free,** upgrade for **one month only** when you have a clear shot list, and then cancel."""),
        ("Terms, privacy and account safety", """Before you upload anything:

1. **Read the key points of the terms,** especially who owns the output, whether commercial use is allowed, and whether the company can use **your uploads** to train its systems. Many tools have settings to opt out. Check them.
2. **Do not upload private material:** other people's photos without permission, client secrets, children's images, identity documents or anything you would not post publicly.
3. **Use a strong, unique password** for each tool, and turn on **two-factor authentication.**
4. **Use a separate email** for creative accounts, so a problem does not touch your main email.
5. **Beware of fake sites and apps** that copy famous tools, and of links that promise “free unlimited” access. They can steal logins and install malware. Go to the official website by typing the address.
6. **Keep a record** of the plan, date and settings you used for every result, as a **use log.** If a rule changes later, you can show what you had when you made the work.

Remember that these companies can **change terms, raise prices or close,** so keep local copies of your best results and prompts."""),
        ("Build a small toolkit", """Aim for a **small, balanced toolkit,** not a huge pile:

- **One text assistant** for planning and drafts.
- **One or two image tools** for characters and backgrounds.
- **One image-to-video tool** for motion, with another as a backup.
- **One voice option** (recorded humans first, tools second).
- **One music option,** and a free editor for sound, such as **Audacity.**
- **One video editor,** such as **DaVinci Resolve, Kdenlive or Shotcut** (check current licences).
- **A folder for notes:** the scorecards, prompts and use log.

Test the **whole chain** with a **5-second mini film** before you commit. Does the character survive from image to video to edit? Is the sound clear? Can you export? Fixing the chain on five seconds is cheap, and finding that it breaks at one minute is expensive. Remember, a tool is only a tool. **Your story, taste and decisions** are what make the film yours."""),
    ],
    diagram=grid([("Text", "ideas and scripts"), ("Image", "looks and boards"), ("Image to video", "motion clips"), ("Voice", "narration, dialogue"), ("Music and sound", "mood and effects"), ("Editing", "cut, colour, export")], cols=3, note="Learn the kinds, not the brand names."),
    caption="Six kinds of AI tools for animation: text, image, image-to-video, voice, music and sound, and editing.",
    terms=[("AI tool category", "A group of tools that do the same kind of job, such as image generation."), ("Credits", "Points a tool charges for each generation."),
           ("Free tier", "The limited free plan of a tool."), ("Scorecard", "A table used to compare tools on the same points."),
           ("Two-factor authentication", "A second step, such as a code, needed to log in safely."), ("Use log", "A record of tools, plans, prompts and dates used to make each result.")],
    mistakes=["Judging a tool by its advertising demo instead of testing it on your own project.", "Making commercial work with a tool whose plan does not allow commercial use.", "Sharing card details or one-time codes outside the official payment page.", "Uploading other people's private photos into a tool."],
    quiz=[dict(q="What is the best way to compare two image tools?", o=["Believe the advertisement", "Use the one with the longest name", "Pick the newest", "Give both the same test prompt several times and score the results"], a=3,
               why="A fair, repeated test on your own project shows real strengths and weaknesses."),
          dict(q="What should you check before using AI output in paid work?", o=["The colour of the logo", "Whether your plan allows commercial use", "The number of followers", "The font"], a=1,
               why="Some tools allow commercial use only on certain plans."),
          dict(q="Which is a safe account habit?", o=["Using one weak password everywhere", "Sharing your code with support chat", "A unique strong password with two-factor authentication", "Clicking links that promise free unlimited access"], a=2,
               why="Strong passwords and two-factor login protect your accounts."),
          dict(q="Why test a 5-second mini film first?", o=["It is required by law", "It finds chain problems cheaply before you commit", "It makes tools free", "It removes the need for a plan"], a=1,
               why="Problems are cheaper to discover on a tiny test than on a full film.")],
    activity="Pick two tools in one category, run the same test three times each, fill in a scorecard, read each one's terms for commercial use and training on uploads, and write your starter toolkit on one page.",
)

LESSONS[7] = dict(   # Story structure: hook, conflict and ending
    minutes=15,
    hook="A short film has very little time to earn attention. On a phone, a viewer decides in about three seconds whether to keep watching. Then, if the film is lucky, it has a minute or two to make them care, and one last moment to leave them feeling something. This is why the structure of a short story matters so much. You already learned the logline and the three acts. In this lesson we zoom in on the three parts that decide whether a short film works: the hook that opens it, the conflict that drives it and the ending that finishes it. You will learn how to open with a question, how to build and raise the conflict, how to plant and pay off small details, how to choose an ending, how to use traditional stories with respect, and how to use an AI assistant as a critic who finds weaknesses, without letting it write the heart of the story for you.",
    sections=[
        ("The hook: win the first three seconds", """A hook is something in the opening that makes the viewer **ask a question** and want the answer. Good hooks:

- **A problem in action:** a girl runs through a market, clutching a bag, with a man shouting behind her. Why is she running?
- **A strange image:** a goat wearing a school uniform, waiting at a bus stop.
- **A promise:** “This is the story of how I lost my grandmother's drum.”
- **A broken pattern:** everything is calm, and then something small is wrong.
- **A character who wants something badly,** shown at once.

Avoid slow openings: long titles, a sunrise over a village with no action, or an explanation of the world. Start **as late as possible,** when something is already happening. Keep your first shot **simple and striking,** because it will also be your **thumbnail.** For a film that will play on social media, put the **most interesting image or action in the first second,** and make sense without sound."""),
        ("Conflict: what stands in the way", """A story is not a list of events. It is **a character who wants something and an obstacle that stops them.** Types of conflict:

- **Person against person:** two traders want the same customer.
- **Person against nature:** a fisherman and a storm.
- **Person against society:** a child who wants to study when the family needs help in the shop.
- **Person against themselves:** a boy who wants to speak up but is afraid.
- **Person against technology or the unknown:** a robot that does not know how to cry.

Make the conflict **clear, personal and visible.** Show what the character **wants,** what they **do,** and what it **costs** them. Then raise the **stakes:** each attempt should make things harder, not easier. A useful pattern is the **rule of three:** the character tries and fails once, fails more badly a second time, and then finds a new way on the third. In 60 seconds, you may have room for only one failed try, and that is fine."""),
        ("Setups and payoffs", """Great short stories feel tight because small things **come back.** A **setup** is a detail shown early. A **payoff** is when it matters later.

- Early: the tortoise has a **cracked shell.** Later: the crack lets him hide a small stone, which saves him.
- Early: a girl keeps her **mother's headscarf** in her pocket. Later: she uses it to signal a bus.
- Early: a vendor says “**Never open the blue gate.**” Later: the child opens it.

Use setups and payoffs to make the audience feel clever and the story feel fair. Rules:

1. **Plant the detail clearly,** but not too loudly.
2. **Make it matter** in the ending, not just as a decoration.
3. **Cut anything** that does not pay off or support the main idea.
4. **Pay off emotions too:** if a character is shown wanting a hug, the film should answer that.

With the shot list in mind, a setup must be **visible in a shot,** and AI image tools need to show it correctly every time, so keep these details simple."""),
        ("Endings that land", """The ending answers the question the film asked. Common types:

- **Happy or resolved:** the character gets what they need, perhaps in a surprising way.
- **Bittersweet:** the character gets something but loses something too.
- **Ironic or twist:** the result is the opposite of what we expected, but fits.
- **Open:** a question is left for the viewer to think about. Use carefully, since it can feel unfinished.
- **Circular:** the film ends with an image from the start, but now it means something different.

Good endings are **surprising but inevitable,** and they come from the **character's choice,** not from luck or a magic rescue. Spend extra time on the **last image,** since it is what people remember. Then end **quickly** after the climax. Do not explain the moral. Let the picture speak, and use one short line if you must.

Test it: **write the last shot in one sentence.** If you can see it clearly and feel something, you are on the right track."""),
        ("Folktales, respect and AI as a critic", """Africa's oral stories, such as tortoise tales, moonlight stories and proverbs, are a rich source of structure: a clever hero, a test, a lesson and often a call-and-response with the audience. You can learn from them, and adapt them with care:

- **Credit the tradition** and, where possible, the person or community who told you the story. **Ask permission** to retell personal or community stories.
- **Do not copy** a recent author's or filmmaker's version. Traditional stories can be free to use, but modern retellings belong to their creators.
- **Keep the heart** of the story and show something new from your own life.

Using AI well in story work:

1. **Ask the assistant to criticise,** not to replace you: “Here is my one-page story. Where is the hook weak? Where does the conflict feel flat? What would a viewer ask here?”
2. **Ask for three alternative endings** and use them as ideas, then write your own.
3. **Ask it to find holes** or unclear motivations.
4. **Check cultural details** with real people, since AI often gets local detail wrong.
5. **Keep your own voice.** If it reads like a generic story, rewrite in your own words and details."""),
    ],
    diagram=timeline([("Hook", "a question in 3 seconds"), ("Setup", "want and world"), ("Conflict", "something blocks it"), ("Escalation", "stakes rise"), ("Climax", "the big choice"), ("Ending", "answer and image")], note="Start late, end fast."),
    caption="A short film structure: hook, setup, conflict, escalation, climax and ending, starting late and ending quickly.",
    terms=[("Hook", "An opening that makes the viewer ask a question."), ("Conflict", "What stands between the character and what they want."),
           ("Stakes", "What the character stands to lose or gain."), ("Setup", "A detail shown early so it can matter later."),
           ("Payoff", "The moment when a setup becomes important."), ("Climax", "The moment of greatest tension or choice.")],
    mistakes=["Opening with a long slow explanation instead of action or a question.", "Writing a list of events with no clear want and obstacle.", "Ending with luck or a magic rescue instead of the character's choice.", "Retelling a modern author's version of a folktale as if it were free."],
    quiz=[dict(q="What does a good hook do?", o=["Explains the whole plot", "Makes the viewer ask a question", "Shows the credits first", "Gives the ending away"], a=1,
               why="A question keeps viewers watching to find the answer."),
          dict(q="What is a payoff?", o=["A late detail that finally matters because it was set up early", "A payment to the tool", "A sound effect", "A title card"], a=0,
               why="Setups and payoffs make a story feel tight and fair."),
          dict(q="How should you use an AI assistant for story ideas?", o=["Let it write the whole film and publish it", "Ask it to critique and offer options, then write in your own voice", "Never read what it says", "Use it to copy a famous film"], a=1,
               why="Use it as a critic and idea partner, and keep creative decisions yourself."),
          dict(q="What should the ending come from?", o=["Luck", "A magic rescue", "A random twist", "The character's choice"], a=3,
               why="Endings feel earned when the character's choice decides the result.")],
    activity="Write the hook, conflict with one failed attempt, one setup and payoff and the ending of a 60-second story in six sentences. Ask an AI assistant to find the three weakest points, fix them yourself and test the story on two people.",
)

LESSONS[8] = dict(   # Writing dialogue and narration with AI
    minutes=15,
    hook="Good dialogue sounds like people, and bad dialogue sounds like a school essay read aloud. In a short animation, words are costly, since every line has to be spoken, recorded, matched to a mouth and fitted into a few seconds. So each word must do a job. AI text tools can generate dialogue in seconds, but they tend to produce lines that are too polite, too long and too neat, and they often get African speech patterns wrong. In this lesson you will learn what makes dialogue and narration work, how to measure lines in seconds, how to write in the real voices of your characters, including Nigerian Pidgin and mother-tongue phrases, how to use AI for options and checks without losing your voice, how to prepare a script for recording and how to test every line aloud. Treat the AI as a draft partner, and you remain the writer.",
    sections=[
        ("What good dialogue does", """Every line should do **at least one** of these jobs:

- **Show character:** how someone speaks tells us who they are. A trader may speak quickly and joke. A grandmother may speak slowly with proverbs.
- **Move the story:** reveal something, make a choice, raise the stakes.
- **Show feeling,** often by **not saying it.** This is **subtext:** the real meaning under the words. “I'm fine” said with a tight face means “I am not fine.”
- **Add humour or rhythm.**

Rules that help:

1. **Keep lines short.** People interrupt, hesitate and use few words.
2. **Cut greetings and filler** that do not matter, unless they show character.
3. **Do not explain what the picture shows.** If we see a girl crying, she does not need to say “I am crying.”
4. **Give each character a different voice:** vocabulary, rhythm, favourite words.
5. **Let silence and action** do work. A look can replace three lines.

In animation, a character may speak **no more than a few short lines per shot.**"""),
        ("Timing: count the words", """Speech has a rhythm, and your film has fixed seconds. As a rough guide, people speak about **2 to 3 words per second** in normal conversation, and a bit slower for narration or emotion. So:

> [Timing guide]
> 5 seconds of speech = about 12 to 15 words
> 10 seconds = about 25 to 30 words
> 15 seconds = about 35 to 40 words

Add time for **pauses, breaths and reactions.** A shot with a **long reaction** needs fewer words. To check:

1. **Read the line aloud** with a stopwatch, acting it, not rushing.
2. **Write the time** next to each line in the script.
3. **Add the times** to see the length of the whole film.
4. **Cut** until it fits. It is better to **remove words** than to speed up a voice until it sounds unnatural.

Tell the AI the limit: “Write this line in no more than 12 words, spoken in about 4 seconds.” Always test the result yourself."""),
        ("Real voices: languages, Pidgin and respect", """Nigerian speech is beautifully varied: English, Pidgin, Yoruba, Igbo, Hausa and many more, often mixed in one sentence. This is a **strength** for your film, but AI tools often get it wrong, writing stiff, textbook, or even offensive versions.

- **Write the lines yourself first,** or with a native speaker. Use AI only to offer extra options.
- **Check every line with real speakers** of that language or dialect, for grammar, tone and respect. Ask: would someone really say it that way?
- **Do not use a language or accent as a joke** or a stereotype. Characters from any background should be real people.
- **Mix languages naturally,** the way your community does. Provide **subtitles** if your audience may not understand.
- **Spell names for pronunciation:** add a phonetic note, such as **Chukwuemeka (choo-kwoo-eh-MEH-kah)** and **Abubakar (ah-boo-BAH-kar),** so voice actors and tools say them correctly.
- **Respect proverbs and sacred phrases.** Use them accurately, and credit the source where you can.

If a tool cannot pronounce a language well, record a **human voice** instead. Human performance is also better for emotion."""),
        ("Using AI to improve, not replace", """Useful ways to work with a text assistant:

1. **Give it the context:** the character, their mood, the situation, the length limit and what the line must achieve.
2. **Ask for five different versions** of one line, with different tones: blunt, shy, funny, angry, proud.
3. **Ask it to find clichés:** “Which of my lines sound like a generic movie?”
4. **Ask for subtext:** “Rewrite this line so that she does not say she is sad, but we can tell.”
5. **Ask it to shorten** and check word counts.
6. **Ask it to explain problems,** not just rewrite them.
7. **Compare and choose:** take the best pieces, then **rewrite in your own words.**

Watch for **AI habits:** over-polite, complete sentences, repeated phrases, generic wisdom, or a neat moral at the end. If it sounds like a motivational poster, **cut it.** For narration, keep a consistent voice: warm, dry, mysterious. Narration should add **what the picture cannot,** such as time, thought or humour."""),
        ("Prepare the script for recording and test it", """Before recording, prepare a clean **dialogue script:**

- **Number each line** (`S03-L02`), with the character, the line, the **emotion note** (“whispering, scared”) and the **target time.**
- **Add phonetic spelling** for hard names.
- **Group lines by actor** so recording sessions are efficient.
- **Keep a master version** of the script and mark changes with version numbers.

Then test:

1. **Table read:** read the whole script aloud with friends, each taking a part. Where do you stumble? Where do people laugh or lose attention?
2. **Time it** again with the actual voices.
3. **Listen for repeated words** and similar-sounding lines.
4. **Check the story** works with the sound off and the dialogue removed. If it does, the dialogue is a bonus. If not, the pictures need work.
5. **Cut one more line** than you think you need.

When you record, give each performer the full context, record **several takes** and credit them. Save the final text as part of your film's **documentation.**"""),
    ],
    diagram=compare(("WEAK DIALOGUE", ["Long and polite", "Explains the picture", "Everyone sounds alike", "Says the feeling out loud"]), ("STRONG DIALOGUE", ["Short and natural", "Adds what we cannot see", "Each voice is different", "Feeling lives in the subtext"]), vs="vs", note="Every word costs seconds."),
    caption="Weak dialogue is long, polite and explains the picture. Strong dialogue is short, natural and carries subtext.",
    terms=[("Subtext", "The real meaning under the words people say."), ("Narration", "A voice that tells the audience something outside the scene."),
           ("Table read", "Reading a script aloud with others to test it."), ("Phonetic spelling", "Writing a word as it sounds to help pronunciation."),
           ("Voice-over", "A voice heard over the picture, not coming from a visible speaker."), ("Line ID", "A number that identifies each line for recording and editing.")],
    mistakes=["Letting the AI write long, polite lines and keeping them.", "Not checking Pidgin or mother-tongue lines with real speakers.", "Writing dialogue that explains what the picture already shows.", "Never timing the lines with a stopwatch."],
    quiz=[dict(q="What is subtext?", o=["A kind of font", "The real meaning under the words", "A music style", "A file type"], a=1,
               why="Characters often mean something other than what they say."),
          dict(q="About how many words fit into 10 seconds of normal speech?", o=["About 25 to 30", "About 2", "About 300", "About 1000"], a=0,
               why="People speak about 2 to 3 words per second."),
          dict(q="Who should check lines in Yoruba, Igbo, Hausa or Pidgin?", o=["Only the AI", "Nobody", "The tool's company", "Real speakers of that language or dialect"], a=3,
               why="AI often gets grammar, tone and respect wrong in African languages."),
          dict(q="How should you use AI-written dialogue?", o=["Copy it exactly", "Use it as options, then rewrite in your own voice", "Never read it", "Use it without timing"], a=1,
               why="You remain the writer, and AI offers drafts and checks.")],
    activity="Write a 30-second dialogue scene between two characters with different voices. Ask an AI assistant for five versions of two lines, choose and rewrite the best, time every line with a stopwatch, check any Pidgin or mother-tongue lines with a speaker and prepare a numbered recording script.",
)

LESSONS[9] = dict(   # Designing a character sheet and style guide
    minutes=16,
    hook="You have learned that AI image tools forget your character from one picture to the next. A character sheet fixes the character. But a film is more than a character: the whole picture must feel like it belongs together, with the same colours, the same kind of lines, the same light and the same mood in every shot. If one shot looks like a watercolour and the next looks like a glossy 3D render, the audience feels the film is a collage of random images. The cure is a style guide: a short document that records exactly how your film looks, and that you check every new picture against. In this lesson you will build a complete character sheet with expressions and poses, define your style in words, colours and examples, write the do and do not lists, build a small project bible, test the style on five different shots and learn how to repair style drift when the tool wanders away.",
    sections=[
        ("From character sheet to a complete model sheet", """You may already have a front view of your hero. A **model sheet** adds more, like the sheets used in professional animation:

- **Turnaround:** front, three-quarter, side and back views, with the same height and outfit.
- **Expression sheet:** happy, sad, angry, surprised, scared and thinking, with the same face and style.
- **Pose sheet:** standing, walking, running, sitting, pointing, and a typical action.
- **Size comparison:** the hero next to other characters and objects.
- **Colour swatches:** the main colours of skin, hair, clothes and accessories.
- **Key details:** a scar, a pattern, a special necklace, drawn close.

Generate each part **separately,** using your **fixed description block** and the approved front image as a reference. Pick the best results and arrange them on one page with an image editor, or in a free tool such as **Krita,** and **label** them. If a result does not match, **do not use it.** Regenerate, or **edit by hand.** It is normal to make 20 images to get 6 good ones. Save the sheet as `charactername_sheet_v01.png`."""),
        ("Define your style in words, colours and examples", """A style is a collection of decisions. Write each down:

1. **Medium look:** hand-drawn 2D, paper cut-out, soft 3D, painted storybook, comic book, pixel art.
2. **Line:** thick or thin, clean or rough, black outlines or none.
3. **Shading:** flat colour, soft gradients, cel shading, painted texture.
4. **Colour palette:** pick **5 to 8 main colours,** and record their **colour codes** (hex values like #E2711D) with names, such as “market orange” and “night blue.” Limit the palette, because it forces unity.
5. **Light:** warm afternoon sun, soft evening glow, cold night.
6. **Camera and lens:** eye-level, slightly wide, shallow depth of field.
7. **Mood words:** warm, playful, mysterious, calm.
8. **Texture and details:** fabric patterns, wood grain, painted brush marks.
9. **Shape language:** round and friendly, or angular and tense.

Then pick **three to five reference images** that show the feeling. They can be your own sketches, photos you took or artwork you have permission to use. Do not use a living artist's name as a style shortcut to copy their look. Describe the qualities in **your own words.**"""),
        ("The style prompt and the avoid list", """Turn your decisions into a **reusable style block,** like the description block for the character:

> [Example style block]
> Warm hand-painted storybook look, soft gouache texture, thick rounded outlines in dark brown, flat colours with gentle shading, palette of market orange, deep green, indigo and cream, golden afternoon light, slightly wide eye-level view, gentle and playful mood.

Paste it at the end of **every image prompt,** after the character block and the shot description. Order: **shot + character + setting + style block.**

Also keep an **avoid list** of things that spoil your style or cause errors, for example: “no photorealism, no glossy 3D, no text or logos, no extra fingers, no watermarks.” Some tools have a field for things to avoid, and others work better when you state what you **do** want. Test which works for yours.

Record **which tool and version** you used, the **settings** (aspect ratio, any seed or style reference if offered), and the **date** in a use log. If the tool updates, results may change, and your log will help you understand why."""),
        ("The project bible", """A **project bible** is a short folder or document that holds everything a collaborator, or you in a month, would need:

1. **Logline and short story summary.**
2. **Characters:** model sheets and description blocks.
3. **Locations:** pictures and description blocks (see the next lessons).
4. **Props** that matter.
5. **Style guide:** palette with hex codes, line, light, camera and the style block.
6. **Voices and music notes.**
7. **Do and do not list.**
8. **Tool list** and settings.
9. **Credits and licences,** including any reference artist or community who helped.
10. **Version history.**

Keep it **short,** perhaps five to ten pages, with pictures. A one-page **cheat sheet** with the character block, the style block and the avoid list is what you will copy from daily. Save a backup in a second place."""),
        ("Test the style and repair drift", """Before you commit, test the style on **five very different shots:** a close-up, a wide shot, an indoor scene, an outdoor scene and a night scene. Then put the results side by side.

Ask:

- Do they look like **one film?**
- Does the **hero** stay recognisable?
- Are the **colours** inside the palette?
- Is the **lighting and mood** right for each scene?

If something drifts:

- **Add the style block more strongly,** or simplify the prompt.
- **Attach a style reference** from your best image.
- **Reduce competing instructions:** too many details can confuse tools.
- **Generate in batches** and choose the closest.
- **Fix in an editor:** adjust colours to the palette, paint out errors, and unify with a gentle overall tint or grain.
- **Update the guide** if you find a better choice, and note the change.

If after trying you cannot hold a style, **make the style simpler.** Flat shapes, limited colours and clear outlines are easier to keep consistent than rich, realistic painting."""),
    ],
    diagram=hub(("STYLE GUIDE", "one look for the film"), [("Palette", "5 to 8 hex colours"), ("Line and shading", "thick, flat, soft"), ("Light", "time of day and mood"), ("Camera", "lens and framing"), ("Shape language", "round or angular"), ("Avoid list", "what spoils the look")], note="Check every new picture against it."),
    caption="A style guide records palette, line and shading, light, camera, shape language and an avoid list for the whole film.",
    terms=[("Model sheet", "A page showing a character from many views, expressions and poses."), ("Style guide", "A document that records how the film should look."),
           ("Hex code", "A short code that names an exact colour, such as #E2711D."), ("Style block", "A reusable paragraph of style words added to every image prompt."),
           ("Style drift", "When pictures slowly stop matching the planned look."), ("Project bible", "A folder of everything needed to make the film consistently.")],
    mistakes=["Using a living artist's name to copy their style.", "Not writing down the colour codes of the palette.", "Using a richly detailed style that the tool cannot repeat.", "Never testing the style on different kinds of shot."],
    quiz=[dict(q="What is style drift?", o=["A kind of camera move", "A sound problem", "Pictures slowly stopping matching the planned look", "A file type"], a=2,
               why="Without a guide, the look changes from shot to shot."),
          dict(q="Where do you add the style block in a prompt?", o=["On every image prompt, after the shot and character description", "Never", "Only on the first image", "Only in the title"], a=0,
               why="Repeating it keeps the look consistent."),
          dict(q="Why limit the palette to 5 to 8 colours?", o=["It forces unity", "It makes files smaller", "It adds sound", "It speeds the internet"], a=0,
               why="A small set of colours holds the pictures together."),
          dict(q="How do you test a style?", o=["Use it on one picture only", "Look at one frame", "Generate five very different shots and compare them side by side", "Ask the tool to rate itself"], a=2,
               why="A varied test shows whether the style holds in different situations.")],
    activity="Build a model sheet with a turnaround, six expressions and three poses, write your style guide with hex colours and a style block, generate five very different test shots, and fix any drift.",
)

LESSONS[10] = dict(   # Backgrounds, props and consistent settings
    minutes=16,
    hook="Characters get the attention, but places carry the feeling. A market at dawn, a compound house at noon, a bus park at night: the setting tells us where we are, what time it is and how the characters live. AI image tools can paint stunning places in seconds, but they fail in a particular way. Ask for the same room from two angles and you get two different rooms, with the window on the wrong wall, a different colour of door and a table that has vanished. In a film, the audience notices at once. This lesson shows you how to design locations that stay the same, using location sheets, a wide master picture, simple 3D or sketch layouts as guides, props that match, consistent light, and clean compositing of characters into backgrounds. It also covers checking local details such as signs, clothing and architecture, and avoiding the use of real places, brands and logos without permission.",
    sections=[
        ("Design each location like a character", """For every place in your film, make a **location sheet,** just as you made a character sheet:

1. **A name:** “Mama Ade's Kitchen,” “Market Lane.”
2. **A description block** to paste into prompts, written in concrete detail: size, materials, colours, main objects and where they stand. For example: “small outdoor kitchen behind a yellow compound house, a clay stove on the left, a blue plastic basin on a wooden stool, a green gate at the back, a zinc roof.”
3. **A floor plan sketch:** a quick top-down drawing showing where the door, window, stove and table are. Even a rough sketch helps you stay logical.
4. **Time of day and light:** morning sun from the left, or night with one lamp.
5. **Key props** that must always be there.
6. **A reference picture** of the approved master image.

Keep the number of locations **small.** A 60-second film needs two or three at most. Re-use the same place from different angles, and it will feel larger and richer than the number of locations suggests."""),
        ("The wide master picture and the angles problem", """The best way to keep a place consistent is to start with a **wide master picture,** an establishing shot that shows the whole space.

1. **Generate the wide shot** with your location block and style block. Make many tries, and pick the one that is clear, uncluttered and logical.
2. **Mark the positions** of things on the sketch plan so that you remember them.
3. **Use the master as a reference image** when generating other angles, if your tool supports it. State clearly what must remain the same.
4. **Crop instead of regenerating.** A close-up of the stove can be a **cropped, enlarged part** of the wide picture (with an upscaler to keep sharpness). This guarantees consistency.
5. **Build a simple 3D blockout** in free **Blender** with boxes for the walls, door and furniture. Render a plain grey picture from each camera angle, and use it as a **layout guide** for image tools that accept a reference or a depth image. This shows the **same geometry** from different views.
6. **Use a flat 2D painted background plate** for a mostly static shot, and let only the characters and a few details move.
7. **Accept limits:** if a shot needs a hard new angle that the tool cannot hold, rethink the shot."""),
        ("Props that match", """Props are the small things people use. They tell stories and cause continuity errors.

- **Make a prop sheet** for important objects: the drum, the bag, the school badge, the phone. Show them from front and side, with a description block.
- **Generate props on a plain background,** then **cut them out** (many editors have background removal) and **place them** in scenes, instead of asking the tool to draw them again each time.
- **Keep scale logical:** a cup is not larger than a stool.
- **Limit the number of props.** Each extra prop is one more thing that can change between shots.
- **Name and number** the props in your shot list, so you know when each appears.
- **Watch for hands:** AI often struggles with hands holding objects. Plan shots where the hand is hidden, in shadow or partly out of frame, or **paint and fix** the hand in an editor.
- **Avoid text on props** such as signs and labels. AI writes **gibberish letters.** Add real text later in an editor, in a font you have the licence for."""),
        ("Light, time of day and atmosphere", """A place changes with the light. Decide your **light plan:**

1. **Choose a limited set of lighting moods:** morning, midday, evening, night.
2. **Write each as a block:** “warm low sun from the left, long soft shadows, golden dust in the air.”
3. **Be consistent within a scene:** if the sun is on the left in the first shot, it remains on the left in the next.
4. **Match the character:** the hero image should be generated, or adjusted, to the scene's light. Mismatched light makes characters look pasted in.
5. **Add contact shadows** under characters in an editor.
6. **Use atmosphere** to unify: a soft haze, dust, rain, a colour tint over the whole shot, a touch of film grain.
7. **Colour-match** all shots of the same scene with your editor's colour tools.

Write the **time and light** in every shot in the shot list. A simple table with “Scene, location, time, light, props” prevents confusion later. Keep **spare variants** such as the same wide picture at dusk, prepared in advance."""),
        ("Local detail, accuracy and rights", """Authentic settings are a great strength, but you must check them:

- **Look for errors:** AI may mix styles of architecture, give the wrong number of floors, draw wrong clothing, invent a strange vehicle, or produce stereotypes of Africa that do not match your own street. **Compare with real photos you took** or with what people from the place tell you.
- **Use your own references:** photos of your neighbourhood, market and bus stop are the best guide, and they belong to you.
- **Do not copy real private places** such as someone's house, a school or a shop, in a way that identifies them, without permission.
- **Avoid real brands, logos, uniforms and signs** unless you have permission. A film with a famous soft drink label can create legal trouble. Replace them with **invented brands.**
- **Do not show real people's faces** from your photos without consent.
- **Check for hidden problems** in generated pictures: odd shapes, melted objects, text that makes no sense, weird reflections. Fix them in an editor or regenerate.
- **Record** the tool, date and prompt for every background.

When you finish, save each location folder with the sheet, master image, variants, props and notes."""),
    ],
    diagram=flow([("Location", "plan and block"), ("Wide master", "whole place"), ("Angles", "crop views"), ("Props", "cut and place"), ("Composite", "match light")], "ai10", note="Build one place, then reuse it."),
    caption="Build a location sheet, generate a wide master, create angles by cropping or using a guide, add props and composite with matching light.",
    terms=[("Location sheet", "A page that describes a place with pictures, a plan and a description block."), ("Establishing shot", "A wide view that shows the whole place."),
           ("Blockout", "A simple 3D layout made of boxes to show geometry from different angles."), ("Prop sheet", "A page showing an important object from several views."),
           ("Background plate", "A background image used behind characters."), ("Contact shadow", "A shadow under a character that makes it sit in the scene.")],
    mistakes=["Asking for the same room from several angles and hoping it stays the same.", "Letting AI write text on signs and props.", "Showing real brands and logos with no permission.", "Pasting a character into a scene with the wrong light."],
    quiz=[dict(q="What is the most reliable way to get a close-up of a place you already generated?", o=["Regenerate from scratch", "Hope the tool remembers", "Crop and enlarge the wide master with an upscaler", "Use a different style"], a=2,
               why="Cropping guarantees it is the same place."),
          dict(q="Why avoid text in generated props?", o=["It is illegal", "AI often draws gibberish letters, so add real text later", "It uses more data", "It is too small"], a=1,
               why="Image tools struggle with accurate lettering."),
          dict(q="What helps keep the geometry of a room consistent between angles?", o=["A simple 3D blockout used as a layout guide", "A longer prompt only", "A new tool each shot", "A random seed"], a=0,
               why="The same 3D shapes give the same layout from every camera."),
          dict(q="What should you do about real brand logos in your scene?", o=["Use them freely", "Replace them with invented brands", "Make them bigger", "Ignore the problem"], a=1,
               why="Using real brands without permission can cause legal problems.")],
    activity="Create a location sheet and floor plan for one place, generate a wide master picture, make three angles using crops or a simple Blender blockout, add two props cut out from separate images and check every sign, brand and detail.",
)

LESSONS[11] = dict(   # Music, sound effects and mixing audio
    minutes=16,
    hook="Turn off the sound of your favourite film scene and it loses half its power. Sound tells us where we are, what is happening off-screen and, above all, how to feel. AI music and sound tools make it easy to create a custom score and effects in minutes, even for people who cannot play an instrument. But easy does not mean automatic. Generated music may not fit your cuts, may sound generic, may carry licence limits you did not notice, and can easily drown your dialogue if you do not mix it carefully. In this lesson you will learn how to describe the music you need, how to choose and edit a track so that it fits your film, how to make or find sound effects and ambience, how to mix the four layers so every word is clear, how to work with real musicians for authenticity and, importantly, how to check the licence and credit everything honestly.",
    sections=[
        ("Decide what the film needs", """Before you generate anything, make a **sound plan** on one page:

1. **Mood by scene:** warm and playful at the start, tense in the middle, hopeful at the end.
2. **Where music starts and stops,** and where silence is better.
3. **Key sound moments:** a door slam, a drum hit, a splash, a bus horn.
4. **Ambience for each location:** market chatter, birds, rain on zinc, generator hum.
5. **Dialogue and narration spots,** where music must stay low.
6. **Length of each piece,** matching your shots.

Music should **support** the film, not decorate every second. Many strong short films use **music only in the key moments** and a simple ambience elsewhere. Listen to films you love, and write what the sound does in each scene. Be careful about relying on music to **create** emotion that the picture and story do not already have."""),
        ("Prompting and choosing music", """When you use an AI music tool, describe the music like a director briefing a composer:

> [Example music prompt]
> Instrumental, warm and playful afrobeat-inspired groove, mid tempo, light percussion, bright guitar and soft bass, 60 seconds, gentle build, no vocals, loopable ending.

Include: **mood, genre or flavour, tempo, instruments, length, structure** (intro, build, end) and **whether it needs vocals.** Then:

1. **Generate several versions,** and listen on speakers and earphones.
2. **Choose the one that fits the picture,** not the one that sounds the most impressive alone.
3. **Avoid asking for “in the style of” a living artist or a particular song,** and avoid requests for existing lyrics or melodies. Besides being unfair to artists, results can be legally risky.
4. **Check how the tool treats rights:** who owns the result, what plan you need for commercial use and whether credit is required. These rules change, so read the **current terms** and save a copy or screenshot.
5. **Keep the original files and your settings** in the use log."""),
        ("Edit the music to fit", """Generated tracks rarely fit exactly. Edit them in a free editor such as **Audacity** or your video editor:

- **Trim** the start and end to match the film's length.
- **Cut and rearrange sections** (repeat a loop, remove a boring part), using the quiet beats between phrases so the joins are smooth.
- **Fade in and out** so there are no sudden starts or stops. Use fades of one or two seconds.
- **Line up musical changes with picture changes:** a drum hit on the cut, a lift when the hero succeeds.
- **Lower the volume** under dialogue (called **ducking**) and raise it in gaps.
- **Use equalisation gently** to cut some low and mid frequencies if the music crowds the voice.
- **Make loops** for long ambience, checking that the join cannot be heard.
- **Layer stems** (separate drums, bass, melody) if the tool provides them, and adjust each.

If a generated piece has odd artefacts, such as warbles, sudden key changes or glitches, **cut those parts** or choose another version."""),
        ("Sound effects and ambience", """Effects tell the audience what happens, and ambience tells them **where.**

- **Hard effects:** a door, a bus, a coin, a splash. You can generate, record or find licensed ones.
- **Foley:** everyday sounds you record to match movement: footsteps in sandals, a bag zip, cloth rustle, a spoon in a pot. Record on a phone in a quiet room, close to the source, and clean it in Audacity.
- **Ambience:** a long, steady sound of the place. Layer **two or three** sources, for example distant traffic, nearby voices and a generator.
- **AI sound tools** can create effects from text prompts. Describe the **action, material and place:** “wooden stool dragged across a concrete floor, short.” Generate several, and pick the one that matches the picture.
- **Sync precisely.** Place each effect on the exact frame of the action. Even two frames late feels wrong.
- **Silence before an impact** makes the sound hit harder.
- **Keep a library** with clear names, such as `sfx_bus_horn_01.wav`, and note the source and licence of each file."""),
        ("Mix, authenticity and credit", """A mix balances the four layers: **dialogue, effects, ambience and music.**

1. **Dialogue first:** it must be clear in every moment.
2. **Set ambience** quietly underneath to give the place life.
3. **Add effects** at suitable levels, louder for important story sounds.
4. **Put the music** where it supports, ducking it under speech.
5. **Check for clipping,** meaning peaks that distort. Keep peaks below the maximum.
6. **Keep a consistent overall loudness.** A common online target is around **minus 14 LUFS,** but check your platform's current guidance.
7. **Test on a phone speaker, earphones and a laptop,** and listen after a break.
8. **Export a clean stereo WAV** to use in your edit.

For **authenticity,** consider working with a real musician or producer. AI trained on mostly Western data may produce a shallow imitation of African styles. A local artist can give your film a true sound, and a written agreement protects both sides. **Credit** everyone: musicians, voice actors, tools and any sound libraries, as in “Music generated with [tool name] and edited by [your name],” and record the licences in your use log."""),
    ],
    diagram=pyramid([("DIALOGUE", "always clear"), ("EFFECTS", "tell what happens"), ("AMBIENCE", "tell where we are"), ("MUSIC", "the mood underneath")], note="Mix from the voice outward."),
    caption="Four sound layers: dialogue on top, then effects, ambience and music underneath. The voice must always be clear.",
    terms=[("Ambience", "The steady background sound of a place."), ("Foley", "Everyday sounds recorded to match on-screen movement."),
           ("Ducking", "Lowering music while someone speaks."), ("Stem", "A separate part of a piece of music, such as drums or bass."),
           ("Clipping", "Distortion caused by a sound being too loud."), ("LUFS", "A unit that measures perceived loudness.")],
    mistakes=["Filling every second with music so nothing stands out.", "Asking a tool to copy a living artist's song or style.", "Letting music cover the dialogue.", "Not checking the music tool's licence for commercial use."],
    quiz=[dict(q="What belongs in a good music prompt?", o=["Only the word music", "A copy of a famous song's lyrics", "A request to copy a living artist", "Mood, genre, tempo, instruments, length and structure"], a=3,
               why="A clear brief helps the tool produce something usable."),
          dict(q="What is ducking?", o=["Recording ducks", "Lowering the music under dialogue", "Raising the picture", "A file type"], a=1,
               why="Ducking keeps the voice clear above the music."),
          dict(q="Why check the licence of a music tool?", o=["It affects who owns the result and whether commercial use is allowed", "To make the file smaller", "To change tempo", "It does not matter"], a=0,
               why="Rules differ by tool and plan, and they change."),
          dict(q="Why might you work with a real musician?", o=["It is required", "AI cannot make sound", "To get an authentic sound and an agreement about rights", "It is cheaper always"], a=2,
               why="A local artist gives real cultural depth, and a written agreement protects both sides.")],
    activity="Write a one-page sound plan for a 60-second film, generate three music options with a detailed prompt, edit one to fit with fades and ducking, record or create five effects and an ambience layer, mix them with the dialogue and write the credit line.",
)

LESSONS[12] = dict(   # Animating images: image-to-video and motion tools
    minutes=17,
    hook="A still picture of a girl by a river is lovely. The same picture, with the water moving, her scarf lifting in the breeze and the camera slowly pushing in, becomes a moment in a film. That is what image-to-video and motion tools do: they take a picture you made and create a few seconds of movement from it. It feels like magic. Then you discover the limits: the face melts, the hands grow extra fingers, the character walks backward, and the clip lasts only five seconds. This lesson teaches you to work with these tools like a director and not a gambler. You will learn how the tools work, how to write a motion prompt, how to keep movements simple so the tools can handle them, how to try, compare and refine, how to stitch clips into longer shots, how to hide weaknesses with design and editing, and how to check every clip frame by frame.",
    sections=[
        ("How image-to-video tools work", """In most tools, you give the system a **starting image** and a **text prompt** that describes the motion and the camera. The tool then generates a short clip, often **3 to 10 seconds,** in which your image appears to come alive. Some tools also accept an **end image,** so that the clip moves from one picture to another. Others can use a **reference video** for movement.

What these tools are good at:

- **Atmosphere:** moving clouds, water, smoke, fire, rain, leaves, light.
- **Slow camera moves:** push in, pull out, pan, gentle orbit.
- **Simple character actions:** turning the head, blinking, smiling, small gestures, hair and clothes moving in wind.

What they are weak at:

- **Fast or complex action:** fights, dances, crowds.
- **Hands and fine details.**
- **Long, continuous actions.**
- **Consistency:** the face or clothes may change during the clip.
- **Physics:** objects can pass through each other.
- **Text and logos.**

Understanding these limits lets you **plan shots that the tool can succeed at.**"""),
        ("Prepare a good starting image", """The quality of the clip depends on the quality of the first picture.

1. **Use a clean, high-resolution image** with clear shapes, in your style and aspect ratio (for example 16:9).
2. **Leave room for the motion:** if the camera will push in, do not put the face at the edge. If a character should walk, leave space in front.
3. **Keep it simple:** fewer characters and details mean fewer errors.
4. **Check the picture first:** fix hands, eyes and strange objects before animating. Problems in the still will get worse in motion.
5. **Separate the foreground from the background** if you want finer control. Some tools or editors let you animate layers differently.
6. **Name the file clearly,** such as `s04_riverbank_start_v02.png`, and keep the original.

If you plan to join two clips, prepare **end pictures** too, or plan to use the **last frame** of one clip as the **first frame** of the next. You can export a frame from a video in your editor and use it as the next starting image."""),
        ("Write a motion prompt", """A good motion prompt is short, concrete and describes only **what moves and how the camera behaves.** A simple formula:

> [Motion prompt formula]
> Subject + one action + camera move + atmosphere + what must not change

Example: “The girl slowly turns her head toward the river and smiles. The camera pushes in gently. The water ripples and her scarf lifts in a light breeze. Her face, clothes and style stay the same.”

Tips:

- **One action per clip.** Two or three actions confuse the tool.
- **Use slow, simple verbs:** turns, blinks, breathes, drifts, flows.
- **Name the camera move** in plain words: slow push in, gentle pan left, static camera.
- **State what should stay still:** “background remains still.”
- **Avoid vague words** such as “epic” and “amazing.”
- **Describe speed:** slow, gentle, steady.
- **Do not ask for text, logos or rapid cuts** inside one clip.
- **Keep a prompt library:** save every prompt that worked and what it did."""),
        ("Try, compare and refine", """Treat each shot as a loop:

1. **Generate** two to four versions of the same prompt, since results vary.
2. **Review** each clip, in full and **frame by frame.** Look at faces, hands, edges and objects. Check the first and last second especially.
3. **Choose** the best, or note what failed.
4. **Adjust** the prompt or the starting image: simplify the action, change the camera, or fix the picture.
5. **Repeat** only a few times. If a shot keeps failing after about **five tries,** change the shot. Make it simpler, use a different angle, or use another method.

Control your **budget:** many tools charge credits for every generation, including the failures. Plan **about 3 tries per shot,** and total clip time. If your film has 12 shots of 4 seconds each, you need about 36 attempts. Decide in advance which shots matter most and spend more tries there. Keep every good clip, with its prompt, tool and date, in a labelled folder."""),
        ("Stitching, hiding weaknesses and alternatives", """To make longer, better films:

- **Use short shots.** Real films usually cut every 2 to 5 seconds, so a 4-second clip is often enough. Cutting hides many weaknesses.
- **Chain clips** by using the last frame of one as the first of the next, and cut on a movement.
- **Speed up or slow down** a clip in your editor to fit, and use a **gentle crop or zoom** to improve framing.
- **Hide faults:** cover a glitch with a cut, a close-up of an object, a reaction shot or a transition.
- **Use limited animation as a style.** Slow camera moves over stills, with small movements, can look beautiful and are cheaper and more reliable than full motion.
- **Use free 2D parallax:** separate your picture into layers (background, middle, character), and move each layer at a different speed in a video editor. It makes a still feel deep, with no AI risk.
- **Combine with hand work:** animate key parts yourself, such as a blink, in a free 2D tool.
- **Clean up:** use an upscaler or noise remover carefully, and check that they do not change faces.
- **Disclose AI use** and keep your use log.

The goal is not to avoid AI or to rely on it fully, but to **design shots the tools can deliver** and use your own craft for the rest."""),
    ],
    diagram=cycle([("Prompt", "one action, one move"), ("Generate", "2 to 4 versions"), ("Review", "frame by frame"), ("Adjust", "simplify or fix")], "ai12", center="One shot|loop", note="After about five tries, change the shot."),
    caption="Each shot is a loop: prompt, generate, review frame by frame and adjust. If it keeps failing, redesign the shot.",
    terms=[("Image-to-video", "A tool that turns a still picture into a short moving clip."), ("Motion prompt", "A short text that describes how things move and how the camera behaves."),
           ("End frame", "A picture that tells the tool how the clip should finish."), ("Last-frame chaining", "Using the last frame of one clip as the first frame of the next."),
           ("Parallax", "A depth effect made by moving layers at different speeds."), ("Credits", "Points a tool charges for each generation.")],
    mistakes=["Asking for several complex actions in one clip.", "Animating a starting image that already has errors in the hands or face.", "Trying the same failing shot twenty times instead of changing it.", "Not checking clips frame by frame for glitches."],
    quiz=[dict(q="How many main actions should a motion prompt contain?", o=["One", "Ten", "As many as possible", "None"], a=0,
               why="One simple action is much more likely to work well."),
          dict(q="What should you do if a shot fails after about five tries?", o=["Keep trying forever", "Give up the film", "Simplify or redesign the shot", "Remove the prompt"], a=2,
               why="Changing the shot saves credits and time."),
          dict(q="Which is a cheap, reliable alternative to AI motion?", o=["Deleting the clip", "Using a different font", "Adding more characters", "Moving layers at different speeds in an editor (parallax)"], a=3,
               why="Layer motion needs no AI and gives depth to still images."),
          dict(q="Why check clips frame by frame?", o=["Because the tool requires it", "To find glitches in faces, hands and edges", "To increase length", "To change colour"], a=1,
               why="Short glitches can slip past a quick viewing.")],
    activity="Choose three shots, prepare clean starting images, write one-action motion prompts, generate two to four versions of each, review them frame by frame, chain two clips using the last frame and make one parallax shot with layers.",
)

LESSONS[13] = dict(   # Shot planning, editing and colour
    minutes=16,
    hook="When your clips come from AI tools, you meet a problem that traditional animators rarely face: every clip is a little different. One has warmer colour, another is sharper, a third has a slightly different face. Cut them together carelessly, and the film feels like a slideshow of unrelated experiments. The solution is the oldest craft in filmmaking: careful shot planning before you generate, and careful editing and colour work after. A good plan means you ask the tools only for shots that the story needs. A good edit hides weaknesses, controls rhythm and turns a pile of clips into a film. A good colour pass makes different clips match. In this lesson you will build a shot list with sizes and lengths, learn the cutting rules that make edits feel natural, assemble the film in a free editor, match and grade colour across clips, add titles, subtitles and finishing touches and export properly.",
    sections=[
        ("Plan the shots before you generate", """A **shot list** is a table that describes every shot. For each shot, write:

- **Shot number and scene.**
- **Size:** wide, medium or close-up.
- **What we see:** the action in one sentence.
- **Camera:** still or moving, and how.
- **Length:** in seconds, for example 3.5.
- **Sound:** dialogue, music or effects.
- **Source:** AI clip, 2D animation, 3D render or still with parallax.
- **Status:** planned, generated, approved, edited.

Plan for **variety:** a wide shot to show the place, mediums for action and close-ups for emotion. A 60-second film with an average shot length of 4 seconds needs about 15 shots. Mark the **three most important shots** that deserve extra tries, and the **easy shots** that can be simple. Plan **cut points:** where one shot ends, the next should begin, with a clear reason. **Fewer, better shots** beat many mediocre ones. Match your list to the **animatic** you made earlier, and update it as you learn."""),
        ("Cutting rules that make edits feel natural", """Simple principles from film editing:

1. **Cut on action:** change shots in the middle of a movement, such as a hand reaching, so the eye follows.
2. **Vary the shot size:** avoid two similar shots in a row. Cut from wide to medium or close-up.
3. **Keep screen direction:** a character moving left to right should continue that way in the next shot, unless you show a change.
4. **The 180-degree rule:** keep the camera on one side of the line between two characters.
5. **Let important moments breathe:** hold a reaction for a beat.
6. **Cut when the viewer has understood,** and not later. Short shots keep energy.
7. **Match the rhythm to the music,** cutting on beats or phrase endings.
8. **Use J-cuts and L-cuts:** let the sound of the next shot begin **before** the picture (J-cut), or the sound of the previous shot continue **after** the picture changes (L-cut).
9. **Use transitions sparingly:** a cut is normal. A dissolve suggests time passing.
10. **Hide glitches:** if a clip has a bad last second, **cut before it.**

With AI clips, **trim the first and last few frames,** where most glitches appear, and cut away from faces that start to distort."""),
        ("Assemble in a free editor", """Use a free editor such as **DaVinci Resolve, Kdenlive or Shotcut** (check current licences and features).

1. **Create a project** with the same **frame rate and resolution** as your final film, for example 24 fps and 1920 by 1080. If a clip has a different rate or size, the editor can convert it, but check the result.
2. **Import** the clips, sound and images into labelled **bins or folders.**
3. **Rough cut:** place the clips in order on the timeline, trimming the start and end.
4. **Add the sound:** dialogue first, then ambience, effects and music on separate tracks.
5. **Refine the timing:** adjust the length of each shot until the rhythm is right.
6. **Fix problems:** speed changes, zoom crops, stabilisation, **freeze frames** for a stronger pause.
7. **Add transitions** where needed.
8. **Watch the whole film** at full speed, and take notes. Repeat.
9. **Save versions** (`film_v03.drp` or similar), and back up the project **and** the media.

Keep the **media files** in a stable folder. If you move them later, the editor may lose the links."""),
        ("Match colour across clips", """Colour work has two jobs: **correction** (making clips match) and **grading** (creating a mood).

1. **Start with a neutral look:** adjust exposure, contrast and white balance for each clip, so that whites look white and blacks look black. Use **scopes** (waveform, histogram, vectorscope), because screens and eyes can mislead.
2. **Match to a reference clip:** pick the best-looking shot of the scene as your reference, and adjust the others to match its brightness and colour. Compare two shots **side by side** (split screen).
3. **Fix skin tones:** make sure the hero's skin looks natural and consistent. Be respectful of all skin colours, and avoid washing out or over-saturating.
4. **Apply a gentle overall grade:** a warm look for the market, cooler for the night scene. Do not overdo it.
5. **Unify with texture:** a soft **film grain** or a light overlay can hide small differences between clips.
6. **Keep the palette:** push colours towards your style guide.
7. **Check on a phone** and a different screen.

Some editors have **colour match tools** and **LUTs** (preset looks). They are good starting points, but always check by eye. Use only LUTs and presets you have the right to use."""),
        ("Titles, subtitles and the final pass", """Finishing touches:

- **Title and credits:** a clear, simple font that you have the licence for, inside the **safe area.** Keep it short.
- **Credits should list** everyone: voice actors, musicians, helpers and **the tools used,** including AI tools and the parts they helped with.
- **Subtitles:** add them for different languages, noisy places and deaf viewers. Check spelling carefully, especially names. Keep lines short and in sync, and consider exporting an **SRT file** too.
- **Upscale and denoise** if necessary, but compare before and after.
- **Final checks:** play the film from start to finish, with sound, on a computer and a phone. Check for black frames, flicker, missing sound, wrong speed and cut-off text.
- **Export:** keep a **master** (high quality) and make **delivery copies:** an **MP4 (H.264) at 1080p,** a lighter **720p version** for WhatsApp and a vertical or square cut if you plan social posts.
- **Name files clearly,** such as `MyFilm_v05_1080p24.mp4`.
- **Archive** the project, clips, prompts and use log.

A careful edit and colour pass is what turns generated clips into a film that feels **intentional.**"""),
    ],
    diagram=tree("SHOT LIST", [("Wide shots", ["Show the place", "Show scale"]), ("Medium shots", ["Show action", "Show dialogue"]), ("Close-ups", ["Show emotion", "Show a key detail"])], note="Vary the size, then cut on action."),
    caption="A shot list mixes wide shots for the place, medium shots for action and dialogue and close-ups for emotion and detail.",
    terms=[("Shot list", "A table that describes every shot in the film."), ("Cut on action", "Changing shots in the middle of a movement so the edit feels smooth."),
           ("J-cut and L-cut", "Edits where sound and picture change at different times."), ("Colour correction", "Adjusting clips so they look natural and match each other."),
           ("LUT", "A preset that applies a colour look to a clip."), ("Master", "The highest quality export, used to make smaller copies.")],
    mistakes=["Generating clips before planning the shots.", "Cutting clips together without matching their colour.", "Keeping the glitchy last second of an AI clip.", "Exporting only one small compressed file and losing the master."],
    quiz=[dict(q="What is a shot list?", o=["A table describing each shot's size, action, camera, length and source", "A list of tools", "A music playlist", "A password list"], a=0,
               why="It plans the film so that you only generate shots you need."),
          dict(q="Why match colour across AI clips?", o=["Clips from different generations often look different", "It makes the file smaller", "It adds sound", "It is a legal rule"], a=0,
               why="Matching makes separate clips feel like one film."),
          dict(q="What is a good way to hide a glitch at the end of a clip?", o=["Make it longer", "Add more effects", "Zoom into the glitch", "Cut before it or cut away"], a=3,
               why="Trimming and cutting away keeps viewers from noticing."),
          dict(q="What is a J-cut?", o=["A cut that deletes sound", "The next shot's sound starts before the picture changes", "A colour filter", "A title style"], a=1,
               why="J-cuts and L-cuts make scenes flow by overlapping sound and picture.")],
    activity="Create a full shot list for your film with size, length, camera and source for each shot, assemble your clips in a free editor, match the colour of three clips to a reference shot with scopes, add titles with credits and subtitles, and export a master and a 720p copy.",
)

LESSONS[14] = dict(   # Ethics, copyright and crediting AI work
    minutes=16,
    hook="You are making a film with tools that learned from millions of pictures, voices and songs made by other people. You did not ask those people, and in most cases the tool's company did not ask them either. Is that fair? Who owns the pictures you generate? Can you sell your film? What should you tell your viewers? These are real questions, and serious people disagree about the answers. You cannot wait for perfect answers, so you need a way of working that is honest, careful and fair, one you can explain to a client, a teacher, a festival or a stranger. This lesson gives you practical habits: how to read terms and licences, how to think about copyright and ownership, how to treat people's faces, voices and cultures, how to disclose and credit AI work, how to keep a use log and how to handle problems if they arise. This is education, not legal advice.",
    sections=[
        ("The questions people are asking", """It helps to understand the main debates, so you can speak about them fairly:

- **Training data:** many AI tools learned from huge collections of images, text, music and video, often collected from the internet. Some creators say this used their work **without permission or payment.** Companies and some lawyers argue the training is allowed under existing rules, while others say new rules are needed. Courts and lawmakers in different countries are still deciding. Some tools say they use licensed or permitted data. Read each company's statements and form your own view.
- **Ownership of the output:** in several countries, copyright protects work with **human authorship,** so purely machine-generated pictures may have weak or no protection, while work in which a person makes real creative choices (writing, selecting, editing, painting over) may be protected for those parts. This is changing.
- **Jobs and fairness:** artists, voice actors and musicians worry about lost work. Others see new opportunities.
- **Honesty:** audiences want to know what is real, especially with realistic images and voices.
- **Bias and culture:** tools reflect their training data, so they may misrepresent African people and places.

You do not have to solve these debates. You do have to **act carefully** while they continue."""),
        ("Terms, licences and ownership in practice", """For each tool and each result:

1. **Read the terms** that apply to your plan: who owns outputs, whether **commercial use** is allowed, whether **credit** is required, what is forbidden, and what happens to your uploads. Take a **screenshot or save a copy** with the date, since terms change.
2. **Check your plan:** free and paid plans may have different rights. A free plan may forbid commercial use, require credit or add watermarks.
3. **Check the inputs:** you may only upload images, voices and music that you own or have permission to use. A tool's terms do not give **you** rights over other people's material.
4. **Check the outputs for copies:** if a result closely resembles a known character, artwork, logo or song, **do not use it.** Generate again, or make your own.
5. **Do not use the name of a living artist** as a prompt to copy their style.
6. **Keep records:** prompts, dates, tool, plan, settings and your edits.
7. **Know the law of your country.** In Nigeria, copyright is governed by the **Copyright Act** (the 2022 Act at the time of writing), and its treatment of AI-made work may develop. **Ask a lawyer** if you will sell or license your film, or if a dispute arises.
8. **Add your own creative work,** such as writing, design, painting, editing and sound. This strengthens both your claim and your craft."""),
        ("People: faces, voices and communities", """Real people are affected by what you make:

- **Likeness:** do not create pictures or videos of a real person, famous or not, doing or saying things they did not do. **Deepfakes** can harm reputations and can be illegal.
- **Voices:** never clone someone's voice without clear, written permission, and tell them how it will be used.
- **Photos you upload:** get permission from everyone shown, and **extra care for children,** whose images should not be uploaded to tools without a parent's or guardian's consent and a very good reason.
- **Personal data:** under **Nigeria's NDPA 2023** and similar laws, personal data such as names, faces and voices needs care. Collect only what you need, explain why and let people withdraw.
- **Communities and culture:** if your film shows a community's traditions, dress, stories or sacred symbols, **consult people from that community,** and credit them. Avoid stereotypes and false details.
- **Performers:** if human actors work on your film, agree in writing about pay, credit and how their work may be used. Do not use their recordings to train or clone voices unless they agree.
- **Fairness to artists:** where you can, **hire and credit human artists,** and avoid using AI only to undercut their pay."""),
        ("Disclose and credit honestly", """Honesty builds trust. How to credit AI work:

- **Add a credits line** such as: “Images created with AI assistance, then edited and composed by [your name]. Voices performed by [names]. Music by [name/tool].”
- **Be specific,** naming the **parts** that used AI (backgrounds, motion, music) and your own contribution.
- **Name the tools,** and keep a **licence list.**
- **Follow platform rules.** Many video and social platforms ask you to **label realistic AI-generated or altered content,** and their rules change. Read the current policy before you upload.
- **Tell clients early** which parts will use AI, and agree in writing.
- **Do not claim** hand-made work that was generated, or enter AI-assisted work in a contest that forbids it. Read each contest's rules.
- **Respond to questions openly,** and be ready to share your process.

A sample **use log** table has these columns: shot or asset, tool and version, plan, date, prompt, settings, your edits, licence notes. Fill it as you work, because trying to remember later is almost impossible."""),
        ("When something goes wrong", """Even with care, problems can arise:

1. **A complaint or takedown notice:** stay calm. Read it carefully. Do not ignore it. Check your records. If it seems fair, remove or replace the material quickly. If you disagree, seek advice from a lawyer or a trusted organisation.
2. **A resemblance claim:** keep your prompts, dates and process. Show your own creative steps. Replace the part in question if in doubt.
3. **A person objects to their image or voice:** remove it and apologise.
4. **A tool changes its terms or closes:** keep local copies of your work and your records, and check whether your rights continue.
5. **A mistake is found in your film:** correct it, say so publicly if needed and learn.
6. **A dilemma you cannot solve:** ask a teacher, a mentor, a community of creators or a lawyer, **before** you publish.

Ask yourself three questions before releasing anything: **Is it true to what I did? Is it fair to the people involved? Would I be comfortable explaining it to the people it affects?** If the answer is yes, you are on solid ground."""),
    ],
    diagram=rings(["Law and platform rules", "Tool terms and licences", "Consent from real people", "Your use log and credits", "YOUR FILM"], note="Each layer protects the one inside."),
    caption="Layers that protect a film: law and platform rules, tool terms, consent from people, and your own use log and credits.",
    terms=[("Training data", "The material an AI system learned from."), ("Human authorship", "Creative work made by a person, which many copyright laws require for protection."),
           ("Deepfake", "A fake image, video or audio that makes a real person seem to say or do something they did not."), ("Disclosure", "Telling others that AI was used and how."),
           ("Use log", "A record of tools, prompts, plans, dates and edits for each asset."), ("Takedown notice", "A formal request to remove material that may break someone's rights.")],
    mistakes=["Assuming a tool's terms give you rights over material you upload.", "Cloning a real person's voice without written permission.", "Hiding AI use from a client or contest that asked for original work.", "Ignoring a complaint instead of checking your records and responding."],
    quiz=[dict(q="What does a use log record?", o=["Only the final export", "Tools, plans, prompts, dates and edits for each asset", "Social media followers", "Computer temperature"], a=1,
               why="Records help you prove how work was made and what rules applied."),
          dict(q="What should you do before uploading a photo of someone to an AI tool?", o=["Nothing", "Post it first", "Get their permission, and extra care for children", "Change the file name"], a=2,
               why="People have rights over their image and personal data."),
          dict(q="Why add your own creative work to AI-assisted material?", o=["It strengthens your claim and your craft", "It makes the tool free", "It removes the need for credits", "It avoids all rules"], a=0,
               why="Human creative choices matter for ownership and quality."),
          dict(q="What is a good first reaction to a takedown notice?", o=["Delete all your files", "Ignore it", "Argue publicly", "Stay calm, read it, check your records and respond"], a=3,
               why="A calm, careful response protects you and the other person.")],
    activity="Write a credits line and a use log template for your film, read the terms of one tool you use and note ownership, commercial use and upload rules, and write your three-question ethics check on a card.",
)

LESSONS[15] = dict(   # Final project: release your AI short film
    minutes=17,
    hook="This is the moment to bring everything together and put a finished film into the world. In this final project you will make a short AI-assisted animated film of about 45 to 90 seconds, and release it with a credits card, a use log, a poster and a short behind-the-scenes post. The film itself matters, but so does the way you work. You will plan the story, build a project bible, write and time the script, record real voices, design the characters and places, generate and animate shots, edit, colour and mix, and check every step for rights and honesty. Remember that a tool is not a team, and a pile of clips is not a film. Your decisions turn the first into the second. You will use a clear schedule, checkpoints and a rubric, and you will end with a film that you can show proudly in your portfolio.",
    sections=[
        ("The brief", """**Make an original 45 to 90 second AI-assisted animated short film** with these requirements:

- **A clear story:** hook, a want, a conflict with stakes, and a satisfying ending, in your own words and decisions.
- **A project bible:** logline, script, character sheet, style guide with palette, location sheets and prop sheets.
- **Real human input:** at least one of: **real recorded voices,** hand-drawn or hand-made elements, a real musician, or your own photos and sounds. The film should show your own craft.
- **AI used carefully:** for chosen parts, such as backgrounds, motion or music, with **terms and licences checked** and recorded.
- **Consistency:** the character and style should hold together across shots.
- **Sound:** clear dialogue or narration, music, effects and ambience, properly mixed.
- **Finish:** edited, colour-matched, with titles, credits and subtitles, exported as an MP4 (1080p) and a 720p copy.
- **Ethics pack:** a credits line, a use log and a short note on how you handled rights.

**Idea examples:** a tortoise who wants to win the market's yearly race. A girl who finds a drum that plays memories. A bus conductor who sees a sleeping lion in his rear mirror. Keep it **small, clear and doable.**"""),
        ("A four-week schedule", """Work backward from your release date. A part-time learner can use **four weeks:**

**Week 1: Plan**
- Day 1 to 2: idea, logline, structure with hook, conflict and ending.
- Day 3 to 4: script and timing, dialogue check with speakers.
- Day 5 to 7: character sheet, style guide, location sheets, shot list, animatic with rough sound.

**Week 2: Create assets and voices**
- Day 8 to 10: record voices, music plan, test the tools on a 5-second mini film.
- Day 11 to 14: generate and approve characters, backgrounds and props.

**Week 3: Generate and animate**
- Day 15 to 19: generate and animate shots, prioritising the key ones, with prompts logged.
- Day 20 to 21: fill gaps, hide weaknesses with edits and parallax.

**Week 4: Finish and release**
- Day 22 to 23: edit, colour and mix.
- Day 24: titles, credits, subtitles, ethics pack.
- Day 25 to 26: export, checks and a **buffer** for problems.
- Day 27 to 28: release, share and reflect.

Add **25% extra time** to every estimate, and **back up every day.**"""),
        ("Checkpoints and quality control", """Put a **checkpoint** after every stage. Do not move on until it passes.

1. **After the script:** read it aloud and time it. Does it tell the story in the target length?
2. **After the animatic:** show it to two people. Do they understand it?
3. **After the style test:** do five different shots look like one film?
4. **After the voice recording:** are the voices clear, correctly pronounced and permitted?
5. **After each batch of shots:** check faces, hands, text and glitches frame by frame.
6. **After the edit:** watch with sound off, and with sound on. Does the story still work?
7. **After the sound mix:** listen on a phone speaker and earphones.
8. **After the colour pass:** compare clips side by side.
9. **Before release:** run the **ethics check:** terms and licences read? permissions held? people respected? credits accurate? use log complete?
10. **After export:** watch the file from start to finish on two devices.

Keep a **production diary:** one line each day on what you did, what failed and what you learned. It will help you write your reflection."""),
        ("Test with viewers and use the rubric", """Judge your film with a rubric like this:

- **Story and clarity (20%):** hook, want, conflict and ending.
- **Craft and consistency (20%):** consistent characters and style, clean shots.
- **Human voice and decisions (15%):** your own creative choices and real human input.
- **Sound (15%):** clear dialogue, balanced mix, licensed music.
- **Editing and colour (10%):** rhythm, matched colour, no glitches.
- **Ethics and rights (15%):** terms checked, permissions, honest credits and a complete use log.
- **Finish and delivery (5%):** correct export, subtitles and credits.

Show the film to **three viewers** who have not seen it. Ask what happened, how they felt, which moment they liked and where they were confused. Look for patterns, and fix the **top two problems.** Do not rebuild everything at the last minute. If a shot is weak, cut it, shorten it or hide it with a good edit."""),
        ("Release and keep growing", """When the film is ready:

- **Upload** to a video platform, with a clear title, a short description, subtitles and **credits.** Follow the platform's **AI-content labelling rules.**
- **Publish the ethics pack:** a short note about how AI was used, the tools and your own contribution.
- **Make a poster or thumbnail** with a striking frame from the film, in your style.
- **Share a short clip** on social media, plus a behind-the-scenes post that shows your sketches, animatic and process. Ask for feedback politely.
- **Add it to your portfolio** with a project page and your use log summary.
- **Submit to festivals or challenges** that accept AI-assisted work, after reading their rules.
- **Reply to comments** and thank those who helped.
- **Write a reflection:** what worked, what failed, what you would change and what you learned about tools, story and ethics.
- **Choose your next step:** a longer film, a series, a client project or learning a new craft such as 2D or 3D animation.

You have planned, made, checked and released a complete film, with honesty and craft. Keep your records, keep learning and keep telling your stories."""),
    ],
    diagram=timeline([("Plan", "story and bible"), ("Voices and assets", "characters, places"), ("Generate", "shots and motion"), ("Edit and mix", "cut, colour, sound"), ("Ethics check", "rights and credits"), ("Release", "share and reflect")], note="Four weeks, checkpoints at every stage."),
    caption="From plan to assets, generation, editing and mixing, an ethics check and release: the path of your AI short film.",
    terms=[("Brief", "A short description of what the project must include."), ("Project bible", "A folder with the story, characters, places, style and notes of a film."),
           ("Checkpoint", "A moment to review and approve a stage before moving on."), ("Rubric", "A list of criteria used to judge the project."),
           ("Ethics pack", "A set of notes on rights, permissions, credits and use of AI."), ("Buffer", "Extra time in a schedule for problems.")],
    mistakes=["Choosing a story that is too big for 90 seconds.", "Skipping the 5-second mini film test of the tool chain.", "Leaving the ethics check and credits to the last hour.", "Releasing without labelling AI use according to the platform's rules."],
    quiz=[dict(q="How long should the final film be?", o=["About 45 to 90 seconds", "Ten minutes", "Two hours", "Five seconds only"], a=0,
               why="A short film is finishable and shows your skills."),
          dict(q="Why test the tool chain on a 5-second mini film first?", o=["Rules require it", "To find problems cheaply before committing", "To make tools free", "To skip the plan"], a=1,
               why="Problems are cheaper to find on a tiny test."),
          dict(q="What belongs in the ethics pack?", o=["Only the poster", "The tool's logo", "Credits, permissions, tool terms checked and a use log", "Nothing"], a=2,
               why="It shows honest, careful work and protects you."),
          dict(q="What should you do before release?", o=["Run the ethics check and watch the export on two devices", "Delete the project", "Hide AI use", "Skip subtitles"], a=0,
               why="A final check catches mistakes in rights, credits and quality.")],
    activity="Complete a 45 to 90 second AI-assisted short film following the four-week schedule, with a project bible, real human input, checked licences, a use log and credits, then release it with a poster, a behind-the-scenes post and a short reflection.",
)
