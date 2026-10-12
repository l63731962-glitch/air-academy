"""App Development Masterclass: deep lesson pages 1 to 8.
Same format as lessons_prompt_engineering.py: hook, sections, diagram, terms, mistakes, quiz. Quiz "a" = index of the right option.
Code examples use Dart and Flutter because the ideas are the same in every mobile toolkit. Store fees and rules change, so lessons tell students to check the store's own page."""
from diagrams import flow, timeline, grid, seq, compare, pyramid, phones

LESSONS = {
    1: dict(
        minutes=14,
        hook="Before a market trader buys a stall, she asks who walks past, what they need and what they already buy somewhere else. Too many first-time app builders do the opposite: they build for months and then ask who wants it. A mobile app is a small shop that lives in someone's pocket, and in Nigeria that pocket often holds a budget Android phone with limited storage, patchy data and a battery that must last all day. This lesson helps you choose the right idea and the right approach before you write any code.",
        sections=[
            ("Start with a user and a problem", """Every good app solves one clear problem for one clear group of people. Write it as a **one-page brief**:

- **User:** who exactly? “Students at my school” is better than “everyone”.
- **Problem:** what is hard, slow or expensive for them today?
- **Three core features:** the smallest set that solves the problem. Everything else waits.
- **Success:** how will you know it works? For example, “a student can check their timetable in under ten seconds”.

Talk to at least three real users before you build. Ask how they solve the problem now. If they already have a good solution, find a different problem."""),
            ("Native or cross-platform?", """An app can be built in two broad ways:

- **Native:** one separate app per system, in the system's own language. Kotlin for Android, Swift for iOS. You get the best speed and every phone feature, but you build and maintain two apps.
- **Cross-platform:** one codebase that runs on both. Flutter (using the Dart language) and React Native (using JavaScript) are the most popular. You write once, and reach Android and iOS.

There is also the **web app or PWA** (progressive web app), a website that can be installed to the home screen. It needs no app store, but has fewer phone features.

For a first project, a cross-platform tool is usually the fastest route. Most phones in Nigeria run Android, so test on Android first, and on a modest phone, not only on a new one."""),
            ("The app lifecycle", """A phone app does not run like a laptop program. Its life has stages:

1. **Foreground:** the app is on the screen and the user is using it.
2. **Background:** the user switched to another app. Your app is paused.
3. **Closed by the system:** the phone needs memory, so it quietly shuts your app down.

This changes how you build. A phone call can interrupt a payment at any moment. The user may return after an hour and expect to continue. So **save important data as you go**, and be ready to restore the screen when the app starts again. Never assume the app stays in memory."""),
            ("Design for real conditions", """Think about the people who will use your app:

- **Data is expensive.** Keep downloads small, compress images and avoid loading things the user did not ask for.
- **Connections drop.** Show what you already have, and explain clearly when something needs the internet.
- **Phones are modest.** Many have limited storage and memory. A small, fast app earns more installs than a heavy one.
- **Battery matters.** Avoid constant background work.
- **Languages and reading levels vary.** Use short, plain words.

Apps that respect these limits feel respectful. Apps that ignore them get uninstalled in the first week."""),
        ],
        diagram=compare(("Native", ["One app per system", "Best speed and features", "Two codebases to maintain", "Kotlin (Android), Swift (iOS)"]), ("Cross-platform", ["One codebase for both", "Faster to build and update", "Slightly less direct access", "Flutter, React Native"]), vs="or", colors=("#8A2BE2", "#00F0FF")),
        caption="Neither is always right. Choose by your team, your time and your users.",
        terms=[("Native app", "An app built separately for one system in its own language."), ("Cross-platform", "One codebase that produces apps for both Android and iOS."), ("PWA", "A website that can be installed on the home screen and works like an app."), ("App lifecycle", "The stages an app goes through: foreground, background and closed."),
               ("One-page brief", "A short plan with the user, the problem, three core features and success measure."), ("MVP", "The smallest version of an app that solves the problem and can be released.")],
        mistakes=["Building for “everyone” instead of one clear group of users.", "Testing only on a new, powerful phone.", "Assuming the app stays open and never saving data as you go.", "Starting with ten features instead of the three that matter most."],
        quiz=[dict(q="What is the best first step before building an app?", o=["Choosing a logo and colours first", "Writing a clear brief about the user and problem", "Registering a store account early", "Buying a faster phone to test on"], a=1, why="A clear user and problem keep you from building something nobody needs."),
              dict(q="What is one advantage of cross-platform tools such as Flutter?", o=["One codebase can reach Android and iOS", "They never need testing", "They only work offline", "They make apps free to publish"], a=0, why="Writing once and running on both systems saves a lot of time for a small team."),
              dict(q="Why should an app save data as the user works?", o=["Stores require it", "Because the system may close the app at any time", "It makes the screen brighter", "It removes the need for a server"], a=1, why="Phones close background apps when they need memory, so unsaved work can be lost."),
              dict(q="Which design choice respects users with expensive data?", o=["Loading every image in full size", "Playing a large video at start-up", "Downloading everything at launch", "Keeping downloads small and loading on request"], a=3, why="Small downloads save users money and make the app faster on weak connections.")],
    ),
    2: dict(
        minutes=14,
        hook="Walk into two shops that sell the same goods. In one, the shelves are labelled, the aisles are clear and you find what you want in a minute. In the other, you search for ten minutes and leave. Nothing about the goods changed. Only the layout did. App design works the same way, with one difference: the shop is only six inches wide, and the customer is holding it with one thumb, probably standing up. This lesson shows you how to plan screens, move between them and make them comfortable to use.",
        sections=[
            ("Wireframes: sketch before you build", """A **wireframe** is a simple black-and-white sketch of a screen. It shows where things go, not how they look. Draw one on paper with a pencil, one box per screen, and arrows showing how users move between them. This is called a **user flow**.

Why start on paper?

- A sketch takes five minutes. A built screen takes five hours.
- You can show it to a user and change it on the spot.
- It keeps you focused on layout and purpose, not colours.

For a first app, sketch **five screens**: for example, a home list, a detail screen, a form to add something, a profile and a settings screen. Then test the sketches by asking a classmate to “find the price of the first item” and watching where they hesitate."""),
            ("Navigation patterns", """How do users get from screen to screen? Three patterns cover most apps:

- **Bottom tabs:** three to five main areas, always visible at the bottom, within thumb reach. Best for the top-level sections of an app, such as Home, Search and Profile.
- **Stack navigation:** each tap opens a new screen on top, with a back button to return. Best for going deeper, from a list to an item to its details.
- **Drawer menu:** a hidden side menu that slides out. Best when there are many sections, but people forget what they cannot see, so use it sparingly.

The picture shows a stack: a list leads to a detail, and an Add button leads to a form. Always make the way back obvious."""),
            ("Make things easy to touch and read", """A thumb is much less exact than a mouse. Follow these basic sizes:

- **Touch targets:** at least about 48 by 48 dp on Android, or 44 by 44 points on iOS, with space between them so users do not tap the wrong one.
- **Text:** body text of at least 16 sp. Do not make users zoom.
- **Spacing:** generous margins. Crowded screens feel stressful.
- **Contrast:** dark text on a light background, or the reverse. Test in bright sunlight, because that is where people really use phones.
- **One main action per screen:** make it a clear, filled button. Secondary actions look quieter.

Put the most important actions in the lower half of the screen, where thumbs rest, not in the top corner."""),
            ("States and feedback", """A good screen is designed for more than the perfect case. Plan these **states** for every screen that shows data:

- **Loading:** show a spinner or placeholder, so the user knows something is happening.
- **Content:** the normal view.
- **Empty:** a friendly message when there is nothing yet, with a button to add the first item.
- **Error:** a plain explanation and a button to try again.

Also give **feedback** for every action: a button that changes when tapped, a message when something is saved, a clear confirmation before something is deleted. Silence makes users tap again, and again."""),
        ],
        diagram=phones(), caption="A user flow: a list leads to a detail screen, and Add leads to a form.",
        terms=[("Wireframe", "A simple sketch of a screen that shows layout, not style."), ("User flow", "The path a user takes from one screen to another."), ("Bottom tabs", "A row of main sections at the bottom of the screen."), ("Stack navigation", "Opening new screens on top of each other, with a way back."),
               ("Touch target", "The area a finger can tap to use a control."), ("Empty state", "What a screen shows when there is no data yet.")],
        mistakes=["Skipping paper sketches and building screens straight away.", "Making buttons too small or too close together.", "Hiding the way back, so users feel trapped.", "Designing only for the case when everything works and data is present."],
        quiz=[dict(q="Why start with a paper wireframe?", o=["It is cheaper than printing", "Apps require paper to be approved", "It is quick to change and keeps focus on layout", "It replaces testing"], a=2, why="A sketch takes minutes to make and change, before any code exists."),
              dict(q="Which navigation pattern suits three to five main sections?", o=["Bottom tabs", "A hidden drawer", "A pop-up message", "A scrolling banner"], a=0, why="Bottom tabs stay visible and within thumb reach."),
              dict(q="What is a good minimum size for a touch target on Android?", o=["About 12 by 12 dp", "About 24 by 24 dp", "About 100 by 100 dp", "About 48 by 48 dp"], a=3, why="Around 48 dp gives enough room for a thumb to tap accurately."),
              dict(q="What should an empty state show?", o=["A blank screen with no guidance", "A friendly message and a way to add one", "A long technical error code", "The settings page of the app"], a=1, why="An empty screen with no guidance leaves users unsure what to do.")],
    ),
    3: dict(
        minutes=15,
        hook="You do not need to become a computer scientist to build an app. You need a small toolbox of ideas and the habit of reading what the computer tells you. A recipe uses ingredients, steps, repeated actions and decisions. A program does too. In this lesson you will learn the toolbox, in Dart, the language used by Flutter. The ideas apply to Kotlin, Swift and JavaScript almost word for word, so what you learn here is never wasted.",
        sections=[
            ("Variables, lists and decisions", """A **variable** stores a value. A **list** stores several in order. An **if** statement chooses between paths. A **loop** repeats steps.

> [Dart]
> final prices = [1500, 2500, 800];
> var total = 0;
> for (final p in prices) {
>   total += p;
> }
> if (total > 3000) {
>   print("Free delivery!");
> } else {
>   print("Add more to get free delivery");
> }

Read it aloud: make a list of prices, start the total at zero, add each price, then decide. If you can say a program in plain words, you can write it."""),
            ("Functions and classes", """A **function** is a named set of steps that you can reuse. A **class** groups related data and actions together into one idea, such as an Item.

> [Dart]
> class Item {
>   final String name;
>   final int price;
>   Item(this.name, this.price);
> }
> 
> int totalOf(List<Item> items) {
>   var sum = 0;
>   for (final item in items) {
>     sum += item.price;
>   }
>   return sum;
> }

Small functions with clear names make code easy to read and test. A good rule: if you need a comment to explain what a block does, turn it into a function with a name that says it."""),
            ("State: why the screen changes", """**State** is the data that can change while the app runs: a counter, items in a cart, whether a form is valid. In Flutter, when the state changes, the screen is rebuilt to match it.

> [Dart]
> int count = 0;
> void increment() {
>   setState(() {
>     count++;
>   });
> }

You do not draw the new number yourself. You change the data inside `setState`, and the toolkit redraws the screen. The cycle in the picture is the heart of every app: the user acts, the state changes, the screen updates. Beginners often change a variable but forget to tell the toolkit, and the screen stays the same."""),
            ("Reading error messages", """Errors are not insults. They are clues. When the red screen or the red text appears:

1. **Read the first line.** It says what went wrong, such as “type 'Null' is not a subtype of type 'String'”, which means you used a value that was empty.
2. **Find your own file** in the list of lines below it. The first line that mentions your code is where to look.
3. **Check the line number**, and what the variables held at that moment.
4. **Print values** to see them, then fix one thing at a time.

When you search for help, copy the exact error text. When you ask another person or an AI assistant, show the error and the relevant code, and then make sure you understand the answer before you paste it in."""),
        ],
        diagram=flow([("USER ACTS", "Taps a|button"), ("STATE", "Data changes|in setState"), ("BUILD", "The toolkit|rebuilds"), ("SCREEN", "The user sees|the new view")], "p3", "Then the user acts again", loop=True),
        caption="Every app is this loop: act, change the state, redraw.",
        terms=[("Variable", "A named place that stores a value."), ("List", "An ordered group of values."), ("Function", "A named set of steps that can be reused."), ("Class", "A blueprint that groups related data and actions."),
               ("State", "Data that can change while the app runs and affects what the screen shows."), ("Stack trace", "The list of lines in an error message that shows where the problem came from.")],
        mistakes=["Changing a variable but not telling the toolkit, so the screen does not update.", "Writing one huge function that does ten things.", "Ignoring the first line of an error message.", "Pasting a fix you do not understand."],
        quiz=[dict(q="What is a class used for?", o=["Drawing the screen on the phone", "Naming a file in the project", "Grouping related data and actions together", "Connecting the app to the internet"], a=2, why="A class bundles data and behaviour, such as an Item with a name and a price."),
              dict(q="In Flutter, what usually makes the screen update after data changes?", o=["Restarting the phone each time", "Changing the data inside setState", "Deleting the app and reinstalling", "Waiting a minute for it to catch up"], a=1, why="setState tells the toolkit that data changed so it rebuilds the affected screen."),
              dict(q="Where should you look first in an error message?", o=["The first line, then your own file in the list", "The last line of the message only", "The size of the project file", "Nowhere, the errors are random"], a=0, why="The first line says what is wrong, and your own file shows where."),
              dict(q="What does a loop do?", o=["Stops the program from running", "Chooses between two different paths", "Gives a name to a stored value", "Repeats steps for each item in turn"], a=3, why="Loops repeat actions, such as adding every price in a list.")],
    ),
    4: dict(
        minutes=15,
        hook="A good waiter does three things when you order: he tells you the kitchen is working on it, he brings the dish, or he explains kindly that the dish is finished. He never stands silently in front of you. A good app is the same when it asks a server for data. It shows that it is working, it shows the result, or it explains what went wrong. This lesson teaches you how apps talk to servers, and how to keep them useful when the network is slow, broken or gone.",
        sections=[
            ("APIs and JSON", """Most apps get their data from a server through an **API**, a set of web addresses that return data. The data usually arrives as **JSON**, text made of names and values that both people and programs can read.

> [JSON]
> {
>   "id": 7,
>   "name": "Jollof rice",
>   "price": 1500,
>   "available": true
> }

Your app asks for this with an HTTP request, just as a browser would. The API's documentation tells you the address, the method (GET to read, POST to create) and the shape of the data. Always read the documentation first."""),
            ("Calling an API without freezing the screen", """Network calls take time, from a fraction of a second to many seconds. If your code waited on the main thread, the screen would freeze. So apps use **asynchronous** code: start the request, let the screen keep working, and continue when the answer arrives.

> [Dart]
> Future<List<Item>> loadItems() async {
>   final res = await http.get(Uri.parse("https://api.example.com/items"));
>   if (res.statusCode != 200) {
>     throw Exception("Server said ${res.statusCode}");
>   }
>   final data = jsonDecode(res.body) as List;
>   return data.map((j) => Item(j["name"], j["price"])).toList();
> }

`async` and `await` let you write the steps in order, while the toolkit handles the waiting. Note the check on the status code. A request that fails must be handled, not ignored."""),
            ("The four states of a data screen", """Every screen that shows server data has four possible faces, as the picture shows. Design and build **all four**:

- **Loading:** a spinner or grey placeholder boxes.
- **Content:** the data, shown clearly.
- **Empty:** nothing yet, with a friendly message.
- **Error:** a short human explanation and a **Try again** button. “Could not load. Check your connection.” beats “Exception 500”.

Apps that show only the happy path look broken the first time the network drops, and in real life that happens every day."""),
            ("Saving data on the phone", """Not everything should come from the internet. Phones can store data locally:

- **Simple settings** (a chosen language, a saved name) fit in a small key-value store such as shared preferences.
- **Structured data** (lists, histories, saved items) fits in a local database such as SQLite.
- **Files**, like downloaded images, are kept in the app's own storage.

**Caching** means keeping the last answer so the app can show it at once and refresh it in the background. An **offline-first** app works fully without a connection, and syncs when it is back. For users with costly or unreliable data, this is a real advantage. Decide for each piece of data: does it need to be fresh, or is yesterday's copy good enough?"""),
        ],
        diagram=grid([("Loading", "Spinner or|placeholders"), ("Content", "The data,|clearly shown"), ("Empty", "A friendly|first step"), ("Error", "Plain words and|Try again")], 4, note="Design all four states for every data screen"),
        caption="A data screen has four faces. Build every one of them.",
        terms=[("API", "A set of web addresses an app uses to get or send data."), ("JSON", "A text format for data made of names and values."), ("Asynchronous", "Code that starts a task and carries on, returning when the task finishes."), ("Cache", "A saved copy of data so it can be shown quickly or offline."),
               ("Offline-first", "Designed so the app works without a connection and syncs later."), ("Local database", "A database stored on the phone, such as SQLite.")],
        mistakes=["Showing a blank screen while data loads.", "Letting a failed request crash the app.", "Re-downloading the same large images every time.", "Showing a raw technical error to the user."],
        quiz=[dict(q="Why do apps use asynchronous code for network calls?", o=["To keep the screen responsive while waiting", "To make the phone faster overall", "To avoid using the internet", "To hide the request"], a=0, why="Waiting on the main thread would freeze the screen, so apps continue working while the answer arrives."),
              dict(q="Which is not one of the four states of a data screen?", o=["Loading", "Error", "Charging", "Empty"], a=2, why="The four states are loading, content, empty and error."),
              dict(q="What is a cache?", o=["A type of secret password", "A saved copy of data for fast or offline use", "A kind of web address", "A loading spinner on the screen"], a=1, why="Caching keeps recent data so the app can show it immediately."),
              dict(q="Which error message is best for users?", o=["Exception 500 at line 42", "null", "Could not load. Check your connection and try again", "Something is wrong with your phone"], a=2, why="Plain words and a clear next step help users recover.")],
    ),
    5: dict(
        minutes=15,
        hook="Your phone holds your messages, your photos, your bank app and your money. When someone installs your app they trust you with a small corner of that. If you lose that trust by leaking a password or collecting information you do not need, they will not forgive you, and in Nigeria the law may not either. This lesson covers how users sign in, how to keep the proof of sign-in safe, how to ask for permissions and how to protect privacy.",
        sections=[
            ("Sign-in flows", """There are several ways to let users prove who they are:

- **Email and password:** familiar, but people reuse weak passwords. You must store passwords safely on the server, as a salted hash, never as plain text.
- **One-time code (OTP):** the user enters their email or phone, receives a short code, and types it in. No password to forget or leak. Codes should expire in a few minutes and allow only a few attempts. SMS delivery can be slow or costly in some places, so email codes are a good option.
- **Social sign-in:** “Continue with Google” saves typing, and the other company handles the passwords.

Whatever you choose, keep the flow short, show clear error messages and let users recover access."""),
            ("Tokens and where to keep them", """After a successful sign-in, the server sends back a **token**, a long random string that proves who the user is. The app attaches it to every later request, so the user does not sign in again each time.

The sequence is shown in the picture. The important question is **where the app keeps the token**. Not in plain text files or ordinary preferences, where other apps or a person with the phone could read it. Use the phone's **secure storage**: the Keystore on Android and the Keychain on iOS, available through packages such as flutter_secure_storage.

Tokens should **expire**, and the app should be able to sign out by deleting the token and telling the server to cancel it."""),
            ("Do not ship secrets in the app", """An app file can be unpacked and read by anyone who downloads it. So **never put secret keys inside the app**: not payment secret keys, not database passwords, not private API keys. If the app needs to use a secret service, the app should call **your server**, and the server, which users cannot open, holds the secret and does the work.

Also always use **HTTPS** for every request, so data cannot be read on the way. And check everything on the server. The app is on the user's phone, so the user, or an attacker, controls it."""),
            ("Permissions and privacy", """Phones protect sensitive features behind **permissions**: camera, location, contacts, notifications. Follow three rules:

1. **Ask only for what you need.** A to-do app does not need the contact list.
2. **Ask at the moment you need it**, with a sentence explaining why: “Allow the camera so you can scan the receipt.”
3. **Work gracefully if the answer is no.** Offer another way to continue.

Collect the least personal data you can, tell users clearly what you keep, and let them delete it. In Nigeria, the **Nigeria Data Protection Act 2023** sets rules for handling personal data. App stores also require a **privacy policy** link, and you should write one that honestly matches what the app does."""),
        ],
        diagram=seq(["App", "Server", "Secure storage"], [(0, 1, "Email and code"), (1, 0, "A token that expires"), (0, 2, "Save the token"), (0, 1, "Request and token"), (1, 0, "The user's own data")], "p5", note="The token is the proof of sign-in, so it needs the safest place"),
        caption="Sign in once, keep the proof safe, and send it with every request.",
        terms=[("OTP", "A one-time code that proves the user controls an email or phone."), ("Token", "A secret string that proves a user is signed in."), ("Secure storage", "A protected place on the phone, such as Keystore or Keychain."), ("Permission", "The user's approval for an app to use a feature like the camera."),
               ("Hashing", "Turning a password into a scrambled value that cannot be reversed."), ("Privacy policy", "A document that explains what data the app collects and why.")],
        mistakes=["Storing the sign-in token in plain text.", "Putting a secret payment key inside the app.", "Asking for every permission as soon as the app opens.", "Collecting personal data the app does not need."],
        quiz=[dict(q="Where should an app keep a sign-in token?", o=["In secure storage, such as Keystore or Keychain", "In a plain text file on the phone", "In the name of the app itself", "In a public GitHub repository"], a=0, why="Secure storage protects tokens from other apps and from people who pick up the phone."),
              dict(q="Why must a secret key never be placed inside the app?", o=["It makes the app too large", "Stores reject apps with keys", "Anyone can unpack the app and read it", "Phones delete keys at night"], a=2, why="App files can be unpacked, so secrets inside them are not secret."),
              dict(q="When should the app ask for camera permission?", o=["As soon as the app is installed", "Never, because permissions are optional", "Every time the screen turns on", "When the user needs it, with a reason"], a=3, why="Asking in context, with a reason, makes people more likely to agree and builds trust."),
              dict(q="Why use HTTPS for every request?", o=["It makes the images much bigger", "It stops people on the network reading the data", "It removes the need for sign-in", "It is faster to type into the code"], a=1, why="HTTPS encrypts data in transit.")],
    ),
    6: dict(
        minutes=14,
        hook="A bridge engineer does not open a bridge and then ask the public to find the cracks. She tests it with heavy loads first. Your app deserves the same respect. Every crash you catch before release is a one-star review you never receive and a user you do not lose. This lesson shows you how to test in layers, where to look for the problems that only real phones reveal, and how to hear about the crashes you could not predict.",
        sections=[
            ("The testing pyramid", """Not all tests are equal. Think of a pyramid:

- **Unit tests** (the wide bottom): check one small function, such as “the total of these items is 4,800”. They are fast and cheap, so write many.
- **Widget or integration tests** (the middle): check that a screen or a few parts work together, such as “when I type a name and tap Save, the item appears in the list”.
- **End-to-end tests on a real device** (the top): walk through the whole app like a user. They are slow and a little fragile, so write only a few for the most important paths.

A good habit is to write a unit test for every bug you fix. Then that bug can never come back unnoticed."""),
            ("A manual test plan", """Automatic tests do not cover everything. A **manual test plan** is a list of test cases a person follows. Each one has **steps** and an **expected result**:

> [Test case]
> Name: Add an item
> Steps: 1. Open the app. 2. Tap Add. 3. Type “Bread”. 4. Tap Save.
> Expected: The list shows “Bread” and a message says “Saved”.
> Result: Pass / Fail

Write ten cases for the main journeys, including the unhappy ones: an empty name, no internet, a very long name. Run the plan before every release, and keep the results. Automate the two or three cases you run most often."""),
            ("Test like a real user, on real phones", """The simulator on your laptop is a good start, but it lies. Test on **real devices**, including an older, cheaper phone. Then try the things real life does:

- **Small and large screens**, and both portrait and landscape.
- **Slow or no network:** switch on aeroplane mode in the middle of a request.
- **Interruptions:** a phone call, a notification, switching to another app and back.
- **Low storage or low battery.**
- **Different Android versions.**

Ask three people who did not help you build the app to try it while you watch silently. Every time they hesitate, that is a design problem, not a user problem."""),
            ("Hearing about crashes you did not catch", """Some problems appear only after release. **Crash reporting** tools, such as Firebase Crashlytics or Sentry, record each crash with details: which screen, which phone and which line. You then fix the most common ones first.

Two more sources of truth: **beta testing**, where a small group of real users try the release candidate before everyone else, and **reviews**, where users tell you what annoys them. Read all of it, thank people for useful feedback and fix problems in small, frequent updates."""),
        ],
        diagram=pyramid([("End-to-end", "Few, on real phones"), ("Widget or integration", "Some, for key screens"), ("Unit tests", "Many, fast and cheap")], note="Many small tests, fewer big ones"),
        caption="Build a wide base of fast tests and a small top of full journeys.",
        terms=[("Unit test", "An automatic test of one small function."), ("Widget test", "An automatic test of a screen or part of a screen."), ("Test case", "A written set of steps and an expected result."), ("Real-device testing", "Trying the app on actual phones, not only a simulator."),
               ("Crash report", "An automatic record of an app crash, with details."), ("Beta test", "A trial release to a small group before everyone gets it.")],
        mistakes=["Testing only on a simulator or only on your own phone.", "Only testing the happy path.", "Writing a huge number of slow end-to-end tests and almost no unit tests.", "Ignoring crash reports and reviews after release."],
        quiz=[dict(q="Which kind of test should you have the most of?", o=["Slow end-to-end tests", "Manual tests only", "Unit tests", "No tests"], a=2, why="Unit tests are fast and cheap, so they form the wide base of the pyramid."),
              dict(q="What does a test case contain?", o=["Only the app name", "Steps and an expected result", "A list of features", "The source code"], a=1, why="A test case says what to do and what should happen."),
              dict(q="Why test on a real, older phone?", o=["It shows problems a simulator hides", "Simulators do not exist", "Old phones never crash", "It is required by stores"], a=0, why="Real hardware, memory limits and networks reveal issues that a laptop simulator can hide."),
              dict(q="What does a crash reporting tool give you?", o=["More users for your app store page", "Free storage for your photos", "A faster phone for testing", "A record of each crash and where it happened"], a=3, why="It shows which screen and device crashed, so you can fix the most common problems first.")],
    ),
    7: dict(
        minutes=15,
        hook="Finishing the code feels like finishing the app. It is not. A trader who has the best goods in town but no sign, no price tags and no way to be found sells nothing. A store listing is your sign, and a release process is your open door. Done well, release day is calm. Done badly, it is a night of confusing error messages. This lesson walks through the whole release: the store page, the signing keys, the build, the review and the updates that follow.",
        sections=[
            ("The store listing", """The store page is often the only thing a person sees before deciding to install. Prepare it carefully:

- **Name and short description:** clear and honest, saying what the app does in one line.
- **Icon:** simple and recognisable at small sizes. Google Play asks for a 512 by 512 pixel icon.
- **Screenshots:** four to eight, showing the real app, with short captions that sell the main benefit.
- **Full description:** what it does, who it is for and what makes it different. Lead with the most important sentence.
- **Privacy policy link:** required. It must be public and match what your app really does.
- **Category and contact email.**

Look at three popular apps in your category and note what their first screenshot says."""),
            ("Signing, versions and the build", """Android apps must be **signed** with a cryptographic key that proves the app and its updates come from you. Treat that key like a bank vault key: back it up safely, and never publish it. If you lose it, you may not be able to update your app. Google Play offers a service called Play App Signing, which keeps the final key for you and makes this safer.

Every release needs a **version**:

- **Version name:** what people see, like 1.2.0.
- **Version code:** a whole number that must go **up** with every upload, such as 12, 13, 14.

Google Play expects new apps to be uploaded as an **Android App Bundle** (a .aab file) rather than a plain APK. Check the store's current requirements before each release, because they change."""),
            ("Accounts, fees and review", """To publish on **Google Play**, you need a developer account. At the time of writing, this has a one-time registration fee of 25 US dollars, and you must be at least 18 and may be asked for a government ID and a card under your legal name. Personal accounts also have to meet testing requirements before an app can go to everyone. Check Google's current page for the details. If you are under 18, ask a parent or guardian, or a school or organisation, to hold the account.

The **Apple App Store** requires the Apple Developer Program, which has a yearly fee, and a Mac to build iOS apps. Check Apple's own page for the current price.

After you submit, the store **reviews** your app. Reviews can take hours to days. Common reasons for rejection: a missing privacy policy, asking for permissions you do not use, a broken sign-in for the reviewer, and crashes on launch."""),
            ("Release carefully, then keep improving", """Use the store's stages, so mistakes reach a few people before they reach everyone:

1. **Internal or closed test:** you and a small group install it first.
2. **Staged rollout:** release to 10 or 20 percent of users and watch the crash reports. If all is well, increase to 100 percent.
3. **Monitor:** watch crashes, ratings and reviews for the first days.

After release, the work continues. Fix bugs quickly, reply to reviews politely, and ship small updates with clear notes on what changed. Apps that improve steadily earn better ratings than apps that are launched and left."""),
        ],
        diagram=flow([("BUILD", "Make the|app bundle"), ("SIGN", "Prove it is|from you"), ("TEST", "Closed test|with a few"), ("REVIEW", "The store|checks it"), ("RELEASE", "Staged first,|then everyone")], "p7", "Then watch the crashes and reviews"),
        caption="Each step catches problems before they reach every user.",
        terms=[("Store listing", "The page that describes your app in the store."), ("Signing key", "A secret key that proves updates come from you."), ("Version code", "A whole number that must rise with every upload."), ("App bundle", "The file format that Google Play expects for new apps."),
               ("Staged rollout", "Releasing to a small share of users first and then more."), ("Privacy policy", "A public document explaining what data the app collects.")],
        mistakes=["Losing the signing key without a backup.", "Reusing the same version code and being unable to upload.", "Submitting without a privacy policy.", "Releasing to everyone at once with no staged rollout."],
        quiz=[dict(q="What must happen to the version code with each new upload?", o=["It must stay the same", "It must go up", "It must be a word", "It must be deleted"], a=1, why="The store uses the version code to know which build is newer."),
              dict(q="Why do a staged rollout?", o=["It makes the app free", "It removes the need for testing", "It limits the damage if a bad bug slips through", "It hides the app from reviews"], a=2, why="If only a few people receive a bad release, fewer people are affected and you can fix it."),
              dict(q="Which item do stores require you to provide?", o=["A video of yourself", "A privacy policy link", "Your phone number on the icon", "A printed manual"], a=1, why="A public privacy policy that matches the app is a standard requirement."),
              dict(q="What is a signing key for?", o=["Proving that updates really come from you", "Making the app icon smaller", "Translating the app into more languages", "Speeding up the app on old phones"], a=0, why="Signing proves the app and its updates come from the same developer.")],
    ),
    8: dict(
        minutes=15,
        hook="The best portfolio piece is not the biggest app. It is a small app that really works, that you can demonstrate on a real phone in five minutes, and that you can explain line by line. A half-finished app with twelve features impresses nobody. A finished app with three features, a clean design, tests and a store-ready listing shows that you can ship, which is the rarest skill of all. This capstone brief shows you how to scope it, build it, prove it and present it.",
        sections=[
            ("The brief", """Build a **working mobile app** that solves a real problem for a real group of users. It must have:

- **Five designed screens** and clear navigation between them.
- **The main screen** with working features.
- **Live or saved data** shown in a list.
- **Loading, empty and error states** where data is shown.
- **Sign-in or a protected screen.**
- **Testing:** a written test plan of ten cases, two of them automated, and a test on a real phone with three people.
- **A store listing draft:** icon, screenshots, description and a release checklist."""),
            ("Scope with MoSCoW", """Most projects fail by trying to do too much. Use **MoSCoW** to decide what to build:

- **Must have:** without it, the app does not solve the problem. Build these first.
- **Should have:** important, but the app still works without them.
- **Could have:** nice, if time remains.
- **Won't have (yet):** write them down so you can stop worrying about them.

A good test: if you had to launch tomorrow, which features would you keep? Those are your Musts. Be ruthless. A launched app with three features beats a perfect plan for thirty."""),
            ("Structure your code so you can explain it", """In the demo you will be asked how the code is organised. Use simple folders with clear jobs:

> [Folders]
> lib/
>   screens/    one file per screen
>   widgets/    small reusable pieces
>   models/     classes such as Item and User
>   services/   talking to the server and the local database

For each file you should be able to say what it does in one sentence. Keep functions short. Name things clearly. Put secrets nowhere in the code. Write a **README** with what the app does, how to run it and a screenshot. If you used an AI assistant for help, be ready to explain every part it wrote, because a reviewer will ask."""),
            ("The demo and the grading", """Prepare a five-minute demo **on a real phone**:

1. **Thirty seconds** on the user and the problem.
2. **Two minutes** using the app along its main journey.
3. **One minute** showing an error state, for example by switching on aeroplane mode.
4. **One minute** on the code structure and one decision you made.
5. **Thirty seconds** on what you would build next.

Have a backup: a screen recording, in case the network or the phone fails. You will be graded on meeting the brief, the quality of the build, testing, documentation and presentation. A calm demo that shows an error handled gracefully impresses more than a flawless one that hides the cracks."""),
        ],
        diagram=grid([("MUST", "Needed to solve|the problem"), ("SHOULD", "Important but|can wait"), ("COULD", "Nice if|time remains"), ("WON'T (YET)", "Written down,|not built")], 4, note="Decide before you build, and protect your scope"),
        caption="A small app that works beats a big app that does not.",
        terms=[("MVP", "The smallest version that solves the problem and can be released."), ("MoSCoW", "A way to sort features into must, should, could and won't have."), ("Release checklist", "A list of steps to complete before publishing."), ("README", "A document that explains what a project is and how to run it."),
               ("Demo", "A short live walk-through of the finished app.")],
        mistakes=["Trying to build ten features instead of finishing three.", "Demonstrating only on an emulator, with no backup plan.", "Being unable to explain code that was copied or generated.", "Skipping the test plan until the last day."],
        quiz=[dict(q="What does the M in MoSCoW stand for?", o=["Must have", "Maybe later", "Main screen", "Mobile only"], a=0, why="Must have features are those without which the app does not solve the problem."),
              dict(q="Where should you give the demo?", o=["Only on your laptop screen", "On a real phone, with a backup recording", "On a printed picture of the screen", "Without any app at all"], a=1, why="A real phone is convincing, and a recording protects you if something fails."),
              dict(q="Why show an error state in the demo?", o=["To waste some of your time", "To confuse the audience a little", "It shows the app handles problems gracefully", "To skip the main features"], a=2, why="Handling failure well is a sign of a mature app."),
              dict(q="What should you do about code you cannot explain?", o=["Hide it from the reviewer", "Leave it and hope nobody asks", "Delete the whole project", "Learn it or replace it, so you can explain it"], a=3, why="You will be asked how your project works, and you are responsible for all of it.")],
    ),
}