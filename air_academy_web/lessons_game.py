"""Game Development Masterclass: deep lesson pages 1 to 8.
Same format as lessons_prompt_engineering.py: hook, sections, diagram, terms, mistakes, quiz. Quiz "a" = index of the right option.
Code examples use GDScript (Godot 4) because Godot is free and light. The ideas are the same in Unity, GameMaker and others.
Store terms change, so lessons tell students to check each platform's current page."""
from diagrams import flow, timeline, grid, compare, cycle, fsm, curve, bars

LESSONS = {
    1: dict(
        minutes=14,
        hook="Think about a game of Ludo on a mat under a mango tree. Nobody explains the graphics, because there are none. Yet children play for hours. Roll the dice, move your piece, hope to capture someone, race to the end, then do it all again. Everything that makes it fun fits into one short sentence about what the player does over and over. That is the core loop, and finding it is the most important step in game design. This lesson teaches you to find it, to scope a game you can really finish, and to test it with cards and paper before you write a single line of code.",
        sections=[
            ("The core loop", """The **core loop** is the small cycle of actions that the player repeats throughout the game. Almost every game loop has four parts:

- **Challenge:** something the player must overcome.
- **Action:** what the player does about it.
- **Feedback:** the game shows the result at once, with movement, sound or numbers.
- **Reward:** the player gains something: points, progress, a new ability or simply relief.

Take Ludo. Challenge: get a six to leave home and avoid capture. Action: roll and choose which piece to move. Feedback: the piece slides across the board, or gets captured with a groan from the whole room. Reward: closer to winning. Then the loop restarts. If this loop is not fun with plain squares and dots, no graphics will save it."""),
            ("Goals and feedback", """Players need goals at three scales:

- **Short term:** “jump over that gap now”.
- **Medium term:** “finish this level”.
- **Long term:** “beat the final boss” or “get the highest score”.

And they need **clear feedback** to know whether they are doing well. If the player cannot tell why they lost, they feel cheated and quit. If the rules are clear and the loss is fair, they say “one more try”. A good test: after a failure, can the player say what they should do differently next time?

Also think about **difficulty**. When the challenge is far above the player's skill, they feel anxious. When it is far below, they feel bored. A good game stays in between, rising gently as the player improves."""),
            ("Scope: make a game you can finish", """The biggest reason beginner games never get released is **scope**: the plan is too big. A finishable first game has:

- **One main mechanic,** such as jumping, dodging or matching.
- **One or two enemies or obstacles.**
- **A handful of short levels,** or one endless mode.
- **A time limit for yourself:** two to four weeks.

Write the idea as a **one-sentence pitch**: “In Mango Dash, you run and jump across market stalls to collect mangoes, but the market women are chasing you.” If you cannot say it in one sentence, cut it down. A small game that is finished and polished is worth far more than a huge one that stays on your laptop."""),
            ("Paper prototype before code", """You can test a game idea in an hour with paper, cards and dice. Draw the board, cut out the pieces, and play it with a friend. Watch for:

- **Is the loop fun** even in this rough form?
- **Do players understand the rules** without long explanations?
- **Where do they get bored or confused?**

Changing a paper rule takes ten seconds. Changing code takes ten minutes. Many professional games begin as paper prototypes. And you will keep a very useful habit: fail cheaply, early, on paper."""),
        ],
        diagram=cycle([("CHALLENGE", "Something to|overcome"), ("ACTION", "The player|does something"), ("FEEDBACK", "The game shows|the result"), ("REWARD", "Progress or|a good feeling")], "d1", center="The core loop|repeat, and keep it fun"),
        caption="Find the loop that is fun when repeated, then build everything around it.",
        terms=[("Core loop", "The small cycle of actions that a player repeats throughout a game."), ("Feedback", "The game's immediate response to what the player does."), ("Scope", "How big a project is. Too big and it never gets finished."), ("Mechanic", "A rule or action the player uses, such as jumping or matching."),
               ("Pitch", "A one-sentence description of the game."), ("Prototype", "A rough, quick version used to test an idea.")],
        mistakes=["Planning a huge game with many mechanics for a first project.", "Adding graphics before finding out whether the loop is fun.", "Giving no clear feedback, so players cannot tell why they lost.", "Skipping paper testing and finding design problems only after coding."],
        quiz=[dict(q="What is the core loop of a game?", o=["The cycle of actions the player repeats", "The game's logo animation", "The list of credits", "The loading screen"], a=0, why="The core loop is the repeating pattern of challenge, action, feedback and reward."),
              dict(q="Why is clear feedback important?", o=["It makes the game file smaller", "It shows players what happened and what to change", "It removes the need for any rules", "It makes the whole screen brighter"], a=1, why="When players understand results, they feel losses are fair and want to try again."),
              dict(q="Which is the best scope for a first game?", o=["Ten mechanics and a huge map", "Several online modes", "One main mechanic and a few short levels", "A game with no end date"], a=2, why="A small, focused game is far more likely to be finished and polished."),
              dict(q="What does a paper prototype let you do?", o=["Skip every later step in making", "Avoid ever testing with other people", "Replace the final game completely", "Test the idea quickly and cheaply"], a=3, why="Rules on paper can be changed in seconds, so you learn early whether the idea works.")],
    ),
    2: dict(
        minutes=15,
        hook="A game is a very fast conversation between the player and the computer. The player presses a key, the computer works out what that means, and the screen changes, all sixty times every second, without a break. Game engines exist so that you do not have to build the stage, the lights and the cameras yourself, and can concentrate on the play. In this lesson you pick an engine, learn the three ideas that every engine shares, and write the code that makes a character run and jump.",
        sections=[
            ("Choosing an engine", """A **game engine** is a program that provides the common parts of a game: drawing, sound, physics, input and an editor. Popular beginner-friendly choices:

- **Godot:** free and open source, small to download and runs well on modest laptops. It has its own simple, Python-like language called GDScript.
- **Unity:** very popular, uses C#, with a large library of tutorials. Its licence terms have changed over time, so check them before you commit.
- **Unreal Engine:** powerful for high-quality 3D, but heavy, and best on strong computers.
- **GameMaker:** good for 2D games, with a gentle learning curve.

For learners in Nigeria, where laptops are often modest and data is costly, a small engine such as Godot is a sensible start. The ideas below apply to all of them."""),
            ("Scenes, nodes and objects", """Engines organise a game as a **tree of things**. In Godot they are called **nodes**, grouped into **scenes**. Other engines use **objects** and **prefabs**.

- A **player** is a scene: a body that can move, a sprite (the picture) and a collision shape (its hitbox).
- A **level** is a scene that contains the player, enemies, platforms and a camera.
- You build **small scenes** and **reuse** them, just as you reuse components in a website.

The tree gives every item a place and lets parents control children: move the parent and everything attached moves too. Name things clearly, because a game quickly holds hundreds of items."""),
            ("The game loop", """Under the surface, every game repeats three steps, as the picture shows:

1. **Input:** read what the player is pressing.
2. **Update:** change the game's data: move characters, check collisions, update the score.
3. **Draw:** show the new picture.

A game at **60 frames per second** runs this loop 60 times each second, so each pass has about 16 milliseconds. Engines call your code once per frame, usually in a function such as `_process` or `_physics_process`. A key idea is **delta**: the time since the last frame. Multiply movement by delta, so the character moves at the same real speed on a fast computer and on a slow one."""),
            ("Move and jump", """Here is a complete 2D character controller in GDScript (Godot 4). Read it line by line:

> [GDScript]
> extends CharacterBody2D
> 
> const SPEED = 200.0
> const JUMP_SPEED = -350.0
> var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")
> 
> func _physics_process(delta):
>     if not is_on_floor():
>         velocity.y += gravity * delta
>     if Input.is_action_just_pressed("ui_accept") and is_on_floor():
>         velocity.y = JUMP_SPEED
>     velocity.x = Input.get_axis("ui_left", "ui_right") * SPEED
>     move_and_slide()

Gravity pulls down a little more each frame. Jumping sets an upward speed, but only when on the floor, which stops endless jumping. The arrow keys set sideways speed, and `move_and_slide` moves the body and handles collisions. Keep the indentation consistent: Godot's editor uses tabs, so mixing tabs and spaces causes errors. Change one number at a time and run the game, to feel how each one changes the movement."""),
        ],
        diagram=cycle([("INPUT", "Read keys|and touches"), ("UPDATE", "Move things,|check rules"), ("DRAW", "Show the|new picture")], "d2", center="60 times|every second"),
        caption="Every game is this loop, running dozens of times a second.",
        terms=[("Game engine", "A program that provides drawing, sound, physics, input and an editor."), ("Scene", "A reusable group of items, such as a player or a level."), ("Node", "One item in an engine's scene tree, such as a sprite or a body."), ("Game loop", "The repeating cycle of input, update and draw."),
               ("Delta", "The time since the last frame, used to keep speed steady."), ("Collision shape", "The invisible shape that decides what an object can touch.")],
        mistakes=["Moving things by a fixed amount each frame, not by delta.", "Letting the player jump in mid-air by forgetting the floor check.", "Choosing a heavy engine for a modest laptop.", "Mixing tabs and spaces in the same script."],
        quiz=[dict(q="What are the three steps of the game loop?", o=["Input, update and draw", "Start, middle and end", "Menu, level and score", "Sound, music and voice"], a=0, why="The game reads input, updates its data and draws the result, again and again."),
              dict(q="Why multiply movement by delta?", o=["To make the game sound louder", "To keep speed steady on any computer", "To change the colours of sprites", "To save the game automatically"], a=1, why="Delta is the time since the last frame, so movement stays steady regardless of frame rate."),
              dict(q="What does a collision shape do?", o=["Plays the sound effects", "Writes the score", "Decides what an object can touch", "Loads the next level"], a=2, why="It is the invisible hitbox that the engine uses to detect contact."),
              dict(q="Why check is_on_floor before allowing a jump?", o=["To make the character much faster", "To change the picture of the sprite", "To save a little memory", "To stop endless jumping in the air"], a=3, why="Without that check, pressing jump in mid-air would add upward speed again and again.")],
    ),
    3: dict(
        minutes=15,
        hook="A character that can only run and jump is a toy. The moment you add something that can hurt it, something it can collect and a rule for winning and losing, it becomes a game. These extra pieces are called gameplay systems, and a handful of them make up most games ever made. This lesson walks through the ones you will use again and again: collisions, health and score, simple enemies, and the state machine that keeps all the behaviour under control.",
        sections=[
            ("Collisions and physics", """A **collision** is when two objects touch. Every object that matters gets a **collision shape**, usually a simple box or circle that roughly covers the picture. That shape is called a **hitbox**. Two tips:

- **Make hitboxes slightly smaller than the art** for the player and larger for pick-ups. Players forgive being hit rarely and get angry when they are hit by something that clearly missed.
- **Use layers** to say who touches whom: the player collides with walls and enemies, enemies collide with walls but not each other.

Basic **physics** is a few numbers: **velocity** (speed and direction) and **gravity** (a constant downward pull). Tuning these numbers is called **game feel**: a jump that rises fast and falls slightly faster usually feels better than a perfectly realistic one."""),
            ("Health, score and win or lose", """Most games track a few **numbers**:

> [GDScript]
> var health = 3
> var score = 0
> 
> func take_damage(amount):
>     health -= amount
>     if health <= 0:
>         game_over()
> 
> func collect_coin():
>     score += 10

Keep the rules visible and fair. Show health and score on screen. Give the player a brief moment of invincibility after being hit, or three enemies touching them at once could drain all their health in one frame. And define **clearly how you win and lose**: reach the flag, survive sixty seconds or beat the high score."""),
            ("Enemies and simple AI", """An enemy does not need to be smart. Simple rules can feel clever:

- **Patrol:** walk back and forth between two points, turning at walls or ledges.
- **Chase:** move toward the player when within a certain distance.
- **Shoot or throw** at intervals.
- **Wait and strike:** stay still until the player is close.

Start with the simplest rule, and add one behaviour at a time. Give every enemy a **tell**: a small animation or sound before it attacks, so the player can react. Danger that cannot be seen coming is not challenge, it is frustration."""),
            ("State machines keep behaviour tidy", """A character can be **idle, running, jumping, hurt or dead**. A pile of `if` statements for all combinations soon turns into spaghetti. A **state machine** fixes this: the character is in **exactly one state** at a time, and each state lists what it does and which states it can move to.

The picture shows one: from Idle you can start running or jump; from Run you can stop or jump or get hurt; when hurt, you return to Idle. Each state has its own small piece of code, and the **transitions** are the arrows. Bugs like “the player can attack while dead” disappear, because a dead character simply has no attack transition.

Finally, tune **difficulty** deliberately: start easy, teach one thing at a time, then raise the challenge gradually. Playtesting, in lesson 6, will tell you if you got it right."""),
        ],
        diagram=fsm([("Idle", 0.08, 0.5), ("Run", 0.92, 0.5), ("Jump", 0.5, 0.0), ("Hurt", 0.5, 1.0)], [(0, 1, "press move"), (1, 0, "stop"), (0, 2, "jump"), (2, 0, "land"), (1, 3, "hit"), (3, 0, "recover")], "d3", note="One state at a time, and clear rules for changing state"),
        caption="A state machine keeps a character's behaviour organised and bug-free.",
        terms=[("Hitbox", "The shape that decides where an object can be hit or touched."), ("Velocity", "The speed and direction of movement."), ("Game feel", "How good the controls and movement feel to the player."), ("Tell", "A warning sign before an enemy attacks."),
               ("State machine", "A system where a character is in exactly one state at a time."), ("Invincibility frames", "A short time after being hit when more damage is ignored.")],
        mistakes=["Making hitboxes larger than the art so players feel cheated.", "Giving enemies no warning before they attack.", "Writing a huge tangle of if statements instead of states.", "Spiking the difficulty in the first level."],
        quiz=[dict(q="Why use a state machine for a character?", o=["It makes the character art nicer", "It keeps behaviour organised, one state at a time", "It removes the need for collisions", "It makes the game sound louder"], a=1, why="A state machine prevents contradictions, such as attacking while dead."),
              dict(q="What is a good reason for brief invincibility after a hit?", o=["It makes the game easier forever", "It saves a little memory", "It stops several hits draining all health", "It speeds up the whole game"], a=2, why="A short pause avoids unfair double damage in the same moment."),
              dict(q="What is an enemy tell?", o=["A warning sign shown before it attacks", "A hidden cheat code for the level", "The name written above the enemy", "A loading screen between levels"], a=0, why="A visible or audible warning lets players react, making danger fair."),
              dict(q="What is a hitbox?", o=["A kind of box art for a game", "A button inside the main menu", "A file that saves your progress", "The shape that decides where it can be hit"], a=3, why="Hitboxes are the invisible shapes used to detect contact.")],
    ),
    4: dict(
        minutes=14,
        hook="Walk into a good game's first level and notice what happens. You are placed in a safe, quiet space. A single gap appears, and the only way across is the new thing you have just been shown. You try it, you fail safely, you succeed. Nobody gave you a tutorial, but you learned. That is level design: the art of teaching, challenging and surprising the player through the space itself. This lesson shows you the pattern behind great levels, how to build them quickly, and how to point the camera and the player's eyes where you want them.",
        sections=[
            ("Teach, test, twist", """Most good levels follow a three-step pattern for every new idea:

1. **Teach:** introduce the mechanic in a **safe** place where failing costs nothing. For a jump over a gap, make the gap over a shallow pit.
2. **Test:** ask the player to use it with some pressure, such as two gaps in a row.
3. **Twist:** combine it with something else, such as a gap with a moving platform, or an enemy.

Never ask the player to use a skill that you have not yet taught. If many testers die at the same place, the fault is often in the teaching, not in the player."""),
            ("Pacing: tension and rest", """A level should breathe. **Pacing** is the rhythm of tension and rest. A level that is hard all the time is exhausting, and one that is easy all the time is dull. The picture shows a healthy shape: rise gently with each new idea, drop to a calm moment, then climb higher toward a climax such as a boss or a finishing run.

Place **rest areas** after hard sections: a safe room, a checkpoint, a pretty view. Place **checkpoints** before hard sections, so a failure does not make the player redo five minutes of easy walking."""),
            ("Build fast: greybox and tilemaps", """Do not make beautiful art for a level that might be thrown away. First **greybox** it: build the level from plain grey boxes in 3D, or from simple solid tiles in 2D, just to test the layout and the feel. Play it. Change it. Only when it is fun do you replace the boxes with real art.

In 2D games, a **tilemap** lets you paint a level from a small set of repeating square pictures, called tiles, such as ground, wall, platform and water. It is quick to build, tiny in memory, and easy to change. For 3D, build from a small kit of reusable pieces."""),
            ("Camera and guiding the player", """The **camera** decides what the player sees. Good 2D cameras:

- **Follow** the player smoothly instead of snapping to them.
- Use a **dead zone**: a small area where the player can move without the camera moving.
- **Look ahead** in the direction of movement, so the player can see what is coming.
- Stay inside the level edges.

Guide the player without words. Use **light**, because eyes go to the brightest area. Use **colour**: a single yellow door in a grey room says “go here”. Use **lines**, such as a path or a row of coins that leads the way. And keep the goal visible, or give a hint, so players are never lost for long."""),
        ],
        diagram=curve([("Teach", 0.18), ("Test", 0.42), ("Twist", 0.7), ("Rest", 0.22), ("Boss", 0.95)], note="Rise, rest, then climb higher", ylabel="Challenge"),
        caption="A good level rises and falls, with a rest after every climb.",
        terms=[("Level design", "Planning the spaces and challenges in a game level."), ("Pacing", "The rhythm of tension and rest in a level."), ("Greyboxing", "Building a rough level from plain shapes to test layout and feel."), ("Tilemap", "A level painted from a set of repeating square pictures."),
               ("Dead zone", "A small area where the player can move without the camera moving."), ("Checkpoint", "A saved point the player returns to after failing.")],
        mistakes=["Asking the player to use a skill you never taught.", "Making the whole level hard, with no rest.", "Polishing art before the layout is fun.", "Putting checkpoints after the hard parts instead of before them."],
        quiz=[dict(q="What is the first step when introducing a new mechanic?", o=["Teach it in a safe place", "Test it with a boss", "Combine it with three enemies", "Hide it from the player"], a=0, why="Players learn best when they can try the new skill without risk."),
              dict(q="What does pacing mean?", o=["The speed of the computer", "The rhythm of tension and rest", "The number of levels", "The size of the file"], a=1, why="Good levels alternate challenge and calm, instead of staying at one level."),
              dict(q="Why greybox a level first?", o=["Grey is the best colour", "Greyboxes load faster in stores", "To test the layout and feel before making art", "Because art is not needed"], a=2, why="Plain shapes are quick to change, so you find the fun before spending time on art."),
              dict(q="Where should a checkpoint usually go?", o=["Right after the hardest section", "At the very end only", "Nowhere", "Just before a hard section"], a=3, why="A checkpoint before a hard part means failing costs seconds, not minutes.")],
    ),
    5: dict(
        minutes=14,
        hook="Press a button on a calculator and the number changes. Press a button in a good game and the world answers: a bright flash, a crunch of sound, a small shake of the screen, a number that pops up and flies to the corner. The rules did not change, only the answer to your action. That reply is what players call game feel, and it is often the difference between a game that feels dead and one that feels alive. This lesson covers the menus and the on-screen information, the sound that carries half the experience, and the small touches that make a simple game feel good.",
        sections=[
            ("The HUD: show what matters", """The **HUD (heads-up display)** is the information drawn over the game: health, score, ammo, a timer. Three rules:

- **Show only what the player needs right now.** Every extra number is noise.
- **Make it readable on a small phone screen.** Use large, high-contrast text, and keep key information away from the very edge, where thumbs and notches get in the way.
- **Keep it steady.** A HUD that moves around or changes style confuses players.

Use icons and colour to say things at a glance: a row of hearts reads faster than the word “Health: 3”. But never use colour alone to carry meaning, because some players cannot tell certain colours apart. Add a shape or a label."""),
            ("Menus and flow", """Players meet your menus before they meet your game. A complete game needs:

- **Start screen** with Play, Settings and Quit.
- **Pause screen** reachable at any time, with Resume and Restart.
- **Settings** with a volume slider and, where it fits, controls.
- **Game-over or win screen** with a clear next step: Try Again or Next Level.

Make the **first press to play** as fast as possible. Always provide a **way back** from every screen. And test the menu on a phone if the game will be played there: buttons must be big enough to tap with a thumb."""),
            ("Sound: half of the experience", """Close your eyes while a game plays. Good sound tells you what is happening. Plan three layers:

- **Sound effects:** short sounds for jumps, hits, pick-ups and menu clicks. They give instant confirmation of the player's actions.
- **Music:** sets the mood. Loop it smoothly, and keep it quieter than the effects.
- **Ambience:** a soft background such as wind, a market or crickets.

You can make your own sounds with a phone microphone, or find free ones. **Always check the licence.** Some free sounds require you to credit the author, and some forbid commercial use. Never copy songs from popular artists into your game: it is not allowed, and it will get your game taken down. Keep a list of every sound's source and licence for your credits."""),
            ("Juice: small touches, big feeling", """**Juice** is the extra feedback that makes actions feel satisfying. The picture compares a coin pick-up without and with it. Cheap, effective tricks:

- **Screen shake** on a big hit, brief and small.
- **Particles:** sparks, dust and little stars on impact.
- **Squash and stretch** on the character when landing or jumping.
- **Hit pause:** freezing the game for a tiny fraction of a second on a strong hit.
- **Number pop-ups** and a sound that gets higher as the player chains successes.

Do not overdo it. Too much shaking makes some players feel sick, so offer an option to reduce it. And put **accessibility** into the settings: adjustable volume, remappable controls where possible and subtitles for speech."""),
        ],
        diagram=compare(("Without feedback", ["The coin just disappears", "The number changes silently", "No sound, no movement", "The action feels weak"]), ("With feedback", ["A bright sparkle at the coin", "A pickup sound rising in pitch", "The number pops and counts up", "The action feels rewarding"]), vs="vs", colors=("#FFB86B", "#00F0FF")),
        caption="Same rule, same coin. The answer to the player's action changes everything.",
        terms=[("HUD", "The information drawn over a game, such as health and score."), ("Juice", "Extra visual and sound feedback that makes actions feel good."), ("Particles", "Many small moving pictures used for effects such as sparks or dust."), ("Hit pause", "A tiny freeze on a strong hit to make it feel heavy."),
               ("Ambience", "Quiet background sound that sets the place."), ("Accessibility option", "A setting that makes the game usable by more people.")],
        mistakes=["Cluttering the screen with numbers the player does not need.", "Using colour alone to show something important.", "Using copyrighted music without permission.", "Adding so much screen shake that it makes players feel unwell."],
        quiz=[dict(q="Why should key HUD information be easy to read on a phone?", o=["Phones have no colours at all", "Screens are small and thumbs cover edges", "HUDs are not allowed in games", "It saves a lot of memory"], a=1, why="Large, high-contrast text and a safe distance from the edges keep information visible."),
              dict(q="What does juice add to a game?", o=["More levels to play through", "A lower price in the store", "Extra feedback that makes actions feel good", "A much bigger file size"], a=2, why="Effects like particles, sound and shake make the world answer the player's actions."),
              dict(q="Which is a safe way to get music for a game?", o=["Copy a hit song from a streaming app", "Use music whose licence allows it and credit it", "Use any song you like, nobody will notice", "Record a song from a radio broadcast"], a=1, why="Only use sounds you have the right to use, and keep a list of licences."),
              dict(q="Why avoid using colour alone to show important information?", o=["Colour costs extra money to use", "Printing in colour is hard", "Players always prefer reading text", "Some players cannot tell some colours apart"], a=3, why="Adding shapes or labels makes the game usable by more people.")],
    ),
    6: dict(
        minutes=15,
        hook="You made the game. You have played it fifty times, and you love it. Now give it to a stranger and watch. Within a minute they press a button you never imagined, get stuck where you thought it was obvious, and ignore the instructions you proudly wrote. This is the most useful and most humbling hour of any project, and it is the heart of this lesson. You will also learn how to track bugs so that none are lost, how to find out why a game runs slowly, and how to tune the numbers until the game feels fair.",
        sections=[
            ("Playtesting: watch, do not explain", """A **playtest** is when someone who did not make the game plays it while you observe. How to run a good one:

1. **Give no instructions** beyond what a real player would get. If you explain, you hide the problems.
2. **Stay quiet and watch.** Notice where they hesitate, get stuck, laugh or get annoyed.
3. **Ask them to think aloud:** “What are you trying to do now?”
4. **Do not defend the game.** If they struggle, the game has a problem, not the player.
5. **Afterwards ask:** “What was the most fun? What was the most confusing?”

Three to five players are usually enough to find the biggest problems. When several people trip over the same thing, fix that first. Write down the top three problems after each session."""),
            ("Track bugs properly", """A **bug** is anything that does not work as intended. Write them down, or you will lose them. A good bug report has:

> [Bug report]
> Title: Player falls through floor on level 2
> Steps: 1. Start level 2. 2. Jump onto the moving platform. 3. Wait five seconds.
> Expected: The player rides the platform.
> Actual: The player falls through and dies.
> Severity: High (blocks progress)

The **steps to reproduce** are the most valuable part, because a bug that you can trigger on demand is half fixed. Use a simple list or board with three columns: To do, Doing, Done. Fix the high-severity bugs first, then re-test to be sure the fix did not break something else."""),
            ("Frame rate and performance", """A smooth game runs at a steady frame rate, often 60 frames per second. That means each frame has a **budget of about 16.7 milliseconds** for everything: logic, physics, drawing and sound. The picture shows an example. If one part uses too much, the frame takes longer and the game stutters.

Find the slow part with the engine's **profiler**, a tool that shows what takes time in each frame. Do not guess. Common causes and fixes:

- **Too many objects** being updated or drawn: remove or hide what is off-screen.
- **Heavy work every frame:** do it less often, or only when something changes.
- **Large images and sounds:** compress them and use sensible sizes.
- **Creating and destroying objects constantly:** reuse them with **object pooling**.

Test on the weakest device that you want to support, not only on your own laptop. A game that runs well on a cheap phone runs well everywhere."""),
            ("Balance: tuning the numbers", """**Balance** means that the numbers in your game, such as enemy health, speed and damage, make it fair and fun. Tune them methodically:

- Keep a **table** of the important numbers and what each does.
- **Change one number at a time,** then play again.
- Ask playtesters: “Was it too easy, too hard or about right?”
- Watch for **dominant strategies**, one trick that always wins and makes everything else pointless.

Aim for a challenge that most players can beat after a few tries. That small moment of “I did it!” is what keeps people playing."""),
        ],
        diagram=bars([("Game logic", 4), ("Physics", 3), ("Drawing", 7), ("Audio", 1), ("Spare time", 1.7, "#FFB86B")], note="One frame at 60 fps: about 16.7 ms in total (example)", unit=" ms"),
        caption="Every frame has a small time budget. Find out what is spending it.",
        terms=[("Playtest", "A session where someone new plays the game while you watch."), ("Bug report", "A written record of a problem, with steps to reproduce it."), ("Frame budget", "The time available to finish all work in one frame."), ("Profiler", "A tool that shows what takes time in each frame."),
               ("Object pooling", "Reusing objects instead of constantly creating and deleting them."), ("Balance", "Tuning numbers so that the game is fair and fun.")],
        mistakes=["Explaining the game to playtesters, which hides the real problems.", "Reporting a bug with no steps to reproduce it.", "Guessing what is slow instead of using the profiler.", "Changing many balance numbers at the same time."],
        quiz=[dict(q="What should you do while someone playtests your game?", o=["Watch quietly and take notes", "Explain every rule as they play", "Take the controller from them", "Leave the room"], a=0, why="Silent observation shows the real problems that explanations would hide."),
              dict(q="What is the most useful part of a bug report?", o=["The date", "A long apology", "The steps to reproduce it", "The name of the engine"], a=2, why="If others can trigger the bug on demand, it is far easier to fix."),
              dict(q="At 60 frames per second, roughly how long does each frame take?", o=["About 1 second", "About 100 milliseconds", "About 1 millisecond", "About 16.7 milliseconds"], a=3, why="1,000 milliseconds divided by 60 frames is about 16.7 milliseconds."),
              dict(q="What does a profiler tell you?", o=["Which player is the best", "What takes time in each frame", "How to publish the game", "Which colours to use"], a=1, why="A profiler shows where the time goes, so you fix the real slow parts.")],
    ),
    7: dict(
        minutes=14,
        hook="A baker whose bread is the best in town but who never opens the shop does not feed anyone. A game that is finished but never published is the same. Publishing is where your work finally meets players, and it is often easier and cheaper than people expect. You can have a playable page on the internet in an afternoon, with no fee, and share the link in one WhatsApp message. This lesson shows you how to export a build, set up a store page that makes people click Play, make a short trailer, and keep improving after launch.",
        sections=[
            ("Exports and platforms", """A **build** is the finished, standalone version of your game, separate from the editor. Common targets:

- **Web (HTML5):** the game runs in a browser with nothing to install. This is the easiest for players to try: they click a link and play. Check that your engine supports it for your type of game.
- **Windows, Mac and Linux:** a downloadable program for computers.
- **Android:** an app for phones. Many players in Nigeria use Android, so this can reach a large audience.

**Always test the exported build**, not just the game inside the editor. On a different computer if you can. Problems like missing files, wrong resolution or broken sound often show up only in the real build."""),
            ("Publishing on itch.io", """**itch.io** is a website where independent developers publish games, and it is very friendly to beginners. There is no fee to list a game. You set the price: free, paid or **pay what you want**. itch.io takes a share of sales that **you choose**, with a default of 10 percent, and you can set it differently. Check the site for the current payout terms.

Steps:

1. Create an account and a **new project**.
2. **Upload** your build, a zip file for web or computer, and mark which platform it is for.
3. Fill in the **store page** (next section).
4. Choose the price, then **publish**, and share the link.

To publish on **Google Play**, you need a developer account with a one-time fee of 25 US dollars at the time of writing, and you must be 18 or older. Check Google's page for current rules."""),
            ("A store page that makes people click Play", """Visitors decide in seconds. Prepare:

- **A clear title** and a **one-line pitch**: what do you do, and what is the twist?
- **A cover image** that is bright and readable at small sizes.
- **Three to five screenshots** that show real gameplay, not menus.
- **A short description:** the pitch, two or three features, the **controls** and how to play.
- **Tags** that match the type of game, so the right people find it.
- **A trailer or animated GIF.**

A good **trailer** is 15 to 30 seconds long. Show real gameplay in the **first five seconds**, because many people stop watching quickly. Add one strong sentence, show the best moments and end with the name and where to play."""),
            ("After launch: listen and improve", """Publishing starts a conversation:

- **Share** the link with friends, classmates and communities that love that type of game. Ask for honest feedback, not only praise.
- **Read every comment.** Group them: bugs, confusion and requests.
- **Fix bugs first,** then confusion, then ideas. Release small updates and say what changed.
- **Write a short devlog:** a post about how you made it. It builds an audience and a portfolio.
- **Credit everyone** and every asset you used, and respect each licence.

Do not be crushed by silence or by harsh comments. Almost every first game gets few players. What counts is that you finished, published, learned and will make the next one better."""),
        ],
        diagram=flow([("EXPORT", "Build the|game"), ("TEST", "Play the real|build"), ("PAGE", "Cover, shots,|pitch"), ("PUBLISH", "Set price,|go live"), ("LISTEN", "Read the|feedback")], "d7", "Then the cycle begins again with a better version"),
        caption="Publishing is a loop: release, listen, improve.",
        terms=[("Build", "The finished standalone version of a game, separate from the editor."), ("HTML5 build", "A version of the game that runs in a web browser."), ("itch.io", "A website where independent developers publish and sell games."), ("Store page", "The page that presents a game to potential players."),
               ("Trailer", "A short video that shows what the game is like."), ("Devlog", "A written diary about making the game.")],
        mistakes=["Testing only inside the editor and never the exported build.", "Using screenshots of menus instead of gameplay.", "A trailer that takes fifteen seconds to show any gameplay.", "Forgetting to credit assets and respect their licences."],
        quiz=[dict(q="Why is a web build easy for players?", o=["Nothing to install, they click a link and play", "It needs a very fast phone to run", "It works without any browser at all", "It costs money to play it online"], a=0, why="A browser build removes the biggest barrier: installing anything."),
              dict(q="Why test the exported build and not only the editor?", o=["The editor deletes finished games", "Stores require a video of the editor", "Problems often show up only in the real build", "Editors cannot run games at all"], a=2, why="Missing files and settings often break only after export."),
              dict(q="What should a trailer show in its first five seconds?", o=["A long logo animation", "Credits", "A blank screen", "Real gameplay"], a=3, why="Many viewers leave quickly, so show the game immediately."),
              dict(q="What is a sensible way to treat feedback after launch?", o=["Fix bugs first, then confusion, then ideas", "Ignore all comments", "Only read praise", "Delete the game after one bad comment"], a=0, why="Bugs block players, so fix them first. Then improve clarity, and consider new ideas.")],
    ),
    8: dict(
        minutes=15,
        hook="Every game developer, from a student in Lagos to a studio with a hundred people, has a folder of unfinished projects. The ones who succeed are not the ones with the best ideas. They are the ones who finished, shipped and learned from it. This capstone has one purpose: to get you to a polished, playable, published game, and to write the short post-mortem that turns the experience into skill. Cut the scope early, protect your core loop and finish.",
        sections=[
            ("The brief", """Release a **small, polished, playable game**. It must include:

- **A core loop** that you can describe in one sentence.
- **A player** who moves and interacts, with controls that feel good.
- **A score and a win or lose rule.**
- **At least one enemy or obstacle.**
- **A menu, sound effects and visual feedback.**
- **A playtest** with three people, and fixes for the top three problems.
- **A published build** with a store page: cover image, screenshots, description and controls.
- **A short post-mortem.**

You may use free assets, if you check each licence, credit the authors and list them on the page."""),
            ("Scope: the cut list", """In week one, write **two lists**:

- **Must have:** the minimum game that is fun and complete. Build this first.
- **Cut list:** everything else you would love to add: extra levels, a second enemy, a shop, cutscenes.

Do not touch the cut list until the Must-have list is **finished, tested and published-ready**. When you are running out of time, the cut list protects you, because you drop items instead of dropping quality. Aim to have a playable version, ugly but complete, by the halfway point. After that you only improve it."""),
            ("A release checklist", """Before you publish, tick each item:

1. The game starts, plays and ends without crashing.
2. A new player can understand the controls in under a minute.
3. The first two minutes are fun and clear.
4. Sound can be turned down, and nothing is painfully loud.
5. There is a way to quit and restart.
6. The exported build was tested on another computer or phone.
7. Every asset is credited, with its licence checked.
8. The store page has a cover, screenshots, controls and a pitch.
9. You have a backup of the project in a second place."""),
            ("The post-mortem", """A **post-mortem** is a short, honest look back. It is how professionals turn one project into the next one's advantage. Use three headings, as in the picture:

- **What went well:** what to repeat, such as paper prototyping or an early playtest.
- **What went wrong:** specific problems, with causes. “I underestimated the art” is more useful than “it was hard”.
- **What I will do differently:** concrete changes, such as “cut the scope by half in week one”.

In your demo, present the live game for two minutes, a short trailer, the three top lessons from your playtest, and the post-mortem. You will be graded on meeting the brief, the quality of the build, testing, documentation and presentation. A game page, a trailer and a post-mortem together make a portfolio piece that shows you can finish."""),
        ],
        diagram=grid([("WHAT WENT WELL", "Keep doing|these things"), ("WHAT WENT WRONG", "Honest causes,|not excuses"), ("NEXT TIME", "Concrete changes|to try")], 3, note="A post-mortem has three honest parts"),
        caption="Finishing, publishing and reflecting is how every developer gets better.",
        terms=[("Cut list", "The list of features you decide not to build, so the core stays finished."), ("Release checklist", "A list of checks to complete before publishing."), ("Post-mortem", "A short, honest review of what went well, what went wrong and what to change."), ("Polish", "The final improvements that make a game feel finished."),
               ("Portfolio piece", "A finished project you can show to others as proof of your skills.")],
        mistakes=["Starting the cut list before the must-have game is finished.", "Publishing without testing on a second device.", "Forgetting to credit free assets.", "Writing a post-mortem that blames luck instead of naming causes."],
        quiz=[dict(q="What is the purpose of a cut list?", o=["To protect your core game by cutting extras", "To list all of your friends", "To delete the whole project", "To replace the playtest session"], a=0, why="Dropping low-priority features keeps the main game finished and polished."),
              dict(q="When should you work on the cut list?", o=["Before anything else, in week one", "Only after the must-have game is finished", "Never, do not write it down", "During the playtest with friends"], a=1, why="The core must be complete first, so extras never put the release at risk."),
              dict(q="Which post-mortem sentence is most useful?", o=["It was very hard and I got tired quickly", "Everything went wrong because of bad luck", "I underestimated the art, so next time I cut scope sooner", "I do not want to talk about the project"], a=2, why="A specific cause and a concrete change turn the experience into learning."),
              dict(q="Which item belongs on the release checklist?", o=["Delete all of the backups", "Hide the controls from players", "Remove all of the sound", "Test the exported build on another device"], a=3, why="Real builds often behave differently from the editor, so test them elsewhere.")],
    ),
}