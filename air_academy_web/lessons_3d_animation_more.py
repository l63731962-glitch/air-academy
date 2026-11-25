"""3D Animation track: lessons 6 to 15, added when the track grew from 5 to 15 lessons (course_plan.py says where each one sits on screen).
Same format as lessons_3d_animation.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option.
Blender menus, shortcuts and add-ons change between versions, so lessons point learners to the current manual and say when a detail may differ."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[6] = dict(   # Installing Blender and setting up your first project
    minutes=15,
    hook="Blender is one of the great gifts to young animators: a complete 3D studio for modelling, rigging, animating, lighting, rendering and even video editing, free and open source, used by hobbyists and professional studios alike. It can look frightening on the first day, with panels, buttons and strange shortcuts everywhere. The trick is to see that the screen is only a few areas, each with a simple job, and that ten keys will carry you a long way. In this lesson you will check your computer, download and install Blender from the official source, set a few preferences that save pain later, learn the four main areas, move around the 3D view without getting lost, set up a clean project folder and save it safely, and render your very first image. Menus and shortcuts change a little between versions, so check the current manual when something looks different.",
    sections=[
        ("Check your computer and download safely", """Blender is demanding in places, but it runs on modest laptops if you keep scenes small. Before you download, look at the **official system requirements page** on blender.org, since these change with each version. As a rough guide:

- **A 64-bit computer** with Windows, macOS or Linux.
- **8 GB of memory** is a comfortable minimum for learning. 4 GB can work for very small scenes, but expect slowness.
- **A graphics card** that supports a recent OpenGL version helps. Very old integrated graphics may run an older Blender version better.
- **Several GB of free disk space** for the program, your projects and renders.

Download **only from blender.org.** Fake download sites bundle malware. Choose the **current stable or long-term support (LTS) version.** The LTS version is updated for bug fixes for a longer time, which is a good choice for a course. Windows offers an **installer** and a **portable ZIP** you can run without installing, which is handy on a school computer or a USB drive. When data is costly, download once at a library or an office and share the installer."""),
        ("Preferences that save you pain", """Open **Edit, then Preferences,** and set up these before you start:

1. **Auto Save:** under **Save and Load,** make sure auto save is on, with a short interval such as 2 minutes. With frequent power cuts, this alone can save a day of work.
2. **Input, Emulate 3 Button Mouse:** if you do not have a middle mouse button (most laptops), turn this on. It lets you orbit the view with **Alt and the left mouse button.**
3. **Input, Emulate Numpad:** if your keyboard has no number pad, this lets the number row switch views.
4. **Interface, Resolution Scale:** raise it if the buttons look tiny.
5. **Viewport, display:** keep the default, but reduce effects if your computer is slow.
6. **Save Preferences** (check that auto-save preferences is on).

Also learn **File, Save Versions,** which by default keeps a backup copy of your file ending in `.blend1` every time you save. If you ever ruin a file, rename the backup and open it. A **mouse** is far better than a touchpad for Blender, and a cheap wired one is a worthwhile purchase."""),
        ("The four areas of the screen", """The default layout is built from areas, each with a job:

- **3D Viewport (the big window):** where you see and edit your scene. The header at the top holds the mode switch, the view menu and the shading buttons.
- **Outliner (top right):** a list of every object in the scene, like a file manager. Rename objects here and hide or show them.
- **Properties editor (bottom right):** all the settings for the selected object, the scene, the render, the materials and modifiers. The tabs run down its left side.
- **Timeline (bottom):** the playback controls and frame numbers, used later for animation.

You can **change any area** into another type from the editor-type button in its corner, and drag the borders to resize. **Workspaces** along the top (Layout, Modeling, Sculpting, UV Editing, Texture Paint, Shading, Animation, Rendering, Compositing, Scripting) are saved arrangements for different jobs. Click through them once to see what they offer, then return to **Layout.**"""),
        ("Moving around the 3D view", """Getting lost in 3D space is the first big frustration, so practise navigation:

- **Orbit:** hold the **middle mouse button** and drag (or **Alt and left mouse** with emulation on).
- **Pan:** hold **Shift and the middle mouse** and drag.
- **Zoom:** scroll the **mouse wheel.**
- **Standard views:** the **number pad** keys give front (1), right (3), top (7) and camera (0) views. Ctrl with the same keys gives the opposite side.
- **Frame the selection:** the **number pad period** key, or View menu, then Frame Selected.
- **Local view:** the slash key isolates the selected object. Press it again to return.

The three basic **transform keys** are **G** (grab and move), **R** (rotate) and **S** (scale). Press the key, move the mouse, and **click to confirm** or **right-click or Escape to cancel.** Type **X, Y or Z** right after to lock the action to an axis, and type a **number** for an exact value. These keys appear in every lesson of this track."""),
        ("Your first saved project and first render", """Set up good habits from day one:

1. **Create a project folder** on your computer, for example `3D_Course/first_scene`, with sub-folders `textures`, `renders` and `reference`.
2. **Start Blender,** and click away the splash screen. You will see a **cube, a light and a camera.**
3. **Select the cube** by clicking it, and press **G, then Z,** and move it up a little. Press **S** to scale and **R** to rotate it.
4. **Add objects** with **Shift and A:** try a sphere and a cone.
5. **Look through the camera** with **number pad 0,** and move the camera until the objects are framed.
6. **Save with Ctrl and S** into your project folder, as `first_scene_v01.blend`. Later versions get new numbers.
7. **Render an image** with **F12.** A new window opens and draws your picture. Save it from **Image, Save As,** into your `renders` folder.

Congratulations: you have modelled, arranged, lit, photographed and saved a 3D scene. Write down the keys you used, and keep the list beside your computer."""),
    ],
    diagram=flow([("Download", "blender.org only"), ("Preferences", "autosave, mouse"), ("Areas", "viewport, outliner"), ("Navigate", "orbit, pan, zoom"), ("Save, render", "Ctrl S, then F12")], "t3d6", note="Ten keys carry you a long way."),
    caption="Download from blender.org, set preferences, learn the areas, navigate the viewport, then save and render a first scene.",
    terms=[("Viewport", "The window where you see and edit your 3D scene."), ("Outliner", "A list of every object in the scene."),
           ("Properties editor", "The panel with settings for objects, materials, modifiers and rendering."), ("Workspace", "A saved arrangement of areas for one job, such as modelling or animation."),
           ("LTS version", "A Blender release supported with bug fixes for a longer time."), ("Auto save", "A setting that saves a backup copy of your work every few minutes.")],
    mistakes=["Downloading Blender from an unofficial site.", "Leaving auto save off when power cuts are common.", "Working on a laptop touchpad with no mouse and no emulation settings.", "Not saving numbered versions of the file."],
    quiz=[dict(q="Where should you download Blender?", o=["Any site with a free link", "blender.org", "A pirate forum", "A chat message"], a=1,
               why="The official site is the safe source."),
          dict(q="Which keys move, rotate and scale an object?", o=["A, B, C", "X, Y, Z only", "G, R, S", "F1, F2, F3"], a=2,
               why="G grabs and moves, R rotates and S scales."),
          dict(q="What does F12 do?", o=["Renders an image", "Deletes the cube", "Opens the manual", "Saves a backup"], a=0,
               why="F12 renders the current frame from the active camera."),
          dict(q="What does the Emulate 3 Button Mouse setting help with?", o=["Faster rendering", "Orbiting the view without a middle mouse button", "Adding sound", "Changing colours"], a=1,
               why="It lets you orbit with Alt and the left mouse button.")],
    activity="Install Blender from blender.org, turn on auto save and mouse emulation if needed, build a folder structure, arrange three objects, frame them with the camera, render with F12 and save the project as version one.",
)

LESSONS[7] = dict(   # Modeling a simple character, step by step
    minutes=17,
    hook="Modelling a character does not require special talent, only a method. Professional modellers do not sculpt a perfect person from nothing. They start with a plain box, add a little shape at a time and check their work from every side. In this lesson you will follow that method in Blender to build a simple, cute, low-polygon character, such as a small robot or a round, friendly creature, in about an hour. You will learn to set up reference pictures, use the mirror modifier to model only half of the body, extrude limbs, add loop cuts for joints, shape a head, smooth the surface with a subdivision modifier and finish with a clean, named, saved model that is ready for texturing and rigging. Key names are for current Blender versions, so check the manual if a menu looks different.",
    sections=[
        ("Set up reference and plan the character", """Good models start before the first cube:

1. **Choose a design** you can finish: a round body, a big head, short arms and legs. Check the model sheet from your design work.
2. **Draw a front view and a side view** with matching heights, on paper or in a drawing program. Keep the feet at the same level in both.
3. **Bring them into Blender** with **Add, Image, Reference,** and set them in the **front (number pad 1)** and **side (number pad 3)** views. Lower their opacity so you can see the model through them.
4. **Choose a polygon budget,** for example **under 5,000 faces** for your first character, so the file stays light on a weak laptop. You can show the statistics with the overlay menu.
5. **Plan the parts:** body, head, arms, legs, and any extra like a hat or antenna.

If the character is **symmetrical,** you only need to build half. That is the next step, and it saves half of your time."""),
        ("Block the body with a mirror", """Start with big, simple forms:

1. **Delete the default cube,** or use it as the body. Press **Tab** to enter **Edit Mode** (and Tab again to leave).
2. Add a **Mirror modifier** from the **Properties editor,** under the wrench tab. Turn on **Clipping,** so the middle vertices stay on the centre line, and check the correct axis (usually X).
3. **Delete half** of the cube's faces if you like, and model only one side.
4. **Scale and move** the body to match your reference.
5. Use **E to extrude** a face to create the **leg.** Extrude downward, then scale the end face a little smaller for a foot or a boot.
6. Select a side face and **extrude an arm.**
7. Use **Ctrl and R** to add a **loop cut** where joints will be, such as the knee and the elbow. Scroll the mouse wheel to add more loops, and click to confirm.

Check from the **front, side and three-quarter views** every few steps. Many beginners model only from the front and get a flat character."""),
        ("The head and the details", """The head carries the personality:

1. **Add a UV sphere or a cube** for the head, and place it on top of the body.
2. **Scale it big,** since a large head reads as cute and friendly.
3. **Loop cut around the eyes and the mouth** so you can add detail there.
4. **Shape the face** by moving vertices, using **proportional editing** (the **O** key) for smooth moves.
5. Add **simple eyes** as spheres, and **ears or a hat** if you want. Keep extra parts **as separate objects** that can be parented later.
6. **Check the silhouette:** use the solid black view. Can you recognise your character?
7. Keep **balance and weight:** a heavy head needs a stable body.

Use **simple shapes first,** and add details only when the large forms are right. Resist adding fingers, buttons and a hundred small parts on the first day. A character with mitten hands is easier to rig and to animate."""),
        ("Smooth the surface and tidy the mesh", """Now make it look polished:

- **Subdivision Surface modifier:** add it under the wrench tab (or press **Ctrl and 1 or 2**). It rounds the corners by adding more faces. Use level 1 or 2 in the viewport and keep render level low on a weak computer.
- **Shade smooth:** from the **Object menu, Shade Smooth,** so the surface does not look faceted. (Check your version's menu for the exact place.)
- **Edge loops for joints:** make sure there are at least **two or three loops** around the knees, elbows and shoulders so they can bend.
- **Quads, not triangles:** keep faces four-sided where possible.
- **Clean up:** **Mesh, Clean Up, Merge by Distance** removes doubled vertices.
- **Check normals:** turn on **Face Orientation** in the overlay. Blue means outward, red means flipped, and flipped faces should be fixed with **Recalculate Outside** (Shift and N in Edit Mode).
- **Apply the scale** (**Ctrl and A, then Scale**) so the object's scale is 1. This prevents odd behaviour in rigging."""),
        ("Name, save and review", """Before you move on:

1. **Name every object** in the Outliner: `Character_Body`, `Character_Head`, `Eye_L` and `Eye_R`, rather than `Sphere.003`.
2. **Group related parts** into a **collection** called `Character`.
3. **Place the origin** (the object's pivot) at the feet or the centre of the body, so it moves sensibly.
4. **Set a neutral pose,** such as a T-pose or relaxed A-pose, with arms away from the body for easier weight painting.
5. **Save the file** as `character_model_v01.blend` and make a backup.
6. **Render a turntable view** or take screenshots from front, side and back, and **compare with your reference.**
7. **Ask a friend:** does it look like the design?

Common mistakes: working only from one view, adding tiny details too early, forgetting the mirror clip, leaving flipped faces, and skipping names. A simple model that is clean and finished is the best foundation for texturing and rigging in the next lessons."""),
    ],
    diagram=timeline([("Reference", "front and side"), ("Block body", "cube and mirror"), ("Limbs", "extrude and loops"), ("Head", "big and simple"), ("Smooth", "subdivide, shade"), ("Clean and save", "name and apply scale")], note="Big forms first, details last."),
    caption="Modelling steps: reference, block the body with a mirror, extrude limbs, shape the head, smooth and clean up.",
    terms=[("Reference image", "A picture placed in the scene to guide modelling."), ("Mirror modifier", "A tool that copies one half of a model to the other side."),
           ("Extrude", "Pulling out new geometry from a face or edge."), ("Loop cut", "Adding a ring of edges around a model."),
           ("Subdivision surface", "A modifier that smooths a model by adding more faces."), ("Apply scale", "Making an object's current size its normal size of one.")],
    mistakes=["Modelling only from the front view.", "Adding fingers and tiny details before the main shapes work.", "Leaving the mirror modifier without clipping so the centre splits.", "Leaving objects named Sphere.003 and Cube.001."],
    quiz=[dict(q="Why use a mirror modifier?", o=["It adds colour", "You model one half and the other half is made for you", "It speeds up rendering", "It removes the camera"], a=1,
               why="Symmetry halves your modelling work."),
          dict(q="What does E do in Edit Mode?", o=["Extrudes new geometry", "Exports the file", "Erases the scene", "Enlarges the window"], a=0,
               why="E pulls new faces or edges out of the selection."),
          dict(q="Why add loop cuts around knees and elbows?", o=["For colour", "So the joints can bend cleanly later", "To reduce file size", "To change the light"], a=1,
               why="Extra loops give the surface room to fold."),
          dict(q="Why apply the scale before rigging?", o=["It prevents odd behaviour in bones and weights", "It removes the mirror", "It makes the file smaller", "It adds a texture"], a=0,
               why="Unapplied scale can cause confusing results in rigging.")],
    activity="Model a simple low-polygon character from front and side references using a mirror modifier, extrusions, loop cuts and a subdivision surface, then name every part, apply the scale, save it and render front, side and back views.",
)

LESSONS[8] = dict(   # UV unwrapping and texturing
    minutes=16,
    hook="Your character is a smooth grey statue. To give it colour, skin, cloth, freckles, stripes or a painted smile, you need to put pictures onto its surface. That is texturing, and it depends on one clever step: unwrapping the 3D model into a flat map, like cutting an orange peel and laying it on the table. That flat map is called a UV map. Once you have it, you can paint on the flat image and the colours appear on the 3D model. In this lesson you will mark seams, unwrap a model, check for stretching with a test pattern, paint a texture directly in Blender, connect it to a material and, importantly, save the painted image so you do not lose it. This is one of the most satisfying steps of the whole 3D process, because your character suddenly gains personality.",
    sections=[
        ("What UV mapping is", """Imagine wrapping a gift in paper. Each point on the 3D surface has a matching point on the flat paper. Those flat coordinates are called **U and V** (not X and Y, to avoid confusion with 3D axes). The **UV map** records where each face of the model sits on the flat image.

You need it because:

- A **texture image** is flat, but the model is 3D.
- Without a UV map, the colour cannot be placed on the right spot.

The steps are always the same: **cut seams, unwrap, check, then paint.** Simple stylised characters can also use **flat materials** with no UV map, for example a red material for the shirt and a brown one for the skin. That is a fast route for your first model. But for painted details such as a face, a pattern or a logo, you need UVs.

Blender includes a **UV Editing workspace** (a tab along the top), which shows the 3D model on one side and the flat UV layout on the other."""),
        ("Mark seams and unwrap", """A **seam** is a cut line on the model where it will be opened. Good seams are **hidden** where people rarely look: under the arms, along the inside of the legs, behind the head.

1. Go to the **UV Editing workspace,** and make sure you are in **Edit Mode** with the model selected.
2. Switch to **Edge select mode** (press **2**).
3. **Select a loop of edges** where you want a cut (Alt and click on an edge loop).
4. Press **Ctrl and E,** and choose **Mark Seam.** The edges turn red.
5. Mark seams around the arms, the legs, the head base, and a line down the back.
6. Select all (**A**), press **U,** and choose **Unwrap.**

The model's flat pieces, called **islands,** now appear in the UV editor. For quick results on simple objects, **Smart UV Project** unwraps with automatic seams, but the result may be messy. Try manual seams for characters. Mirrored models should have a clean, symmetrical layout, which you can **overlap** for the two halves if the texture is also symmetrical."""),
        ("Check for stretching and pack the islands", """A bad unwrap **stretches** the texture, making squares into long rectangles. Check it:

1. In the UV editor, open the **Image menu, New,** and create a **UV Grid** or **Color Grid** test image, for example 1024 by 1024.
2. Assign it temporarily in the Shading workspace, or view it in the **UV editor overlay.**
3. Look at the checker pattern on the 3D model. **Even squares** mean a good map. **Stretched or tiny squares** mean you should add seams or adjust.
4. **Scale the islands** so that important areas, such as the face, get **more** of the texture space.
5. **Pack the islands** (UV menu, Pack Islands) so they fit into the square with small gaps, using the space well.
6. Keep islands **inside the square,** between 0 and 1.

Fix problems now. A stretched map cannot be repaired by painting. Also keep the **texel density** (the number of pixels per area) similar across the model, so one arm does not look blurry while the other is sharp."""),
        ("Paint the texture", """You can paint in Blender or an outside program:

1. Open the **Texture Paint workspace.** Blender may ask you to add a **base color** texture: click **Add Texture Slot, Base Color,** name it `character_color`, and choose **1024 by 1024** pixels (use 2048 later if you need more detail on a good computer).
2. Choose the **Draw brush,** pick a colour and size, and **paint directly on the model.** The paint appears on the UV image too.
3. Paint **big areas of flat colour** first (skin, clothes), then **details** like eyes, mouth, buttons and patterns.
4. Use **separate layers** in an outside painting program such as **Krita** if you prefer: export the UV layout (UV menu, Export UV Layout), paint over it, and import the finished image.
5. Keep your **palette** from the design stage.
6. **Check from all sides,** and paint **across the seams** carefully.

**Important:** painted images live only in memory until saved. In the image editor, use **Image, Save As** (or Save All Images) and store the file in your project's `textures` folder. **If you forget, you lose your painting when you close Blender.**"""),
        ("Connect the texture to a material", """Finally, make sure the material uses your texture:

1. Go to the **Shading workspace.** You will see a **node editor** with a **Principled BSDF** node connected to **Material Output.**
2. Add an **Image Texture node** (Shift and A, Texture, Image Texture) and select your saved image.
3. **Connect the Color output** of the image node to the **Base Color** input of the Principled BSDF.
4. In the viewport, switch to **Material Preview** shading, to see the colours with lighting.
5. Adjust **Roughness** (higher is matte, lower is shiny) for skin, cloth and metal.
6. For several parts, create **several materials** and assign them to different faces.
7. **Pack the textures** into the file (File, External Data, Pack Resources) or keep the files in a clear `textures` folder with **relative paths,** so nothing breaks when you move the project.
8. **Only use images you made or have a licence for.**

Save the project as `character_textured_v01.blend`, render a quick image and compare with your design. A neat, simple texture is more valuable than a complicated one that is blurry or stretched."""),
    ],
    diagram=flow([("Mark seams", "hidden places"), ("Unwrap", "flatten the model"), ("Check", "use a test grid"), ("Paint", "colour, then detail"), ("Save image", "do not lose it")], "t3d8", note="Cut, flatten, check, paint, save."),
    caption="Mark seams, unwrap, check with a test grid, paint the texture and save the image file.",
    terms=[("UV map", "A flat layout of a model's surface used to place a texture."), ("Seam", "An edge where the model is cut open for unwrapping."),
           ("Island", "A flat piece of the unwrapped model in the UV map."), ("Texture", "An image applied to the surface of a model."),
           ("Principled BSDF", "Blender's main material node, with colour, roughness and other settings."), ("Texel density", "The number of texture pixels covering each area of the model.")],
    mistakes=["Painting a texture and closing Blender without saving the image.", "Placing seams in the middle of the face.", "Ignoring stretched squares in the test grid.", "Using textures from the web without a licence."],
    quiz=[dict(q="What is a UV map?", o=["A sound file", "A flat layout of a model's surface for placing textures", "A camera setting", "A kind of light"], a=1,
               why="UVs tell Blender where each face sits on the flat image."),
          dict(q="Where should seams usually go?", o=["Across the middle of the face", "In hidden places like under arms and inside legs", "Nowhere", "Only on the eyes"], a=1,
               why="Hidden seams stop visible breaks in the texture."),
          dict(q="What does a stretched checker pattern show?", o=["A good unwrap", "A problem with the UV map", "A sound error", "A lighting error"], a=1,
               why="Even squares mean even texture, and stretching means poor UVs."),
          dict(q="What must you do with a painted texture image?", o=["Save it as a file", "Nothing", "Delete it", "Rename the camera"], a=0,
               why="Unsaved painted images are lost when Blender closes.")],
    activity="Mark seams on your character, unwrap it, check it with a colour grid, paint a 1024 pixel base colour texture in Texture Paint mode, save the image, connect it to a Principled BSDF and render a textured picture.",
)

LESSONS[9] = dict(   # Inverse kinematics and control rigs
    minutes=17,
    hook="A basic rig, with bones that rotate, is enough to pose a character. But try to make a character walk, and you quickly meet a problem: when you move the body, the feet slide and you must fix them by hand on every frame. Professionals solve this with inverse kinematics, a system in which you place a foot or hand and the leg or arm bends itself to reach it. They also build control rigs, with simple shapes such as circles and boxes that an animator can grab instead of the hidden bones inside the model. In this lesson you will build an IK leg with a pole target, create control bones with custom shapes, add helpful constraints such as eye targets, organise the rig, test it thoroughly and learn when to use an automatic rig. Names of menus can change between Blender versions, so use the manual to confirm.",
    sections=[
        ("From a simple rig to a control rig", """In the earlier rigging lesson you made an **armature** and skinned the model to it. That is the **deformation rig:** the bones that actually move the mesh. A **control rig** adds a layer on top:

- **Control bones** are easy to select, with clear shapes and names. The animator only touches these.
- **Deform bones** are hidden. They follow the controls and move the mesh.
- **Helpers** are bones for special jobs, such as a pole target or an eye target.

Reasons to build controls:

1. **Speed:** big, clear shapes are quick to select in a busy scene.
2. **Safety:** the animator cannot accidentally move the wrong bone.
3. **Power:** controls can drive many bones at once, such as an IK foot that moves the whole leg.
4. **Consistency:** the same controls work for every shot.

For a small character, you can start with a **small number of controls:** a root, a hip or body control, a foot control on each leg, a hand control on each arm, a head control and the eyes."""),
        ("Build an IK leg step by step", """With FK, you rotate the thigh, then the shin, then the foot. With **IK,** you move the **foot** and the leg bends to follow. To set up an IK leg:

1. **Enter Pose Mode** with the armature selected.
2. Add an **extra bone at the ankle** for the foot control. Make it a separate bone that is **not** connected or parented to the shin (parent it to the root instead). Name it `foot_ctrl.L`.
3. Select the **shin bone,** open the **Bone Constraints tab,** and add an **Inverse Kinematics constraint.**
4. Set the **Target** to the armature and the **Bone** to `foot_ctrl.L`.
5. Set **Chain Length** to **2,** so the IK moves the shin and the thigh only (not the whole body).
6. **Move the foot control.** The leg bends. If the knee points the wrong way, add a **pole target.**

A **pole target** is a second bone placed in front of the knee. In the IK constraint, set **Pole Target** to that bone. The knee now points towards it. You may need to adjust **Pole Angle.** Repeat and mirror for the other leg."""),
        ("Control shapes, collections and naming", """Make controls readable:

- **Custom bone shapes:** create a **circle, a square or an arrow** as a simple object, then set it as the **Custom Shape** in the Bone properties. A circle around a foot is easy to find and click.
- **Colours:** use one colour for the left side, another for the right, and a third for the centre.
- **Hide the deform bones.** In current Blender versions, bones are organised into **bone collections** (in older versions, bone layers). Put controls in one collection and deform bones in another, and show only controls.
- **Names with sides:** use the standard suffixes **.L** and **.R** (or _L and _R). Blender's **mirror and symmetry** tools understand them.
- **Lock what should not move:** in a foot control, you may lock **scale.** Locking channels prevents accidents.
- **Hierarchy:** keep a sensible parent chain. The root moves everything, the body control moves hips and spine, the head control follows the neck.

A rig that is **tidy and well named** is much easier to animate and to share with others."""),
        ("Eyes, constraints and other helpers", """A few more tools make a rig feel professional:

- **Eye target:** add a bone in front of the face, and give each eye bone a **Damped Track** or **Track To** constraint aimed at it. Move one control and **both eyes look at the same point.** Eye direction is vital for acting.
- **Copy Rotation:** make one bone copy another, such as a twist bone following the wrist.
- **IK and FK switch:** advanced rigs let you toggle between IK and FK for an arm, using a custom property. Use FK for swinging arms and IK when a hand must stay on a surface.
- **Limit constraints:** stop a knee from bending backward by limiting rotation on one axis.
- **Spine controls:** two or three controls along the back give a flowing curve.
- **Parenting objects to bones:** attach a hat or a bag to the head bone.

Keep it **simple.** Every control you add is one more thing to animate, and a small character with 15 to 25 controls is plenty. Add a feature only when a shot needs it."""),
        ("Test, fix and consider Rigify", """Before animating, test the rig hard:

1. **Pose extremes:** raise the arms, bend deeply, twist the head, and look for **pinching, stretching and parts that follow the wrong bone.**
2. **Move the root** and check that nothing is left behind.
3. **Test a walk step:** plant the foot, move the body forward and see if the foot stays.
4. **Fix weights** in Weight Paint mode where the mesh breaks.
5. **Reset:** make sure that you can return to the **rest pose** easily (select all bones, then clear the transforms).
6. **Save a clean version** called `character_rig_v01.blend` before animating. If the rig must change later, save a new numbered file, and tell anyone using it.

**Rigify** is an add-on, shipped with Blender, which generates a complete human control rig from a template. It saves a great deal of time for human-shaped characters, but you must match its bones to your model and learn its controls. Check the current manual for how to enable and use it in your version. For a first project, building a **small custom rig** teaches you how everything works."""),
    ],
    diagram=tree("CONTROL RIG", [("Controls", ["Root", "Foot IK", "Hand and head"]), ("Deform bones", ["Spine", "Arms", "Legs"]), ("Helpers", ["Knee pole", "Eye target", "Constraints"])], note="Animate the controls, hide the rest."),
    caption="A control rig has easy controls for the animator, hidden deform bones for the mesh and helper bones for special jobs.",
    terms=[("Control rig", "A rig with easy-to-grab controls that drive hidden bones."), ("Inverse kinematics", "A system where moving the end of a limb makes the joints bend to follow."),
           ("Pole target", "A helper bone that decides which way an elbow or knee points."), ("Bone collection", "A group of bones that can be shown, hidden and coloured together."),
           ("Constraint", "A rule that controls how one bone or object follows another."), ("Rigify", "A Blender add-on that builds a full human control rig automatically.")],
    mistakes=["Making the IK chain too long so the whole body is pulled.", "Forgetting the pole target so the knee flips.", "Leaving all bones visible so animators select the wrong one.", "Changing the rig halfway through a shot without saving a new version."],
    quiz=[dict(q="What does inverse kinematics let you do?", o=["Move the foot and let the leg bend to reach it", "Change the colour of bones", "Add sound", "Render faster"], a=0,
               why="IK solves the joint angles from the position of the end bone."),
          dict(q="What does a pole target control?", o=["The speed of the animation", "The direction the knee or elbow points", "The texture size", "The camera lens"], a=1,
               why="The bend points towards the pole."),
          dict(q="Why use custom bone shapes?", o=["To make controls easy to see and select", "To make the file smaller", "To add more bones", "To remove the mesh"], a=0,
               why="Clear shapes like circles are quicker to find than plain bones."),
          dict(q="Why add a single eye target control?", o=["Both eyes look at the same point with one control", "It makes eyes bigger", "It adds blinking", "It removes the head"], a=0,
               why="Aiming constraints make eye direction easy to animate.")],
    activity="Add IK feet with pole targets and hand and head controls to your rig, give them custom shapes and side colours, add an eye target, hide the deform bones, test ten extreme poses and save the rig as a numbered version.",
)

LESSONS[10] = dict(   # Bouncing ball and body mechanics in 3D
    minutes=17,
    hook="The bouncing ball is the first exercise in every animation school, and in 3D it teaches you something extra: how to think in keyframes, curves and controls instead of drawings. Once the ball works, the same ideas carry directly to a character. Body mechanics is the study of how a body moves: how weight shifts from one foot to the other, how a jump begins in the hips and not in the knees, how a push travels through the whole body. In this lesson you will animate a ball in Blender step by step, using blocking, splines and the graph editor, add squash and stretch by scaling the ball, and then apply the same method to a character jump, with a centre of gravity, anticipation, flight and a heavy landing. You will also learn the workflow of blocking in stepped mode before smoothing, which professionals use to protect their timing.",
    sections=[
        ("Keyframes, the Timeline and the Dope Sheet", """A **keyframe** records a value of a property, such as the position of an object, at a certain frame. Blender fills in the frames between keys.

- **Set the project to 24 fps** and the frame range to match your shot, in the **Output properties.**
- **Insert a key:** hover over the 3D viewport and press **I.** Depending on your version and settings, this keys location, rotation and scale (or a chosen set). You can also right-click a property field, such as Location Z, and choose **Insert Keyframe.**
- **The Timeline** (bottom) shows the keys as small diamonds. Drag the **playhead** to change frames, and press **Space** to play.
- **The Dope Sheet** is a table of keys, where you can **select, move and copy keys** in time. It is the best place to change timing.
- **The Graph Editor** shows each channel as a **curve.** You will use it to shape movement.

Practise: key a cube moving left to right over 24 frames, play it and see how it slows at the ends (the default smooth interpolation). Try moving the keys closer together and farther apart to feel timing change."""),
        ("Animate the ball: block, then spline", """Work in stages, as professionals do.

**Stage 1: Blocking (stepped keys)**
1. Add a **sphere,** named `Ball`, and a flat **plane** as the ground.
2. Set the key poses on the **Z location:** frame 1 high up, frame 10 on the ground (contact), frame 20 at the top of the first bounce (lower than the start), frame 29 contact, and so on.
3. In the Graph Editor or Dope Sheet, set the **interpolation to Constant,** so the ball jumps from pose to pose. Play it. Watch the rhythm: does it feel like a bounce?

**Stage 2: Spline (smooth)**
4. Change the interpolation to **Bezier** (the default smooth curve).
5. Open the **Graph Editor.** The Z curve should look like a series of **arches.**
6. At the **contact points,** the curve should have a **sharp V shape,** because the ball does not slow down before hitting the ground. Select those keys and set the handles to **Vector** (shortcut **V**), so the curve has a point.
7. At the **tops,** keep the curve **smooth and rounded,** so the ball slows and hangs for a moment.

Because you blocked first, the timing was already right before you smoothed it."""),
        ("Squash, stretch and shadow in 3D", """Add life to the ball with **scale:**

1. Key the **scale** on the contact frames: wider on X and Y and **shorter on Z,** such as 1.2, 1.2, 0.7.
2. Key a **stretch** just before and after contact: **taller and thinner,** such as 0.9, 0.9, 1.2.
3. Return to **1, 1, 1** at the top of the arc.
4. Keep the **volume similar:** if the scale on Z drops, X and Y rise a little.
5. Make sure the **bottom of the ball touches the ground** on the contact frame. When you squash a sphere around its centre, the bottom lifts. Fix by moving the ball down or setting the **origin to the bottom** of the sphere before animating.
6. Add a **soft shadow:** a light and the ground plane give one automatically.

Try a **bowling ball** (no squash, short bounces) and a **balloon** (slow timing, floaty top, light squash). The **same method gives different weight** just by changing timing and scale. Put all three in one scene as a portfolio exercise."""),
        ("Body mechanics: a jump with weight", """Now use a character with a control rig. A jump has a centre of gravity, usually at the hips, that follows a **smooth arc,** even as limbs move on their own paths.

Block the key poses in **stepped mode** (use these frames as a starting point at 24 fps):

1. **Frame 1:** standing, relaxed.
2. **Frame 8: Anticipation.** Crouch deep, hips down and back, arms swung back.
3. **Frame 12: Take-off.** Body stretched upward, toes pushing, arms swinging up.
4. **Frame 20: Apex.** The highest point, hips over the feet, limbs tucked or spread.
5. **Frame 28: Contact.** Feet touch, knees bend, arms down.
6. **Frame 32: Down.** Deepest squat of the landing.
7. **Frame 44: Recovery.** Stand up and settle.

Tips: **move the hips first,** then the rest of the body follows with a few frames of **offset.** The head should stay fairly steady, and the **arcs** of the hands and feet should be smooth. In the Graph Editor, check the **hip Z curve:** a clean arch, with a longer time near the top."""),
        ("Check weight, timing and polish", """Look at your jump with these questions:

- **Does the character feel heavy or light?** Slow the crouch and deepen the landing for weight. Quicken the take-off for energy.
- **Is there a moment of hang time** at the top, with close spacing?
- **Does the landing absorb force** with bent knees and a dip in the hips, and then recover?
- **Is there overlap,** with arms and head lagging a few frames behind the body?
- **Do feet stay planted** on the ground when they should? Use IK and check there is no sliding.
- **Is the arc smooth?** Trace the path of the hips with the **motion path** feature (Pose menu, Motion Paths).
- **Is the timing right** when played at full speed, and in context with a camera?

Reference helps: film yourself jumping, and count frames. Do not copy exactly: **exaggerate** the crouch and the stretch. Save versions like `jump_block_v01` and `jump_spline_v02`, so you can compare. A **jump shot,** looped or placed in a scene, makes a great portfolio exercise."""),
    ],
    diagram=compare(("STEPPED BLOCKING", ["Constant interpolation", "Poses jump, no in-betweens", "Test timing and rhythm", "Fix big problems early"]), ("SPLINE POLISH", ["Bezier curves", "Computer fills in-betweens", "Shape arcs in the graph", "Add overlap and detail"]), vs="then", note="Block first, smooth second."),
    caption="Block in stepped mode to prove the timing, then switch to splines and polish the curves in the Graph Editor.",
    terms=[("Keyframe", "A saved value of a property at a certain frame."), ("Interpolation", "How the computer fills the frames between keys, such as constant or Bezier."),
           ("Blocking", "Setting the main poses and timing before smoothing."), ("Graph Editor", "A window that shows animation channels as curves."),
           ("Centre of gravity", "The point of a body that moves along the main arc, usually near the hips."), ("Motion path", "A line that shows the path of a bone or object across frames.")],
    mistakes=["Smoothing the animation before the timing of the blocking works.", "Letting the ball float above the ground on contact frames.", "Starting a jump from the knees instead of the hips.", "Never checking the arc of the hips."],
    quiz=[dict(q="Why block animation in stepped (constant) mode first?", o=["It uses less memory", "It adds sound", "It lets you judge timing before smoothing", "It changes the colour"], a=2,
               why="With no in-betweens you see the real rhythm of the poses."),
          dict(q="What shape should the ball's curve have at the contact points?", o=["A sharp V", "A smooth hill", "A flat line", "A circle"], a=0,
               why="The ball does not slow before hitting the ground."),
          dict(q="Which part of a jumping body should be keyed first?", o=["The fingers", "The eyes", "The toes", "The hips, the centre of gravity"], a=3,
               why="The body's main arc follows the hips."),
          dict(q="What does the Dope Sheet help with?", o=["Painting textures", "Changing the timing of keys", "Adding lights", "Exporting video"], a=1,
               why="You can select and move keys in time.")],
    activity="Animate three bouncing balls, a rubber ball, a bowling ball and a balloon, by blocking in stepped mode then splining, add squash and stretch, and then block a 44 frame jump for your rigged character with a hip arc.",
)

LESSONS[11] = dict(   # Facial rigs and expressions
    minutes=16,
    hook="You can make a body move beautifully, but audiences connect through the face. A small smile, a doubtful eyebrow, a blink at the right moment can say more than a whole body of action. In 3D, faces are brought to life with a few tools. The simplest and most reliable are shape keys, which are saved versions of the mesh, such as smile, frown and mouth open, that you can blend in and out with sliders. Combined with eye controls and a jaw bone, they give a character a full range of expression with very little rigging. In this lesson you will learn how to plan a face rig, make shape keys for expressions, blinks and mouth shapes, connect them to easy-to-use controls with drivers, test combinations, and prepare the face for lip-sync and acting. These steps use the current Blender interface, so check the manual if a panel has moved.",
    sections=[
        ("Plan the face rig", """A face rig has three main parts:

- **Eyes:** the eyeballs that rotate to look at a target, and the **eyelids** for blinking.
- **Brows:** which move up, down and in to show emotion.
- **Mouth and jaw:** the jaw opens and closes, and the lips make shapes for speech and smiles.

A simple and powerful method is **shape keys** (also called **blend shapes** or **morph targets** in other programs). Each shape key is a **new position of the vertices** of the face, stored on top of the **basis** (the neutral face). A slider from 0 to 1 blends between them. You can combine several: a **smile at 0.6** with **brows up at 0.4.**

Plan a **small, useful list** for a stylised character:

1. Blink (left and right separately)
2. Brow up (left and right) and brow down
3. Smile and frown
4. Jaw open
5. Mouth shapes: O, wide (E), closed press (M, B, P) and teeth-on-lip (F, V)
6. Cheek puff or a squint, if needed

Fifteen shape keys can express a lot."""),
        ("Make shape keys", """In **Object Data properties** (the green triangle tab) you find the **Shape Keys** panel.

1. **Add the Basis** key by clicking the plus. It stores the neutral face. **Never edit the Basis once other keys exist.**
2. **Add a new key** with the plus, and name it `blink_L`.
3. With that key selected, enter **Edit Mode** and **move the vertices** of the left eyelid closed. Use **proportional editing** for smoothness.
4. Leave Edit Mode. Move the **slider** to see the blink from 0 to 1.
5. Repeat for each shape: `smile`, `brow_up_L` and the rest.
6. For **symmetrical shapes,** make the left key, then use **Mirror** options (check the manual for the shape key tools in your version) to build the right one.
7. Use **Value**, **Min** and **Max** settings. Keep most between 0 and 1.
8. Use **Vertex Group** limits so a key affects only one area, such as the left half of the face.

**Important:** if you change the mesh with new vertices after making shape keys, some programs break them. Finish your modelling **before** you make shape keys, and ask for help from the manual if you must change the mesh later."""),
        ("Eyes and eyelids", """The eyes are the focal point:

- **Eyeballs as separate objects,** parented to **eye bones** (or to the head bone).
- **An eye target** (a controller in front of the face) and **Damped Track or Track To constraints** on the eye bones, as in the control rig lesson. Move the target and both eyes follow.
- **Blinks:** use the `blink` shape keys, or rotate separate **eyelid bones.** A blink should not go all the way closed in the first frame: it **closes quickly (about 2 frames) and opens slightly slower (about 3 frames).**
- **Eyelids follow the eye:** when the eye looks up, the upper lid rises a little. When it looks down, it lowers. This detail adds realism. A simple way is a **driver** or **Copy Rotation** constraint with a small influence.
- **Pupil size and highlights:** a **white highlight** on the eye gives life.
- **Avoid crossed or dead stares:** check eye alignment from the front and the side.

The **line of sight** tells the audience what the character is thinking, so give it as much attention as the mouth."""),
        ("Drivers: connect shape keys to controls", """A slider hidden in a panel is awkward to animate. A **driver** links one property to another, so a **bone** or a **custom property** can control the shape key.

A simple method:

1. Add a **control bone** in the face area, for example `mouth_ctrl`, and a small custom shape.
2. **Right-click the shape key's Value** and choose **Add Driver.**
3. In the driver editor, choose **Single Property,** and set the target to the control bone's **location Z** (or another transform channel).
4. Choose a simple **expression** or use the **map range** so that moving the bone by 0.02 meters gives a value from 0 to 1.
5. Move the bone and watch the face change.
6. **Limit the control bone** so it stays within a box.

Alternatively, **keep the shape key sliders** and animate them directly in the **Dope Sheet's Shape Key Editor.** Many studios do this for simple characters. Choose the system you will actually enjoy using, and keep it **simple and tested.** Name every driver clearly, and save the file as `face_rig_v01.blend` before animating."""),
        ("Test, combine and prepare for acting", """Test the face thoroughly:

1. **Check each shape alone,** at full value.
2. **Combine common pairs:** smile with brows up, jaw open with the O shape. Look for **odd distortions** when shapes overlap. Adjust the shapes or limit their ranges.
3. **Look from the side and the three-quarter view.** A face that works only from the front is not finished.
4. **Create a pose library** of the six core emotions: happy, sad, angry, surprised, scared and thinking, and save it. A quick way is to key the shape values at different frames and label them as **markers.**
5. **Test lip-sync:** record a short line, and animate mouth shapes to the sound.
6. **Check blinks and eye darts.**
7. **Render a close-up** and view it on a phone.

Keep the number of shapes small, since each extra shape is more work to animate and more to go wrong. A well-built, simple face rig lets you spend your time on **performance** and not on fighting the tools. In the next lesson, you will use it to animate a short acting shot."""),
    ],
    diagram=grid([("Basis", "the neutral face"), ("Blink", "left and right"), ("Brows", "up, down, in"), ("Smile", "and frown"), ("Jaw open", "for speech"), ("Mouth shapes", "O, E, M, F")], cols=3, note="Fifteen shape keys can express a lot."),
    caption="A simple face rig uses a neutral basis plus shape keys for blinks, brows, smiles, jaw and mouth shapes.",
    terms=[("Shape key", "A saved version of the mesh that can be blended in with a slider."), ("Basis", "The neutral shape that other shape keys are measured from."),
           ("Driver", "A link that lets one property control another."), ("Damped Track", "A constraint that points a bone at a target."),
           ("Vertex group", "A set of vertices that a setting or shape key can be limited to."), ("Eye target", "A control that both eyes look at.")],
    mistakes=["Editing the Basis shape after other shape keys exist.", "Making dozens of shape keys that nobody will use.", "Testing the face only from the front view.", "Closing a blink in one frame and opening it in one frame."],
    quiz=[dict(q="What is a shape key?", o=["A keyboard shortcut", "A saved version of the mesh that blends with a slider", "A sound file", "A type of camera"], a=1,
               why="Shape keys store alternative positions of the vertices."),
          dict(q="What should you never do once shape keys exist?", o=["Add colour", "Rename them", "Edit the Basis", "Save the file"], a=2,
               why="Other keys are measured from the Basis, so changing it breaks them."),
          dict(q="What does a driver do?", o=["Links one property to another so a control can drive it", "Renders faster", "Adds light", "Deletes bones"], a=0,
               why="A bone can control a shape key through a driver."),
          dict(q="Why use an eye target?", o=["It adds colour to eyes", "It makes eyes bigger", "It stops blinks", "Both eyes look at one point with a single control"], a=3,
               why="Tracking constraints make eye direction simple to animate.")],
    activity="Create a neutral basis and ten shape keys for your character, including blinks, brows, smile, jaw open and four mouth shapes. Add an eye target, test pairs of shapes, and save a pose library of six emotions.",
)

LESSONS[12] = dict(   # Acting and performance shots
    minutes=17,
    hook="A rig is a puppet, and a puppet does not act until someone gives it a thought. Performance animation is where 3D becomes storytelling. Anyone can make a character wave its arm. It takes an animator to make an audience believe that the character is thinking, hesitating, deciding. You have the tools now: a model, a rig, a face and the graph editor. This lesson gives you a method for a complete acting shot of about 8 to 10 seconds, such as a character hearing a noise, realising something and reacting. You will learn how to plan the thought, record and use reference, block key poses in stepped mode, add the face and eyes, refine with splines, use holds and contrast, and polish with a clear checklist. These are the same steps used in professional studios, scaled to a student project.",
    sections=[
        ("Choose a performance and plan the thought", """Pick a **short, simple acting idea** that you can finish. Good examples:

- A character **hears a strange sound,** looks, is scared, then hides.
- A character **receives good news** and tries not to smile, then bursts out.
- A character **tries to lift a heavy box,** fails, then succeeds.
- A character **waits nervously** then sees a friend arrive.

Answer these questions before you touch the computer:

1. **Who is the character** and what is their mood at the start?
2. **What triggers the change?**
3. **What do they think and feel** at each moment?
4. **What is the final feeling?**

Write a **thought sentence** in your own words, for example: “Kofi is bored, hears a clink from the kitchen, realises the cake is gone, and tiptoes away guiltily.” Break it into **beats:** idle, hear, look, realise, decide. Each beat needs a **clear pose and a clear time.** Keep the shot to **one character and one place.**"""),
        ("Record reference and thumbnails", """Make a video of yourself acting it out:

1. **Set up your phone** to film from the front and from the side if you can.
2. **Do several takes.** The first is stiff. The third is usually better.
3. **Watch and choose the key moments,** such as the moment you freeze, the look, the breath, the weight shift, the hand gesture.
4. **Count the timing in frames,** by stepping through the video. At 24 fps, a one-second pause is 24 frames.
5. **Draw thumbnails** of the strongest poses, with a **clear line of action and silhouette.**
6. **Exaggerate** each pose beyond what you did. Real life is quieter than animation needs.

Do not copy the video frame by frame. Reference is a guide to **timing, weight and ideas,** not an instruction. If you do not have a good place to film, use a mirror or ask a friend to act it out. Keep your reference in the project's `reference` folder."""),
        ("Block the performance in stepped mode", """Now work in the software:

1. **Set the frame range** (for example 1 to 216 for a 9 second shot at 24 fps) and add the **audio** if there is dialogue (see the editing lesson).
2. **Block only the major poses** for the body, head and eyes, at the right times, with **stepped interpolation.** Keep the number of poses small.
3. **Use markers** to label beats in the timeline.
4. **Play the blocking.** Does the story read, even with no in-betweens? Is the rhythm right?
5. **Check the poses in silhouette** and from the camera angle you will use.
6. **Adjust the timing** in the Dope Sheet: move keys, add holds and remove poses that do nothing.
7. **Show a friend** and ask what the character is thinking. If they do not know, fix the poses.

Stepped blocking is the most important stage. **If the blocking works, the rest is polish. If it does not, nothing will save it.**"""),
        ("Face, eyes, holds and breakdowns", """Once the blocking works:

1. **Switch to spline** interpolation, and look at the result. It will look floaty at first, which is normal.
2. **Add the eyes first.** Move the eye target so the **line of sight** is clear: where does the character look, and when? **Eyes lead:** the eyes arrive a few frames before the head, and the head before the body.
3. **Add blinks** on head turns and changes of thought.
4. **Add the face:** brows, smiles, mouth shapes. Time the expression change **just before** or with the pose.
5. **Add breakdowns:** extra poses between the keys that control arcs and the path of movement.
6. **Use holds:** keep the pose for several frames so the audience can read it, with a tiny **moving hold,** like breathing.
7. **Add overlap:** hands and head settle a few frames after the body.
8. **Use contrast:** a fast move after a long pause hits harder.

Work **from big to small,** one body part at a time. Check the graph editor for spikes and wobbles, and fix them."""),
        ("Polish, review and finish", """Use a clear checklist:

- **Story:** is the thought clear?
- **Poses:** strong silhouettes with a line of action?
- **Timing:** does it have rhythm, with holds and surprises?
- **Weight:** do feet stay planted, and do the hips shift?
- **Arcs and overlap:** smooth paths, parts settling at different times?
- **Face and eyes:** clear direction, blinks, expressions that match the thought?
- **Camera:** is the framing clear and the character readable?
- **Cleanliness:** no sliding, popping or jitter?

Use the tricks you already know: **take a break, play at small size, scrub frame by frame, watch with sound off.** Then **ask for feedback,** note the patterns and fix the top three issues.

Finally, **render a clean preview** at low quality and watch it on a phone. If it holds attention, **render the final.** Save every stage as a numbered file. A good acting shot of 8 to 10 seconds is one of the strongest items you can show in a portfolio."""),
    ],
    diagram=stack([("POLISH", "clean, overlap, details"), ("SPLINE AND FACE", "eyes, brows, mouth"), ("BLOCKING", "stepped key poses"), ("THOUGHT AND REFERENCE", "who, what, why")], "t3d12", note="Build from the bottom up.", both=False, arrows=False),
    caption="Acting is built from the bottom up: the thought and reference, then blocking, then spline and face, then polish.",
    terms=[("Beat", "A small unit of story, such as a look or a realisation."), ("Thought sentence", "A one-sentence summary of what the character thinks and does."),
           ("Reference", "A video or photo you study to find timing and weight."), ("Breakdown", "An extra pose between keys that controls the arc of the movement."),
           ("Moving hold", "A tiny movement during a held pose so it does not look frozen."), ("Line of sight", "The direction a character is looking, which shows what they think.")],
    mistakes=["Starting to animate without deciding what the character thinks.", "Copying reference frame by frame with no exaggeration.", "Splining before the blocked poses and timing work.", "Moving the head and body before the eyes lead."],
    quiz=[dict(q="Why block in stepped mode before splining?", o=["It makes the file smaller", "It adds colour", "It lets you judge the story and rhythm of the poses", "It adds sound"], a=2,
               why="If the blocking works the rest is polish."),
          dict(q="What usually moves first in a look?", o=["The feet", "The eyes", "The hands", "The hips"], a=1,
               why="Eyes lead, then the head and body follow."),
          dict(q="How should you use video reference?", o=["As a guide to timing and weight, with exaggeration", "Copy every frame", "Never film yourself", "Use it as the final render"], a=0,
               why="Reference gives ideas but animation needs stronger, clearer poses."),
          dict(q="What is a moving hold?", o=["A fast run", "A camera zoom", "A tiny movement such as breathing in a held pose", "A skipped frame"], a=2,
               why="It keeps a still pose alive.")],
    activity="Write a thought sentence and beats for an 8 to 10 second acting shot, film reference, block it in stepped mode, add eyes, blinks and face on splines, polish with the checklist and render a preview to watch on your phone.",
)

LESSONS[13] = dict(   # Camera moves, lighting and render settings for polish
    minutes=17,
    hook="Two renders of the same animation can look like different films. One is flat, noisy and grey. The other has soft shadows, a warm glow on the face, a gentle camera push and a clean picture. The difference is not the model or the animation, but the camera, the lights and the render settings, the finishing touches that turn a technical exercise into a picture people want to look at. They are also where beginners lose the most time, because a single wrong setting can turn a one-hour render into a ten-hour render. In this lesson you will animate the camera, choose lens and depth of field, build a good lighting setup with area lights and a simple sky, understand the main render settings in Blender's two render engines, estimate render time before you start and plan the render so that a power cut does not ruin your work. Menus change between versions, so confirm them in the current manual.",
    sections=[
        ("Animate the camera with purpose", """Camera moves tell the audience where to look and how to feel. Common moves:

- **Static:** no movement. Calm, stable, ideal for acting shots.
- **Push in (dolly in):** the camera moves towards the character. Builds focus or tension.
- **Pull out:** reveals the surroundings, or shows isolation.
- **Pan and tilt:** the camera turns left, right, up or down from a fixed position.
- **Track or truck:** the camera moves with the character.
- **Orbit:** the camera circles the subject, for a hero moment.

How to do it in Blender:

1. Add a camera, then **look through it** with number pad 0, and place it using **Ctrl, Alt and number pad 0** (aligns the camera to the current view).
2. **Insert keyframes** for the camera's location and rotation at the start and the end of the move.
3. In the **Graph Editor,** make the move **ease in and ease out,** so it does not start and stop suddenly.
4. For following a character, add an **Empty** at the character's chest and give the camera a **Track To constraint** aimed at it.
5. **Ask why** the camera moves. If there is no reason, leave it still. Slow, smooth moves usually beat fast, shaky ones."""),
        ("Lens, framing and depth of field", """The camera's settings change the feeling of a shot:

- **Focal length:** around **35 to 50 mm** is natural. **24 mm and below** is wide and exaggerates depth, which can distort faces up close. **85 mm and above** compresses space and flatters faces.
- **Framing:** use the **rule of thirds,** with the eyes near a top third line, and leave **look room** in front of a character who faces a direction.
- **Safe margins:** keep key elements away from the very edges.
- **Camera height:** eye level feels equal, low angles feel strong, high angles feel weak.
- **Depth of field:** enable it in the camera settings, set the **focus object** to the character's eye (or use the focus distance), and set a modest **f-stop,** such as 2.8 or 4. This blurs the background and draws attention. Be careful: deep blur costs render time, and too much looks fake.
- **Aspect ratio:** match your output, such as 16:9 (1920 by 1080) for most video.

Check the framing in the **camera view** with the **safe areas** overlay turned on, and look at every key pose, not only the first frame."""),
        ("Lighting that shapes the character", """Build lighting in layers, with the fewest lights that work:

1. **Key light:** the main light, an **area light** from the front and one side, slightly above eye level. Larger area lights give softer shadows.
2. **Fill light:** a weaker, softer light from the opposite side, or a bit of **world (environment) light.** It lifts the shadows.
3. **Rim (back) light:** from behind and above, to outline the character and separate it from the background.
4. **Background light:** to shape the environment.
5. **The world:** set a **sky colour** or a simple gradient. An **HDRI** (a panoramic image of a real place) gives realistic reflections, but **only use HDRIs you have the licence for.** Many free libraries offer CC0 images, and you should read each licence.

Adjust the **light colour and strength.** Warm key and cool fill is a classic, attractive mix. Aim for a **clear value structure:** the character's face should be the brightest, best-lit area of the frame. Start with **one light,** look at the render and add others only when needed."""),
        ("Render engines and the settings that matter", """Blender offers different render engines. Their names and options change with versions, so check the manual.

- **Eevee:** a real-time style engine that renders in seconds. It is excellent for stylised looks, previews and weaker computers.
- **Cycles:** a physically based path tracer that gives realistic light, reflections and soft shadows, but takes much longer, and is faster with a good graphics card.
- **Workbench:** very fast, for viewing models, not for final films.

Key settings:

1. **Resolution and percentage:** render drafts at **50%** (for example 960 by 540), the final at 100%.
2. **Samples:** the number of light calculations per pixel. More samples mean less noise but more time. Start low (for example 64 to 128 in Cycles) and increase only if noise is visible.
3. **Denoising:** turn it on to clean noise with fewer samples.
4. **Light bounces:** reduce for speed (for example 4 to 6 total).
5. **Colour management:** the default **view transform** gives pleasant contrast. Keep the default unless you know why you change it.
6. **Motion blur** only when it helps, since it costs time.
7. **Frame range and rate:** check them before every render.
8. **Output:** render **PNG image sequences** to a folder, not directly to a video file."""),
        ("Estimate and plan your render", """Do the maths before you press render:

> [Render budget]
> Shot length: 6 seconds at 24 fps = 144 frames
> Test one frame: 25 seconds
> 144 x 25 seconds = 3,600 seconds = 1 hour

Then:

- **Test several frames,** from busy and quiet parts of the shot, and use the **slowest** for your estimate.
- **If it is too slow,** reduce samples, resolution, bounces, the number of lights, texture sizes and effects like depth of field. Or switch to Eevee.
- **Render in sections** (for example frames 1 to 48, then 49 to 96), so you can stop and restart.
- **Render an image sequence.** If the power fails, you keep every completed frame and Blender can skip existing frames when **Overwrite** is turned off.
- **Choose your time:** long renders are best overnight or when power is stable. Close other programs.
- **Use render services** only after reading their prices, privacy and licence terms.
- **Check a few finished frames at full size** before leaving a long render.

Render a **draft of the whole shot** at low quality first. Fix problems in the animation, and then render the final. Rendering only once is the goal."""),
    ],
    diagram=bars([("Eevee draft", 4), ("Eevee final", 12), ("Cycles 64 samples", 30), ("Cycles 256 samples", 110)], note="Example seconds per frame. Test your own computer.", unit=" s"),
    caption="Example render times per frame for different settings. Real numbers depend on your scene and computer, so always test.",
    terms=[("Dolly", "Moving the camera towards or away from the subject."), ("Focal length", "A lens setting that decides how wide or narrow the view is."),
           ("Depth of field", "Blur on things that are not in focus."), ("Area light", "A light shaped like a panel that gives soft shadows."),
           ("Samples", "How many light calculations are made per pixel, affecting noise and render time."), ("HDRI", "A panoramic image used to light and reflect an environment.")],
    mistakes=["Rendering a full shot before testing a single frame.", "Rendering directly to one video file that can be lost in a crash.", "Using an HDRI image without checking its licence.", "Moving the camera for no reason."],
    quiz=[dict(q="Why render as a PNG image sequence?", o=["You keep finished frames if the computer stops", "It plays faster", "It adds sound", "It changes the lens"], a=0,
               why="A crash or power cut does not lose completed frames."),
          dict(q="What does a push in usually do for the audience?", o=["Hides the character", "Adds focus or tension", "Makes the shot silent", "Changes the aspect ratio"], a=1,
               why="Moving closer concentrates attention."),
          dict(q="How can you estimate total render time?", o=["Guess", "Ask a friend", "Time one test frame and multiply by the number of frames", "Wait to see"], a=2,
               why="A measured frame time gives a reliable plan."),
          dict(q="Which is a good lighting approach?", o=["Add twenty lights at once", "Start with one light and add others only when needed", "Use no lights", "Only use a flash"], a=1,
               why="Fewer lights are faster to render and easier to control.")],
    activity="Add a slow eased push-in camera move to your shot, set a 50 mm lens with a gentle depth of field, build key, fill and rim lights, test render three frames at half size, time them, calculate the full render time and render a draft sequence.",
)

LESSONS[14] = dict(   # Compositing, sound and exporting
    minutes=16,
    hook="Your frames are rendered, a folder full of numbered pictures. To a viewer, that is not a film yet. It needs sound, a little finishing and a file that plays on a phone. Blender itself can do all of these final steps. Its compositor can adjust colour and add glow, and its video sequencer can edit clips, add music and voices and export a finished video. Many students leave this stage until the last day and rush it. In this lesson you will learn how to build a simple compositing setup, assemble your rendered frames and sound in the video editor, add titles and credits, mix the sound, export a high-quality master and smaller copies, and check the result, so that your film is finished properly and plays correctly everywhere. As ever, check the current Blender manual for menu names in your version.",
    sections=[
        ("What compositing does", """**Compositing** means combining and adjusting images **after** rendering. It is faster than re-rendering, which makes it very useful on a slow computer. Common jobs:

- **Colour balance and contrast:** a slightly warm look for a sunset, a cooler one for night.
- **Glow (bloom)** around bright lights.
- **Vignette:** darker edges to focus attention.
- **Blur** for depth or speed effects.
- **Combining render passes,** such as a shadow pass and a mist pass, for more control.
- **Adding grain** to unify the picture.

In Blender, open the **Compositing workspace.** Enable **Use Nodes** in the compositor, and you will see a **Render Layers** node and a **Composite** node. Place nodes such as **Color Balance, Glare** and **Lens Distortion** between them. Keep the effects **subtle.** If you render frames and then apply the compositor to the sequence, you have a second chance to fix colour without re-rendering the 3D scene. Newer Blender versions reorganise some compositing features, so check the manual."""),
        ("Assemble the film in the Video Sequencer", """The **Video Editing workspace** works like a simple editor:

1. **Create a new scene or file** for the edit, and set the **frame rate and resolution** to match your renders.
2. **Add an Image/Sequence strip:** Add, Image/Sequence, and select all the PNG frames of a shot. The strip appears on the timeline.
3. **Trim and arrange** the strips in order. Move them with **G,** cut with **K** (a soft cut) and delete with **X.**
4. **Add transitions** only when needed. A **cut** is the default.
5. **Add colour strips or text strips** for titles and credits. Use a clean font whose licence you have checked, and keep text inside the safe area.
6. **Play back** the whole timeline, and fix the timing.
7. **Set the end frame** of the project to the last frame of the film.

If you have several shots, name each strip clearly (`sc01`, `sc02`) and **colour-code** them. Save the edit file as `film_edit_v01.blend`."""),
        ("Add voice, music and effects", """Sound makes the film:

1. **Import your sound files** with Add, Sound. Use **WAV** for clean quality. Place each on its own **channel:** voice, music, sound effects.
2. **Sync the sound to the picture.** Zoom in and move the sound strip frame by frame until hits and mouth shapes line up.
3. **Set the volume** of each strip in its properties. Keep dialogue clear and loudest, music lower, effects between.
4. **Use fades** (keyframe the volume) at the start and end, and **duck** the music under dialogue.
5. **Avoid clipping:** peaks should stay below the maximum. Watch the meters.
6. **Use only sound you have the rights to,** and keep a **credits list.**
7. For advanced cleaning, such as removing noise, prepare the audio in **Audacity** before importing.
8. Listen on **earphones and a phone speaker.**

If your shot has a **mouth sync,** make sure the sound track you used for animation is the **same version and starts at the same frame** as in the final edit."""),
        ("Export a master and copies", """Export in two steps:

**1. The master**
- Render the **PNG image sequence** with the compositor on, as your highest quality copy. Keep it safe.
- From the sequencer, you can also render a high-quality video.

**2. Delivery copies,** set in **Output properties:**
- **File format:** **FFmpeg Video.**
- **Container:** **MPEG-4.**
- **Video codec:** **H.264.**
- **Quality:** a high, constant-quality setting for the master-like version, or a moderate one for sharing.
- **Audio codec:** **AAC,** with a sensible bitrate. Enable **audio mixdown** so the sound is included.
- **Resolution:** **1920 by 1080** for the web, **1280 by 720** for WhatsApp and a smaller file.
- **Frame rate:** the same as the project.

Then press **Render Animation (Ctrl and F12).** The video file appears in your output folder. If a setting is missing in your version, check the current manual. For social media, you may need vertical or square crops, with titles in the safe area. Name files clearly, such as `MyShort_v03_1080p24.mp4`."""),
        ("Check and archive", """Always check the final file:

1. **Play the whole video** from start to end in a normal player, with sound.
2. **Look for problems:** black frames, flicker, missing frames, cut-off text, wrong speed, sound out of sync, clipping.
3. **Watch on a phone** at medium brightness, and on a computer.
4. **Compare file size** with the platform's limits and your audience's data costs.
5. **Fix problems and export again,** keeping numbered versions.
6. **Add a short credits card** at the end: your name, music and sound sources, asset licences and tool credits (Blender is open source, but it is kind to say what you used).
7. **Archive the project:** the `.blend` files, textures, renders, sound and a README of settings. Back up in **two places.**
8. **Share it:** upload to a video platform with a title, description and credits.

A film is finished only when it is exported, checked and backed up. Finish properly, and you will have a complete piece for your showreel."""),
    ],
    diagram=hub(("FINAL FILM", "one timeline"), [("Frames", "PNG sequence"), ("Compositor", "glow, colour"), ("Sound", "voice, music, fx"), ("Titles", "text and credits"), ("Export", "MP4 H.264"), ("Archive", "backup twice")], note="Finish properly, then back it up."),
    caption="The final film joins rendered frames, compositing, sound and titles, then exports to MP4 and is archived.",
    terms=[("Compositing", "Combining and adjusting images after they are rendered."), ("Video Sequencer", "Blender's built-in video editor."),
           ("Strip", "A block on the sequencer timeline representing a clip, image sequence or sound."), ("Codec", "A method of compressing video or audio, such as H.264 or AAC."),
           ("Master", "The highest quality version kept as the source for all copies."), ("Mixdown", "Combining all audio into the final sound track.")],
    mistakes=["Leaving the final edit and export to the last hour.", "Exporting the video without turning on the audio mixdown.", "Using music without checking its licence.", "Not backing up the master in two places."],
    quiz=[dict(q="What does compositing do?", o=["Models characters", "Rigs bones", "Combines and adjusts images after rendering", "Records voices"], a=2,
               why="Compositing adjusts colour and effects without re-rendering the 3D scene."),
          dict(q="Which video codec is commonly used for sharing?", o=["Nothing", "H.264", "ZIP", "JPEG only"], a=1,
               why="H.264 in an MP4 is widely supported."),
          dict(q="Why keep a PNG master?", o=["It is the highest quality copy for making other versions", "It plays on all phones", "It is the smallest file", "It adds sound"], a=0,
               why="All delivery copies should be made from the master."),
          dict(q="What should dialogue be relative to music?", o=["Quieter", "Clear and louder", "Muted", "Random"], a=1,
               why="Voice must be understood, so music sits underneath.")],
    activity="Add a subtle glow and colour balance in the compositor, assemble your frames and sound in the sequencer, add a title and credits, export a 1080p MP4 and a 720p copy, then watch both on a phone and note any problems.",
)

LESSONS[15] = dict(   # Final project: a rendered 3D character shot
    minutes=17,
    hook="This is where the track comes together. In this final project you will make a single polished 3D character shot of about 5 to 8 seconds, from an idea to a finished video with sound, and you will do it as a small production with a plan, a schedule, checkpoints and a review. One short shot, done well, is more valuable than a long film done badly. It shows modelling, texturing, rigging, animation, lighting, rendering and editing, all the skills a studio looks for, in a piece that can sit at the front of your showreel. The skill that is tested most is project management: choosing a doable idea, protecting your time, backing up your work and finishing. In this lesson you get the brief, a realistic four-week plan, a production checklist, a way to test your shot and advice on how to share it with the world.",
    sections=[
        ("The brief", """**Create a 5 to 8 second rendered shot of an original 3D character** with these requirements:

- **An original character,** modelled by you, with a clear silhouette, and textured with a painted or material-based design.
- **A control rig,** with IK feet or similar, and a simple face rig.
- **A performance with a clear thought:** an acting beat, a jump, a reaction or a short action. It must show **weight, timing and personality.**
- **A simple set:** a floor and a background, with at least one prop.
- **Lighting and camera:** key, fill and rim lights, and a purposeful camera.
- **Sound:** at least one sound effect, plus music or voice you have the right to use.
- **Format:** 1280 by 720 or 1920 by 1080, 24 fps, exported as an MP4 and a PNG master.
- **Credits:** a short end card.

**Idea examples:** a robot discovers a flower. A tired cook flips a pancake and misses. A cat-like creature spots a laser dot. A superhero lands from a jump and checks that nobody saw. Keep the idea **small, clear and fun.**"""),
        ("A four-week plan", """Work backward from your deadline. A part-time learner can use **four weeks:**

**Week 1: Plan and model**
- Day 1 to 2: idea, thought sentence, reference and thumbnails.
- Day 3 to 5: model the character, and name and tidy the mesh.
- Day 6 to 7: unwrap and texture.

**Week 2: Rig and set up**
- Day 8 to 10: rig the character with IK controls and test hard.
- Day 11 to 12: face shape keys and eye target.
- Day 13 to 14: build the simple set, props and a rough camera.

**Week 3: Animate**
- Day 15 to 16: block in stepped mode and check.
- Day 17 to 19: spline, face and eyes, breakdowns and overlap.
- Day 20 to 21: polish, feedback and fixes.

**Week 4: Finish**
- Day 22 to 23: final lighting, camera and render tests, then the render.
- Day 24 to 25: compositing, sound and export.
- Day 26 to 27: **buffer** for problems.
- Day 28: share, and write a reflection.

Add **25% more time** to every estimate. Back up **at the end of every work session.**"""),
        ("Production checklist", """Tick each box as you go.

**Pre-production:** idea and thought sentence, reference video, thumbnails, model sheet.

**Asset creation:**
1. Model: clean mesh, mirror, applied scale, named parts.
2. Texture: seams, UV map, painted image saved, material connected.
3. Rig: armature, IK controls, custom shapes, hidden deform bones.
4. Face: shape keys, eye target, blinks.
5. Test the rig in ten extreme poses.

**Production:**
6. Set the scene: ground, background, prop, units.
7. Camera and lighting tests.
8. Block in stepped mode, and show it to a friend.
9. Spline, eyes, face, breakdowns and overlap.
10. Polish passes in order: timing, poses, arcs, details.

**Finishing:**
11. Test render of several frames, time them and plan.
12. Final render as a PNG sequence.
13. Composite, add sound and credits, export MP4.
14. Check on phone and computer.
15. Archive and back up in two places.

Keep a **production diary:** one line a day."""),
        ("Test and review with a rubric", """Review your shot against a rubric similar to one a teacher or a studio might use:

- **Story and clarity (20%):** is the thought clear in the time given?
- **Animation (25%):** weight, timing, arcs, overlap and acting.
- **Character (15%):** appealing design, clean model and texture.
- **Rig and technical quality (10%):** no pinching, sliding or popping.
- **Lighting and camera (15%):** readable, appealing and purposeful.
- **Sound (10%):** clear and properly licensed.
- **Finish (5%):** a clean export, credits and backups.

Show your shot to **three people** who have not seen it. Ask: What happened? What did the character feel? Where were you confused? Which part did you like? Then **fix the top two problems.** Resist the urge to redo the entire shot at the last minute. If something is not going to improve the story, **leave it.**"""),
        ("Share it and keep growing", """When it is done:

- **Upload** the video, with a title, a short description, your role and the tools used. Credit every asset, sound and helper, and say honestly if any part used AI assistance.
- **Make a short breakdown reel,** showing the wireframe, the rig, the blocking and the final shot. Employers love to see how you work.
- **Add it to your portfolio page** and **showreel,** at a strong position.
- **Share on social media** with a short clip and a behind-the-scenes picture. Ask for feedback from animation communities.
- **Write a reflection:** what worked, what was hard, what you learned, and what you would change.
- **Plan your next step:** a longer shot, a second character, a short film, a game animation or a collaboration.

You have taken a character from an idea to a finished film. Keep that rhythm, and animate every week."""),
    ],
    diagram=timeline([("Plan", "thought and reference"), ("Model and texture", "build the look"), ("Rig", "controls and face"), ("Animate", "block, spline, polish"), ("Light and render", "test, then final"), ("Edit and share", "sound, export, credit")], note="Four weeks, one step at a time."),
    caption="A character shot goes from plan to model and texture, rig, animation, lighting and render, then editing and sharing.",
    terms=[("Brief", "A short description of what the project must include."), ("Production diary", "Short daily notes about what you did and learned."),
           ("Buffer", "Extra time in a schedule for problems."), ("Rubric", "A list of criteria used to judge the project."),
           ("Breakdown reel", "A short video that shows how a shot was made, step by step."), ("Checkpoint", "A moment to review and save before moving to the next stage.")],
    mistakes=["Choosing an idea that is far too big for one short shot.", "Leaving the final render and export to the last day.", "Having no buffer in the schedule.", "Skipping backups until something is lost."],
    quiz=[dict(q="How long should the final shot be?", o=["About 5 to 8 seconds", "Ten minutes", "One hour", "Two frames"], a=0,
               why="A short, polished shot is finishable and shows all the skills."),
          dict(q="Why add a buffer to the schedule?", o=["To make the film longer", "Because problems and delays always happen", "To remove sound", "To change the frame rate"], a=1,
               why="Power cuts, bugs and illness should not ruin the deadline."),
          dict(q="What should you do before the final render?", o=["Delete the backups", "Skip testing", "Add random effects", "Test render several frames and time them"], a=3,
               why="Tests prevent wasted hours of rendering with wrong settings."),
          dict(q="What is a breakdown reel?", o=["A reel of crashes", "A video that shows how a shot was made", "A sound file", "A texture"], a=1,
               why="It shows process, such as the rig and blocking, and helps employers judge your skill.")],
    activity="Plan and complete a 5 to 8 second 3D character shot following the four-week schedule: model, texture, rig, animate, light, render, composite, add sound and export. Share it with a breakdown clip and three viewers' feedback.",
)
