"""Game Development Masterclass: lessons 9 to 24, added when the course grew into a full course (course_plan.py says where each one sits on screen).
Same format as lessons_game.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option.
Code examples use Godot 4 GDScript because it is free and light, and each lesson says how the idea carries to other engines.
Engine licences, store rules, fees and revenue shares change often, so lessons that mention them tell the learner to check the current page."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[9] = dict(   # Game loops, rules and player goals
    minutes=15,
    hook="Ask ten people why a game is fun and you will hear ten answers, but almost every fun game shares the same bones: the player wants something, the rules make it hard enough to be interesting, and the game keeps answering what the player does. Designers call this the structure of play. You have already met the core loop in the foundations lesson. Here you go deeper and learn to design the loops inside loops, write rules that are clear and fair, and set goals that pull the player forward. Whether you are making a puzzle game, a runner or a village builder, these ideas decide whether people keep playing or quit after one minute.",
    sections=[
        ("Loops inside loops", """Good games have several loops running at different speeds:

- **Micro loop (seconds):** the action the player repeats, such as jump, land or shoot.
- **Core loop (minutes):** a satisfying cycle such as explore, fight, collect, upgrade.
- **Meta loop (hours):** the long arc, such as story chapters, unlocking new areas, or building a base.

Take a simple endless runner. The micro loop is dodge or jump. The core loop is run, collect coins and crash. The meta loop is spending coins on upgrades so the next run goes further. If any one loop is boring, the others cannot save it, so **test the micro loop first.** A jump that feels good for ten seconds is the foundation for everything else."""),
        ("Writing rules that are clear and fair", """Rules define what the player can and cannot do. Strong rules are:

1. **Few:** a rule you can say in one sentence is better than a rule you must look up.
2. **Visible:** the player should be able to see or learn the rule by playing, for example a red wall that hurts.
3. **Consistent:** if fire burns the player in level one, it must burn in level five. Breaking a rule without warning feels unfair.
4. **Fair:** when the player loses, they should know **why** and believe they could have done better.
5. **Interesting:** rules create choices. “Collect ten coins” is a rule. “You may carry only three coins, so choose which to take” is a choice.

> [Example: three tiny rules]
> The player has 3 lives. Touching an enemy costs 1 life. A heart pickup restores 1 life, but never above 3.

Notice that each rule is short and testable. If you cannot test a rule, you cannot be sure it works."""),
        ("Goals: why should the player act", """A **goal** tells the player what to do next. Games usually mix three kinds:

- **Long-term goal:** save the village, reach the end, get the highest score.
- **Short-term goal:** cross this gap, open this door, beat this wave.
- **Player-chosen goals:** build the biggest farm, find every secret, finish without dying.

Players need to see **progress** toward each goal: a score counter, a map that fills in, a progress bar or a door that opens. Without progress, even a clear goal feels pointless. The flow idea from psychology says people enjoy tasks that are **just hard enough:** too easy is boring, too hard is stressful. Your job is to keep the challenge slightly ahead of the player's skill, and to teach new skills before demanding them."""),
        ("Risk, reward and meaningful choices", """Fun comes from decisions with consequences. Ask of every feature: **what does the player choose, and what does it cost?**

- **Risk and reward:** a coin hangs over a pit. Is it worth the jump?
- **Trade-offs:** a fast character with low health, or a slow one with high health.
- **Resource limits:** limited ammunition, time or money force prioritising.
- **Uncertainty:** a little randomness keeps replays fresh, but too much makes skill feel useless.

Avoid **fake choices** where one option is always best, and avoid **grind** where the player repeats a dull task only to progress. If a feature makes the player do the same thing without a decision, either cut it or add a decision."""),
        ("Win, lose and the next try", """How a game ends shapes whether players try again:

- **Make losing quick to recover from.** Restart in under three seconds with a short message such as “So close!”.
- **Show what happened:** “You were hit by the red slime” teaches the player more than a blank screen.
- **Reward even when losing:** a score record, a new unlock or a small bonus.
- **Make winning feel earned:** a pause, a sound, a short celebration.
- **Create a hook for next time:** a best score to beat, a locked door to return to.

Write your game's rules and goals on one page before coding. A paper version with a friend, using cards and counters, will show weak rules in minutes and costs nothing."""),
    ],
    diagram=stack([("META LOOP", "hours: unlock areas, build, story"), ("CORE LOOP", "minutes: explore, collect, upgrade"), ("MICRO LOOP", "seconds: jump, shoot, dodge")], "g9", note="Test the bottom layer first.", both=False, arrows=True),
    caption="Three loops: seconds of action, minutes of play and hours of progress. The bottom loop must feel good first.",
    terms=[("Micro loop", "The small action the player repeats every few seconds."), ("Meta loop", "The long-term progress that keeps players returning, such as unlocks."),
           ("Flow", "The enjoyable state when a challenge matches the player's skill."), ("Risk and reward", "A choice where a bigger prize comes with a bigger chance of failure."),
           ("Fake choice", "A choice where one option is clearly best, so there is no real decision."), ("Grind", "Repeating a dull task only to reach the next reward.")],
    mistakes=["Writing too many rules for the player to remember.", "Breaking a rule without warning, which feels unfair.", "Making the player replay a long section after every failure.", "Adding features that give no real choice."],
    quiz=[dict(q="Which loop should you test and polish first?", o=["The micro loop, the action repeated every few seconds", "The meta loop", "The credits screen", "The store page"], a=0,
               why="If the smallest action is not fun, nothing built on it will be."),
          dict(q="What makes a rule fair?", o=["It is secret", "The player can see or learn it and it is applied consistently", "It changes each level", "It is very long"], a=1,
               why="Fair rules are clear and consistent so players can learn and improve."),
          dict(q="What is a meaningful choice?", o=["One where the best option is always obvious", "A decision where each option has a real cost and benefit", "A random result", "A menu button"], a=1,
               why="Meaningful choices involve trade-offs."),
          dict(q="How should failure be handled?", o=["Make the player wait a minute", "Restart quickly and show why the player lost", "Hide the reason", "Delete progress"], a=1,
               why="Fast restarts with clear feedback keep players trying.")],
    activity="Write a one-page rules and goals sheet for a tiny game with three short rules, one long-term goal, one short-term goal and what happens when the player loses. Test it on paper with a friend.",
)

LESSONS[10] = dict(   # Writing a one-page game design document
    minutes=15,
    hook="A builder does not start a house by stacking bricks. They draw a plan, and the plan lets the family, the engineer and the workers agree before anything is built. A game design document, or GDD, is that plan. Many beginners avoid writing one because they imagine a hundred-page book. In practice, a one-page GDD is one of the most useful things a solo developer or small team can have. It forces you to decide what the game is, keeps you from adding endless ideas, and lets you explain the game to a friend, a teacher, a teammate or a funder in two minutes. In this lesson you will learn what goes on the page and write your own.",
    sections=[
        ("Why one page", """A short document gets read, and a long one does not. A one-page GDD helps you:

- **Decide** what the game is and is not.
- **Communicate** the idea to teammates, artists, testers and publishers.
- **Resist scope creep:** when a new idea appears, check it against the page.
- **Stay motivated:** you can see the finish line.
- **Measure progress** by ticking off features.

The page is a **living document.** You update it when you learn something, and keep a short change log. Big studios write longer documents, but they all start with a one-page pitch."""),
        ("The sections of the page", """A clear structure for a small game:

1. **Title and one-sentence pitch:** “A tiny fisherman races a storm to bring his catch home.”
2. **Genre, platform and audience:** 2D arcade, Android and web, ages 10 and up.
3. **Core loop:** what the player does repeatedly.
4. **Player goal and challenge:** what they want and what stops them.
5. **Key features (maximum five):** the things that make this game this game.
6. **Controls:** how it is played on touch or keyboard.
7. **Art and sound direction:** two or three words and a few reference images.
8. **Scope:** the smallest version that is fun (the **minimum playable game**).
9. **Cut list:** nice-to-have ideas you will add only if time allows.
10. **Schedule:** milestones with dates.
11. **Risks:** what might go wrong, such as an untested mechanic."""),
        ("Writing a strong pitch and feature list", """The pitch is the sentence that sells the game. A useful formula: **“You are [who], doing [what], to get [goal], but [challenge].”**

> [Example: pitch]
> You are a village goalkeeper stopping penalties from a rival team, but every save makes the ball faster.

Then the **feature list.** Write each feature as something the **player experiences,** not a technical task:

- Good: “Collect fruit to grow longer, but do not hit your own tail.”
- Weak: “Implement a snake body array.”

Limit the list to **five.** If you have twelve, you have two games. Mark each feature as **must have, should have or could have.** Build the musts first."""),
        ("Scope, milestones and risk", """Most unfinished games die from being too big. To size your plan:

- **Estimate honestly,** then **double it.** Everything takes longer than expected, especially art, bugs and polish.
- Plan a **vertical slice:** one short level that is fully playable with real art, sound and menus. If the slice is fun, you can extend it.
- Set **milestones** such as: week 1 prototype, week 3 playable level, week 5 art and sound, week 6 playtest and fixes, week 7 release.
- List the **riskiest assumption** (“players will enjoy the tilt controls”) and test it **first,** with a rough prototype.
- Decide your **cut order:** what you remove first if time runs short.

Remember your real constraints: other work, school, power cuts and costly data. A plan that fits your actual hours is better than a perfect one."""),
        ("Using the document with others", """A GDD is also a tool for teamwork:

- **Share it** in an online document or a repository, with edit rights for your team.
- **Add images:** a sketch of the main screen explains more than a paragraph.
- **Keep a decision log:** short notes such as “We chose touch controls because most players use phones.”
- **Review it** at each milestone and remove what no longer fits.
- **Attach a one-page version** to messages when asking for feedback, so people can respond in minutes.

If you work with artists or musicians, include a **style sheet** and an **asset list** (name, size, status). Clear lists prevent confusion and wasted work. Keep the file in more than one place so a lost laptop does not lose your plan."""),
    ],
    diagram=grid([("PITCH", "one sentence"), ("CORE LOOP", "what players repeat"), ("FEATURES", "five at most"), ("SCOPE", "minimum playable game"), ("SCHEDULE", "milestones with dates"), ("RISKS", "test the riskiest first")], cols=3, note="One page, living document."),
    caption="A one-page design document: pitch, core loop, features, scope, schedule and risks.",
    terms=[("GDD", "Game design document: a plan that describes the game."), ("Pitch", "A short description that explains and sells the game."),
           ("Scope creep", "A project growing larger than planned as new ideas keep being added."), ("Vertical slice", "One short part of the game finished to full quality to prove the idea."),
           ("Minimum playable game", "The smallest version that is already fun."), ("Cut list", "Ideas you will drop first if time runs short.")],
    mistakes=["Writing a huge document that nobody reads.", "Listing technical tasks instead of player experiences.", "Planning twelve features for a first game.", "Not testing the riskiest idea early."],
    quiz=[dict(q="What is a vertical slice?", o=["A short section finished to full quality", "A cut of the sound", "A bug", "A save file"], a=0,
               why="A vertical slice proves the idea with real art, sound and play."),
          dict(q="How many key features should a small game's one-page GDD list?", o=["Fifty", "About five", "None", "Every idea you have"], a=1,
               why="A small feature list keeps the project finishable."),
          dict(q="What is scope creep?", o=["A slow enemy", "The project growing beyond the plan as ideas pile up", "A graphics setting", "A sales method"], a=1,
               why="Scope creep is the main reason small games are never finished."),
          dict(q="Why test the riskiest assumption first?", o=["It is easiest", "If it fails, you learn early before building everything else", "It looks good", "Rules require it"], a=1,
               why="Early tests prevent wasted work on an idea that does not work.")],
    activity="Write a one-page GDD for a game you could finish in six weeks. Include a one-sentence pitch, the core loop, five features marked must, should or could, a cut list and a risk you will test first.",
)

LESSONS[11] = dict(   # Choosing a game engine and creating your first project
    minutes=16,
    hook="Picking a game engine feels like a huge decision, and beginners often waste weeks comparing options instead of making something. The truth is simpler: the skills of game making, such as loops, collisions, state and feedback, transfer between engines. What matters is picking one that runs well on your computer, has good free learning material and can export where your players are. In this lesson you will compare the main engines honestly, make your choice with a short checklist, install and set up a first project, learn the editor layout and run your first scene. We use Godot 4 for examples because it is free, small and friendly to modest laptops, but we explain how each idea maps elsewhere.",
    sections=[
        ("Comparing the main engines", """Remember that licences, prices and features change, so **always check each engine's current page** before committing. In general:

- **Godot:** free and open source, a download of under a few hundred megabytes, ideal for 2D and capable for simple 3D. Languages: GDScript (Python-like) and C#.
- **Unity:** very large community and many tutorials, uses C#, strong for 2D, 3D, mobile and AR. Needs a stronger computer. Its licence terms have changed before, so read the current ones.
- **Unreal Engine:** top-quality 3D graphics, uses C++ and visual scripting (Blueprints), heavy on hardware, best for experienced teams.
- **GameMaker:** focused on 2D, gentle to learn, has its own language, usually paid for exports.
- **Construct and other no-code tools:** work in a browser, good for quick prototypes.
- **Web frameworks** such as Phaser and PixiJS use JavaScript, great if you already know web development.

There is no single best engine, only the best engine **for your project and computer.**"""),
        ("A short checklist for choosing", """Answer these questions honestly:

1. **What computer do I have?** If it has 4 GB of memory and no graphics card, choose a light engine.
2. **2D or 3D?** Most beginners should start in 2D, because the art and the maths are simpler.
3. **What do I already know?** Python experience points to GDScript. JavaScript points to a web framework. C# points to Unity.
4. **Where will players be?** Phones, web browsers, Windows PCs? Check that the engine exports there.
5. **Is there learning material I can use offline?** Data is costly, so download tutorials and documentation.
6. **What does it cost** to release, now and later? Check the licence for revenue limits or fees.

Pick one, **commit for three months,** and finish a small game. Switching engines in the middle of a project is the most common way to never finish."""),
        ("Installing and creating a project", """Using Godot as the example, the steps are similar in other engines:

1. Download Godot 4 from its **official website** only. Avoid unofficial download sites that may include malware.
2. Unzip and run the program. The standard build needs no installer.
3. In the **Project Manager,** click **New Project,** name it (for example `first_game`), choose a folder and a renderer, for a light 2D game the compatibility option is a safe choice on older laptops.
4. Click **Create and Edit.**

The project is a **folder.** Inside are your scenes (`.tscn`), scripts (`.gd`), art and sounds, and a `project.godot` settings file. Because it is just a folder of text-based files, it works well with **Git.** Put the project in a repository from day one, and add an ignore file so generated folders are not uploaded."""),
        ("The editor layout", """Every engine has the same main areas:

- **Scene or hierarchy panel:** the tree of objects in the current scene.
- **Viewport:** where you see and move things visually.
- **Inspector:** the properties of the selected object, such as position, size or colour.
- **File system panel:** your project's files.
- **Script editor:** where you write code.
- **Debugger and output:** messages, errors and performance data.
- **Play buttons:** run the game, run the current scene or stop.

Spend your first session just **clicking around.** Add a node, change a property in the inspector, press play. Learn the shortcuts for play, save and the move and scale tools. Most beginner confusion disappears once you know where things live."""),
        ("Your first running scene", """Build the smallest scene that proves everything works:

1. Create a root node of type **Node2D** and name it `Main`.
2. Add a **Sprite2D** child, and drag the project icon from the file panel into its Texture property.
3. Attach a script to `Main` and write:

> [GDScript]
> extends Node2D
>
> func _ready() -> void:
>     print("Hello from my first game")
>
> func _process(delta: float) -> void:
>     $Sprite2D.rotation += 1.0 * delta

4. **Save** the scene as `main.tscn` and press **Play.**

The icon should spin and the output panel should print your message. `_ready` runs once when the scene starts, and `_process` runs every frame, with `delta` the time since the last frame, so movement stays smooth on fast and slow computers. You have just used a **scene, a node, a script and the game loop.** In Unity the same ideas are a **GameObject,** a **MonoBehaviour** with `Start` and `Update`."""),
    ],
    diagram=compare(("PICK FOR YOUR GAME", ["Runs on your computer", "Exports where players are", "Free learning material", "Fits 2D or 3D choice"]), ("AVOID", ["Changing engine mid-project", "Chasing the newest tool", "Choosing only by hype", "Downloading from unofficial sites"]), vs="or", note="The best engine is the one you finish a game in."),
    caption="Choose an engine that suits your computer, your players and your learning material, then stay with it.",
    terms=[("Game engine", "Software that provides drawing, sound, physics, input and an editor for making games."), ("GDScript", "Godot's Python-like scripting language."),
           ("Scene", "A saved group of objects, such as a player or a level."), ("Node", "A building block in Godot that does one job, such as showing a sprite."),
           ("Inspector", "The panel that shows and edits the properties of the selected object."), ("Delta", "The time since the last frame, used to keep movement smooth.")],
    mistakes=["Spending weeks comparing engines instead of building.", "Downloading the engine from an unofficial site.", "Switching engines halfway through a project.", "Not keeping the project in Git from the start."],
    quiz=[dict(q="What is the best engine for a beginner?", o=["The one that suits your computer, project and learning material", "Always the most expensive", "Always the newest", "None"], a=0,
               why="Game making skills transfer, so choose a suitable engine and finish something."),
          dict(q="Why multiply movement by delta?", o=["To make the game slower", "So speed stays the same on fast and slow computers", "To save the game", "To change colours"], a=1,
               why="Delta is the frame time, so movement is based on time and not frame rate."),
          dict(q="Where should you download an engine from?", o=["Any site offering it free", "The official website", "A friend's email", "A random torrent"], a=1,
               why="Unofficial downloads can contain malware."),
          dict(q="What runs once when a Godot scene starts?", o=["_process", "_ready", "delta", "print only"], a=1,
               why="_ready is called once when the node enters the scene and is ready.")],
    activity="Download your chosen engine from its official site, create a project, put it in Git, make the spinning sprite scene and note what each editor panel does.",
)

LESSONS[12] = dict(   # Player movement and input
    minutes=17,
    hook="Movement is the first thing a player feels. If the character answers each press instantly and smoothly, the game feels alive. If it is sluggish, floaty or sticky, nothing else can rescue it. Great movement is not an accident. It is built from a few small ideas: reading input properly, using velocity, speeding up and slowing down, and for platformers, tuning jumps with tricks such as coyote time and jump buffering. In this lesson you will write top-down and platformer movement in GDScript, learn how to support keyboard, gamepad and touch, and learn how to tune the numbers until the character feels right. The same ideas apply in Unity, GameMaker and every other engine.",
    sections=[
        ("Reading input the right way", """Do not hardcode keys. Use **input actions:** named controls such as `move_left` or `jump` that you map to keys, gamepad buttons or touch. In Godot you set them in the **Input Map** in project settings. Then your code asks about actions, not keys:

> [GDScript]
> var direction := Input.get_vector("move_left", "move_right", "move_up", "move_down")

`get_vector` combines four actions into one direction that is already **normalised** (diagonal movement is not faster). Benefits of actions:

- Players can **remap** controls.
- You can support **keyboard and gamepad** together.
- Your code stays clean, and you can change keys without editing scripts.

For phones, add **on-screen buttons or a virtual joystick** that trigger the same actions."""),
        ("Top-down movement with velocity", """A character body has a **velocity:** how fast it moves and in which direction. You change velocity, and the engine moves the body and handles collisions:

> [GDScript]
> extends CharacterBody2D
>
> const SPEED := 220.0
> const ACCEL := 1400.0
> const FRICTION := 1800.0
>
> func _physics_process(delta: float) -> void:
>     var dir := Input.get_vector("move_left", "move_right", "move_up", "move_down")
>     if dir != Vector2.ZERO:
>         velocity = velocity.move_toward(dir * SPEED, ACCEL * delta)
>     else:
>         velocity = velocity.move_toward(Vector2.ZERO, FRICTION * delta)
>     move_and_slide()

Use `_physics_process` for movement because it runs at a fixed rate, which keeps physics stable. **Acceleration** and **friction** stop the character from snapping to full speed and give a sense of weight. Higher acceleration feels tight and responsive, lower feels slippery."""),
        ("Platformer: gravity and jumping", """A side-on platformer adds **gravity** and a jump:

> [GDScript]
> const SPEED := 260.0
> const JUMP_VELOCITY := -520.0
> const GRAVITY := 1500.0
>
> func _physics_process(delta: float) -> void:
>     if not is_on_floor():
>         velocity.y += GRAVITY * delta
>     var x := Input.get_axis("move_left", "move_right")
>     velocity.x = move_toward(velocity.x, x * SPEED, 1800.0 * delta)
>     if Input.is_action_just_pressed("jump") and is_on_floor():
>         velocity.y = JUMP_VELOCITY
>     move_and_slide()

In 2D screens, **negative y points up** in Godot. Gravity adds to downward speed every frame. Jumping sets an upward velocity. Tune **JUMP_VELOCITY** and **GRAVITY** together: a stronger gravity with a stronger jump feels snappy, and weak gravity feels floaty."""),
        ("Making jumps feel good", """Professional platformers add small kindnesses that players never notice but always feel:

1. **Coyote time:** allow a jump for about 0.1 seconds after walking off a ledge.
2. **Jump buffering:** if the player presses jump slightly **before** landing, jump as soon as they land.
3. **Variable jump height:** if the player releases the button early, cut the upward speed, so a tap gives a short hop and a hold gives a full jump.
4. **Faster falling:** apply extra gravity when falling so the jump feels crisp.
5. **Corner correction:** nudge the player around a block's edge when they almost fit.

> [GDScript: variable jump height]
> if Input.is_action_just_released("jump") and velocity.y < 0:
>     velocity.y *= 0.4

Each trick is a few lines, but together they make controls feel forgiving and fair."""),
        ("Tuning, testing and accessibility", """Movement is tuned by playing, not by thinking:

- **Expose numbers** as variables (`@export var speed := 220.0`) so you can change them while the game runs.
- Keep a **test room** with gaps, steps and walls, to try jumps and turns quickly.
- Ask others to play and say how it **feels,** such as floaty, heavy or sticky, then change one number at a time.
- **Record your best values** so you can go back.
- Check **frame rate independence:** the feel should be the same on slow and fast computers, because you use `delta`.
- Offer **accessibility:** remappable keys, one-handed options and an optional auto-run.
- On phones, test with real thumbs. Controls must not be hidden under fingers, and buttons need generous size.

Unity uses `Rigidbody2D` or `CharacterController`, and GameMaker uses `hspeed` and `vspeed`, but coyote time and acceleration work the same everywhere."""),
    ],
    diagram=flow([("Input", "actions, not keys"), ("Direction", "normalised vector"), ("Velocity", "speed up, slow"), ("Move", "move_and_slide"), ("Feel", "tune and test")], "g12", note="Change velocity, let the engine move the body."),
    caption="Read actions, build a direction, change velocity, let the engine move and collide, then tune the feel by playing.",
    terms=[("Input action", "A named control such as jump that can be mapped to any key or button."), ("Velocity", "How fast and in which direction something moves."),
           ("Acceleration", "How quickly velocity changes towards a target speed."), ("Coyote time", "A short grace period for jumping after leaving a ledge."),
           ("Jump buffering", "Remembering an early jump press and applying it on landing."), ("Normalised vector", "A direction scaled to length one so diagonals are not faster.")],
    mistakes=["Hardcoding specific keys in scripts.", "Moving diagonally faster than straight.", "Putting physics movement in the wrong function, so it jitters.", "Never tuning acceleration and jump numbers by playing."],
    quiz=[dict(q="Why use input actions instead of hardcoded keys?", o=["Players can remap controls and one script supports keyboard and gamepad", "They are faster", "They hide bugs", "They need no code"], a=0,
               why="Actions separate what the player means from the physical key."),
          dict(q="What is coyote time?", o=["A slow enemy", "A short grace period to jump after leaving a ledge", "A sound effect", "A loading screen"], a=1,
               why="It forgives late jumps and makes controls fair."),
          dict(q="Which function should run physics movement in Godot?", o=["_ready", "_physics_process", "_exit_tree", "_draw"], a=1,
               why="_physics_process runs at a steady rate suited to physics."),
          dict(q="What makes a variable-height jump?", o=["Reducing upward speed when the button is released early", "Adding more enemies", "Deleting gravity", "Using bigger sprites"], a=0,
               why="Cutting the upward velocity gives short hops on a tap and full jumps on a hold.")],
    activity="Build a movement test room with a character that has acceleration, friction, a jump with coyote time and jump buffering. Change five numbers one at a time and write down how each changes the feel.",
)

LESSONS[13] = dict(   # Collisions, physics and triggers
    minutes=17,
    hook="When a coin vanishes the moment the player touches it, when a spike hurts, when a crate slides, when a door opens as you step near it, the engine is answering one question thousands of times a second: who is touching whom? Collision handling is the quiet machinery behind almost every game rule. Done well, it is invisible. Done badly, players fall through floors, get hit by things that missed them by a mile, or shoot straight through thin walls. In this lesson you will learn the difference between solid bodies and trigger areas, how collision layers and masks keep your rules tidy, how to react with signals, how raycasts let a game look ahead, and how to debug the strange problems that every developer meets.",
    sections=[
        ("Bodies, areas and shapes", """Most engines split collision objects into two families:

- **Solid bodies** (in Godot: `StaticBody2D`, `CharacterBody2D`, `RigidBody2D`) that **block** each other. Walls, floors, players and crates.
- **Areas / triggers** (`Area2D`) that **detect** overlap but do not block. Coins, damage zones, doors, checkpoints and cameras zones.

Each needs a **shape:** a rectangle, circle or polygon that defines its physical outline. Keep shapes **simple and slightly smaller** than the sprite, so touching feels fair. A player hitbox slightly smaller than the picture is forgiving, while an enemy hitbox slightly larger than the attack picture is unfair. In Unity, the same ideas are **colliders** and the **Is Trigger** checkbox."""),
        ("Layers and masks: who sees whom", """Without organisation, everything collides with everything. **Layers** say **what an object is,** and **masks** say **what it looks for.**

> [Example layers]
> Layer 1 = World   Layer 2 = Player   Layer 3 = Enemy   Layer 4 = Player bullets   Layer 5 = Pickups

- The **player** sits on layer Player and its mask is World, Enemy and Pickups.
- A **player bullet** sits on Player bullets and its mask is World and Enemy, so it never hits the player who fired it.
- An **enemy** sits on Enemy and its mask is World and Player bullets.

Name your layers in project settings so the inspector shows readable labels. A well-planned layer table prevents a whole category of bugs, and it is faster, because the engine skips pairs that cannot interact."""),
        ("Reacting to a trigger with signals", """Triggers tell you when something enters through a **signal:** a message the engine sends when an event happens. A coin:

> [GDScript]
> extends Area2D
>
> signal collected(value: int)
> @export var value := 1
>
> func _ready() -> void:
>     body_entered.connect(_on_body_entered)
>
> func _on_body_entered(body: Node2D) -> void:
>     if body.is_in_group("player"):
>         collected.emit(value)
>         queue_free()

The coin does not know about the score system. It just **announces** that it was collected. Another script, such as the HUD or score manager, listens. This **loose coupling** keeps code tidy. Use **groups** (`add_to_group("player")`) to identify objects by role instead of checking names, and use `queue_free()` to remove an object safely at the end of the frame."""),
        ("Raycasts, sensors and moving things", """A **raycast** shoots an invisible line and reports the first thing it hits. Uses:

- **Ground and wall checks** under a character's feet.
- **Line of sight:** can the enemy see the player, or is a wall in the way?
- **Instant weapons** such as lasers and hitscan guns.
- **Mouse picking** and interaction ranges.

Other physics ideas worth knowing:

- **Tunnelling:** a fast, small object can jump over a thin wall between frames. Fix with thicker walls, slower speed, continuous collision detection or a raycast in front of the bullet.
- **One-way platforms:** can be jumped through from below but stood on from above, with a simple option on the shape.
- **Moving platforms:** carry the player along, move them in `_physics_process`, and let the engine pass the motion to the body standing on them.
- **Physics bodies (rigid bodies)** are good for crates, balls and ragdolls, but are harder to control. For player and enemies, a character body with your own movement code gives more predictable results."""),
        ("Debugging collisions", """When something passes through a wall or a coin refuses to collect, check:

1. **Turn on visible collision shapes** (in Godot, the Debug menu, Visible Collision Shapes). Most problems become obvious: the shape is missing, the wrong size or in the wrong place.
2. **Check layers and masks** on **both** objects.
3. **Check the shape is enabled** and the node has a shape assigned.
4. **Check scale:** non-uniform scaling can distort shapes. Scale the sprite, not the body.
5. **Check you move in the physics step** and not only through teleporting the position.
6. **Print the signal arguments** to see exactly who is colliding.
7. **Keep shapes simple.** Dozens of tiny shapes slow the game, especially on cheap phones.

Make a **collision test scene** with walls, a moving platform, a coin, a spike and a fast bullet. When you change physics settings, run the test scene again."""),
    ],
    diagram=compare(("SOLID BODY", ["Blocks other bodies", "Walls, floors, players", "Moves with move_and_slide", "Used for rules of space"]), ("AREA / TRIGGER", ["Detects overlap only", "Coins, spikes, doors", "Fires signals on enter", "Used for rules of events"]), vs="vs", note="Layers and masks decide who sees whom."),
    caption="Solid bodies block movement, areas detect events. Layers and masks keep the interactions organised.",
    terms=[("Collision shape", "The simple outline an object uses for collision tests."), ("Trigger", "An area that detects overlap without blocking movement."),
           ("Collision layer", "The group an object belongs to for collision purposes."), ("Collision mask", "The layers an object looks for when testing collisions."),
           ("Signal", "A message an object sends when something happens."), ("Raycast", "An invisible line that reports the first object it hits.")],
    mistakes=["Making every object collide with every other object.", "Making the player's hitbox larger than the picture.", "Letting fast bullets pass through thin walls.", "Never turning on visible collision shapes when debugging."],
    quiz=[dict(q="What is the difference between a body and an area?", o=["A body blocks movement, an area only detects overlap", "They are the same", "Areas are for sound only", "Bodies are invisible"], a=0,
               why="Solid bodies block, areas detect, so coins and doors are areas."),
          dict(q="What does a collision mask define?", o=["The colour of the object", "Which layers the object looks for", "Its speed", "The sound"], a=1,
               why="Layer is what an object is, mask is what it checks against."),
          dict(q="Why can a fast bullet pass through a thin wall?", o=["Tunnelling: it moves past the wall between two frames", "The wall is magic", "Gravity is off", "The sprite is blue"], a=0,
               why="Fast small objects can skip over thin colliders."),
          dict(q="What is the first debugging step for a collision bug?", o=["Reinstall the engine", "Turn on visible collision shapes", "Delete the scene", "Change the music"], a=1,
               why="Seeing the shapes usually shows the problem straight away.")],
    activity="Build a collision test scene with a player, a wall, a coin, a spike, a moving platform and a fast bullet. Set up named layers and masks so the bullet cannot hit the player, then turn on visible collision shapes and fix any problem.",
)

LESSONS[14] = dict(   # Game state, saving and loading
    minutes=17,
    hook="A player spends two hours in your game, closes the app to answer a phone call and returns to find everything gone. Few things feel worse, and few things get a game deleted faster. Saving seems like a simple feature, but it touches almost every part of a game: which information counts as the state, where files are stored, what happens when you update the game and the old save no longer fits, and how to stop a corrupted file from ruining someone's progress. It also covers the larger state of the game, whether it is in the menu, playing, paused or over. In this lesson you will learn to organise game state, write and read save files in JSON, handle versions and errors, and think about cheating and privacy.",
    sections=[
        ("Two kinds of state", """**State** is the information that describes the game at one moment. There are two levels:

- **Game flow state:** which mode you are in, such as `MENU`, `PLAYING`, `PAUSED`, `GAME_OVER` and `CUTSCENE`. Each mode decides what is visible, which input is accepted and whether time runs.
- **World and player state:** health, position, score, inventory, unlocked levels, settings and which doors are open.

Keep both in **clear, central places,** not scattered across a hundred scripts. In Godot, an **autoload** (a global singleton node) such as `GameState` can hold the data and emit signals when it changes. In Unity, a persistent manager object does the same job."""),
        ("A flow-state machine", """A small, tidy way to manage modes:

> [GDScript: autoload GameFlow]
> extends Node
>
> enum State { MENU, PLAYING, PAUSED, GAME_OVER }
> var state: State = State.MENU
> signal state_changed(new_state: State)
>
> func change_state(new_state: State) -> void:
>     if new_state == state:
>         return
>     state = new_state
>     get_tree().paused = (state == State.PAUSED)
>     state_changed.emit(state)

Menus, the HUD and music listen to `state_changed` and react. Pausing is one line, because the engine can freeze the scene tree. Use **only legal transitions** (you cannot go from `GAME_OVER` to `PAUSED`), and your code stays predictable."""),
        ("Saving to a file", """Store what you need to **rebuild** the game, not everything. A simple, readable format is **JSON:**

> [GDScript]
> const SAVE_PATH := "user://save.json"
>
> func save_game(data: Dictionary) -> void:
>     var file := FileAccess.open(SAVE_PATH, FileAccess.WRITE)
>     if file == null:
>         push_error("Could not open save file")
>         return
>     file.store_string(JSON.stringify(data))
>
> func load_game() -> Dictionary:
>     if not FileAccess.file_exists(SAVE_PATH):
>         return {}
>     var text := FileAccess.get_file_as_string(SAVE_PATH)
>     var parsed = JSON.parse_string(text)
>     return parsed if parsed is Dictionary else {}

`user://` is a safe folder that the engine maps to the right place on each platform, including Android, iOS and the web. Never write into the game's install folder, because it is often read-only. Save **simple values** (numbers, text, lists), plus identifiers such as `"level": "forest_2"` instead of references to objects."""),
        ("Versions, errors and safety", """Real games need defences:

1. **Add a version number** to every save (`"version": 2`). When you change the format, write a small function that upgrades old saves instead of breaking them.
2. **Use defaults** for missing keys, so a save from an older version still loads.
3. **Handle corrupt files:** if parsing fails, tell the player, and keep a backup copy (`save.bak`) from the last good save.
4. **Write safely:** save to a temporary file and then rename it, so a crash in mid-write cannot destroy the only copy.
5. **Autosave at safe moments:** checkpoints, level ends and when the app goes to the background, which on phones may be the only warning you get before the system closes it.
6. **Offer several slots** if players may want to try different choices.

On the **web,** saves live in the browser's storage, which a player can clear, so tell them. For **cloud saves,** use the platform's service rather than building your own."""),
        ("Settings, cheating and privacy", """A few more points:

- **Settings** (volume, controls, language) belong in a separate small file, so they survive deleting a save.
- **Cheating:** in a single-player game, players editing their own save harm only themselves, so do not waste time on heavy protection. In **online games** with scores or prizes, never trust the client: the **server** must check results.
- **Do not store sensitive data** in a save: no passwords, no payment details.
- **Personal data:** if you collect names, emails or anything identifying, for leaderboards or accounts, treat it under **Nigeria's NDPA 2023** and the privacy rules of the stores you publish in. Collect the minimum, say why, and let players delete it.
- **Test saving** at every stage: new game, mid-level, after an update and with the save file deleted.

A reliable save system is invisible when it works and a disaster when it fails, so it deserves real testing."""),
    ],
    diagram=flow([("Menu", "pick play"), ("Playing", "time runs"), ("Paused", "time frozen"), ("Game over", "show result")], "g14", loop=True, note="Allow only legal transitions."),
    caption="A flow state machine: menu, playing, paused and game over, with only the legal transitions allowed.",
    terms=[("Game state", "The information that describes the game at one moment."), ("Autoload", "A Godot node that is always available globally, such as a game manager."),
           ("JSON", "A simple text format for storing structured data."), ("Save version", "A number in the save file that lets newer code upgrade older saves."),
           ("Autosave", "Saving automatically at safe moments."), ("Corrupt save", "A damaged file that cannot be read correctly.")],
    mistakes=["Scattering game state across dozens of scripts.", "Writing saves into the read-only install folder.", "Overwriting the only save without a backup.", "Changing the save format with no version number."],
    quiz=[dict(q="Why add a version number to a save file?", o=["To make it bigger", "So newer code can upgrade older saves", "To hide it", "To speed up graphics"], a=1,
               why="Updates often change the format, and versions let you migrate old saves."),
          dict(q="Where should a Godot game write save files?", o=["The install folder", "user://", "The desktop only", "An email"], a=1,
               why="user:// maps to a safe writable location on each platform."),
          dict(q="How can you protect against a crash during saving?", o=["Write to a temporary file, then rename it", "Save twice in the same file", "Never save", "Turn off the screen"], a=0,
               why="A temporary file plus rename leaves the old save intact if the write fails."),
          dict(q="In an online game with prizes, who must check results?", o=["The player's device", "The server", "Nobody", "The sound system"], a=1,
               why="The client can be modified, so the server must verify.")],
    activity="Add a save and load system to a small game that stores the level, score and settings in JSON with a version number. Add a backup copy, test with a deleted and a damaged file, and add a pause state.",
)

LESSONS[15] = dict(   # Enemies and simple AI
    minutes=17,
    hook="An enemy does not need to be intelligent. It needs to look intelligent, be readable and be fair. The ghosts in a classic maze game follow just a few simple rules, yet players talk about their personalities. A guard who patrols, notices you, chases and gives up creates a story with very little code. The existing lessons introduced enemies and state machines. In this lesson you go further: how enemies sense the world, how they choose between actions, how they find a path around obstacles, how to give different enemies different personalities and how to keep them fair, so that losing feels like the player's mistake and not the game's cheating.",
    sections=[
        ("Sense, think, act", """Almost all game AI follows one loop:

1. **Sense:** gather information, such as the player's position, distance, whether there is a wall in between and the enemy's own health.
2. **Think (decide):** choose what to do with simple rules.
3. **Act:** move, attack, flee or call for help.

> [GDScript: a decision in a few lines]
> var to_player := player.global_position - global_position
> if to_player.length() < attack_range:
>     state = State.ATTACK
> elif to_player.length() < sight_range and can_see_player():
>     state = State.CHASE
> else:
>     state = State.PATROL

Run the sensing a few times per second instead of every frame, to save work and to give **natural reaction delay,** so enemies do not feel like perfect machines."""),
        ("Patrol, chase and line of sight", """Three behaviours build a believable guard:

- **Patrol:** walk between two or more points, and wait a moment at each.
- **Chase:** move towards the player when seen.
- **Search or give up:** if the player escapes, go to the **last seen position,** look around, then return to patrol.

**Line of sight** uses a raycast from the enemy to the player. If a wall is hit first, the enemy cannot see. A **vision cone** (only seeing in front, within an angle) adds stealth gameplay. Add **hearing** with a noise radius when the player runs.

> [GDScript: can the enemy see the player?]
> func can_see_player() -> bool:
>     var space := get_world_2d().direct_space_state
>     var query := PhysicsRayQueryParameters2D.create(global_position, player.global_position)
>     query.exclude = [self]
>     var hit := space.intersect_ray(query)
>     return hit.is_empty() or hit.collider == player"""),
        ("Pathfinding around obstacles", """Moving straight at the player fails when walls are in the way. **Pathfinding** finds a route:

- **A-star** is the classic algorithm. It searches a graph of points or grid cells and finds the shortest route efficiently.
- **Navigation meshes** describe the walkable area. In Godot, a `NavigationRegion2D` and a `NavigationAgent2D` do the work for you:

> [GDScript]
> @onready var agent: NavigationAgent2D = $NavigationAgent2D
>
> func _physics_process(delta: float) -> void:
>     agent.target_position = player.global_position
>     var next := agent.get_next_path_position()
>     velocity = (next - global_position).normalized() * speed
>     move_and_slide()

Recalculating the path every frame is wasteful. Update the target **a few times per second.** On weak phones, limit how many enemies pathfind at once. For flocks, add **steering:** keep a distance from neighbours so enemies do not stack on top of each other."""),
        ("Variety: personalities from parameters", """You can make many enemies from one script by changing **parameters:**

- **Speed, sight range and reaction time.**
- **Aggression:** attacks at once, or waits for an opening.
- **Preferred distance:** melee rushers, ranged shooters who keep away.
- **Group roles:** one distracts while another flanks.
- **Weaknesses:** slow after attacking, weak from behind, afraid of light.

The maze ghosts show this beautifully: one chases directly, one aims ahead of the player, one ambushes and one wanders. Four tiny rule changes create four personalities. Store parameters in **resource files** or data tables, so you can tune enemies without editing code, and so designers can create new variants."""),
        ("Fair AI and boss fights", """AI should challenge, not cheat. Fairness rules:

1. **Telegraph attacks.** A wind-up animation, a flash or a sound (the **tell**) gives the player time to react. About 0.3 to 0.6 seconds is typical for a fast attack.
2. **Do not hit through walls** or from off-screen with no warning.
3. **Cap how many enemies attack at once.** Let others circle and wait, so the player faces a fair number.
4. **Make mistakes:** a small random delay and imperfect aim make enemies feel alive.
5. **Show state:** an exclamation mark when alerted, a question mark when searching.
6. **Use difficulty settings** to change reaction time, damage and aggression, not to give enemies hidden advantages.

**Boss fights** are sequences of patterns: each phase has two or three attacks, a pause that invites a counter-attack, and a change in pattern as health falls. Test with fresh players, and ask whether deaths felt fair."""),
    ],
    diagram=tree("ENEMY BRAIN", [("Sense", ["Distance", "Line of sight", "Noise"]), ("Decide", ["Patrol", "Chase", "Attack", "Give up"]), ("Act", ["Move or path", "Attack with a tell", "Call for help"])], note="Simple rules can look smart."),
    caption="Enemy AI senses the world, decides with simple rules and acts, using a tell so attacks stay fair.",
    terms=[("Line of sight", "Whether an enemy can see the player without a wall in the way."), ("Pathfinding", "Finding a route around obstacles to a target."),
           ("A* (A-star)", "A classic algorithm that finds the shortest path efficiently."), ("Navigation mesh", "A map of the walkable area used for pathfinding."),
           ("Tell", "A visible or audible warning before an attack."), ("Steering", "Adjusting movement to avoid obstacles and crowding.")],
    mistakes=["Making enemies perfect, with instant reactions and aim.", "Attacking with no warning or tell.", "Recalculating paths every single frame for many enemies.", "Letting five enemies attack at once from all sides."],
    quiz=[dict(q="What is a tell?", o=["A save file", "A sound bug", "A visible or audible warning before an attack", "A score"], a=2,
               why="Tells let the player react, which makes defeat feel fair."),
          dict(q="What does a raycast between enemy and player check?", o=["The score", "Whether a wall blocks the line of sight", "The volume", "The frame rate"], a=1,
               why="If something else is hit first, the enemy cannot see the player."),
          dict(q="Which is a good way to create enemy variety cheaply?", o=["Change parameters such as speed, range and aggression", "Rewrite the script each time", "Remove all enemies", "Use only one speed"], a=0,
               why="One script with different parameters can give many personalities."),
          dict(q="Why add a small reaction delay?", o=["To slow the computer", "So enemies feel less like perfect machines", "To save the game", "To hide bugs"], a=1,
               why="A short delay makes enemies feel natural and beatable.")],
    activity="Build a guard who patrols between points, sees the player with a raycast, chases with pathfinding, searches the last seen position and then returns. Add a visible alert icon and a 0.4 second tell before its attack.",
)

LESSONS[16] = dict(   # Health, scoring, inventory and progression
    minutes=17,
    hook="Numbers give a game its memory. Health says how close you are to failing, score says how well you are doing, an inventory says what you own and experience says how far you have come. They look like simple counters, but how you design and store them affects almost everything else: how fair the game feels, how players plan, and how easy your code is to change. The earlier foundation covered the idea of health and score. In this lesson you will build them properly as reusable parts, design an inventory that can hold stacks of items, and create a progression curve of levels and unlocks that keeps players moving forward without grinding.",
    sections=[
        ("A reusable health component", """Health is needed by the player, enemies, crates and even doors. Instead of copying code, build one **health component** you can add to anything:

> [GDScript]
> class_name Health
> extends Node
>
> signal changed(current: int, maximum: int)
> signal died
>
> @export var maximum := 100
> var current := maximum
>
> func take_damage(amount: int) -> void:
>     current = max(current - amount, 0)
>     changed.emit(current, maximum)
>     if current == 0:
>         died.emit()
>
> func heal(amount: int) -> void:
>     current = min(current + amount, maximum)
>     changed.emit(current, maximum)

The component only manages the number and announces changes. The **HUD** listens to `changed` to update the bar. The **owner** listens to `died` to play an animation and disappear. Add **invincibility frames** after a hit so the player is not killed by one touch repeated sixty times a second."""),
        ("Damage, armour and feedback", """A hit should be **felt:**

- **Flash** the sprite white or red, with a short **screen shake** for big hits.
- **Knock back** the target a little, and add a **hit pause** of a few frames.
- **Play a sound** that differs for light and heavy hits.
- **Show numbers** floating up if the game is about stats.

For the numbers, keep formulas simple and readable: `damage = attack - defence`, with a **minimum of 1** so armour never makes damage zero. Types such as fire and water can give multipliers (2 times, 0.5 times). Add a small **random range** (such as 90% to 110%) only if it improves the game. Display everything the player needs to plan, such as enemy health bars or clear states."""),
        ("Score and rewards", """Scoring tells players how well they did and gives them something to beat:

- **Reward skill and risk,** not only time spent: bonuses for speed, accuracy and avoiding damage.
- **Combos:** chaining actions within a time window multiplies points, so players aim for streaks.
- **Show the score clearly,** and let it **count up** with a satisfying sound.
- **Save the high score,** and show it on the game over screen with “New record!”.
- **Use stars or ranks** (bronze, silver, gold) so even beginners have a goal.
- **Leaderboards** add competition, but need a server and anti-cheat checks, and they raise privacy duties if you store names.

Be careful with **rewards that encourage harm to the player,** such as pushing people to play for hours. Design for fun and healthy breaks."""),
        ("Designing an inventory", """An inventory is a list of items with amounts. A beginner-friendly design:

- Define each item as **data:** an id, name, icon, description, maximum stack and effect, stored as a **resource** or table.
- The inventory stores **only ids and counts:**

> [GDScript]
> var items: Dictionary = {}   # item_id -> amount
>
> func add_item(id: String, amount: int = 1) -> void:
>     items[id] = items.get(id, 0) + amount
>     changed.emit()
>
> func remove_item(id: String, amount: int = 1) -> bool:
>     if items.get(id, 0) < amount:
>         return false
>     items[id] -= amount
>     if items[id] == 0:
>         items.erase(id)
>     changed.emit()
>     return true

Then add **limits** (slots or weight) if the game needs scarcity, **stacking** for ammunition and potions, and **equipment slots** (weapon, armour) that change the player's stats. Because the inventory is only ids and numbers, it **saves and loads** easily as JSON. The user interface is a separate scene that reads the data and shows it."""),
        ("Progression: levels, unlocks and curves", """Progression keeps players coming back. Common tools:

1. **Experience and levels:** the next level costs more than the last, such as `xp_needed = 100 * level ** 1.5`. Players should level quickly at first and more slowly later.
2. **Unlocks:** new levels, characters or abilities that appear when a goal is met.
3. **Upgrades:** spend coins on a stronger jump or bigger magnet.
4. **Mastery:** harder challenges for those who want them, such as time trials.
5. **Story and exploration:** a map that fills in, secrets that reward curiosity.

Watch for **grind:** if the player must repeat the same dull action to progress, redesign it. Watch for **runaway power,** where upgrades make the game trivial, and plan the **numbers in a spreadsheet** before coding, so you can see how long each level takes. Always test whether progress **feels** earned and whether the player can always see the next goal."""),
    ],
    diagram=bars([("Level 1", 100), ("Level 2", 283), ("Level 3", 520), ("Level 4", 800), ("Level 5", 1118)], note="Each level costs more experience than the last.", unit=" XP"),
    caption="An experience curve: each level asks for more experience than the last, so early progress feels fast and later progress feels earned.",
    terms=[("Health component", "A reusable piece that manages health for any object."), ("Invincibility frames", "A short time after a hit when more damage is ignored."),
           ("Combo", "A chain of actions that multiplies the reward."), ("Stack", "Several copies of an item held in one inventory slot."),
           ("Progression curve", "How quickly a player gains power or unlocks over time."), ("Grind", "Repeating a dull task only to progress.")],
    mistakes=["Copying health code into every object.", "Letting armour reduce damage to zero.", "Storing whole objects in the inventory instead of ids and counts.", "Designing progression numbers without testing how long they take."],
    quiz=[dict(q="Why make health a reusable component?", o=["It is shorter to write once and add to any object", "It makes the game slower", "It hides bugs", "It needs no code"], a=0,
               why="One tested component serves the player, enemies and objects."),
          dict(q="What should an inventory store?", o=["Whole copies of objects", "Item ids and counts", "Only images", "Nothing"], a=1,
               why="Ids and counts are simple to change, show and save."),
          dict(q="Why keep a minimum damage of 1?", o=["So high armour cannot make a character immune", "To speed up play", "To hide health", "To change colours"], a=0,
               why="A minimum keeps every hit meaningful."),
          dict(q="What is grind?", o=["A smooth animation", "Repeating a dull task only to progress", "A graphics setting", "A weapon"], a=1,
               why="Grind replaces decisions with repetition and bores players.")],
    activity="Build a health component with signals, a coin score with combos and a saved high score, and a small inventory with stacking. Then design a five-level XP table in a spreadsheet and test how long each level takes.",
)

LESSONS[17] = dict(   # Balancing difficulty and game feel
    minutes=17,
    hook="Two games can have exactly the same rules and the same levels, and one can feel wonderful while the other feels dead. The difference is often balance and feel: how hard the game is at each moment, and how it responds under the player's fingers. Balance decides whether players feel challenged or cheated. Game feel, sometimes called juice, decides whether a jump, a hit or a pickup feels powerful or flat. Neither can be solved by thinking alone, because both need testing and tuning with real people. In this lesson you will learn to shape difficulty curves, tune numbers from data, offer difficulty options kindly, and add the small touches, from screen shake to squash and stretch, that make a game feel good.",
    sections=[
        ("The difficulty curve", """Difficulty should rise like a staircase with landings, not like a wall:

- **Start easy** so everyone can succeed in the first minutes.
- **Introduce one new thing at a time,** then combine things.
- **Add rest points** after hard sections, so players can breathe.
- **Raise the peak gradually,** with a final challenge that tests everything learned.
- **Let mastery show:** players should feel they got better, because the same challenge becomes easy later.

A typical shape is a **sawtooth:** difficulty climbs, drops a little at a new area where something new is taught, then climbs higher. Avoid **difficulty spikes,** where one section is far harder than the one before. If testers all fail at the same place, the spike is yours to fix, not theirs to endure."""),
        ("Tuning numbers with data", """Balance is a numbers job, and numbers can be tested:

1. **Put values in one place:** a spreadsheet or a data file with enemy health, damage, speed, spawn rates, prices and rewards.
2. **Define target experiences:** “A new player should win level one in about 90 seconds, and fail twice in level five.”
3. **Change one value at a time,** then replay. If you change five, you will not know which one worked.
4. **Measure:** log how long levels take, where players die, which items are bought and where people quit. Even a simple counter helps. Tell players if you collect analytics, and respect privacy rules.
5. **Compare options:** if one weapon is used by 90% of players, it is too strong or the others are too weak.
6. **Test with different skill levels,** and keep an eye on people who struggle.

Use **ratios** to reason: an enemy that dies in 3 hits and kills the player in 5 hits creates a fair fight. Change either number and the whole feel changes."""),
        ("Difficulty options and kindness", """Players differ in skill, time and ability. Respect that:

- **Offer modes,** such as Easy, Normal and Hard, that change numbers like enemy damage, health and the time to react.
- **Never insult the player** for choosing Easy. Use friendly names, such as “Story” and “Challenge.”
- **Assist features:** slower game speed, more checkpoints, aim assist, colour-blind options and remappable controls.
- **Dynamic difficulty** can help: after several deaths in a row, quietly offer more health pickups. Do it gently and never in a way that feels like cheating.
- **Do not hide the rules.** Even in the hardest mode, a fair game tells the player what is dangerous.

Accessibility makes your game playable by more people, which means more players and more feedback."""),
        ("What game feel is made of", """Game feel is the sense of how a game responds. Its ingredients are small:

- **Responsiveness:** input should produce a visible reaction in **less than about 100 ms.** On phones, avoid heavy work that causes delay.
- **Anticipation and follow-through:** a short wind-up before a swing and a settle after it.
- **Squash and stretch:** a character stretches when jumping and squashes when landing.
- **Screen shake:** a quick jolt for big hits or explosions, always small and short.
- **Hit stop:** freeze the game for 2 to 6 frames when a hit lands, so impact feels heavy.
- **Particles:** dust on landing, sparks on hits and trails on fast things.
- **Sound that matches:** a sharp sound at the exact frame of contact.
- **Easing:** objects speed up and slow down smoothly, not at constant speed.

Use them with care. Too much shaking and flashing becomes unpleasant, and flashing can hurt people with photosensitive epilepsy, so offer an option to reduce effects."""),
        ("Game feel in code", """Small helpers go a long way in Godot:

> [GDScript: squash and stretch with a tween]
> func squash() -> void:
>     var tween := create_tween()
>     tween.tween_property($Sprite2D, "scale", Vector2(1.3, 0.7), 0.05)
>     tween.tween_property($Sprite2D, "scale", Vector2.ONE, 0.12) \\
>         .set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)

> [GDScript: camera shake]
> extends Camera2D
> var strength := 0.0
>
> func shake(amount: float) -> void:
>     strength = amount
>
> func _process(delta: float) -> void:
>     strength = lerpf(strength, 0.0, 10.0 * delta)
>     offset = Vector2(randf_range(-1, 1), randf_range(-1, 1)) * strength

> [GDScript: hit stop]
> func hit_stop(seconds := 0.06) -> void:
>     Engine.time_scale = 0.05
>     await get_tree().create_timer(seconds, true, false, true).timeout
>     Engine.time_scale = 1.0

The last argument of `create_timer` makes the timer ignore the slowed time, so it ends on schedule. Add effects **one at a time,** play, and keep only those that improve the game. Add a setting to turn shake and flashes down."""),
    ],
    diagram=timeline([("Easy start", "everyone succeeds"), ("Teach", "one new idea"), ("Test", "use it under pressure"), ("Rest", "a breather"), ("Twist", "combine ideas"), ("Peak", "final challenge")], note="A sawtooth, not a wall."),
    caption="A healthy difficulty curve: teach, test, rest and twist, rising to a final challenge.",
    terms=[("Difficulty spike", "A sudden jump in challenge that many players fail at."), ("Sawtooth curve", "Difficulty that rises, drops slightly at a new teaching moment, then rises higher."),
           ("Dynamic difficulty", "Adjusting the challenge quietly based on how the player performs."), ("Hit stop", "A brief freeze when a hit lands to make it feel heavy."),
           ("Squash and stretch", "Changing a shape to show weight and speed."), ("Easing", "Smooth speeding up and slowing down of motion.")],
    mistakes=["Changing many balance numbers at once.", "Ignoring the place where all testers fail.", "Adding too much shake and flashing, with no option to turn it down.", "Giving enemies hidden advantages instead of adjusting fair numbers."],
    quiz=[dict(q="What is a difficulty spike?", o=["A sudden jump in challenge that many players fail at", "A fast character", "A reward", "A new menu"], a=0,
               why="Spikes cause frustration and players leaving."),
          dict(q="Why change one balance value at a time?", o=["To make testing slower", "So you know which change caused the result", "To hide bugs", "To save memory"], a=1,
               why="If you change many values, you cannot tell which one worked."),
          dict(q="What is hit stop?", o=["A brief freeze when a hit lands to add weight", "A save feature", "A sound setting", "An enemy type"], a=0,
               why="Freezing a few frames makes impacts feel powerful."),
          dict(q="Why offer an option to reduce screen shake and flashing?", o=["Rules forbid effects", "Some players are sensitive, including people with photosensitive epilepsy", "It saves disk space", "It improves sound"], a=1,
               why="Accessibility options make the game safe and comfortable for more people.")],
    activity="Pick one level of a game and write its target experience. Tune three numbers one at a time, record the results in a table and add screen shake, squash and hit stop with a setting to reduce them.",
)

LESSONS[18] = dict(   # Level design principles and flow
    minutes=16,
    hook="You are dropped into a new level with no tutorial text, no arrow and no voice telling you where to go, and yet you know. A bright tower on the horizon pulls you forward. A path of coins curves round a corner. A gap makes you slow down, because you can see a danger below. This is not luck. It is level design: the craft of shaping space so that players understand where they are, where to go and how to feel, without being told. The earlier lesson taught the teach, test and twist pattern and pacing. Here you will learn how to guide the eye, structure routes and secrets, gate progress with keys and abilities, measure your space so it works, and document levels so a team can build them.",
    sections=[
        ("Guiding the player without words", """Players follow what they notice. You can steer attention with:

- **Landmarks:** a tall tower, a glowing tree or a big statue that tells you where you are and where to go.
- **Light and colour:** people walk towards the brightest area, and warm colours draw the eye in a dark scene.
- **Leading lines:** roads, rivers, rails and rows of lamps point towards the goal.
- **Framing:** a doorway or arch around the exit, with the goal seen through it.
- **Motion and sound:** a waving flag, moving water or distant music.
- **Rewards as breadcrumbs:** a trail of coins or items.
- **Funnels:** wide space narrowing to a gate that shows the way.

If playtesters get lost, **add guidance, do not add text.** An arrow in the world is a last resort. A change of lighting is usually better."""),
        ("Routes, branches and secrets", """Think about the shape of the level as a **map of choices:**

- **The critical path** is the main route from start to finish. It must always be clear.
- **Side paths** offer optional rewards: extra health, a shortcut, a secret room.
- **Loops** let players return to a safe place by a new route, and **shortcuts** that open back to the start are deeply satisfying.
- **Hubs** connect several areas and make progress feel like a world and not a corridor.
- **Dead ends** should have a reason, such as a treasure or a story detail, so that exploring is rewarded and not punished.

**Linear levels** are easier to build and tune, and give better control of pacing. **Open levels** give freedom and need more guidance and testing. Choose the shape that fits your game and your time."""),
        ("Gates, keys and abilities", """Progress can be **gated** so players must achieve something before moving on:

- **Lock and key:** a door that needs a key found elsewhere.
- **Ability gates:** a high ledge that needs a double jump, a wall that needs a bomb. This is the heart of exploration games.
- **Skill gates:** a section that requires mastering a technique shown earlier.
- **Story gates:** a character who will not let you pass until you talk to someone.

Good gates are **visible before they are solvable:** the player sees the locked door early, and remembers it when the key appears. This creates **curiosity and goals.** Bad gates are invisible or unfair, such as a required item hidden with no hints. Always check that the **key is reachable** before the lock and that players can never get permanently stuck, or add a way to recover."""),
        ("Measure your space", """Levels must match the character's abilities. Use **metrics:**

1. Measure the **maximum jump height and distance** in your test room, then design gaps **below** that, with a safety margin for most challenges (about 70 to 80% of the maximum).
2. Mark the **run speed** and how far the player travels in one second.
3. Plan **camera visibility:** the player should see danger early enough to react.
4. Use a **grid** so everything aligns, and **greybox** the level with simple blocks first.
5. Place **checkpoints** before hard sections and after rewards.
6. **Test the critical path** many times, with a stopwatch, to learn how long the level takes.

Greybox testing is fast and cheap: if the level is fun with grey boxes, art will make it better. If it is boring, art will not rescue it."""),
        ("Document, test and iterate", """Treat each level as a small project:

- **Write a one-paragraph brief:** purpose, new skill taught, mood, length and gating.
- **Sketch the layout** on paper first, with the critical path, secrets and checkpoints.
- **Build in stages:** greybox, gameplay pass, art pass, polish.
- **Watch people play** without speaking. Note where they hesitate, get lost or die.
- **Use heatmaps** of deaths and positions, if you collect them, to find problems.
- **Cut ruthlessly:** a short, excellent level beats a long, uneven one.
- **Keep a level checklist:** can every item be reached, can the player be stuck, does it run well on the weakest phone?

A portfolio with three polished levels and their design notes shows employers real skill."""),
    ],
    diagram=hub(("LEVEL FLOW", "guide without words"), [("Landmarks", "tall and visible"), ("Light", "bright draws the eye"), ("Lines", "paths point the way"), ("Gates", "locks and abilities"), ("Rewards", "trails and secrets"), ("Rest", "safe places")], note="Show the way, do not tell it."),
    caption="Landmarks, light, lines, gates, rewards and rest points guide players through a level without any text.",
    terms=[("Critical path", "The main route a player must take from start to finish."), ("Landmark", "A memorable object that helps players find their position and direction."),
           ("Leading lines", "Shapes in the scene that point the player's eye towards a goal."), ("Ability gate", "A barrier that can only be passed once the player has a certain power."),
           ("Greybox", "A level built from simple blocks to test layout before art."), ("Shortcut", "A route that connects a later part of the level back to an earlier one.")],
    mistakes=["Explaining the way with text instead of using the level to guide.", "Designing gaps at the exact maximum jump distance.", "Hiding a required item with no hints.", "Building final art before testing the layout in grey boxes."],
    quiz=[dict(q="What is the critical path?", o=["The main route from start to finish", "The longest dead end", "A bug", "A secret room"], a=0,
               why="The critical path must always be clear to the player."),
          dict(q="Which is a good way to guide a lost player?", o=["A long paragraph of text", "Light, landmarks and leading lines", "Removing the map", "Hiding the goal"], a=1,
               why="Visual guidance works without interrupting play."),
          dict(q="What is an ability gate?", o=["A barrier passable only with a certain power, such as a double jump", "A loading screen", "A pause menu", "A music change"], a=0,
               why="Ability gates create goals that come back when the power is found."),
          dict(q="Why design most gaps well below the maximum jump distance?", o=["To make the game boring", "To leave a safety margin so jumps feel fair", "To waste space", "To hide enemies"], a=1,
               why="A margin accounts for imperfect timing and keeps challenges fair.")],
    activity="Draw a level on paper with a critical path, one side path, one gate, a shortcut and three checkpoints. Greybox it, measure gaps against your jump, and watch two people play without giving any hints.",
)

LESSONS[19] = dict(   # 2D art, sprites and animation for games
    minutes=16,
    hook="You do not need to be a great artist to make a game that looks good. Many successful small games use simple shapes, a tight set of colours and clear animation. What matters is consistency, readability and a few technical habits that save you hours: using the right size, a limited colour palette, neat sprite sheets and frames that read clearly at a glance. In this lesson you will learn the basics of 2D game art: choosing between pixel art and vector art, planning sizes and palettes, drawing a character with a handful of animation frames, packing sprite sheets, importing and playing animations in the engine, and getting art legally when you cannot draw it yourself.",
    sections=[
        ("Choose a style you can finish", """Pick a style that matches your skill and time:

- **Pixel art:** small images where each square pixel is visible. Fast to make, small files, and loved by players. Typical character sizes are **16 by 16, 32 by 32 or 64 by 64** pixels.
- **Flat vector or shapes:** clean, scalable shapes made in a vector tool. Easy to colour and resize.
- **Hand-drawn:** expressive, but each frame takes longer.
- **Cut-out animation:** a character built from separate parts (arms, legs, head) that you rotate in the engine. It needs fewer drawings.

Decide on **one style and keep it,** because mixing styles looks messy. Choose the **resolution** early, for example a 320 by 180 game screen scaled up, and keep all art to the same pixel scale. Most beginners should pick small pixel art or flat shapes, since they finish faster."""),
        ("Colour palettes and readability", """A **palette** is a limited set of colours. Using 8 to 32 colours makes art look unified and keeps you from agonising over choices. Free palette collections exist online, such as on **Lospec.** Rules for readable art:

1. **Silhouette first:** the player's shape should be recognisable even if filled with solid black.
2. **Contrast:** characters must stand out from the background. Make the background calmer and less saturated.
3. **Colour means something:** red for danger, yellow for pickups, green for safe, used consistently.
4. **Avoid too much detail** in small sprites. Every pixel counts.
5. **Test on a small, dim phone screen,** outdoors if you can, where many players will play.
6. **Think about colour-blind players:** do not rely on red versus green only. Add shapes or icons."""),
        ("Making animation frames", """Animation is a quick series of drawings. For a small game, you need only a few:

- **Idle:** 2 to 4 frames, a gentle breathing motion.
- **Run or walk:** 4 to 8 frames, in a loop.
- **Jump:** up, peak and fall, 2 to 3 frames.
- **Attack:** a wind-up, a strike and a recovery.
- **Hit and death:** short and clear.

The **12 principles of animation** help even at tiny sizes: timing, squash and stretch, anticipation, and so on. Fewer frames with strong poses beat many weak frames. Draw **key poses first,** then fill between. Check your loop plays smoothly at the speed the game will use, typically **8 to 12 frames per second** for pixel art. Free tools include **Piskel** (in the browser), **LibreSprite, Pixelorama, Krita** and **GIMP,** and **Aseprite** is a paid favourite. Check each tool's current licence and price."""),
        ("Sprite sheets and the engine", """A **sprite sheet** packs all frames into one image, in a grid. Advantages: fewer files, faster loading and easier management. Name the animations clearly.

In Godot:

1. Import the PNG into the project. For pixel art, set the texture filter to **Nearest** (Project Settings, Rendering, Textures, Default Texture Filter) so pixels stay sharp and not blurry.
2. Add an **AnimatedSprite2D** and create **SpriteFrames,** or use a **Sprite2D** with `hframes` and `vframes` and an **AnimationPlayer.**
3. Name the animations `idle`, `run` and `jump`.
4. Play them from code:

> [GDScript]
> func _physics_process(delta: float) -> void:
>     # ... movement code ...
>     if not is_on_floor():
>         $AnimatedSprite2D.play("jump")
>     elif absf(velocity.x) > 10.0:
>         $AnimatedSprite2D.play("run")
>         $AnimatedSprite2D.flip_h = velocity.x < 0.0
>     else:
>         $AnimatedSprite2D.play("idle")

Keep sheets at a **size that phones handle well,** and avoid huge images when small ones will do. Powers of two are no longer required in most engines, but keep it tidy."""),
        ("Getting art you do not have time to draw", """You can use assets made by others, with care:

- **Read the licence.** **CC0 / public domain** may be used freely. **CC BY** requires credit. Some licences forbid commercial use. Keep a **credits file** with the artist, source and licence for every asset.
- **Free asset sites** such as **OpenGameArt** and **itch.io** asset sections, and creators such as **Kenney,** offer many packs. Check the licence on each page, since it can change or differ between packs.
- **Paid assets** from stores are fine if the licence allows games like yours.
- **Never copy art from other games, anime, films or the web,** and never use AI-generated or traced images without checking the rules and rights. Stolen art can get your game removed and you sued.
- **Commission an artist:** write a clear brief, agree on price, deadline and **who owns the rights,** in writing. Nigerian artists and local communities are a wonderful source of unique work.
- **Credit everyone,** in the game and on the store page.

Using one pack consistently also keeps your game's style unified."""),
    ],
    diagram=flow([("Sketch", "shapes first"), ("Palette", "8 to 32 colours"), ("Frames", "key poses"), ("Sprite sheet", "pack in a grid"), ("Animate", "play in engine")], "g19", note="Small, consistent, readable."),
    caption="From sketch and palette to frames, a sprite sheet and an animation playing in the engine.",
    terms=[("Sprite", "A 2D image or animated picture used in a game."), ("Sprite sheet", "One image that contains many animation frames in a grid."),
           ("Palette", "A limited set of colours used throughout the art."), ("Silhouette", "The solid outline of a character, which should be recognisable."),
           ("Nearest filter", "A setting that keeps pixel art sharp when scaled up."), ("Licence", "The rules about how you may use someone else's asset.")],
    mistakes=["Mixing several art styles in one game.", "Using a blurry texture filter on pixel art.", "Using art from the internet without checking the licence.", "Forgetting to credit asset creators."],
    quiz=[dict(q="Why use a limited colour palette?", o=["It makes art look unified and decisions easier", "It uses more memory", "It hides bugs", "It makes sound louder"], a=0,
               why="A limited palette keeps the style consistent."),
          dict(q="What does a sprite sheet contain?", o=["Many animation frames in one image", "Only sound", "The code", "A save file"], a=0,
               why="Packing frames in one image is neat and efficient."),
          dict(q="Which texture filter keeps pixel art sharp?", o=["Linear", "Nearest", "Blur", "Smooth"], a=1,
               why="Nearest filtering avoids blurring when pixels are scaled up."),
          dict(q="What should you do before using a free asset?", o=["Ignore the licence", "Read the licence and note the credit requirements", "Remove the credits", "Resell it as your own"], a=1,
               why="Licences set the rules, and breaking them can remove your game from stores.")],
    activity="Draw a 32 by 32 character with idle, run and jump animations in a free tool using a palette of 16 colours. Make a sprite sheet, import it with a nearest filter, switch animations from code and write a credits file.",
)

LESSONS[20] = dict(   # Cameras, lighting and atmosphere
    minutes=16,
    hook="Two identical scenes can feel completely different: one cold and lonely, the other warm and safe. The change comes from the camera and the light. A camera decides what the player sees and how the world moves around them. Lighting and colour decide the mood, the importance of things and sometimes even the player's feelings, whether fear in a dark forest or comfort by a fire. In 2D games, a few simple tools can transform a flat scene: a smooth camera, parallax layers, coloured light, shadows, particles and a little post-processing. In this lesson you will learn to set up a good camera, scale for many screen sizes, build depth with parallax and add lighting and atmosphere while keeping the game fast enough for cheap phones.",
    sections=[
        ("A camera that helps the player", """The camera should help the player and stay out of the way:

- **Follow smoothly:** a camera that locks rigidly to the player feels harsh. Smoothing makes movement graceful.
- **Look ahead:** shift the view slightly in the direction the player is moving, so they see what is coming.
- **Dead zone:** the player can move a small distance in the centre before the camera follows.
- **Limits:** stop the camera at the edges of the level so it does not show empty space.
- **Zoom:** zoom out for exploring, in for focus. Keep changes smooth.
- **Shake:** a short jolt for impact, with an option to reduce it.

> [GDScript: a smooth Godot camera]
> extends Camera2D
>
> func _ready() -> void:
>     position_smoothing_enabled = true
>     position_smoothing_speed = 6.0
>     limit_left = 0
>     limit_top = 0
>     limit_right = 3200
>     limit_bottom = 720

Make the camera a **child of the player** or make it follow the player's position, and test on a real phone to check that movement does not cause eye strain."""),
        ("Many screens, one game", """Players have phones, tablets, laptops and TVs with different shapes. Plan for this early:

1. Choose a **base resolution,** for example 1280 by 720 (or smaller for pixel art).
2. Set the **stretch mode** in project settings so the game scales: in Godot, `canvas_items` for smooth scaling or `viewport` for pixel-perfect scaling, with an aspect setting such as `keep` or `expand`.
3. **Anchor the user interface** to the corners and edges so buttons stay in reach on tall, narrow phones.
4. Keep **important gameplay in the safe area,** away from notches and rounded corners.
5. Decide **landscape or portrait** and lock it, if the game is built for one.
6. **Test** on at least three screen shapes, including a very wide and a very tall one.

A game that is cut off or has tiny buttons on a common phone will collect bad reviews quickly."""),
        ("Depth with parallax and layers", """Parallax makes a flat world feel deep: **distant layers move slowly and near layers move quickly** as the camera moves.

A typical scene has:

1. **Far background:** sky, moon or mountains, moving very slowly.
2. **Middle background:** hills and trees.
3. **Gameplay layer:** the player, platforms and enemies, moving 1 to 1 with the camera.
4. **Foreground:** grass, leaves or posts that pass in front, moving faster, used sparingly so they do not block the view.
5. **User interface:** fixed to the screen on top.

In Godot 4.3 and newer, use **Parallax2D** nodes with a scroll scale, and in older versions use `ParallaxBackground` and `ParallaxLayer`. In Unity, move background layers by a fraction of the camera movement. Keep the background **calmer and lower in contrast** than the gameplay layer, so players can always read what matters."""),
        ("Lighting and colour mood", """Light is the strongest mood tool:

- **Colour temperature:** warm light (orange, yellow) feels safe and friendly, cool light (blue, green) feels calm, cold or eerie.
- **Contrast:** a dark scene with a bright spot pulls attention to the spot.
- **2D lights:** in Godot, a **CanvasModulate** darkens the whole scene, and **PointLight2D** nodes (with a soft texture) add pools of light around torches, windows and the player. **Light occluders** cast shadows from walls.
- **Fake it cheaply:** a soft, semi-transparent glow sprite with additive blending looks like light and costs very little.
- **Palette by area:** give each world its own colour identity: a green forest, an orange desert, a purple cave.
- **Time of day:** shift colour over time for dawn, noon and night.

Lights and shadows cost performance, especially on cheap phones, so use few lights, keep them small and test. The player must always be able to **see the important things,** even in a dark mood."""),
        ("Particles and post-processing", """Atmosphere comes alive with movement:

- **Particles:** drifting dust, fireflies, falling leaves, rain, snow, smoke and sparks. In Godot, **CPUParticles2D** works on almost every device including the web, while **GPUParticles2D** is faster for many particles on stronger hardware.
- **Weather and fog:** layers of slowly moving transparent shapes.
- **Vignette:** darkening at the edges guides focus to the centre.
- **Colour grading:** shifting colour to a mood, such as a warm sunset or a washed-out flashback.
- **Bloom:** a soft glow around bright things, used lightly.
- **Screen effects** for damage, such as a brief red edge.

**Limit the effects.** Every one costs processing power and battery, and too many make a scene noisy and hard to read. Check the frame rate on your weakest target device, and provide a **low quality setting.** Great atmosphere is about choosing a few effects that support one clear feeling, and keeping the rest simple."""),
    ],
    diagram=stack([("USER INTERFACE", "fixed to the screen"), ("LIGHT AND EFFECTS", "glow, fog, particles"), ("FOREGROUND", "fast, used sparingly"), ("GAMEPLAY LAYER", "player, platforms, enemies"), ("MIDDLE BACKGROUND", "slower hills and trees"), ("FAR BACKGROUND", "slowest sky and mountains")], "g20", note="Farther layers move slower.", both=False, arrows=False),
    caption="A layered 2D scene: far layers move slowly, the gameplay layer moves with the camera and the interface stays fixed.",
    terms=[("Parallax", "A depth effect where distant layers move slower than near ones."), ("Dead zone", "An area around the centre where the player moves without moving the camera."),
           ("Stretch mode", "A setting that scales the game to fit different screens."), ("Colour temperature", "How warm or cool a light or scene looks."),
           ("Light occluder", "A shape that blocks light to cast a shadow."), ("Vignette", "A darkening around the edges of the screen to focus attention.")],
    mistakes=["Locking the camera rigidly to the player with no smoothing.", "Making the background as bright and detailed as the gameplay layer.", "Using many dynamic lights on cheap phones.", "Not testing on tall and wide screen shapes."],
    quiz=[dict(q="What does parallax do?", o=["Makes distant layers move slower than near ones to create depth", "Stops the camera", "Saves the game", "Plays sound"], a=0,
               why="Different speeds create an illusion of depth."),
          dict(q="Which colour usually feels warm and safe?", o=["Cold blue", "Orange or yellow light", "Grey", "Pure black"], a=1,
               why="Warm colours suggest comfort, cool colours suggest calm or eeriness."),
          dict(q="Why keep the background lower in contrast than the gameplay layer?", o=["It uses less code", "So players can read what matters", "To hide the sprites", "It makes the game louder"], a=1,
               why="Readability matters more than decoration."),
          dict(q="Which is the cheaper way to fake light on weak phones?", o=["Many real-time shadow lights", "A soft glow sprite with additive blending", "Removing all light", "Running at higher resolution"], a=1,
               why="Glow sprites cost very little compared to real-time lights and shadows.")],
    activity="Set up a level with a smooth camera, limits, three parallax layers, a darkening CanvasModulate with two torch lights and a few dust particles. Test it on a real phone, and add a low quality setting that removes the extras.",
)

LESSONS[21] = dict(   # Sound effects and music in your game
    minutes=16,
    hook="Mute a game and it loses half its life. Jump without the soft thump of landing, collect a coin without the bright ping, hit an enemy without the crunch, and the world feels like a silent film. Sound tells the player that something happened, how big it was and where it came from, and music sets the emotion of the whole experience. The earlier lesson explained why sound matters. This lesson shows you how to do it: choosing formats, making or finding effects, avoiding the repetitive sound that annoys players after ten minutes, mixing levels with audio buses, writing or finding music that loops, using sound in space, and, very important, using only audio you have the rights to. You do not need an expensive studio. A phone, free tools and good ears are enough.",
    sections=[
        ("Audio basics for games", """A few facts save you from many problems:

- **Formats:** use **WAV** for short effects (instant playback, larger size) and **OGG Vorbis** for music and long sounds (small size). MP3 also works in most engines, but is less ideal for seamless loops.
- **Sample rate:** 44.1 kHz is standard. For small mobile games, effects at 22 kHz mono can be enough and save space.
- **Mono or stereo:** effects that play from a place in the world should be **mono,** so the engine can position them. Music is usually stereo.
- **Loudness:** keep all sounds at a consistent level so none jumps out. Peak around **minus 3 decibels,** and balance by listening.
- **File size matters:** phones and web builds download your whole game. Compress music and trim silence from the start and end of effects, since silence at the start causes delay.

Always listen on **cheap earphones and a phone speaker,** because that is where most players will hear it."""),
        ("Making and finding sound effects", """You have several routes:

1. **Generate them:** free tools such as **jsfxr, Bfxr and ChipTone** make retro beeps, jumps, hits and explosions in seconds. Click, tweak, export.
2. **Record them yourself (foley):** a phone and a quiet room give you footsteps (shoes on a mat), doors, rustling cloth for movement, a snapped celery stick for a bone crunch, water splashes and clapping. Clean the recording in a free editor such as **Audacity,** removing noise and normalising volume.
3. **Use libraries:** sites such as **Freesound, OpenGameArt** and creator packs offer many sounds. **Read the licence of each one:** CC0 is free to use, CC BY needs credit, and some forbid commercial use.
4. **Hire a sound designer** for a larger project, with a written agreement about rights.

Name files clearly (`coin_pickup_01.wav`, `player_land_soft.wav`) and keep a **credits list** of sources and licences."""),
        ("Make it feel alive: variation and layering", """The same sound repeated again and again becomes irritating. Fix it with:

- **Pitch variation:** randomise the pitch slightly each time, for example between 0.9 and 1.1.
- **Several versions:** three footstep sounds chosen at random, never the same twice in a row.
- **Layering:** a big explosion is a low boom, a mid crack and a high sparkle layered together.
- **Short and clear:** a sound that is too long overlaps with the next one.
- **Priorities:** limit how many copies of a sound can play together so ten coins do not make a roar.

> [GDScript: a sound with random pitch]
> extends AudioStreamPlayer2D
>
> func play_varied() -> void:
>     pitch_scale = randf_range(0.92, 1.08)
>     play()

Time every effect to the **exact frame** of the action, because a sound even slightly late feels wrong. Use sound to tell **meaning:** pickups rise in pitch, damage drops, and warnings are sharp and urgent."""),
        ("Music: loops, layers and moods", """Music sets emotion, so choose it to match the scene:

- **Seamless loops:** a track should loop without a gap or click. Many engines support loop points in OGG files. Test by listening for several minutes.
- **Keep it supportive:** music should not fight sound effects. Lower its volume under effects, and avoid loud melodies in a game that needs concentration.
- **Adaptive music:** add or remove layers as the action changes, such as drums fading in when enemies appear, or a different track for the boss.
- **Stingers:** short musical hits for victory, defeat or discovery.
- **Silence is a tool:** quiet moments make loud moments hit harder.

You can make music with free tools: **LMMS, BeepBox** (in the browser) and **Bosca Ceoil** are friendly for beginners. Partner with a local musician: Nigerian music has a rich rhythm that can give your game a distinct identity. **Never** use a commercial song, even for a short clip, without a licence. Copyright claims can remove your game and your store account."""),
        ("Buses, mixing and accessibility", """A **bus** is a mixing channel. Send sounds to named buses, such as **Master,** **Music,** **SFX** and **UI,** and control each one's volume.

> [GDScript: a volume slider for the Music bus]
> func set_music_volume(value: float) -> void:   # value from 0.0 to 1.0
>     var bus := AudioServer.get_bus_index("Music")
>     AudioServer.set_bus_volume_db(bus, linear_to_db(value))
>     AudioServer.set_bus_mute(bus, value <= 0.001)

Give players **separate sliders** for music and effects, and save the settings. Use **2D positional audio** (`AudioStreamPlayer2D`) so sounds come from where things are and fade with distance. A few more habits:

1. **Add visual cues for important sounds,** and subtitles for dialogue and key audio, so deaf and hard-of-hearing players can play.
2. **Pause audio properly** when the game is paused or the phone goes to the background, and respect the phone's silent mode and calls.
3. **Mix with a reference:** play a game you like next to yours and compare levels.
4. **Test with the sound off:** the game should still be understandable."""),
    ],
    diagram=tree("MASTER BUS", [("Music", ["Menu theme", "Level loop", "Boss layer"]), ("SFX", ["Player", "Enemies", "Pickups"]), ("UI", ["Clicks", "Warnings"])], note="One slider per bus."),
    caption="Sounds go to named buses such as Music, SFX and UI, which feed the master bus and give players separate volume controls.",
    terms=[("Audio bus", "A mixing channel that sets the volume and effects for a group of sounds."), ("Foley", "Sound effects made by recording everyday objects."),
           ("Loop point", "The place where a music track jumps back to the start."), ("Stinger", "A short musical hit for a moment such as victory."),
           ("Pitch variation", "Slightly changing the pitch so repeated sounds feel natural."), ("Adaptive music", "Music that changes layers as the gameplay changes.")],
    mistakes=["Playing the same sound again and again with no variation.", "Using a commercial song without a licence.", "Making music so loud that effects cannot be heard.", "Giving players no separate volume controls."],
    quiz=[dict(q="Which format is best for a long music track in a small game?", o=["OGG Vorbis, small and good for loops", "Uncompressed WAV always", "A screenshot", "A text file"], a=0,
               why="Compressed music keeps the download small."),
          dict(q="How can you stop a repeated effect becoming annoying?", o=["Make it louder", "Randomise pitch and use several versions", "Make it longer", "Remove the picture"], a=1,
               why="Variation keeps repeated sounds feeling natural."),
          dict(q="What is an audio bus?", o=["A vehicle", "A mixing channel for a group of sounds", "A save file", "A texture"], a=1,
               why="Buses let you control volume for music, effects and interface sounds separately."),
          dict(q="Why must you check the licence of a music track?", o=["Using it without rights can get your game and account removed", "To make the file smaller", "To add bass", "Licences are optional"], a=0,
               why="Copyright claims can remove your game from stores.")],
    activity="Make five sound effects with a free generator or your phone, give each three variations with random pitch, build Music, SFX and UI buses with volume sliders, and write a credits file listing the licence for every sound.",
)

LESSONS[22] = dict(   # Bug hunting and playtesting with real players
    minutes=17,
    hook="Every game has bugs. The famous ones, such as a character stuck in a wall, a score that goes negative or a door that never opens, happen to professional studios with hundreds of testers, so they will happen to you. What separates good developers is not avoiding bugs but finding them quickly, understanding them and fixing them without creating new ones. Earlier you learned the basics of watching playtesters and writing bug reports. In this lesson you go deeper into the craft: a calm method for hunting bugs, the debugging tools built into your engine, the kinds of bugs that game developers meet again and again, a simple test plan and automated tests, version control as a bug-finding tool, and how to run a beta with real players on real phones, including how to handle their feedback with respect.",
    sections=[
        ("A calm method for debugging", """Do not guess. Follow a loop:

1. **Reproduce it.** Find the exact steps that always cause the bug. A bug you cannot reproduce cannot be fixed.
2. **Isolate it.** Remove everything that is not needed. Which scene, which object, which input? A small test scene helps.
3. **Form a hypothesis.** “I think the coin is collected twice because the signal fires for two shapes.”
4. **Test the hypothesis** with a print, a breakpoint or a change.
5. **Fix the cause,** not the symptom. Hiding an error with a patch leaves the real problem.
6. **Verify.** Run the original steps and confirm the bug is gone.
7. **Check for side effects,** and add a note or test so it does not return.

Change **one thing at a time.** Take short breaks when stuck, and explain the problem aloud to a friend or a rubber duck. Often you find the answer while describing it."""),
        ("Engine tools for finding bugs", """Learn the tools in your editor:

- **Print and logging:** quick messages such as `print("health:", health)`. Remove or switch off noisy messages later.
- **Breakpoints:** pause the game at a line and inspect the values step by step. This is far better than guessing.
- **The debugger and call stack:** when an error occurs, the stack shows which functions led to it.
- **Remote scene tree and inspector:** while the game runs, look at every object and its live values.
- **Visible collision shapes and navigation:** show invisible problems.
- **Profiler and monitors:** frame time, memory and draw calls.
- **Assertions:** `assert(health >= 0)` stops the game when something impossible happens, which catches bugs near their source.

> [GDScript: a safe check]
> func apply_damage(amount: int) -> void:
>     assert(amount >= 0, "Damage must not be negative")
>     health = max(health - amount, 0)

Read **error messages carefully,** from the first line. They usually name the file and line."""),
        ("Bugs game developers meet again and again", """Learn the usual suspects:

- **Null or missing object:** using something that was deleted or never created. Check before using, and disconnect signals when objects are removed.
- **Frame-rate problems:** movement not multiplied by delta, so the game runs fast on a good phone and slow on a weak one.
- **Order of events:** two scripts that both change the same value, or something used before it is ready.
- **Off-by-one:** counting from 0 or 1, or a level index one too high.
- **Double triggers:** a coin collected twice, a door opened twice, a signal connected twice.
- **Physics surprises:** tunnelling through walls, objects jittering at edges, bodies stuck in each other.
- **State bugs:** the player can pause during a cutscene, or die while the menu is open.
- **Save and load errors:** missing keys after an update.
- **Platform differences:** a feature that works on a laptop but not on a phone or in the web build.
- **Memory leaks:** things created again and again and never freed.

Each time you fix a bug, ask: **where else might this same mistake hide?**"""),
        ("Test plans, automation and version control", """A little structure finds more bugs:

1. **A test checklist:** list the main things to check before each build: start, play, pause, die, win, save, quit and restore.
2. **A device matrix:** a table of the phones and computers you test on, including the weakest, with the version, screen and result.
3. **Edge cases:** do silly things on purpose: press every button at once, tap rapidly, rotate the phone, lose the connection, switch apps and return, fill the storage.
4. **Regression testing:** after each fix, repeat old tests so earlier bugs do not return.
5. **Automated tests:** for pure logic, such as damage formulas, inventory and save upgrades, write tests with a framework such as **GUT** for Godot. They run in seconds.
6. **Version control:** commit small changes with clear messages. When a bug appears, `git bisect` finds the commit that introduced it by testing half of the history at a time.

Triage bugs by **severity** (crash, blocks progress, annoying, cosmetic) and **frequency,** and fix the worst first. Keep a visible list so nothing is forgotten."""),
        ("Beta testing with real players", """Real players find what you cannot:

- **Start small:** five to ten people, then more. Include friends, classmates, local developer groups and online communities, and ask people with weak phones to join.
- **Distribute safely:** use the stores' testing tracks, such as **Google Play's internal and closed testing** and **Apple's TestFlight,** or a private build page on **itch.io,** and check the current rules of each.
- **Ask focused questions:** a short form with “What confused you?”, “Where did you stop playing?” and “What did you enjoy?”, plus an easy way to send a screenshot and device name.
- **Collect crash reports** with a simple tool or a request to send logs, and be clear about what data you collect and why, in line with the **NDPA 2023.**
- **Watch and listen:** the most valuable feedback is behaviour, not opinion. If three people get stuck at the same place, that is a bug in the design.
- **Thank testers and credit them,** and reply to their reports. People who feel heard keep helping.
- **Do not argue.** Feedback is a gift, even when it stings.

Fix the top problems, then release another build, and repeat."""),
    ],
    diagram=cycle([("Reproduce", "find exact steps"), ("Isolate", "shrink it"), ("Guess", "one hypothesis"), ("Fix", "the cause"), ("Verify", "and retest")], "g22", center="Debug|loop", note="Never fix by guessing."),
    caption="The debugging loop: reproduce, isolate, form a hypothesis, fix the cause, verify and retest.",
    terms=[("Reproduce", "To make a bug happen again by following exact steps."), ("Breakpoint", "A marker that pauses the game at a line so you can inspect values."),
           ("Assertion", "A check that stops the game when something impossible happens."), ("Regression", "A bug that returns after it was fixed."),
           ("Triage", "Sorting bugs by how serious and how frequent they are."), ("Beta test", "Testing a nearly finished game with real players.")],
    mistakes=["Fixing bugs by guessing without reproducing them.", "Fixing the symptom and leaving the cause.", "Testing only on your own fast device.", "Arguing with testers instead of listening."],
    quiz=[dict(q="What should you do first when you find a bug?", o=["Reproduce it with exact steps", "Delete the project", "Ignore it", "Change five things"], a=0,
               why="A bug you cannot reproduce cannot be fixed reliably."),
          dict(q="What does a breakpoint do?", o=["Breaks the phone", "Pauses the game at a line so you can inspect values", "Deletes a file", "Adds a sound"], a=1,
               why="Breakpoints let you see exactly what the code is doing."),
          dict(q="Which common bug makes a game run faster on faster phones?", o=["Movement not using delta", "A missing icon", "A long title", "A wrong colour"], a=0,
               why="Without delta, speed depends on the frame rate."),
          dict(q="What does git bisect help you find?", o=["The best art", "The commit that introduced a bug", "A cheaper phone", "A new engine"], a=1,
               why="It tests halves of the history to find where the bug began.")],
    activity="Create a one-page test checklist and a device table for your game, deliberately break it in five silly ways, log and fix each bug with the debugging loop, then send a build to five beta testers and collect their answers.",
)

LESSONS[23] = dict(   # Store pages, trailers and marketing your game
    minutes=16,
    hook="Every year thousands of good games are released and almost nobody notices, not because they are bad, but because nobody ever heard of them. Making the game is only half of the job. The other half is helping the right players find it, understand it in a few seconds and decide to try it. That is marketing, and it is not shouting or tricking people. It is showing your game honestly to the people who would enjoy it. The earlier lesson covered the basics of a store page and listening after launch. Here you will go further: finding your audience, building a marketing funnel, making a trailer and screenshots that work, building a community on a small budget, approaching creators and press, timing a launch and measuring what works, all with honest methods that will not get you banned from a store.",
    sections=[
        ("Know who the game is for", """You cannot market to everyone. Start by describing your **target player** in a sentence: “Teens and young adults on mid-range Android phones who like short, tricky puzzle games and Afrobeats.” Then ask:

- **Where do they spend time?** Which apps, videos, groups and communities?
- **What games do they already love,** and how is yours similar and different? These are your **comparison titles.**
- **What is the one thing** that makes your game worth trying? Your **hook** must fit in a short sentence.
- **What do they have to spend?** Time, data and money. In Nigeria, a small download, offline play and a fair price can be your selling points.

Write down your **unique selling point,** the thing a player gets from your game that they do not get elsewhere. Local setting, culture, language and music can be real strengths when they are authentic."""),
        ("The marketing funnel", """Most players pass through steps, and each step loses people:

1. **See** your post, video or screenshot.
2. **Visit** your store page or website.
3. **Wishlist or follow,** so they hear about launch.
4. **Install or buy.**
5. **Play, review and tell friends.**

Your job is to improve each step. If many see your posts but few visit, the **image or hook** is weak. If many visit but few install, the **store page** needs work. If many install but quit quickly, the **game** needs fixing, not the marketing. Track numbers at each step, however small, such as page visits, followers and wishlists. Without numbers you will not know where the leak is."""),
        ("Store pages, screenshots and trailers", """The store page is your shop window. It must work in **three seconds:**

- **Title and short description:** clear genre and hook in the first line. Put the most important words first.
- **Capsule or icon art:** readable at tiny size, with the main character and a clear style. Avoid tiny text.
- **Screenshots:** the first two or three decide everything. Show **real gameplay,** with a short caption on each. Do not use misleading images.
- **GIFs or short clips** of the most satisfying moment.
- **Trailer:** keep it **30 to 60 seconds.** Show gameplay in the **first five seconds,** not a long logo. Build rhythm: show the hook, show variety, build to the best moment, and end with the title and a call to action such as “Wishlist now” or “Play free.” Add music and make it understandable with the sound off, using short captions.
- **Reviews and ratings:** answer politely, and never buy, fake or trade for reviews. Stores remove such games and accounts.
- **Localisation:** translating the page into languages your players speak raises installs.

On Google Play and the App Store, small details of the page affect how easily the game is found, called **app store optimisation.** Use honest keywords that describe your game, and check each store's current rules, asset sizes and policies."""),
        ("Building a community on a small budget", """Free and cheap methods that work:

- **Devlogs:** short posts or videos about how you build the game. People love behind-the-scenes.
- **Short videos** on platforms such as TikTok, Instagram Reels and YouTube Shorts: a satisfying moment, a funny bug, a before-and-after. Post consistently.
- **A Discord or WhatsApp group** for fans and testers.
- **Game jams:** build something small in a few days, share it and meet other developers.
- **Local meetups and developer communities,** in person and online. Teach what you learned.
- **Communities such as Reddit** welcome genuine contributions, but many ban pure self-promotion. **Read each group's rules,** join in properly and share your game only where it is allowed.
- **A simple website or press kit:** a page with a description, screenshots, a trailer, logo and a contact, so anyone can write about you in minutes.

Post often, reply to every comment and be yourself. Ten real fans are better than a thousand bought followers."""),
        ("Creators, press, launch and measuring", """When the game is ready:

1. **Choose a launch date** and avoid clashes with huge releases. Tell your community in advance.
2. **Contact small creators** who play games like yours. Send a short, personal message with a clear description, a link and a free key or build. Do not mass-spam, and do not demand a good review. Be honest and respectful, and understand that many will not reply.
3. **Contact local and niche press** with your press kit.
4. **Launch week:** be present, answer feedback, fix urgent bugs quickly and thank players.
5. **Update after launch:** patches and small additions keep a game alive and prompt new coverage.
6. **Measure and learn:** which post brought the most visits, which country installs most, which screenshot converts.

**Be honest.** Do not claim features the game does not have, do not buy fake reviews or followers, and follow advertising rules. Honest marketing builds a reputation that helps your next game too."""),
    ],
    diagram=pyramid([("PLAY AND TELL FRIENDS", "the real goal"), ("INSTALL OR BUY", "a good page converts"), ("WISHLIST OR FOLLOW", "so they come back"), ("VISIT THE PAGE", "a strong hook"), ("SEE YOUR POST", "videos, screenshots, community")], note="Fix the step that loses the most people."),
    caption="The marketing funnel: many people see your post, fewer visit, fewer follow, fewer install and a few tell their friends.",
    terms=[("Target player", "The specific type of person you make the game for."), ("Unique selling point", "The one thing your game offers that others do not."),
           ("Marketing funnel", "The steps from seeing your game to playing and recommending it."), ("Wishlist", "A list of games a player wants to be told about at launch."),
           ("Press kit", "A page with descriptions, images, trailer and contact for writers and creators."), ("Devlog", "Posts or videos about how a game is being made.")],
    mistakes=["Trying to market to everyone.", "Starting to promote on launch day instead of months before.", "Buying fake reviews or followers.", "Posting a trailer that starts with a long logo before any gameplay."],
    quiz=[dict(q="When should gameplay appear in a trailer?", o=["In the first five seconds", "After a one-minute logo", "Never", "Only at the end"], a=0,
               why="Viewers decide almost at once, so show the game immediately."),
          dict(q="If many people visit your page but few install, what should you improve?", o=["The store page", "The weather", "Your keyboard", "The engine version"], a=0,
               why="A leak at the page step points to screenshots, text or trailer."),
          dict(q="Why must you read a community's rules before sharing your game?", o=["Many ban pure self-promotion", "Rules are decoration", "To get free keys", "To slow down"], a=0,
               why="Breaking rules can get you banned and hurts your reputation."),
          dict(q="Which of these is honest marketing?", o=["Buying fake reviews", "Showing real gameplay in screenshots and the trailer", "Claiming features that do not exist", "Copying another game's art"], a=1,
               why="Honest, accurate marketing builds long-term trust and keeps your accounts safe.")],
    activity="Write a one-sentence target player and a hook, make three honest screenshots and a 30 second trailer that shows gameplay in the first five seconds, publish a store page draft and post two short videos of your game this week, tracking visits.",
)

LESSONS[24] = dict(   # Making money from games and staying legal
    minutes=17,
    hook="Many people dream of earning a living from games, and some do, but the path is rarely a single viral hit. Most game developers earn through a mix of sales, advertising, in-app purchases, grants, jams and prizes, client work and, over time, a catalogue of several small games. In this lesson you will learn the main business models and their trade-offs, how to price fairly, how store fees and payouts work in general, how to protect yourself legally with licences, trademarks and privacy rules, and what special care children's games need. Rules, fees, tax and payout availability change often and differ by country, so treat this lesson as a map, check each platform's current terms, and speak to an accountant or lawyer before making big decisions. This is education, not legal or financial advice.",
    sections=[
        ("The main ways games earn money", """Each model suits different games:

- **Premium (paid upfront):** a one-time price. Simple and honest. It works best on PC and consoles, and for well-known niches. On mobile, many players avoid paying before they try.
- **Free with ads:** players install free, and you earn from adverts. **Rewarded ads** (watch a video to get a bonus) are generally better liked than ads that interrupt play. Earnings per player are small, so you need many players.
- **In-app purchases (IAP):** free game with optional purchases such as cosmetic items, extra levels or removing ads. Avoid selling unfair advantage that spoils the game for others.
- **Freemium and subscriptions:** ongoing payments for continuing content. Only works when you keep delivering value.
- **DLC and expansions:** extra content for a game people already love.
- **Pay what you want and tips:** platforms such as itch.io let players choose a price or donate.
- **Crowdfunding and community support:** raise money from fans before or during development.
- **Grants, game jams, prizes and competitions:** non-repayable money or services, often for original or educational games. Check local and international programmes.
- **Client and contract work:** building games or interactive training for businesses, schools and organisations, a steady income that funds your own projects.
- **Serious and educational games:** learning tools, quizzes and simulations can have real buyers in schools and companies."""),
        ("Pricing, fees and payouts", """A few principles:

1. **Price for your market.** A game priced fairly for Nigerian players may differ from one for the US. Stores usually let you set **regional prices.**
2. **Compare similar games,** and think about the value for time spent, not only cost to make.
3. **Understand the store's share.** Stores keep a percentage of each sale, historically around 15% to 30%, with reduced rates for small developers on some platforms. **Check the current figures,** because they change.
4. **Know the entry costs:** some stores charge one-time or yearly developer fees. Check each store's current pricing.
5. **Payouts:** each platform pays only in certain countries and by certain methods, such as bank transfer or a payment service. **Confirm that your country and your bank are supported before you build your plan,** and consider that currency conversion and transfer fees reduce what you receive.
6. **Selling directly:** you can sell on your own website or through itch.io, using a payment provider that supports your country, such as Paystack for Nigerian customers. Check their current rules, fees and the products they allow.
7. **Plan for taxes:** keep records of income and costs. In Nigeria, speak to an accountant about registering a business, a tax identification number and what you must report.

A small number of steady players who love your game is worth more than a big download count that earns nothing."""),
        ("Ethics in monetisation", """Be careful how you ask for money:

- **Be transparent:** show real prices, what purchases give, and how to cancel subscriptions.
- **No dark patterns:** do not trick people into spending, hide the close button on ads or make costs unclear.
- **Be careful with random rewards** such as loot boxes. Rules about them vary and are tightening in some countries, and they can resemble gambling. Never target children with them.
- **Do not make the game unplayable** unless players pay. Balance fairness and income.
- **Protect players from overspending,** with clear receipts and refund guidance that follows store policy.
- **Respect time:** avoid designs built to make players feel guilty for stopping.

Players remember how you treated them. A reputation for fair treatment is a lasting business asset."""),
        ("Intellectual property and licences", """Protect your work and respect others':

- **Copyright** automatically protects your original code, art, music and writing. You can strengthen your position by keeping dated drafts, source files and commit history.
- **Licences of what you use:** engine, plugins, fonts, art, music and sound all have terms. Some need credit, some limit commercial use. **Keep a list** with source, licence and proof of purchase.
- **Game names and logos:** search stores and trademark databases before you choose a name. A name too close to a famous one can lead to removal. Registering a trademark in Nigeria goes through the national registry, so ask a professional.
- **Never use** others' characters, music, brand names or code without permission, even in a fan game you sell.
- **Contracts with collaborators:** artists, musicians and co-developers should sign a short agreement about payment, credit and who owns what. Do this **before** work begins.
- **Open source:** libraries have licences (such as MIT or GPL) with different duties. Read them.
- **Your own game's licence:** decide whether others may copy, mod or stream it, and say so on your page.

When in doubt, ask a lawyer who understands software and creative work."""),
        ("Privacy, children and age ratings", """If your game collects any information, you take on duties:

- **Collect the minimum.** If you do not need names, emails or locations, do not collect them. This includes data collected by **ad and analytics tools** that you add, so read what they collect.
- **Write a privacy policy** in plain language that says what you collect, why, who receives it, how long you keep it and how people can ask to see or delete it. Link it on your store page and in the game. Nigeria's **NDPA 2023** and the rules of the stores and of countries where your players live can apply.
- **Children need extra care.** If your game is for children or likely to attract them, stores have special rules, for example Google Play's Families policy and similar programmes. Rules limit personal data, advertising and certain ad networks. Some countries require parental consent. **Read the current policy before you add ads or analytics to a children's game.**
- **Age ratings:** stores ask you to complete a rating questionnaire (many use a system called IARC). Answer honestly about violence, gambling-like features and online interaction.
- **Online features** such as chat need moderation and reporting tools to keep players safe.
- **Terms of service and a refund note:** state the rules and follow the store's refund policy.

Keep records, update your documents when features change and respond promptly when players ask about their data. If you plan to earn real money, consider a short consultation with a lawyer and an accountant to set up the business properly."""),
    ],
    diagram=hub(("GAME INCOME", "mix several sources"), [("Premium sales", "pay once"), ("Ads", "rewarded works best"), ("In-app items", "fair extras only"), ("Grants and jams", "prizes and funding"), ("Client work", "games for others"), ("Support", "tips and crowdfunding")], note="Most developers combine several."),
    caption="Game income usually comes from a mix: premium sales, ads, in-app items, grants and jams, client work and fan support.",
    terms=[("Premium game", "A game sold for a one-time price."), ("In-app purchase", "Something a player buys inside a free game."),
           ("Rewarded ad", "An advert the player chooses to watch in return for a bonus."), ("Dark pattern", "A design trick that pushes people to do things they did not intend."),
           ("Privacy policy", "A document that explains what personal data you collect and why."), ("Trademark", "Legal protection for a name or logo that identifies your product.")],
    mistakes=["Planning income without checking that payouts work in your country.", "Using assets without noting their licences.", "Adding ad and analytics tools to a children's game without reading the policy.", "Working with collaborators without a written agreement."],
    quiz=[dict(q="Which ad type do players usually dislike least?", o=["Ads that block the screen at random", "Rewarded ads they choose to watch", "Ads that hide the close button", "Ads in the middle of a jump"], a=1,
               why="When players choose to watch for a reward, it feels fair."),
          dict(q="What must you confirm before relying on a store for income?", o=["That your country and bank are supported for payouts", "The colour of its logo", "Its slogan", "Nothing"], a=0,
               why="Payout availability differs by country and method."),
          dict(q="What is a dark pattern?", o=["A night-time level", "A design trick that pushes people into choices they did not intend", "A colour palette", "A music style"], a=1,
               why="Dark patterns harm trust and can break store rules."),
          dict(q="Why get a written agreement with an artist or musician?", o=["It makes the game faster", "It sets payment, credit and ownership before work begins", "Stores require a photo", "It replaces a licence for the engine"], a=1,
               why="Clear agreements prevent disputes about who owns and may use the work.")],
    activity="List three income sources that suit your game and your players, check payout support for your country on one store, write a short plain-language privacy policy, and prepare a table of every asset with its licence and credit.",
)
