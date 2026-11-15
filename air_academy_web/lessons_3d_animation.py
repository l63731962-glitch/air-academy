"""3D Animation Mastery: deep lesson pages 1 to 5.
Taught with Blender (free and open source) using its default keymap. Shortcuts are limited to the ones that are stable.
Same format as lessons_animation.py. Quiz "a" = index of the right option."""
from diagrams import flow, compare, hub, grid, timeline

LESSONS = {
    1: dict(
        minutes=14,
        hook="A carpenter in Ikeja does not start with a finished wardrobe. He starts with a plain plank, cuts it, joins it and sands it until it becomes something useful. 3D modelling works the same way. You begin with a plain cube and push, pull and cut it into a chair, a car or a character. The strange part is that the cube lives inside a computer, so you must first learn how to look around it, how to move things in three directions, and how to find your object when you lose it. This lesson gives you that map, using Blender, a free tool that professionals also use.",
        sections=[
            ("Three axes and one scene", """Flat drawing has two directions: across and up. 3D adds a third: depth. Every point in a 3D scene is described by three numbers, written **(X, Y, Z)**. In Blender these axes are coloured, so you can tell them apart at a glance:

- **X** is red and runs left and right.
- **Y** is green and runs forward and back.
- **Z** is blue and points **up**.

A new Blender project holds three objects: a **cube** (2 metres on each side), a **camera** and a **light**. Blender measures in metres by default, so a cube that is 2 units wide is 2 metres wide. Keep real sizes in mind. A door is about 2 metres tall and a person about 1.7 metres, so building at believable sizes makes lighting and physics behave more naturally later. Download Blender from its official website, blender.org, and check the manual there when a menu or key differs on your version."""),
            ("Know your workspace", """The screen is divided into **areas**. Learn the five you will use every day:

- **3D Viewport** (centre): your stage, where you see and edit the scene.
- **Outliner** (top right): a list of every object, like a file manager for your scene. You can rename, hide or select objects here.
- **Properties** (bottom right): tabs for settings such as materials, modifiers, render and output.
- **Timeline** (bottom): frames and keyframes. You will use it from Lesson 4.
- **Toolbar and header**: tools on the left and menus plus the mode switch along the top of the viewport.

Press **N** with the mouse over the viewport to open the sidebar, which shows exact numbers for location, rotation and scale. Rename every object as you create it, for example "Stool_Seat" instead of "Cube.001". A scene with fifty objects named "Cube" becomes impossible to manage."""),
            ("Moving around the viewport", """Looking around is a skill you must practise, like driving a gear car. The standard controls are:

- **Orbit:** hold the **middle mouse button** and drag.
- **Pan:** hold **Shift** and the middle mouse button and drag.
- **Zoom:** scroll the mouse wheel.
- **Numpad shortcuts:** 1 is front view, 3 is right view, 7 is top view, 0 is the camera view, and 5 switches between perspective and orthographic.
- **Home** shows everything, and **Numpad period (.)** frames the selected object. Use these when you are lost.

**On a laptop with no middle button or numpad:** open Edit, then Preferences, then Input, and tick **Emulate 3 Button Mouse** (then Alt plus left-click drag orbits) and **Emulate Numpad** (the top-row number keys act as the numpad). You can also drag the small **navigation gizmo** in the top right corner of the viewport with your mouse or finger. Spend ten minutes just orbiting around the cube until it feels natural."""),
            ("Meshes, modes and the three transforms", """Most 3D objects are **meshes**, built from three parts: **vertices** (points), **edges** (lines joining two points) and **faces** (flat surfaces between edges). A cube has 8 vertices, 12 edges and 6 faces.

Blender works in **modes**. Press **Tab** to switch between them:

- **Object Mode** moves the whole object.
- **Edit Mode** changes the shape of the mesh itself. Press 1, 2 or 3 to select vertices, edges or faces.

Three keys do most of the work. **G** grabs (moves), **R** rotates and **S** scales. Follow the key with **X**, **Y** or **Z** to lock to one axis, then type a number and press **Enter** for an exact value. Example: **S, then Z, then 0.5, then Enter** squashes the object to half its height. Right-click or press **Esc** to cancel. If you make a mistake, **Ctrl+Z** undoes it. Add new objects with **Shift+A**, and press **X** to delete the selection."""),
            ("Your first model: a stool", """Build a simple stool to practise everything above. Take your time with each step.

1. Delete nothing yet. With the cube selected, press **S, Z, 0.2, Enter** to flatten it into a seat, then **S, 1.2, Enter** to widen it a little.
2. Press **Shift+A**, choose Mesh, then Cylinder to add a leg. Press **S, 0.2, Enter** to make it thin, then **S, Z, 3, Enter** to make it tall. Use **G, Z** to move it down under the seat.
3. Press **Shift+D** to duplicate the leg, then **G** to move the copy to another corner. Repeat until the stool has four legs.
4. Select the seat, press **Tab** for Edit Mode, press **3** for face select, click the top face, press **E** (extrude), type **0.1**, and press Enter to give the seat a thicker top edge.
5. Back in Object Mode, open the **Modifiers** tab (the wrench icon) and add a **Subdivision Surface** modifier. It smooths a blocky shape into a rounded one, without changing your original mesh.

Name every part, save with **Ctrl+S**, and save a new version each session. You have now modelled, scaled, duplicated, extruded and smoothed."""),
        ],
        diagram=grid([("3D VIEWPORT", "Your stage|N opens numbers"), ("OUTLINER", "List of|every object"), ("PROPERTIES", "Materials,|modifiers, render"), ("TIMELINE", "Frames and|keyframes"), ("TOOLBAR", "Tools along|the left side"), ("HEADER", "Menus and|the mode switch")], 3, "The six places you will keep returning to"),
        caption="The six areas of the Blender screen. Learn what each one does before you model anything.",
        terms=[("Axis", "One of the three directions in 3D space: X red, Y green and Z blue (up)."), ("Mesh", "A 3D shape built from vertices, edges and faces."),
               ("Vertex", "A single point of a mesh."), ("Face", "A flat surface bounded by edges."), ("Object Mode", "The mode for moving, rotating and scaling whole objects."),
               ("Edit Mode", "The mode for changing the shape of a mesh itself."), ("Modifier", "A non-destructive effect, such as Subdivision Surface, applied on top of a mesh.")],
        mistakes=["Leaving every object named Cube, Cube.001 and Cube.002, then losing track of the scene.", "Typing numbers while the mouse is over the wrong area, so the key does nothing or does something else.",
                  "Modelling at random sizes, so that lights and physics behave strangely later.", "Never saving versions, so one mistake or one power cut costs a whole session."],
        quiz=[dict(q="Which axis points up in Blender by default?", o=["X", "Y", "Z", "W"], a=2, why="Z is the blue axis and it points up. X is red and runs left and right, and Y is green and runs forward and back."),
              dict(q="You press Tab with a mesh selected. What happens?", o=["It switches between Object Mode and Edit Mode", "It deletes the mesh", "It starts a render", "It opens the camera view"], a=0, why="Tab toggles between Object Mode, for whole objects, and Edit Mode, for the mesh itself."),
              dict(q="Which input scales an object to half its height only?", o=["G, Z, 0.5, Enter", "R, Z, 0.5, Enter", "S, Z, 0.5, Enter", "E, Z, 0.5, Enter"], a=2, why="S scales, Z locks it to the up axis, and 0.5 is half. G moves, R rotates and E extrudes."),
              dict(q="Your laptop has no middle mouse button. What helps you orbit?", o=["Press Delete", "Use only the numpad", "Install a new keyboard", "Turn on Emulate 3 Button Mouse, then Alt plus left-click drag"], a=3, why="That preference makes Alt plus left-click act as the middle button. You can also drag the navigation gizmo.")],
    ),
    2: dict(
        minutes=15,
        hook="At a wedding in Surulere, the photographer asks everyone to stand near the window. He is not being bossy. He knows that the same face can look dull in a dark room and beautiful in soft window light. In 3D, you are both the photographer and the person who builds the room, so light is completely your job. A grey sphere with good lighting looks more professional than a detailed character in flat, bad light. This lesson teaches the three things that decide how a 3D shot looks: the surface (the material), the light and the camera.",
        sections=[
            ("Materials: how a surface reacts to light", """A **material** describes what a surface is made of, so the renderer knows how light behaves when it hits it. By default, you work with the **Principled BSDF** shader, which offers three settings that you will use constantly:

- **Base Color:** the colour of the surface.
- **Metallic:** 0 for non-metals such as skin, wood and plastic, and 1 for metals. Real surfaces are almost always near 0 or near 1.
- **Roughness:** 0 is a perfect mirror, and 1 is completely matte, like chalk. This setting does the most to make something look real.

Starting recipes:

> [Plastic toy] Base Color bright red, Metallic 0, Roughness 0.3
> [Brushed metal] Base Color light grey, Metallic 1, Roughness 0.35
> [Skin] Base Color warm brown, Metallic 0, Roughness 0.5
> [Rubber ball] Base Color any colour, Metallic 0, Roughness 0.8

To add one, select the object, open the Material tab in Properties, and click **New**. Set the viewport to **Material Preview** to see the result while you work."""),
            ("Light types and what they are for", """Blender gives you four kinds of light. Add them with Shift+A, then Light:

- **Point:** a bulb that shines in all directions. Good for lamps and candles.
- **Sun:** parallel rays from very far away, like real sunlight. Only its **rotation** matters, not where you place it.
- **Spot:** a cone of light, like a stage light or torch.
- **Area:** a glowing panel. It gives the soft light you see from a window or a softbox.

**Size changes softness.** A big area light, close to the subject, gives soft shadows. A small light, far away, gives hard, sharp shadows. If your character looks harsh and flat, make the light bigger and move it closer. Power is measured in watts for point, spot and area lights, and as a strength value for the sun. Because scene sizes differ, always judge by eye and adjust. Start low, as bright lights hide detail and burn out the colours."""),
            ("Three-point lighting", """Almost every film, photo and cartoon uses a simple setup called **three-point lighting**. You place three lights around the subject:

1. **Key light:** your main light. Place it about 45 degrees to one side of the camera and a little above the subject's eye level. It decides the overall look.
2. **Fill light:** a softer light from the opposite side. It lifts the dark shadows so you can still see detail. Make it about **a third to half as strong** as the key.
3. **Rim light (back light):** a light behind and above the subject, aimed at the edges. It draws a thin bright outline that separates the character from the background. Make it about half to three-quarters as strong as the key.

Try this example: key at 100%, fill at 35%, rim at 60%. Give the key a slightly warm colour and the fill a slightly cool one, and the picture gets depth immediately. To test, hide two lights, then turn them on one by one and watch how each one changes the face."""),
            ("The camera: framing and lens", """The camera is the audience's eyes. Press **Numpad 0** to look through it. To place it, go to the sidebar (N), open the **View** tab, and tick **Camera to View**. Then orbit around the viewport as usual and the camera follows. Untick it when you are done, or you may move the camera by accident.

**Focal length** (in the Camera properties) changes the look:

- **24 to 35 mm:** wide. Shows more of the room but stretches objects close to the edges.
- **50 mm:** a natural view, similar to human eyes and the starting setting.
- **85 mm and above:** telephoto. Flattens space and is flattering for faces.

**Framing tips:** place the subject on a third line, not dead centre, and leave a little space in the direction they are looking. A **low angle** makes a character feel powerful. A **high angle** makes them feel small. In Output properties, set the resolution to **1920 x 1080** now so your framing matches the final video, and enable **Safe Areas** in the camera's Viewport Display settings."""),
            ("Your first render", """Blender includes two main render engines:

- **Eevee:** fast, near real-time. It is ideal for learning, tests and stylised looks, and it works on modest laptops.
- **Cycles:** it simulates how light bounces, so results look more realistic, but it is slower. Use denoising and a lower sample count to speed it up.

Do this exercise with your stool from Lesson 1:

1. Add a large plane under the stool as the floor, and give it a light grey, rough material.
2. Give the stool a wood-coloured material (Base Color brown, Roughness 0.6).
3. Build the three-point setup with area lights.
4. Press **Numpad 0**, frame the stool on the third line, and press **F12** to render.
5. Save the image from the Image menu in the render window.

Your first render may look dull, which is normal. Change one thing at a time: first the light angle, then the strength, then the colour. If a render takes too long, lower the resolution percentage in Output properties for tests, then return to 100% for the final."""),
        ],
        diagram=hub(("SUBJECT", "Your model"), [("Key light", "Main and brightest"), ("Fill light", "Softens shadows"), ("Rim light", "Outlines edges"), ("Camera", "Frames the shot")], "Every shot is a subject, three lights and one camera"),
        caption="A good shot is the subject, three lights and one camera, arranged on purpose.",
        terms=[("Material", "A description of a surface that tells the renderer how light reacts to it."), ("Principled BSDF", "The all-round shader with Base Color, Metallic and Roughness settings."),
               ("Roughness", "How matte or shiny a surface is, from 0 (mirror) to 1 (matte)."), ("Key light", "The main, brightest light in a setup."),
               ("Rim light", "A light from behind that outlines the subject's edges."), ("Focal length", "The lens setting that decides how wide or narrow the view is, in millimetres."),
               ("Render engine", "The system that calculates the final image, such as Eevee or Cycles.")],
        mistakes=["Using a very small, harsh light on a face, so the shadows look cheap.", "Setting Metallic to 0.5 on everything, which does not match real materials.",
                  "Leaving Camera to View ticked and moving the camera by accident later.", "Judging a scene in the dark viewport instead of looking through the camera and rendering a test."],
        quiz=[dict(q="What does Roughness 1 look like?", o=["A perfect mirror", "Fully matte, like chalk", "Transparent glass", "A glowing surface"], a=1, why="Roughness 0 is mirror-like and Roughness 1 is completely matte."),
              dict(q="Which light gives soft, even light like a window?", o=["Sun", "Spot", "Area", "Point"], a=2, why="An area light is a glowing panel. The bigger and closer it is, the softer the shadows."),
              dict(q="In three-point lighting, which light is behind the subject to outline its edges?", o=["Key", "Fill", "Camera", "Rim"], a=3, why="The rim (back) light skims the edges and separates the subject from the background."),
              dict(q="Which focal length gives the widest view?", o=["85 mm", "50 mm", "24 mm", "200 mm"], a=2, why="A smaller focal length means a wider view. 24 mm is wide, and 85 mm and above are telephoto.")],
    ),
    3: dict(
        minutes=16,
        hook="A tailor's mannequin has a hidden skeleton that lets you bend its arms and legs into any pose. A puppet has strings. A 3D character needs the same thing, because moving thousands of points one by one is impossible. The answer is a **rig**: a skeleton of bones, hidden inside the model, that you can pose with a simple rotation. Rigging is the technical part of animation, and many beginners fear it. It is actually a small set of ideas, repeated. You will build a skeleton, attach the skin, fix the places where it bends badly, and learn when to use two different ways of controlling a limb.",
        sections=[
            ("What a rig is and why you need one", """A **rig** is a control system for a model. It is made of an **armature**, which is a set of **bones**. Each bone has a **parent**, and the chain of parents and children is called the **hierarchy**. Move the thigh and the shin, foot and toes follow, because they are its children. Move the **root** (often the hips) and the entire body moves.

A good rig follows a few rules:

- Start from the **rest pose**: a relaxed, neutral stance, usually arms out slightly, feet apart and facing forward. Bones are built in this pose, and every animation is measured against it.
- The model needs **clean topology**: extra loops of edges around the elbows, knees and shoulders, so they can bend without collapsing.
- Place bones **inside** the mesh, with their joints exactly where the real joints are.

Without a rig, you can only animate whole objects. With one, you can pose a character the way you would pose a wooden art mannequin."""),
            ("Building the armature", """Follow these steps:

1. Press **Shift+A**, choose Armature, then Single Bone.
2. In the Armature properties (Object Data tab), tick **In Front** under Viewport Display so the bone is visible through the mesh.
3. Press **Tab** to enter Edit Mode. Move the bone to the hips, then press **E** to extrude the next bone upward for the spine. Keep extruding for the chest, neck and head.
4. For the legs, extrude from the hip bone downward: thigh, shin, then foot. Rotate and place each joint in the middle of the real joint.
5. Turn on **X-Axis Mirror** in the Armature options, build only the left side, and then the right side is created for you.
6. **Name every bone.** Use the suffixes **.L** and **.R**, for example "thigh.L" and "thigh.R". The mirror and symmetry tools depend on them.

Rig only what you will animate. A simple character needs about 15 to 25 bones, so avoid adding fingers if your story never shows hands up close."""),
            ("Skinning: attaching the mesh to the bones", """To make the mesh follow the bones, you **parent** it with **automatic weights**:

1. In Object Mode, select the **mesh** first.
2. Hold **Shift** and select the **armature** last, so it is the active object.
3. Press **Ctrl+P** and choose **With Automatic Weights**.

Blender calculates how much each bone affects the nearby points of the mesh. Now select the armature, press **Ctrl+Tab** to enter **Pose Mode**, select a bone, and press **R** to rotate it. The mesh should bend with it.

Always test with extreme poses before you animate. Raise both arms, squat deeply, bend the knee all the way, and twist the spine. If an elbow pinches or a hip tears the mesh, the weights need fixing. Return to the rest pose when you finish by clearing the pose, so the bones do not stay twisted. If automatic weights fail completely, the usual cause is a mesh with gaps or overlapping parts, or bones placed outside the body."""),
            ("Weight painting: fixing the bends", """Each point in the mesh has a **weight** for each bone, from 0 to 1. A weight of 1 means the bone fully controls that point, and 0 means it has no effect. In **Weight Paint mode**, the weights are shown as colours:

- **Red:** full influence of the active bone.
- **Green and yellow:** partial influence.
- **Blue:** no influence.

To fix a problem, select the mesh, switch to **Weight Paint** mode, choose the bone from the **Vertex Groups** list (each group is named after a bone), and paint. The **Draw** brush adds weight. The **Smooth** brush (or Blur) smooths harsh changes. Typical trouble spots are shoulders, elbows, knees and hips.

A common recipe for a pinching elbow: select the forearm group, use Smooth over the crease, and lower the brush Strength to about 0.3 so you can build up gently. Make small changes and test the pose after each one, because heavy painting can damage areas that were already good."""),
            ("FK and IK: two ways to move a limb", """You can control a chain of bones in two ways, and a good animator uses both.

- **FK (Forward Kinematics):** you rotate each bone in order, from the top of the chain down, such as shoulder, then elbow, then wrist. It gives smooth, curved arcs and is good for arms, spines and tails.
- **IK (Inverse Kinematics):** you move the **end** of the chain, such as the foot or hand, and the rest of the chain works out the rotations by itself. A target keeps the foot in place, and a **pole target** decides which way the knee or elbow points.

For legs, IK is usually the better choice. If the body moves, the foot stays planted on the ground, which solves the foot-sliding problem from the 2D walk lesson. To add IK, enter Pose Mode, select the shin bone, open the **Bone Constraints** tab, click Add Bone Constraint, choose **Inverse Kinematics**, set its target, and set **Chain Length** to 2 (shin and thigh)."""),
        ],
        diagram=compare(("FK, from the top", ["Rotate bone by bone", "Smooth, curved arcs", "Great for arms and spine", "Foot can slide"]), ("IK, from the end", ["Move the foot or hand", "Chain follows by itself", "Great for planted feet", "Needs a pole target"]), vs="vs", note="Most rigs use IK for legs and FK for arms"),
        caption="FK rotates from the top of the chain down. IK moves the end and lets the chain follow.",
        terms=[("Armature", "The skeleton object that holds all the bones of a rig."), ("Bone", "One controllable part of a skeleton, with a parent and children."),
               ("Hierarchy", "The parent and child chain that makes children follow their parents."), ("Rest pose", "The neutral pose the rig is built in, before any animation."),
               ("Weight", "A value from 0 to 1 that says how much a bone controls a point of the mesh."), ("Pose Mode", "The mode for rotating and moving bones to pose the character."),
               ("IK", "Inverse Kinematics: moving the end of a chain and letting the rest follow.")],
        mistakes=["Building the rig with the character in an extreme pose instead of a neutral rest pose.", "Placing bone joints outside the body, so the mesh bends in the wrong place.",
                  "Skipping the .L and .R naming, then fighting with symmetry tools later.", "Testing only the rest pose, then finding broken elbows and shoulders after the animation is done."],
        quiz=[dict(q="Why do you parent a mesh to an armature with automatic weights?", o=["It adds colours to the mesh", "It makes each bone influence the nearby mesh, so the mesh bends with the bones", "It sets the frame rate", "It exports the file"], a=1, why="Automatic weights give each bone a starting influence over the points near it, so the mesh follows when you pose the bones."),
              dict(q="In Weight Paint mode, what does red mean?", o=["The bone is deleted", "The mesh is hidden", "No influence from the bone", "Full influence from the bone"], a=3, why="Red is a weight of 1, full influence. Blue is 0, no influence."),
              dict(q="Which method keeps a foot planted on the ground while the body moves?", o=["IK", "FK", "Subdivision", "Roughness"], a=0, why="With IK, the foot follows a target, so it stays where you put it while the body moves above it."),
              dict(q="Why name bones thigh.L and thigh.R?", o=["It makes the file smaller", "So mirror and symmetry tools can match left and right", "It makes rendering faster", "The camera needs it"], a=1, why="Blender's mirror features use the .L and .R suffixes to match the two sides.")],
    ),
    4: dict(
        minutes=15,
        hook="In a Nollywood scene, the actor hears the bad news, pauses for two long seconds, and only then turns around. That pause is the whole scene. 3D animation is also built from timing, and the computer lets you control it down to a single frame. The good news is that you do not pose every frame. You set a few key moments and the computer fills the gaps between them. The bad news is that the computer fills them in its own way, which is often floaty and lifeless until you take control. This lesson teaches you to set keys, read the timing, and then shape the movement with the Graph Editor.",
        sections=[
            ("Frames, frame rate and the Timeline", """Start by setting the project's rules, just like in 2D. Open **Output properties** and set the **Frame Rate** to 24. Then, at the **Timeline**, set the start frame to 1 and the end frame to match your clip. The sum is the same as before: **frames = fps x seconds**, so a 5-second clip at 24 fps ends at frame 120.

In the Timeline:

- The **current frame** is shown by a blue marker. Drag it to scrub through time.
- Press **Space** to play and press it again to stop.
- A **keyframe** appears as a small diamond. It marks a value stored for one frame, and Blender calculates the frames between two keys on its own.

Decide the frame rate and clip length before you start to animate. Changing the frame rate later changes the speed of everything you have done, exactly as in 2D."""),
            ("Setting keyframes", """To keyframe an object:

1. Go to the frame where the pose or position should be set.
2. Move, rotate or scale the object (or the bone, in Pose Mode).
3. Press **I** with the mouse over the viewport and choose what to key, such as Location, Rotation or Scale. The options in this menu differ slightly between Blender versions, so check the manual for yours.
4. Move to the next important frame, change the pose and key again.

Read the colours in the Properties fields. **Yellow** means there is a keyframe on this frame. **Green** means the value is animated but has no key on this frame. **Orange** means you changed it since the last key, so the change will be lost if you jump to another frame without keying. If you move an object and it snaps back, that is usually the reason.

There is also **Auto Keying**, the red record button in the Timeline, which inserts keys as you change things. It is quick, but easy to forget it is on, so beginners are safer using the I key."""),
            ("Pose to pose with the Dope Sheet", """In 3D, pose to pose is the standard method. You set the key poses first, and only then refine the timing. The **Dope Sheet** shows every keyframe as a diamond in a row for each property, and it is the best place to adjust **timing**.

- Select diamonds and press **G** to move them in time.
- Press **S** to stretch or compress the timing of a group of keys. Scaling by 1.5 makes the action 50% slower.
- Press **Shift+D** to duplicate keys, which is useful for repeated movements.

The most common fix of all: move a key a few frames and look again. An action that feels slow often needs two or three frames removed, and an action that feels rushed often needs one more frame at the start (anticipation) or the end (settle).

For **follow-through**, offset the keys of trailing parts, such as a tail or an antenna, by 2 to 4 frames behind the main body. It is quick in the Dope Sheet, because you simply select the tail's diamonds and press G."""),
            ("The Graph Editor: shaping the movement", """The Dope Sheet tells you **when** things happen. The **Graph Editor** shows you **how**. Each property gets a curve, an **F-curve**, with time going across and the value going up.

How to read a curve:

- A **steep** section means fast change.
- A **flat** section means little or no change, so slow or stopped.
- A **smooth** curve gives smooth movement, and a **sharp corner** gives a sudden change of direction.

Blender's default interpolation is **Bezier**, which eases in and out of every key. That feels floaty for some actions. Press **T** to choose another type: **Linear** for constant speed (good for a spinning wheel) and **Constant** for sudden stepped changes. Select a key and press **V** to choose the **handle type**, and drag the handles to reshape the curve. Press **Home** to frame all your curves in view.

If a movement looks wrong but the poses are right, the problem is nearly always in the curves."""),
            ("Worked example: a bouncing ball in 3D", """Create a ball with a radius of 0.5 m, resting on a floor at Z = 0. When its centre is at Z = 0.5, it touches the floor. We will drop it from a height 1.2 m above that, so the centre starts at Z = 1.7. Physics says a 1.2 m fall takes about 0.5 seconds, which is 12 frames at 24 fps.

1. **Frame 1:** set Z location to 1.7 and press I (Location).
2. **Frame 12:** set Z to 0.5 (contact) and key it. Also key the Scale: X and Y at 1.2, Z at 0.7, a squash that keeps the volume nearly constant (1.2 x 1.2 x 0.7 is about 1).
3. **Frame 24:** set Z back to 1.7 and Scale to 1, 1, 1, then key both.
4. Open the Graph Editor. By default, the curve is smooth at the bottom, so the ball seems to slow down just before it hits the ground, which is wrong.
5. Select the key at frame 12 on the Z curve, press **V** and choose **Vector**. The bottom of the curve becomes a sharp point, so the ball hits hard and bounces away.
6. Leave the keys at frame 1 and frame 24 smooth, so the ball slows gently at the top of the bounce.

Press Space and watch. One small change in the Graph Editor turned a floaty ball into a heavy one."""),
        ],
        diagram=timeline([("Set up", "24 fps and|end frame"), ("Key poses", "Press I on|important frames"), ("Timing", "Adjust in the|Dope Sheet"), ("Curves", "Shape in the|Graph Editor"), ("Play", "Space bar,|then refine")], note="Poses first, then timing, then curves"),
        caption="Set up the project, key the poses, adjust the timing, shape the curves, then play it again and again.",
        terms=[("Keyframe", "A stored value for a property at one frame."), ("Timeline", "The strip at the bottom of the screen that shows frames and keyframes."),
               ("Dope Sheet", "A view of all keyframes in rows, best for adjusting timing."), ("Graph Editor", "A view of the curves between keyframes, best for adjusting how the motion feels."),
               ("F-curve", "The curve that describes how one property changes over time."), ("Interpolation", "The way the computer fills in the values between two keyframes."),
               ("Handle", "A control on a key that shapes the curve entering and leaving it.")],
        mistakes=["Changing a value on a frame without pressing I, then losing it when the frame changes (an orange field).", "Leaving Auto Keying on and keying things by accident.",
                  "Accepting the default smooth curves for a hard impact, so heavy things look floaty.", "Fixing timing problems by adding more keys, instead of moving or scaling the keys already there."],
        quiz=[dict(q="A clip is 5 seconds at 24 fps and starts at frame 1. What is the last frame?", o=["60", "100", "120", "240"], a=2, why="Frames equal fps times seconds: 24 x 5 = 120, so a clip starting at frame 1 ends at frame 120."),
              dict(q="Which key inserts a keyframe in the viewport?", o=["I", "K", "Tab", "F12"], a=0, why="Press I over the viewport and choose what to key. The menu differs a little between versions."),
              dict(q="In the Graph Editor, what does a flat stretch of a curve mean?", o=["Very fast movement", "The value is barely changing, so slow or stopped", "A deleted key", "The maximum speed"], a=1, why="Steep means fast change. Flat means the value is almost constant."),
              dict(q="How do you get a sharp, heavy bounce at the ground contact key?", o=["Increase the frame rate", "Delete the top keys", "Make all the keys smoother", "Set the handle type to Vector on the contact key"], a=3, why="A Vector handle gives a sharp corner, so the ball hits the ground and leaves it instantly.")],
    ),
    5: dict(
        minutes=16,
        hook="You press Render Animation and go for dinner. Thirty minutes later NEPA takes the light, the laptop battery dies and you have nothing: no frames, no video, only a bad mood. Every 3D artist in Nigeria learns this lesson once. The fix is simple and it starts with how you render. This lesson finishes the track with two big jobs: building a walk cycle on your rigged character so it loops, and rendering the final clip in a way that survives power cuts, slow laptops and different phones. By the end, you will have a 5-second animated clip that you can send to anyone.",
        sections=[
            ("Building the walk cycle", """Use the same four poses from the 2D walk lesson: **Contact, Down, Passing and Up**. This time you key them on the rig in Pose Mode. A 24-frame cycle has a pose every three frames, as in the 2D plan, with the right foot forward at frame 1 and the left foot forward at frame 13.

A smart shortcut saves half of the work:

1. Pose the character at the **right contact** on frame 1 and key all the bones.
2. In Pose Mode, select all bones and press **Ctrl+C** to copy the pose.
3. Go to frame 13 and press **Ctrl+Shift+V**. This pastes the pose **flipped**, so the left foot is now forward. Key it.
4. Go to frame 25 and press **Ctrl+V** to paste the original pose, so the cycle ends where it began.
5. Build the down, passing and up poses for the right step, then copy them flipped for the left step.

Check the body: it should be lowest at the down pose and highest at the up pose. Use IK on the feet, so each planted foot stays still while the body passes over it."""),
            ("Making it loop", """For a clean loop, frame 25 must be identical to frame 1, so the cycle itself is **24 frames long**. Frame 25 is only there to complete the final movement. When you play or render the loop, use frames **1 to 24**, so that the repeated pose is not shown twice.

To make the animation repeat automatically, open the **Graph Editor**, select the channels, and choose **Channel, then Extrapolation Mode, then Make Cyclic**. This adds a Cycles modifier to the curves, so the walk continues forever after the last key. The result is that you only keep keys from frame 1 to frame 25, and the same cycle runs from frame 1 to frame 120.

Check the loop by setting the frame range to 1 to 24 and turning on **Loop** playback. Watch for a tiny hitch at the same place on each pass. If you see one, a bone's first and last key do not match. Compare the values on frame 1 and frame 25 channel by channel."""),
            ("Moving across the screen without sliding", """You can animate the walk **in place** and move the camera, or move the character's **root** bone forward along the path. If you move the root, the numbers must agree with the steps:

> Step length: 0.7 m
> Step time: 12 frames
> Root speed: 0.7 / 12 = about 0.058 m each frame
> Full cycle (2 steps): 1.4 m in 24 frames

Key the root at frame 1 and at frame 25 with a forward difference of 1.4 m, then select those keys in the Graph Editor and press **T** to choose **Linear** interpolation, so the speed is constant. Set the extrapolation to linear as well, so the character keeps moving at the same pace.

If the feet look like they skate on ice, the body is travelling too fast or too slow for the step. Change the distance by small amounts, such as 1.2 m or 1.6 m per cycle, until the planted foot sticks to the ground. A 5-second clip needs about 7 metres of floor: 5 cycles at 1.4 m each."""),
            ("Rendering that survives power cuts", """Open **Output properties** and set up the following:

- **Resolution:** 1920 x 1080 at 100%.
- **Frame rate:** 24, matching your animation.
- **Frame range:** start 1, end 120 for 5 seconds.
- **Render engine:** Eevee for speed or Cycles for realism, with denoising and fewer samples.

First, press **F12** to render one test frame and note the time. If one frame takes 15 seconds, then 120 frames take 15 x 120 = 1,800 seconds, which is **30 minutes**. Plan your day around that number. If it is too long, lower the samples, lower the resolution to 75%, or switch to Eevee.

Then set the **Output file format to PNG** and choose a folder, such as a "render" folder next to your project. Blender will save one image per frame, named like walk_0001.png. Turn **Overwrite off** and **Placeholders on**. If the power goes out, you keep every finished frame, and after the light returns, **Render Animation** (Ctrl+F12) continues from the first missing frame, instead of starting again."""),
            ("Making the final video and delivering it", """When all the PNG frames are done, turn them into one video. You can use Blender's **Video Editing** workspace: add the image strip, set the frame rate to 24, then go to Output properties, set **File Format to FFmpeg Video**, **Container to MPEG-4** and **Video Codec to H.264**. This is the format almost every phone and website plays. If you have a sound track, add it in the same workspace and set the audio codec to AAC.

Run this **delivery checklist** before you send anything:

1. Does it loop or end cleanly, with no repeated pose?
2. Do the feet stay planted, with no sliding?
3. Is the key light, fill and rim still doing their jobs in the final render?
4. Is the video 1920 x 1080 at 24 fps, as an MP4 file?
5. Did you watch it on a real phone?
6. Did you make a smaller 720p copy for WhatsApp?
7. Did you keep the **.blend file and the PNG frames** as your master, in two different places?

Congratulations. You modelled, lit, rigged, animated and rendered a real 3D scene."""),
        ],
        diagram=flow([("LOOP", "First and last|keys match"), ("TEST", "One frame,|note the time"), ("RENDER", "PNG frames,|resume allowed"), ("ENCODE", "H.264 MP4|1080p, 24 fps"), ("DELIVER", "Phone check,|keep a master")], "e5", "Render frames first, then make the video"),
        caption="Render PNG frames first, then encode one MP4, so a power cut never costs you the whole job.",
        terms=[("Walk cycle", "A short loop of walking poses that repeats without a visible jump."), ("Root bone", "The top bone of the hierarchy, which moves the whole character."),
               ("Cyclic extrapolation", "A setting that repeats an animation curve forever."), ("Render engine", "The system that calculates the final image from the scene."),
               ("PNG sequence", "A folder of still images, one for each frame, that is later turned into a video."), ("H.264", "A common video codec that nearly every phone and website supports."),
               ("Master copy", "Your original, highest-quality files, kept so you can export again later.")],
        mistakes=["Rendering straight to a video file, so a power cut or crash destroys everything.", "Copying frame 1 onto frame 24 instead of frame 25, so the loop stutters.",
                  "Starting a full-quality render without timing one test frame first.", "Delivering one huge file and never checking it on a real phone."],
        quiz=[dict(q="A walk cycle has identical keys on frames 1 and 25. How long is the cycle?", o=["25 frames", "24 frames", "12 frames", "1 frame"], a=1, why="Frame 25 only completes the last movement and matches frame 1, so the cycle is 24 frames."),
              dict(q="A step is 0.7 m and takes 12 frames. How far should the root move each frame?", o=["0.7 m", "0.012 m", "0.058 m", "1.4 m"], a=2, why="0.7 m divided by 12 frames is about 0.058 m per frame, which stops the feet from sliding."),
              dict(q="Why render a PNG sequence before making the MP4?", o=["PNG files are always smaller", "It adds sound automatically", "Cycles requires it", "If the power goes out, the finished frames are saved and you can resume"], a=3, why="Each frame is saved as it finishes, so a power cut only costs the frame in progress."),
              dict(q="One test frame takes 15 seconds. How long will 120 frames take?", o=["3 minutes", "15 minutes", "30 minutes", "3 hours"], a=2, why="15 seconds x 120 frames = 1,800 seconds, which is 30 minutes.")],
    ),
}
