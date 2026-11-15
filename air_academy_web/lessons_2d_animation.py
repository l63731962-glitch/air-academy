"""2D Animation Fundamentals: deep lesson pages 1 to 5.
Same format as lessons_animation.py: hook, sections, diagram, terms, mistakes, quiz. Quiz "a" = index of the right option."""
from diagrams import flow, compare, hub, cycle

LESSONS = {
    1: dict(
        minutes=13,
        hook="Open the camera on your phone and record two seconds of a friend clapping. Play it back in slow motion and you will notice something strange: the hands are never really moving. Every frame is a still photo, and the hands are simply in a different place each time. Animation uses the same trick, except you decide where the hands are in every frame. Get two decisions right, how long and how far, and even a plain circle can feel heavy, light or alive. Those two decisions are called timing and spacing, and they are the foundation of everything else in this track.",
        sections=[
            ("A clip is a stack of still pictures", """Your eyes and brain join pictures that change quickly into smooth movement. To plan an animation, you only need three numbers:

- **Frame:** one single picture.
- **Frame rate (fps):** how many frames play each second. Cinema uses 24. Many television systems use 25, and a lot of online video uses 30.
- **Duration:** how long the clip runs.

The sum is easy: **frames = fps x seconds**. A 3-second clip at 24 fps needs 72 frames. A 15-second clip needs 360 frames. Choose one frame rate at the start of the project and keep it until the end. If you change it halfway, every movement you timed will speed up or slow down."""),
            ("On ones and on twos", """Drawing 24 new pictures for every second of film is a lot of work, so animators often draw **on twos**: each drawing is shown for two frames. At 24 fps that is **12 drawings per second** instead of 24. Drawing **on ones** means a new drawing for every frame.

- **On twos** looks classic and readable. Use it for walking, talking, waving and anything at a calm pace.
- **On ones** looks smoother. Use it for very fast action, quick camera moves and sharp turns, where on twos would look jumpy.

You can mix them in one scene. A character who slowly lifts a cup can be on twos, then a fast slap on the table can switch to ones for three or four frames. Our eyes forgive twos in slow action, but we notice them in fast action."""),
            ("Timing: how many frames an action takes", """**Timing** is the number of frames an action uses. It carries weight, size and feeling. A balloon drifts down slowly, so it needs many frames. A stone drops fast, so it needs few.

Real life is a good teacher. An object dropped from about one metre takes a little under half a second to land. At 24 fps that is about **10 to 12 frames**. So a basketball falling from head height can use 11 frames, and a full bounce (down and back up) fits in about 22 to 24 frames, one second.

> [Quick feel guide, at 24 fps]
> 4 frames: a snap, a blink, a slap
> 12 frames: half a second, a normal gesture
> 24 frames: one second, a full bounce or one stride pair
> 48 frames: two seconds, a slow, heavy or sleepy movement

These are starting points, not laws. Act it out yourself with a stopwatch on your phone, then adjust."""),
            ("Spacing: how far the object moves each frame", """**Spacing** is the distance an object travels between one frame and the next. The same timing can feel completely different with different spacing.

- Gaps that stay the same feel mechanical, like a robot or a conveyor belt.
- Gaps that grow bigger feel like **speeding up**.
- Gaps that shrink feel like **slowing down**.

Gravity has a neat pattern. A ball released from rest covers distances in the ratio **1 : 3 : 5 : 7 : 9** in equal time steps. Say it falls 25 units in five frames. The gaps between its positions will be 1, 3, 5, 7 and 9 units, and 1 + 3 + 5 + 7 + 9 = 25. On the way back up, the ball slows down, so you use the same gaps in reverse: 9, 7, 5, 3, 1. Draw those gaps on a ruler and the ball will feel like it obeys gravity."""),
            ("Your first exercise: the bouncing ball", """Do this on paper with a phone camera, or in a free tool such as Krita or Pencil2D. Tool features change, so check each tool's own website for its current download and manual.

1. Draw a ground line and a ball at the top of its bounce. This is **key 1**.
2. Draw the ball just touching the ground. This is **key 2**.
3. Draw the ball back at the top. This is **key 3**.
4. Mark the gaps on a chart: small gaps near the top, big gaps near the ground.
5. Draw the in-betweens following your chart. Turn on **onion skinning**, which shows faint ghosts of the drawings before and after the one you are working on. It makes the gaps easy to see.
6. Flip through the pages or play the frames, then fix any gap that looks wrong.

Finish with 24 frames on twos (12 drawings). Keep the ball the same size in every drawing for now. In the next lessons you will learn when to change it on purpose."""),
        ],
        diagram=compare(("On ones", ["24 drawings each second", "Smoothest movement", "Best for fast action", "More work"]), ("On twos", ["12 drawings each second", "Classic, readable look", "Best for calm action", "Half the work"]), vs="vs", note="Same one second of film at 24 fps"),
        caption="The same one second of film: ones give the smoothest movement, twos use half the drawings.",
        terms=[("Frame", "One single picture in an animation."), ("Frame rate (fps)", "The number of frames shown each second."), ("On ones", "A new drawing for every frame."),
               ("On twos", "Each drawing is held for two frames, so you draw half as many."), ("Timing", "The number of frames an action takes."),
               ("Spacing", "The distance an object moves from one frame to the next."), ("Onion skinning", "A view that shows faint copies of the drawings before and after the current one.")],
        mistakes=["Changing the frame rate halfway through a project, so every movement you timed runs too fast or too slow.", "Spacing every frame evenly, so the object moves like a machine.",
                  "Drawing slow actions on ones and doubling the work for no visible gain.", "Letting the ball change size from drawing to drawing by accident."],
        quiz=[dict(q="A 3-second clip runs at 24 frames per second. How many frames is that?", o=["48", "72", "36", "96"], a=1, why="Frames equal fps times seconds, so 24 x 3 = 72 frames."),
              dict(q="You animate on twos at 24 fps. How many different drawings do you need for one second?", o=["24", "6", "12", "48"], a=2, why="On twos, each drawing lasts two frames, so 24 frames need 12 drawings."),
              dict(q="A ball falls and the gaps between frames are 1, 3, 5, 7 and 9 units. What does this pattern show?", o=["It is speeding up, as gravity pulls it", "It falls at a steady speed", "It is slowing down", "It has stopped"], a=0, why="Gaps that grow bigger from frame to frame mean the object is speeding up, which is how a falling object behaves."),
              dict(q="What is onion skinning?", o=["Cutting a drawing into layers", "Exporting the clip as a video", "Choosing a frame rate", "Seeing faint ghosts of the drawings before and after the current one"], a=3, why="Onion skinning shows the neighbouring drawings faintly, so you can judge the gaps and keep the movement smooth.")],
    ),
    2: dict(
        minutes=14,
        hook="Watch a goalkeeper dive for a penalty. You remember three pictures: the crouch before the kick, the stretch in mid-air, and the landing in the dust. You do not remember the pictures in between, and neither does your audience. Animators work the same way. They draw the three or four pictures that matter first, and only then fill the gaps. This lesson shows how to choose those pictures, how to fill the gaps without losing the energy, and how to make movement speed up and slow down the way real bodies do.",
        sections=[
            ("Keys, breakdowns and in-betweens", """Every action is built in three layers of drawings:

- **Key poses** (keys) are the most important moments: where the action starts, its extreme point, and where it ends.
- **Breakdowns** sit between keys and decide the **path** the movement takes, for example whether the arm goes up in a curve or a straight line.
- **In-betweens** are all the remaining frames that join the poses smoothly.

Take a one-second jump at 24 fps. Frame 1 is the crouch (key). Frame 8 is the body leaving the ground, stretched (key). Frame 14 is the top of the jump (key). Frame 20 is the landing (key). A breakdown at frame 11 shows the body curving up. Frames such as 2 to 7 are in-betweens. You can already judge the jump from four rough pictures, so fix the story there before you spend time on cleaner drawings."""),
            ("Two ways to work: pose to pose and straight ahead", """**Pose to pose** means you draw the keys first, then the breakdowns, then the in-betweens. You stay in control of timing and the final pose, which is why most character work is done this way.

**Straight ahead** means you start at frame 1 and draw one frame after another to the end, without planning each pose. It gives lively, surprising motion, so it suits fire, smoke, water, hair and wild, chaotic action. The risk is that the drawing can drift, grow or shrink along the way.

Many animators combine both: keys for the body, straight ahead for the hair and the flames. If you are new, start with pose to pose. It is easier to fix, because a problem in a key pose is visible in the first rough pass."""),
            ("Arcs: living things rarely move in straight lines", """Look at your own arm as you wave. The hand does not travel in a straight line, it follows a curve. Joints rotate, so almost every part of a living body moves in an **arc**. Animation that follows arcs looks natural. Animation that moves in straight lines looks stiff.

To check, draw the path of the hand, the head or the ball through every frame, as a dotted line. If the dots form a smooth curve, you are good. If one dot jumps out of line, fix that in-between.

There are exceptions. Machines, a falling stone and a sliding box move in straight lines, so for them, a straight path is correct. Choose the path that matches what is moving."""),
            ("Easing: slow in and slow out", """Real things do not start and stop instantly. They pick up speed and then settle. Animators call this **ease in** (slowing in) and **ease out** (slowing out), or together **slow in and slow out**. In drawings, you create it with spacing: put the in-betweens close together near a key, and spread them out in the middle.

Here is a worked example. A box slides 100 pixels in 8 frames.

> [Linear, no easing]
> Gaps: 12, 13, 12, 13, 12, 13, 12, 13  (steady, robotic)
>
> [Eased, slow in and slow out]
> Gaps: 4, 11, 16, 19, 19, 16, 11, 4  (starts gently, speeds up, settles)

Both add up to 100 pixels and both take 8 frames. Only the spacing changed, and the second one feels natural. If an action is sudden, such as a slap, use less easing at the start."""),
            ("Reading a timing chart", """A **timing chart** is a small ruler drawn beside a key pose. It tells the person who draws the in-betweens exactly where each one goes. Ticks show the frames, and a number or fraction beside each tick says how far between the two keys that drawing sits.

> [Key A to Key B over 8 frames, eased]
> Frame 1: Key A
> Frame 2: very close to A (about 1/20 of the way)
> Frame 3: about 1/6 of the way
> Frame 5: the middle, the breakdown (1/2)
> Frame 7: close to B (about 5/6 of the way)
> Frame 9: Key B

The rule of thumb is: **favour the key you are leaving or arriving at**. Put the in-betweens nearer to the key at both ends, and you get slow in and slow out. Always test by flipping or playing the frames, because your eye is a better judge than the numbers."""),
        ],
        diagram=flow([("KEYS", "Big moments|first"), ("BREAKDOWN", "Choose the|path"), ("IN-BETWEEN", "Fill the|gaps"), ("CLEAN-UP", "Tidy the|lines"), ("TEST", "Play and|fix timing")], "d2", "Work from big decisions to small ones, and test at every stage"),
        caption="Work from the big decisions to the small ones, and test your timing at every stage.",
        terms=[("Key pose", "An important drawing that defines the start, extreme or end of an action."), ("Breakdown", "A drawing between two keys that decides the path of the movement."),
               ("In-between", "A drawing that fills the gap between two poses."), ("Pose to pose", "Drawing the keys first, then filling in the rest."),
               ("Straight ahead", "Drawing every frame in order from the first to the last."), ("Arc", "The curved path that most living movement follows."),
               ("Slow in and slow out", "Easing: gentle starts and stops, with the fastest movement in the middle.")],
        mistakes=["Drawing clean, final frames before the rough keys are approved.", "Moving a hand or head in a straight line instead of along an arc.", "Spreading in-betweens evenly, so everything starts and stops like a machine.",
                  "Using straight ahead for a precise action, then finding that the character drifts or changes size."],
        quiz=[dict(q="In a jump, which drawing is a key pose?", o=["Frame 2, between two other drawings", "A drawing that only tidies a line", "The extreme point at the top of the jump", "The sound that plays during the jump"], a=2, why="Key poses are the important moments: the start, the extreme point and the end. The others fill the gaps."),
              dict(q="Which method suits smoke, fire and wild hair best?", o=["Straight ahead", "Pose to pose only", "Timing charts only", "Colouring first"], a=0, why="Drawing straight ahead gives lively, unpredictable motion, which suits natural and chaotic movement."),
              dict(q="A box slides 100 pixels in 8 frames with gaps 4, 11, 16, 19, 19, 16, 11, 4. What does this show?", o=["It speeds up all the way", "It moves at a steady speed", "It only slows down", "It starts gently, speeds up, then settles"], a=3, why="Small gaps at both ends and big gaps in the middle make slow in and slow out."),
              dict(q="Why do you draw the path of a waving hand as a dotted line?", o=["To make the drawing smaller", "To check that it follows a smooth arc", "To change the frame rate", "To add colour"], a=1, why="Living movement follows arcs. A dotted path shows quickly whether one in-between jumps out of line.")],
    ),
    3: dict(
        minutes=14,
        hook="A boy kicks a football. Before his foot swings forward, it goes back. After the ball has left, his leg keeps swinging, and his shirt keeps flapping for a moment longer. Those extra movements are so natural that you never notice them, until they are missing. Remove them and the kick looks like a puppet being jerked on strings. This lesson teaches the principles that fix that: squash and stretch, anticipation, follow-through and exaggeration. Learn these four and your ball, your character and even a simple box will start to feel alive.",
        sections=[
            ("Squash and stretch", """A soft object changes shape when it moves. It **squashes** when it hits something and **stretches** when it moves fast. The golden rule: **its volume stays the same**. If it gets wider, it must get shorter.

For a ball that is 100 units wide and 100 units tall, a good squash on landing could be 130 wide and 77 tall. Check it: 100 x 100 = 10,000 and 130 x 77 = 10,010, so the size feels the same. When the ball shoots upward, stretch it **in the direction it is moving**, for example 85 wide and 118 tall.

How much to squash depends on the material. A rubber ball squashes a lot. A bowling ball hardly squashes at all. A brick does not squash. Match the amount to what the object is made of, or the audience will not believe it."""),
            ("Anticipation", """**Anticipation** is a small movement in the opposite direction before the real action. A person bends their knees before a jump, and a bowler swings the arm back before the throw. It tells the audience what is about to happen and gives the action power.

How long should it be? Think of it as a ratio. For a one-second jump at 24 fps, a crouch of 6 to 8 frames and a launch of only 1 or 2 frames makes the jump feel explosive. A bigger action needs a bigger wind-up.

You can also break the rule on purpose. A surprise, such as a ball suddenly leaping out of a bush, may have no anticipation at all, which is why it shocks. Use anticipation when the audience must read the action, and skip it when you want a surprise."""),
            ("Follow-through and overlapping action", """**Follow-through** means parts of an object keep moving after the main body has stopped. **Overlapping action** means different parts start and stop at different times. Loose or heavy things lag behind: hair, a shirt, a tail, a hat, an antenna.

A reliable way to think about it is that the **leading part moves first and the trailing parts arrive a few frames later**. Two to four frames of delay is a good starting point.

> [A character stops suddenly after running]
> Frame 1: the body stops
> Frames 2 to 4: the shirt and hair keep going forward
> Frames 5 to 8: they swing back a little, a smaller movement
> Frames 9 to 12: they settle

Each swing should be smaller than the last, like a ball bouncing lower each time, until it rests. Without this, the character looks like a single hard block."""),
            ("Exaggeration", """Animation is not copying real life, it is the **illusion** of real life. A pose that is exactly realistic often looks weak on screen. So push the pose a little further than real life: a deeper crouch, a bigger stretch, a wider smile. The audience reads it faster.

Keep control, though:

- Exaggerate **one thing** at a time so the moment stays clear.
- Keep the volume rule from squash and stretch, even when you exaggerate.
- If it looks silly, pull it back a little. Good exaggeration feels powerful, not broken.

A fast way to check is to look at your key poses as small thumbnails. If you can understand the action from the silhouette alone, the pose is strong."""),
            ("Worked example: a ball with a tail lands", """Combine all four ideas in one short exercise. Imagine a ball with a long tail falling to the ground.

1. **Frames 1 to 8 (fall):** the ball stretches a little as it speeds up, and the tail trails **above** it, because it lags behind.
2. **Frame 9 (contact):** the ball squashes flat, 130 wide and 77 tall. The tail keeps moving down and arrives a few frames later.
3. **Frames 10 and 11:** the ball stretches back up as it rebounds, and the tail whips down past the ball, a clear follow-through.
4. **Frames 12 to 20:** the ball rises to a smaller bounce. The tail swings back up and down in smaller and smaller waves until frame 24, when it settles.

When you finish, flip through the drawings. Check three things: the ball's volume feels constant, the tail always lags the ball, and each swing is smaller than the one before."""),
        ],
        diagram=hub(("Alive", "4 ideas"), [("Squash", "and stretch"), ("Anticipation", "the wind-up"), ("Follow-through", "parts keep going"), ("Exaggeration", "push it further")], "Use them together, one clear idea at a time"),
        caption="Four ideas that turn a moving shape into something that feels alive.",
        terms=[("Squash", "Flattening an object when it hits something."), ("Stretch", "Lengthening an object in the direction it moves quickly."),
               ("Volume", "The overall size of an object, which should feel constant during squash and stretch."), ("Anticipation", "A small opposite movement before the main action."),
               ("Follow-through", "Parts that keep moving after the main body stops."), ("Overlapping action", "Different parts of an object starting and stopping at different times."),
               ("Exaggeration", "Pushing a pose or movement beyond real life so it reads more clearly.")],
        mistakes=["Squashing a ball so it gets wider and also taller, so it seems to grow.", "Squashing hard objects such as a brick or a bowling ball as much as a rubber ball.",
                  "Moving hair, tails and clothes at exactly the same time as the body, so they look glued on.", "Exaggerating everything at once, so the audience cannot tell what is important."],
        quiz=[dict(q="A ball is 100 wide and 100 tall. Which squash best keeps its volume?", o=["130 wide and 130 tall", "100 wide and 150 tall", "70 wide and 70 tall", "130 wide and 77 tall"], a=3, why="When the shape gets wider it must get shorter. 130 x 77 is about 10,000, the same as 100 x 100."),
              dict(q="Why do animators add anticipation before a jump?", o=["It makes the action clearer and more powerful", "It makes the clip longer for no reason", "It removes the need for in-betweens", "It changes the frame rate"], a=0, why="The small opposite movement tells the audience what is about to happen and gives the jump energy."),
              dict(q="A character stops running. What should the loose shirt do?", o=["Stop at exactly the same frame", "Keep moving, then swing back in smaller movements", "Disappear", "Move faster each swing"], a=1, why="Loose parts lag behind and keep going, then settle with smaller and smaller swings."),
              dict(q="You squash a bowling ball as much as a rubber ball. What is the problem?", o=["It uses too few frames", "The colour is wrong", "The amount of squash does not match the material", "It needs more anticipation"], a=2, why="A heavy, hard ball hardly changes shape. The squash must match what the object is made of.")],
    ),
    4: dict(
        minutes=15,
        hook="Stand at a bus stop and watch people walk past. Without hearing a word, you can tell who is tired, who is late, who is carrying something heavy and who is happy. You can even recognise your own mother from far away just by the way she walks. A walk is full of information, and it is also the first big test of an animator. If you can animate a walk that loops, feels heavy enough and does not slide on the ground, you have learned most of what makes character animation work. This lesson gives you the four poses, the timing and the checks.",
        sections=[
            ("The four poses of a step", """One step is built from four poses. Learn them and you can draw a walk from memory:

1. **Contact:** the front heel has just touched the ground. The legs are as far apart as they get.
2. **Down:** the body drops onto the front leg and takes the weight. This is the **lowest** point of the body.
3. **Passing:** the back leg swings past the front one, and the body starts to rise.
4. **Up:** the body is pushed to its **highest** point, with the back toe leaving the ground.

Then the next contact starts the other leg, so a full walk cycle repeats these four poses twice, once for each leg. Draw them as rough stick figures first, and check the body height: it goes down, rises through the passing pose, peaks at up, and comes back down."""),
            ("Timing: how many frames", """A normal walking pace is a little under two steps each second. At 24 fps, that means **12 frames for one step** and **24 frames for a full cycle of two steps**. This is a good starting point. Use fewer frames for a fast or hurried walk and more for a slow, tired one.

Here is a plan for a 24-frame cycle with a pose every three frames:

> [24-frame walk cycle]
> Frame 1: Contact (right foot forward)
> Frame 4: Down
> Frame 7: Passing
> Frame 10: Up
> Frame 13: Contact (left foot forward)
> Frame 16: Down
> Frame 19: Passing
> Frame 22: Up
> Then back to frame 1

Draw the contact poses first, then the passing poses, then the down and up poses. Finish with the in-betweens."""),
            ("Arms, head and weight", """The body does many small things together:

- **Opposite arm and leg:** when the right leg goes forward, the left arm swings forward. The arms usually swing less than the legs.
- **Hips and shoulders:** they rotate in opposite directions. A little twist makes the walk look natural.
- **Head:** it stays fairly steady and bobs only a little. A strong head bounce looks cartoony, and that can be fine on purpose.
- **Weight:** bend the supporting knee at the down pose, and hold the down pose a frame longer for a heavy character. A light, bouncy character spends longer on the up pose.

A walk also shows character. A market porter carrying a load walks low and slow, with short steps. A student late for school walks with a long stride and forward-leaning body. Change the poses, not just the speed."""),
            ("Making the cycle loop", """A **cycle** is a short animation that you repeat again and again. For it to loop, the last drawing must lead smoothly back to the first one.

The most common bug is a stutter. If your cycle is 24 frames and frame 25 is a copy of frame 1, then looping frames 1 to 25 shows the same pose twice and the walk hiccups. The loop must contain frames **1 to 24 only**. The next drawing after frame 24 is frame 1 again.

Test it by playing the cycle on repeat for 30 seconds. If you feel a tiny pause at the same spot each time, a pose is duplicated or missing. Also compare the first and last drawings. They should look like two neighbouring frames, not two identical ones."""),
            ("In place or across the screen", """You can show a walk in two ways:

- **In place:** the character's body stays in the same spot, and the background slides past in the opposite direction. Easy to make and easy to loop.
- **Across the screen:** the character actually travels. Now you must avoid **foot sliding**, where the planted foot skates on the ground.

Here is a worked example. Say a step is 60 pixels long and takes 12 frames. The character must move forward 60 / 12 = **5 pixels every frame**, at the same speed, with no easing. The planted foot must move backward relative to the body by exactly 5 pixels per frame, so that it stays still on the ground. If the foot looks like it is sliding, the body is moving too fast or too slow for the step length. Change one number until the foot sticks to the ground."""),
        ],
        diagram=cycle([("CONTACT", "Heel lands"), ("DOWN", "Lowest point"), ("PASSING", "Legs cross"), ("UP", "Highest point")], "d4", "ONE STEP|12 frames", "Repeat on the other leg to finish the cycle"),
        caption="One step is four poses. Repeat them on the other leg and you have a full cycle.",
        terms=[("Contact", "The pose when the front heel touches the ground and the legs are furthest apart."), ("Down", "The lowest point of the body, as it takes the weight."),
               ("Passing", "The pose where the back leg swings past the supporting leg."), ("Up", "The highest point of the body, as it pushes off the ground."),
               ("Cycle", "A short animation that repeats without a visible jump."), ("Foot sliding", "A mistake where a planted foot appears to skate across the ground."),
               ("Walk in place", "A walk where the character stays still and the background moves.")],
        mistakes=["Copying the first frame onto the last, so the loop shows the same pose twice and stutters.", "Swinging the arm on the same side as the forward leg.",
                  "Moving the character at a speed that does not match the step length, which causes foot sliding.", "Keeping the body at the same height all the time, so the walk has no weight."],
        quiz=[dict(q="Which pose is the lowest point of the body in a step?", o=["Down", "Up", "Passing", "Contact"], a=0, why="At the down pose, the body drops onto the front leg and takes the weight, so it is at its lowest."),
              dict(q="At 24 fps, how many frames are a good starting point for a full two-step cycle?", o=["6", "12", "48", "24"], a=3, why="A step takes about 12 frames at a normal pace, so two steps take about 24 frames."),
              dict(q="Your walk cycle has 24 frames, and frame 25 is a copy of frame 1. What happens when it loops?", o=["It plays faster", "A pose is shown twice, causing a stutter", "The character walks backwards", "The loop is perfect"], a=1, why="Looping 1 to 25 repeats the same pose twice. A 24-frame cycle should loop frames 1 to 24."),
              dict(q="A step is 60 pixels and takes 12 frames. How far should the character move each frame to avoid foot sliding?", o=["12 pixels", "3 pixels", "5 pixels", "60 pixels"], a=2, why="60 pixels divided by 12 frames is 5 pixels per frame, so the planted foot stays still on the ground.")],
    ),
    5: dict(
        minutes=14,
        hook="You have animated a bouncing ball and a walking character. Right now they live on a blank white page, with no place to be and no sound. A film is more than moving drawings. It needs a world, a camera that decides what we look at, sound that makes us feel something, and a file that actually plays on a friend's phone. This lesson walks you through the finishing work for a short clip of 10 to 20 seconds, the stage where a pile of animation exercises becomes something you can proudly send on WhatsApp or put in your portfolio.",
        sections=[
            ("Build the scene in layers", """Most 2D scenes are made of **layers**, like sheets of clear plastic stacked on top of each other:

- **Background:** the sky, the street, the room. It rarely changes, so draw it once and reuse it.
- **Character layer:** the animated drawings.
- **Foreground:** things in front of the character, such as a fence, a plant or a table edge.

Layers have two big benefits. First, you never redraw the background for every frame. Second, you can move layers at **different speeds** to create depth. When the camera pans, far-away layers move slowly and near layers move faster. This is called **parallax**, and it makes a flat drawing feel like a real space.

Name your layers clearly, such as "bg_street", "char_walk" and "fg_fence", and lock the background so you do not move it by accident. Keep the character's feet on a consistent ground line."""),
            ("Pan, zoom and the camera", """A **pan** slides the view across the scene. A **zoom** moves closer to or further from something. A **hold** keeps the camera still. Each one tells the audience where to look.

Use camera moves with a reason:

- **Pan** to follow a walking character, or to reveal a new place.
- **Zoom in** slowly to build tension or show a feeling on a face.
- **Hold** when something important happens, so nothing competes for attention.

Ease the start and stop of every move, exactly like slow in and slow out, or the camera will feel robotic. Keep faces and key action away from the extreme edges of the frame. Phones, apps and video sites crop and cover parts of the screen, so a safe margin of about a tenth of the width on each side protects your important details."""),
            ("Sound: music, effects and levels", """Sound is half of the film. A silent bouncing ball is nice, but a ball with a small "boing" at the exact frame of impact is delightful.

- **Sync effects to the frame.** At 24 fps, one frame lasts about 0.04 seconds. Put the footstep sound on each contact frame, and the bounce sound on the squash frame.
- **Set the levels.** Music should sit **under** voices and effects, so it supports the scene without covering it. Watch the level meter: the loudest peaks should never hit the red zone, because that causes ugly distortion.
- **Listen on two systems.** Check on headphones and on a phone speaker, because many viewers will use only the phone.
- **Respect licences.** Use sounds you recorded or made yourself, or sounds whose licence allows your use. Some free sounds require you to credit the creator, so read the licence and put the credit in your end card.

A good test: close your eyes and listen to the clip once. If you can follow the story by sound alone, the mix is working."""),
            ("Export: an MP4 for WhatsApp and one for YouTube", """The most widely supported format is an **MP4 file with H.264 video**. Almost every phone, computer and website plays it. Make **two versions**:

1. **For WhatsApp and sharing on mobile data:** a smaller size, such as 720p, so it sends quickly. WhatsApp recompresses videos anyway, so a huge file gives no benefit.
2. **For YouTube and your portfolio:** a larger size, such as 1080p (1920 x 1080), in the frame rate you animated, whether 24, 25 or 30.

If you plan to post on vertical-video apps, choose a 9:16 shape (1080 x 1920) at the start, and plan your storyboard in that shape. Cropping a wide film into a tall one later cuts off your story.

Before the final export, render a short 2-second test and check it plays with sound. Keep a **master** copy as well, either your project file or a high-quality export, because every compressed copy loses a little quality. Tool menus differ, so check your software's manual for the export options."""),
            ("Your finishing checklist", """Use this list for every clip before you call it finished:

1. **Story:** can a stranger understand it without you explaining?
2. **Timing:** play it on repeat once. Do any movements feel too fast or too slow?
3. **Loops and sliding:** do walk cycles loop cleanly, and do the feet stay planted?
4. **Camera:** does every pan or zoom have a reason, with eased starts and stops?
5. **Sound:** are the effects on the right frames, and is the music below the voices?
6. **Cards:** add a title card at the start and an end card with your name and any credits.
7. **Phone test:** watch it on a real phone, at arm's length, not only on your computer.
8. **Files:** name your files clearly and keep **two copies** of the project in different places, for example a phone and a computer or a flash drive.

Then show it to two people, say nothing, and watch their faces. Where they laugh or look confused tells you exactly what to fix next time."""),
        ],
        diagram=flow([("LAYERS", "Stack the|scene in parts"), ("CAMERA", "Pan and zoom|with easing"), ("SOUND", "Effects and|music levels"), ("EXPORT", "MP4 (H.264)|two sizes"), ("CHECK", "Watch it on|a real phone")], "d5", "Finish in this order, then keep a master copy"),
        caption="Finishing happens in five steps: layers, camera, sound, export and a real-phone check.",
        terms=[("Layer", "A transparent sheet in your project that holds part of the scene."), ("Parallax", "Layers moving at different speeds so a flat scene feels deep."),
               ("Pan", "Sliding the camera view across the scene."), ("Zoom", "Moving the view closer to, or further from, the action."),
               ("Safe margin", "An edge area where you keep important details so they are not cropped."), ("MP4 (H.264)", "A video format that almost every device can play."),
               ("Master copy", "Your highest-quality version, kept so you can export again later.")],
        mistakes=["Putting the whole picture on one layer, so every change means redrawing the background.", "Starting and stopping a camera move instantly instead of easing it.",
                  "Making the music louder than the voices or effects, or letting the sound clip into the red.", "Exporting only one huge file and never testing it on a real phone."],
        quiz=[dict(q="What is parallax?", o=["A video format", "A kind of sound effect", "Layers moving at different speeds to create depth", "A frame rate"], a=2, why="When far layers move slowly and near layers move faster, a flat scene feels like real space."),
              dict(q="Where should the sound of a footstep be placed in a walk cycle?", o=["On the contact frame", "Only at the very end", "Anywhere, it does not matter", "Before the clip starts"], a=0, why="The footstep happens when the foot hits the ground, which is the contact pose."),
              dict(q="Why keep faces away from the very edges of the frame?", o=["It saves file size", "It improves the frame rate", "It makes the music louder", "Phones and apps crop or cover the edges"], a=3, why="A safe margin keeps important details visible when a screen or app covers or crops the edges."),
              dict(q="Which is the best export plan for one clip?", o=["One huge file for everything", "A smaller MP4 for sharing and a larger one for YouTube, plus a master copy", "A GIF only", "Only the project file"], a=1, why="Two MP4 versions suit sharing and publishing, and a master copy lets you export again later.")],
    ),
}
