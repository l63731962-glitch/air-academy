"""2D Animation track: lessons 6 to 15, added when the track grew from 5 to 15 lessons (course_plan.py says where each one sits on screen).
Same format as lessons_2d_animation.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option.
Software is named only as examples. Menu names and features change between versions, so lessons point learners to the tool's current manual."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[6] = dict(   # Setting up free 2D animation software
    minutes=15,
    hook="Every animator, from a school student to a studio artist, starts the same way: opening a blank canvas and a blank timeline. The good news is that you do not need to spend money. Several free programs can make complete 2D animations, and you can install one in a few minutes. The harder part is knowing which to choose, setting it up so it does not fight you later and learning the five or six controls that you will use every day. In this lesson you will compare the free tools, install one safely, create a project with the right canvas size and frame rate, learn the timeline, layers and onion skin, draw and play a short loop, and export it as an image sequence, a GIF and a video. You will also learn how to protect your work from crashes and power cuts.",
    sections=[
        ("Choose one free program", """Names, versions and features change, so always check the official website. Good free options:

- **Krita:** a full painting program with an animation workspace, a timeline and onion skin. Great drawing brushes. Slightly heavier on old computers.
- **Pencil2D:** very light and simple, made for hand-drawn animation. It runs on weak laptops and is perfect for learning.
- **OpenToonz** and **Tahoma2D:** professional-grade tools that have been used in studios. More powerful, with a steeper learning curve.
- **Synfig Studio:** vector and cut-out animation, with automatic in-betweening.
- **Blender Grease Pencil:** draw in a 3D program, useful if you also want 3D later.

**Our advice:** start with **Pencil2D** if your computer is modest, or **Krita** if you want beautiful brushes. Pick **one** and stay with it for this track. The animation ideas are the same everywhere. Download only from the **official website,** and avoid cracked paid programs, which often hide malware."""),
        ("Install and prepare your computer", """A simple setup routine:

1. **Check your system:** how much memory and free disk space do you have? Aim for at least 4 GB of memory and 5 GB of free space for small projects.
2. **Download the installer** from the official site. If data is costly, download at a library or school, or ask a friend to share the installer on a USB drive.
3. **Install it** and open it. If it asks about updates, you can postpone them, but note the version number.
4. **Look for the autosave setting** and turn it on, with a short interval, such as every five minutes. Nigerian power cuts make this essential.
5. **Create a folder** for your course projects, with a clear name such as `2D_Animation_Course`.
6. **Pick an input device:** a mouse is fine. A **drawing tablet** helps greatly, and some people use a phone or a spare tablet as a display for sketching ideas.
7. **Learn three shortcuts:** undo, save and play. Write them on a sticky note."""),
        ("Create a project with the right settings", """Choose these settings **before** drawing and never change them halfway:

- **Canvas size:** **1280 by 720 pixels** is a good size for learning, because it is light and clear on phones. Use 1920 by 1080 later for finished films.
- **Frame rate:** **24 fps** is the film standard. For simple learning exercises, 12 fps with each drawing held for two frames is also fine.
- **Background:** keep it **transparent** or white for the animation layer, and put colours on a separate layer.
- **Project name and folder:** save as `bounce_v01` in your course folder.

Many programs ask you to choose a **colour profile.** Keep the default sRGB. If you will make more than a few seconds of animation, keep the **canvas size the same across all scenes.** Write your settings in a small text file in the project folder, so you remember them next week."""),
        ("The timeline, layers and onion skin", """Every 2D animation program has the same three core tools:

- **The timeline** is a row of boxes, one for each frame. You draw on a frame, and press play to see the sequence. Hold a drawing by extending it across several frames.
- **Layers** are transparent sheets stacked on top of each other. Put the **character** on one layer and the **background** on another, so you can change one without redrawing the other. Name every layer.
- **Onion skin** shows faint copies of the previous and next frames, in colours such as red and green, so you can see where the drawing was and where it will go. It is how you keep movement smooth.

Other useful controls: **Play and loop,** **frame rate** and **scrubbing** (dragging the playhead to look at frames). Spend your first practice session only on moving around: add a frame, draw, go back, copy a frame, delete one, and play."""),
        ("Your first loop and your first export", """Draw a **12-frame bouncing ball loop** to test your setup:

1. Make a new layer called `ball`.
2. On **frame 1** draw the ball high up. On **frame 7** draw it at the bottom, squashed slightly.
3. On **frame 12** draw it near the top again. Fill the gaps in between with in-betweens, using onion skin.
4. Turn on **loop** and press play.

Then export it three ways, to learn what each is for:

- **Image sequence (PNG):** numbered pictures like `ball_0001.png`. This is the **safest master,** because if a video export fails you still have every frame.
- **GIF:** a small looping picture for chats and websites.
- **MP4 video (H.264):** good for sharing. If your program asks for an extra helper tool such as **FFmpeg,** follow its current manual, or export PNG frames and build the video in a free editor.

**Save your project** and make a **backup copy** on a second device. Name versions, such as `bounce_v02`."""),
    ],
    diagram=flow([("Install", "official site only"), ("Project", "720p, 24 fps"), ("Timeline", "frames and layers"), ("Draw", "use onion skin"), ("Export", "PNG, GIF, MP4")], "t6", note="Set up once, then animate."),
    caption="Install from the official site, set the project once, learn the timeline and onion skin, draw a loop and export it.",
    terms=[("Timeline", "The row of frames where you draw and arrange an animation."), ("Layer", "A transparent sheet that holds part of the picture."),
           ("Onion skin", "Faint copies of nearby frames shown to help you draw smooth movement."), ("Image sequence", "A series of numbered pictures that make up the animation."),
           ("Autosave", "A feature that saves your work automatically at regular times."), ("Frame rate", "How many frames play in one second.")],
    mistakes=["Downloading cracked software from unofficial sites.", "Changing canvas size or frame rate halfway through a project.", "Putting the character and background on one layer.", "Exporting only a video and keeping no image sequence."],
    quiz=[dict(q="What does onion skin show?", o=["Faint copies of the previous and next frames", "The sound", "The final colours", "A different file"], a=0,
               why="Seeing nearby frames helps you keep movement smooth."),
          dict(q="Why put the character and background on separate layers?", o=["You can change one without redrawing the other", "It makes the file larger", "It removes frames", "It changes the frame rate"], a=0,
               why="Layers keep parts independent and editable."),
          dict(q="Which export is the safest master?", o=["A PNG image sequence", "A screenshot", "A GIF", "A shortcut"], a=0,
               why="If a video export fails, you still have every frame."),
          dict(q="Where should you download animation software?", o=["Any link you are sent", "The official website", "A pirate site", "A video comment"], a=1,
               why="Official sources are safest and free of hidden malware.")],
    activity="Install one free 2D program from its official site, set 1280 by 720 at 24 fps, turn on autosave, draw a 12-frame bouncing ball loop on its own layer, and export a PNG sequence and a GIF.",
)

LESSONS[7] = dict(   # The bouncing ball and the feeling of weight
    minutes=16,
    hook="Every animator remembers their first bouncing ball. It looks like the easiest exercise in the book, one circle moving up and down, yet it quietly teaches nearly everything: timing, spacing, squash and stretch, arcs and weight. A ball that bounces with the right numbers feels real. The same ball with slightly different timing becomes a heavy stone, a light beach ball or a ball of rubber. You already met the idea of timing and spacing in the first lessons. Now you will build the full exercise frame by frame, with real numbers you can follow, study how to change the same bounce to make different materials, learn the common mistakes and finish with a polished, shaded ball that you can proudly put in your portfolio.",
    sections=[
        ("Plan before you draw", """Always plan the bounce on paper or in a rough layer:

1. **Decide the material:** a rubber ball, a football, a bowling ball.
2. **Draw the path:** a series of arcs that get lower each time, like a staircase of rainbows.
3. **Mark the contact points** where the ball touches the ground.
4. **Plan the timing:** the ball takes the same time to go up as to come down. At 24 fps, a first bounce might take **10 frames down and 10 frames up.**
5. **Draw a ground line** and a **shadow** so the ball has a place to be.
6. **Plan the spacing** with tick marks. The ball is **fastest just before it hits the ground** (wide gaps), and **slowest at the top** (close gaps).

Fifteen minutes of planning saves hours of redrawing. Keep the plan on a layer under the animation, and turn it off at the end."""),
        ("Draw the key poses", """Block the main drawings first, on **frames you choose:**

- **Frame 1:** the ball at its highest point, at rest for a moment.
- **Frame 10:** **contact,** with the ball squashed slightly, wider than tall.
- **Frame 11:** the squash **recovers** and begins to stretch as the ball rises.
- **Frame 20:** the top of the first bounce, **lower** than the starting height.
- **Frame 29:** the second contact. Squash is **smaller** because the impact is weaker.
- **Frame 38 and onward:** each following bounce is **shorter in height and in time,** until the ball rolls.

Note the **pattern:** each bounce loses energy. If every bounce was the same height, the ball would look magical, not real. Check the keys by playing them as a rough slideshow, before drawing any in-betweens. If the rhythm feels wrong, fix it now."""),
        ("In-betweens, squash and stretch", """Now fill the spaces:

1. Add **breakdowns** halfway between the keys. These decide the arc.
2. Add the in-betweens, using **onion skin** and the **spacing chart.**
3. **Stretch** the ball in the direction of travel when it moves fast: tall and thin as it falls, and again as it rises right after the bounce.
4. **Squash** it at contact: short and wide, **keeping the volume the same.**
5. Return to a round shape at the top, where the ball is almost still.
6. Make the **shadow** follow the ball: **small and dark** when the ball is close to the ground, **larger and lighter** when it is high.

Do not overdo the stretch. A stiff ball needs small changes. A soft rubber ball can stretch a lot. Play the animation often, and use **look-and-adjust** until the motion feels natural."""),
        ("Make the same bounce a different material", """Weight comes from the numbers. Try the same ball with different choices:

- **Rubber ball:** quick, lively bounces, lots of height, **moderate squash.**
- **Beach ball:** floaty, **slow** timing, a long hang at the top, **little squash,** and bounces that fade slowly.
- **Bowling ball:** heavy, **no stretch,** hardly any bounce, drops with a thud and may bounce once.
- **Water balloon:** big squash, almost no bounce, a wobble after impact.
- **Ping pong ball:** very fast, high, small and light.

Draw all five on the same canvas and compare. This simple test shows that **materials are made by timing, spacing and squash,** not by shading. When you can show weight with a plain circle, you can show it in any character."""),
        ("Polish and common mistakes", """Check your ball for these problems:

- **Floating at the bottom:** the ball must touch the ground exactly on the contact frame, and the squash must be on the ground, not above it.
- **Even spacing:** the ball moves at constant speed, like a ball on a string. Add easing at the top.
- **Same height every bounce:** use a clear drop in height.
- **Bounce on the wrong frame:** make sure sound or a dust puff matches the contact.
- **Too much squash:** it looks like jelly.
- **Volume changes:** a squashed ball that gets larger and larger looks wrong.
- **No arc between bounces,** if the ball also moves sideways: the path should be a series of parabolas.

For a **portfolio piece,** add a simple background, a shadow, a sound effect on each contact and a short title. Export a looping GIF and an MP4. This single exercise, done well, shows a recruiter you understand weight, timing and spacing."""),
    ],
    diagram=bars([("Drop", 100), ("Bounce 1", 64), ("Bounce 2", 41), ("Bounce 3", 26), ("Bounce 4", 17)], note="Each bounce keeps less energy than the last.", unit="%"),
    caption="Bounce height for a rubber ball: each bounce reaches a lower height than the one before, as energy is lost.",
    terms=[("Contact frame", "The frame where the ball first touches the ground."), ("Squash", "Making a shape shorter and wider on impact."),
           ("Stretch", "Making a shape longer and thinner when it moves fast."), ("Breakdown", "A drawing between keys that decides the path of movement."),
           ("Parabola", "The curved path of a thrown or bouncing object."), ("Contact shadow", "A shadow under an object that shows how high it is above the ground.")],
    mistakes=["Letting the ball float above the ground at contact.", "Making every bounce the same height.", "Changing the ball's volume while squashing.", "Using the same timing for a bowling ball and a beach ball."],
    quiz=[dict(q="Where is the ball fastest during a drop?", o=["At the top", "Just before it hits the ground", "At the start of the rise", "It never changes"], a=1,
               why="Gravity speeds it up as it falls, so gaps are widest near the ground."),
          dict(q="What should happen to each following bounce?", o=["It gets lower and shorter", "It gets higher", "It stays the same", "It vanishes at once"], a=0,
               why="Energy is lost at each impact."),
          dict(q="Which ball should barely stretch or bounce?", o=["Beach ball", "Bowling ball", "Ping pong ball", "Balloon"], a=1,
               why="A heavy hard ball hits with a thud and stays low."),
          dict(q="What does the shadow show?", o=["How high the ball is above the ground", "The ball's colour", "The sound", "The frame rate"], a=0,
               why="A small dark shadow means close to the ground, and a larger lighter shadow means high.")],
    activity="Animate a rubber ball with at least four bounces, a shadow and squash on contact, then redo it as a beach ball and a bowling ball, and write one sentence about how timing changed each.",
)

LESSONS[8] = dict(   # Arcs, overlap and secondary action
    minutes=16,
    hook="A robot moves in straight lines and stops everything at once. A living creature does not. Watch a cat jump down from a shelf, a child running with a scarf or a tailor swinging a long piece of cloth: the body leads, the loose parts follow a little later, and everything moves along curves. These three ideas, arcs, overlapping action and secondary action, are what turn a correct animation into a lively one. You met their names in the earlier lessons. Now you will practise them with small exercises that use a pendulum, a swinging tail and a cloak, learn how to measure the delay between parts in frames, learn to test your arcs by tracing the path and add small supporting actions that give a character personality without confusing the main action.",
    sections=[
        ("Arcs: trace the path", """Almost all natural movement follows **arcs,** curved paths, because joints rotate. Your arm swings from the shoulder, your head turns on the neck, and a thrown ball follows a parabola.

How to check an arc:

1. **Mark one point** on the moving part, such as the tip of the hand, on every frame, with a small dot of a different colour.
2. **Turn on onion skin** or view all the dots at once.
3. **Connect the dots.** The line should be a smooth curve.
4. **Fix the bumps.** If one dot jumps off the curve, redraw that in-between so it sits on the line.

Practise with a **pendulum:** a weight on a string. It speeds up at the bottom and slows at the top, along a perfect arc. Draw it swinging for 24 frames, with the extremes (the top points) as keys and the bottom as the fastest point. Then draw a **head turn** and a **hand wave** the same way."""),
        ("Overlapping action: parts settle at different times", """When the main body stops, the loose parts keep moving for a short time, and then settle. This is **follow-through,** and the delay between parts is **overlapping action.**

A simple recipe uses **delay in frames:**

- The **body** reaches its pose at frame 0.
- The **upper arm** settles at about frame 2.
- The **hand** settles at about frame 4.
- The **hair, tail or cloth** settles at about frame 6 to 8.

Each part also **overshoots** a little past its final pose and then comes back, like a spring. Use **small numbers:** a delay of two frames is plenty. Too much delay and the character looks like it is made of jelly.

**Drag** is the other half: when the body starts to move, loose parts lag behind. A skirt or a cloak trails and then catches up. Think of a long tail as a **chain of pendulums,** each one following the one before."""),
        ("Exercise: the swinging tail", """Draw a ball with a long tail that jumps and lands:

1. **Plan the ball's path** as a bounce with a simple arc.
2. Draw the tail as a **curved line with three or four segments.**
3. As the ball **rises,** the tail **trails below** it, pointing down.
4. At the **top,** the tail hangs straight and curves slightly.
5. As the ball **falls,** the tail floats **above** it.
6. On **landing,** the ball squashes and stops, but the tail **keeps going,** whips over and slowly settles over 8 to 12 frames.

Use **onion skin** to see how each segment follows the one before, and trace the tip of the tail. Its path should look like a wavy ribbon, not a zigzag. Repeat the exercise with a **cloak** on a running figure, or a **flag** in the wind, which loops. These small tests teach you more than long theory."""),
        ("Secondary action: the supporting story", """A **secondary action** is a smaller movement that supports the main action and adds character. Examples:

- A character **walks** (main), while **whistling** or swinging a bag (secondary).
- A character **talks** (main), while **scratching their head** or fiddling with a cap (secondary).
- A character **waits** (main), while **tapping a foot** and glancing at a watch (secondary).
- A character **sits sadly** (main), while **a tear rolls** and shoulders sag (secondary).

Rules for secondary action:

1. It must **support** the main action, never fight it. If the audience watches the whistling and misses the walk, remove it.
2. It should **fit the personality:** a nervous character fidgets, a calm character does not.
3. Plan it **after** the main action works. Add it as a separate layer, so you can delete it if it does not help.
4. **Keep it small and simple.**
5. Time it **slightly off** the main rhythm, so it feels natural, not mechanical."""),
        ("Putting it all together", """Take a simple character **hopping** across the screen and apply all three ideas:

1. **Block** the hop with strong key poses and a clear arc for the whole body.
2. **Trace the arc** of the head and the feet, and fix any bumps.
3. Add **overlap:** an ear, a tail or a scarf that lags on take-off and swings on landing.
4. Add a **secondary action:** a blink on the landing, or a small look to the side.
5. Play at full speed, then **scrub** slowly. Check that the **delay stays small.**
6. Show it to a friend and ask what they noticed first. It should be the **hop.**

Common mistakes to avoid: using the same delay for every part, letting parts stop at the same time, over-exaggerating until the character becomes rubber, and adding so many secondary actions that the main idea is lost. Keep a **notebook of observations:** every day, watch one real movement, such as someone adjusting a bag, and write down how parts lead and follow."""),
    ],
    diagram=timeline([("Body stops", "frame 0"), ("Upper arm", "about frame 2"), ("Hand", "about frame 4"), ("Tail or cloth", "about frame 6"), ("Settled", "about frame 8")], note="Each part settles a little later."),
    caption="After the body stops, each loose part settles a little later: arm, hand, then tail or cloth.",
    terms=[("Arc", "A curved path that natural movement follows."), ("Overlapping action", "Different parts of a character moving and settling at different times."),
           ("Follow-through", "Loose parts continuing to move after the main body stops."), ("Drag", "Loose parts lagging behind when the body starts to move."),
           ("Secondary action", "A smaller movement that supports and adds character to the main action."), ("Overshoot", "A part moving a little past its final pose and then returning.")],
    mistakes=["Moving along straight lines so the character looks like a robot.", "Letting every part stop on the same frame.", "Using a very long delay so the character looks like jelly.", "Adding a secondary action that steals attention from the main action."],
    quiz=[dict(q="How do you check an arc?", o=["Mark a point on every frame and connect the dots", "Change the colour", "Add sound", "Delete the frames"], a=0,
               why="The dots should form a smooth curve, and any bump is a frame to fix."),
          dict(q="What is a good delay between the body and a hand settling?", o=["About 200 frames", "No delay at all", "About 2 to 4 frames", "One minute"], a=2,
               why="Small delays give a natural look, and big ones look like jelly."),
          dict(q="What should a secondary action do?", o=["Support the main action without stealing attention", "Replace the main action", "Hide the character", "Change the frame rate"], a=0,
               why="It adds personality but must never fight the main action."),
          dict(q="What is drag?", o=["A sound", "A new layer", "A kind of file", "Loose parts lagging behind when the body starts to move"], a=3,
               why="A cloak or tail trails and then catches up.")],
    activity="Animate a ball with a three-segment tail jumping and landing, trace the tail tip to check its path, then add a one-second blink or glance as a secondary action on a hopping character.",
)

LESSONS[9] = dict(   # Run cycles and jumps
    minutes=17,
    hook="Walks are gentle. Runs and jumps are where animation gets exciting: speed, force, a body thrown into the air, and the heavy thump of coming back down. These actions carry a lot of the drama in games, adventure films and sports animation, and they are the moves your audience remembers. They also look hard, but they follow the same logic as the walk: a few strong key poses, careful timing and spacing, and clear weight. The main differences are that in a run the body leans forward, there is a moment when both feet are off the ground, and the timing is much faster. In this lesson you will build a run cycle from four poses, learn a loop-friendly timing, animate a full jump with anticipation, flight and landing, and learn to give both actions personality.",
    sections=[
        ("From walk to run: what changes", """Compare the two:

- **Walk:** one foot is always on the ground. The body bobs gently. Arms swing a little.
- **Run:** there is a moment of **flight,** when **both feet leave the ground.** The body leans **forward.** Arms bend and pump strongly. The head stays steady.

Because a run is fast, the cycle is **shorter.** A common full run cycle (two steps) is about **12 to 16 frames at 24 fps,** and often animated on ones or twos. The **down pose** is deeper, since the body absorbs the impact, and the **up pose** is higher, since the body pushes off the ground with force.

The **lean** shows speed. A jogger leans a little, a sprinter leans a lot. Add a **head that stays level,** like a camera moving along a track, even while the body bobs up and down."""),
        ("The four poses of a run cycle", """Draw a run with these poses, then mirror them for the other leg:

1. **Contact:** the front foot lands, usually on the heel or the ball of the foot. The back leg trails behind. The body is **leaning forward.**
2. **Down (recoil):** the body sinks as the front leg takes the weight. The back foot comes off the ground, and the knee swings forward.
3. **Passing:** the back leg swings forward past the standing leg. The body begins to rise.
4. **Up (flight):** the body pushes off the ground, and for a moment **both feet are in the air.** The body is at its highest.

Add **opposite arms:** when the right leg is forward, the left arm is forward, and the elbows are bent about 90 degrees. Use **onion skin** to check the loop and that the feet reach the ground at the same height on each contact. A **run in place** with a moving background keeps the loop clean, just as in the walk."""),
        ("Make the run feel right", """Details that sell the run:

- **Timing:** use fewer frames for a fast run, and more frames for a slow jog. Test 12, 14 and 16 frames and compare.
- **Spacing:** the foot hitting the ground moves **backward** at the same speed as the background, so it does not slide. Match them.
- **Weight:** a heavy character has a deeper down pose and slower up. A light character barely dips.
- **Overlap:** hair, a scarf, a school bag or a loose shirt lag behind and bounce.
- **Personality:** a happy run is bouncy, with big arm swings. A tired run has small steps, low feet and hanging arms. A scared run leans back, looks around and has frantic arms.
- **Run, then stop:** add a **skid or a settle** at the end, with follow-through.
- **Camera:** a slight shake or a following pan adds energy.

Test on a **loop for 10 seconds,** and look for any bump or limp. Fix the weakest pose first."""),
        ("The jump: anticipation, flight, landing", """A jump has a clear structure:

1. **Anticipation (crouch):** the body squats and the arms swing back. It lasts about 4 to 8 frames and tells the audience what is coming.
2. **Take-off:** the body **stretches** upward as the legs push off, in just 2 to 3 frames. The arms swing up.
3. **Rise:** the character moves up along an arc, **slowing** as it reaches the top.
4. **Apex (hang time):** at the highest point, movement is slowest, with close spacing. A short hang makes the jump feel floaty and strong.
5. **Fall:** the character speeds up, with wider spacing, and the legs prepare to land.
6. **Landing:** the feet touch, and the body **squashes** into a crouch. The deeper the crouch, the heavier the landing.
7. **Recovery:** the character stands up and settles, with follow-through in clothes and hair.

A rough timing at 24 fps for a normal jump: **anticipation 6, take-off 2, rise 8, hang 3, fall 6, land 4, recover 8.** Adjust to taste."""),
        ("Jump variations and common mistakes", """Try variations:

- **A small hop** (short anticipation, little height) and a **huge leap** (long squat, long hang).
- **A running jump,** where the run carries into the jump with no pause, and the arc continues the run's direction.
- **A jump over an obstacle,** with the legs tucked.
- **A cartoon jump** with extreme stretch, a long hang and a heavy landing cloud of dust.
- **A jump for joy,** with a spin and a burst of energy.

Common mistakes:

- **No anticipation:** the character just pops into the air.
- **Even spacing in the air:** it looks like a lift. Use closer spacing at the top.
- **No weight on landing:** add a squash, a dust puff and a short pause.
- **Floating arms:** the arms need a clear arc and a reason for their movement.
- **Wrong arc:** a jump should be a smooth parabola.

Combine a **run, a jump and a landing** into one 5-second action sequence for your portfolio, with a looping background and sound effects."""),
    ],
    diagram=flow([("Crouch", "anticipation"), ("Launch", "stretch up"), ("Apex", "slow and floaty"), ("Fall", "speeds up"), ("Land", "squash and settle")], "t9", note="Anticipation first, weight last."),
    caption="A jump goes from crouch to launch, apex, fall and landing, with slow spacing at the top and a squash on landing.",
    terms=[("Run cycle", "A short looping animation of a character running."), ("Flight pose", "The moment in a run when both feet are off the ground."),
           ("Lean", "Tilting the body forward to show speed."), ("Anticipation", "The preparation before a jump or other action."),
           ("Apex", "The highest point of a jump."), ("Hang time", "The short moment near the apex when movement seems to pause.")],
    mistakes=["Making a run with one foot always on the ground, so it looks like a fast walk.", "Skipping anticipation before a jump.", "Using even spacing in the air so the jump looks mechanical.", "Landing with no squash, dust or settle."],
    quiz=[dict(q="What is the main difference between a run and a walk?", o=["Both feet leave the ground during a run", "A run is slower", "A run has no arms", "A walk has more colours"], a=0,
               why="The flight pose, with both feet off the ground, is the signature of a run."),
          dict(q="Where is movement slowest in a jump?", o=["At take-off", "On landing", "At the apex", "Never slow"], a=2,
               why="The character slows at the top, giving a hang time."),
          dict(q="What does anticipation do before a jump?", o=["Removes the arc", "Adds sound", "Changes the background", "Prepares the audience and adds power"], a=3,
               why="The crouch tells the audience what is coming and sets up the push."),
          dict(q="How can you stop feet sliding in a run in place?", o=["Match the background speed to the foot on the ground", "Remove the feet", "Add more frames", "Change the colour"], a=0,
               why="The planted foot should travel backward at the same speed as the ground.")],
    activity="Animate a 12 to 16 frame run cycle in place with a looping background, then add a six-part jump with anticipation, hang time and a squashing landing, and join them into one short sequence.",
)

LESSONS[10] = dict(   # Facial expressions and simple lip-sync
    minutes=16,
    hook="Your character can walk, run and jump, but until it can speak and show feeling, it is only a puppet. The face is where the audience looks for the story: surprise in a pair of raised brows, fear in wide eyes, a secret in a half smile. Good news for a beginner: you do not need to draw hundreds of faces. A small, well-planned set of eyes, brows and mouths, swapped on separate layers, can express almost anything, and a simple lip-sync with four or five mouth shapes can make a character talk convincingly. In this lesson you will build an expression sheet, set up a face on layers, learn the essential mouth shapes for simple dialogue, animate blinks and eye movement, and sync a short line of speech to your own voice recording.",
    sections=[
        ("Build an expression sheet", """Start on paper or a new layer. Draw your character's head six times, one for each basic emotion:

- **Happy:** raised cheeks, eyes slightly narrowed, brows relaxed or lifted, a smile.
- **Sad:** brows pulled up in the middle, eyes lowered, mouth corners down.
- **Angry:** brows pulled down and together, eyes narrowed, mouth tight or showing teeth.
- **Surprised:** brows high, eyes wide, mouth open and round.
- **Scared:** brows raised and tilted, eyes wide, mouth open and stretched.
- **Thinking:** one brow raised, eyes looking up or aside, mouth small and pressed.

The **eyebrows and eyes carry most of the emotion.** Try covering the mouth with your finger: you should still know the feeling. **Exaggerate** the shapes so they read clearly even on a phone. Add **subtle** expressions later, such as shy, smug, bored and confused. Keep the **same style and line weight** for every face."""),
        ("Set up the face on layers", """Instead of redrawing the whole head every frame, separate the parts:

1. **Head base** (no features).
2. **Eyes** layer, with open, half-closed and closed versions.
3. **Brows** layer.
4. **Mouth** layer, with each mouth shape on its own frame.
5. **Extras:** cheeks, blush, sweat or tears.

On the timeline, you **change only the layer you need.** To make a blink, change the eyes for two or three frames. To say a word, swap the mouth drawings. This saves huge amounts of work, and it keeps the head the same shape. Name the layers clearly, such as `eyes`, `brows`, `mouth`, and keep a **numbered library of mouth drawings.** In most 2D programs, you can copy a drawing from one frame to another, or save frames in a library to reuse."""),
        ("The essential mouth shapes", """For a simple character, **five shapes** are enough:

1. **Closed:** lips together. Used for M, B, P and for rest.
2. **Open (A, I):** wide open mouth, for loud, open vowels.
3. **Smile or E:** a wide mouth with teeth showing slightly.
4. **Round (O, U):** a small round mouth.
5. **Teeth on lip (F, V):** the top teeth touch the lower lip.

Optional extras: a **tongue shape** for L and TH, and a **half-open** mid shape.

Rules for simple sync:

- **Do not draw every letter.** Match the main **vowels** and the **closed** sounds.
- Make the mouth **close** for M, B and P.
- **Hold shapes** for a few frames, as speech is not a flicker.
- **Add the head:** a small nod or tilt on stressed words makes the face feel connected.
- **Match the style:** a cartoon with big mouth shapes needs big, clear changes."""),
        ("Blinks, eyes and small details", """A face that never blinks or moves its eyes looks dead.

- **Blink** every **3 to 5 seconds.** A fast blink takes about 3 to 5 frames: open, half, closed, half, open.
- **Hide changes in a blink:** a blink during a head turn or a change of expression feels smooth.
- **Eye direction:** the eyes often move **before** the head. When thinking, a character may look up or away.
- **Eye darts:** tiny quick eye movements add life.
- **Pupil size:** a small pupil can look suspicious and a large one innocent or scared.
- **Eyebrow moves:** raise them on a question or a stressed word.
- **Hold the final expression** for a moment after the line, rather than snapping back to neutral.

A great **exercise:** make the same line sound happy, sad or sarcastic by changing only the brows, eyes and a head tilt, without changing the voice."""),
        ("Sync a short line to your voice", """Practise with a **five-second line,** such as “Hello, my name is Kemi, and I love mango!”

1. **Record the line** on your phone in a quiet room, then save it as a WAV or MP3.
2. **Import the sound** into your project. Many 2D programs show the **waveform** in the timeline (check your program's manual for the exact steps).
3. **Scrub slowly** and note the frame where each important sound starts.
4. **Place mouth shapes** on those frames, **one or two frames early.**
5. **Fill the gaps** with holds and extra shapes only where they help.
6. **Add blinks, brow moves and a head nod.**
7. **Play at full speed,** and watch with and without sound.

A free helper such as **Papagayo-NG** can suggest mouth shapes from a recording, which you can then refine. Check its current download page and the formats your program supports."""),
    ],
    diagram=grid([("Happy", "cheeks up, smile"), ("Sad", "brows up in middle"), ("Angry", "brows down, tight mouth"), ("Surprised", "brows high, round mouth"), ("Scared", "wide eyes, tilted brows"), ("Thinking", "one brow up, look aside")], cols=3, note="Eyes and brows carry the feeling."),
    caption="Six basic expressions and the eye, brow and mouth changes that make each one readable.",
    terms=[("Expression sheet", "A page of a character's face showing different emotions."), ("Mouth chart", "A set of mouth shapes used for dialogue."),
           ("Blink", "A quick closing and opening of the eyes, usually 3 to 5 frames."), ("Waveform", "A picture of a sound's loudness over time."),
           ("Hold", "Keeping a drawing for several frames."), ("Eye dart", "A tiny quick movement of the eyes that adds life.")],
    mistakes=["Redrawing the whole head every frame instead of using layers.", "Drawing a mouth shape for every letter.", "Never blinking or moving the eyes.", "Forgetting to close the mouth for M, B and P."],
    quiz=[dict(q="Which part of the face carries most of the emotion?", o=["Eyes and eyebrows", "The ears only", "The neck", "The hair"], a=0,
               why="Even with the mouth covered you should know the feeling."),
          dict(q="Why separate eyes, brows and mouth on layers?", o=["It hides the face", "It slows the computer on purpose", "You can change one part without redrawing the whole head", "It removes colour"], a=2,
               why="Layers save work and keep the head consistent."),
          dict(q="Which sounds need a closed mouth?", o=["M, B and P", "A and I", "O", "E"], a=0,
               why="These sounds are made by pressing the lips together."),
          dict(q="How often should a character blink?", o=["Every frame", "Never", "Once a minute", "Roughly every 3 to 5 seconds"], a=3,
               why="Regular blinks keep the character alive.")],
    activity="Draw six expressions, set up eyes, brows and mouth on separate layers, record a five-second line on your phone, and sync it with five mouth shapes, two blinks and a head nod.",
)

LESSONS[11] = dict(   # Acting: showing emotion through movement
    minutes=16,
    hook="Watch a silent scene of someone opening a letter. Their shoulders lift, they breathe in, their eyes scan the page, then slowly their whole body droops, and without a single word you know the news is bad. That is acting, and in animation you must create it from nothing, one drawing at a time. Animators are actors who work with a pencil. You do not need to be a performer, but you need to observe people, choose clear poses, control timing and decide where the character is looking. In this lesson you will learn a method for planning a performance, how pose, timing and eyes combine to show emotion, how to use your own body as reference, how to use holds and contrast to make feelings land and how to animate a complete 8 to 10 second acting shot.",
    sections=[
        ("Start with the thought", """A character does not just move. It **thinks and feels,** and the movement shows it. Before drawing, answer five questions:

1. **Who is the character** and what is their personality?
2. **What do they want** right now?
3. **What just happened?** (The trigger.)
4. **What do they feel,** and does it change during the shot?
5. **What do they do about it?**

A shot with a clear thought has a **beginning, a middle and an end:** a trigger, a reaction and a decision. For example: a boy waits for exam results (want), the teacher hands him a paper (trigger), he looks, his face falls (reaction), he straightens his back and smiles bravely (decision). Write the thought in **one sentence** and keep it near your desk. Every pose you draw must serve it."""),
        ("Pose, timing and eyes", """Three tools carry emotion:

- **Pose:** the body shape. Happiness lifts the chest and head. Sadness drops the shoulders and head. Fear pulls the body back and small. Pride raises the chin. A strong **line of action** (one flowing curve through the body) makes the emotion clear. Test your pose as a **silhouette.**
- **Timing:** how fast and how long. Quick movements show energy, surprise or anger. Slow movements show sadness, thought or tiredness. A **hold** makes the audience feel the moment.
- **Eyes:** the audience looks at the eyes first. **Where** the character looks shows what they think about. **When** the eyes move shows when they decide. Lead with the eyes, then let the head and body follow.

Use all three **together.** A sad pose with fast, bouncy timing looks like confusion. A happy pose with a slow hold looks like a smug smile. When something feels wrong, check which of the three disagrees with the others."""),
        ("Use your own body as reference", """You are the best acting teacher you have.

1. **Act it out** in front of a mirror or film yourself with a phone. Do it three times, in different ways.
2. **Watch the footage** and note what your body does: where the weight shifts, when the head moves, what the hands do, how long you hold still.
3. **Do not copy every frame.** Pick the **three to five key moments,** and exaggerate them. Real life is subtle, but animation needs clear, stronger poses.
4. **Sketch quick thumbnails** from the video.
5. **Observe real people** in the market, at church or on the bus: how do they show impatience, joy, doubt or tiredness? Keep a small sketchbook.
6. **Study great scenes** with the sound off, and ask what they show.

Reference helps you find timing and weight, but your drawings must still follow the principles you have learned: arcs, anticipation, overlap and appeal."""),
        ("Holds, contrast and breathing", """Many beginners animate too much. Strong acting uses **stillness.**

- **Hold the key pose** for several frames so the audience can read it. A 12-frame hold on a realisation feels like a heartbeat.
- **Contrast** makes movement clear: a **sudden** move after a **long hold** shocks, and a **slow** move after **fast** action calms.
- **Anticipate the emotion:** before a big reaction, draw a small preparation, such as a quick breath in before shouting.
- **Moving holds:** even when a character is still, add tiny movement such as **breathing** or a slow drift, so it does not freeze like a photograph.
- **Weight shifts:** a character changes weight from foot to foot when thinking or waiting.
- **Hands:** they are expressive. A clenched fist, a trembling hand and a hand covering the mouth each tell different stories.
- **Do less, better:** one clear gesture beats five busy ones.

Check each key pose. Does it **read in one second** at thumbnail size?"""),
        ("Animate a full acting shot", """Make an **8 to 10 second** shot, with one character and no walking:

1. Choose the **thought sentence** and the emotion changes.
2. **Record reference** and pick the key moments.
3. **Draw thumbnails** of the main poses, with a strong silhouette.
4. **Block the key poses** on the timeline with rough timing, then play.
5. **Add breakdowns and in-betweens** with arcs and overlap.
6. **Time the eyes,** blinks and brows.
7. **Add the holds** and moving holds.
8. **Check with sound off:** do you still understand the story?
9. **Show it to a friend** without telling them the plot. Ask what the character feels.
10. **Polish** and fix.

Good scenes to practise: **receiving good news, waiting nervously, lifting a heavy object, hearing a strange sound,** or **losing and finding a toy.** Save the best as part of your showreel."""),
    ],
    diagram=triangle([("POSE", "shape of the body"), ("TIMING", "speed and holds"), ("EYES", "where and when")], middle="emotion|that reads", note="All three must agree."),
    caption="Emotion in animation comes from pose, timing and eyes working together. If one disagrees, the feeling is confused.",
    terms=[("Acting", "Showing thoughts and feelings through movement and expression."), ("Line of action", "A flowing curve through a pose that shows its energy."),
           ("Hold", "Keeping a pose still so the audience can read it."), ("Moving hold", "A tiny movement, such as breathing, that stops a held pose from looking frozen."),
           ("Trigger", "The event that makes the character react."), ("Reference", "A real video or photo used to study movement and timing.")],
    mistakes=["Animating constant movement with no holds.", "Copying video reference frame by frame instead of choosing key moments.", "Using fast, bouncy timing for a sad pose.", "Drawing a pose that does not read as a silhouette."],
    quiz=[dict(q="What are the three main tools of emotion in animation?", o=["Pose, timing and eyes", "Colour, price and size", "Sound only", "Layers and files"], a=0,
               why="Body shape, speed and where the character looks work together."),
          dict(q="Why use a hold?", o=["It lets the audience read and feel the moment", "It deletes frames", "It changes colour", "It adds music"], a=0,
               why="A held pose gives time to understand an emotion."),
          dict(q="What should you do with video reference?", o=["Copy every frame exactly", "Choose key moments and exaggerate them", "Ignore it", "Delete it"], a=1,
               why="Reference teaches timing and weight, but animation needs clear, stronger poses."),
          dict(q="What is a moving hold?", o=["A tiny movement such as breathing during a still pose", "A fast run", "A camera zoom", "A skipped frame"], a=0,
               why="It stops a held pose from looking frozen like a photograph.")],
    activity="Write a one-sentence thought for a character who receives news, film yourself acting it, draw three key poses with strong silhouettes, and animate an 8 second shot with at least two holds and a moving hold.",
)

LESSONS[12] = dict(   # Backgrounds, layers and camera moves
    minutes=16,
    hook="You already know that a background is built in layers and that a camera can pan or zoom. This lesson puts that knowledge into practice with a real, simple scene. You will paint a background in a free program with the help of perspective guides, split it into layers that move at different speeds, plan the numbers for a smooth pan and zoom so that your camera glides instead of jerks, and add a few finishing touches such as shadows, light and depth. We will use plain steps that work in Krita, Pencil2D, OpenToonz and similar tools, though menu names differ, so check your program's manual for the exact buttons. By the end you will have a short, layered scene with a moving camera that looks far richer than a flat drawing.",
    sections=[
        ("Plan the scene and the canvas", """Start by deciding what the camera will do, because it controls the size of your paintings.

- **A pan across a street** needs a background **wider** than the frame. If the frame is 1280 pixels wide and the camera moves 640 pixels, paint a background at least **1920 pixels wide.**
- **A zoom in** needs an image **larger** than the frame, for example 1.5 times, so that it stays sharp when scaled up. For a 1280 by 720 frame, paint at 1920 by 1080 or more.
- **A static shot** needs only the frame size.

Make a quick **thumbnail** with the frame drawn as a rectangle over the background, so you can see what will be visible at the start and the end. Mark the **horizon line** and decide where the characters will stand. Keep a **safe area** around the edges, because screens crop slightly. Save the canvas at a larger size, and keep a **template file** with the frame size marked."""),
        ("Paint a simple background with perspective", """A background does not have to be complicated. Follow these steps:

1. **Draw the horizon line** at the character's eye level.
2. **Add a vanishing point** on the horizon. Many programs, including Krita, have **assistant tools** that draw perspective lines for you. Check the manual for the current tool names.
3. **Block big shapes:** ground, buildings, sky, in flat colours. Use perspective lines to keep the sides of buildings pointing to the vanishing point.
4. **Use values:** the background should be **lighter or calmer** than the characters, or have lower contrast.
5. **Add detail** only in places the viewer will look, such as near the characters.
6. **Colour:** stick to your palette, and suggest the time of day with the colour of the sky and light.
7. **Paint on separate layers** so each can move: sky, far hills or buildings, middle ground, near ground.

Do not try to be perfect. A clean, simple background helps the character stand out."""),
        ("Layers and parallax speeds", """Parallax is the depth effect you get when near things move faster than far things as the camera moves. You can calculate it:

- Choose the **total pan distance** for the nearest layer, for example **600 pixels.**
- Give each farther layer a **smaller fraction:** the middle ground moves **60%** (360 pixels), the far buildings **30%** (180 pixels), and the sky **10%** (60 pixels).
- The **character layer** usually stays still on screen if the camera follows them, while the background moves **past.**

Sketch the layers like this:

1. **Sky:** slowest.
2. **Far background:** slow.
3. **Middle ground:** medium.
4. **Character layer.**
5. **Foreground objects** such as a fence or leaves: fastest, drawn in front.

Make sure each layer is **wide enough** to cover the whole pan, with no empty edges. Name each layer clearly and **lock** the finished ones."""),
        ("Planning pan and zoom with numbers", """To make smooth camera moves, work out the distance per frame.

> [Example: a pan]
> Pan 600 pixels in 3 seconds at 24 fps = 72 frames
> 600 / 72 = about 8.3 pixels per frame (an even move)

An **even move** looks robotic. Add **easing:** start slowly, speed up in the middle, and slow before stopping. In many programs you set a **keyframe** at the start and the end of the move and choose an **ease in and ease out** curve. Some programs let you move the layer by hand on keyframes, and then the program fills the in-betweens. Check how your tool animates a layer's position and scale.

For a **zoom,** scale the layers from 100% to about 110% or 120% over the move, with easing. The **nearer layers should scale a little more** than far ones for extra depth. **Slow** camera moves feel calm or tense. **Fast** moves feel energetic. **Hold the camera still** for a moment before and after the move. And always ask: **why does the camera move?** It should reveal something, follow action or build feeling."""),
        ("Finishing touches and checking", """A few small touches add polish:

- **Contact shadows** under characters, so they sit in the world.
- **A soft light overlay** or a gradient to unify the colours.
- **Atmospheric depth:** make far layers **lighter and bluer,** and near layers darker and warmer.
- **Small moving details:** a flag, drifting dust or birds.
- **A slight vignette** to focus attention.
- **Grain or texture,** gently, to unify.

Check the final scene:

1. Play at **full speed.** Do the layers slide smoothly, with no jumping?
2. Look for **edges** where a layer ends too early.
3. Look for **flicker** in thin lines when the camera moves slowly.
4. Check that **characters stay readable** against every part of the background.
5. Export a **small test** and watch it on a phone.

Save your layered file and a flattened copy of the background as a **PNG,** so you can reuse it in future scenes."""),
    ],
    diagram=compare(("PAN", ["Slides sideways", "Needs a wider background", "Far layers move less", "Ease in and out"]), ("ZOOM", ["Scales up or down", "Needs a larger image", "Near layers scale more", "Slow zoom builds tension"]), vs="or", note="Plan the canvas before you paint."),
    caption="A pan slides across a wider background, and a zoom scales a larger one. Both need easing and a reason.",
    terms=[("Horizon line", "The eye-level line in a perspective drawing."), ("Vanishing point", "The point where parallel lines seem to meet."),
           ("Parallax", "A depth effect where near layers move faster than far ones."), ("Easing", "Starting and stopping a move gradually."),
           ("Safe area", "The part of the picture that will not be cropped on most screens."), ("Atmospheric depth", "Making far objects lighter and bluer to suggest distance.")],
    mistakes=["Painting the background only as wide as the frame and then trying to pan.", "Moving all layers at the same speed so there is no depth.", "Starting and stopping a camera move suddenly.", "Moving the camera with no reason."],
    quiz=[dict(q="Why paint a background wider than the frame for a pan?", o=["There must be picture to slide across", "It improves sound", "It reduces file size", "It changes colour"], a=0,
               why="A pan needs extra image so no empty edge shows."),
          dict(q="In parallax, which layer moves fastest?", o=["The sky", "The far hills", "The nearest foreground layer", "None"], a=2,
               why="Near layers move more, and far layers move less."),
          dict(q="What does easing do to a camera move?", o=["Starts and stops it gradually so it looks smooth", "Makes it faster", "Adds sound", "Deletes layers"], a=0,
               why="Even speed looks robotic, and easing feels natural."),
          dict(q="Which makes far objects feel distant?", o=["Making them lighter and bluer", "Making them bright red", "Making them very sharp", "Making them larger"], a=0,
               why="Atmospheric depth reduces contrast and colour in the distance.")],
    activity="Paint a three-layer background at 1.5 times the frame width, calculate a 3 second pan with parallax percentages, ease the move, add contact shadows, and export a test to check it on your phone.",
)

LESSONS[13] = dict(   # Effects: smoke, water, fire and impact
    minutes=16,
    hook="A character stamps the ground, and a puff of dust bursts out. A candle flickers. A raindrop falls into a puddle and sends out rings. These small effects, called FX, are what make an animated world feel physical, and they are some of the most satisfying things to draw. They look complicated, but each one follows a handful of simple rules that you can learn in an afternoon. Effects are also drawn quickly: few frames, loose shapes, and no need to be precise. In this lesson you will learn the logic of smoke, fire, water and impact, with frame-by-frame recipes you can follow, how to loop effects, how to give them colour and glow, how to time them to the action and how to build a small library that you can reuse in every project.",
    sections=[
        ("Rules that apply to all effects", """Before the recipes, remember the common rules:

- **Shapes change quickly.** Do not draw the same shape twice. Each frame is a new, loose drawing.
- **Draw on twos or threes.** Effects look natural with 8 to 12 drawings per second, and the choppiness adds energy.
- **Start strong, end soft.** Most effects begin with a burst and fade away gradually.
- **Straight-ahead animation** suits effects, where you draw each frame after the last, so shapes evolve.
- **Anticipate and settle:** an effect comes from an action, such as a punch or a splash, so it **follows the action in time.**
- **Use few colours,** usually 2 or 3 tones.
- **Keep effects on their own layer,** so you can change timing without touching the character.
- **Look at real references** on your phone in slow motion.

If an effect looks wrong, check **timing first,** and then shape."""),
        ("Smoke and dust", """**Smoke** and **dust** are made of rounded puffs that grow and fade.

**A puff of smoke, about 10 to 12 frames on twos:**

1. **Frame 1:** a small, dense cloud at the source.
2. **Frames 2 to 4:** it **grows** and rises, with new bumps appearing at the edges.
3. **Frames 5 to 8:** it keeps **expanding but slows down,** and the shape gets lighter, with gaps.
4. **Frames 9 to 12:** it **breaks into pieces,** thins out and fades away.

Tips: use **soft round shapes with a few small details.** Make the **top move faster** than the bottom. Add a **darker core and a lighter edge.** **Dust** from feet is a low, flat cloud that spreads sideways along the ground, and shrinks and fades in 8 to 10 frames. Use a **loop** for continuous smoke from a chimney: the end must lead into the beginning."""),
        ("Fire", """Fire is a set of **tongues** that rise, split and shrink.

**A fire loop of 6 to 8 frames:**

1. **Draw a base** shape, a few tongues pointing upward.
2. In each new frame, **tongues move up,** get **thinner,** and **a small piece breaks off the top** and disappears.
3. **New tongues** grow from the base, so the fire is always renewing.
4. **Change the shape each frame** to avoid a mechanical look. Vary the heights.
5. Add a **bright core** (yellow or white) and an **outer layer** (orange and red).
6. Add a **few sparks** drifting up on a separate layer.

To make the loop work, **the last drawing should lead into the first,** and **different tongues should have different timing,** so the fire does not pulse together. Fire also **lights its surroundings:** add a warm orange glow on nearby objects and a flicker in the light."""),
        ("Water and impact", """**Water splash,** about 10 to 14 frames:

1. **Impact:** a small flat disc where the object hits.
2. **Crown:** the water rises in a ring, with points on top, in the first 3 or 4 frames.
3. **Drops:** droplets leave the crown, travel along **arcs** and fall.
4. **Settle:** the crown collapses, and **rings** spread out on the surface and fade.

**Rain and ripples:** a small drop, a tiny splash and a ring that expands and thins.

**Impact effect for a punch or a landing:**

1. **Frame 1:** a **bright flash** or a big, simple shape.
2. **Frames 2 and 3:** a **burst** with lines or a star shape, and a **smear** of the moving object.
3. **Frames 4 to 8:** **debris and dust** fly outward and slow down.
4. A tiny **camera shake** for a few frames.

Time the effect to **the exact contact frame.** Remember **anticipation:** a slight pause before a big hit makes it stronger."""),
        ("Colour, loops and an effects library", """To finish effects:

- **Colour:** use a limited palette that matches the scene. Warm tones for fire and explosions, blues and whites for water, greys and browns for smoke and dust.
- **Glow:** a soft, semi-transparent shape behind a bright effect, or a layer with a blend mode such as **add** or **screen** (check your program), makes light appear to glow.
- **Fade:** reduce opacity over the last few frames for a smooth finish.
- **Loops:** fire, rain, running water and chimney smoke should loop. **Check the join** by playing on repeat.
- **Scale and reuse:** a good effect can be **scaled, flipped and recoloured** to serve in many shots.
- **Build a library:** save your best effects as a **folder of PNG sequences** with clear names, like `fx_smoke_puff_12f`. Keep notes on frame count and use.

Practise by making **one new effect every week.** Within a month you will have a toolbox that makes every scene richer, and a strong showreel piece."""),
    ],
    diagram=timeline([("Frame 1", "bright flash"), ("Frames 2 to 3", "burst and smear"), ("Frames 4 to 6", "debris flies out"), ("Frames 7 to 10", "dust slows down"), ("Frames 11 to 12", "fade away")], note="Start strong, end soft."),
    caption="An impact effect starts with a flash, bursts and smears, throws debris, slows down and fades.",
    terms=[("FX", "Short for effects animation, such as smoke, fire, water and impacts."), ("Straight-ahead", "Drawing each frame in order so shapes evolve naturally."),
           ("Smear", "A stretched drawing that shows fast movement."), ("Loop", "An animation that ends where it begins so it can repeat."),
           ("Blend mode", "A setting that decides how a layer mixes with the layers below, such as add or screen."), ("Debris", "Small pieces thrown out by an impact.")],
    mistakes=["Drawing the same smoke shape on every frame.", "Starting a splash effect before the object has touched the water.", "Making a fire loop that jumps because the last frame does not match the first.", "Using too many colours in one effect."],
    quiz=[dict(q="What usually happens at the start of an impact effect?", o=["A bright flash or big simple shape", "A slow fade", "Silence", "A new layer"], a=0,
               why="Effects start strong and end soft."),
          dict(q="Which animation method suits effects best?", o=["Copying one drawing", "Only pose to pose", "Straight ahead, drawing frame after frame", "Tracing a photo"], a=2,
               why="Letting shapes evolve gives natural, flowing results."),
          dict(q="How should a fire loop end?", o=["With a cut", "With a long hold", "With a new colour", "The last drawing should lead into the first"], a=3,
               why="A smooth join makes the loop invisible."),
          dict(q="Why keep effects on their own layer?", o=["You can change them without touching the character", "To hide the character", "To lower the frame rate", "To remove sound"], a=0,
               why="Separate layers make timing and colour changes easy.")],
    activity="Draw four effects, a 12-frame smoke puff, an 8-frame fire loop, a splash and an impact, each on its own layer, export them as PNG sequences and use two of them in a short scene.",
)

LESSONS[14] = dict(   # Polishing, feedback and fixing common mistakes
    minutes=15,
    hook="Your animation is finished, in the sense that every part is drawn. But does it feel finished? Often the difference between student work and professional work is not talent but polish: the extra pass that smooths a jerky arc, fixes a floating foot, adds a missing blink, and trims two frames from a slow beat. Polish also means learning to take feedback without taking it personally, and learning when to stop, because you can polish forever. In this lesson you will learn a reliable order for polishing, the tricks that expose problems your eyes have got used to, a list of the most common mistakes and how to fix each one, how to give and receive feedback, and how to know when your work is ready to show.",
    sections=[
        ("Polish in the right order", """Work from the **big problems to the small ones.** Fixing small details on a scene with weak timing wastes time.

1. **Timing and spacing:** is the action clear and the weight right? Fix this first.
2. **Poses and silhouettes:** do the key poses read clearly?
3. **Arcs:** are the paths smooth?
4. **Overlap and follow-through:** do parts settle at different times?
5. **Holds and acting:** are there pauses for the audience?
6. **Details:** blinks, fingers, hair, small movements.
7. **Clean-up:** line quality, colour fills, stray marks, missing frames.
8. **Effects, sound and camera.**

Never skip ahead. A beautiful clean-up on top of the wrong timing is still a wrong animation. Give each pass a **checklist** and tick it off, and **save a new version** before each pass."""),
        ("Tricks to see your own work clearly", """After hours of work, your eyes stop seeing problems. Use these tricks:

- **Take a break.** Even ten minutes, or better, a night. Fresh eyes spot problems at once.
- **Play it small.** View the animation in a tiny window or on your phone. Weak poses and unclear actions show up.
- **Play it backward** or **flip it horizontally.** Your brain stops following the story and notices bumps in movement.
- **Scrub slowly** and step **frame by frame,** looking for popping and jumps.
- **Change the speed.** Play at half speed for the details and at double speed for the rhythm.
- **Watch with the sound off,** and then with the sound on.
- **View in silhouette** by turning the colour to black.
- **Look at one thing at a time:** one pass for arcs, one for the feet, one for the face.
- **Compare with reference** of real movement or a favourite film."""),
        ("Common mistakes and fixes", """The usual suspects, and what to do:

- **Floating or sliding feet:** pin the foot on the ground for the contact frames, and match the background speed.
- **Jerky or popping movement:** an in-between is off the arc. Trace the path and redraw the offending drawing.
- **Boiling lines:** outlines that wobble because each frame is traced differently. Keep a steadier line, draw on twos, or use a clean-up pass.
- **Changing size or proportion:** the character gets bigger or smaller across frames. Use a model sheet and a guide layer.
- **Stiff, robotic movement:** add overlap, arcs, easing and a head tilt.
- **Everything moves at once:** stagger the parts and add holds.
- **Too much squash and stretch:** the volume changes. Reduce, and keep it consistent.
- **Weak anticipation:** add a clearer wind-up before the main action.
- **Unclear action:** simplify the staging, and make the silhouette readable.
- **Too slow or too fast:** adjust the frame count.
- **Mismatched sound:** shift the audio or the frame so that hits line up."""),
        ("Giving and receiving feedback", """Feedback is how professionals improve. How to ask well:

1. **Show it to two or three people,** ideally including someone who has not seen it.
2. **Ask specific questions:** “Does the jump feel heavy?” “Where did you lose interest?” “What did the character feel?”
3. **Watch their faces** as they view it, without explaining.
4. **Listen, take notes and do not argue.** You do not have to agree, but understand the problem behind each comment.
5. **Look for patterns:** if three people mention the same moment, fix it.
6. **Separate problems from solutions.** People are often right about the problem and wrong about the fix.

How to give feedback: be **kind, specific and useful.** Say what works first, then name one or two problems with the exact moment (“frame 40, the foot slides”), and suggest a way to fix it. Join an **animation community** or class to exchange critiques regularly. Your skill grows fastest when you learn to see in other people's work what you cannot see in your own."""),
        ("Knowing when to stop", """You could polish forever, so set limits:

- **Define finished** before you start: a checklist of passes.
- **Set a deadline** for each pass.
- **Use the rule of diminishing returns:** if the last two hours made no visible change, you are done with that pass.
- **Do not chase perfection.** Aim for clear, appealing and consistent. Many professional animators say a project is never finished, only released.
- **Keep a final checklist:** correct frame rate and size, no missing frames, sound in sync, credits added, file named and backed up.
- **Export a test,** watch it on two devices, and fix only real problems.
- **Save the project,** write a short note about what you learned and **start something new.** The next piece teaches you more than another week of fixing this one.

Remember that every animator looks back on early work and sees mistakes. That is a sign you are improving."""),
    ],
    diagram=pyramid([("CLEAN-UP", "last: lines and colour"), ("DETAILS", "blinks, hands, hair"), ("OVERLAP AND ACTING", "holds and follow-through"), ("POSES AND ARCS", "clear and smooth"), ("TIMING AND SPACING", "fix this first")], note="Fix the big problems first."),
    caption="Polish from the bottom up: timing and spacing first, then poses and arcs, then acting, details and clean-up.",
    terms=[("Polish", "The final passes that make an animation smooth and appealing."), ("Boiling lines", "Outlines that wobble from frame to frame."),
           ("Popping", "A sudden jump in movement caused by a drawing off the path."), ("Silhouette check", "Viewing the animation as solid black shapes to test clarity."),
           ("Critique", "A careful, constructive discussion of someone's work."), ("Diminishing returns", "The point where extra work gives very little improvement.")],
    mistakes=["Polishing small details before the timing is right.", "Arguing with people who give feedback.", "Never stepping away so problems stay invisible.", "Polishing forever instead of releasing and starting something new."],
    quiz=[dict(q="What should you fix first when polishing?", o=["Clean-up of lines", "Timing and spacing", "The credits font", "The file name"], a=1,
               why="Wrong timing cannot be saved by clean lines."),
          dict(q="Why play your animation backward or flipped?", o=["It exposes bumps your eyes have grown used to", "It improves sound", "It reduces size", "It changes frame rate"], a=0,
               why="A new view stops your brain following the story, so problems show."),
          dict(q="What causes boiling lines?", o=["Outlines traced differently on every frame", "Too many layers", "Wrong audio", "A slow computer"], a=0,
               why="Wobbly outlines come from inconsistent line work."),
          dict(q="How should you react to feedback?", o=["Listen, take notes and look for patterns", "Argue", "Ignore all of it", "Delete the project"], a=0,
               why="Patterns in feedback show real problems to fix.")],
    activity="Take a finished animation and polish it in order using a written checklist. Use at least four seeing tricks, get feedback from three people with specific questions, fix the top three problems and stop on a set deadline.",
)

LESSONS[15] = dict(   # Final project: a 10-second animated scene
    minutes=17,
    hook="Now you bring everything together. A ten-second scene sounds tiny, yet it is 240 frames at 24 frames per second, and it will contain all the skills you have built: planning, timing, weight, acting, backgrounds, effects, sound and polish. Ten seconds is also the perfect size for a first complete piece. It is short enough to finish, long enough to show a story and strong enough to open a showreel. The skill that this project tests most is not drawing but project management: choosing a small idea, breaking it into steps, protecting your time and finishing. In this final lesson you will receive a clear brief, a realistic plan with dates, a production checklist, a way of testing your work and a plan for sharing it with the world.",
    sections=[
        ("The brief", """**Create an original 10-second animated scene** with these rules:

- **One main character** (original, not copied from another film or game).
- **One location** with at least two layers.
- **A clear small story:** a want, a problem and a result in ten seconds.
- **At least three skills** from the course visible: for example weight and timing, a walk or jump, an acting moment with a hold, an effect and a camera move.
- **Sound:** at least one sound effect, plus music or voice you have the right to use.
- **Format:** 1280 by 720 (or 1920 by 1080), 24 fps, exported as an MP4 and a PNG master.
- **Credits:** a short end card.

**Idea examples:** a fisherman pulls a boot out of the water instead of a fish. A child chases a rolling mango through a market. A tired robot finds a charging socket. A cat jumps for a bird and lands in a bucket. Keep it **simple, funny or touching,** and doable."""),
        ("Plan the schedule", """Work backward from a deadline. For a part-time student, **three weeks** is realistic.

**Week 1: Plan**
- Day 1 to 2: idea, one-sentence story, thumbnails.
- Day 3 to 4: character design, model sheet, background sketch.
- Day 5 to 7: storyboard and an **animatic** with rough sound. Lock the timing at 240 frames.

**Week 2: Animate**
- Day 8 to 10: key poses and breakdowns for all shots.
- Day 11 to 13: in-betweens and arcs.
- Day 14: background and layers.

**Week 3: Finish**
- Day 15 to 16: effects and camera.
- Day 17: sound and music.
- Day 18 to 19: polish passes and feedback.
- Day 20: export, test, credits.
- Day 21: **buffer** for problems and rest.

Add **25% extra** to every estimate. Power cuts, illness and life will happen. Mark each day on a calendar, and **save and back up every day.**"""),
        ("Production checklist", """Use this list and tick as you go.

**Pre-production:** logline, thumbnails, model sheet, background sketch, storyboard, animatic with timing.

**Production:**
1. Set the project (size, 24 fps) and the folder structure.
2. Block key poses on the timeline and **watch the rhythm.**
3. Add breakdowns, then in-betweens.
4. Check **arcs, weight and overlap.**
5. Add the background layers and **camera move.**
6. Add **effects** on their own layers.
7. Record or find **sound,** and sync it.
8. **Polish** in order: timing, poses, details, clean-up.

**Finishing:**
9. Colour check on a phone.
10. Add the end card with your name, music credits and tool credits.
11. Export a **PNG master** and an **MP4** (H.264) at 720p or 1080p.
12. Watch the export from start to finish with sound.
13. Back up in two places.

Keep a short **production diary:** one line a day about what you did and learned."""),
        ("Test, feedback and the rubric", """Before you call it finished, test it against a **rubric** like the one a teacher or reviewer might use:

- **Story and clarity (20%):** does it make sense in ten seconds?
- **Timing and weight (20%):** do things feel heavy or light as intended?
- **Principles in use (20%):** arcs, anticipation, overlap, squash and stretch.
- **Acting and appeal (15%):** does the character feel alive?
- **Design and layers (10%):** clear backgrounds, depth and consistency.
- **Sound (10%):** clear, in sync, and properly licensed.
- **Finish (5%):** clean export, credits, no errors.

Show the scene to **three viewers** who have not seen it, and ask: what happened, what did the character want, which moment did you like, and where were you confused? Fix the **top two problems.** Do not rewrite the whole scene at this stage."""),
        ("Share it and keep growing", """Finishing is only half of the job. Show your work:

- **Upload** to a video site and a **portfolio page,** with a title, a short description, your role and the tools used.
- **Credit** everyone and every asset, and mention any AI assistance honestly if you used it.
- **Share** a short clip on social media, with a behind-the-scenes sketch or the animatic. Post a **looping GIF** of the best moment.
- **Join challenges and communities,** and ask for critique.
- **Add it to your showreel,** at the strongest place.
- **Write a short reflection:** what worked, what was hard, what you would do differently, and your next goal.
- **Pick the next step:** a longer scene, a new skill such as 3D or lip-sync, or a team project.

Congratulations. You have planned, animated, polished and delivered a complete piece. Keep that spirit, and animate something every week."""),
    ],
    diagram=timeline([("Idea", "one sentence"), ("Animatic", "lock the timing"), ("Key poses", "block the action"), ("In-betweens", "arcs and weight"), ("Polish", "feedback and fixes"), ("Release", "export and share")], note="240 frames, one step at a time."),
    caption="Idea, animatic, key poses, in-betweens, polish and release: the path of a ten-second scene.",
    terms=[("Brief", "A short description of what the project must include."), ("Animatic", "A storyboard timed with sound that locks the length of the scene."),
           ("Buffer", "Extra time added to a schedule for problems."), ("Rubric", "A list of criteria used to judge a project."),
           ("PNG master", "The numbered image sequence kept as the highest quality copy."), ("Production diary", "Short daily notes about what you did and learned.")],
    mistakes=["Choosing an idea too big for ten seconds.", "Skipping the animatic and locking timing late.", "Having no buffer in the schedule.", "Exporting only a video file and not backing up the project."],
    quiz=[dict(q="How many frames is a ten-second scene at 24 fps?", o=["24", "120", "240", "2400"], a=2,
               why="10 seconds multiplied by 24 frames per second is 240 frames."),
          dict(q="Why add a buffer to the schedule?", o=["Problems and delays will happen", "To make the film longer", "To remove sound", "To change fps"], a=0,
               why="Power cuts, illness and mistakes should not ruin the deadline."),
          dict(q="What should you do before calling the scene finished?", o=["Show it to three viewers and fix the top problems", "Delete the backup", "Add random effects", "Skip the export test"], a=0,
               why="Fresh viewers find confusion you cannot see."),
          dict(q="Which kind of idea suits a ten-second project?", o=["A small, simple, clear story", "A feature film plot", "A battle with fifty characters", "A music video with ten locations"], a=0,
               why="Small ideas get finished and can be polished.")],
    activity="Plan and animate your own 10-second scene using the three-week schedule: animatic, key poses, in-betweens, background, effect, sound, polish and export. Share it with a short reflection and ask three viewers for feedback.",
)
