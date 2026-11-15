"""AI Animation and Storytelling: deep lesson pages 1 to 5.
Category level only: no product names, prices or free-tier numbers, because those change every month.
Same format as lessons_animation.py. Quiz "a" = index of the right option."""
from diagrams import curve, grid, hub, compare, cycle

LESSONS = {
    1: dict(
        minutes=14,
        hook="Think of the moonlight tales that grandmothers tell: a clever tortoise, a greedy king, a river that talks. Nobody gave her a software tool, yet every child sat still until the end, because the story had a hero who wanted something, trouble that got in the way, and an ending that changed things. AI can now write, draw and animate for you, but it cannot decide what is worth saying. If the story is weak, the most expensive tool will only make a weak story look polished. This lesson teaches the story skills first, and shows how to use AI as a writing partner that you direct, not a machine that directs you.",
        sections=[
            ("The logline: your whole film in one sentence", """A **logline** is one sentence that tells you who the story is about, what they want, what stands in the way and what is at risk. If you cannot write it, you are not ready to generate anything. A reliable formula is:

> When [something happens], a [character] must [goal] before [stakes], but [obstacle].

A worked example: "When the generator breaks on the night of her exam, a 12-year-old girl in Lagos must find a way to study before sunrise, but every neighbour's light is also out." It has a character (the girl), a goal (study), a clock (before sunrise), stakes (the exam) and an obstacle (no light).

Test your logline with three questions. Can a stranger picture the hero? Is there a clear goal? Is there a real obstacle? Write five different loglines before you choose one. The first idea is rarely the best one, and a few minutes here saves days of generating the wrong film."""),
            ("Three acts for a short film", """Most stories follow **three acts**: a beginning (setup), a middle (trouble and struggle) and an end (climax and resolution). For a 60-second film, a practical plan is:

> **Setup (10 seconds):** meet the hero and the normal world.
> **Trouble (15 seconds):** something goes wrong and the hero has a goal.
> **Struggle (20 seconds):** the hero tries, fails, and tries again, getting closer.
> **Climax (10 seconds):** the biggest moment, where the hero wins, loses or chooses.
> **Ending (5 seconds):** one last image that shows what changed.

Add them up: 10 + 15 + 20 + 10 + 5 = 60 seconds. At 24 fps that is 1,440 frames, so you can see why every second must earn its place. Short films have no room for long introductions. Start as late as possible, close to the trouble. Each beat should change something. If a scene can be removed and the story still works, remove it."""),
            ("AI as your writing partner", """Text-based AI tools are good at generating options quickly and bad at knowing what is true to your life. Use them for:

- **Brainstorming:** ten loglines, twenty character names, five possible endings.
- **Rewriting:** shorter dialogue, a different tone, a clearer action line.
- **Checking structure:** "Where does the hero's goal become clear? Where is the climax?"

Do not use them to replace your taste, your local detail or your voice.

A strong prompt has five parts: **role, context, task, limits and format**. Example: "You are a story editor for children's animation. My film is 60 seconds long, set in a Lagos compound, for ages 6 to 10. Give me 8 loglines. Each must be one sentence, with a clear obstacle, and no magic. List them as a numbered list." Then pick two you like, ask for a mix, and rewrite the result in your own words. Treat the first answer as a rough draft. Ask follow-up questions to push it further, such as "make the obstacle bigger" or "make the ending less obvious"."""),
            ("Writing a script that can be animated", """A film script is different from a story. It only includes what the audience can **see and hear**. You cannot film a thought. Instead of "she is worried", write "she checks the clock, again, and bites her lip".

The basic format has three elements:

> **SCENE HEADING:** INT. COMPOUND KITCHEN, NIGHT
> **Action line:** Ada sits at a small table. A candle flickers. She turns a page, but the words are too dark to read.
> **Dialogue:** ADA: (whispering) Please, NEPA, just for one hour.

Keep action lines short and visual, one idea each. A page of this format is about one minute of film, so a 60-second short is about one page. Keep dialogue even shorter, because voices cost time and every spoken line must be recorded or generated and then lip-synced. Where a picture can say it, use the picture. Ask yourself of each line: could we show this instead of saying it?"""),
            ("Review it and keep it yours", """Before you move on, test the script with this checklist:

1. Does the hero **want** something we can see?
2. Is there a **choice** or a struggle, not just things happening to the hero?
3. Does the ending **change** something, such as the hero's situation or understanding?
4. Is there at least one **specific local detail** that only you would know, such as a danfo, a generator or a market stall?
5. Could a six-year-old follow it without a narrator explaining?

Then read it aloud and time it. Reading speed is a good guide to screen time.

Finally, keep a simple **story bible**: a one-page file with the logline, character names, ages, locations and the rules of your world. You will paste from it into prompts in every later lesson. Remember that you are responsible for the final work. Do not copy another writer's script or paste someone else's work into an AI tool and pass the result off as new. Use AI to find ideas, then own the choices."""),
        ],
        diagram=curve([("Setup", 0.2), ("Trouble", 0.45), ("Struggle", 0.7), ("Climax", 1.0), ("Ending", 0.3)], note="Tension rises through the middle, peaks at the climax, then settles", ylabel="Tension"),
        caption="A short film's tension rises through the struggle, peaks at the climax and settles in the ending.",
        terms=[("Logline", "A one-sentence summary of the hero, the goal, the obstacle and the stakes."), ("Three acts", "A story shape with a beginning, a middle and an end."),
               ("Beat", "One important story moment that changes something."), ("Prompt", "The instruction you give to an AI tool."),
               ("Action line", "A script line that describes only what can be seen or heard."), ("Story bible", "A one-page reference with your characters, places and rules."),
               ("Stakes", "What the hero stands to lose if they fail.")],
        mistakes=["Starting to generate pictures before the logline and the ending are clear.", "Accepting the first answer from the AI tool without asking for options or changes.",
                  "Writing thoughts and feelings in the action lines, which cannot be filmed.", "Using generic settings instead of specific local details that make the film yours."],
        quiz=[dict(q="What should a good logline include?", o=["Only the hero's name", "The full script", "The music choice", "A character, a goal, an obstacle and the stakes"], a=3, why="A logline names who the story is about, what they want, what stands in the way and what is at risk, all in one sentence."),
              dict(q="A 60-second short has beats of 10, 15, 20, 10 and 5 seconds (setup, trouble, struggle, climax, ending). Which part is the longest?", o=["Setup", "Trouble", "Struggle", "Ending"], a=2, why="The struggle gets 20 seconds, the most of any beat, because the hero tries, fails and tries again."),
              dict(q="What is the best way to use an AI writing tool?", o=["Ask once and use the first answer", "Ask for several options, pick and combine, then rewrite in your own voice", "Let it write everything without reading it", "Paste another writer's script and change the names"], a=1, why="AI is best at producing options quickly. You choose, combine and rewrite, so the story stays yours."),
              dict(q="What belongs in an animation script's action lines?", o=["Only what can be seen or heard", "What a character secretly thinks", "The budget", "The brand of the camera"], a=0, why="Film shows pictures and sounds. A thought has to be turned into something visible, such as a look or an action.")],
    ),
    2: dict(
        minutes=15,
        hook="On a film set, a director can shout \"go again\" and the actors repeat the scene. AI lets you \"go again\" too, but every attempt costs time, data and patience, and on a slow connection one bad batch can eat an afternoon. That is why professionals never start by generating. They first decide, on paper, exactly which shots they need, and only then do they generate. This lesson turns your script into a shot list, teaches the one prompt formula that works for nearly every image or video tool, and shows how to move from a still picture to a short moving clip without wasting your attempts.",
        sections=[
            ("From script to shot list", """A **shot** is one continuous piece of film, from one camera view, with no cut. A **shot list** is a table that breaks your script into shots. Each row needs five things: the shot number, the **size** (how close), the **angle** (from where), the action, and the length in seconds.

> 1 | Wide | Eye level | Ada's compound at night, one candle in a window | 4 s
> 2 | Medium | Eye level | Ada at the table, turning a page | 4 s
> 3 | Close-up | Eye level | Her eyes, struggling to read | 3 s
> 4 | Close-up | Low | The candle flame shrinking | 3 s

Do the arithmetic: 60 seconds divided by an average of 4 seconds per shot gives about **15 shots**. Most modern films cut often, so shots of 2 to 6 seconds are normal. Your list tells you exactly how much you need to generate, so you can plan your time and your data."""),
            ("Shot sizes, angles and moves", """These small choices carry the emotion of the story.

**Size:** a **wide** shot shows the place and where the hero is in it. A **medium** shot shows the body and is good for action and dialogue. A **close-up** shows a face or an object, and it is the shot for feelings. An **extreme close-up** shows a tiny detail, such as an eye or a hand.

**Angle:** **eye level** is neutral. A **low angle** looks up at a character and makes them feel strong. A **high angle** looks down and makes them feel small.

**Movement:** **static** (still), **pan** (turning left or right), **push in** (moving closer) and **pull back** (moving away). Push in when something important is being realised, and pull back to show a character is alone.

Mix sizes: a sequence of only close-ups confuses the viewer, and only wide shots keeps them at a distance. A simple pattern is wide, medium, close-up, which introduces the place, the person and then the feeling."""),
            ("The scene prompt formula", """Image and video tools respond best to clear, ordered descriptions. Use this checklist for every shot, in this order:

1. **Subject:** who or what, with key details.
2. **Setting:** where and when.
3. **Shot size and angle:** wide, medium or close-up; eye level, low or high.
4. **Lighting:** time of day and direction, such as "warm candlelight from the left".
5. **Mood and colour:** the feeling of the picture.
6. **Style and aspect ratio:** the look of the artwork and the shape of the frame, such as 16:9 or 9:16.

Example: "A ten-year-old girl in a yellow dress, sitting at a small wooden table in a Lagos compound kitchen at night, medium shot, eye level, warm candlelight from the left, quiet and tense mood, flat-colour children's cartoon style, 16:9."

Put the most important idea first. Use **one idea per prompt**, because a prompt that asks for ten things delivers none of them well. Describe what you want to see rather than what you do not want. Keep a text file of your best prompts so you can reuse and adapt them."""),
            ("From a still image to a moving clip", """A safe and efficient workflow is to create the **still image** first, and only then animate it.

1. Generate several stills for the shot and pick the best one. This is your **keyframe**.
2. Give that still to an image-to-video tool, with a **motion prompt**. Describe only what moves and how the camera moves: "slow push in, the candle flame flickers, she turns the page".
3. Generate a short clip. Most tools make clips of a few seconds, which matches the 2 to 6 second shots in your list.
4. Review it frame by frame, then repeat or fix.

Expect problems and plan for them. Hands, text, crowds and fast action often go wrong, and some clips shimmer or change details halfway. When a shot fails, simplify: use a closer shot, slower movement or fewer subjects. A weak detail hidden by a close-up or a cut is a normal professional solution. Check the tool's own guide for what it supports, because features change quickly."""),
            ("Storyboard, animatic and a generation budget", """Place your approved stills in order in any editing tool, give each the length from your shot list, and add a rough sound or voice track. This is an **animatic**, a moving storyboard. Play it and check the pacing **before** you generate any video. It is much cheaper to remove a shot at this stage than after you have spent hours on it.

Then plan your budget. Imagine your shot list has 15 shots and you expect about 3 attempts for each shot. That is 15 x 3 = **45 generations**. Free allowances and speeds change often, so read the tool's current page, then divide: if a tool allows 10 generations a day, 45 generations will take 5 days. Generate the most important shots first, such as the opening and the climax, so any shortage hits the less important ones.

Note the settings that worked, keep every file named by shot number, such as s04_v02, and back up the folder. Good filing is what lets you rebuild the film after a mistake."""),
        ],
        diagram=grid([("SUBJECT", "Who or what,|with details"), ("SETTING", "Where and|when"), ("SHOT", "Size and|angle"), ("LIGHT", "Time of day,|direction"), ("MOOD", "Feeling|and colour"), ("STYLE", "Look and|aspect ratio")], 3, "Six parts, in this order, for every shot prompt"),
        caption="A strong shot prompt has six parts, written in the same order every time.",
        terms=[("Shot", "One continuous piece of film from one camera view."), ("Shot list", "A table that breaks a script into shots, with size, angle, action and length."),
               ("Close-up", "A shot that shows a face or an object up close, used for feelings."), ("Keyframe image", "The still picture that you animate or build a video clip from."),
               ("Motion prompt", "A description of what moves and how the camera moves."), ("Animatic", "A storyboard played in order with timing and rough sound."),
               ("Aspect ratio", "The shape of the frame, such as 16:9 (wide) or 9:16 (tall).")],
        mistakes=["Generating clips before writing a shot list, then discovering the story has gaps.", "Putting ten ideas into one prompt and getting none of them clearly.",
                  "Skipping the still image and spending video attempts on a shot that was never approved.", "Not naming and saving files, so a good shot cannot be found again."],
        quiz=[dict(q="A 60-second film has an average shot length of 4 seconds. About how many shots will you need?", o=["4", "15", "60", "240"], a=1, why="60 seconds divided by 4 seconds per shot is 15 shots."),
              dict(q="Which prompt is the strongest?", o=["a nice picture of a boy", "boy", "make it good", "A boy in a yellow shirt at a Lagos bus stop at dusk, medium shot, eye level, warm backlight, calm mood, flat-colour cartoon style, 16:9"], a=3, why="It covers subject, setting, shot, lighting, mood, style and aspect ratio in a clear order."),
              dict(q="Why generate a still image before animating it?", o=["You can check the look and composition cheaply before spending attempts on motion", "Stills never have mistakes", "Video tools cannot read words", "It makes the film longer"], a=0, why="A still that you approve gives the video tool a clear starting point, and fixing a picture costs less than fixing a clip."),
              dict(q="What should a motion prompt mainly describe?", o=["The price of the tool", "The file name", "What moves and how the camera moves", "The character's whole life story"], a=2, why="The still image already shows the subject. The motion prompt only needs to say what moves and how the camera moves.")],
    ),
    3: dict(
        minutes=15,
        hook="Imagine a Nollywood film where the hero has a different face in every scene. In the market he is thin, at home he is round, and in the final fight he has a new nose. The audience would walk out. This is the most common problem in AI animation, because every picture an AI tool makes is a fresh guess. This lesson shows how professionals tame that guess: with a character sheet, a fixed description block, reference images and a tidy asset folder. Once your hero looks the same in the market, at home and in the final shot, your film starts to look like it was made by a studio.",
        sections=[
            ("Why characters drift", """An AI image tool does not remember your character. Each time, it reads your words and makes a new picture that fits them. Small changes in the words, even changing the order, give a different face, a different outfit or a different age. Different shot sizes, lighting and styles also pull the result in other directions.

You cannot remove the randomness completely, but you can **narrow** it. Four habits do most of the work:

1. Write the character description **once** and reuse it exactly.
2. Create a **character sheet** and pick one approved version as your anchor.
3. Use a **reference image** with the same character in later prompts, when the tool supports it.
4. Keep the **style** and the **outfit** the same, and change only the shot and the action.

Accept that you will still reject some results. Your aim is a character who is recognisably the same person, not one who is identical in every pixel."""),
            ("The character sheet", """A **character sheet** is a single reference image, or a small set, showing your hero from different views. It is your anchor, and every later shot is judged against it. A good sheet includes:

- **Front view, side view and back view**, standing in a neutral pose.
- **Three expressions:** happy, worried and angry, or whatever fits your story.
- **One action pose**, such as running or reaching.
- A **plain background**, so the character is easy to see.
- The **same outfit** in every view.

To build it, write the full description (next section), ask for a "character turnaround sheet" or a set of expressions, and generate several versions. Pick the best, and note exactly which prompt and settings produced it. Save the approved sheet in a folder called "anchor". If you plan a longer film, make a sheet for every important character and for the main locations as well."""),
            ("The fixed description block", """The **fixed description block** is a paragraph that you write once and paste into every prompt for that character. Write it like a police description: concrete and specific, not poetic.

> Ada, a girl of about 10, round face, big dark eyes, short natural hair in two puffs, warm brown skin, yellow dress with a green belt, white sandals, flat-colour children's cartoon style.

Then each shot prompt is: **description block + shot + setting + action + lighting**. Only the part after the block changes.

Why it works: the more specific you are about stable features such as the hairstyle and the colours, the less room the tool has to invent. Avoid vague words like "pretty" or "cool", because they mean different things each time. Do not change a single word of the block while you work. If you must improve it, make a new version, such as v2, and regenerate the shots that were affected. Keep the block in your story bible."""),
            ("Reference images, locations and props", """Many tools can use a picture as a guide: you attach your approved image, and the tool tries to keep the same character, outfit or style. Features, names and limits differ and change quickly, so read the current guide of your tool before you plan around it. Where the tool allows it, use the **same reference** for every shot of that character.

Apply the same thinking to everything else:

- **Locations:** make one wide establishing image of each place, such as the compound or the market, and reuse it as a reference.
- **Props:** the candle, the school bag or the generator should keep one design.
- **Style:** pick one look at the start, such as flat colour or soft watercolour, and use the exact same style words in every prompt.

Where one image does not match, you can fix it by editing it in a photo editor, by generating the character separately on a plain background and placing it over the scene, or by keeping the shot closer so that fewer details are visible. These small manual fixes are normal in professional work."""),
            ("Asset hygiene and rights", """A film can have hundreds of files, so organise from day one.

- **Name files clearly:** ada_front_v03.png, bg_compound_night_v02.png, s04_v02.mp4.
- **Use folders:** anchor, characters, backgrounds, shots, audio, exports.
- **Save the prompt and the settings** next to each important file, in a text file or in the file name. That is how you recreate a result later.
- **Back up** to two places, such as the phone and a flash drive or cloud folder.

Be careful with **rights**. Read each tool's licence terms to see what you may do with the output, especially if you will sell the film or run adverts. Do not use the name of a living artist, a famous cartoon character or a real person's face in a prompt without permission. Keep your drafts and prompts as evidence of your own creative work. Original characters, designed by you, are safer and also more valuable to your portfolio."""),
        ],
        diagram=hub(("CHARACTER", "Your anchor sheet"), [("Description", "One fixed block"), ("Reference", "Same image each time"), ("Style", "One look for all"), ("Log", "Prompts saved")], "Four habits keep your hero looking like the same person"),
        caption="Four habits that keep a hero looking like the same person from the first shot to the last.",
        terms=[("Character sheet", "A reference image or set of images showing a character from several views."), ("Anchor", "The one approved version that every later shot is compared against."),
               ("Description block", "A fixed paragraph describing a character, pasted into every prompt."), ("Reference image", "A picture you give a tool to guide the result."),
               ("Establishing shot", "A wide shot that shows where the scene takes place."), ("Asset", "Any file used in the film, such as a character, background or sound."),
               ("Licence", "The rules that say how you may use a tool's output.")],
        mistakes=["Retyping the character description from memory each time, so the wording and the face change.", "Changing the outfit colours between shots without meaning to.",
                  "Forgetting to save the prompt that made the best image, then never matching it again.", "Using a famous character or a living artist's name in a prompt, which risks rights problems."],
        quiz=[dict(q="Why does a character's face change from picture to picture?", o=["The computer is broken", "The screen colours are wrong", "Each generation is a new guess based on the words, so small changes give different results", "The file name is too long"], a=2, why="The tool does not remember your character. It makes a new picture from the prompt every time, so you must narrow the guess."),
              dict(q="What is a fixed description block?", o=["A paragraph you write once and paste unchanged into every prompt for that character", "A locked folder", "A type of video file", "A background music track"], a=0, why="Reusing the exact same words about the hair, face, outfit and style reduces the room for the tool to invent changes."),
              dict(q="Which of these belongs on a character sheet?", o=["The price of the tool", "A long story", "A busy background", "Front, side and back views plus a few expressions on a plain background"], a=3, why="A character sheet is a clear reference: several views and expressions, the same outfit, and a plain background."),
              dict(q="What should you save next to each important asset?", o=["Only a screenshot", "The prompt and the settings that made it", "Nothing, the tool remembers", "The password of your account"], a=1, why="With the prompt and settings, you can recreate or adjust the result later instead of starting again.")],
    ),
    4: dict(
        minutes=16,
        hook="A voice that cannot pronounce \"Chukwuemeka\", \"Adebayo\" or \"Abubakar\" properly can ruin a scene, no matter how beautiful the picture is. Sound is where AI helps a lot and where it can also hurt you, because a voice carries a person's identity. This lesson covers three jobs that make characters feel alive: giving them voices, making their mouths match the words (lip-sync), and borrowing real human movement from a phone video (motion capture). You will also learn the rules about permission, because using someone's voice or likeness without consent is not a technical problem but a trust problem.",
        sections=[
            ("Your voice options", """You have three main ways to make a character speak:

- **Record real people.** A friend, a family member or you. It gives the best acting and costs nothing. Ask for a few takes of each line.
- **Text to speech.** You type the lines and a synthetic voice reads them. It is fast and consistent, and it is useful for narration and rough tracks. Quality, accents and language support differ, so **test a line in your language and with your names** before you commit.
- **Voice change.** You perform the line and a tool turns it into a different voice, keeping your timing and emotion.

Tips for good recording with a phone: use a quiet room (a closet full of clothes absorbs echo), keep the phone about 20 cm from the mouth, record the same distance each time, and keep the file in the highest quality available. **Write for the ear:** short sentences, no tongue twisters. For names that a synthetic voice misreads, try spelling them the way they sound, such as "Chook-wem-eh-ka", then listen again."""),
            ("Consent, rights and honesty", """A voice is part of a person's identity, so treat it carefully.

- **Never clone a real person's voice without their clear permission**, and keep that permission in writing, with a short message or a signed note saying what you will use it for.
- **Never use a cloned voice to deceive** people, for example to make someone appear to say something they never said.
- **Read the licence** of any voice tool, especially about commercial use, and about what happens to the voice data.
- **Pay or credit** the voice actors who help you, and agree the terms before recording.
- **Be open** about synthetic voices. If a client, a festival or a platform asks, tell them clearly. A short line in the credits, such as "Voices created with AI tools", is honest and normal.

These rules protect other people, and they also protect you. A film that uses a stolen voice can be taken down, and it can end a young creator's reputation before it begins."""),
            ("Lip-sync: matching the mouth to the sound", """People do not move the mouth for every letter. They move it for groups of sounds, called **visemes**. A simple set of mouth shapes is enough:

- **Closed lips** for M, B and P.
- **Wide open** for "ah".
- **Wide, spread lips** for "ee".
- **Small round shape** for "oo" and "oh".
- **Teeth on the lower lip** for F and V.
- **Resting** between words.

In 2D, draw four to six of these shapes and swap them in time with the sound. In 3D, you can use **shape keys** (also called blend shapes) for the same mouth positions. Many automatic lip-sync tools estimate the shapes from the audio, which is a great first pass, but always check it by hand.

Do the arithmetic: if your character speaks about 4 syllables a second, then at 24 fps each syllable lasts about 24 / 4 = **6 frames**. You do not need a new mouth shape every frame. Many animators place the mouth shapes **one or two frames before the sound**, because the eye expects to see the mouth move first. Test both and see what feels right."""),
            ("Markerless motion capture from a phone video", """**Motion capture** records a real person's movement and transfers it to a digital character. **Markerless** tools use ordinary video, so you do not need special suits. This is a powerful shortcut, especially for walking, dancing and fight scenes.

To get good results:

1. **Fix the camera** on a stable support. Do not hold it.
2. Keep the **whole body in the frame**, from head to feet, for the whole take.
3. Use a **plain background and good, even light**. Wear fitted clothes in a colour that is different from the background.
4. Film at 1080p and a steady frame rate, and keep the action in the **centre**.

Then run the video through a video-to-motion tool and **export** the result in a standard animation format, such as BVH or FBX. Import it into your 3D software and **retarget** it, which means mapping the captured skeleton to your character's rig. Always clean up the result: smooth shaky curves, fix feet that slide, and repair fingers and hands, which are usually weak. Fast spins and moments when a limb is hidden are the hardest cases for the tools."""),
            ("Mixing and checking the sound", """Sound should be built in layers: **dialogue, effects, ambience and music**. Set the levels so that dialogue is clearly the loudest, and the music sits well beneath it. Keep the peaks out of the red, to avoid distortion. Add small **ambience** such as a generator, a distant radio or crickets, so that the world does not feel empty. Put the effects on the exact frames of the action, as you did in the 2D track.

Check the mix on a **phone speaker** and on **headphones**. Many people in your audience will use one phone speaker, and many will watch **without sound** because of public transport, school or a sleeping baby. So **add captions**. They make the film accessible, and they also make sure that the story survives on mute.

Finally, re-check consent and credits. List every voice, every sound and every music track you used, with its licence or the permission you have. A tidy credits file now will save you an argument later."""),
        ],
        diagram=compare(("Real voices", ["Best acting and emotion", "Free with friends or family", "Needs a quiet place", "Hard to repeat identically"]), ("Synthetic voices", ["Fast and consistent", "Easy to redo any line", "Accents and names need tests", "Consent and licence matter"]), vs="vs", note="Many creators mix them: real voices for the heroes, synthetic for rough tracks"),
        caption="Real voices give the best acting, synthetic voices give speed. Test names and accents either way.",
        terms=[("Text to speech", "A tool that turns typed words into a spoken voice."), ("Voice cloning", "Making a synthetic copy of a specific person's voice, which needs their permission."),
               ("Viseme", "A mouth shape that matches a group of speech sounds."), ("Shape key", "A saved mesh shape, such as a mouth pose, that can be blended in."),
               ("Motion capture", "Recording real movement and transferring it to a digital character."), ("Retargeting", "Mapping captured motion onto a different character's skeleton."),
               ("Ambience", "The soft background sound of a place.")],
        mistakes=["Using a synthetic voice without testing how it reads local names and accents.", "Cloning a real person's voice without clear permission.",
                  "Animating a new mouth shape on every frame, so the mouth flaps and looks nervous.", "Filming mocap with a hand-held camera, cropped feet or a cluttered background."],
        quiz=[dict(q="A character speaks about 4 syllables per second at 24 fps. About how many frames does each syllable last?", o=["1", "3", "6", "24"], a=2, why="24 frames divided by 4 syllables is 6 frames per syllable, so you do not need a new mouth shape every frame."),
              dict(q="What must you do before cloning a real person's voice?", o=["Nothing, if the voice is online", "Get their clear permission, ideally in writing", "Change the pitch a little", "Ask a friend of theirs"], a=1, why="A voice is part of someone's identity. You need clear consent and a record of it."),
              dict(q="What is a viseme?", o=["A mouth shape that matches a group of sounds", "A video format", "A sound effect", "A type of light"], a=0, why="Visemes group similar sounds into a small set of mouth shapes, which is why a few drawings are enough."),
              dict(q="Which set-up gives the best phone-video motion capture?", o=["A moving hand-held camera", "Dark light and loose clothes", "Feet cropped out of the frame", "A fixed camera with the whole body in frame, in good light"], a=3, why="A steady camera, a full-body view and even light give the tool the clear picture that it needs.")],
    ),
    5: dict(
        minutes=16,
        hook="A young creator in Lagos with a laptop, a phone and a data bundle can now make what once needed a whole studio. But a tool is not a team, and a pile of generated clips is not a film. The difference is a **pipeline**: a clear sequence from idea to finished video, with a human decision at every stop. This final lesson ties together everything in this track and the 2D and 3D tracks. You will plan the film, count the work, mix hand-made and generated parts into one look, check the quality, and deliver a short film that you are proud to put in your portfolio.",
        sections=[
            ("The full pipeline", """A complete AI-assisted short film moves through these stages. Learn which parts a tool can help with and which parts must stay with you:

> 1. **Idea and logline:** AI brainstorms. You choose.
> 2. **Script:** AI drafts options. You rewrite in your voice.
> 3. **Shot list and storyboard:** you plan. AI makes stills.
> 4. **Characters and assets:** AI generates. You approve the anchor sheet.
> 5. **Shots:** AI or hand animation or 3D. You check every clip.
> 6. **Voice and sound:** recorded or generated. You direct and mix.
> 7. **Edit and finish:** you assemble, colour-match and add captions.
> 8. **Review and release:** you test with real viewers and deliver.

The pattern is simple: **AI produces options, you make decisions.** The stage where you must be most careful is the beginning, because a mistake in the script or the shot list is multiplied by every shot that follows."""),
            ("Planning your time and your limits", """Before you start, do the sums.

**Shots:** a 60-second film at an average of 4 seconds per shot needs 15 shots.

**Attempts:** assume about 3 tries for each shot, so that is 15 x 3 = 45 generations. Add roughly 20 more for the character sheet, the locations and the fixes, which gives about **65 generations**.

**Time:** note how long a typical generation takes on your connection, then multiply. If a generation takes 5 minutes, 65 of them take over 5 hours of waiting, which you can spread across days.

**Limits:** free allowances, speeds and rules vary between tools and change often, so read the current page of each tool. If a tool allows 10 generations a day, 65 generations is 7 days of work. Plan your calendar around it, and generate your most important shots first.

Write your plan on one page, with a date for each stage. A realistic four-week plan is: week 1 for the script and storyboard, week 2 for characters and assets, week 3 for shots, and week 4 for sound, editing and release."""),
            ("Mixing AI, 2D and 3D into one film", """You do not have to choose one method. Hybrid films are common and often look the best, because each method does the job it is best at.

- **Hand-drawn 2D character, AI background:** you animate the walk cycle yourself, and place it over a generated street.
- **3D character from Blender, AI textures and backdrops:** use the walk cycle you built in the 3D track, and generate the materials and the skyline.
- **AI for the previs:** make the storyboard and the animatic with AI, then animate the final shots by hand.

The danger of mixing is a film that looks like a patchwork. Fix that in the finishing stage by using the same treatment on everything: one **colour grade**, one amount of **film grain**, the same **title font**, and a matching **frame rate and shape**. A shared look is what makes shots from different sources feel like one film. Also check **screen direction**: if the hero walks left to right in one shot, keep it consistent in the next, or the audience will feel they turned around."""),
            ("Human checkpoints and quality control", """Put a **checkpoint** after every stage, and do not move on until it passes:

1. **After the script:** read it aloud and time it.
2. **After the storyboard:** can a friend tell the story from the pictures alone?
3. **After the asset sheets:** is the hero clearly the same person in every view?
4. **After the animatic:** is the pacing right? Cut now, because it is cheap.
5. **After the shots:** check for flicker, odd hands, wrong text and changing details.
6. **After the mix:** listen on a phone speaker, and read the captions.

Then show the film to two people without explaining anything, and watch their faces. Where they laugh, look confused or check their phone tells you exactly what to fix.

Be honest about how you made it. If a competition, a client or a platform asks whether AI tools were used, answer truthfully. A short note in the credits is good practice. And never use these tools to make deceptive content about real people. Your reputation is your main asset as a creator."""),
            ("Deliver, publish and grow", """Export the final film as an **MP4 with H.264**, at 1080p, in the frame rate you worked in. Make a smaller **720p version for WhatsApp**, and, if you plan to post on vertical-video apps, a **9:16 cut** made for that shape from the beginning, not cropped at the end. Add **captions** and a clean **title and end card** with your name and credits.

Build your portfolio around **process**, not just the result. Show the logline, a page of the storyboard, the character sheet and the final shot side by side. Clients and employers want to see that **you** made the decisions: the story, the shot choices, the timing and the fixes. That is the skill that tools cannot replace.

Keep the project folder safe, with the story bible, the prompts and the licence notes. Then start the next film. Your second film will be quicker, and your tenth will be better than most. You now have the skills of three tracks: 2D, 3D and AI-assisted filmmaking. Use them to tell stories that only you can tell."""),
        ],
        diagram=cycle([("WRITE", "Idea and script"), ("PLAN", "Shots and boards"), ("MAKE", "Assets and shots"), ("ASSEMBLE", "Edit and sound"), ("REVIEW", "Test and fix")], "ai5", "YOU DECIDE|at every stop", "AI makes options. You make the film."),
        caption="Every stage of the pipeline ends with a human decision, and review feeds back into the next film.",
        terms=[("Pipeline", "The fixed sequence of stages that takes a film from idea to delivery."), ("Previs", "Early rough versions of a film, used to plan before the final work."),
               ("Hybrid film", "A film that mixes methods, such as hand animation, 3D and AI-generated parts."), ("Colour grade", "A shared colour treatment that unifies the look of all the shots."),
               ("Screen direction", "The direction a subject moves across the frame, which should stay consistent."), ("Checkpoint", "A review point where a human approves the work before the next stage."),
               ("Portfolio", "A collection of your best work and process, shown to clients and employers.")],
        mistakes=["Skipping checkpoints and discovering at the end that the story or the character was wrong from the start.", "Mixing styles from different sources and not unifying them with one colour grade.",
                  "Estimating the work in your head instead of counting shots, attempts and days.", "Showing only the final video in your portfolio, with no proof of your own decisions."],
        quiz=[dict(q="A film has 14 shots with 3 attempts each. At 10 generations per day, how many days are needed?", o=["3", "4", "5", "14"], a=2, why="14 x 3 = 42 generations. 42 divided by 10 is 4.2, so you need 5 days."),
              dict(q="Why apply one colour grade and one film grain over every shot?", o=["To make shots from different sources feel like one film", "To make the file smaller", "To skip the edit", "To make it louder"], a=0, why="A shared treatment hides the differences between hand-made, 3D and generated shots."),
              dict(q="Which is the best time to cut a weak shot?", o=["After you have rendered every shot", "After you publish", "In the animatic, before you generate video", "Never"], a=2, why="Removing a shot from the animatic costs almost nothing, but removing it after production wastes hours."),
              dict(q="What should a portfolio piece show?", o=["Only the final video", "The process: logline, storyboard, character sheet and the final shot", "Only the tool's logo", "Only the prompts"], a=1, why="Process proves that you made the decisions, which is the skill that tools cannot replace.")],
    ),
}
