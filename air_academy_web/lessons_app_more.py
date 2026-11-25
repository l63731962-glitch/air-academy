"""App Development Masterclass: lessons 9 to 24, added when the course grew into a full course (course_plan.py says where each one sits on screen).
Same format as lessons_app.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[9] = dict(   # Native, cross-platform and web apps: choosing your path
    minutes=14,
    hook="Before you write a single line of app code, you make a decision that shapes your whole project: what kind of app will you build, and with which tools? Pick well, and one person can ship to thousands of phones in a few months. Pick badly, and you rebuild everything or spend your savings on features nobody can use. The decision is not about which technology is cool. It is about your users' phones, your skills, your budget and your deadline. In this lesson you will compare the real options, look at the conditions of the Nigerian market, and learn a simple method for choosing with confidence.",
    sections=[
        ("The four paths", """You can reach phone users in four main ways:

- **Native apps:** written separately for each system, in **Kotlin** (Android) and **Swift** (iPhone). They have the best access to every phone feature and the smoothest feel, but you build and maintain two apps.
- **Cross-platform apps:** one codebase that runs on both systems. **Flutter** (Dart) draws its own interface and is very consistent. **React Native** (JavaScript) uses native components and suits web developers.
- **Progressive Web Apps (PWA):** a website that can be installed to the home screen, works offline in part and needs no store. Limited access to some phone features.
- **Hybrid wrappers** such as Capacitor: a web app packed inside an app shell, so it can be listed in the stores.

All four are real, professional choices. The right one depends on your project."""),
        ("Criteria for choosing", """Score each option against questions that matter:

1. **Which users and devices?** Which phones do your customers really own?
2. **What features do you need?** Camera, Bluetooth, background location, heavy graphics, payments and notifications?
3. **What skills do you have?** The best tool is often the one you can already use.
4. **How big is your budget and how soon is your deadline?** Two native apps cost roughly double.
5. **How important is performance and feel?** A game or a video editor has different needs from a booking app.
6. **How will people find and install it?** Through the stores, through a link, or both?
7. **How will you maintain it?** Every operating system update means work.

Write the answers down. A decision with reasons is easier to defend to a team, an investor or yourself."""),
        ("The Nigerian reality check", """Good product decisions start from how real people use phones. In Nigeria and much of Africa:

- **Android dominates,** and many devices are mid-range or low-end with limited memory and storage.
- **Data costs money,** so small downloads, light screens and offline use are real selling points.
- **Connections drop** often, so your app must handle weak networks gracefully.
- **Many users share storage-poor phones,** and will delete heavy apps first.
- **Payments** are mostly by card, bank transfer and USSD, handled through providers such as Paystack.
- **iPhone users exist** and often spend more, so know whether your audience includes them.

For many Nigerian projects, a **cross-platform app that works well on Android first** or a **lightweight PWA** is the sensible starting point."""),
        ("A recommendation for most beginners", """If you are learning and want to build real products fast, a good default is:

- **Flutter** for a mobile app that targets Android and iPhone from one codebase, with a single language (Dart), excellent tools and fast screens. This course uses it for its examples.
- A **PWA** if your app is mostly content, forms and simple features, and you want users to start instantly with no store.
- **Native** only when you need the very latest phone features, top performance, or you are joining a team that uses it.

Remember that the **ideas** in this course (screens, state, data, security, testing, releases) are the same in every tool. Skills transfer, so do not worry about picking the single perfect option."""),
        ("Test your choice before committing", """Do not bet months on a guess. Spend a weekend proving it:

1. Build the **riskiest feature** as a tiny prototype, such as the camera scan or the payment step.
2. Run it on **two real, cheaper phones** and not only on your own.
3. Check how **big the install file** is and how fast it opens.
4. Show it to **three real users** and watch them use it.
5. Decide, write down the reasons and the date, and **commit.**

Changing course because you learned something is wise. Changing course because a new tool is trending is expensive. Keep a record, and review the decision honestly after the first release."""),
    ],
    diagram=grid([("NATIVE", "Kotlin or Swift|best access, two apps"), ("FLUTTER", "Dart, one codebase|fast, consistent"), ("REACT NATIVE", "JavaScript|good for web teams"), ("PWA", "A web app you install|no store needed"), ("HYBRID", "Web app in a shell|listed in stores"), ("YOUR CHOICE", "Decided by users,|skills, budget")], cols=3,
                 note="Several good paths. Choose by your project."),
    caption="Native, Flutter, React Native, PWA and hybrid are all real options. Your users, skills and budget decide.",
    terms=[("Native app", "An app written specifically for one operating system using its own tools."), ("Cross-platform", "One codebase that runs on more than one operating system."),
           ("Flutter", "Google's toolkit for building apps for several platforms with the Dart language."), ("PWA", "A website that can be installed on the home screen and works partly offline."),
           ("Prototype", "A small, quick version built to test an idea or risk."), ("Codebase", "All the source code of a project.")],
    mistakes=["Choosing a tool because it is trending.", "Testing only on your own expensive phone.", "Building two native apps with a team of one.", "Ignoring data costs and weak networks in your market."],
    quiz=[dict(q="Which option needs no app store to install?", o=["Native Android", "Native iPhone", "A PWA", "A Flutter app"], a=2,
               why="A PWA is installed from the browser to the home screen."),
          dict(q="What is a key advantage of a cross-platform framework like Flutter?", o=["One codebase for Android and iPhone", "It needs no testing", "It works without a phone", "It is always faster than native"], a=0,
               why="Sharing one codebase saves time and money for small teams."),
          dict(q="Why does data cost matter for app design in Nigeria?", o=["It does not", "Users prefer small, light apps that work on weak networks", "Apps must be huge", "Only for iPhones"], a=1,
               why="Small downloads and offline use respect users' data and connections."),
          dict(q="What should you test before committing to a tool?", o=["Only the logo", "The riskiest feature on real, cheaper phones", "Nothing", "The website colours"], a=1,
               why="A quick prototype reveals real problems early.")],
    activity="List your app idea's five most important features and your users' likely phones. Score Flutter, React Native, native and PWA against the seven criteria and write the one-paragraph decision.",
)

LESSONS[10] = dict(   # Setting up your tools and your first running app
    minutes=14,
    hook="Every developer remembers the first time a tiny app they built appeared on a real phone. It makes everything real. But the setup step is where many beginners get stuck, with long downloads, strange errors and slow computers. The good news is that the process is the same for everyone and the problems are well known. In this lesson you will install the tools, check them with one command, create an app, run it on an emulator or a real phone, make your first change appear instantly with hot reload and understand what the project folders are for. The steps use Flutter, but the habits apply to any toolkit.",
    sections=[
        ("What you need to install", """You need a few tools, each with a clear job:

1. **A code editor:** Visual Studio Code is free and popular. Install its **Flutter** and **Dart** extensions.
2. **The Flutter SDK:** the toolkit itself, downloaded from the official Flutter site. Follow the current instructions for Windows, macOS or Linux, and add it to your PATH.
3. **Android Studio:** it provides the Android SDK, the emulator and the licences. You do not have to write code in it.
4. **Git:** to save your work and download code.
5. **A real phone** (strongly recommended): switch on **Developer options** and **USB debugging**.

Download sizes are large, so plan for a good connection. The official documentation changes with each version, so always follow the **current** steps at flutter.dev instead of an old video."""),
        ("Check everything with one command", """Open a terminal and run:

> [Terminal]
> flutter doctor

It inspects your computer and lists each tool with a tick or a warning. Read every line. Typical fixes:

- **Android licences not accepted:** run `flutter doctor --android-licenses` and answer `y`.
- **SDK or command-line tools missing:** install them from Android Studio's SDK Manager.
- **Path problems:** close and reopen the terminal after changing the PATH.
- **No connected device:** start an emulator or plug in a phone and allow debugging.

Do not continue until `flutter doctor` is happy, because every later problem will look mysterious if the setup is incomplete. Search the exact error message, and read the official docs."""),
        ("Create and run your first app", """With the tools ready:

> [Terminal]
> flutter create my_first_app
> cd my_first_app
> flutter devices
> flutter run

`flutter create` builds a complete starter project with a counter app. `flutter devices` lists the places you can run it. `flutter run` builds the app and installs it. The first build can take several minutes, and the later ones are much faster.

**Emulator or real phone?** An emulator needs a computer with enough memory (8 GB or more is comfortable) and virtualisation turned on. If your computer is old, a **real phone with a USB cable** is faster, and it shows true performance. Test on both when you can."""),
        ("Hot reload: your best friend", """With the app running, open `lib/main.dart`, change some text such as the title, and **save**. The change appears on the screen in under a second, without restarting. This is **hot reload**, and it keeps your current state, so you can tune colours and layouts quickly.

Pressing `r` in the terminal does a hot reload and `R` does a full **hot restart**, which resets the state. If something odd happens, a hot restart often fixes it. Some changes, such as new packages or changes to native settings, need a full stop and `flutter run` again. Try breaking the code on purpose to see a red error screen, then read the message in the terminal. It usually names the file and line."""),
        ("Understand the project folders", """Look at what was created:

> [Folders]
> my_first_app/
>   lib/main.dart       your app's starting point
>   pubspec.yaml        name, version, packages, assets
>   android/            Android-specific project and settings
>   ios/                iPhone-specific project and settings
>   test/               automated tests
>   assets/             images and fonts you add

Most of your work lives in **`lib/`**. **`pubspec.yaml`** lists the packages you use (add one with `flutter pub add package_name`) and the images you include. Put the project under Git from the start with `git init`, and create a `.gitignore` (Flutter makes one). Commit after your first successful run, so you always have a working version to return to."""),
    ],
    diagram=flow([("Install", "editor, SDK,|Android Studio"), ("Check", "flutter doctor"), ("Create", "flutter create"), ("Run", "emulator or|real phone"), ("Change", "save and see|hot reload")], "app10",
                 note="Get to a running app before anything else."),
    caption="Install the tools, check with flutter doctor, create the app, run it and change it with hot reload.",
    terms=[("SDK", "A software development kit: the tools and libraries you need to build for a platform."), ("Emulator", "A virtual phone that runs on your computer."),
           ("Hot reload", "Showing your code changes on the running app instantly without a restart."), ("pubspec.yaml", "The file that lists a Flutter project's packages and assets."),
           ("USB debugging", "A phone setting that lets your computer install and debug apps on it."), ("Package", "A reusable library of code that you add to your project.")],
    mistakes=["Skipping flutter doctor warnings and hoping for the best.", "Following an old video with outdated commands.", "Running a heavy emulator on a computer with too little memory.", "Not saving a Git commit after the first success."],
    quiz=[dict(q="Which command checks your setup?", o=["flutter run", "flutter doctor", "flutter fix", "flutter heal"], a=1,
               why="flutter doctor lists each tool and what still needs attention."),
          dict(q="What does hot reload do?", o=["Deletes the app", "Restarts the phone", "Uploads to the store", "Shows code changes on the running app quickly"], a=3,
               why="It updates the running app in under a second and keeps its state."),
          dict(q="Where do you add packages your project uses?", o=["pubspec.yaml", "README.md", "android/", "test/"], a=0,
               why="pubspec.yaml lists the dependencies."),
          dict(q="Why is a real phone useful for testing?", o=["It is required by law", "Emulators do not exist", "It is faster than a weak emulator and shows true performance", "It makes code shorter"], a=2,
               why="Real devices reveal true speed and behaviour.")],
    activity="Install the tools, get flutter doctor green, create and run the starter app on a phone or emulator, change the title and colour with hot reload, and save a first Git commit.",
)

LESSONS[11] = dict(   # Planning an app: idea, users and features
    minutes=15,
    hook="Thousands of apps are launched every week, and most are downloaded a few times and forgotten. The ones that last usually have something in common: they solve a real problem for specific people. Planning is where you find out whether your idea is one of those, before you spend months building it. In this lesson you will learn how to test an idea with real people, write a clear problem statement, decide which features belong in version one, and produce a short plan that guides everything else. It is the cheapest work you will do, and it saves the most time.",
    sections=[
        ("Start with a problem, not an app", """Many beginners start with “I want to build an app like Uber for…”. A stronger start is: **who has what problem, and how do they handle it today?**

A good problem statement fits in one sentence:

> [Example]
> Small tailors in Lagos lose customer measurements and miss delivery dates because they record everything in notebooks and WhatsApp chats.

Notice that it names **who**, **what goes wrong** and **how it is done now**. If you cannot say these, you are not ready to design screens. Also ask: **is this a problem people will spend time or money to fix?** Some problems are real but small, and people will not install anything for them."""),
        ("Talk to real people", """Validate before you build. Find **five to ten** people who match your users and have short, friendly conversations:

1. Ask about their **last experience** with the problem: “Tell me about the last time you lost an order.”
2. Ask what they **do now** and what it costs them in time or money.
3. **Listen** more than you talk. Do not pitch your idea or ask “would you use this?”, because people say yes to be polite.
4. Ask whether they have **paid** or **tried** something to fix it. Past behaviour is stronger evidence than opinions.
5. Write down their **exact words**, and look for patterns.

Check competitors, including WhatsApp, paper and spreadsheets. If people already solve it a different way, learn why that works and what annoys them. Your app must be **clearly better** at something that matters."""),
        ("Define your user and value", """Turn what you learned into a small **persona**: one real-sounding person with a goal and a frustration.

> [Example]
> Funke, 34, tailor in Surulere. Has 40 active customers. Wants to know what is due this week. Frustrated that measurements are in three notebooks.

Then write your **value proposition**, one line on what your app gives them: “Keep every customer's measurements and deadlines in one place on your phone, even without data.” This line will guide your screens, your store page and your marketing. Also write your **success measure**: for example, “10 tailors use it weekly after one month.” Without a goal, you cannot tell whether you succeeded."""),
        ("Features and the first version", """List every feature you can imagine, then sort them with **MoSCoW**:

- **Must:** the app is useless without it (add a customer, save measurements, see due dates).
- **Should:** important, but version one can ship without it (reminders).
- **Could:** nice to have (photos of designs).
- **Won't, for now:** parked ideas (payments, multi-staff accounts).

Your first release, the **MVP** (minimum viable product), contains only the **Musts**, done well. Each extra feature adds design, code, testing and bugs. A small app that solves one problem beautifully beats a large one that does ten things badly. Keep the parked list, so ideas are not lost."""),
        ("Write a one-page plan", """Collect your decisions on one page that anyone can read in five minutes:

1. **Problem and users:** the one-sentence problem and the persona.
2. **Value proposition and success measure.**
3. **Must-have features** and the parked list.
4. **Main user journey:** the steps from opening the app to the goal.
5. **Platforms and tools** you chose, and why.
6. **Risks:** what could go wrong (a hard feature, a rule from the store, a slow network) and how you will test it first.
7. **Rough timeline,** with a buffer, and **who does what.**
8. **Money:** costs (accounts, hosting, services) and how the app might earn.

Share the page with a few users and a mentor. Their questions will show what you missed."""),
    ],
    diagram=flow([("Problem", "who and what"), ("Talk", "5 to 10 users"), ("Value", "one clear line"), ("Features", "Must, Should,|Could"), ("MVP", "build the Musts")], "app11",
                 note="Learn first, build second."),
    caption="Start with a problem, talk to users, write the value, choose features and build only the Musts first.",
    terms=[("Problem statement", "One sentence naming who has a problem, what goes wrong and how it is handled now."), ("Persona", "A realistic example user with a goal and a frustration."),
           ("Value proposition", "One line saying what your app gives the user."), ("MoSCoW", "A way to sort features into Must, Should, Could and Won't."),
           ("MVP", "The smallest first version that solves the main problem."), ("Validation", "Checking with real people that a problem and a solution are worth building.")],
    mistakes=["Asking “would you use my app?” and trusting the polite yes.", "Building before speaking to a single user.", "Making every feature a Must.", "Ignoring that people already solve the problem some other way."],
    quiz=[dict(q="Which is a better interview question?", o=["Do you like my idea?", "Would you use my app?", "Tell me about the last time you lost an order", "Is my logo nice?"], a=2,
               why="Questions about real past behaviour give honest evidence."),
          dict(q="What does MVP stand for?", o=["Most valuable player", "Minimum viable product", "Maximum visible profit", "Main version proposal"], a=1,
               why="The MVP is the smallest first version that solves the core problem."),
          dict(q="What belongs in the first version?", o=["Every idea", "Only the Must-have features, done well", "Nothing", "Only the logo"], a=1,
               why="A small, focused product is quicker to build and test."),
          dict(q="Why look at competitors such as WhatsApp or paper?", o=["To copy them exactly", "Because people already solve the problem somehow, and you must be clearly better", "It is not needed", "To avoid users"], a=1,
               why="The real competitor is whatever people do now.")],
    activity="Interview five people who have the problem you want to solve, write their words down, then write a one-sentence problem statement, a persona, a value line and a MoSCoW feature list.",
)

LESSONS[12] = dict(   # Wireframes and clickable prototypes
    minutes=14,
    hook="It is cheap to change a drawing and expensive to change an app. A prototype lets your users tap through a pretend version of your app before a single line of real code exists, so you find the confusing buttons, the missing steps and the wrong words while they cost nothing to fix. You already know how to sketch wireframes on paper. In this lesson you take the next step: building a clickable prototype in a free design tool, setting a simple visual style so screens look consistent, running a quick usability test with real people, and handing a clear design to the build stage.",
    sections=[
        ("From paper sketch to clickable prototype", """The usual path has three levels of detail:

1. **Paper sketches:** fast, rough, thrown away without regret.
2. **Low-fidelity wireframes:** grey boxes and labels in a tool, showing structure and flow, without colour or images.
3. **Clickable prototype:** the screens linked together, so tapping a button moves to the next screen.

Use **Figma**, which has a free plan and runs in the browser. Make a **frame** the size of a phone (for example 390 by 844), draw rectangles and text for each screen, and use the **Prototype** tab to connect buttons to screens. Start with the **main journey** only, such as add a customer, then save measurements, then see the list. You do not need to prototype every corner of the app."""),
        ("A small design system", """Consistency makes an app feel professional and makes building faster. Decide a few things once:

- **Colours:** one main brand colour, one accent, plain neutrals, and colours for success, warning and error. Check **contrast** so text is readable (at least 4.5 to 1).
- **Type:** one font family, and a few sizes (title, heading, body, caption).
- **Spacing:** a scale such as 4, 8, 16, 24 and 32 pixels, used everywhere.
- **Components:** buttons, text fields, cards and list rows, designed once and reused.
- **Icons:** one set, in one style.

Name these in your design file. Later you will turn them into your theme in code, and the design and the app will match. Use **real text**, not “Lorem ipsum”, so you see the true layout."""),
        ("Test with real people", """You do not need a lab. Five people reveal most problems:

1. Give each person a **task**, not instructions: “You just met a new customer. Save her details.”
2. Ask them to **think aloud**: what they expect, what confuses them.
3. **Stay quiet** and watch where they hesitate, tap the wrong thing or look lost. Resist the urge to help.
4. Note **what they did**, not only what they said.
5. After the task, ask what they liked and what was confusing.

If three of five people get stuck at the same place, the **design** is at fault, not the people. Test with the kind of users you really have, including those with lower digital confidence and smaller screens."""),
        ("Improve and repeat", """After a round of testing:

- **List the problems** and rate each by how many people hit it and how much it hurt.
- **Fix the biggest first:** a missing step, a vague label, a hidden button.
- **Change one thing at a time** where possible, so you know what helped.
- **Test again** with new people, even briefly.

Typical fixes are plain words (“Save” instead of “Submit”), larger buttons, fewer steps, and clearer **feedback** after an action. Resist adding features to fix a confusing screen. Often the answer is to remove something. Keep a short log of what you changed and why, as it records your design decisions."""),
        ("Hand over to the build stage", """A good handover saves hours of guessing:

1. **Organise the file:** one page per flow, clear names, and a page for the components.
2. **Write the states** for each screen: loading, empty, error and success.
3. **Mark behaviour:** what happens on tap, swipe or long press, and any validation rules.
4. **Export assets:** icons as SVG, images in sensible sizes, and a list of fonts.
5. **Define the data:** what fields each screen shows and where they come from.

When you are both designer and developer, do this anyway. It forces you to think before you code, and it helps a future collaborator. Treat the prototype as a **living reference**, and update it when the app changes."""),
    ],
    diagram=cycle([("Sketch", "paper first"), ("Prototype", "clickable screens"), ("Test", "5 real people"), ("Improve", "fix the biggest problems")], "app12", center="Cheap to|change here",
                  note="Find mistakes before you code."),
    caption="Sketch, build a clickable prototype, test with five people and improve. It is cheapest to change the design now.",
    terms=[("Prototype", "A clickable, pretend version of an app used to test ideas before building."), ("Frame", "A phone-sized canvas in a design tool that holds one screen."),
           ("Design system", "A set of agreed colours, fonts, spacing and components."), ("Think aloud", "Asking a tester to say what they are thinking while using the app."),
           ("Fidelity", "How detailed and realistic a design is, from rough sketch to polished."), ("Contrast", "The difference between text and background colours, which affects readability.")],
    mistakes=["Designing every screen in detail before testing any of them.", "Helping testers instead of watching them struggle.", "Using fake text that hides real layout problems.", "Changing many things at once so you cannot tell what worked."],
    quiz=[dict(q="Why build a clickable prototype before coding?", o=["Mistakes are cheaper to fix in a design than in code", "It is required by law", "It makes the app faster", "Code is not needed later"], a=0,
               why="Changing a design costs minutes. Changing a built app costs days."),
          dict(q="How many test users reveal most major problems?", o=["One", "About five", "Five hundred", "None"], a=1,
               why="Small tests with about five people catch the big issues."),
          dict(q="During a usability test, what should you do?", o=["Explain every screen", "Stay quiet and watch where they hesitate", "Take the phone", "Argue with them"], a=1,
               why="Their confusion shows what the design needs."),
          dict(q="What is a design system for?", o=["Selling the app", "Keeping colours, type, spacing and components consistent", "Encrypting data", "Making icons bigger"], a=1,
               why="Consistency speeds up building and improves the look.")],
    activity="Build a clickable Figma prototype of your app's main journey with real text and a simple design system. Test it with five people, note where they struggled and fix the top three problems.",
)

LESSONS[13] = dict(   # Lists, forms and common screen patterns
    minutes=15,
    hook="Open any app on your phone and you will see the same handful of screen types again and again: a scrolling list, a detail page, a form, a settings page, a search screen. Professional app builders do not invent these from nothing. They know the standard patterns, build each one carefully and spend their creativity on what makes their own app special. In this lesson you will build the screens that make up most real apps: efficient lists, forms that validate, detail and settings screens, and the small touches such as pull to refresh, dialogs and messages that make an app feel finished.",
    sections=[
        ("Lists that stay fast", """A list is the most common screen. In Flutter, use **`ListView.builder`**, which builds only the rows that are visible, so a list of 10,000 items stays smooth:

> [Dart]
> ListView.builder(
>   itemCount: customers.length,
>   itemBuilder: (context, i) {
>     final c = customers[i];
>     return ListTile(
>       leading: CircleAvatar(child: Text(c.name[0])),
>       title: Text(c.name),
>       subtitle: Text("Due: ${c.dueDate}"),
>       trailing: const Icon(Icons.chevron_right),
>       onTap: () => openDetail(c),
>     );
>   },
> )

Never build a long list by putting all items in a plain `Column`. Add **`RefreshIndicator`** for pull to refresh, load more items as the user nears the end (**pagination**), and always design the **empty** and **loading** states."""),
        ("Search, filter and sort", """People find things faster by searching than scrolling. A basic pattern:

1. A **search field** at the top with a clear (x) button.
2. A `query` kept in state. Filter the list from it: `customers.where((c) => c.name.toLowerCase().contains(query.toLowerCase()))`.
3. **Wait a moment** after typing (about 300 milliseconds) before searching a server, so you do not send a request per keystroke.
4. **Chips or a filter sheet** for categories such as “Due this week”.
5. A clear **“no results”** message with a suggestion, not a blank screen.

Keep the filter choice visible so the user knows why the list looks as it does, and make it easy to **reset**."""),
        ("Forms that help", """A form collects information, and a clumsy form makes people quit. Use `Form` with `TextFormField` and a key:

> [Dart]
> final _formKey = GlobalKey<FormState>();
>
> Form(
>   key: _formKey,
>   child: Column(children: [
>     TextFormField(
>       decoration: const InputDecoration(labelText: "Phone number"),
>       keyboardType: TextInputType.phone,
>       validator: (v) =>
>           (v == null || v.trim().length != 11) ? "Enter 11 digits" : null,
>     ),
>     FilledButton(
>       onPressed: () {
>         if (_formKey.currentState!.validate()) save();
>       },
>       child: const Text("Save"),
>     ),
>   ]),
> )

Set the right **keyboard** for each field (number, email, phone), use **autofill hints**, show errors next to the field in plain words, **disable the button while saving**, and keep what the user typed if something fails. Ask only for what you need."""),
        ("Detail, settings and onboarding screens", """Several standard screens appear in almost every app:

- **Detail screen:** the full information for one item, with clear actions (call, edit, delete). Confirm destructive actions with a dialog.
- **Settings:** grouped rows with switches and choices. Save changes immediately and show the current value.
- **Onboarding:** two or three short screens at first launch that explain the value, with a **Skip** option. Do not force a long tutorial. Ask for permissions only when needed, with a reason.
- **Profile and account:** show who is signed in, and provide sign out and account deletion.
- **Login and sign-up:** short, with clear errors, a way to show the password and a reset link.

Reuse the same building blocks, so screens feel consistent."""),
        ("Feedback and polish", """Small signals make an app feel alive and trustworthy:

- **SnackBar** for brief messages: “Customer saved”, with an **Undo** when possible.
- **Dialogs** for important decisions, with a clear verb on the button (“Delete customer”, not “OK”).
- **Bottom sheets** for secondary choices such as sort options.
- **Loading indicators** where work happens, and skeleton placeholders for lists.
- **Empty states** with a friendly message and a button to add the first item.
- **Error states** with a retry button.
- **Haptic feedback** and small animations used sparingly.

Test each screen with long names, no data, slow networks and large text size. These conditions reveal most layout bugs."""),
    ],
    diagram=grid([("LIST", "ListView.builder,|pull to refresh"), ("DETAIL", "One item,|clear actions"), ("FORM", "Right keyboard,|clear errors"), ("SEARCH", "Filter, no results|message"), ("SETTINGS", "Switches and|choices"), ("FEEDBACK", "Snackbar, dialog,|loading, empty")], cols=3,
                 note="Most apps are built from these screens."),
    caption="Lists, details, forms, search, settings and feedback make up most real app screens.",
    terms=[("ListView.builder", "A Flutter widget that builds only the list rows currently visible."), ("Validator", "A function that checks a form field and returns an error message or nothing."),
           ("SnackBar", "A brief message that appears at the bottom of the screen."), ("Pagination", "Loading a long list in small pages instead of all at once."),
           ("Empty state", "A friendly screen shown when there is nothing to display yet."), ("Skeleton", "A grey placeholder shape shown while real content loads.")],
    mistakes=["Building a long list with a plain Column.", "Using the default keyboard for phone numbers.", "Showing a blank screen for no results or no data.", "Using OK on a delete dialog instead of a clear verb."],
    quiz=[dict(q="Why use ListView.builder for long lists?", o=["It builds only visible rows, so scrolling stays smooth", "It looks nicer", "It is required for text", "It stores data"], a=0,
               why="Building thousands of widgets at once would be slow."),
          dict(q="What should you set on a phone number field?", o=["A password keyboard", "A phone keyboard type", "No type", "A date picker"], a=1,
               why="The right keyboard makes typing faster and reduces errors."),
          dict(q="Which dialog button label is clearest?", o=["OK", "Yes", "Delete customer", "Proceed"], a=2,
               why="A specific verb tells the user exactly what will happen."),
          dict(q="What should a list show when a search finds nothing?", o=["A blank screen", "A message with a suggestion", "An error code", "Nothing, the app should close"], a=1,
               why="A clear no-results message helps people recover.")],
    activity="Build a customer list screen with search, pull to refresh, an empty state, a detail screen and an add form that validates a phone number, shows a snackbar and offers Undo.",
)

LESSONS[14] = dict(   # Responsive layouts and dark mode
    minutes=14,
    hook="Your app will run on a small old phone with a cracked corner, a large new phone, a tablet and possibly a foldable. Some users will set their text size to large because their eyes are tired. Many will switch their phone to dark mode at night, and some will open your app while holding the phone sideways. A good app copes with all of this without breaking. You do not need many special cases to do it. You need a few good habits: flexible layouts, safe areas, a proper theme and testing on awkward sizes. In this lesson you will learn them.",
    sections=[
        ("Flexible, not fixed", """The enemy of responsive design is the fixed number. A button 380 pixels wide fits one phone and overflows another. Instead:

- Let widgets **fill the space** they are given: `Expanded`, `Flexible` and `SizedBox(width: double.infinity)`.
- Use **padding and spacing** from your design scale, not hard-coded positions.
- Allow **text to wrap** and avoid fixed heights on boxes that hold text.
- Put content that might not fit inside a **scrollable** widget (`SingleChildScrollView` or a list).
- Use `Wrap` for chips and tags so they flow onto a new line.

If you ever see the yellow and black stripes of a **RenderFlex overflow** error, a child is bigger than its space. Read the message, find the widget and make it flexible."""),
        ("Adapting to the screen", """Sometimes the layout should change with the available space. Flutter offers two tools:

> [Dart]
> LayoutBuilder(
>   builder: (context, constraints) {
>     final wide = constraints.maxWidth >= 600;
>     return wide ? TwoColumnLayout() : OneColumnLayout();
>   },
> )

`LayoutBuilder` tells you the space your widget got, and `MediaQuery.of(context)` tells you the screen size, orientation and text scale. Common adaptations: one column on phones and two on tablets, a **bottom navigation bar** on phones and a **side rail** on large screens, and a grid whose column count grows with the width. Wrap your screens in **`SafeArea`** so content is not hidden by notches, the status bar or the gesture bar."""),
        ("Text size and accessibility", """Many people increase their system font size. Your app must still work:

- **Never fix the height** of text containers. Let them grow.
- Test with the text scale set to **150% and 200%** in the phone's accessibility settings.
- Keep **touch targets at least 48 by 48 logical pixels**, with space between them.
- Maintain good **contrast**, and do not rely on colour alone to show state.
- Add **semantic labels** to icons and images (`semanticLabel`, `Semantics`) so a screen reader such as TalkBack can describe them.
- Support **reduced motion** by keeping animations short and optional.

An accessible app is also easier for everyone in bright sun, on bumpy buses and with one hand. It widens your audience."""),
        ("Dark mode with a real theme", """Do not scatter colours through your widgets. Define a **theme** once and let widgets read from it:

> [Dart]
> MaterialApp(
>   theme: ThemeData(
>     colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF0B6E4F)),
>     useMaterial3: true,
>   ),
>   darkTheme: ThemeData(
>     colorScheme: ColorScheme.fromSeed(
>       seedColor: const Color(0xFF0B6E4F),
>       brightness: Brightness.dark,
>     ),
>     useMaterial3: true,
>   ),
>   themeMode: ThemeMode.system,
>   home: const HomePage(),
> )

In widgets, use `Theme.of(context).colorScheme.primary` instead of `Colors.green`. With `ThemeMode.system`, the app follows the phone's setting. Offer a manual choice (system, light, dark) in settings and save it. Dark mode can also **save battery** on OLED screens."""),
        ("Test the awkward cases", """Create a short **device test list** and run it before each release:

1. A small phone (about 360 by 640) and a large phone.
2. A **tablet** or wide window.
3. **Portrait and landscape.**
4. **Large text** at 200%.
5. **Dark and light mode,** including images and logos that may need a dark version.
6. **Slow device** and low memory.
7. **Right to left** languages if you plan to support them.
8. **Keyboard open,** so fields are not covered.

Use the emulator's different device sizes, Flutter DevTools' layout tools and, above all, **real phones**. Fix issues at the source by making layouts flexible, rather than adding one-off patches for each device."""),
    ],
    diagram=compare(("PHONE", ["One column", "Bottom navigation bar", "Large touch targets"]), ("TABLET OR WIDE", ["Two columns or grid", "Side navigation rail", "More content visible"]), vs="and",
                    note="One app, layouts that adapt."),
    caption="One app adapts: one column and bottom bar on phones, more columns and a side rail on wide screens.",
    terms=[("Responsive", "A layout that adapts to different screen sizes and orientations."), ("LayoutBuilder", "A Flutter widget that tells you how much space it has."),
           ("SafeArea", "A widget that keeps content clear of notches and system bars."), ("Theme", "A central set of colours, fonts and styles used by all widgets."),
           ("Touch target", "The tappable area of a control, which should be at least 48 pixels."), ("Overflow", "An error that appears when a widget is bigger than its available space.")],
    mistakes=["Hard-coding widths and heights in pixels.", "Colours scattered through widgets instead of a theme.", "Never testing with large text or in landscape.", "Making tap targets tiny and close together."],
    quiz=[dict(q="What causes the yellow and black RenderFlex overflow stripes?", o=["A child is bigger than its available space", "The phone is old", "The app has no theme", "A missing package"], a=0,
               why="Make the layout flexible with Expanded, Flexible or scrolling."),
          dict(q="What does SafeArea do?", o=["Encrypts the screen", "Keeps content clear of notches and system bars", "Makes the app faster", "Stores data"], a=1,
               why="Without it, content can hide behind the notch or gesture bar."),
          dict(q="What is the recommended minimum touch target size?", o=["10 pixels", "20 pixels", "48 pixels", "200 pixels"], a=2,
               why="Large enough targets are easier to tap, especially with one hand."),
          dict(q="Why define a theme instead of hard-coding colours?", o=["It is a rule of Dart", "Light and dark mode and brand changes become simple", "Colours are illegal", "It makes apps bigger"], a=1,
               why="Widgets read colours from one place, so changes stay consistent.")],
    activity="Take one of your screens and fix it for a 360 pixel phone, a tablet width, landscape and 200% text. Add a light and dark theme with ThemeMode.system, and test every screen in both.",
)

LESSONS[15] = dict(   # Variables, logic and functions in practice
    minutes=15,
    hook="You have met variables, decisions, functions and classes. Knowing the words is not the same as using them to solve a real problem. In this lesson you will practise them on the kind of logic every app contains: a price and delivery calculator, a bill splitter, a due-date checker. Along the way you will learn the Dart features that prevent the most common crashes, such as null safety, the collection methods that replace clumsy loops, and the habit of keeping calculations in small plain functions that are easy to test, separate from the screens that show them.",
    sections=[
        ("Keep logic out of the screen", """Beginners often write calculations inside the widget that shows them. As the app grows, this becomes impossible to read or test. Put the logic in **plain Dart functions or classes** that know nothing about screens:

> [Dart]
> int deliveryFee(int subtotal, bool isMember) {
>   if (isMember) return 0;
>   if (subtotal >= 10000) return 0;
>   if (subtotal >= 5000) return 500;
>   return 1000;
> }
>
> int orderTotal(List<Item> items, bool isMember) {
>   final subtotal = items.fold(0, (sum, i) => sum + i.price * i.qty);
>   return subtotal + deliveryFee(subtotal, isMember);
> }

Now the widget just calls `orderTotal(...)` and shows the number. You can test the function with a few inputs without running the app. Notice the money is in whole naira (or kobo), not decimals."""),
        ("Null safety: avoiding the biggest crash", """Many crashes come from a value that is **null** (missing) when code expects something. Dart's **null safety** makes you deal with it:

- `String name` can never be null. `String? nickname` may be null.
- `nickname ?? "Friend"` gives a default when it is null.
- `nickname?.length` safely returns null if `nickname` is null.
- `if (nickname != null) { ... }` promotes it to non-null inside the block.
- The `!` operator (`nickname!`) says “trust me, it is not null”. If you are wrong, the app crashes, so use it rarely.

Data from a server can be missing or wrong, so read it defensively: `final price = (json["price"] as num?)?.toInt() ?? 0;`. Decide what “missing” should mean in your app, and handle it deliberately."""),
        ("Collections: say what you mean", """Dart lists have methods that replace many loops and read like plain English:

> [Dart]
> final unpaid   = orders.where((o) => !o.paid).toList();
> final names    = customers.map((c) => c.name).toList();
> final total    = orders.fold<int>(0, (sum, o) => sum + o.amount);
> final first    = orders.firstWhere((o) => o.id == 7, orElse: () => Order.empty());
> final anyLate  = orders.any((o) => o.due.isBefore(DateTime.now()));
> orders.sort((a, b) => a.due.compareTo(b.due));

Also learn **maps** (`Map<String, int>`) for lookups, and **sets** for unique values. Use **enums** for a fixed set of choices (`enum Status { pending, paid, delivered }`), and `switch` on them, so the compiler warns you if you forget a case. These tools make code shorter and bugs fewer."""),
        ("Handling things that can go wrong", """Real input is messy: empty fields, letters in a number box, a date in the past. Plan for failure:

> [Dart]
> int? parseAmount(String text) {
>   final cleaned = text.replaceAll(",", "").trim();
>   return int.tryParse(cleaned);          // null if it is not a number
> }
>
> try {
>   final data = jsonDecode(body);
>   // use data
> } on FormatException {
>   showMessage("The server sent something unexpected.");
> } catch (e) {
>   log("Unexpected error: $e");
> }

Prefer **`tryParse`** over `parse`, validate input **before** using it, and catch specific errors where you can do something useful. Never show a raw exception to the user. Write a clear message, and log the detail for yourself."""),
        ("Habits of readable code", """A few habits make everything easier:

1. **Name things for what they mean:** `deliveryFee`, not `x2`. A function name should be a verb, a variable a noun.
2. **Keep functions short** and focused on one job.
3. **Do not repeat yourself:** if you copy and paste a block, make it a function.
4. **Avoid magic numbers:** `const freeDeliveryFrom = 10000;`.
5. **Use `const` and `final`** for values that never change.
6. **Format your code** (`dart format .`) and run the analyser (`flutter analyze`), and fix its warnings.
7. **Write a small test** for each important function, with normal, edge and bad inputs.

Reading your own code six months later is the real test. Write for that future person, who is you."""),
    ],
    diagram=flow([("Input", "text from the|user"), ("Validate", "tryParse,|ranges"), ("Calculate", "plain functions"), ("Format", "₦ and commas"), ("Show", "update the|screen")], "app15",
                 note="Logic lives in the middle, away from the screen."),
    caption="Input is validated, calculated in plain functions, formatted and shown. The logic stays out of the screen code.",
    terms=[("Null safety", "A Dart feature that forces you to handle values that might be missing."), ("fold", "A list method that combines all items into one value, such as a total."),
           ("Enum", "A type with a fixed set of named choices."), ("tryParse", "A method that converts text to a number and returns null instead of crashing on failure."),
           ("Magic number", "An unexplained number written directly in code."), ("Edge case", "An unusual input at the limits of what is allowed, such as zero or empty.")],
    mistakes=["Putting calculations inside widgets.", "Using the ! operator to silence null warnings.", "Using parse instead of tryParse on user input.", "Copying and pasting code instead of writing a function."],
    quiz=[dict(q="Why keep calculations in plain functions?", o=["They are easy to test and reuse away from the screen", "Dart requires it", "Screens cannot do maths", "It makes the app larger"], a=0,
               why="Pure functions can be tested with simple inputs and reused anywhere."),
          dict(q="What does nickname ?? \"Friend\" do?", o=["Deletes nickname", "Uses \"Friend\" if nickname is null", "Makes it null", "Prints it"], a=1,
               why="The ?? operator supplies a default when the value is null."),
          dict(q="Which is safer for converting text from a user to a number?", o=["int.parse", "int.tryParse", "Hope for the best", "Guess"], a=1,
               why="tryParse returns null instead of throwing, so you can handle bad input."),
          dict(q="What does the where method on a list do?", o=["Sorts it", "Keeps only items that pass a test", "Deletes the list", "Finds a screen"], a=1,
               why="where filters a collection by a condition.")],
    activity="Write a bill splitter as plain Dart functions: subtotal, tip percentage, delivery fee and amount per person. Handle bad input with tryParse and write five small tests, including zero and negative values.",
)

LESSONS[16] = dict(   # Managing app state
    minutes=15,
    hook="Your first apps keep state inside the screen that uses it, and that works, until you add a shopping cart. Now the cart count appears in the top bar, the product list changes its buttons, the checkout screen needs the total and the badge must update the moment something is added. Four places need the same data. Passing it through every widget becomes a mess, and bugs appear where one place shows a different number from another. State management is the set of ideas that keeps shared data in one trusted place. In this lesson you will learn why it matters, the common approaches and how to build a small, clean cart with one of them.",
    sections=[
        ("Local state and its limits", """You already know `setState`: it changes data inside one widget and redraws it. It is perfect for **local state** that only one widget needs, such as whether a password is hidden or which tab is selected.

It becomes painful when **many distant widgets** need the same data:

- You must pass values and callbacks **down through many layers**, even through widgets that do not use them.
- Two screens might each keep their **own copy**, and the copies drift apart.
- The whole screen may **rebuild** for a tiny change.

The cure is to move shared state **out of the widgets** into a separate object that any widget can watch. When it changes, only the widgets that depend on it redraw. This idea, **one source of truth**, is the heart of every state management approach."""),
        ("A simple store with ChangeNotifier", """The simplest approach in Flutter uses a **`ChangeNotifier`** class with the **Provider** package:

> [Dart]
> class CartModel extends ChangeNotifier {
>   final List<CartLine> _lines = [];
>
>   List<CartLine> get lines => List.unmodifiable(_lines);
>   int get count => _lines.fold(0, (s, l) => s + l.qty);
>   int get total => _lines.fold(0, (s, l) => s + l.price * l.qty);
>
>   void add(Product p) {
>     final i = _lines.indexWhere((l) => l.productId == p.id);
>     if (i >= 0) {
>       _lines[i] = _lines[i].copyWith(qty: _lines[i].qty + 1);
>     } else {
>       _lines.add(CartLine(p.id, p.price, 1));
>     }
>     notifyListeners();            // tell everyone who is watching
>   }
> }

The model holds the data and the rules. `notifyListeners()` tells watchers to redraw. The **total is calculated**, not stored separately, so it can never disagree with the lines."""),
        ("Using the store in widgets", """Provide the model high in the tree, then read or watch it where needed:

> [Dart]
> void main() => runApp(
>   ChangeNotifierProvider(create: (_) => CartModel(), child: const MyApp()),
> );
>
> // Watch: redraws when the cart changes
> final count = context.watch<CartModel>().count;
>
> // Read: call an action without redrawing
> onPressed: () => context.read<CartModel>().add(product),

Use **`watch`** in `build` to show data, and **`read`** in event handlers to perform actions. Use **`select`** to watch just one value and avoid needless rebuilds. Widgets stay simple, because they only describe how the screen looks for the current state."""),
        ("Choosing an approach", """Several well-known options exist, and they share the same core idea:

- **`setState`:** local, simple state.
- **Provider with ChangeNotifier:** small to medium apps, easy to learn.
- **Riverpod:** a modern evolution of Provider with compile-time safety and easier testing.
- **Bloc or Cubit:** strict separation with events and states, popular in larger teams.
- **GetX, MobX, Redux style:** other choices with their own fans.

Pick one for your project and **use it consistently**. A simple, well-understood approach used everywhere beats a clever mix. Learn the **concept** (single source of truth, unidirectional data flow, UI as a function of state), and you can switch tools easily later. Always check the current documentation, because packages evolve."""),
        ("Good state habits", """These habits prevent most state bugs:

1. **Keep one source of truth** for each piece of data, and calculate everything else from it.
2. Treat state as **immutable** where possible: create new objects instead of editing hidden ones, and expose lists as unmodifiable.
3. **Separate UI from logic:** put business rules in the model, not in the widgets.
4. **Keep widgets small** and use `const` constructors so Flutter can skip rebuilding them.
5. **Dispose** controllers, streams and listeners you create.
6. **Persist what matters:** a cart should survive an app restart, so save it to local storage.
7. **Test the model** without any screen: add items, check the total, remove, check again.

If you can describe the app's state as a plain list of facts, the screens become simple."""),
    ],
    diagram=hub(("CART MODEL", "one source of truth"), [("Product list", "Add buttons call add()"), ("Cart screen", "Shows lines and total"), ("App bar badge", "Watches the count"), ("Checkout", "Reads the total")],
                note="Many widgets watch one store."),
    caption="Several widgets read from one cart model, so the count, list and total can never disagree.",
    terms=[("State management", "Ways of keeping shared app data in one place that many screens can use."), ("ChangeNotifier", "A Flutter class that can tell listeners when its data has changed."),
           ("Provider", "A package that makes a model available to widgets lower in the tree."), ("Source of truth", "The one place where a piece of data is stored."),
           ("Immutable", "Data that is never edited in place, only replaced with a new copy."), ("Rebuild", "Redrawing a widget because its data changed.")],
    mistakes=["Keeping a separate copy of the cart in each screen.", "Storing the total as well as calculating it.", "Putting business rules inside widgets.", "Forgetting to call notifyListeners or to dispose controllers."],
    quiz=[dict(q="When is setState enough?", o=["For state used by many screens", "For local state used by one widget", "Never", "Only for databases"], a=1,
               why="setState is great for local, simple state such as a toggle."),
          dict(q="What does notifyListeners do?", o=["Sends an email", "Tells watching widgets to redraw", "Deletes the model", "Saves to the cloud"], a=1,
               why="It signals that the data changed."),
          dict(q="Why calculate the cart total instead of storing it?", o=["It cannot get out of step with the lines", "Dart cannot store numbers", "It uses less battery", "Stores are forbidden"], a=0,
               why="A calculated value always matches its source data."),
          dict(q="Which is the core idea shared by every state management tool?", o=["A single source of truth that widgets watch", "More widgets", "Bigger files", "No tests"], a=0,
               why="One trusted store prevents copies from drifting apart.")],
    activity="Build a shopping cart with a ChangeNotifier model: add, remove and clear, a calculated total, a badge in the app bar and a checkout screen. Write a test of the model without any screen.",
)

LESSONS[17] = dict(   # Device features: camera, location and notifications
    minutes=15,
    hook="What makes a mobile app different from a website is the phone itself. It has a camera, a GPS, a vibration motor, a microphone, a notification system and a fingerprint reader. A delivery app that knows where you are, a banking app that scans a cheque and a class app that reminds you at 8 a.m. all use these features. But each one touches something private, and users have learned to be careful. In this lesson you will learn how to use the camera, location and notifications properly, how the permission system works, and how to ask in a way that earns trust instead of a tap on Deny.",
    sections=[
        ("Permissions: ask well", """The phone protects private features behind **permissions**. The user can say yes or no, and can change their mind later in Settings. Good practice:

1. **Ask only when needed,** at the moment the feature is used, not all at once at the first launch.
2. **Explain why before the system pop-up:** “To scan the receipt, we need to use your camera.” Many users deny when the reason is unclear.
3. **Ask for the least access:** coarse location is enough for “shops near me”.
4. **Handle denial gracefully.** The app must still work, perhaps with a manual option, such as typing an address.
5. **Handle “denied forever”:** show a button that opens the app settings.

In Flutter, the `permission_handler` package gives a common way to check and request permissions. Each platform also needs **declarations** in its project files (Android manifest, iOS `Info.plist` text explaining why), or the app will crash or be rejected."""),
        ("The camera and photos", """Many apps need a picture: a profile photo, a receipt, a product. The simplest route is a package such as **`image_picker`**:

> [Dart]
> final picker = ImagePicker();
> final XFile? photo = await picker.pickImage(
>   source: ImageSource.camera,
>   maxWidth: 1280,
>   imageQuality: 80,
> );
> if (photo == null) return;          // the user cancelled
> setState(() => path = photo.path);

Always handle **cancel**. Resize and compress **before uploading**, because phone photos are several megabytes and data costs money. Do not keep pictures in public places, and tell people what happens to them. For scanning codes, use a package that reads QR codes. If you only need a photo from the gallery, the system picker often needs **no permission at all**."""),
        ("Location", """Location is powerful and sensitive. A package such as **`geolocator`** can give the current position:

> [Dart]
> Future<Position?> currentPosition() async {
>   if (!await Geolocator.isLocationServiceEnabled()) return null;
>   var perm = await Geolocator.checkPermission();
>   if (perm == LocationPermission.denied) {
>     perm = await Geolocator.requestPermission();
>   }
>   if (perm == LocationPermission.denied ||
>       perm == LocationPermission.deniedForever) {
>     return null;
>   }
>   return Geolocator.getCurrentPosition();
> }

Four things to remember: the user may have switched **GPS off**, may **deny** access, indoor accuracy can be poor, and **constant tracking drains the battery**. Request location **while the app is in use** unless background tracking is essential, and explain it clearly. Never collect location you do not need. Under Nigeria's NDPA 2023 and similar laws, location is personal data."""),
        ("Notifications", """There are two kinds:

- **Local notifications:** scheduled by the app on the phone itself, for reminders such as “Delivery due today”. They work offline (package `flutter_local_notifications`).
- **Push notifications:** sent from a server through **Firebase Cloud Messaging** (FCM) or a similar service, even when the app is closed.

Practical points: on recent **Android versions the user must grant the notification permission**, and Android uses **channels** so users can control types of messages. On iPhone you must ask permission and have the right capability set up. Send **useful, timely and rare** notifications: order updates, replies, reminders. A flood of promotions trains users to switch them off or uninstall. Let users **choose** what they receive, and never put sensitive details in a message that appears on a locked screen."""),
        ("Test on real devices and fail gracefully", """Device features behave differently on real phones than on emulators:

1. **Test every permission path:** allowed, denied, denied forever, and later granted in Settings.
2. **Test with GPS off, airplane mode and a weak connection.**
3. **Test on at least one low-end Android phone,** and check how the camera and memory behave.
4. **Check battery use** after the feature runs for a while.
5. **Provide a fallback** for every feature: manual address entry, uploading from the gallery, an in-app list instead of a notification.
6. **Respect privacy:** collect the minimum, store it safely, explain it in the privacy policy and let people delete it.

An app that works well even when features are unavailable feels solid, and avoids bad reviews that say “it keeps crashing”."""),
    ],
    diagram=flow([("Need", "feature is used"), ("Explain", "why we ask"), ("Ask", "system pop-up"), ("Allowed?", "yes: use it"), ("Denied", "fallback and|settings link")], "app17",
                 note="Ask in context, explain, and always have a fallback."),
    caption="Explain why, ask at the moment of need, use the feature if allowed, and offer a fallback if denied.",
    terms=[("Permission", "A user's allowance for an app to use a private feature such as the camera or location."), ("Rationale", "A short explanation of why the app needs a permission."),
           ("Local notification", "A reminder scheduled by the app on the phone itself."), ("Push notification", "A message sent from a server to the phone, even when the app is closed."),
           ("FCM", "Firebase Cloud Messaging, a common service for sending push notifications."), ("Least privilege", "Asking only for the access you really need.")],
    mistakes=["Asking for every permission at the first launch.", "Crashing or blocking the app when a permission is denied.", "Uploading full-size photos over mobile data.", "Sending many promotional notifications."],
    quiz=[dict(q="When should an app ask for the camera permission?", o=["At install", "At the first launch for everything", "When the user is about to use the camera, after explaining why", "Never"], a=2,
               why="Asking in context with a reason makes users more likely to agree."),
          dict(q="What should the app do if location permission is denied?", o=["Crash", "Keep working with a manual alternative", "Delete the account", "Hide the screen forever"], a=1,
               why="A fallback keeps the app useful for everyone."),
          dict(q="Which is a push notification?", o=["A reminder the app schedules offline", "A message sent from a server, even if the app is closed", "A sound", "A screenshot"], a=1,
               why="Push messages come from a server, for example through FCM."),
          dict(q="Why resize photos before uploading?", o=["Phones forbid big files", "Large photos waste data and time", "It deletes metadata only", "It is required by Dart"], a=1,
               why="Smaller uploads are faster and cheaper for users.")],
    activity="Add a receipt photo feature and a nearby shops feature to a test app. Handle allowed, denied and denied forever for each, add a manual fallback, and test with GPS off and in airplane mode.",
)

LESSONS[18] = dict(   # Local storage and working offline
    minutes=15,
    hook="A phone leaves the network more often than you think: in a lift, on a bus, in a basement shop, during a data bundle that ran out, when a mobile network has a bad day. An app that shows a blank screen or an error every time that happens quickly gets uninstalled. An app that opens instantly with the last known information, lets people keep working and quietly catches up later feels reliable and is a real advantage in many African markets. In this lesson you will learn where to store data on the phone, how an offline-first design works, and how to handle the hardest part, which is syncing changes without losing anything.",
    sections=[
        ("Choose the right place to store data", """Phones offer several storage options. Pick by what you are saving:

- **Simple settings and flags** (theme choice, “seen onboarding”): `shared_preferences`, a small key and value store.
- **Structured data** (customers, orders, lessons): a local **database**, usually **SQLite**, through packages such as `sqflite`, **Drift** or **Isar**.
- **Files** (images, downloaded PDFs): the app's documents or cache folder.
- **Secrets** (login tokens): **secure storage** (`flutter_secure_storage`), which uses the phone's Keychain or Keystore. Never `shared_preferences` for secrets.

Remember that local data lives **only on that phone**. If the user loses the phone or reinstalls the app, it is gone, unless you also sync it to a server."""),
        ("A local database in practice", """With SQLite you use the same SQL ideas as on a server:

> [Dart]
> final db = await openDatabase(
>   join(await getDatabasesPath(), "tailor.db"),
>   version: 1,
>   onCreate: (db, v) => db.execute(
>     "CREATE TABLE customers("
>     "id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT, updated_at INTEGER)",
>   ),
> );
>
> await db.insert("customers", {"name": "Funke", "phone": "08012345678"});
> final rows = await db.query("customers", orderBy: "name");

Use **parameters** instead of joining text into SQL. Give the database a **version**, and write **migrations** so that when you release an update with a new column, the existing users' data upgrades safely rather than being lost. Keep database work off the main thread, and test migrations from every old version you have shipped."""),
        ("The offline-first idea", """In an **offline-first** app, the **local database is what the screens read**, always. The network is just a way to keep it up to date:

1. The screen shows data from the **local database** instantly.
2. In the background, the app **fetches fresh data** from the server and updates the local copy.
3. When the user makes a change, it is **saved locally first** and added to a **queue of pending changes**.
4. When the connection is available, a **sync service** sends the queue to the server and marks items as done.

The user never waits for the network to do something simple. Show a small, honest **status**: “Saved on this phone, will sync when online”. Detect connectivity with a package such as `connectivity_plus`, but remember it only says there is a connection, not that the internet works, so treat failed requests as normal and retry."""),
        ("Syncing and conflicts", """Sync is the difficult part. Suppose the user edits a customer on the phone offline, and an assistant edits the same customer on another device. Which version wins?

- **Last write wins:** the newest change overwrites the other. Simple, but can silently lose work.
- **Field-level merge:** combine changes to different fields.
- **Ask the user** when it matters.

Helpful techniques:

- Give every record a **unique id created on the phone** (a UUID), so records created offline do not clash.
- Store **`updated_at`** and a **deleted flag** (soft delete), so deletions can sync too.
- Make requests **idempotent**, so a retry does not create duplicates.
- Sync in **small batches** and **resume** after failures.
- **Test** by turning the network on and off while using the app."""),
        ("Cache sensibly and respect storage", """Not everything should be kept forever:

- **Set expiry rules:** product prices may be stale after a day, while a user's own notes should stay.
- **Limit cache size** and clear old images, because many users have little free storage.
- **Download on Wi-Fi or ask first** for large files such as videos or lesson packs. Let users choose what to save offline.
- **Encrypt or protect sensitive data** stored locally, and clear it on logout.
- **Never keep more personal data than needed.** A lost phone should not expose your whole customer base.
- **Back up** important data to the server, and explain to the user where their data lives.

Offline support is a promise to users: their work is safe, even when the network is not."""),
    ],
    diagram=stack([("SCREENS", "Always read from the local database"), ("LOCAL DATABASE", "SQLite on the phone, instant"), ("SYNC SERVICE", "Queue of changes, retries, conflict rules"), ("SERVER", "The shared copy, available when online")], "app18",
                  both=True, note="The screen never waits for the network."),
    caption="Screens read the local database. A sync service sends and receives changes with the server when a connection exists.",
    terms=[("Offline-first", "A design where the app works from local data and syncs when the network is available."), ("SQLite", "A small database that lives inside the app on the phone."),
           ("Migration", "A script that upgrades the local database structure when the app updates."), ("Sync queue", "A list of changes waiting to be sent to the server."),
           ("Conflict", "A situation where two devices changed the same data in different ways."), ("Soft delete", "Marking a record as deleted instead of removing it, so the deletion can sync.")],
    mistakes=["Storing login tokens in shared_preferences.", "Showing a blank error screen whenever there is no connection.", "Forgetting a database migration, so an update wipes users' data.", "Using last write wins everywhere without thinking about lost work."],
    quiz=[dict(q="Where should a login token be stored on the phone?", o=["shared_preferences", "In a text file", "Secure storage", "In the app name"], a=2,
               why="Secure storage uses the Keychain or Keystore, which protect secrets."),
          dict(q="In an offline-first app, what do the screens read?", o=["Only the server", "The local database", "The clipboard", "The network cable"], a=1,
               why="The local database gives instant data, and sync keeps it up to date."),
          dict(q="Why create record ids on the phone, such as UUIDs?", o=["So records made offline do not clash", "To make ids shorter", "To avoid databases", "Servers forbid ids"], a=0,
               why="Unique ids allow safe creation without asking the server first."),
          dict(q="What is a database migration for?", o=["Moving the phone", "Upgrading existing users' data when the structure changes", "Making the app louder", "Deleting caches"], a=1,
               why="Without migrations an app update can break or erase local data.")],
    activity="Add a local SQLite database to your customer app so it opens instantly offline. Add a pending changes queue, sync it when the network returns, and test by toggling airplane mode while editing.",
)

LESSONS[19] = dict(   # Connecting your app to a backend
    minutes=15,
    hook="Many apps are only a pretty window onto a server. The server holds the shared data, the accounts, the payments and the rules, and the app asks it for what it needs. You already know what an API and JSON are. In this lesson you will connect an app to a backend in a way that survives the real world: a clean API layer, models that turn JSON into safe objects, sensible timeouts and retries, authentication on every request, a choice between building your own server and using a ready-made one, and the unusual problem that mobile developers face and web developers do not: old versions of your app stay in people's pockets for months.",
    sections=[
        ("One API layer for the whole app", """Do not scatter network calls through screens. Create a single class that knows how to talk to your server:

> [Dart]
> class ApiClient {
>   ApiClient(this.baseUrl, this.getToken);
>   final String baseUrl;
>   final Future<String?> Function() getToken;
>
>   Future<dynamic> get(String path) async {
>     final token = await getToken();
>     final res = await http
>         .get(Uri.parse("$baseUrl$path"),
>             headers: {if (token != null) "Authorization": "Bearer $token"})
>         .timeout(const Duration(seconds: 15));
>     if (res.statusCode == 401) throw SessionExpired();
>     if (res.statusCode >= 400) throw ApiError.from(res);
>     return jsonDecode(res.body);
>   }
> }

The base address, headers, timeouts and error handling now live **in one place**. Packages such as `dio` add retries and interceptors. Set the **base URL per environment** (development, test, live) with build settings such as `--dart-define`, never by editing code."""),
        ("Models: from JSON to safe objects", """Turn raw JSON into typed objects as soon as it arrives, so the rest of the app never touches loose maps:

> [Dart]
> class Product {
>   Product({required this.id, required this.name, required this.price});
>   final int id;
>   final String name;
>   final int price;
>
>   factory Product.fromJson(Map<String, dynamic> j) => Product(
>         id: j["id"] as int,
>         name: (j["name"] as String?) ?? "Unnamed",
>         price: (j["price"] as num?)?.toInt() ?? 0,
>       );
> }

Read data **defensively**, because servers send missing fields, unexpected nulls and new fields. Packages such as `json_serializable` and `freezed` generate this code to avoid typing mistakes. Keep the models in one folder and use the **same names and formats** as the API documentation."""),
        ("Failure, timeouts and retries", """Mobile networks fail often, and your code must expect it:

- Set a **timeout** on every request, so the screen never waits forever.
- **Retry** safe requests (reading data) a few times with a growing delay. Do not blindly retry actions such as payments, unless the server supports **idempotency keys**.
- Turn technical errors into **plain words**: “No connection” (network), “Please sign in again” (401), “Something went wrong on our side” (5xx).
- **Never show raw exceptions** to users. Log them for yourself.
- Support **pagination** (`?page=2`), so lists load in small pieces.
- **Cancel** requests when the user leaves the screen.

Always **test failure on purpose**: switch to airplane mode, throttle the network and make the server return errors."""),
        ("Build your own backend or use a ready-made one?", """You have two main routes:

- **Your own API** (for example Flask or Node with PostgreSQL): maximum control and flexibility, your own business rules, works with any front end. You must build, secure, host and maintain it.
- **Backend as a service (BaaS)** such as **Firebase** or **Supabase**: ready-made database, authentication, file storage and push notifications. Very quick to start, with fewer servers to manage, but you depend on the provider, its pricing and its data rules.

A sensible approach for a small team: start with a BaaS for speed, or with your own API if you need custom rules, **but always put business rules and security on the server side** with proper access rules. Whichever you choose, use **HTTPS only**, keep **secret keys off the phone** and read the provider's pricing carefully before you grow."""),
        ("The old-app problem", """On the web, you update the site and everyone gets the change. On mobile, **thousands of users keep running old versions** for weeks or months. If you change the API in a way that breaks the old app, those users see crashes.

Protect them:

1. **Version your API** (`/api/v1/`) and keep old versions working for a stated period.
2. Make **additive changes** (new optional fields) rather than renaming or removing fields.
3. Send the **app version** in a header, so the server knows who is calling.
4. Provide a **minimum supported version** endpoint. If the app is too old, show a friendly **“Please update”** screen with a link to the store.
5. Use **feature flags or remote config** to switch features on and off without a new release.
6. **Monitor** which versions are active before you retire an old API.

Plan for change from day one, because your first API is never the last."""),
    ],
    diagram=compare(("YOUR OWN API", ["Full control and custom rules", "You host and secure it", "More work to build and run"]), ("BACKEND AS A SERVICE", ["Auth, database, storage ready", "Very fast to start", "Depends on the provider"]), vs="or",
                    note="Put rules and security on the server side either way."),
    caption="Your own API gives control but needs more work. A backend as a service is fast to start but depends on a provider.",
    terms=[("API client", "One class that handles all requests from the app to the server."), ("Model", "A typed object that represents data such as a product, created from JSON."),
           ("Timeout", "A limit on how long to wait for a response before giving up."), ("BaaS", "Backend as a service: a ready-made server for data, accounts and files."),
           ("Minimum supported version", "The oldest app version the server still accepts."), ("Feature flag", "A setting that turns a feature on or off without releasing a new app.")],
    mistakes=["Scattering network calls with hard-coded addresses across screens.", "Showing raw exceptions to users.", "Renaming API fields and breaking old app versions.", "Keeping secret keys inside the app."],
    quiz=[dict(q="Why create a single ApiClient class?", o=["Base address, headers and error handling live in one place", "Dart requires it", "It hides the app", "It removes the need for a server"], a=0,
               why="One place makes changes and fixes consistent."),
          dict(q="What is a risk of changing an API without versioning?", o=["Nothing", "Old app versions may crash for users who have not updated", "Servers stop working", "Phones restart"], a=1,
               why="Old versions stay on phones for a long time."),
          dict(q="What does fromJson do?", o=["Deletes data", "Turns raw JSON into a typed object", "Sends an email", "Draws a button"], a=1,
               why="Models give the rest of the app safe, typed data."),
          dict(q="Which is a good practice for requests?", o=["No timeout", "Retry payments blindly", "Set a timeout and turn errors into plain words", "Show the stack trace"], a=2,
               why="Timeouts and friendly messages make apps dependable on weak networks.")],
    activity="Create an ApiClient and a Product model for a small shop API. Add timeouts, friendly error messages, a minimum supported version check and a test run with airplane mode and a forced 500 error.",
)

LESSONS[20] = dict(   # In-app purchases and payments
    minutes=15,
    hook="Money is where apps meet the real world, and where the rules are strictest. Two things trip up many first-time developers. First, the app stores have their own payment rules: what you may sell with a card payment service and what you must sell through the store's own billing depends on what you sell. Second, payment security is unforgiving: one mistake can lose money or expose customers' cards. In this lesson you will learn which payment method fits which kind of product, how a safe payment flow works using a hosted checkout such as Paystack, and the golden rules that keep both you and your customers safe. Store policies change, so always read the current rules before you build.",
    sections=[
        ("Digital goods or real-world goods?", """The first question is **what you are selling**:

- **Digital goods used inside the app:** subscriptions, premium features, extra lives, unlock codes, digital content. On the **Apple App Store** and **Google Play**, these generally must use the store's own billing systems (**StoreKit / in-app purchase** and **Google Play Billing**). The stores take a commission, commonly between 15% and 30%, and there are special programmes for small developers. Rules and exceptions differ by country and change over time.
- **Physical goods and real-world services:** food delivery, a taxi ride, clothing, event tickets, school fees, paying a tailor. These can generally be paid through other payment providers such as **Paystack**, with no store commission.

Read the **current** App Store Review Guidelines and Google Play policies before designing, because breaking them can get your app rejected or removed. This is not legal advice."""),
        ("Never handle card details yourself", """Card data is highly regulated (the **PCI DSS** standard). Your app should **never** receive, store or log card numbers, expiry dates, CVV codes or PINs. Instead, use a provider's **hosted checkout** or official SDK, where the customer types card details into the provider's secure form, and your app only receives a **result and a reference**.

Using a provider such as Paystack gives you card payments, bank transfers and other methods in Nigeria without touching sensitive data. If anyone, including a “friend” or a customer, asks you to collect card numbers in a plain form or over WhatsApp, say no. Also never put your **secret API key** inside the app, because anyone can extract it from the installed file. Only the **public key** may live in the app."""),
        ("The safe payment flow", """A secure design never trusts the phone to say that a payment succeeded:

1. The app asks **your server** to start a payment for order 88.
2. Your server **calculates the amount itself** from its own prices and calls the provider to **initialise** the transaction, receiving a checkout address and a **reference**.
3. The app opens the **hosted checkout**, and the customer pays.
4. The provider tells **your server** the result through a **webhook**, and your server can also **verify** the transaction by reference.
5. Your server checks the **amount, currency and reference** match, then marks the order paid and unlocks the product. It does this **once only**, even if the webhook arrives twice.
6. The app **refreshes the order** from your server and shows the result.

If the app closes after paying, the webhook still completes the order, which is why the **server confirms**, not the phone."""),
        ("Testing, refunds and records", """Treat payments like critical infrastructure:

- **Use test keys and test cards** from the provider's documentation until everything works. Switch to live keys only for the real launch, and never mix them.
- **Test the unhappy paths:** declined payment, cancelled checkout, closed app, duplicate webhook, slow network.
- **Keep clear records:** order id, amount, reference, status and time, with no card data.
- **Have a refund policy** that is easy to find, and a way to process refunds. Customers and the stores expect it.
- **Show receipts** and send a confirmation.
- **Reconcile regularly:** compare your records with the provider's dashboard.
- **Watch for fraud and misuse,** and set limits where appropriate.

Money mistakes damage trust faster than bugs."""),
        ("Pricing, trust and the rules around money", """Some further points that matter in practice:

1. **Be clear about prices.** Show the final amount, currency and what the customer gets before they pay.
2. **Subscriptions** need clear terms, easy cancellation and reminders. Store rules require this, and unhappy customers charge back.
3. **Use whole units** (kobo) in code to avoid rounding errors.
4. **Support the methods your customers use:** cards, bank transfer and others offered by your provider.
5. **Comply with the law:** a business that takes payments should be registered appropriately, keep tax records and publish its terms, refund and privacy policies. Ask a qualified professional about your obligations.
6. **Consider fees:** payment providers charge a percentage per transaction, and the stores take commission on digital goods, so price with these in mind.

Trust is the real product: customers pay apps that feel safe and honest."""),
    ],
    diagram=seq(["App", "Your server", "Paystack"], [(0, 1, "Pay for order 88"), (1, 2, "initialise: amount from our price"), (2, 1, "checkout link and reference"), (0, 2, "customer pays on the hosted page"), (2, 1, "webhook: payment success"), (1, 0, "order paid and unlocked")], "app20",
                note="The server confirms the payment, never the phone."),
    caption="The app asks the server to start payment, the customer pays on the provider's page, and the server confirms by webhook.",
    terms=[("In-app purchase", "Buying digital content or features inside an app through the store's billing system."), ("Hosted checkout", "A secure payment page run by the provider, so your app never sees card details."),
           ("Webhook", "A message the provider sends to your server when a payment status changes."), ("Reference", "A unique code that identifies one transaction."),
           ("PCI DSS", "A security standard for handling card data."), ("Idempotent", "Safe to repeat: processing the same payment twice has no extra effect.")],
    mistakes=["Putting a secret payment key inside the app.", "Trusting the phone to say the payment succeeded.", "Collecting card numbers in your own form.", "Selling digital goods with an outside payment method without checking store rules."],
    quiz=[dict(q="Who should confirm that a payment succeeded?", o=["The phone app", "The customer", "Your server, using the provider's webhook or verification", "A friend"], a=2,
               why="Only the server can safely verify payment, because the phone can be tampered with."),
          dict(q="Which key may be stored in the app?", o=["The secret key", "The database password", "The public key designed for client use", "The admin password"], a=2,
               why="Secret keys must stay on the server. Public keys are designed for clients."),
          dict(q="What does the server do with a duplicate webhook?", o=["Processes it twice", "Ignores the repeat so the order is completed only once", "Crashes", "Refunds automatically"], a=1,
               why="Handlers must be idempotent, because providers may send webhooks more than once."),
          dict(q="Which products generally must use the store's billing system?", o=["A pizza delivery", "A taxi ride", "Digital subscriptions and premium features used inside the app", "A pair of shoes"], a=2,
               why="Digital goods inside the app generally go through Apple or Google billing, but always read the current rules.")],
    activity="Draw the full payment sequence for a physical order in your app. Mark what the app, your server and the provider each do, where the amount is calculated and how a duplicate webhook is handled. Then try test mode.",
)

LESSONS[21] = dict(   # Protecting user data and privacy
    minutes=15,
    hook="Every app you build holds a piece of someone's life: their phone number, their photos, their location, their orders, sometimes their money. People hand over that information because they trust you, and a single careless mistake can break that trust and bring legal trouble too. Privacy and security are not features you add at the end. They are decisions you make at every step, starting with a question many developers skip: do we really need to collect this at all? In this lesson you will learn how to collect less, protect what you keep, follow the main rules, including Nigeria's data protection law, and satisfy what the app stores require.",
    sections=[
        ("Collect less, keep less", """The safest data is data you never collected. For each piece of information, ask:

1. **Why do we need it?** If you cannot name a clear purpose, do not collect it.
2. **How long do we need it?** Delete it when the purpose ends.
3. **Who can see it?** Limit access to the people and systems that must.
4. **Is there a safer way?** For example, ask for an age range instead of a birth date, or a nearby area instead of an exact address.

Sort your data by sensitivity: **public**, **personal** (name, phone, email), **sensitive** (health, location history, financial details, children's data) and **secrets** (passwords, tokens). The more sensitive, the stronger the protection and the stricter the limits. Write a simple **data inventory**: what you hold, where it lives, why, and for how long."""),
        ("Protect data on the phone and in transit", """On the device:

- Keep tokens and secrets in **secure storage**, not plain preferences or files.
- Do not put personal data in **logs, crash reports or analytics** events, and do not write it to the clipboard or screenshots of sensitive screens.
- **Clear local data on logout** and offer to hide sensitive screens in the app switcher.
- Remember that code inside the app can be **inspected**, so never hard-code secrets, and treat the app as untrusted. **Obfuscation** only slows people down.

In transit:

- Use **HTTPS for everything**, and never turn off certificate checks to “make it work”.
- For high-risk apps, consider **certificate pinning**, with a plan for rotating certificates.
- Use short-lived **tokens** and let users **sign out** of all devices."""),
        ("Protect data on the server", """The server holds the most valuable data, so it needs the strongest care:

- **Encrypt data at rest** where your database or storage provider supports it, and protect **backups** equally well.
- **Hash passwords** with bcrypt or Argon2, and never store card details.
- Apply **least privilege**: the app's database user can only do what the app needs.
- **Check permissions on every request:** a user may only read their own records.
- **Log access to sensitive data** and review it, but do not log the data itself.
- **Keep software updated,** scan dependencies for known problems and remove unused packages and SDKs.
- Have a **breach plan:** who decides, who is told, and how quickly. Practise it once.

Third-party SDKs (analytics, ads) can collect data too. Know what each one does, because **you are responsible** for it."""),
        ("The rules: Nigeria and the stores", """Several sets of rules apply:

- **Nigeria Data Protection Act (NDPA) 2023**, overseen by the Nigeria Data Protection Commission: you need a **lawful basis** (such as consent or a contract), must be open about what you do, must keep data secure, and must respect people's rights to **access, correct and delete** their data. Larger-scale processors may need to register and appoint a data protection officer. Check the Commission's current guidance. This is not legal advice.
- **Other countries' laws**, such as the EU's GDPR, apply if you have users there.
- **App stores** require a **privacy policy** at a public address, accurate **privacy labels** (Apple) and a **Data safety form** (Google), and an in-app way to **delete the account** and its data.
- **Children:** extra rules apply. Avoid collecting their data, and follow store programmes for apps aimed at kids.

Your privacy policy must match what the app really does."""),
        ("Make privacy a habit", """Build privacy into everyday work:

1. **Ask for consent clearly,** with plain wording and no pre-ticked boxes. Let people change their mind easily.
2. **Offer account and data deletion** in settings, and actually delete the data.
3. **Give users a copy** of their data if they ask.
4. **Review each new feature** with one question: what personal data does it touch, and is that necessary?
5. **Train everyone** who has access to production data.
6. **Respond quickly to reports** of problems, and publish a contact address for security issues.
7. **Be honest** after an incident: tell affected people clearly and early.

Respect is the standard. Treat other people's data the way you would want your own family's data treated."""),
    ],
    diagram=rings(["Collect less and delete on time", "Encrypt on the phone and in transit", "Control who can access what", "Monitor, update and plan for breaches", "USERS' DATA"],
                  note="Layers of care around the data."),
    caption="Collect less, encrypt, control access and monitor. Several layers protect users' data.",
    terms=[("Data minimisation", "Collecting only the personal data you truly need."), ("NDPA 2023", "Nigeria's law on the protection of personal data."),
           ("Secure storage", "The phone's protected place for secrets such as tokens."), ("Encryption at rest", "Scrambling stored data so it is useless if copied."),
           ("Privacy policy", "A public document explaining what data an app collects and why."), ("Data safety form", "Google Play's declaration of how an app collects and uses data.")],
    mistakes=["Collecting data you have no clear purpose for.", "Putting personal data in logs and analytics events.", "Having a privacy policy that does not match what the app does.", "Disabling certificate checks to get past an error."],
    quiz=[dict(q="What is the safest data to protect?", o=["Encrypted data", "Data you never collected", "Data in logs", "Data in the cloud"], a=1,
               why="Not collecting unneeded data removes the risk entirely."),
          dict(q="Where should tokens be kept on the phone?", o=["Plain preferences", "Secure storage", "Logs", "Screenshots"], a=1,
               why="Secure storage uses the phone's protected Keychain or Keystore."),
          dict(q="What must apps generally offer users, according to store rules?", o=["A way to delete their account and data", "A free gift", "A dark mode", "A game"], a=0,
               why="Both major stores expect in-app account deletion."),
          dict(q="Why should you review third-party SDKs?", o=["They may collect data, and you are responsible for it", "They are always safe", "They make the app smaller", "They are illegal"], a=0,
               why="SDKs run inside your app, so what they collect is your responsibility.")],
    activity="Write a data inventory for your app listing each piece of personal data, why you need it, where it is stored and when it is deleted. Remove anything without a clear purpose and add account deletion.",
)

LESSONS[22] = dict(   # Debugging, crashes and performance
    minutes=15,
    hook="Your app works perfectly on your phone, then a user on an older device writes a one-star review: “It keeps freezing.” Apps fail in ways you cannot predict, on devices you do not own, in conditions you never imagined. Strong developers are not the ones who never see a bug. They are the ones who find the cause quickly, fix it properly and hear about problems before the reviews do. In this lesson you will learn a calm debugging method, how to use Flutter's developer tools, how to make your app smooth and light, how to find slowdowns, and how to collect crash reports from real users.",
    sections=[
        ("A calm debugging method", """When something breaks, resist random changes. Follow steps:

1. **Reproduce it.** Find the exact steps that cause the problem. A bug you cannot repeat is a bug you cannot fix.
2. **Read the error.** The console message and **stack trace** usually name the file and line. Start from the first line that points at your own code.
3. **Narrow it down.** Use `debugPrint`, breakpoints, or comment out sections to find where it goes wrong.
4. **Form a guess** about the cause and test it by changing **one thing at a time**.
5. **Fix the cause,** not the symptom.
6. **Check** that the fix works and that nothing else broke, and write a **test** so it cannot return.

Explaining the problem aloud to a friend (or a rubber duck) often reveals the answer. When you ask for help, share the error, your steps and what you tried."""),
        ("Flutter DevTools", """Flutter comes with powerful free tools. Open **DevTools** from VS Code or with `flutter pub global run devtools`:

- **Debugger and breakpoints:** pause your code on a line and look at the variables, then step through.
- **Widget Inspector:** click a widget on the running app to see its place in the tree, its size and its constraints. Perfect for layout bugs.
- **Logging:** see `print` and system messages together.
- **Performance and CPU profiler:** find slow frames and expensive functions.
- **Memory:** watch memory use and spot leaks.
- **Network:** see the requests your app makes.

Learn the shortcuts and use breakpoints instead of printing everything. A few minutes with the Widget Inspector solves many “why is it that size?” mysteries."""),
        ("Smooth screens and frame rate", """A smooth app draws a new frame every 16 milliseconds (60 frames per second), or 8 milliseconds on 120 Hz screens. When work takes longer, the screen **janks**, meaning it stutters. Common causes and fixes:

- **Heavy work on the main thread** (parsing a large JSON, image processing). Move it to the background with `compute()` or an **isolate**.
- **Rebuilding too much.** Make widgets small, use `const` constructors, and watch only the state you need.
- **Long lists built at once.** Use `ListView.builder`.
- **Huge images.** Resize them and use cached network images with sensible dimensions.
- **Expensive effects,** such as many shadows or clip operations on big areas, and complex animations.

Always profile in **profile mode** (`flutter run --profile`) on a **real, modest phone**. Debug mode is slower and gives misleading results."""),
        ("Memory, battery and app size", """Performance is also about resources:

- **Memory leaks:** objects that never get freed, often because a controller, stream or listener was not **disposed** in `dispose()`. Watch memory in DevTools after opening and closing a screen many times.
- **Battery:** avoid constant GPS, frequent polling and wake locks. Batch work and use push messages instead of checking the server every few seconds.
- **App size:** big downloads put off users with limited data. Remove unused packages and assets, compress images, use the **app bundle** format on Android, and check with `flutter build apk --analyze-size`.
- **Start-up time:** do only essential work before the first screen appears, and load the rest afterwards.
- **Network use:** cache, compress and request less.

A lighter app is a polite app, and it earns better reviews from users on cheaper phones."""),
        ("Hear about crashes before your users complain", """You cannot watch every phone, so your app must **report** problems. Add a crash reporting service such as **Firebase Crashlytics** or **Sentry**, and catch errors:

> [Dart]
> void main() {
>   FlutterError.onError = (details) {
>     FlutterError.presentError(details);
>     reportToService(details.exception, details.stack);
>   };
>   runZonedGuarded(() => runApp(const MyApp()), (error, stack) {
>     reportToService(error, stack);
>   });
> }

Reports show the error, the device model, the system version and the app version, so you can spot patterns, such as a crash only on one old phone. Do **not** include personal data in reports. Track the **crash-free users** percentage, fix the most common crash first, show friendly error screens instead of white ones, and check the store dashboards (Play Console and App Store Connect) regularly."""),
    ],
    diagram=compare(("DEBUG MODE", ["Slow on purpose", "Helpful error messages", "Good for finding bugs", "Not for judging speed"]), ("PROFILE OR RELEASE MODE", ["Close to real speed", "Few debugging helpers", "Measure frame rate here", "Test on a modest phone"]), vs="vs",
                    note="Judge performance in profile mode on a real phone."),
    caption="Debug mode is slow on purpose. Judge speed in profile or release mode on a real, modest phone.",
    terms=[("Stack trace", "A list of the code calls that led to an error."), ("Breakpoint", "A marker that pauses the app on a line so you can inspect its state."),
           ("Jank", "Visible stutter when frames take too long to draw."), ("Isolate", "A separate worker in Dart that runs code without freezing the screen."),
           ("Memory leak", "Memory that is never released because something still holds on to it."), ("Crash-free users", "The percentage of users who did not experience a crash.")],
    mistakes=["Changing many things at once while debugging.", "Judging performance in debug mode.", "Forgetting to dispose controllers and streams.", "Never adding crash reporting, so you learn about bugs from reviews."],
    quiz=[dict(q="What is the first step in fixing a bug?", o=["Rewrite everything", "Reproduce it with exact steps", "Ignore it", "Blame the phone"], a=1,
               why="You can only be sure you fixed what you can repeat."),
          dict(q="Where should you measure performance?", o=["Profile mode on a real, modest phone", "Debug mode on a fast laptop", "Only in the emulator", "Never"], a=0,
               why="Debug mode is slow on purpose, and real devices show true behaviour."),
          dict(q="What does jank mean?", o=["A type of font", "A database", "A permission", "Visible stutter from slow frames"], a=3,
               why="Frames that take longer than 16 ms make motion look uneven."),
          dict(q="Why add a crash reporting service?", o=["To slow the app", "To delete data", "To learn about crashes on real devices before reviews do", "To show ads"], a=2,
               why="Reports give the error, device and version so you can fix what matters.")],
    activity="Profile one screen of your app in profile mode on a real phone. Move one heavy task to an isolate, fix a missing dispose, add crash reporting, and compare frame times before and after.",
)

LESSONS[23] = dict(   # App store listings, screenshots and review rules
    minutes=15,
    hook="You have built the app, but nobody can use it until they find it, trust it and press Install. For most apps that moment happens on a store page, in about five seconds, with a few lines of text and a handful of pictures. Your listing is your shop window, and the review process is the shop inspector who decides whether you may open. Developers who ignore either one often wait weeks for approval or get rejected over avoidable mistakes. In this lesson you will learn how to write a listing that people understand, make screenshots that sell, follow the rules reviewers check and move through the testing and release steps without surprises.",
    sections=[
        ("The words and the picture of your listing", """A store listing has a few key parts, and each one has a job:

- **Name and subtitle or short description:** say what the app does in plain words. Include the most important search words naturally. Do not stuff keywords or promise what the app does not do.
- **Icon:** simple, recognisable at small sizes, and different from competitors. No tiny text.
- **Screenshots:** the most important element. Use the **first two or three** to show the main benefit, with a short headline on each: “Never lose a measurement”. Show real screens, not stock photos.
- **Preview video** (optional): a short clip of the main journey with captions.
- **Full description:** start with the benefit, then list features, then say who it is for. Use short paragraphs.
- **Category, contact email, privacy policy link and a support page.**

This is called **ASO** (app store optimisation), and it works like SEO for the stores. Test different versions and watch how many visitors install."""),
        ("Screenshots and assets that sell", """People decide from the pictures. Follow these tips:

1. **Show the benefit, not the menu.** One idea per screenshot, with a large readable caption.
2. **Use the sizes each store requires,** for phones and, if supported, tablets. Check the current requirements in Play Console and App Store Connect.
3. **Keep a consistent look** with your brand colours and the same device frame style.
4. **Use real, attractive sample data,** not “Test User”.
5. **Localise** captions for important markets, such as English and, if relevant, local languages.
6. Add a **feature graphic** for Google Play, and make sure all text is legible on a small screen.
7. **Never show other companies' logos, fake ratings or awards** you did not receive.

Ask a friend who has never seen the app what it does after looking at your screenshots. If they cannot tell, redesign them."""),
        ("What reviewers check", """Both stores have **published guidelines**, and many rejections come from the same few reasons:

- **Crashes, bugs and broken links.** The reviewer will tap around on a real device.
- **An incomplete or placeholder app,** with “coming soon” screens or test data.
- **Login problems.** If the app needs an account, give the reviewer a **working demo account** and instructions.
- **Missing or wrong privacy policy,** or a data declaration that does not match the app's behaviour.
- **No way to delete an account** inside the app.
- **Payment rule violations,** such as selling digital goods without the store's billing.
- **Misleading claims, copied content or copyright and trademark problems.**
- **Asking for permissions you do not need.**
- **Poor quality,** such as a website simply wrapped in an app with no real value.

Read the current guidelines of the store you are targeting **before** you build, and again before you submit."""),
        ("Testing tracks and release steps", """Stores let you test before the world sees the app:

1. **Internal testing** (Google Play) or **TestFlight** (Apple): you and your team install early builds quickly.
2. **Closed or external testing:** invite a group of real testers by email. Google may require **new developer accounts to run a closed test with a minimum number of testers for a set period** before production access. Check the current requirements in Play Console.
3. **Production:** the public release.

Before you submit: set the **version name and build number**, create a signed **release build** (Android App Bundle or an iOS archive), fill in the **content rating questionnaire**, the **data safety or privacy label**, pricing and countries, and the target audience. Then **submit for review**. Typical reviews take from several hours to a few days, but allow **extra time** for the first submission. Keep your **signing keys** and account credentials safe, because losing them can lock you out of updating your own app."""),
        ("Costs, accounts and a launch plan", """Plan the practical details:

- **Developer accounts:** Google Play has a one-time registration fee (about 25 US dollars at the time of writing), and Apple's Developer Program has a yearly fee (about 99 US dollars). Check the current prices. Individuals and organisations may need to **verify identity**, and an organisation account may need business details.
- **Use a business email and keep the account yourself,** not an employee's or a freelancer's.
- **Launch with a plan:** tell your first users, ask early users for honest ratings, and respond to every review politely.
- **Use a staged rollout** (for example 10% of users first), and watch crash reports before releasing to everyone.
- **Keep your store page updated** with real changes and fresh screenshots.

A calm, prepared launch beats a rushed one. Your first week sets the tone for your ratings."""),
    ],
    diagram=timeline([("Prepare", "listing and assets"), ("Internal test", "you and your team"), ("Closed test", "real testers"), ("Submit", "for review"), ("Review", "hours to days"), ("Staged rollout", "10% then all")],
                     note="Allow extra time for the first release."),
    caption="Prepare the listing, test internally and with real testers, submit, pass review and release in stages.",
    terms=[("ASO", "App store optimisation: improving a listing so more of the right people find and install the app."), ("Feature graphic", "A banner image on a Google Play listing."),
           ("TestFlight", "Apple's service for testing builds before release."), ("App Bundle", "The Android publishing format the stores use to create optimised installs."),
           ("Staged rollout", "Releasing to a small percentage of users first, then to everyone."), ("Content rating", "A questionnaire that sets the age category of your app.")],
    mistakes=["Showing menus instead of benefits in the first screenshots.", "Forgetting to provide a demo account for the reviewer.", "A privacy declaration that does not match the app.", "Keeping the store account in someone else's name."],
    quiz=[dict(q="Which listing element do people look at most?", o=["The screenshots", "The version number", "The file size", "The developer address"], a=0,
               why="Screenshots communicate the benefit quickly, so the first few matter most."),
          dict(q="What should you give the reviewer if your app needs a login?", o=["Nothing", "Your personal password", "A working demo account and instructions", "A refund"], a=2,
               why="Reviewers cannot test what they cannot open."),
          dict(q="What is a staged rollout?", o=["Releasing to a small percentage of users first", "Removing the app", "Charging more", "Publishing screenshots twice"], a=0,
               why="It lets you watch crashes before everyone gets the update."),
          dict(q="Which is a common reason for rejection?", o=["Too many features", "Crashes, incomplete screens or a missing privacy policy", "A blue icon", "A short name"], a=1,
               why="Reviewers test on real devices and check the policy and declarations.")],
    activity="Prepare a complete store listing for your app: name, short and full description, icon, five captioned screenshots, privacy policy link and a demo account note. Ask three people what the app does from the screenshots alone.",
)

LESSONS[24] = dict(   # Updates, analytics and user feedback
    minutes=14,
    hook="Releasing your app is the beginning, not the end. The apps people love are not the ones that launched perfectly. They are the ones that kept getting better, because their makers listened to users, watched what people actually did and shipped small, careful updates. But improvement without evidence is guesswork, and updates without care break things. In this lesson you will learn how to release updates safely, how to measure what users do without invading their privacy, how to gather and respond to feedback and ratings, and how to decide what to build next with limited time.",
    sections=[
        ("Shipping updates safely", """Each update is a small risk. Reduce it:

- **Version clearly:** a version name for people (`1.4.2`) and a build number that always increases. Many teams use `major.minor.patch`.
- **Keep releases small and frequent.** Big updates hide bugs and are hard to undo.
- **Write a changelog** in plain words: “Fixed the crash when opening photos. Added search.” Users read it.
- **Test the upgrade path:** install the **old version**, add data, update to the new one and check that nothing is lost, especially database migrations.
- **Use a staged rollout** and watch crash rates before going to 100%.
- **Have a rollback plan:** you cannot easily undo an installed update, but you can **halt the rollout** and release a fix quickly, or turn off a feature using a remote flag.
- **Keep your backend compatible** with older app versions."""),
        ("Measure what users really do", """Opinions are loud and behaviour is quiet. **Analytics** show what people actually do. Tools include Firebase Analytics, PostHog and Mixpanel. Track a small set of **events** that matter:

- **Key actions:** `signup_completed`, `customer_added`, `order_paid`.
- **Funnels:** how many people complete each step of a flow, and where they drop off.
- **Retention:** how many users return after 1 day, 7 days and 30 days. This is the best sign of a useful app.
- **Active users:** daily and monthly.
- **Quality:** crash-free users, load times, error rates.

Decide the **question first**, then track just what answers it. More data is not better data."""),
        ("Analytics with respect", """Tracking can harm trust and break the law if done carelessly:

1. **Collect the minimum** and never put names, phone numbers, messages or exact locations into events.
2. **Tell people** in the privacy policy and, where needed, ask **consent**. Offer a way to opt out.
3. **Use anonymous or random ids,** not real identities, unless you truly need them.
4. **Check each SDK:** what does it collect, and where does it send it?
5. **Declare it correctly** in the stores' privacy forms.
6. **Delete old data** according to a schedule.

Under Nigeria's NDPA 2023 and similar laws, analytics that identify people are personal data. A privacy-friendly approach also builds trust, which is good for business."""),
        ("Listen to users", """Numbers tell you what happens. People tell you why. Create easy ways to hear from them:

- An **in-app feedback** option with a short form and a support email.
- **Ask for a rating at a happy moment,** for example after someone completes a task, not at launch and not repeatedly. Use the stores' official review prompts.
- **Read and reply to every review,** politely, even the angry ones. Thank people, explain fixes and invite them to contact support.
- **Short surveys** after key actions, and **conversations** with a few loyal users each month.
- **Watch for patterns** in feedback, such as five people confused by the same screen.
- **Be honest** when something is not fixed yet, and say when it will be.

Treat criticism as free research. Users who complain still care enough to tell you."""),
        ("Decide what to build next", """You will always have more ideas than time. Choose with a simple method:

1. **Collect** requests, bugs and ideas in one list.
2. **Score each item** by the value for users, the effort needed, the risk and how it supports your goal (for example weekly active users).
3. **Fix serious bugs and trust problems first,** then high-value, low-effort improvements.
4. **Plan the next release** with a small number of items, and say no to the rest, for now.
5. **Measure the result** after release: did the number you aimed at move?
6. **Keep the app healthy:** update dependencies, support new phone and system versions, and remove features that nobody uses.
7. **Know when to stop or change:** if retention stays low after real effort, talk to users again and consider a different direction.

This loop of release, measure, listen and decide is how small apps grow into lasting ones."""),
    ],
    diagram=cycle([("Release", "small and safe"), ("Measure", "events and retention"), ("Listen", "reviews and feedback"), ("Decide", "score and choose"), ("Improve", "ship the next fix")], "app24", center="Keep|improving",
                  note="Evidence, not guesses."),
    caption="Release, measure, listen, decide and improve, then repeat. It is how an app keeps getting better.",
    terms=[("Changelog", "A plain-language list of what changed in each update."), ("Funnel", "The steps of a flow showing how many users reach each one."),
           ("Retention", "The share of users who come back after a period such as 7 days."), ("Event", "A recorded user action, such as order_paid."),
           ("Staged rollout", "Releasing an update to a small share of users first."), ("Consent", "A user's clear permission for their data to be collected.")],
    mistakes=["Shipping huge updates that hide bugs.", "Tracking everything without a question to answer.", "Putting personal data in analytics events.", "Ignoring or arguing with negative reviews."],
    quiz=[dict(q="What is retention?", o=["The size of the app", "The share of users who return after a period", "The price", "The number of icons"], a=1,
               why="Retention shows whether people find the app useful enough to come back."),
          dict(q="What should you do before releasing an update with database changes?", o=["Nothing", "Test upgrading from the old version with real-looking data", "Delete the old version", "Skip the changelog"], a=1,
               why="Upgrade testing prevents lost data after an update."),
          dict(q="When is a good time to ask for a rating?", o=["At every launch", "Right after the user completes something successfully", "During an error", "Never"], a=1,
               why="A happy moment gives more positive and honest ratings."),
          dict(q="Which should never be put in an analytics event?", o=["The event name", "The app version", "A user's phone number or exact location", "The screen name"], a=2,
               why="Personal data in analytics is risky and often unnecessary.")],
    activity="Plan your first three updates: write the changelog, choose five analytics events with the question each answers, add an in-app feedback link and score ten ideas by value, effort and risk.",
)
