"""Animation Masterclass: deep lesson pages 1 to 8.
Same format as lessons_prompt_engineering.py: hook, sections, diagram, terms, mistakes, quiz. Quiz "a" = index of the right option."""
from diagrams import flow, compare, timeline, bars, spacing, keyframes, shots

LESSONS = {
    1: dict(
        minutes=13,
        hook="Take the last pages of an old exercise book. Draw a stick figure in the corner of each page, with the arm a little higher every time. Now flick the pages with your thumb. The figure waves. Nothing on any single page moves, yet your eyes see motion. That flip book is the secret behind every animation, from a WhatsApp sticker to a cinema film. In this lesson you learn why it works and the five ideas that make movement feel alive instead of stiff.",
        sections=[
            ("Why still pictures seem to move", """When your eyes see a series of slightly different pictures quickly one after another, your brain joins them into movement. Scientists call this **apparent motion**. You do not need special software to benefit from it. You need a clear idea of three things:

- **Frame:** one single picture in the sequence.
- **Frame rate:** how many frames are shown each second, written as **fps**. Cinema uses 24 fps. Television and online video often use 25 or 30. Games and smooth screen animation often use 60.
- **Duration:** how long the clip runs. A 2-second clip at 24 fps needs 48 frames.

Animators save work by drawing **on twos**: one drawing is held for two frames, so 24 fps needs only 12 drawings per second. Fast, sharp action is drawn **on ones**, a new drawing for every frame."""),
            ("Keyframes and in-betweens", """Nobody draws a clip from the first frame to the last in order. Animators work in two passes:

1. **Keyframes** are the important poses: where the action starts, its highest or lowest point, and where it ends.
2. **In-betweens** are the frames that connect one key pose to the next.

In a bouncing ball, the keys are the ball at the top, the ball touching the ground, and the ball at the top again. Everything else is an in-between. In most software, you set the keys and the computer draws some of the in-betweens for you. In hand-drawn work, you or an assistant draw them. Either way, the keys decide whether the action reads well, so you always do those first and check them before you fill the gaps."""),
            ("Five ideas that make movement look alive", """These come from the twelve principles of animation, written down by Disney animators Frank Thomas and Ollie Johnston. Start with five:

- **Squash and stretch:** a soft object flattens when it hits something and stretches when it moves fast. Keep its total volume the same, or it looks like it is growing and shrinking.
- **Anticipation:** a small movement in the opposite direction before the real action. A person bends their knees before they jump.
- **Timing:** how many frames an action takes. Fewer frames feels fast and light. More frames feels slow and heavy.
- **Spacing:** how far the object moves between frames. Close spacing feels slow, wide spacing feels fast.
- **Ease in and ease out:** things speed up gradually and slow down gradually, instead of moving at one steady speed. Real objects never start or stop instantly."""),
            ("Worked example: planning a bouncing ball", """Plan a one-second bounce at 24 fps before you draw anything. Write it as a chart:

> [Plan]
> Frame 1: ball at the top (KEY), slow, spacing very close
> Frame 6: ball falling, spacing getting wider
> Frame 12: ball touches the ground, squashed flat (KEY)
> Frame 13: ball stretches as it leaves the ground
> Frame 18: ball rising, spacing getting closer
> Frame 24: ball at the top again (KEY)

The ball is slowest at the top, where the frames bunch together, and fastest just above the ground, where they spread out. That is **ease in** on the way down and **ease out** on the way up. Look at the picture above: both columns cover the same distance, but only the right one feels like gravity."""),
            ("Free tools to start today", """You can begin with a pencil, paper and a phone camera: photograph each page and play the photos quickly. On a computer, several tools are free:

- **Krita** and **Pencil2D** for hand-drawn 2D animation.
- **Blender** for 3D, and it also has a 2D drawing mode.
- **OpenToonz** for traditional 2D production.

Tool features and versions change, so check each tool's own website for the current download. The skill you build here, judging timing and spacing, works in every one of them."""),
        ],
        diagram=spacing(), caption="Same ball, same distance. Only the spacing changed, and one of them looks like real gravity.",
        terms=[("Frame", "One single picture in an animation."), ("Frame rate (fps)", "How many frames play each second."), ("Keyframe", "An important pose that defines the action."),
               ("In-between", "A frame that connects one key pose to the next."), ("Timing", "How many frames an action takes."), ("Spacing", "How far an object moves from one frame to the next."),
               ("Easing", "Gradual speeding up and slowing down, instead of one constant speed.")],
        mistakes=["Spacing every frame evenly, so the movement looks robotic.", "Skipping anticipation, so actions look sudden and unreadable.", "Letting the ball grow or shrink while squashing instead of keeping its volume.",
                  "Drawing finished, clean frames first instead of rough keys that you can fix quickly."],
        quiz=[dict(q="What is a frame?", o=["The speed of the animation", "A single picture in the sequence", "The length of the clip", "A drawing program"], a=1, why="A frame is one still picture. Playing many frames quickly creates the feeling of movement."),
              dict(q="At 24 frames per second, how many frames does a 2-second clip need?", o=["24", "12", "72", "48"], a=3, why="24 frames per second times 2 seconds is 48 frames."),
              dict(q="A falling ball is drawn with gaps that get wider each frame. What does this show?", o=["It speeds up as it falls, like gravity", "It is slowing down", "It is moving at a steady speed", "It is about to stop"], a=0, why="Wider spacing means faster movement. Growing gaps look like acceleration."),
              dict(q="Which idea warns the audience that a big action is about to happen?", o=["Squash and stretch", "Anticipation", "Frame rate", "In-betweening"], a=1, why="Anticipation is a small opposite movement before the action, such as bending the knees before a jump.")],
    ),
    2: dict(
        minutes=14,
        hook="Nobody builds a house by stacking blocks and hoping for a roof. First there is a plan, then a drawing, then the foundation. Animation is the same, and it is even more expensive to change your mind late: one second of finished animation can take hours. That is why professionals spend a big share of the project planning on paper before they animate a single frame. This lesson shows you how to plan a short film so the animating itself is calm and fast.",
        sections=[
            ("Start with one sentence: the logline", """A **logline** is the whole story in one or two sentences. A simple formula works well:

> [Formula]
> When (something happens), (a character) must (do something) before (what is at stake).

Here is one for a 30-second film: “When Ngozi's goat escapes from the market, she must catch it before the rain washes her stall away.” You can already see a character, a problem, a goal and a clock. If you cannot say your idea in one sentence, it is probably too big for a short film. Cut it down until you can."""),
            ("From logline to script", """A short film has the same three parts as a long one:

- **Beginning:** meet the character and what they want.
- **Middle:** the problem gets harder, and the character tries something.
- **End:** it works, or it fails, and something has changed.

For a 30-second film, give each part about ten seconds. Write the script as short lines of action and sound, one action per line: “Ngozi sweeps her stall. A goat runs past. Ngozi drops the broom.” Do not describe things the camera cannot show, such as what a character is thinking. If a feeling matters, find an action that shows it."""),
            ("Design your character", """A **character design sheet** is the reference every drawing follows. A good one includes:

- **Silhouette:** fill the character in black. You should still recognise who it is. Strong silhouettes read quickly on a small phone screen.
- **Shape language:** circles feel friendly, squares feel stable, triangles feel sharp or dangerous.
- **Turnaround:** the character drawn from the front, side and back at the same size.
- **Expressions:** at least happy, angry, scared and surprised.
- **Colour palette:** three to five colours, with the exact codes written down.

Keep the design simple. Every extra stripe or button is something you must redraw hundreds of times."""),
            ("Storyboard and animatic", """A **storyboard** is your film as a comic strip. Each panel is one shot, with a short note about the action, the camera and the sound. Stick figures are fine. What matters is the order of shots and how they connect.

An **animatic** is the next step: you put the storyboard panels on a timeline, add rough sound, and give each panel the time it will have in the finished film. Then you play it. If a joke takes too long, or a moment is confusing, you find out now.

Here is why this matters:

- Changing a storyboard panel takes minutes.
- Changing an animatic timing takes seconds.
- Changing finished animation takes hours or days.

Always fix problems on the left side of the pipeline, where they are cheap."""),
        ],
        diagram=flow([("IDEA", "One sentence"), ("SCRIPT", "Short lines|of action"), ("STORYBOARD", "A comic strip|of shots"), ("ANIMATIC", "Panels with|timing"), ("ANIMATE", "The expensive|part")], "a2", "Fix problems on the left, where changes are cheap"),
        caption="Every step to the right costs more time. Test your idea early.",
        terms=[("Logline", "The whole story in one or two sentences."), ("Character design sheet", "A reference page that keeps a character looking the same in every drawing."), ("Silhouette", "The solid outline of a character, used to test whether the design is clear."),
               ("Turnaround", "A character drawn from several angles at the same size."), ("Storyboard", "A film planned as a sequence of drawn panels."), ("Animatic", "A storyboard put on a timeline with timing and rough sound.")],
        mistakes=["Starting to animate before the storyboard and animatic are tested.", "Writing a story that is too big for the running time.", "Designing a character with so much detail that it cannot be redrawn consistently.",
                  "Describing thoughts in the script instead of actions the camera can show."],
        quiz=[dict(q="What is a logline?", o=["The first line of dialogue", "A line drawn in the storyboard", "A timeline marker", "The whole story in one or two sentences"], a=3, why="A logline sums up character, problem and stakes so you can test whether the idea fits a short film."),
              dict(q="Why fill a character in solid black during design?", o=["To check that the silhouette is clear and recognisable", "To save printer ink when printing the sheet", "To choose the final colours for the character", "To start the animation on the first frame"], a=0, why="If you can still tell who it is from the outline alone, the design reads quickly on screen."),
              dict(q="What does an animatic add to a storyboard?", o=["Finished colour on every frame", "Final sound mixing for the film", "Timing on a timeline with rough sound", "A brand new script for the story"], a=2, why="An animatic lets you play the film and test its timing before you spend time animating."),
              dict(q="Where is it cheapest to fix a story problem?", o=["After the final render", "In the storyboard or animatic", "During the screening", "After the sound mix"], a=1, why="Changes cost more the later they happen. Panels and timings are quick to change.")],
    ),
    3: dict(
        minutes=14,
        hook="Watch someone walk past your gate. Their body goes up and down, their arms swing the opposite way to their legs, and their head hardly moves. You have seen walking all your life, so you know instantly when it looks wrong. That is the challenge and the fun of 2D animation: everybody is a critic. In this lesson you will learn the working method animators use to make a clean, believable clip, and you will build a walk cycle, the classic first test of every animator.",
        sections=[
            ("Pose first, then fill the gaps", """Good 2D animation follows a fixed order, which keeps you in control:

1. **Rough keys:** draw only the main poses, with loose lines. Check that the action reads when you flick between them.
2. **Breakdowns:** add the poses halfway between keys that decide the path of the movement, for example the arc of an arm.
3. **In-betweens:** fill the remaining frames.
4. **Clean-up and colour:** redraw the lines neatly and add colour, last of all.

Beginners often start at step 4 and run out of energy. Professionals protect their effort: rough first, polish only what survived testing."""),
            ("The walk cycle", """A **walk cycle** is a short loop of a character walking in place. When it repeats, the character appears to walk forever. It has four main poses for each step:

- **Contact:** the front heel touches the ground and the legs are furthest apart.
- **Down (recoil):** the body sinks as the weight lands on the front leg. This is the lowest point.
- **Passing:** the back leg swings past the standing leg. The body is rising.
- **Up:** the body is at its highest, pushing off the front toes.

Draw these four for one leg, then repeat them mirrored for the other leg. A relaxed step takes about 12 to 14 frames at 24 fps, so a full cycle of two steps is roughly 24 to 28 frames. Fewer frames makes the character hurry. More frames makes it stroll."""),
            ("Layers and basic rigging", """Software lets you stack drawings on **layers**, like sheets of clear plastic. Put the background on its own layer so you never redraw it. Split the character into body, head, front arm, back arm and legs when the action allows it.

That brings us to **cut-out animation** and **rigging**. Instead of redrawing the character every frame, you draw each body part once, then connect the parts with joints, a skeleton called a **rig**. To move the character you rotate the arm at the shoulder and the forearm at the elbow. This is much faster for walks, talking and repeated actions. The trade-off is that it looks more mechanical, and it takes time to set up. Hand-drawn frames still give more freedom for expressive, stretchy movement.

A good rule: use hand-drawn frames for the moments that carry emotion, and a rig for repeated or background actions."""),
            ("Check your work like a professional", """Before you call a clip finished, run through this list:

- **Flick test:** play the clip slowly and fast. Does it stay readable?
- **Arcs:** do hands, heads and feet move along smooth curved paths instead of straight lines?
- **Overlap:** do loose parts such as hair, a scarf or a skirt follow the body a moment later?
- **Silhouette:** is each key pose clear if filled with black?
- **Loop:** does the last frame flow smoothly into the first?

Ask one other person to watch it without telling them what it is. If they say “someone walking”, you have succeeded."""),
        ],
        diagram=keyframes(), caption="Draw the keys first. Then in-betweens fill the gaps and set the timing.",
        terms=[("Keyframe", "A main pose that defines the action."), ("Breakdown", "A pose between two keys that shapes the path of the movement."), ("Walk cycle", "A short looping animation of a character walking in place."),
               ("Layer", "A transparent sheet in the software that holds part of the drawing."), ("Rig", "A skeleton of joints that lets you move drawn body parts without redrawing them."),
               ("Overlap", "When loose parts follow the main movement a moment later.")],
        mistakes=["Polishing line work before the poses are tested.", "Making hands and feet move in straight lines instead of arcs.", "Letting the last frame jump when the cycle loops.", "Using a rig for a moment that needs expressive, stretchy movement."],
        quiz=[dict(q="Which should you do first?", o=["Colour every frame", "Clean up the line work", "Draw rough keyframes and test them", "Add the sound effects"], a=2, why="Rough keys let you check the action cheaply before spending time on polish."),
              dict(q="At which pose is the body at its lowest point in a walk cycle?", o=["Down (the recoil pose)", "Passing (the back leg swings through)", "Up (the highest pose)", "Contact (the heel touches down)"], a=0, why="After contact, the weight lands and the body sinks. This lowest pose is called the down or recoil pose."),
              dict(q="What does a rig let you do?", o=["Skip the storyboard and the animatic", "Move drawn parts through joints without redrawing", "Export a video in several sizes", "Record the voice and sound effects"], a=1, why="A rig connects body parts with joints, so you rotate parts instead of redrawing the whole character."),
              dict(q="What does the loop check ask?", o=["Is the clip the right length for WhatsApp?", "Are there enough colours?", "Is the file small?", "Does the last frame flow smoothly into the first?"], a=3, why="A cycle repeats. If the last frame does not match the first, you see a jump every time it loops.")],
    ),
    4: dict(
        minutes=14,
        hook="Think of a puppet. Someone carves it, someone adds strings or joints, someone dresses it, and then a puppeteer makes it perform under stage lights. 3D animation follows exactly that order. The difference is that the puppet lives inside the computer and a camera films it. Once you see the pipeline as a production line, 3D stops being mysterious: each stage has one job and hands its result to the next.",
        sections=[
            ("The 3D pipeline in order", """Almost every 3D film, game cutscene and advert follows these stages:

1. **Modeling:** build the shape of the character or object from points, edges and faces called a **mesh**.
2. **Rigging:** add a skeleton of bones, called an **armature**, and controls to move them.
3. **Skinning:** attach the mesh to the bones so the skin follows. The strength of each bone's pull is set with **weights**.
4. **Animation:** pose the rig on keyframes over time.
5. **Lighting and rendering:** place lights and a camera, then the computer turns the 3D scene into finished images.

Each stage depends on the one before. A badly modeled mesh bends strangely however good the rig is, so patience in the early stages saves effort later."""),
            ("Posing and the graph editor", """3D animation uses the same keyframe thinking as 2D. You pose the character at a key time, move forward, pose again, and the computer works out the in-betweens.

The big difference is the **graph editor**. It shows each movement as a curve over time. A straight line means constant speed, which looks robotic. A curve that flattens at both ends means ease in and ease out. To fix movement that feels wrong, you reshape the curve instead of adding more keys.

Two ways to pose a limb:

- **Forward kinematics (FK):** you rotate each joint in turn, shoulder, then elbow, then wrist. Good for swinging arcs.
- **Inverse kinematics (IK):** you move the hand or foot, and the rest of the limb follows. Good for feet that must stay planted on the ground."""),
            ("Lighting: the three-point setup", """Lighting decides mood. The classic starting setup uses three lights:

- **Key light:** the main, brightest light, placed to one side and slightly above the subject.
- **Fill light:** a softer light from the other side, to lift the shadows.
- **Rim (back) light:** a light from behind that outlines the subject and separates it from the background.

Then change the colour and strength to change the story. Warm and soft feels friendly. Cold and hard from below feels threatening."""),
            ("Rendering: real-time or offline", """**Rendering** turns the scene into pictures. There are two broad approaches:

- **Real-time rendering** draws the scene many times per second, as in games. It is fast but trades some realism for speed.
- **Offline rendering** takes seconds or minutes for every frame, and it can handle realistic light, reflections and soft shadows.

Blender, a free 3D program, includes both kinds: a fast real-time engine called Eevee and a physically based offline engine called Cycles. For your first projects, a fast render lets you try more ideas. Remember that render time multiplies: a 10-second clip at 24 fps is 240 frames, so a frame that takes one minute needs four hours."""),
        ],
        diagram=flow([("MODEL", "Build the|mesh"), ("RIG", "Add the|skeleton"), ("SKIN", "Attach mesh|to bones"), ("ANIMATE", "Pose over|time"), ("RENDER", "Light and|make images")], "a4", "Each stage hands its work to the next"),
        caption="3D is a production line. Fix problems in the earliest stage where they appear.",
        terms=[("Mesh", "The 3D shape, made of points, edges and faces."), ("Armature", "The skeleton of bones used to move a character."), ("Skinning", "Attaching the mesh to the armature so it bends with the bones."),
               ("Graph editor", "A view that shows movement as curves over time."), ("Inverse kinematics", "A way of posing where moving the hand or foot moves the rest of the limb."), ("Render", "The process of turning a 3D scene into finished images.")],
        mistakes=["Starting animation before the rig and skin weights are tested.", "Leaving movement on straight curves, so it looks robotic.", "Using only one harsh light, so the shapes look flat.", "Choosing a very slow render setting for a first test and losing a whole day."],
        quiz=[dict(q="What is a mesh?", o=["A kind of light", "A skeleton for the character", "A render setting", "The 3D shape made of points, edges and faces"], a=3, why="The mesh is the surface shape of the model."),
              dict(q="Which pipeline order is correct?", o=["Model, rig, skin, animate, render", "Render, animate, rig, model, skin", "Animate, model, skin, rig, render", "Rig, render, model, animate, skin"], a=0, why="You must build a model first, then give it a skeleton, attach the skin, animate it and finally render."),
              dict(q="A straight curve in the graph editor usually means what?", o=["Perfect ease in and out", "Constant speed that looks robotic", "A broken rig", "A lighting error"], a=1, why="Straight means one speed all the way. Curves that flatten at the ends add natural easing."),
              dict(q="What does the rim light do in a three-point setup?", o=["Fills the shadows with soft light", "Lights the whole background evenly", "Outlines the subject against the background", "Adds colour to the final render"], a=2, why="A light from behind creates a bright edge that makes the subject stand out.")],
    ),
    5: dict(
        minutes=14,
        hook="Think about the last film that made you laugh, cry or jump. Now imagine it muted, with all the shots the same size. Most of the feeling would be gone. Filmmakers do not only choose what to show. They choose how close to stand, where to put the camera and what to let the audience hear. In animation you control every one of those choices from nothing, so learning them is how a plain animation becomes a film.",
        sections=[
            ("Shot types: how close?", """The distance of the camera tells the audience what to feel and what to notice:

- **Wide shot:** shows the whole place and the character small inside it. Use it to show where we are and how big or lonely the world is.
- **Medium shot:** shows the character from about the waist up. Use it for conversation and action.
- **Close-up:** fills the frame with a face or an object. Use it for emotion and for important details, like a key in a hand.

A simple rule is to start wide so the audience understands the place, move in as the story gets more personal, and use the close-up sparingly so it keeps its power."""),
            ("Camera moves and framing", """A moving camera also carries meaning. The most common moves:

- **Pan:** the camera turns left or right from a fixed position.
- **Tilt:** the camera turns up or down.
- **Dolly or track:** the camera itself travels forward, back or sideways.
- **Zoom:** the lens changes size, which looks different from physically moving closer.

For **composition**, use the **rule of thirds**: imagine the frame cut into a three-by-three grid and place important things on the lines or where they cross, not dead centre. Use **leading lines** such as a road or a fence to pull the eye toward the subject. Leave **look room** in front of a character who is looking sideways.

Finally, the **180-degree rule**: imagine a line between two characters who are talking. Keep the camera on one side of that line, or left and right will flip and confuse the audience."""),
            ("Sound has four layers", """Sound is half of the film. It comes in four layers:

- **Dialogue:** voices. Always the priority, and it must stay clear.
- **Music:** sets the mood and the pace.
- **Sound effects (SFX):** the specific sounds of actions, like a door or a splash.
- **Ambience:** the background sound of a place, like market noise or rain.

Animation has no sound at the start, so everything must be added. **Foley** is the craft of recreating everyday sounds by hand: shaking a bag of rice for rain, tapping a bowl for footsteps. It is cheap, fun and sounds more natural than many library clips. For music and library sounds, use only tracks you have the right to use, and keep a note of the licence and the credit required."""),
            ("Mixing: who gets to be loud?", """**Mixing** means setting the level of every sound so that the audience hears what matters. A simple order of priority:

1. Dialogue is the loudest and clearest.
2. Sound effects support the action without covering speech.
3. Music sits under the dialogue and swells when nobody speaks.
4. Ambience stays quiet and steady in the background.

Always listen on two systems, for example good headphones and a phone speaker, because many viewers will watch on a phone. **Silence** is also a tool: dropping all sound for a moment before an impact makes the impact stronger."""),
        ],
        diagram=shots(), caption="The same person, three distances, three different messages.",
        terms=[("Wide shot", "A shot showing the whole scene with the character small inside it."), ("Close-up", "A shot that fills the frame with a face or an object."), ("Rule of thirds", "Placing key things on the lines of a three-by-three grid."),
               ("180-degree rule", "Keeping the camera on one side of an imaginary line between characters."), ("Foley", "Making everyday sounds by hand to match the action."), ("Mixing", "Balancing the level of every sound so the important ones are heard.")],
        mistakes=["Using only medium shots, so every scene feels the same.", "Crossing the 180-degree line without a reason, so left and right flip.", "Letting music cover the dialogue.", "Using music or sounds without checking that you have the right to use them."],
        quiz=[dict(q="Which shot is best for showing how a character feels?", o=["A close-up", "A wide shot", "A tilt", "A pan"], a=0, why="A close-up fills the frame with the face, so the audience reads emotion."),
              dict(q="What does the 180-degree rule protect?", o=["The sound mix levels", "The frame rate of the film", "Left and right between characters", "The colour palette of the film"], a=2, why="Staying on one side of the line keeps each character on the same side of the screen."),
              dict(q="In a mix, which sound should be clearest?", o=["Ambience", "Music", "Sound effects", "Dialogue"], a=3, why="If the audience cannot hear what people say, the story is lost."),
              dict(q="What is Foley?", o=["A camera move that follows a character", "Making everyday sounds by hand to match the action", "A kind of lens for close-ups", "A music licence for films"], a=1, why="Foley artists recreate footsteps, rustles and other sounds with simple objects.")],
    ),
    6: dict(
        minutes=14,
        hook="A tailor who buys ready-made buttons does not become a worse tailor. The shirt is still his, because he decided which buttons, where to sew them and whether the shirt is good enough to sell. AI tools can be the ready-made buttons of animation. They can draft, suggest and speed up the boring parts. But you are still the director who decides what stays. This lesson shows where AI helps, where it does not, and how to use it honestly.",
        sections=[
            ("Where AI can help you", """AI tools are useful at the **start** of a task and on **repetitive** parts. Here are the common uses:

- **Ideas and scripts:** brainstorm loglines, alternative endings, or character names, then choose and rewrite.
- **Reference and mood boards:** quickly explore colour palettes, locations and lighting ideas.
- **Backgrounds and textures:** draft scenery or surfaces that you then paint over and adjust.
- **In-betweens and clean-up:** some tools suggest frames between your keys or smooth rough lines.
- **Voice and sound:** temporary voice tracks for the animatic, noise removal, and subtitles.

Notice the pattern: AI produces a first draft, and you shape it."""),
            ("Where you must stay in charge", """AI is weak where animation needs **intention**:

- **Performance:** the small choices of timing that make a character feel alive. A tool can give you movement, but you decide what the character feels.
- **Consistency:** the same character must look the same in every shot. AI images often drift in face, clothes or proportions from one image to the next.
- **Details and errors:** extra fingers, melted text, objects that change between frames. You must check every frame.
- **Taste:** a tool will give you something average. Your style comes from your decisions.

A useful rule is to use AI for the first 20 percent and the boring parts, and keep the performance and the final look in your own hands."""),
            ("A prompt for a background", """Prompt skills from the prompt engineering course carry over directly. Say the setting, shot, style, mood, space for characters and what to leave out:

> A quiet Lagos street at dusk, wide shot, flat 2D cartoon style, warm orange light, empty space in the centre for characters, no people, no text, no logos.

Generate several options, pick one, then paint over it so it matches your character design. If every background comes from a different prompt style, the film will look like it was made by five different people. Write down your best prompt and reuse it."""),
            ("Rights, honesty and safety", """Before you use any AI output in a film you share or sell, check four things:

1. **The tool's terms:** do they allow commercial use of the results?
2. **Copyright and style:** do not ask a tool to copy a living artist's style or a famous character. You may not own the result, and it is unfair to the artist.
3. **Voices and faces:** never copy a real person's voice or face without their permission.
4. **Honesty:** tell clients, teachers and audiences when AI was used. Many competitions and employers ask.

Keep a **use log**: the tool, the date, what you asked for, and what you changed by hand. It protects you and shows your own contribution."""),
        ],
        diagram=compare(("AI can draft", ["Ideas and loglines", "Mood boards and references", "Rough backgrounds", "Temporary voice tracks", "Noise removal"]), ("You decide", ["Performance and timing", "Character consistency", "Checking every frame", "Rights and permissions", "The final look"]), vs="+", colors=("#00F0FF", "#FFB86B")),
        caption="AI speeds up the drafts. Your judgement makes it a film.",
        terms=[("AI-assisted", "Work where AI helps with some steps and a person makes the decisions."), ("Reference", "A picture or example used for guidance, not copied."), ("Consistency", "Keeping a character, colours and style the same across shots."),
               ("Commercial use", "Using a result to make money, which some tools restrict."), ("Use log", "A record of the tools you used, what you asked and what you changed.")],
        mistakes=["Using raw AI output without checking every frame for errors.", "Mixing many different AI looks in one film.", "Copying a living artist's style or a famous character.", "Hiding AI use from a client or teacher who asked about it."],
        quiz=[dict(q="Where is AI most useful in animation?", o=["Drafts, references and repetitive tasks", "Deciding what a scene should feel like", "Final performance timing", "Replacing the director"], a=0, why="AI is strongest at first drafts and boring tasks. People keep control of intention and taste."),
              dict(q="What is a common weakness of AI-made images across a film?", o=["They are always far too small to use", "They never have any colour", "Characters may drift from image to image", "They cannot show backgrounds"], a=2, why="Consistency is hard. You have to check and fix drift by hand."),
              dict(q="You want to copy the voice of a famous singer for your character. What should you do?", o=["Do it, nobody will notice the difference", "Do not copy a real person's voice without permission", "Do it but lower the volume a little", "Use it only in the trailer of the film"], a=1, why="Copying a real voice without permission is unfair and can break the law and tool terms."),
              dict(q="What is a use log for?", o=["Rendering the film faster", "Making backgrounds for scenes", "Recording the tools you used and your edits", "Choosing a frame rate for export"], a=2, why="A log protects you and proves your own contribution.")],
    ),
    7: dict(
        minutes=13,
        hook="A great tailor with no sign above the shop and no sample in the window gets no customers. In animation, the clip is not enough. People need to find it, open it quickly and see your best work in under a minute. That is what a showreel and portfolio do. This lesson is about the unglamorous part of the craft that decides whether your work gets seen: planning your time, exporting correctly and presenting your best.",
        sections=[
            ("Plan backward from the deadline", """Animation always takes longer than you think. Plan **backward**: start at the delivery date and work toward today.

1. Decide the final date, and subtract a **buffer** of 15 to 20 percent for things that go wrong.
2. Split the remaining time into stages: pre-production, animation, sound, export.
3. Set **milestones**, checkpoints you can see and test: “animatic approved”, “all keys done”, “first full render”.

Check progress at every milestone. If you are behind, cut scope, for example fewer shots or simpler backgrounds, instead of working through the night. A finished smaller film beats an unfinished big one every time."""),
            ("Export: a master and copies", """**Exporting** turns your project into a video file. Do it in two levels:

- **Master:** your highest-quality version, kept safe. Export it from the original project at full size with the best quality your software offers.
- **Copies:** smaller files made from the master for sharing. A common choice is an MP4 video, with the H.264 format, at 1080p, which almost every phone, laptop and website plays.

WhatsApp and many social apps compress video heavily, so make a smaller copy yourself and check that the text and faces are still readable. Always **name files clearly**, for example `ngozi_goat_v3_1080p.mp4`, and keep the project files and assets together in one folder with a backup on a second device or in cloud storage."""),
            ("Build a showreel", """A **showreel** is a short video of your best work. The rules are strict:

- **30 to 60 seconds** is enough. Viewers decide in the first few seconds.
- **Best work first, second best last.** Never start with something weak.
- **Only your own work**, and say clearly what you did in each clip.
- **Title card** with your name and contact details at the start and the end.
- **Sound** that supports the clips, with clean cuts.

Cut anything you would hesitate to show to a professional. Five excellent seconds beat thirty average ones."""),
            ("A portfolio page that gets replies", """Your **portfolio** is the page that holds your reel and your projects. It can be a simple one-page website or a profile on a site for creative work. Include:

- Your name, a one-line description of what you do, and how to contact you.
- Your showreel at the top.
- **Three to five** projects, each with a short description, your role and the tools used.
- A **process** image or two, for example a storyboard next to the finished shot. It shows how you think.

Keep it updated, and make sure every link works from a phone. Many people will open it on one."""),
        ],
        diagram=timeline([("Plan", "Deadline and|buffer"), ("Animate", "Keys, then|in-betweens"), ("Sound", "Mix on two|speakers"), ("Export", "Master and|copies"), ("Reel", "30 to 60|seconds"), ("Portfolio", "Reel plus|3 to 5 projects")], note="Plan backward from the deadline"),
        caption="Finishing, presenting and sharing are part of the craft, not extras.",
        terms=[("Milestone", "A visible checkpoint in a project schedule."), ("Buffer", "Extra time added to a schedule for things that go wrong."), ("Master file", "The highest-quality export, kept safe as the source for copies."),
               ("H.264 / MP4", "A very common video format that plays on nearly every device."), ("Showreel", "A short video of your best work."), ("Portfolio", "A page or site that collects your best projects.")],
        mistakes=["Making a schedule with no buffer.", "Exporting only one tiny, low-quality file and losing the master.", "Putting weak work first in the showreel.", "Naming files “final”, “final2” and “final_REAL” instead of clear versions."],
        quiz=[dict(q="What does planning backward mean?", o=["Animating the last shot of the film first", "Starting at the deadline and working toward today", "Deleting your early drafts to save space", "Rendering the film in reverse order"], a=1, why="You fix the end date, subtract a buffer and fit the stages into the time left."),
              dict(q="Why keep a high-quality master export?", o=["Because it is the only file that plays on phones", "To make WhatsApp videos bigger", "It is the safe source for making any smaller copy later", "Because it is faster to upload"], a=2, why="Making copies from a master avoids losing quality twice."),
              dict(q="How long should a showreel usually be?", o=["10 minutes", "30 to 60 seconds", "2 hours", "3 seconds"], a=1, why="Viewers have little time. Short and strong wins."),
              dict(q="Which piece goes first in a showreel?", o=["Your weakest piece", "Your best piece", "A long credits list", "A blank screen"], a=1, why="The first seconds decide whether people keep watching, so lead with your strongest work.")],
    ),
    8: dict(
        minutes=15,
        hook="Every film you have ever loved was once a sentence on a page. The difference between an idea and a finished film is not talent, it is a method: a plan, milestones and the discipline to finish. This lesson is your capstone brief. It gives you the whole path from first sentence to a screening, with a schedule you can follow, a checklist you can tick and a rubric that shows what a strong film looks like.",
        sections=[
            ("The brief", """Make a **finished animated short film of 30 to 60 seconds**. It must have:

- One main character and a clear goal.
- A beginning, a middle and an end.
- At least **two different camera shots** or moves.
- Sound: music or effects at a balanced level, and dialogue if you use it.
- A title card and an end card with credits and the licences of any assets you did not make.

Use what you learned. Choose a story you can finish in the time available, not the biggest idea you have."""),
            ("A schedule that works", """Most shorts fail because the schedule is wrong, not because the idea is bad. A realistic split of your time:

- **About 30 percent** pre-production: logline, script, design, storyboard and animatic.
- **About 40 percent** animation: keys, in-betweens, backgrounds and effects.
- **About 15 percent** sound and polish.
- **About 15 percent** export, checks and screening.

Set milestones: animatic approved, all keys done, picture lock, sound lock, final export. **Picture lock** means you stop changing the images. **Sound lock** means you stop changing the sound. Locks protect you from endless tinkering, because after picture lock you only fix bugs."""),
            ("The final checklist", """Before the screening, go through every item:

1. The story is clear to someone who did not help you make it.
2. The character looks the same in every shot.
3. Every action has timing, spacing and anticipation you can defend.
4. Dialogue is clear and music never covers it.
5. There are no flashes, missing frames or flickers. Play the whole film with full attention.
6. The credits list every person, tool and licensed asset.
7. You have a master export and a small copy that plays on a phone.
8. The project folder is backed up in a second place."""),
            ("Screening and feedback", """A film is finished when other people have seen it. Screen it in class and then ask three questions of your audience:

- What did you think happened?
- Where were you confused, bored or surprised?
- What is the one thing you would change?

Do not defend your work while people are speaking. Write the answers down and look for patterns. If three people stumbled at the same moment, that moment is the problem. You will be marked on the rubric below. The best students improve their film once after feedback."""),
        ],
        diagram=bars([("Pre-production", 30), ("Animation", 40), ("Sound and polish", 15), ("Export and screening", 15)], note="Share of your project time (percent)", unit="%"),
        caption="Spend a third of your time planning. It makes the animating faster and calmer.",
        terms=[("Capstone", "A final project that brings together everything in a course."), ("Picture lock", "The point where you stop changing the images."), ("Sound lock", "The point where you stop changing the sound."),
               ("Rubric", "A scoring guide that shows what each level of quality looks like."), ("Credits", "The list of people, tools and licensed assets used in a film.")],
        mistakes=["Choosing a story that is too big to finish.", "Changing the pictures after picture lock, so sound no longer fits.", "Forgetting to credit tools and licensed assets.", "Defending the film instead of listening during feedback."],
        quiz=[dict(q="Roughly how much of the schedule should go to pre-production?", o=["About 30 percent", "None", "90 percent", "5 percent"], a=0, why="Planning before animating saves much more time than it costs."),
              dict(q="What does picture lock mean?", o=["Locking the computer", "Hiding the film", "Adding music", "You stop changing the images"], a=3, why="After picture lock you stop editing the pictures so that sound and final export can be finished."),
              dict(q="Three people stumble at the same moment in your film. What does this suggest?", o=["That moment probably needs fixing", "The audience is unkind", "Nothing, ignore it", "The film should be restarted"], a=0, why="Patterns in feedback point to real problems. One opinion is a clue, three are a signal."),
              dict(q="What belongs on the end card?", o=["Credits and licences for borrowed assets", "Only your name in large letters", "The storyboard panels for the film", "Nothing at all, the film just ends"], a=0, why="Honest credits and licence notes are part of professional work.")],
    ),
}