"""Animation Masterclass: lessons 9 to 24, added when the course grew into a full course (course_plan.py says where each one sits on screen).
Same format as lessons_animation.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option.
Software is named only as examples. Licences, prices and features change, so lessons tell the learner to check each tool's current page."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[9] = dict(   # The 12 principles of animation in action
    minutes=16,
    hook="In the 1930s, animators at Disney studied why some drawings felt alive and others felt like moving pictures. They wrote down what they learned, and in 1981 two of those animators, Ollie Johnston and Frank Thomas, published twelve principles in a book called The Illusion of Life. Nearly a century later, the same twelve ideas are used in hand-drawn films, 3D movies, video games, motion graphics and even phone interface animation. You met five of them in the foundations lesson. Now you will see all twelve working together on one simple object, a flour sack or a bouncing ball, so that you stop memorising a list and start using it as a checklist every time something moves. Learn these well and every tool you use later will give better results.",
    sections=[
        ("Weight and shape: squash, stretch and timing", """These three decide whether something feels heavy, light, soft or hard.

1. **Squash and stretch:** objects change shape to show force and flexibility. A ball squashes when it hits the floor and stretches when it moves fast. The **volume stays the same:** if it gets wider, it must get shorter.
2. **Timing:** the number of frames an action takes. Fewer frames feel fast and sharp. More frames feel slow, heavy or soft.
3. **Slow in and slow out (easing):** movement does not start and stop at full speed. Objects accelerate gently and slow down before stopping. Put more drawings near the start and end of a move, and fewer in the middle.

Test them on a **flour sack:** a sack that squashes softly on landing feels heavy and floppy. A rubber ball squashes less and bounces back faster. The same shape, with different squash and timing, becomes a different material."""),
        ("Flow of movement: anticipation, follow-through and arcs", """These make motion feel natural and connected.

- **Anticipation:** a small move in the opposite direction before the main action. A character bends the knees before jumping, or pulls the arm back before a throw. It prepares the audience for what is coming.
- **Follow-through and overlapping action:** parts do not all stop together. When a character stops running, the hair, clothes and tail keep moving for a few frames, then settle. Different parts start and stop at different times.
- **Arcs:** almost everything alive moves along curved paths, not straight lines. A swinging arm, a turning head and a thrown ball all follow arcs. Straight, mechanical paths look robotic.

A good test: draw the path of a moving hand across all frames. If the line looks like a smooth curve, you are on track. If it zigzags, fix the in-betweens."""),
        ("Clarity: staging, pose to pose and secondary action", """These help the audience understand what they are looking at.

- **Staging:** present each idea so that it is clear. Use strong silhouettes, show the important action in the clearest view, and avoid too many things moving at once. If everything moves, nothing is noticed.
- **Straight ahead and pose to pose:** two ways of working. **Straight ahead** means drawing frame after frame in order, which gives spontaneous, flowing results, good for fire and smoke. **Pose to pose** means drawing the key poses first and filling in between, which gives control and strong acting. Most character work uses pose to pose.
- **Secondary action:** a small action that supports the main one, such as a character whistling while walking, or scratching the head while thinking. It adds personality, but it must never steal attention from the main action."""),
        ("Character: exaggeration, solid drawing and appeal", """The last three are about quality.

- **Exaggeration:** push poses and expressions further than real life so they read clearly. Exaggeration does not mean chaos. It means making the idea stronger. A surprised face with wide eyes and raised brows beats a subtle one in a short film.
- **Solid drawing:** understanding form, weight, volume and balance, even in 2D. Draw characters as three-dimensional shapes, not flat outlines. In 3D this means good poses and balanced weight.
- **Appeal:** the quality that makes a character interesting to watch. It is not the same as pretty. A villain can have appeal through a clear shape, a strong personality and a pleasing design.

Appeal comes from **clear shapes, believable emotion and a design the viewer wants to look at.** Study characters you love and ask why you want to watch them."""),
        ("Using the principles as a checklist", """Before you show any shot, ask these questions:

1. Does it have **weight?** (squash, stretch, timing)
2. Does it **ease** in and out?
3. Is there **anticipation** before the main action?
4. Do parts **overlap** and settle (follow-through)?
5. Do the paths form **arcs?**
6. Is the **staging** clear in silhouette?
7. Have I used **exaggeration** enough to read?
8. Is there **appeal** in the pose and shape?

Practise by animating the same bouncing ball five times, each time focusing on one principle, then compare the clips. Keep every version: your progress will be visible. Do not try to use all twelve at full strength in every shot. Pick the ones the shot needs, and let the rest support quietly."""),
    ],
    diagram=grid([("Squash", "shape shows force"), ("Timing", "frames set speed"), ("Easing", "slow in and out"), ("Anticipation", "prepare the move"), ("Follow-through", "parts settle late"), ("Arcs", "curved paths"), ("Staging", "clear idea"), ("Pose to pose", "key poses first"), ("Secondary", "supporting action"), ("Exaggeration", "push the idea"), ("Solid drawing", "form and weight"), ("Appeal", "worth watching")], cols=3, note="Use them as a checklist."),
    caption="The twelve principles grouped as cards. Use them as a quick checklist before showing any shot.",
    terms=[("Squash and stretch", "Changing an object's shape to show force and flexibility while keeping volume."), ("Anticipation", "A small opposite movement that prepares the audience for the main action."),
           ("Follow-through", "Parts of a character continuing to move after the main body stops."), ("Overlapping action", "Different parts starting and stopping at different times."),
           ("Arcs", "The curved paths that natural movement follows."), ("Appeal", "The quality that makes a character interesting to look at.")],
    mistakes=["Moving everything in straight lines at constant speed.", "Skipping anticipation so actions look sudden.", "Letting every part of a character stop at the same moment.", "Animating too many things at once so nothing is clear."],
    quiz=[dict(q="What should stay the same when a ball squashes and stretches?", o=["Its volume", "Its colour only", "Its name", "Its frame number"], a=0,
               why="If it gets wider it must get shorter, so it still looks like the same solid object."),
          dict(q="What is anticipation?", o=["A small opposite movement before the main action", "The end of a shot", "A sound effect", "A camera cut"], a=0,
               why="Anticipation prepares the audience and adds power."),
          dict(q="Which method draws the key poses first and then fills between them?", o=["Straight ahead", "Pose to pose", "Copying", "Tracing"], a=1,
               why="Pose to pose gives control over acting and timing."),
          dict(q="What is follow-through?", o=["Parts such as hair continuing to move after the body stops", "Repeating a shot", "Saving a file", "Colouring the frame"], a=0,
               why="Loose parts settle a little later, which makes movement feel natural.")],
    activity="Animate a flour sack hopping across the screen three times, each focusing on a different principle such as squash, anticipation and follow-through, then compare the clips side by side.",
)

LESSONS[10] = dict(   # Timing, spacing and weight
    minutes=15,
    hook="Show the same drawing of a ball moving from left to right to ten people, once taking 12 frames and once taking 48 frames, and they will tell you two different stories. The first ball looks thrown hard. The second looks floating, perhaps a balloon. Nothing in the picture changed, only the timing and the spacing between the drawings. These two ideas are the real secret of believable animation. Timing is how many frames an action takes. Spacing is where each drawing sits between the start and end. Together they create weight, mood and personality. In this lesson you will learn frame rates and how animators count, how to read and draw spacing charts, how to build heavy and light movement, and how to test your timing before you spend hours polishing.",
    sections=[
        ("Frames, frame rates and counting", """Animation plays pictures in sequence. The **frame rate** is how many appear each second. Common rates:

- **24 fps:** the film standard, and the usual choice for animated films.
- **25 fps:** common in television in Nigeria and across Europe.
- **30 fps:** common for video and online content, and **60 fps** for smooth screen motion.

Animators often animate **on twos:** one drawing held for two frames, giving 12 drawings per second at 24 fps. It saves work and gives a classic look. **On ones** means a new drawing on every frame, used for fast action or very smooth movement. **On threes** is for slow movement. Learn to count in frames: **a one-second action is 24 frames, a half-second is 12, a quarter-second is 6.** A blink takes about 4 to 6 frames, and a quick punch might take 3 to 4. Decide your frame rate **before you start,** and never change it halfway."""),
        ("Spacing: the distance between drawings", """Timing is how many drawings. **Spacing** is where they sit. Draw a line from the start to the end of an action, then mark each frame:

- **Even spacing** (equal gaps) means constant speed: mechanical, like a conveyor belt.
- **Close spacing** means slow movement. **Wide spacing** means fast movement.
- **Ease out** (starting slowly): gaps start close and become wider.
- **Ease in** (stopping slowly): gaps start wide and become close.

A **spacing chart** is a small line with tick marks that you draw next to a key pose to plan the in-betweens. It looks simple, but it is the most useful planning tool in 2D and 3D. In 3D software, the same idea is controlled by curves in the graph editor, where a steep curve means fast and a flat curve means slow."""),
        ("Weight: heavy and light", """Weight is not drawn. It is **felt** through timing and spacing.

- **Heavy objects** are slow to start moving (long ease out), need more force, move less on impact and settle quickly. A bowling ball barely bounces.
- **Light objects** speed up quickly, float, bounce more and take longer to settle. A balloon or a feather drifts.
- **Soft objects** squash a lot. **Hard objects** barely change shape.
- A character lifting a heavy box shows it by **slow anticipation, strain, slower speed and a body leaning back.** The same box with a quick lift looks empty.

Gravity pulls everything at the same rate. Heavy and light objects fall similarly in a vacuum, but in real life air resistance changes feathers and balloons. In animation, you cheat for **clear storytelling.** Decide the weight in the story, then use timing to show it."""),
        ("The bouncing ball: a full timing study", """The bouncing ball is the classic exercise because it teaches everything:

1. **Plan the path** with a line of arcs on the page.
2. **Spacing on the way down:** gaps get wider as the ball speeds up.
3. **Contact:** the ball squashes on the frame it touches the ground.
4. **Spacing on the way up:** gaps get closer as it slows near the top, with the ball almost hanging for a moment at the peak.
5. **Each bounce is lower and shorter** than the one before, until it rolls to a stop.

A **basketball** bounces fast and high with a small squash. A **bowling ball** hits and barely rises. A **balloon** floats down slowly. Draw all three and compare, and the idea of weight becomes clear. Try 24 frames for the first bounce, then 20, 16 and 12 for the next ones."""),
        ("Testing and improving your timing", """Timing is easiest to fix **early:**

- Block out your animation with **rough key poses only,** and play it at full speed. Do not polish until the timing works.
- Use the **time-slider or scrub** (dragging back and forth) to feel the rhythm.
- **Act it out** with your own body, and use a phone stopwatch to count how long it takes.
- **Film reference** of someone doing the movement, and count the frames. Do not copy it exactly. Exaggerate the timing.
- **Change one thing at a time,** such as adding two frames to the hold before the jump, and watch again.
- **Ask someone to watch** without explanation. If they understand the action, the timing works.

Remember, **holds** matter. A character that stops and thinks for 12 frames before reacting feels intelligent. A reaction that arrives instantly feels robotic. Timing is where the acting lives."""),
    ],
    diagram=compare(("HEAVY", ["Slow to start", "Gaps grow slowly", "Small bounce", "Settles quickly"]), ("LIGHT", ["Quick to start", "Floats at the top", "Big bounce", "Takes long to settle"]), vs="vs", note="Weight is felt through timing and spacing."),
    caption="Heavy things start slowly and settle quickly. Light things move quickly, float and take longer to settle.",
    terms=[("Frame rate", "How many pictures play each second, such as 24 fps."), ("On twos", "Holding each drawing for two frames, giving 12 drawings per second at 24 fps."),
           ("Spacing", "The distance between successive drawings of a moving object."), ("Spacing chart", "A small line with tick marks used to plan the in-betweens."),
           ("Hold", "Keeping a pose still for several frames."), ("Ease out", "Starting a movement slowly and then speeding up.")],
    mistakes=["Changing the frame rate halfway through a project.", "Using even spacing so movement looks mechanical.", "Polishing before the timing of the blocking works.", "Giving a heavy object the same bounce as a light one."],
    quiz=[dict(q="How many frames are in one second at 24 fps?", o=["12", "24", "60", "100"], a=1,
               why="24 fps means 24 frames each second."),
          dict(q="What does close spacing between drawings show?", o=["Fast movement", "A cut", "A sound", "Slow movement"], a=3,
               why="Drawings close together make the object appear to move slowly."),
          dict(q="Animating on twos means what?", o=["Each drawing is held for two frames", "Two characters", "Two cameras", "Two songs"], a=0,
               why="Holding each drawing for two frames gives 12 drawings per second at 24 fps."),
          dict(q="Which object barely bounces?", o=["A balloon", "A bowling ball", "A feather", "A basketball in the air"], a=1,
               why="Heavy objects absorb impact and rise very little.")],
    activity="Animate three bouncing balls, a basketball, a bowling ball and a balloon, using spacing charts first. Compare frame counts and write one sentence on what timing made each feel the way it does.",
)

LESSONS[11] = dict(   # Choosing your software and setting up your workspace
    minutes=15,
    hook="Beginners often waste weeks hunting for the perfect software, when what really matters is whether the program runs on your computer, has plenty of free tutorials and lets you finish a short film. Professional studios use expensive tools, but you can make a complete animation today using free and open-source software. The bigger challenge in many places, including Nigeria, is practical: a laptop with 4 or 8 GB of memory, power cuts that can destroy unsaved work, costly data for downloads and little storage space. In this lesson you will compare the tools for 2D, 3D, editing and sound, learn how to match them to your computer, set up a tidy project folder and a backup habit, and choose the project settings once so you never fight them later.",
    sections=[
        ("Tools for 2D, 3D, editing and sound", """Names, prices and licences change, so check each tool's current website. Common free or low-cost options:

- **2D drawing and frame-by-frame:** **Krita** (painting with an animation timeline), **Pencil2D** (light and simple), **OpenToonz** and **Tahoma2D** (studio-grade tools), **Synfig Studio** (cut-out and vector).
- **2D and 3D together:** **Blender** (free and open source) includes **Grease Pencil,** which lets you draw 2D inside a 3D scene.
- **3D modelling, rigging, animation and rendering:** **Blender.**
- **Paid industry tools:** Toon Boom Harmony, Adobe Animate, Maya, Cinema 4D, often with student or trial offers. Check the terms and never use cracked copies. They contain malware and are illegal.
- **Video editing:** **DaVinci Resolve** (free version available), **Kdenlive,** **Shotcut.**
- **Sound:** **Audacity** for recording and cleaning, **LMMS** for music.
- **Reference and planning:** a phone camera, a notebook and a free storyboard tool such as **Storyboarder.**"""),
        ("Match the tools to your computer", """Look at your computer before you choose:

1. **Memory (RAM):** 8 GB is a comfortable minimum for most animation. With 4 GB, choose lighter tools such as Pencil2D, Krita with small canvases and low-resolution previews.
2. **Processor and graphics:** 3D rendering is demanding. Weak computers can still make 3D by using small render sizes, simple lighting and fewer samples.
3. **Storage:** animation files grow quickly. Keep at least 20 GB free, and use an external drive for finished work.
4. **Screen:** work at the size you can see clearly.
5. **A drawing tablet** helps 2D work greatly, but you can start with a mouse and a phone-based drawing app.
6. **Power:** a power bank or a small UPS gives time to save during a cut. Turn on **autosave** in every program.

Download software only from the **official website,** and when data is expensive, download at a library, a school or a friend's office, and share installers on a drive."""),
        ("Project settings: choose once", """Fix these settings **before** you draw the first frame:

- **Frame rate:** 24 fps is a good default.
- **Resolution:** **1920 by 1080** (Full HD) for the final film, and **1280 by 720** for faster drafts and weaker machines. Vertical video for phones is **1080 by 1920.**
- **Aspect ratio:** 16:9 for most video.
- **Colour space:** leave the default (sRGB) unless you know why you are changing it.
- **Audio sample rate:** 48 kHz for video.
- **Canvas size for backgrounds:** draw them **larger than the frame** if you plan camera pans.

Write these settings in a small text note at the top of the project folder. If you change resolution or frame rate later, drawings may need redoing and sound may drift out of sync."""),
        ("A project folder that never confuses you", """Chaos in files kills projects. Use a **consistent folder structure** like this:

> [Project folder]
> MyShort/
>   01_Script/
>   02_Design/
>   03_Storyboard/
>   04_Animation/   (one folder per scene: sc01, sc02)
>   05_Backgrounds/
>   06_Audio/       (voice, music, sfx)
>   07_Renders/
>   08_Edit/
>   09_Export/

Habits that save you:

- **Name files clearly with versions:** `sc03_walk_v02.kra`, not `final_final2_REAL.kra`.
- **Never overwrite** a good version. Save a new number every work session.
- **Keep sources** (project files) separate from outputs (renders).
- **Write a short README** with settings, fonts and credits.
- **Use short, simple names** with no spaces or special characters, because some tools fail on them."""),
        ("Backups, learning and starting small", """Protect your work with the **3-2-1 rule:** three copies, on two different devices, with one stored somewhere else, such as a friend's drive or a cloud folder. Back up **at the end of every work session.** A stolen or crashed laptop should be an inconvenience, not a disaster.

Learn efficiently:

- Choose **one tool for 2D** and **one for 3D.** Do not install ten programs.
- Follow **free official tutorials** and download videos when you have data.
- Make **tiny test projects** first: a bouncing ball, a 3-second walk.
- Join a **community** of animators, such as local groups and online forums, to ask questions and share work.
- **Set aside a regular time** each day, even 30 minutes.

The best software is the one you actually finish a short film with. Choose, install, set up your folder and start."""),
    ],
    diagram=tree("MYSHORT", [("Pre-production", ["01 Script", "02 Design", "03 Storyboard"]), ("Production", ["04 Animation", "05 Backgrounds", "06 Audio"]), ("Finishing", ["07 Renders", "08 Edit", "09 Export"])], note="Same folder names in every project."),
    caption="A project folder with numbered steps from script to export keeps files organised and easy to back up.",
    terms=[("Open source", "Software whose code is open and which is usually free to use."), ("Grease Pencil", "Blender's tool for drawing 2D animation inside a 3D scene."),
           ("Frame rate", "How many images play per second, set once at the start of a project."), ("Autosave", "A feature that saves your work automatically at intervals."),
           ("3-2-1 backup", "Three copies, on two devices, with one stored elsewhere."), ("Aspect ratio", "The shape of the picture, such as 16:9.")],
    mistakes=["Downloading cracked software that contains malware.", "Changing frame rate or resolution halfway through a project.", "Saving over a good version instead of making a new number.", "Installing many tools and mastering none."],
    quiz=[dict(q="Why avoid cracked software?", o=["It is illegal and often contains malware", "It is faster", "It uses less memory", "It has more tools"], a=0,
               why="Cracked programs can steal data and harm your computer, and using them is illegal."),
          dict(q="What frame rate is a good default for animated films?", o=["24 fps", "2 fps", "1000 fps", "0 fps"], a=0,
               why="24 fps is the film standard and works well for animation."),
          dict(q="What does the 3-2-1 backup rule suggest?", o=["Three copies, two devices, one stored elsewhere", "One copy only", "Three laptops", "Two files deleted"], a=0,
               why="Multiple copies in different places protect against loss."),
          dict(q="Which file name is better?", o=["final_final2_REAL", "sc03_walk_v02", "newfile", "asdf"], a=1,
               why="A clear scene name with a version number is easy to find and safe to keep.")],
    activity="Pick one 2D and one 3D tool, install them from the official sites, set the project to 24 fps and 1280 by 720, build the numbered folder structure and make your first backup to a second place.",
)

LESSONS[12] = dict(   # Writing a short animation script
    minutes=15,
    hook="Every animation you love began as words on a page. Before the first drawing, someone decided who the character is, what they want and what stops them. The good news is that a short animation script is small: a one-minute film may have just one page. The bad news is that a small script has no room for waste, so every line must earn its place. And because animation is a visual art, the best scripts tell the story through actions and pictures, not through long speeches. In this lesson you will learn how to shape a short story with a beginning, middle and end, how to write in the standard script format, how to use dialogue sparingly, and how to test your script so that it is ready for storyboards.",
    sections=[
        ("The shape of a short story", """A short film does not need a complicated plot. It needs a **clear want and a clear obstacle.** A simple structure for one to three minutes:

1. **Hook:** show the character and the situation in the first few seconds.
2. **Setup:** what the character wants.
3. **Problem:** something blocks them.
4. **Attempts:** the character tries, and fails, at least once. This is where humour and emotion grow.
5. **Twist or climax:** the turning point where something surprising or decisive happens.
6. **Ending:** a clear result, whether happy, sad or funny, that answers the question the film asked.

> [Example: a one-minute idea]
> A small boy in a Lagos market wants one mango from a high stall (want). He is too short (problem). He stacks crates and falls (attempt). A tall trader laughs, then lifts him up (twist). Both share the mango (ending).

The logline you wrote earlier is your compass. Every scene should serve it."""),
        ("Show, do not tell", """Animation is a **visual** medium, so tell the story through action:

- Instead of “Ada is nervous,” show her **fingers drumming and her eyes darting** to the clock.
- Instead of a character saying “I am hungry,” show her **staring at a plate of jollof** and her stomach rumbling.
- Use **props, colour and setting** to tell the audience about people and places.
- **Pantomime** (acting without words) is powerful and travels across every language. Many of the best short animations have no dialogue at all.
- If a line of dialogue only repeats what the picture already shows, **cut it.**

Read your script and ask of each line, “Can I show this instead?” Dialogue should add what pictures cannot, such as a joke, a secret or a surprise."""),
        ("Script format", """A script has a standard layout that everyone can read:

> [Script format]
> INT. MARKET STALL - DAY
>
> KEMI (8) stretches on her toes. The mango hangs just out of reach.
>
> She grabs a crate and stacks it. Another. The tower wobbles.
>
> KEMI
> (whispering)
> Almost there.
>
> The crates tumble. CRASH.

- **Scene heading (slug line):** INT. or EXT. (inside or outside), the place and the time of day.
- **Action lines:** what we **see and hear,** in the present tense, short and clear.
- **Character name** above the dialogue, in capitals when they first appear.
- **Dialogue** under the name. A short **parenthetical** may show the way it is spoken.

Keep action lines to **one to three lines.** Write only what can be seen or heard on screen. Avoid thoughts and unfilmable details. Free tools such as **Trelby, Fountain-based editors** and word processors can format scripts, and a plain document also works."""),
        ("Pacing, length and dialogue for animation", """Animation is expensive in time, so keep it small:

- **One page of script roughly equals one minute** on screen, but action-heavy animation can run shorter. Most students should aim for **one to two minutes.**
- **Fewer characters and fewer locations** mean less work. One or two characters and one or two settings is a smart limit for a first film.
- **Keep dialogue short.** Each line costs voice recording, lip-sync and animation time.
- **Cut early.** A line cut from the script saves hours of animation.
- **Think about what is hard to draw:** crowds, complex machines and fast camera moves. Simplify.
- **Culture and language:** you can include Yoruba, Igbo, Hausa, Pidgin and other languages in dialogue, and give a short subtitle or a clear visual meaning. Make sure the language is accurate and respectful, and ask native speakers to check it.
- **Use sound** as part of the writing, such as a market noise or a ringing phone."""),
        ("Test and improve the script", """Before you draw anything:

1. **Read it aloud** and time it with a stopwatch.
2. **Ask a friend to read it** and tell you the story in their own words. If they miss the point, fix the script.
3. **Check the want and the obstacle** are clear by the end of the first third.
4. **Look for the single strongest image,** such as the crates falling, and make sure the story builds towards it.
5. **Cut every scene, line or character** that the story could live without.
6. **Rewrite the ending** until it feels earned.
7. **Check that you can finish it:** can you really animate every shot in the time you have?

Then keep a **version number** and a date on the page. A short, strong script is the best gift you can give your future self, the animator."""),
    ],
    diagram=timeline([("Hook", "who and where"), ("Want", "what they need"), ("Problem", "what blocks them"), ("Attempts", "try and fail"), ("Twist", "the turning point"), ("Ending", "the answer")], note="A tiny story still needs a shape."),
    caption="A short script moves from a hook to a want, a problem, attempts, a twist and an ending.",
    terms=[("Script", "A written plan of what the audience will see and hear."), ("Slug line", "The scene heading that gives the place and time, such as INT. MARKET - DAY."),
           ("Action line", "A short line describing what we see and hear."), ("Pantomime", "Telling a story through movement and expression without words."),
           ("Twist", "A surprising turn that changes how the story ends."), ("Parenthetical", "A short note about how a line of dialogue is spoken.")],
    mistakes=["Writing a story that is far too big for the time available.", "Using dialogue to explain what the pictures already show.", "Writing thoughts that cannot be seen on screen.", "Adding many characters and locations to a first film."],
    quiz=[dict(q="What two things does every short story need?", o=["A clear want and an obstacle", "A long speech and a song", "Ten characters", "A fixed length of ten minutes"], a=0,
               why="Wants and obstacles create the conflict that drives a story."),
          dict(q="Which line is better visual writing?", o=["She is nervous.", "Her fingers drum on the desk and her eyes dart to the clock.", "She feels many emotions.", "It is a sad moment."], a=1,
               why="Action lines show what we see and hear."),
          dict(q="What does INT. mean in a slug line?", o=["Internet", "Inside", "International", "Interval"], a=1,
               why="INT. means the scene takes place indoors."),
          dict(q="How long is a good first animation?", o=["Ten minutes", "One to two minutes", "One hour", "Ten seconds always"], a=1,
               why="A short film is far more likely to be finished.")],
    activity="Write a one-page script for a one-minute silent film with one character and one location. Give it a hook, a want, an obstacle, one failed attempt, a twist and an ending, then read it to a friend and ask them to retell the story.",
)

LESSONS[13] = dict(   # Character and world design
    minutes=16,
    hook="Think of a character you can recognise from a tiny shadow: the round shape of one, the spiky hair of another, the long coat of a third. That instant recognition is the result of design, and it makes a character easy to animate, easy to remember and easy to love. A world works the same way. A few clear choices about shape, colour and detail make a place feel real and consistent. In this lesson you will learn the building blocks of character design, which are silhouette, shape language, proportion and colour, how to draw the sheets that a whole team can follow, how to design worlds and props that match your characters, and how to draw on Nigerian and African life with authenticity and respect, without copying anyone else's work.",
    sections=[
        ("Start with silhouette and shape language", """Designers begin with **simple shapes,** in black, before any detail.

- **Silhouette:** if you fill your character with solid black, can you still tell who it is, and what it is doing? A strong silhouette is the most important test.
- **Shape language:** shapes carry feelings.
  - **Circles** feel friendly, soft and safe.
  - **Squares** feel strong, stable and reliable.
  - **Triangles** feel sharp, dangerous or energetic.

Combine them with purpose. A hero might be round and warm. A grumpy trader could be square and solid. A villain could be built from triangles. Draw **twenty quick thumbnail silhouettes** of your character, small and rough, and pick the three most interesting. Do not fall in love with your first idea."""),
        ("Proportion, personality and appeal", """Proportion means the size relationship between parts of the body:

- **Heads tall:** measure the body in head-heights. A realistic adult is about seven or eight heads tall. A cartoon child might be only two or three, giving a cute, simple look.
- **Big head, big eyes, small body** reads as young and appealing. **Broad shoulders** read as strong. **Long thin limbs** read as agile or awkward.
- **Pose and posture** tell personality: a tall, upright character feels proud, a hunched one feels shy.
- **Keep it simple enough to animate.** Every extra button, pattern and braid must be drawn on every frame, or built and rigged in 3D. A good rule is to be able to **redraw the character in a few seconds.**
- **Give the character a clear want,** a flaw and a quirk. A fisherman who is afraid of water is more interesting than one who is perfect.

Appeal does not mean pretty. It means **clear, readable and interesting to watch.**"""),
        ("Colour and the model sheet", """**Colour** sets mood and helps the audience follow the story.

1. Choose a **limited palette,** about three main colours plus accents.
2. **Contrast** the character from the background, since your hero should never vanish into the scenery.
3. **Colour has meaning,** but meaning differs between cultures. Red may signal danger, love or celebration. Research your audience.
4. **Test in greyscale.** If the values (lightness) work in grey, the colours will work in colour.
5. **Consider lighting:** a character looks different in a bright market and in a dark room. Plan a day and a night version if needed.

A **model sheet** is the official reference every animator follows:

- **Turnaround:** front, side, back and three-quarter views.
- **Expression sheet:** happy, sad, angry, surprised, scared, thinking.
- **Pose sheet:** typical actions.
- **Size chart:** the character next to others and to props.
- **Colour swatches** with codes, and notes on details.

A good model sheet keeps the character **consistent** across every shot and every artist."""),
        ("Designing the world", """The world should **fit the characters and serve the story,** not just look pretty.

- **Rules of the world:** is it realistic, magical or comic? Once you set the rules, keep them. A cat that talks in one scene should talk in every scene.
- **Few locations, well designed:** one market, a house and a street are enough for a short film.
- **Shape and colour match:** a gentle story might use soft curves and warm tones. A tense story might use sharp angles and dark colours.
- **Props** such as a bucket, a danfo bus, a radio or a mortar show culture and character. Design the important ones as carefully as the characters.
- **Depth:** design foreground, middle ground and background, so you can build layers.
- **Reference without copying.** Collect photos, sketches and notes on real places and people. **Study** them, then draw from your understanding, not tracing. Copying another artist's design or a famous character can create legal problems and spoil your own voice.
- **Make a mood board** of images, colours and textures to share with your team."""),
        ("Authenticity, respect and 3D needs", """Nigerian and African settings, languages, clothes and traditions are a huge strength, because audiences everywhere want fresh stories. Handle them with care:

- **Research properly,** and talk to people from the community you depict.
- **Avoid stereotypes.** Show people as individuals with different goals and feelings, not as a single type.
- **Get the details right:** hairstyles, fabrics, patterns, food, greetings and architecture.
- **Credit and compensate** cultural collaborators, such as consultants, artists and musicians.
- **Check sacred or sensitive symbols** with people who understand them before using them.

If your character will be **3D,** also consider:

- **Polygon budget:** fewer polygons render faster and run on weak computers.
- **Clothing and hair** are harder in 3D. Simpler designs are easier to rig.
- **Provide front and side views** exactly aligned, so the modeller can build from them.

Finish with a **one-page design bible:** character sheets, palette, key props, locations and rules."""),
    ],
    diagram=triangle([("CIRCLE", "friendly and safe"), ("SQUARE", "strong and stable"), ("TRIANGLE", "sharp and dangerous")], middle="shape|language", note="Shapes carry feelings."),
    caption="Shape language: circles feel friendly, squares feel strong and stable, and triangles feel sharp or dangerous.",
    terms=[("Silhouette", "The solid outline of a character, which should be easy to recognise."), ("Shape language", "Using circles, squares and triangles to express personality."),
           ("Model sheet", "A reference page that shows a character from many views and with many expressions."), ("Turnaround", "Views of a character from the front, side and back."),
           ("Mood board", "A collection of images and colours that sets the look and feel."), ("Palette", "The limited set of colours used in a design.")],
    mistakes=["Adding so much detail that the character is hard to animate.", "Copying an existing character instead of designing your own.", "Relying on stereotypes when showing a culture.", "Using colours that make the character vanish into the background."],
    quiz=[dict(q="What does a strong silhouette test show?", o=["Whether the character is recognisable as solid black", "Its voice", "Its speed", "The final price"], a=0,
               why="If the shape reads clearly in black, the design will be clear on screen."),
          dict(q="Which shape usually suggests friendliness?", o=["Sharp triangles", "Circles", "Spikes", "Thin lines"], a=1,
               why="Soft round shapes feel safe and friendly."),
          dict(q="What does a model sheet do?", o=["Keeps the character consistent across shots and artists", "Plays the sound", "Edits the video", "Sells the film"], a=0,
               why="Everyone follows the same turnarounds, expressions and colours."),
          dict(q="Why avoid stereotypes in character design?", o=["They make files larger", "People are individuals, and stereotypes are inaccurate and unfair", "They use fewer colours", "They are a legal licence"], a=1,
               why="Specific, respectful portrayals make stronger stories.")],
    activity="Draw twenty tiny black silhouettes for a character, pick the best, and then make a one-page model sheet with front and side views, six expressions and a colour palette. Test the colours in greyscale.",
)

LESSONS[14] = dict(   # Storyboards and animatics
    minutes=16,
    hook="Animating a scene is slow. One second of work can take hours. So professionals never start animating until they have watched the film in rough form first. That rough version has two stages. First the storyboard, a comic-strip of drawings that plans every shot. Then the animatic, the storyboard played in time with sound so that you can feel the rhythm of the film. Finding a problem at this stage costs minutes. Finding the same problem after finishing the animation costs weeks. The earlier lesson introduced both. In this lesson you will go deeper: how to compose a clear panel, how to show the camera and movement, how to keep the audience oriented, how to time an animatic and how to use it as the master plan for the whole production.",
    sections=[
        ("What a storyboard panel must show", """A storyboard is not about beautiful drawing. It is about **clear communication.** Each panel is one shot or one important moment, and it should show:

- **Who and where:** the characters and the place.
- **The framing:** wide, medium or close-up (see the shot types you learned).
- **The action:** the key pose or the main change.
- **The camera:** arrows showing pans, zooms and tracking.
- **Movement:** arrows for characters or objects.
- **Dialogue or sound** written under the panel.
- **Timing:** an estimate in seconds.

Use **stick figures and simple shapes** if you must. A rough board that is finished is better than a beautiful one that is half done. Number each shot and scene so everyone can refer to them."""),
        ("Composition and staging in a panel", """A good panel is **readable in one second:**

1. **One idea per shot.** If a panel needs three things to be noticed, split it.
2. **Rule of thirds:** place the important thing near a third of the frame, not always dead centre.
3. **Foreground, middle ground and background** add depth.
4. **Leading lines and contrast** guide the eye to the focus.
5. **Strong silhouettes,** so the action reads clearly.
6. **Eye lines:** characters looking at each other must face the right directions.
7. **Camera height and angle:** a low angle makes a character feel powerful. A high angle makes them small or weak.
8. **Leave room** in front of a moving or looking character.

Draw a **frame border** at your real aspect ratio, such as 16:9, so you never plan something that will not fit. Thumbnail small first, then choose the best."""),
        ("Continuity and the 180-degree rule", """Cutting between shots can confuse people if space is not clear:

- **The 180-degree rule:** imagine a line between two characters. Keep the camera on one side of it, so that the left and right positions do not flip between shots.
- **Screen direction:** if a character runs left to right in one shot, the next shot should also show them going left to right, unless the change is shown on screen.
- **Match the action:** a door that is open in the wide shot should be open in the close-up.
- **Establishing shot:** begin a scene with a wide view that shows where we are.
- **Match cuts and eye-line matches** link two shots smoothly.
- **Transitions:** a **cut** is the default. A **fade** suggests time passing. Use fancy wipes rarely.

Break these rules only on purpose, when you want the audience to feel confused or surprised."""),
        ("From storyboard to animatic", """An **animatic** puts the storyboard on a **timeline** with sound. Steps:

1. **Scan or export** your panels as images at the project resolution.
2. **Place them in an editor** such as Kdenlive, DaVinci Resolve or Shotcut, or in a storyboard tool such as Storyboarder.
3. **Add a scratch track:** a rough voice recording (even your own), temporary music and key sound effects.
4. **Set the duration** of each panel to match the intended action. Use extra drawings or simple movement (pans, zooms) where needed.
5. **Watch the whole thing** and note where it drags or rushes.
6. **Cut, reorder and fix** panels until the story flows. This is far cheaper than fixing finished animation.
7. **Lock the animatic** when you are happy. It becomes the **timing guide** for each shot: each shot's length is now known."""),
        ("Using feedback and the animatic as a plan", """Show your animatic to **two or three people** who have not read the script:

- Do they understand **who wants what?**
- Where did they **get bored or lost?**
- Which moment **made them react?** Make sure it lands.
- Is the **ending clear?**

Take notes, do not argue, and make changes. Then use the animatic for production:

- **Shot list:** list every shot with its length in frames, which you can use as a budget.
- **Schedule:** estimate how long each shot will take to animate and add a buffer of 25% or more.
- **Replace panels with real animation** as you finish shots, and keep playing the film, so you always see progress.
- **Cut shots that are not needed.** An animatic reveals what the story can live without.

A solid animatic is the single best predictor that a short film will be finished and will work."""),
    ],
    diagram=flow([("Script", "words on a page"), ("Thumbnails", "quick sketches"), ("Storyboard", "clean panels"), ("Animatic", "timed with sound"), ("Approve", "lock the plan")], "an14", note="Fix problems here, not after animating."),
    caption="From script to thumbnails, storyboard and a timed animatic that becomes the plan for the whole film.",
    terms=[("Storyboard", "A series of drawings that plans each shot of a film."), ("Animatic", "A storyboard played in time with sound."),
           ("Establishing shot", "A wide view that shows where a scene takes place."), ("180-degree rule", "A guideline that keeps the camera on one side of the action line."),
           ("Screen direction", "The direction characters move across the screen."), ("Scratch track", "A temporary rough sound track used while planning.")],
    mistakes=["Spending weeks on beautiful panels instead of finishing the board.", "Putting several ideas in one panel.", "Flipping screen direction between shots without meaning to.", "Skipping the animatic and discovering timing problems after animating."],
    quiz=[dict(q="What is an animatic?", o=["A storyboard played in time with sound", "A finished film", "A type of pencil", "A colour palette"], a=0,
               why="An animatic lets you feel the rhythm of the film before animating."),
          dict(q="What does the 180-degree rule help with?", o=["Colour", "Keeping left and right positions clear between shots", "Audio loudness", "Frame rate"], a=1,
               why="It keeps the audience oriented in the space."),
          dict(q="How many ideas should one storyboard panel carry?", o=["Five", "One", "Ten", "None"], a=1,
               why="One clear idea reads in a second."),
          dict(q="Why is an animatic useful?", o=["It makes problems cheap to fix early", "It replaces animation", "It improves the sound only", "It is required by software"], a=0,
               why="Fixing a panel takes minutes, and fixing animation takes weeks.")],
    activity="Draw a thumbnail storyboard of at least twelve panels for your script, mark camera arrows and timing, put it on an editor timeline with a scratch voice and sound effects, and show the animatic to two viewers.",
)

LESSONS[15] = dict(   # Walk cycles and character acting in 2D
    minutes=17,
    hook="A walk cycle is the animator's first big test. It is only a few steps repeated, yet it reveals everything: weight, rhythm, personality and mood. A walk can show that a character is happy, tired, proud, sneaky or scared without a word. A walk cycle also teaches the idea of a loop, which is used in games, advertisements and background characters everywhere. And once a character can walk, you can make it act: think, react, notice and decide. In this lesson you will break the walk down into four key poses, learn how to time and draw it, add personality, and then move to acting: how eyes, head and body work together to show a thought, so that your characters feel alive and not just moving.",
    sections=[
        ("The four key poses of a walk", """A walk cycle for one full step is built on four poses:

1. **Contact:** the front heel just touches the ground, legs are furthest apart, and the arms are opposite to the legs.
2. **Down (recoil):** the body sinks to its lowest point as the weight lands on the front leg.
3. **Passing:** the back leg swings past the standing leg. The body is rising.
4. **Up (high point):** the body is at its highest, pushing off the toe.

Then the same four poses repeat on the **other leg** to complete the cycle. A full cycle of two steps at 24 fps commonly takes **16 to 24 frames** at a normal pace. Draw the contact poses first, then the passing pose, then the down and up poses, and finally the in-betweens. In the key poses, remember that **opposite arms and legs swing together:** when the right leg is forward, the left arm is forward."""),
        ("Timing, loops and the moving background", """To make the cycle work:

- **Plan the loop:** the last frame must lead smoothly back into the first. Many tools let you play the cycle on repeat so you can check it.
- **Timing:** a **slow walk** takes more frames per step, a **run** takes fewer. A typical walking step is 12 frames at 24 fps, so a full two-step cycle is 24 frames, and a brisk walk can be around 16.
- **Walk in place:** draw the character walking in place, and move the **background** instead. This is easier than moving the character across the screen, and keeps the loop clean.
- **Foot sliding:** if the feet seem to slide, the background moves at the wrong speed. Match the speed of the background to the speed of the foot on the ground.
- **Head and arcs:** the head follows a smooth wave, rising and falling. Trace it to check.
- **Onion skinning** shows faint copies of previous and next frames, so you can see the motion path while you draw. Use it constantly."""),
        ("Personality in a walk", """The same four poses, changed slightly, create characters:

- **Happy:** a bounce, upturned head, wide arm swings, a longer step.
- **Tired:** slow timing, drooping head, small steps, feet dragging, arms hanging.
- **Proud:** chest out, head high, steady rhythm.
- **Sneaky:** low body, light steps, quick looks around.
- **Heavy:** wide stance, a deep down pose, slow recovery.
- **Scared:** hunched, fast small steps, jerky head turns.

Change the **posture, timing, step length and arm swing,** and add a **secondary action:** swinging a bag, adjusting a cap. Always ask what the character **feels,** and let that decide the walk. Test it by showing the walk with the face covered and asking someone to guess the mood."""),
        ("Acting: thinking, reacting and deciding", """Acting is what makes an audience care. A character shows a thought through a clear sequence:

1. **The trigger:** something happens, such as a sound or a note.
2. **The look:** the **eyes lead,** moving first, then the head, then the body follows. This order feels natural.
3. **The reaction:** a change of expression and pose, the realisation.
4. **The hold:** a pause that gives the audience time to understand. Do not rush this.
5. **The decision:** the character acts.

Other tips:

- **Use a strong line of action:** one flowing curve through the pose that shows the emotion.
- **Strong poses first,** then fill. A great acting scene often has only five to ten key drawings.
- **Contrast** makes feelings clear: a quick movement followed by a stillness.
- **Act it out** in a mirror or film yourself on a phone. Study what your eyebrows, shoulders and hands do.
- **Blinks:** a blink during a head turn helps hide the change. A blink every few seconds keeps the character alive."""),
        ("Planning a performance shot", """To animate a short acting shot:

1. **Choose the line or the action,** and the exact emotion.
2. **Record reference** of yourself performing it, then pick the moments that matter. Do not copy every movement.
3. **Thumbnail the key poses** on paper.
4. **Block the key poses** in your software with rough timing.
5. **Play it back** and adjust the holds and timing.
6. **Add breakdowns and in-betweens,** then overlap and follow-through.
7. **Polish:** arcs, eyes, hands and small touches.
8. **Get feedback** from a friend and fix.

Hands and eyes carry much of the acting. Even a simple character with dot eyes can show strong emotion with the angle of the head and the weight of the body. Keep a **library of your own walk cycles and acting clips** to reuse for practice and for your showreel."""),
    ],
    diagram=cycle([("Contact", "heel touches"), ("Down", "weight lands"), ("Passing", "leg swings past"), ("Up", "body rises")], "an15", center="Walk|cycle", note="Then repeat on the other leg."),
    caption="A walk is built from four key poses: contact, down, passing and up, repeated on each leg to form a loop.",
    terms=[("Walk cycle", "A short looping animation of a character walking."), ("Contact pose", "The key pose where the front heel first touches the ground."),
           ("Passing pose", "The key pose where the back leg swings past the standing leg."), ("Onion skinning", "Showing faint copies of nearby frames to guide drawing."),
           ("Line of action", "A flowing curve through a pose that shows its energy."), ("Hold", "A pause in a pose that gives the audience time to understand.")],
    mistakes=["Making the loop jump because the last frame does not match the first.", "Letting feet slide because the background speed is wrong.", "Moving head and body at the same instant instead of eyes first.", "Rushing the hold after a reaction."],
    quiz=[dict(q="Which pose has the front heel just touching the ground?", o=["Passing", "Contact", "Up", "Hold"], a=1,
               why="Contact is when the front foot lands."),
          dict(q="In a walk, which arm swings forward with the right leg?", o=["The left arm", "The right arm", "Neither", "Both"], a=0,
               why="Opposite arms and legs swing together."),
          dict(q="What is the usual order of a look reaction?", o=["Body, head, eyes", "Eyes, head, body", "Head only", "No order"], a=1,
               why="The eyes lead, and the head and body follow."),
          dict(q="Why walk the character in place?", o=["It makes the loop cleaner and the background does the travelling", "It uses more frames", "It removes arms", "It is a law"], a=0,
               why="The background moves at the speed of the ground and the loop stays simple.")],
    activity="Animate a 24 frame walk cycle of a simple character in place with four key poses and a looping background. Then change only posture and timing to make it tired and proud, and ask a friend to guess each mood.",
)

LESSONS[16] = dict(   # Backgrounds, layers and effects
    minutes=16,
    hook="A character floating in white space is a drawing. The same character in a rich, layered world, with dust drifting past, a lamp glowing behind and a cloud of smoke trailing after a bus, is a scene. Backgrounds and effects do not usually get the attention of characters, but they carry the mood, the depth and much of the polish that separates beginner work from professional work. Better still, layers are a time-saver: you draw the background once, and reuse it across many frames. In this lesson you will learn how backgrounds are designed with perspective and colour, how layers are stacked and moved to create depth, how simple camera moves work, and how to animate common effects such as smoke, fire, water and impact.",
    sections=[
        ("Designing a background that supports the story", """A background has jobs: place the story, set the mood and **keep the characters readable.**

- **Perspective:** use a **horizon line** and vanishing points. **One-point perspective** has lines meeting at a single point (a corridor or a straight road). **Two-point perspective** shows a corner of a building. Draw a simple perspective grid first.
- **Values:** the background should be **calmer and slightly lower in contrast** than the character, so the character stands out.
- **Colour:** keep it within the palette you chose in design, and match the time of day and weather.
- **Composition:** leave space where characters will act, and place details around, not behind, the main action.
- **Details tell the story:** peeling paint, a rusted gate, posters and market stalls tell us about the place.
- **Size:** if the camera will pan, paint the background **wider or taller than the frame.**
- **Simplify:** a few strong shapes beat a thousand tiny details."""),
        ("Layers and the multiplane idea", """Instead of one picture, build the scene in **layers,** like sheets of glass:

1. **Sky and far background:** distant hills, sky, buildings.
2. **Middle ground:** trees, walls, vehicles.
3. **Character layer:** the animation.
4. **Foreground:** a fence, grass, leaves, drawn in front of the characters.
5. **Overlays:** light, mist, grain.

Move the layers at **different speeds** when the camera pans: close layers move more, far layers move less. This is **parallax,** and it creates depth. Old studios did this with real sheets of glass in a machine called a multiplane camera. Today your software does it. Benefits: **reuse** (draw once and reuse), **easy changes** (recolour one layer), and **flexibility** (move the camera in the edit). Name layers clearly and **lock** the ones you are not editing."""),
        ("Camera moves in 2D", """Even in 2D, you can move the camera by moving or scaling layers:

- **Pan:** the camera moves sideways. Layers slide across the frame.
- **Tilt:** the camera moves up or down.
- **Zoom or push-in:** scaling up to focus attention. Slow zooms build tension.
- **Track:** the camera follows a moving character.
- **Shake:** a quick random movement for impact, small and short.

Always **ease** camera moves in and out, since a sudden start or stop looks mechanical. Hold the camera still before and after a move. Avoid moving the camera without a reason: each move should **mean** something, such as discovering a place, following action or creating tension. Check that **fast pans do not blur or flicker** thin lines when you export."""),
        ("Effects: smoke, fire, water and impact", """Effects animation, called **FX,** brings energy. The secret is that natural effects follow simple rules:

- **Smoke:** it rises, spreads, slows and fades. Draw wavy shapes that grow and thin out. Use few drawings, on twos or threes.
- **Fire:** shapes lick upward, split into pieces and shrink. Loop a few frames. Keep it lively with different timing for each flame.
- **Water:** a splash rises in a crown, forms droplets that follow arcs, and settles into rings. Ripples spread and fade.
- **Impact:** a flash of one or two frames, a **smear** (a stretched drawing of fast movement), dust, and a small camera shake.
- **Speed:** speed lines, motion blur drawings and dust trails.
- **Wind and rain:** repeated loops that run behind or in front.

Use **straight-ahead** animation for effects, drawing frame after frame so the shapes evolve naturally. Study real references in slow motion on your phone. Keep effects **simple and stylised,** matching your film's style, and always **time them to the action,** such as the flash on the exact frame of contact."""),
        ("A practical workflow and common problems", """Work in order:

1. **Lock the animatic** and shot length.
2. **Paint backgrounds** at full size, with layers.
3. **Animate characters** over the background in place.
4. **Add FX** after the main animation is approved.
5. **Composite:** combine layers, adjust colour, add light and shadows.
6. **Render a test** and watch it on a phone and a laptop.

Common problems and fixes:

- **Characters seem to float:** add contact shadows under them and match the lighting direction.
- **Background too busy:** reduce contrast and detail, or blur it slightly.
- **Edges flicker:** use thicker lines or higher resolution.
- **Mismatched style:** paint the background with the same brush style and line weight as the characters.
- **Huge files:** reduce image size, merge layers you will not change, and render in sections.

Backgrounds and effects are an excellent area for specialists, so they are good portfolio pieces too."""),
    ],
    diagram=grid([("Smoke", "rises, spreads, fades"), ("Fire", "licks up and splits"), ("Water", "crown, drops, rings"), ("Impact", "flash, smear, dust"), ("Speed", "lines and trails"), ("Wind and rain", "loops in layers")], cols=3, note="Natural effects follow simple rules."),
    caption="Common 2D effects follow simple rules: smoke rises and fades, fire licks upward, water forms crowns and rings, and impacts flash and smear.",
    terms=[("Parallax", "Layers moving at different speeds to create depth."), ("Multiplane camera", "A setup that stacks layers at different distances to create depth."),
           ("Horizon line", "The eye-level line in a perspective drawing."), ("FX", "Effects animation such as smoke, fire, water and impact."),
           ("Smear", "A stretched drawing that shows very fast movement."), ("Compositing", "Combining layers and adjusting them into the final picture.")],
    mistakes=["Painting backgrounds so detailed that the characters get lost.", "Painting a background exactly the size of the frame and then trying to pan.", "Moving the camera with no reason.", "Adding effects before the main animation is approved."],
    quiz=[dict(q="What does parallax create?", o=["Sound", "A sense of depth from layers moving at different speeds", "A new character", "A frame rate"], a=1,
               why="Near layers move more and far layers move less."),
          dict(q="How should a background compare to the character?", o=["Calmer and lower in contrast", "Louder", "Always brighter", "Identical"], a=0,
               why="The character must stand out from the scenery."),
          dict(q="What is a smear?", o=["A stretched drawing that shows fast movement", "A saved file", "A sound effect", "A font"], a=0,
               why="Smears suggest speed in a single frame."),
          dict(q="Why paint a background wider than the frame for a pan?", o=["It is cheaper", "So there is picture to move across", "It improves audio", "It is a rule of colour"], a=1,
               why="A pan needs extra image to travel over.")],
    activity="Paint a three-layer background with a sky, a middle ground and a foreground fence, set a slow pan with eased start and stop, and add one looping smoke effect timed to a character action.",
)

LESSONS[17] = dict(   # Lip-sync and facial animation
    minutes=16,
    hook="When a character speaks, the audience looks at the face. If the mouth moves in time with the voice and the eyes and brows show the feeling, the character seems to think. If the mouth flaps randomly, the illusion breaks at once. Lip-sync, matching mouth shapes to sound, sounds technical, but the secret is that you do not animate letters or even whole words. You animate the **sounds** and the **emotion** behind them. In this lesson you will learn the basic mouth shapes that cover almost every sound, how to read a voice recording frame by frame, how to time the mouth, how to bring the rest of the face to life with eyes, brows and blinks, and which free tools can speed up the work. These steps apply to hand-drawn, cut-out and 3D characters.",
    sections=[
        ("From sounds to mouth shapes", """English has about forty speech sounds, called **phonemes.** Animators group them into a small set of **mouth shapes** (called visemes), often between six and ten:

- **A and I** (as in “father,” “like”): mouth wide open.
- **E** (as in “see,” “bed”): teeth showing, mouth slightly open and wide.
- **O:** a rounded open mouth.
- **U and W:** a small, round, pushed-forward mouth.
- **M, B, P:** lips pressed together. This one is essential: the mouth **must** close.
- **F and V:** the top teeth touch the lower lip.
- **L, TH:** the tongue tip shows behind the teeth.
- **Rest:** a closed or relaxed mouth between words.

You do not need a separate shape for every letter. Many sounds look alike on the lips, so six well-drawn shapes can cover a whole film. Languages such as Yoruba, Igbo, Hausa and Pidgin also use mouth shapes that overlap with these, so **watch and film a real speaker** and animate what the mouth actually does."""),
        ("Reading the recording", """Always work from the **final voice recording,** because timing changes everything.

1. **Listen several times** to learn the rhythm and where the stresses fall.
2. **Mark the beats:** in your software, open the sound **waveform** and mark where each syllable or important sound starts.
3. **Write the dialogue** on an **exposure sheet** (or the timeline) frame by frame.
4. **Find the strongest sounds first,** such as the closing lips for M, B and P, and the wide opening for loud vowels. Draw these as key shapes.
5. **Add in-between shapes** only where needed.

Scrub the audio slowly, so you hear small pieces and see exactly which frame a sound begins. Many animators work **one to two frames ahead:** the mouth shape appears slightly **before** the sound, because we see the mouth move before we hear. A common trick: if it looks late, move it earlier."""),
        ("Timing and style tips", """Good lip-sync is simple and clear:

- **Animate the accents.** Hit the stressed syllables hard, and treat unstressed ones lightly.
- **Do not over-animate.** Fast speech with every shape drawn becomes a blur. Skip tiny sounds and let the mouth hold.
- **Use holds.** A shape held for several frames reads better than constant change.
- **The jaw drives the mouth.** Open and close the jaw first, then add lip shape on top.
- **Mouth and head move together.** A head nod or tilt on a stressed word adds life.
- **Closed shapes matter.** Show M, B and P clearly, even if for only two frames.
- **Match the style.** A bouncy cartoon may use few, big shapes. A realistic 3D face needs subtle control.
- **Think in phrases,** not words. Plan the main shapes for the sentence, then refine.

Play your lip-sync **at full speed** often. It should feel natural, not tick like a clock."""),
        ("The rest of the face", """The mouth is only part of speech. The **eyes and brows** show the thought:

- **Eyes lead:** the eyes often move before the head. They look away when someone is thinking, and return when ready to speak.
- **Eyebrows** are powerful. Raised brows show surprise or a question. Lowered brows show anger or focus. A single raised brow shows doubt.
- **Blinks:** a person blinks every **3 to 5 seconds,** and more often when nervous. A blink on a head turn hides changes. No blinking makes a character look dead.
- **Eye darts:** tiny quick eye movements keep the face alive.
- **Cheeks and nose** move when we smile or frown.
- **Expressions** blend: a smile with sad eyes shows a bittersweet feeling.
- **Hold the emotion** after the line, instead of snapping back to neutral.

Use your own face as **reference** in a mirror or phone camera. Feel what your forehead, eyes and cheeks do when you say the line."""),
        ("Tools, 3D faces and workflow", """You do not have to do every frame by hand:

- **Papagayo-NG** (free) analyses an audio file and gives you phoneme timings. **Rhubarb Lip Sync** (open source) does the same, and exports mouth shape data. Check each tool's current download page and supported formats.
- **Blender** uses **shape keys** (also called blend shapes) to morph a 3D face between expressions. Create keys such as `smile`, `O` and `MBP`, then animate their sliders.
- **Cut-out and Synfig-style rigs** swap mouth drawings on a layer. Make a **mouth library** of the six or more shapes, and switch between them on the timeline.
- **Automatic tools** give a rough first pass. **Always refine by hand,** because machines miss emphasis and emotion.

A practical order: record voice, break it down, block key mouth shapes, add head and eye acting, then smooth and polish. Test with the sound **off,** too. You should still understand how the character feels."""),
    ],
    diagram=grid([("A, I", "wide open mouth"), ("E", "teeth, wide smile"), ("O", "round open"), ("U, W", "small and pushed"), ("M, B, P", "lips pressed shut"), ("F, V", "teeth on lip")], cols=3, note="Six shapes cover most speech."),
    caption="Six basic mouth shapes cover most speech: wide, smile, round, small, closed and teeth-on-lip.",
    terms=[("Phoneme", "A basic sound of speech."), ("Viseme", "The mouth shape that matches a group of sounds."),
           ("Exposure sheet", "A table that lists what happens on each frame, including dialogue."), ("Waveform", "A picture of a sound's loudness over time."),
           ("Shape key", "A saved 3D mesh shape, such as a smile, that you can blend in and out."), ("Hold", "Keeping a mouth shape still for several frames.")],
    mistakes=["Animating every letter instead of the main sounds.", "Forgetting to close the mouth for M, B and P.", "Placing mouth shapes late so they trail the sound.", "Animating the mouth only and leaving eyes and brows dead."],
    quiz=[dict(q="Which sounds require the lips to close?", o=["M, B and P", "A and I", "O", "U"], a=0,
               why="These sounds are made with the lips pressed together."),
          dict(q="Why place mouth shapes one or two frames ahead of the sound?", o=["We see mouth movement slightly before we hear it", "To save time", "To change the frame rate", "It is random"], a=0,
               why="Early shapes read as in sync."),
          dict(q="How often does a person blink, roughly?", o=["Every 3 to 5 seconds", "Every frame", "Never", "Once a minute"], a=0,
               why="Regular blinks keep a character alive."),
          dict(q="What should you do with automatic lip-sync results?", o=["Accept them without checking", "Refine them by hand", "Delete the audio", "Remove the eyes"], a=1,
               why="Automatic results are a first pass, and acting still needs a human.")],
    activity="Record a 10 second line of dialogue, mark the beats on a waveform, draw six mouth shapes and animate the line with head and eye acting, including two blinks and a held expression at the end.",
)

LESSONS[18] = dict(   # Modeling and texturing a simple character
    minutes=17,
    hook="Making a 3D character feels like a mystery until you realise it is a simple trick: you start with a plain shape such as a cube or sphere and push, pull and cut it a little at a time until it becomes a head, a body and a pair of boots. Nobody models in one go. Professionals block out big forms first, refine them in stages and keep the model light enough for a normal computer to handle. Then they paint colours onto it, called texturing, so that cloth looks like cloth and skin looks like skin. In this lesson you will learn the main modelling methods, the vocabulary of polygons, the idea of clean topology that makes later animation easier, the basics of UV unwrapping and materials, and a gentle workflow in free Blender. Menu names and shortcuts change between versions, so use this as a map and check the current Blender manual.",
    sections=[
        ("Meshes: vertices, edges and faces", """A 3D model is a **mesh,** made of three things:

- **Vertices:** points in space.
- **Edges:** lines that join two vertices.
- **Faces:** flat surfaces enclosed by edges. Faces with four sides are called **quads,** and with three sides are **triangles.**

More faces mean more detail, but also a heavier model that is slower to work with and render. The number of faces is the **polygon count.** A simple stylised character may use only a few thousand. A film hero may use hundreds of thousands. For a weak laptop, keep your first character **under about 5,000 faces.**

In Blender you move between **Object Mode** (working with whole objects) and **Edit Mode** (working with vertices, edges and faces). Learn the keys for moving, rotating and scaling, and how to look around the scene. Spend your first hour only on moving the view and selecting things."""),
        ("Box modelling, step by step", """The easiest way to start is **box modelling:**

1. **Collect references:** front and side drawings from your model sheet, set up as background images.
2. **Block out the big shapes** with simple primitives: a cube for the body, a sphere for the head, cylinders for limbs. Get the proportions right first.
3. **Use symmetry.** Model only half of the character and use a **mirror modifier** to create the other half automatically. This halves your work.
4. **Extrude** (pull out new faces) to make arms, legs and feet from the body.
5. **Loop cut** (add a ring of edges) where you need more detail, such as elbows and knees.
6. **Use a subdivision modifier** to smooth the shape, or keep it low poly for a stylised look.
7. **Refine the silhouette** from the front, side and three-quarter views.
8. **Check from every angle,** and keep checking against your reference.

Add detail **last.** Many beginners start with fingers and eyes and never finish the body."""),
        ("Clean topology for animation", """**Topology** is the way edges flow across a model. Good topology deforms nicely when the character moves:

- **Prefer quads.** They subdivide and bend predictably.
- **Add edge loops** around joints such as the elbows, knees, shoulders and mouth, so those areas can bend without stretching.
- **Follow the muscles and form:** edge loops around the eyes and mouth help facial animation.
- **Avoid very long, thin faces** and sudden changes in density.
- **Avoid stray vertices, hidden faces and overlapping parts.** Use the clean-up tools.
- **Apply scale** and check that the model's size is realistic before rigging.
- **Name the parts** (Head, Body, LeftArm) clearly.
- **Keep it watertight:** no holes where the surface should be solid.

A good rule: if you were to bend the elbow, would you see a clean fold or an ugly pinch? Test early by moving a few vertices, and fix before you spend time on texturing."""),
        ("UV unwrapping and materials", """To paint a flat image onto a 3D surface, the surface must be flattened, like peeling an orange. That flat map is called the **UV map.**

1. **Mark seams:** cut lines where the surface will open, in hidden places like under the arms or the back of the head.
2. **Unwrap:** the software flattens the model into UV islands.
3. **Check for stretching:** place a **checker pattern** on the model. Even squares mean a good map.
4. **Pack the islands** efficiently inside the square UV space, so the texture uses all the pixels.

A **material** controls how a surface looks, using settings such as **base colour,** **roughness** (shiny or matte), **metallic** and **normal** (fine bumps). Many stylised characters need only flat colour materials, and you can skip UVs entirely at first. For painted details, use a texture image. A texture size of **1024 by 1024** or **2048 by 2048** pixels is plenty for a student project."""),
        ("Texturing, saving and sharing", """You can texture a character in several ways:

- **Flat colours:** assign a colour to each part. Fast, clean and good for stylised work.
- **Hand painting:** in Blender's Texture Paint mode or in a free painting program such as Krita, paint directly on the model or on the UV map. Keep the style consistent.
- **Image textures and tiling patterns** for cloth, wood and skin. **Only use images you made or have a licence for.**
- **Procedural materials:** made from nodes, with no image needed.
- **Baking:** saving complex lighting or detail into an image to make models lighter.

Good habits:

- **Save versions,** such as `hero_model_v03.blend`, and back up.
- **Pack textures** into the file or keep them in a clear `textures` folder, so nothing goes missing.
- **Render a turnaround** and compare it to the model sheet.
- **Export** for games or other tools in a format they accept, such as glTF or FBX, and test the import.

A first finished character, simple but clean, is far more valuable than a half-finished masterpiece."""),
    ],
    diagram=flow([("Reference", "model sheet views"), ("Block out", "big simple shapes"), ("Refine", "edge loops, mirror"), ("Unwrap", "flatten for paint"), ("Texture", "colour and detail")], "an18", note="Big forms first, detail last."),
    caption="Model a character from reference, block out big shapes, refine, unwrap and then texture.",
    terms=[("Mesh", "The surface of a 3D model made of vertices, edges and faces."), ("Polygon count", "The number of faces in a model."),
           ("Topology", "The way edges flow across a model."), ("Mirror modifier", "A tool that copies one half of a model to the other side."),
           ("UV map", "A flattened version of a 3D surface used to place textures."), ("Material", "The settings that define how a surface looks, such as colour and shininess.")],
    mistakes=["Adding fine detail before the basic shape and proportions are right.", "Modelling both halves by hand instead of using a mirror.", "Leaving messy topology around joints and then struggling to animate.", "Using textures downloaded from the web without checking the licence."],
    quiz=[dict(q="What is the benefit of a mirror modifier?", o=["You model half and get the other half automatically", "It adds colour", "It plays sound", "It renders faster"], a=0,
               why="It halves the work and keeps the model symmetrical."),
          dict(q="What is a UV map?", o=["A flattened version of the surface for placing textures", "A camera setting", "A type of light", "A file backup"], a=0,
               why="UVs tell the software how a flat image wraps around the model."),
          dict(q="Why add edge loops around elbows and knees?", o=["So the joints can bend cleanly", "To add colour", "To make a sound", "To shrink the file"], a=0,
               why="Extra loops give the mesh room to fold smoothly."),
          dict(q="When should you add fine details like fingers?", o=["First", "After the main forms and proportions are right", "Never", "Before reference"], a=1,
               why="Block out big shapes first and refine later.")],
    activity="Model a simple low-poly character under 5,000 faces from your model sheet using box modelling with a mirror modifier, unwrap it, paint flat colour materials, and render a front and side view next to your reference.",
)

LESSONS[19] = dict(   # Rigging and posing
    minutes=17,
    hook="A 3D model is like a statue. It looks fine, but it cannot move. A rig gives it a skeleton and controls, so that an animator can bend an arm or turn a head without touching a single vertex. Rigging sits halfway between art and engineering, and it is one of the most in-demand skills in the industry, because every moving 3D character, in films and games alike, needs a rig someone built. Even a simple rig, done well, lets you pose a character like a puppet and then bring it to life with keyframes. In this lesson you will learn what a rig is made of, how bones and skin weights work, the difference between forward and inverse kinematics, how to build and test a simple rig, and how to pose a character so that it looks alive and not stiff.",
    sections=[
        ("What a rig is made of", """A rig has several parts:

- **Armature (skeleton):** a set of connected **bones** placed inside the model, like a human skeleton.
- **Hierarchy:** bones are connected as parents and children. Move the **parent** (upper arm) and its **children** (forearm, hand) follow. The **root** bone is usually at the hips.
- **Skinning:** attaching the mesh to the bones so that the surface moves with them.
- **Weight painting:** deciding how strongly each bone pulls each vertex. A vertex near the elbow may be 50% upper arm and 50% forearm so it bends smoothly.
- **Controls:** easy-to-grab shapes (circles, boxes) that the animator uses instead of selecting bones directly.
- **Constraints and drivers:** rules that connect parts, such as a foot staying on the ground.

You can build a rig from scratch, or use an automatic helper such as **Rigify** in Blender (an add-on that creates a full human rig). Check the current instructions for your version, and for 2D, cut-out rigs use similar ideas with pivots and parent layers."""),
        ("Forward and inverse kinematics", """There are two ways to move a limb:

- **Forward kinematics (FK):** you rotate each joint from the top down: shoulder, then elbow, then wrist. It gives natural **arcs** and is great for swinging arms, tails and spines. The disadvantage: if the hand must touch something, you have to adjust every joint.
- **Inverse kinematics (IK):** you move the end of the chain (the hand or foot) and the computer works out how the joints must bend. It is perfect for **planting a foot on the ground** or placing a hand on a wall, since the end point stays fixed.

Rigs often let you **switch** between them. Use **IK for legs** that touch the ground, and **FK for arms** that swing freely, though many animators use IK for hands too when they grab things. Add a **pole target** (a control that points the knee or elbow in the right direction) so joints do not flip."""),
        ("Building and testing a simple rig", """A reasonable beginner sequence:

1. **Check the model:** apply scale, name parts, and set the pose to a neutral **T-pose or A-pose.**
2. **Add the armature:** make a spine, neck and head, then arms and legs. Use the **symmetry** tools to mirror one side to the other.
3. **Name bones clearly,** such as `arm.L` and `arm.R`.
4. **Parent the mesh to the armature** with automatic weights.
5. **Test by posing** every joint to extreme positions: raised arms, deep knee bends and head turns.
6. **Fix weight problems:** pinching, spikes and parts that follow the wrong bone. Paint the weights.
7. **Add IK and controls** for hands and feet.
8. **Save a clean, tested version** before animating, and never change the rig halfway through animation without telling the team.

Test often. Rigging problems are cheap to fix at the start and expensive after animation begins."""),
        ("Posing: making a stiff puppet look alive", """A rig is only as good as its poses. Principles:

- **Line of action:** an invisible curve through the body from head to feet that carries the energy. A straight vertical pose looks lifeless.
- **Silhouette:** the outline should read clearly. Rotate and test it in solid black.
- **Weight and balance:** the body's centre of gravity should be over the supporting foot. A character leaning too far without support looks fake.
- **Asymmetry:** avoid perfectly mirrored poses. Tilt the head, drop one shoulder and shift the hips.
- **Overlap in pose:** hands rarely mirror each other. Give each arm a different job.
- **Hands and fingers:** shape matters. Avoid flat open hands.
- **Eyes and head:** decide where the character looks, and let the head, neck and body lead towards it.
- **Contrast between poses:** a clear change between key poses makes movement readable.

Keep a **pose library:** save good poses so you can reuse and study them."""),
        ("Keyframes, the graph editor and polish", """Once a character is rigged:

1. **Block** the key poses at rough timing. This is the **stepped** stage, where poses jump from one to the next with no in-betweens.
2. **Check the timing** at full speed, and adjust.
3. **Switch to spline (smooth) interpolation** so the computer fills in curves.
4. **Open the graph editor.** Each control has **F-curves,** graphs that show value against time. Steep means fast, flat means a hold.
5. **Adjust the curves:** smooth peaks for arcs, and remove sliding. Do not make every curve perfect, because computer movement can look dull.
6. **Offset** parts: move the arms slightly later than the body for follow-through.
7. **Add breakdowns** and secondary motion.
8. **Polish:** eyes, fingers and tiny details come last.

Remember the principles of animation. A rig only gives you the controls, and **acting** is your job."""),
    ],
    diagram=tree("ARMATURE", [("Spine", ["Hips (root)", "Chest", "Head"]), ("Arms", ["Shoulder", "Elbow", "Hand"]), ("Legs", ["Thigh", "Knee", "Foot"])], note="Move the parent and the children follow."),
    caption="A rig is a bone hierarchy: moving a parent bone moves its children, such as shoulder, elbow and hand.",
    terms=[("Rig", "A skeleton and controls that let an animator pose a 3D model."), ("Armature", "The set of bones inside a model."),
           ("Weight painting", "Setting how strongly each bone moves each part of the mesh."), ("Forward kinematics", "Posing a limb by rotating each joint in order from the top."),
           ("Inverse kinematics", "Moving the end of a limb and letting the computer bend the joints."), ("F-curve", "A graph of a value changing over time in the graph editor.")],
    mistakes=["Starting to animate before testing the rig in extreme poses.", "Leaving pinching joints because the weights were never painted.", "Posing in perfect symmetry so the character looks stiff.", "Changing the rig halfway through animation without warning."],
    quiz=[dict(q="What is inverse kinematics useful for?", o=["Planting a foot or hand on a point while the joints adjust", "Changing colours", "Adding sound", "Rendering faster"], a=0,
               why="IK keeps the end of a limb fixed while the rest bends to match."),
          dict(q="What does weight painting control?", o=["How strongly each bone moves each vertex", "The speed of the render", "The colour of the sky", "The audio volume"], a=0,
               why="Weights decide how the skin follows the bones."),
          dict(q="What does a steep part of an F-curve mean?", o=["A hold", "Fast change", "No movement", "A cut"], a=1,
               why="A steep curve means the value changes quickly."),
          dict(q="Why avoid perfectly symmetrical poses?", o=["They look stiff and lifeless", "They use more memory", "They break the rig", "They change the frame rate"], a=0,
               why="Asymmetry gives poses life and personality.")],
    activity="Rig your low-poly character with spine, arms and legs using IK for the feet, test it in ten extreme poses, fix any weight problems and make three strong, asymmetrical poses with a clear silhouette.",
)

LESSONS[20] = dict(   # Lighting, camera and rendering in 3D
    minutes=17,
    hook="You can have a beautiful model and a brilliant animation and still produce a flat, dull image if the lighting and camera are poor. Light shapes what we see, tells us the time of day and the mood, and directs our eyes. The camera decides what is in the frame and how big it feels. Then there is the final step, rendering, where the computer calculates every frame. Rendering can take seconds or hours per frame, which is a serious matter if you have a modest laptop and unreliable electricity. In this lesson you will learn how to light a scene for mood, how to choose lenses and framing, how to manage render settings so that you finish on time, and how to avoid the mistakes that waste days, such as starting a long render with the wrong settings.",
    sections=[
        ("Light that tells the story", """Think of light as a storyteller:

- **Three-point lighting** is the classic setup. The **key light** is the main, brightest light. The **fill light** is softer and reduces harsh shadows. The **rim (back) light** outlines the character and separates them from the background.
- **Direction:** light from the front is flat. Light from the side adds drama and shape. Light from below feels eerie.
- **Hard or soft:** a small, sharp light gives hard shadows. A large, diffused light gives soft shadows. Soft light is kinder to faces.
- **Colour and mood:** warm orange suggests a sunset or safe warmth. Cool blue suggests night, cold or sadness. Contrast between warm and cool is beautiful.
- **Brightness and contrast:** a bright, low-contrast scene feels cheerful. A dark, high-contrast scene feels tense.
- **Natural light:** the sun and sky are your main lights outdoors. A sun at a low angle gives long shadows and golden colour.

Start with **one light** and add others only when they improve the picture."""),
        ("Camera, lenses and composition", """A 3D camera works like a real one:

- **Focal length (lens):** a **wide lens** (about 24 mm) shows more, exaggerates depth and distorts edges. A **normal lens** (about 50 mm) feels natural. A **long (telephoto) lens** (85 mm or more) compresses space and flatters faces.
- **Depth of field:** blurring objects that are not in focus draws attention to the subject. It costs render time, so use it with purpose.
- **Camera height and angle:** low looks heroic, high looks vulnerable.
- **Rule of thirds and leading lines:** place the subject on a third and guide the eye.
- **Framing:** use doorways or trees to frame the subject.
- **Camera movement:** use slow, smooth moves, with easing, and give every move a reason. Handheld shake adds a documentary feel.
- **Safe margins:** keep key elements away from the very edges.

Plan the shots from your **storyboard and animatic,** and check the framing through the camera view, not the free view."""),
        ("Render engines and settings", """Rendering turns the 3D scene into pictures. In Blender, there are two main engines (names and options may change, so check the current manual):

- **Eevee:** a fast, real-time-style engine. It can render a frame in seconds, and is ideal for weaker computers and stylised looks.
- **Cycles:** a physically based path-tracing engine. It gives realistic light and shadows, but takes much longer, and benefits from a good graphics card.

Settings that matter:

1. **Resolution:** draft at **50% (for example 960 by 540)** and render final at the full size.
2. **Samples:** more samples means less noise, but more time. Use a **denoiser** to clean the picture with fewer samples.
3. **Frame range and frame rate:** check them before you press render.
4. **Output format:** render as an **image sequence (PNG)** rather than a video file. If the computer crashes, you keep all finished frames and resume from where it stopped.
5. **Colour management:** keep the default unless you have a reason."""),
        ("Planning render time on a modest computer", """Calculate before you start:

> [Render budget]
> Film length: 60 seconds at 24 fps = 1,440 frames
> Test one frame: 20 seconds
> 1,440 x 20 seconds = 28,800 seconds = 8 hours

If the budget is too high, you can:

- **Lower samples** and use the denoiser.
- **Reduce resolution** for the first full render.
- **Simplify the scene:** fewer lights, smaller textures, no unnecessary reflections.
- **Use Eevee** instead of Cycles for a stylised look.
- **Render only what changes:** split into layers or passes.
- **Use render farms** (online services that rent computing), or free student offers, but check costs, privacy and licence terms first.
- **Plan for power cuts:** render image sequences, keep the machine on a UPS or power bank if you can, and run long renders overnight when power is steady.

**Always test render several frames** from different parts of the film before starting the full job."""),
        ("Checking, passes and compositing", """After rendering:

- **Watch the sequence** at full speed in a player or editor, looking for flicker, noise and glitches.
- **Check a few frames at full size,** for details like eye reflections.
- **Fix problems and re-render only the bad frames.**
- **Render passes** such as the beauty, shadow, depth and mist layers, if you want to adjust the look later without re-rendering. This is an advanced step, so use it only when you need it.
- **Composite and colour-correct** in your editing or compositing program, adding glow, grain or vignette.
- **Keep the original render files** as your master.
- **Document your settings** in a note, so you can match them later.

Lighting, camera and rendering are the finishing touches that make a 3D shot look professional. They reward patience, and testing small, early and often."""),
    ],
    diagram=compare(("DRAFT RENDER", ["Half resolution", "Few samples", "A few test frames", "Minutes to check"]), ("FINAL RENDER", ["Full resolution", "More samples and denoise", "Image sequence", "Hours, plan the time"]), vs="then", note="Test small, then render big."),
    caption="Test with small draft renders first, then run the final render at full resolution as an image sequence.",
    terms=[("Key light", "The main and brightest light in a scene."), ("Focal length", "A lens property that decides how wide or narrow the view is."),
           ("Depth of field", "The blurring of things that are not in focus."), ("Samples", "How many light calculations are made per pixel, affecting noise and render time."),
           ("Denoiser", "A tool that cleans noise from a render, so fewer samples are needed."), ("Image sequence", "A video rendered as a numbered series of pictures.")],
    mistakes=["Starting a full render before testing the settings.", "Rendering to a single video file that is lost if the computer crashes.", "Using many lights when one would do.", "Using a wide lens too close to a face and distorting it."],
    quiz=[dict(q="What is the key light?", o=["The main, brightest light", "The sound mixer", "A camera lens", "A texture"], a=0,
               why="The key light is the main source that shapes the subject."),
          dict(q="Why render an image sequence instead of one video file?", o=["You keep the finished frames if the computer crashes", "It is smaller", "It plays faster", "It adds colour"], a=0,
               why="You can resume from where it stopped."),
          dict(q="What does a long (telephoto) lens do?", o=["Compresses space and flatters faces", "Exaggerates depth", "Adds sound", "Hides the subject"], a=0,
               why="Longer lenses give a compressed, pleasing look to faces."),
          dict(q="How can you predict render time?", o=["Guess", "Time one test frame and multiply by the number of frames", "Wait and see", "Ask the camera"], a=1,
               why="A simple test gives a reliable estimate for planning.")],
    activity="Light one shot with a key, fill and rim light, set the camera with a 50 mm lens, test render at half size, time one frame, calculate the full render time and render the shot as a PNG sequence.",
)

LESSONS[21] = dict(   # Music, voice and sound design
    minutes=16,
    hook="Close your eyes during a great animated film and you can still follow the story: the footsteps tell you who is coming, the music tells you how to feel and the voice tells you who is speaking and what they want. Audiences forgive rough pictures far more easily than bad sound. A crackling, muffled voice makes a film feel amateur at once, while clean dialogue with a simple, well-chosen sound track makes simple animation feel professional. You learned the four layers of sound and the idea of mixing earlier. In this lesson you will put that into practice: how to record clear voices with a phone, how to direct a performer, how to find or make music legally, how to build a sound effects library and how to mix everything so that every word can be understood.",
    sections=[
        ("Recording clear voices with a phone", """You do not need a studio. You need a **quiet place and good habits:**

1. **Choose a quiet room** with soft things that absorb echo: a bedroom with a mattress, curtains, clothes in a wardrobe. Switch off fans and generators if you can, and record at a time of day with less noise.
2. **Mouth 10 to 20 cm from the microphone,** a little off to the side to avoid breathing noises and harsh P and B sounds. A **sock or foam over the microphone** or a pop filter helps.
3. **Use a headset or phone microphone** closer to the mouth, rather than a laptop speaker far away. A cheap wired microphone is a good investment.
4. **Record a few seconds of silence** (room tone) to help remove noise later.
5. **Do a test and listen with headphones** before recording everything.
6. **Record several takes** of each line with different energy.
7. **Save in WAV** or a high-quality format. Avoid heavy compression at this stage.

Watch your levels: loud enough to be clear, but never so loud that the sound **distorts** (clips)."""),
        ("Directing a voice performance", """A good voice performance creates the character:

- **Give the actor the context:** who they are, what they want, what just happened.
- **Read the script together** and explain the emotion, not only the words.
- **Use real situations.** Ask a performer to stand, move and act while speaking. A sleepy voice reads from a sleepy body.
- **Record more takes than you need,** and give kind, specific direction: “a little more worried,” “faster.”
- **Keep each line in a separate file** with a clear name, such as `sc03_kemi_line02_take3.wav`.
- **Get permission in writing.** Agree how and where the voice will be used, whether the actor is paid, and whether they are credited. Never copy or clone someone's voice without their consent. Their voice is part of their identity.
- **Children as voice actors:** get a parent's or guardian's permission, and protect them.
- **Languages and accents:** use performers who really speak the language, and respect the culture.

Always **thank and credit** your performers."""),
        ("Finding and making music", """Music sets the heart of the film. Options:

- **Compose it yourself** with free tools such as **LMMS** or **BeepBox,** or record instruments you play.
- **Work with a local musician or producer.** Nigeria has remarkable talent, and a clear written agreement protects both sides: payment, credit, ownership, and where the film may be shown.
- **Use properly licensed music:** royalty-free libraries, Creative Commons tracks and music marketplaces. **Read the licence:** some need credit, some forbid commercial use, and some limit the platforms where you can use the track.
- **Never use commercial songs** without permission, even for ten seconds. Video platforms scan for copyright and can block, demonetise or remove your film.
- **Use a temp track** while editing, but replace it before release.
- **Keep the music supportive.** It should serve the scene, not fight with dialogue. Often, **less music is better.** Let silence do some work.
- **Match tempo and mood** to the picture, and cut the music to the edit, not the other way round.

Keep a list of every track: title, creator, source, licence and where you downloaded it."""),
        ("Building your sound effects", """Sound effects (SFX) make the world real:

- **Hard effects:** doors, impacts, vehicles. **Foley:** everyday sounds recorded in sync with the picture, such as footsteps, cloth movement and objects handled. **Backgrounds (ambience):** the constant sound of a place, such as market chatter, traffic, wind or crickets.
- **Record your own.** A bag of rice for rain, a stick of celery for a bone crunch, walking on gravel in different shoes, a bucket of water. Always record **cleaner and closer** than you expect.
- **Use sound libraries** with correct licences, and keep credits.
- **Layer sounds:** a punch might be a thud, a whoosh and a cloth rustle together.
- **Cartoon sounds** can be exaggerated: boings, zips and whistles. Keep them in the same style.
- **Sync precisely:** place the sound on the exact frame of contact. Even two frames late feels wrong.
- **Silence before an impact** can make it hit harder.
- **Cut sound** at the start and end so there is no click.

A small library of 50 well-chosen sounds can cover a short film."""),
        ("Mixing so every word is heard", """A mix balances all the sound layers:

- **Dialogue comes first.** Every word must be clear. Everything else sits underneath it.
- **Lower the music** while people speak (called **ducking**) and raise it in gaps.
- **Balance effects** so they support, not drown, the story.
- **Use panning** (left and right placement) where it helps. Keep dialogue mostly in the centre.
- **Clean the voice:** remove noise, reduce harsh sounds and add a little gentle equalisation, using **Audacity** or your editor. Do not over-process.
- **Keep consistent loudness.** A common target for online video is around **minus 14 LUFS,** but check the current guidelines of the platform you use.
- **Avoid clipping:** peaks should stay below 0 dB.
- **Test on different speakers:** phone speaker, earphones and a laptop. Most of your audience listens on phones.
- **Listen after a break** with fresh ears, and ask someone else to listen too.

Export a clean **stereo WAV** at 48 kHz for the final edit."""),
    ],
    diagram=triangle([("DIALOGUE", "always clear"), ("MUSIC", "supports mood"), ("EFFECTS", "make it real")], middle="clean|mix", note="Voices first, the rest underneath."),
    caption="A good mix balances dialogue, music and effects, with the voice always clear.",
    terms=[("Room tone", "The quiet sound of a room, recorded so noise can be matched or removed."), ("Foley", "Everyday sound effects recorded in sync with the picture."),
           ("Ambience", "The background sound of a place."), ("Ducking", "Lowering music or effects while someone speaks."),
           ("Clipping", "Distortion that happens when a recording is too loud."), ("LUFS", "A unit used to measure perceived loudness.")],
    mistakes=["Recording in a noisy or echoey room.", "Using a commercial song without permission.", "Letting music drown the dialogue.", "Cloning or using someone's voice without their consent."],
    quiz=[dict(q="What should come first in a mix?", o=["Dialogue, which must be clear", "Music at maximum", "Effects at maximum", "Silence"], a=0,
               why="If the audience cannot understand the words, the story is lost."),
          dict(q="What is ducking?", o=["Lowering the music while someone speaks", "A kind of microphone", "A camera move", "A file type"], a=0,
               why="Ducking keeps the voice on top of the music."),
          dict(q="Why get a voice actor's permission in writing?", o=["It sets how their voice may be used and paid", "It improves the sound", "It reduces file size", "It is a camera rule"], a=0,
               why="A voice is part of someone's identity, and agreements prevent disputes."),
          dict(q="What happens if you use a famous song without a licence?", o=["Nothing ever", "The video may be blocked or removed", "It sounds better", "It becomes yours"], a=1,
               why="Platforms scan for copyright and can block or remove content.")],
    activity="Record a 15 second line with a phone in a quiet room, clean it in Audacity, add room tone, two foley effects and a licensed music bed with ducking, and test the mix on a phone speaker and earphones.",
)

LESSONS[22] = dict(   # Using AI tools responsibly: ethics, rights and credit
    minutes=15,
    hook="AI tools can now draw backgrounds, animate still pictures, write scripts and imitate voices in minutes. For a young animator with little money, this feels like a gift, and in many ways it is. But there are real questions behind every click: Where did the training images come from? Who owns the result? Are you allowed to sell it? Whose voice or face is being copied? Will you take work away from a fellow artist, or will you create new work? And how will your audience feel if you do not tell them? The earlier lesson showed where AI can help an animation workflow and where you must stay in charge. This lesson goes into the ethics, rights and credit in more depth, and gives you a simple checklist you can use on every project. Laws and tool terms are changing quickly and differ by country, so this is guidance, not legal advice.",
    sections=[
        ("Why this matters", """Responsible use protects **you, your clients, other artists and your audience.**

- **You** can be blocked, sued, or lose your reputation if you use content you had no right to.
- **Clients** expect work they can legally use. A single copyright complaint can cost them money.
- **Other artists** worry that their work was used to train systems without permission, and that AI tools may reduce paid work.
- **Audiences** deserve honesty about what they are watching.

At the same time, AI is **a tool,** like a camera or software. It does not remove the need for ideas, taste and craft. Animators who understand both the opportunities and the limits will be the most trusted and the most employable. Ethical habits are part of professional skill."""),
        ("Copyright, ownership and terms of use", """The rules are **unsettled and differ between countries.** Key points to understand:

- **Training data:** many AI tools were trained on large collections of images, text, voices and video. Courts and lawmakers in different countries are still deciding what is allowed. Some tools say they train only on licensed or permitted data, and some do not. Read each company's statements.
- **Who owns the output?** In several countries, copyright protects only works with **real human authorship,** so purely machine-generated content may have **weak or no protection,** while work in which a person makes creative choices may be protected in part. This is changing, so check current guidance.
- **Terms of service decide a lot.** They may say who owns outputs, whether **commercial use** is allowed, which **plan** you need, and what you may not do. A free plan may forbid commercial use, or require credit.
- **Never ask for an artist's or a famous character's style or likeness** in a way that copies their work, and never present the output as hand-made by you if it was not.
- **Keep records:** screenshots of settings and the plan you used, the prompts, the date and the tool and version.

When a client pays you, **tell them in writing** which parts were AI-assisted, and ask whether that is acceptable."""),
        ("Voices, faces and consent", """Some uses are **never acceptable,** because they harm real people:

- **Voice cloning:** do not copy a real person's voice, whether a celebrity, a teacher or a friend, without clear permission. It can be used for fraud and harassment.
- **Faces and likeness:** do not make images or videos of real people doing or saying things they did not do. **Deepfakes** can hurt reputations, and in many places creating or sharing harmful ones is a crime.
- **Children:** never create sexual or harmful content involving children. Be especially careful with any image of a child.
- **Personal data:** do not upload private photos, other people's documents or client secrets to online tools without permission. Check how the company stores and uses what you upload. In Nigeria, the **NDPA 2023** protects personal data, so collect and share only what you are allowed to.
- **Consent for performers:** if an actor's voice is used to train or drive a tool, agree this in writing.

If you are unsure, **do not do it,** or ask the person involved. A consent form takes five minutes. A scandal takes years to fix."""),
        ("Fairness, bias and quality", """AI systems reflect the data they learned from, and so they can carry **bias.**

- **Representation:** tools may default to narrow looks, such as lighter skin, Western clothing, or stereotypes about Africans. Check outputs and correct them with careful prompts and real references, and consult people from the culture you show.
- **Respect artists:** do not use AI to undercut fellow artists by copying their style and offering the work for almost nothing. Hire and credit human artists where you can, especially for the heart of the film.
- **Check accuracy and quality.** AI can make visual mistakes, such as extra fingers, shifting faces and wrong text. It can also invent facts in scripts. **You are responsible for what you publish.**
- **Be mindful of cost and resources.** Large models use a lot of energy and often money. Use them with purpose, not for endless random tries.
- **Keep your own skills growing.** Use AI to speed up routine steps, not to avoid learning the craft."""),
        ("A responsible-use checklist", """Use this on every project:

1. **Purpose:** what exactly will AI do, and why is it the right tool?
2. **Terms:** have I read the tool's terms, plan and commercial-use rules?
3. **Inputs:** do I own or have permission for every image, voice and text I upload?
4. **People:** is any real person's face, voice or name involved? Do I have their consent?
5. **Originality:** am I avoiding copying a living artist's style or a protected character?
6. **Human control:** have I reviewed, edited and made creative choices myself?
7. **Records:** have I logged prompts, tools, dates and plans in a **use log?**
8. **Credit and disclosure:** have I told my client, audience and platform which parts used AI? Some platforms require labels on realistic AI content.
9. **Review:** have I checked the final work for bias, mistakes and harm?
10. **Plan B:** if a problem appears, can I replace the AI part quickly?

Add a clear **credits line,** such as “Backgrounds created with AI assistance, then painted and edited by [your name].” Transparency builds trust."""),
    ],
    diagram=compare(("SAFER PRACTICE", ["Read the tool's terms", "Get written consent", "Keep a use log", "Disclose AI use", "Edit and add your craft"]), ("RISKY PRACTICE", ["Copy an artist's style", "Clone a real voice", "Hide that AI was used", "Upload private files", "Publish unchecked output"]), vs="vs", note="Transparency builds trust."),
    caption="Safer practice reads terms, gets consent, keeps a log and discloses. Risky practice copies, clones, hides and skips checks.",
    terms=[("Training data", "The collection of images, text or sounds an AI system learned from."), ("Human authorship", "Creative work made by a person, which many copyright laws require for protection."),
           ("Terms of service", "A tool's rules about what you may do and who owns the output."), ("Deepfake", "A fake image, video or audio that makes a real person appear to say or do something they did not."),
           ("Use log", "A record of which AI tools, prompts, dates and plans you used."), ("Disclosure", "Telling others that AI was used in the work.")],
    mistakes=["Using a free plan for a commercial job without checking the terms.", "Cloning a real person's voice without permission.", "Hiding AI use from a client who asked for original art.", "Uploading private photos or client files to an online tool."],
    quiz=[dict(q="Why keep a use log?", o=["To prove which tools, prompts and plans you used", "To make the film longer", "To change the frame rate", "To reduce file size"], a=0,
               why="Records protect you if someone asks how a piece was made."),
          dict(q="What should you do before using AI output in a paid job?", o=["Nothing", "Check the tool's terms for commercial use and tell the client", "Delete the prompts", "Hide it"], a=1,
               why="Terms and honesty with the client prevent legal and trust problems."),
          dict(q="Is it acceptable to clone a real person's voice without permission?", o=["Yes, always", "No, it needs clear consent", "Only on weekends", "Only for short clips"], a=1,
               why="Voice is part of identity, and unauthorised cloning can cause harm."),
          dict(q="Who is responsible for the quality and accuracy of what you publish?", o=["The AI company", "You", "Nobody", "The audience"], a=1,
               why="Whatever tools you use, you are the author who publishes the work.")],
    activity="Pick an AI tool you might use, read its terms and write down who owns outputs, whether commercial use is allowed and what the free plan permits. Then write a credits line and a use log template for your next project.",
)

LESSONS[23] = dict(   # Editing, colour and final export
    minutes=16,
    hook="You have animated all the shots, painted the backgrounds and recorded the sound. Now comes the stage that turns a pile of clips into a film: the edit. Editing decides rhythm, emotion and clarity. A great edit makes animation feel inevitable, and a rushed one makes good animation feel clumsy. After that comes colour, which gives all your shots one consistent look, and finally export, where many beginners lose hours by choosing the wrong settings and producing blurry, huge or unplayable files. In this lesson you will learn how to assemble and trim a film, cut on action and pace to music, fix and grade colour, add titles, credits and subtitles, and export a high-quality master and smaller copies that play well on phones with limited data.",
    sections=[
        ("Assembling the cut", """Work in a video editor such as **DaVinci Resolve, Kdenlive** or **Shotcut** (check each tool's current version and licence).

1. **Import** your final renders, sound and the locked animatic.
2. **Replace the animatic panels** with finished shots, in order.
3. **Match the timeline** to the project settings: same frame rate and resolution as your animation.
4. **Trim shots:** cut the start and end tightly. Keep only what the story needs.
5. **Watch the whole film** from start to finish before fine tuning. Take notes.
6. **Fix pacing:** shorten slow bits, hold the important moments a little longer.
7. **Save often** and keep numbered project versions.

Do not be afraid to **cut shots you love** if they slow the story. The best edits are often shorter than the first assembly."""),
        ("The craft of cutting", """Basic techniques that make a cut feel invisible:

- **Cut on action:** change shots in the middle of a movement, such as a hand reaching for a door, so the eye follows smoothly.
- **Match the eye line and screen direction** you planned in the storyboard.
- **Vary shot size:** alternate wide, medium and close to keep interest.
- **Let moments breathe:** hold on a reaction for a beat before cutting away.
- **Pace to the music or the dialogue,** with cuts on beats or between phrases.
- **J-cuts and L-cuts:** let the sound of the next shot begin a little **before** the picture (J-cut), or let the sound of the previous shot continue after the picture changes (L-cut). This makes scenes flow.
- **Transitions:** use **cuts** by default. A **dissolve** or **fade** can show time passing. Avoid flashy wipes unless they suit the style.
- **Time:** shorten what is boring and lengthen what is emotional.

Always ask, “What does the audience need to see and feel next?”"""),
        ("Colour correction and grading", """**Colour correction** fixes problems and makes shots **match.** **Colour grading** adds a creative look.

1. **Fix exposure** so the shot is neither too dark nor washed out. Use the **scopes** (waveform and histogram) to see brightness values, instead of trusting your eyes only. Screens differ, and your eyes adapt.
2. **Set white and black points** for a full range of tones.
3. **Match shots** across the film, so that a character does not change colour from one scene to the next. Compare two shots side by side.
4. **Grade for mood:** warm tones for comfort, cooler tones for night or sadness. Keep skin tones believable and respectful to every skin colour.
5. **Keep it consistent** with the palette you chose in design.
6. **Do not overdo it.** Subtle changes usually look best.
7. **Check on several screens,** especially a phone at medium brightness.

Because animated shots are made by you, the easiest approach is to **keep colours consistent during animation,** and use grading for small fine tuning and a unified finish."""),
        ("Titles, credits and subtitles", """Text on screen must be readable:

- **Titles and credits:** use a simple, clear font. Check the **font licence** before using it. Keep text inside the **safe area,** away from the edges.
- **Credits matter.** List everyone who helped, including voice actors, musicians, testers and any asset creators whose licences require credit. Place AI-assistance credits there too, if used.
- **Duration:** credits should be slow enough to read. Short films often show them over a still or the final shot.
- **Subtitles and captions:** they help viewers who are deaf, hard of hearing, in a noisy bus or watching without sound, and those who speak another language. A film in Yoruba or Pidgin with English subtitles can reach far more people. Create them in your editor or write an **SRT** file.
- **Contrast and size:** white text with a thin dark outline or box is readable on most pictures.
- **Spelling:** proofread everything twice, especially names.
- **Copyright notice and contact:** add year and name, and a way to reach you, if you wish."""),
        ("Export: master, copies and checking", """Exporting means turning your project into a video file. Do it in two steps:

1. **Export a master:** the highest quality version, at full resolution (for example **1920 by 1080**) at your project frame rate, with a **high bitrate** or a lossless or near-lossless format, plus 48 kHz audio. Keep this file **safe forever.** It is your source for every other copy.
2. **Make delivery copies from the master:**
   - **Web and YouTube:** **H.264 in an MP4** container, 1080p, with a sensible bitrate. Most platforms recommend settings, so check their current guidance.
   - **WhatsApp and mobile:** a smaller **720p** version with lower bitrate, so it downloads quickly with limited data.
   - **Social media:** vertical or square crops if needed, with titles placed safely.
   - **Festivals:** follow each festival's rules for format and length.
3. **Check every file:** play the whole film on a computer and a phone, with sound. Look for black frames, sound drift, cut-off text and wrong aspect ratio.
4. **Name files clearly:** `MyShort_v03_master_1080p24.mp4`.
5. **Archive the project:** keep the project files, assets and a README, and back up in two places."""),
    ],
    diagram=flow([("Assemble", "shots in order"), ("Cut", "trim and pace"), ("Sound", "mix to picture"), ("Colour", "match and grade"), ("Export", "master first")], "an23", note="Always keep a master."),
    caption="Assemble, cut, finish the sound, colour and export a master first, then make smaller delivery copies.",
    terms=[("Cut on action", "Changing shots during a movement so the edit feels smooth."), ("J-cut and L-cut", "Edits where the sound and picture change at different times."),
           ("Colour correction", "Fixing exposure and colour so shots match."), ("Colour grading", "Creating a creative look with colour."),
           ("Bitrate", "How much data is used per second of video, which affects quality and size."), ("Master file", "The highest quality export, kept as the source for all copies.")],
    mistakes=["Exporting only a small compressed file and losing the high-quality master.", "Using a font without checking its licence.", "Putting titles at the very edge where they may be cropped.", "Never watching the finished export on a phone."],
    quiz=[dict(q="What is a master file?", o=["The highest quality export, kept as the source for copies", "A tiny preview", "A caption file", "A sound effect"], a=0,
               why="All delivery versions should be made from the master."),
          dict(q="What is a J-cut?", o=["A cut that deletes sound", "A colour effect", "The next shot's sound starts before the picture changes", "A title style"], a=2,
               why="J-cuts and L-cuts make scenes flow by overlapping sound and picture."),
          dict(q="Why make a 720p copy?", o=["It improves colour", "It downloads faster and uses less data", "It is required by law", "It adds subtitles"], a=1,
               why="Smaller files suit slow connections and limited data."),
          dict(q="Why add subtitles?", o=["They help deaf viewers, noisy places and other languages", "They hide the picture", "They remove audio", "They speed up export"], a=0,
               why="Subtitles make your film accessible to more people.")],
    activity="Assemble your finished shots with sound, cut on action, match the colours, add titles with credits and English subtitles, export a 1080p master and a 720p copy, then watch both on a phone and write down any problems.",
)

LESSONS[24] = dict(   # Showreel, portfolio and finding work
    minutes=15,
    hook="Making animation is one skill. Being found, trusted and paid for it is another. Many talented animators, in Lagos and everywhere else, stay unknown because they never learned how to show their work or where to look for opportunities. The good news is that animation is one of the few creative careers where your work can be sent anywhere in the world with a link, and where studios, agencies and clients care much more about what you can show than about a certificate. The earlier lesson explained how to cut a showreel and build a portfolio page. In this lesson you will map the careers that exist, choose a focus, tailor your reel for each role, learn the basics of freelancing, pricing and contracts, get paid across borders safely and plan a steady path from learner to professional. No one can guarantee a job, but a clear plan and visible work improve your chances a great deal.",
    sections=[
        ("The careers in animation", """Animation is a family of jobs. Common roles:

- **2D animator:** draws movement for characters and effects.
- **3D animator:** poses and animates rigged characters and objects.
- **Character designer, background artist, storyboard artist:** the pre-production roles you have practised.
- **Rigger and technical artist:** builds the controls and tools that make animation possible.
- **Modeler, texture and lighting artist:** build and light the 3D world.
- **Motion graphics artist:** animated logos, titles, explainers and adverts, in constant demand from businesses.
- **VFX artist:** effects, compositing and clean-up.
- **Game animator:** animations for characters in games, a fast-growing area in Africa.
- **Explainer and educational video maker:** simple animated videos for schools, companies and NGOs.
- **Editor, sound designer and composer:** finishing roles.
- **Director, producer and writer:** leadership roles that often grow from experience.

Employers also hire in advertising agencies, TV, streaming, education, fintech and social media. Research the studios and creators in Nigeria, Africa and online, since the field changes quickly."""),
        ("Choose a focus and tailor your showreel", """Specialising makes you easier to hire. After trying many things, pick **one main focus,** for example character animation, motion graphics or backgrounds.

**Showreel tips (revisiting and extending the basics):**

1. **Show only your best work.** Five great seconds are better than a mediocre minute.
2. **Open with your strongest shot** within the first few seconds, and end with a strong one.
3. **Keep it short:** 30 to 90 seconds.
4. **Match the role:** an animator's reel shows acting and movement, with simple backgrounds. A motion graphics reel shows design and timing.
5. **Add a shot list** or breakdown with what you did on each shot, particularly if you worked in a team.
6. **Credit others** for work that is not yours.
7. **Use clean music** you have rights to.
8. **Put your name and contact** at the start and the end.
9. **Make several versions:** a 30 second social cut, a longer reel for studios and a role-specific reel for each application.
10. **Update it** every few months, removing weaker pieces."""),
        ("Portfolio, presence and networking", """Make it easy to find and judge you:

- **A simple portfolio website** or page, with your reel at the top, project pages, a short bio and a clear contact. Keep the design plain and fast to load on mobile data.
- **Project pages** that explain the brief, your role, tools, and process, with sketches and breakdowns. Show how you think.
- **Social media:** share short clips, progress, and lessons learned. Post regularly. Be kind and professional.
- **Communities:** join local and online animation groups, game developer groups and festivals. Ask for feedback, give feedback, and help beginners.
- **Challenges and contests:** monthly animation challenges give deadlines and exposure.
- **Mentors:** find someone more experienced and ask specific questions. Respect their time.
- **Festivals and competitions:** submit your short film, and read each festival's rules and fees carefully. Avoid sites that charge high fees with no real reputation.

Every public post is part of your **reputation,** so credit sources, tell the truth and be reliable."""),
        ("Freelancing, pricing and contracts", """Many animators start with small paid projects:

- **Where work comes from:** local businesses, schools, churches, musicians, start-ups, NGOs and friends of friends. Also freelance platforms and job boards, where competition is strong.
- **Start small:** a 30 second explainer, a logo animation, a lyric video, social media animation.
- **Pricing:** price by **the value and the time you will spend,** not only by seconds of film. Estimate hours, add time for revisions, and add a profit margin. Research what other animators charge in your market, and do not work for free for companies that can pay. Prices vary widely, so use ranges and revise them as your skills grow.
- **Write a clear quote:** what is included, how many rounds of **revisions,** the deadline, and the price.
- **Use a simple contract,** even for small jobs: scope, price, payment dates, who owns the final work, credit, and what happens if the client cancels. Ask a lawyer to review a template.
- **Ask for a deposit** (such as half) before starting.
- **Keep records and invoices,** and learn the basics of tax for freelancers in Nigeria. Speak to an accountant.
- **Communicate often** and deliver on time."""),
        ("Getting paid and growing safely", """Practical points:

- **Payments:** for Nigerian clients, bank transfer is common. For clients abroad, look at **international payment services that support Nigeria,** and check their fees, exchange rates and limits. Check the current options, since they change.
- **Avoid scams.** Be careful with anyone who sends a cheque or transfer for **more** than the agreed amount and asks you to return the difference, who asks you to pay a fee to get a job, who wants to move to a private chat and avoid contracts, or who offers huge pay for little work. Never share your bank passwords or one-time codes.
- **Protect your work:** deliver watermarked previews and give final files after payment.
- **Look after yourself:** deadlines can be tough. Rest, protect your eyes and back, and keep a work routine. Say no to unfair terms.
- **Keep learning:** new tools appear each year. Follow tutorials, study great films frame by frame, and keep a **personal project** going.
- **Plan your path:** in the first year, finish three polished shorts, build a reel, and apply or pitch to ten places. In the second, specialise, join a team or build steady clients.

Be patient and keep showing your work. Opportunities go to people who are visible, reliable and kind."""),
    ],
    diagram=hub(("ANIMATION CAREERS", "pick a focus"), [("2D animator", "drawn movement"), ("3D animator", "rigged characters"), ("Motion graphics", "ads and explainers"), ("Storyboard", "plan the shots"), ("Game animator", "animation for games"), ("VFX and FX", "effects and compositing")], note="Choose one main focus, then tailor your reel."),
    caption="Animation careers include 2D and 3D animation, motion graphics, storyboards, games and effects. Pick a main focus.",
    terms=[("Showreel", "A short video of your best animation work."), ("Portfolio", "A collection of your projects, usually on a website."),
           ("Freelancer", "Someone who works for different clients on separate projects."), ("Revision round", "A set of changes a client asks for after seeing a draft."),
           ("Deposit", "Part of the payment made before work begins."), ("Motion graphics", "Animated text, logos and graphic design for video.")],
    mistakes=["Filling the showreel with weak work to make it longer.", "Working without a written agreement or deposit.", "Accepting payment arrangements that ask you to send money back.", "Never updating the showreel after improving."],
    quiz=[dict(q="How long should a typical showreel be?", o=["About 30 to 90 seconds", "Ten minutes", "Ten seconds always", "One hour"], a=0,
               why="Short reels respect viewers' time and show only your best work."),
          dict(q="Which is a warning sign of a scam?", o=["A signed contract", "A deposit paid correctly", "A client sends extra money and asks you to return the difference", "A clear brief"], a=2,
               why="Overpayment scams rely on you returning money before the payment fails."),
          dict(q="Why ask for a deposit?", o=["It speeds up your computer", "It shows commitment and covers early work", "It is a tax", "It changes the film"], a=1,
               why="A deposit reduces the risk of working without payment."),
          dict(q="What helps you get hired faster?", o=["Showing a focused reel for the role", "Showing everything you ever made", "No contact details", "A very long website"], a=0,
               why="A reel tailored to a role shows exactly what an employer needs.")],
    activity="Choose your main focus, cut a 45 second reel with your best three shots and a shot breakdown, build a one-page portfolio with contact details, and write a quote template with scope, revisions, deposit and deadline.",
)
