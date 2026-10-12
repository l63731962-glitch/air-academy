"""Full Stack Development Masterclass: deep lesson pages 1 to 8.
Same format as lessons_prompt_engineering.py: hook, sections, diagram, terms, mistakes, quiz. Quiz "a" = index of the right option.
Examples use a notes app, Python (Flask) on the back end and React-style components on the front end; the ideas carry to any stack."""
from diagrams import flow, timeline, grid, seq, compare, tree, stack, erd

LESSONS = {
    1: dict(
        minutes=14,
        hook="A restaurant has a dining room, a kitchen and a store room. Customers sit in the dining room and never see the rest. Waiters carry orders to the kitchen, cooks follow the rules of the house, and the store room keeps everything safe until it is needed. A full-stack application is built the same way, and a full-stack developer is someone who can work in all three rooms. This lesson gives you the map: the three layers, the path of one request through them and the project setup that keeps a real app organised from the first day.",
        sections=[
            ("The three layers", """Almost every web application has three layers:

- **Front end (the client):** what the user sees and touches, running in the browser. It shows data, collects input and sends requests.
- **Back end (the server):** the program with the rules. It checks who the user is, validates input, applies business logic and talks to the database.
- **Database:** the long-term memory. It stores users, notes, orders and everything else that must survive a restart.

Two rules follow, and you will use them all course. **Never trust the front end**, because users control their own browsers. And **never let the front end talk straight to the database**. The server stands between them and decides what is allowed."""),
            ("Follow one request", """The best way to understand a system is to follow one action all the way through. The picture shows a user logging in. In words:

1. The user types an email and password and clicks **Log in**.
2. The browser sends a request to the server: `POST /api/login` with the details.
3. The server asks the database for the user with that email.
4. The database returns the row, or nothing.
5. The server checks the password, and if it matches, starts a session.
6. The server replies with a success code and a session cookie.
7. The browser stores the cookie and shows the user's dashboard.

Every feature you build, saving a note, paying, uploading a photo, follows the same journey: click, request, check, database, response, screen update. When something breaks, you ask: **at which step did it stop?**"""),
            ("Client-server thinking", """The client and server are separate programs that only talk through requests and responses. This has consequences:

- **They can change independently.** As long as the messages stay the same, you can redesign the front end without touching the back end.
- **The server has no memory of the browser** between requests, unless you give it one, through cookies and sessions.
- **Everything over the network can fail or be slow.** Plan for errors and loading time from the start.
- **The browser is not safe.** Anything in your JavaScript can be read, so no secrets live there."""),
            ("Set up the project properly", """A tidy structure saves hours later. A simple layout:

> [Folders]
> notes-app/
>   frontend/    the pages and components
>   backend/     the server code
>   README.md    what the app does and how to run it
>   .gitignore   files Git must never upload, such as .env

Then create an isolated Python environment for the back end, so its libraries do not mix with other projects:

> [Terminal]
> python -m venv .venv
> source .venv/bin/activate
> pip install flask python-dotenv

On Windows, activate it with `.venv\\Scripts\\activate`. Put settings and secrets in a `.env` file that Git ignores, and start using Git from the first minute, committing after each small piece of progress."""),
        ],
        diagram=seq(["Browser", "Server", "Database"], [(0, 1, "POST /api/login"), (1, 2, "Find user by email"), (2, 1, "The user row"), (1, 0, "200 OK and a session cookie")], "f1", note="The path of a login request, from click to database and back"),
        caption="Every feature is a journey through three layers and back.",
        terms=[("Front end", "The part of the app that runs in the browser and that users see."), ("Back end", "The server program that holds the rules and talks to the database."), ("Database", "The long-term storage for the app's data."), ("Request and response", "A message from the client to the server and the answer that comes back."),
               ("Session", "A way for the server to remember a user between requests."), ("Environment", "A separate copy of the app setup, such as development or production.")],
        mistakes=["Trusting data from the browser without checking it on the server.", "Putting secret keys in front-end code.", "Letting the front end connect straight to the database.", "Starting without Git and losing work when something breaks."],
        quiz=[dict(q="Which layer holds the business rules and checks who the user is?", o=["The back end (server)", "The front end (browser)", "The user's screen", "The domain name"], a=0, why="The server applies the rules and security checks, because it is the part users cannot change."),
              dict(q="Why should the front end never talk straight to the database?", o=["Databases cannot read text", "The server must stand between and decide what is allowed", "Browsers cannot send requests at all", "It would make the page too colourful"], a=1, why="Without the server in between, anyone could read or change any data."),
              dict(q="In the login journey, who checks the password against the stored one?", o=["The browser", "The domain registrar", "The server", "The CSS file"], a=2, why="The server compares the password with the stored value, never the browser."),
              dict(q="Which file should Git ignore in your project?", o=["The README file", "The folder of page components", "The list of installed libraries", "The .env file holding secrets"], a=3, why="Secrets must never be uploaded, so .env is listed in .gitignore.")],
    ),
    2: dict(
        minutes=15,
        hook="A good shop window is arranged in a way that a stranger understands in two seconds: what is sold, what it costs and where to go in. The front end of an application is the shop window and the shop floor together. It must look right, respond quickly, work for people who tap with one thumb or navigate with a keyboard, and stay honest about what is happening when a request is slow or fails. This lesson shows you how to build it in pieces that stay under control as the app grows.",
        sections=[
            ("Think in components", """Look at the main screen of a notes app and split it into pieces: a **sidebar** with folders, a **note list**, and an **editor** with a toolbar. Each piece becomes a **component**: a small, reusable unit with one clear job. The picture shows how they nest.

Why this helps:

- **Reuse:** one `NoteItem` component serves every note in the list.
- **Focus:** you work on one small piece at a time.
- **Testing:** a small component is easy to check on its own.

A useful guide: if a component does more than one thing, or its file runs past a couple of hundred lines, split it."""),
            ("State: where should the data live?", """**State** is the data that changes while the app runs. The key question is **who owns it**.

- If **only one component** needs it, such as whether a dropdown is open, keep it inside that component.
- If **several components** need it, such as the list of notes, put it in their **closest common parent** and pass it down. This is called “lifting state up”.
- Data that lives on the server, such as the notes themselves, is not “yours”. Your state holds a **copy**, and the server remains the source of truth.

Keep state as small as you can. If you can work something out from other state, like the number of notes, calculate it instead of storing it twice. Two copies of the same fact will eventually disagree."""),
            ("Forms and calling the API", """Forms are where front ends fail most often. In React, a **controlled input** keeps what the user types in state. Show validation messages next to the field, disable the button while saving, and keep the user's text if the save fails.

Fetching data needs three pieces of state: the data, a loading flag and an error message.

> [JavaScript]
> function NotesPage() {
>   const [notes, setNotes] = useState([]);
>   const [loading, setLoading] = useState(true);
>   const [error, setError] = useState("");
> 
>   useEffect(() => {
>     fetch("/api/notes")
>       .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
>       .then(setNotes)
>       .catch(() => setError("Could not load your notes."))
>       .finally(() => setLoading(false));
>   }, []);
> 
>   if (loading) return <p>Loading…</p>;
>   if (error) return <p role="alert">{error}</p>;
>   return notes.map((n) => <NoteItem key={n.id} note={n} />);
> }

Notice that all three cases are handled: loading, error and success. An app that handles only success looks broken the first time the connection drops."""),
            ("Accessibility from the start", """Accessible apps work for everyone, including people using screen readers, keyboards or small screens, and adding it later is much harder than building it in.

- Use real **buttons and links**, not clickable divs, because they work with the keyboard for free.
- Give every input a **label**.
- Make sure the **focus order** follows the visual order, and the focus is always visible.
- Announce errors in a way screen readers notice, with `role="alert"`.
- Keep **contrast** high and **text** at a readable size.

Try your own app with the mouse unplugged. If you cannot finish the main task using the Tab, Enter and Escape keys, a lot of users cannot either."""),
        ],
        diagram=tree("NotesApp", [("Sidebar", ["FolderList"]), ("NoteList", ["NoteItem", "NoteItem"]), ("Editor", ["Toolbar", "TextBox"])], note="Pieces with one job each, nested like a family"),
        caption="Split the screen into small components, and decide who owns each piece of data.",
        terms=[("Component", "A small reusable unit of the interface with one clear job."), ("State", "Data that changes while the app runs and affects the screen."), ("Lifting state up", "Moving shared data to the closest parent so that several components can use it."), ("Controlled input", "A form field whose value is kept in state."),
               ("Source of truth", "The one place where the correct version of the data lives."), ("Accessibility", "Making an app usable by people with different abilities and devices.")],
        mistakes=["Writing one giant component that does everything.", "Storing the same fact in two places so they disagree.", "Handling only the success case of a request.", "Using clickable divs instead of real buttons."],
        quiz=[dict(q="When two components need the same data, where should it live?", o=["In the closest common parent", "In both, copied separately", "In the database only", "In a CSS file"], a=0, why="Putting the data in the closest common parent lets both read the same copy."),
              dict(q="Which three pieces of state are usually needed to fetch data?", o=["Colour, size and font of the text", "Data, a loading flag and an error message", "Username, email and phone number", "Header, body and footer text"], a=1, why="Tracking data, loading and error lets the screen show every case properly."),
              dict(q="Why prefer a real button over a clickable div?", o=["It looks more colourful on screen", "It uses less memory on the server", "It works with keyboards and screen readers", "It prevents every kind of bug"], a=2, why="Native buttons come with keyboard and accessibility behaviour built in."),
              dict(q="Where is the source of truth for the notes?", o=["In the browser's memory", "In a component's props", "In the page title", "On the server and database"], a=3, why="The front end holds a copy. The server and database hold the true version.")],
    ),
    3: dict(
        minutes=15,
        hook="Think of a good waiter at a busy restaurant. He takes orders in a fixed format, refuses a request for a dish that does not exist, politely reports when the kitchen is out of something and never hands the cook the wrong ticket. An API works the same way. Developers who build a clear, predictable API make the front end easy to write, and developers who build a messy one make everyone's life harder for years. This lesson teaches the habits of a clean back end.",
        sections=[
            ("REST: nouns and methods", """**REST** is a common style for designing APIs. The idea: URLs name **things** (nouns), and the HTTP **method** says what to do with them.

> [HTTP]
> POST   /api/notes        create a new note
> GET    /api/notes        list my notes
> GET    /api/notes/7      read note 7
> PATCH  /api/notes/7      change note 7
> DELETE /api/notes/7      delete note 7

These five endpoints are called **CRUD**: create, read, update, delete. Use plural nouns, keep URLs lowercase, and never put verbs in the path, such as /api/deleteNote. Return the right **status code** every time: 201 for created, 400 for bad input, 401 when not signed in, 404 when not found, 500 for a server fault."""),
            ("Validate every request", """Treat every request as untrusted. Check **type, presence, length and format** before doing anything.

> [Python]
> @app.patch("/api/notes/<int:note_id>")
> def update_note(note_id):
>     data = request.get_json(silent=True) or {}
>     title = str(data.get("title", "")).strip()
>     if not title or len(title) > 200:
>         return jsonify(error="Title must be 1 to 200 characters"), 400
>     note = notes.get(note_id)
>     if note is None:
>         return jsonify(error="Note not found"), 404
>     note["title"] = title
>     return jsonify(note), 200

The order matters: validate the input first, then find the record, then act. And only accept the fields you expect. Never copy a whole request into the database, because a user could slip in a field like is_admin."""),
            ("Errors that help", """Decide on **one error format** and use it everywhere:

> [JSON]
> { "error": "Title must be 1 to 200 characters", "field": "title" }

The front end can then show the message beside the right field. Rules for good error handling:

- **Tell the user what to fix**, in plain words.
- **Do not leak internals.** Never send stack traces, file paths or SQL errors to the client. Log them on the server instead.
- **Catch the unexpected.** A last-resort handler turns any crash into a clean 500 response with a short message, while the details go to the logs."""),
            ("Structure the code in layers", """If every route contains its own validation, business rules and SQL, the code becomes a tangle. Split it into layers, as in the picture:

- **Routes:** receive the request, call the service, return the response. Thin and boring.
- **Services:** the business rules, such as “a free user can have at most 50 notes”.
- **Data access:** the only place that writes SQL.

Each layer talks only to the one below it. Now you can change the database without touching the routes, and you can test the business rules without a web server. This small habit is what separates a weekend project from something a team can maintain."""),
        ],
        diagram=stack([("Routes", "Receive requests and send responses"), ("Services", "Business rules and decisions"), ("Data access", "The only place that writes SQL"), ("Database", "Long-term storage")], "f3", both=True),
        caption="Each layer has one job and talks only to its neighbour.",
        terms=[("REST", "A style of API design where URLs name things and methods say what to do."), ("CRUD", "Create, read, update and delete: the four basic data actions."), ("Endpoint", "A URL and method combination that the API answers."), ("Validation", "Checking that input is complete, correct and safe."),
               ("Service layer", "The part of the code that holds the business rules."), ("Status code", "A number that tells the client how a request went.")],
        mistakes=["Putting verbs in URLs, such as /api/deleteNote.", "Sending stack traces or SQL errors to the client.", "Copying the whole request body into the database.", "Mixing routes, rules and SQL in one huge function."],
        quiz=[dict(q="Which URL and method follow REST style for deleting note 7?", o=["GET /api/deleteNote?id=7", "POST /api/removeNoteNow", "DELETE /api/notes/7", "PUT /api/notes/delete/7"], a=2, why="REST uses the method DELETE on the URL that names the thing."),
              dict(q="Which status code means a new record was created?", o=["201", "404", "500", "401"], a=0, why="201 Created is the correct response after a successful create."),
              dict(q="Why avoid sending stack traces to the client?", o=["They are always far too short", "They reveal internals that help attackers", "Browsers cannot display them at all", "They make the response load faster"], a=1, why="Internal details show attackers how your system works. Log them privately instead."),
              dict(q="What is the job of the data access layer?", o=["Drawing the page for the user", "Choosing the colours of the site", "Sending emails to every user", "Being the only code that writes SQL"], a=3, why="Keeping SQL in one layer makes it easier to change and to test.")],
    ),
    4: dict(
        minutes=15,
        hook="A school keeps a register of students, a list of classes and a record of who attends which class. It would never write the full address of each student next to every class, because when the student moves, you would have to change it in twenty places. Databases solve the same problem by splitting information into tables and linking them. Done well, the data stays accurate and fast. Done badly, it slowly fills with contradictions. This lesson shows you how to model data, ask it questions and look after it.",
        sections=[
            ("Tables, keys and relations", """A relational database stores facts in **tables**. A table has **columns** (the kinds of facts) and **rows** (one item each). Two kinds of columns tie everything together:

- A **primary key (PK)** uniquely identifies each row, such as the id of a user.
- A **foreign key (FK)** holds another table's primary key, linking the two. In the picture, `notes.user_id` points to `users.id`.

That link is a **one-to-many relation**: one user has many notes. Store each fact **once**, in the right place, and link to it. A note stores `user_id`, not a copy of the user's name and email. When the user changes their email, you change one row."""),
            ("Asking questions with SQL", """You read and combine data with **SQL**. A **JOIN** combines rows from two tables using the link between them.

> [SQL]
> SELECT users.name, notes.title
> FROM notes
> JOIN users ON users.id = notes.user_id
> WHERE users.id = 3
> ORDER BY notes.id DESC
> LIMIT 20;

Read it as: take the notes, match each with its user, keep only user 3's, newest first, at most 20. Always add a `WHERE` to restrict the rows and a `LIMIT` to cap the result, so a growing table never overloads your server. Use **placeholders** for any value that came from a user."""),
            ("Migrations: changing the structure safely", """Your app will change, and so will the tables. A **migration** is a small, numbered script that changes the database structure, for example adding a column:

> [SQL]
> ALTER TABLE notes ADD COLUMN pinned BOOLEAN NOT NULL DEFAULT FALSE;

Keep migrations in your project, in order, and run them the same way on every machine. Then your laptop, your test server and your live server all end up with the same structure, and the history is in Git. Never change a live database by hand and forget to record it.

Make changes in steps that old code can survive: add a column first, deploy code that uses it, and only later remove the old one."""),
            ("Indexes, transactions and backups", """Three ideas keep a database fast and safe:

- **Index:** like the index at the back of a book. Without one, the database reads every row to find user 3's notes. With `CREATE INDEX idx_notes_user ON notes(user_id);` it jumps straight there. Index the columns you search and join on, but not everything, because each index slows down writes.
- **Transaction:** a group of changes that succeed **all together or not at all**. When you move 5,000 naira between two accounts, subtracting from one and adding to the other must not be separated by a crash.
- **Backup:** a copy you can restore. A backup that you have never restored is only a hope. Schedule automatic backups and practise a restore."""),
        ],
        diagram=erd(), caption="One user has many notes. The foreign key user_id links each note to its owner.",
        terms=[("Primary key", "A column that uniquely identifies each row in a table."), ("Foreign key", "A column that points to a row in another table."), ("JOIN", "A SQL operation that combines rows from two tables using a link."), ("Migration", "A numbered script that changes the database structure."),
               ("Index", "A structure that helps the database find rows quickly."), ("Transaction", "A group of changes that all succeed or all fail.")],
        mistakes=["Copying the same fact into many tables.", "Searching a big table with no index on the column.", "Changing the live database by hand with no migration.", "Keeping backups but never testing a restore."],
        quiz=[dict(q="What does a foreign key do?", o=["Links a row to a row in another table", "Encrypts the whole table of data", "Deletes old data after a month", "Gives the database its own name"], a=0, why="A foreign key stores another table's primary key to create a relation."),
              dict(q="Why store a user's email in one place only?", o=["Emails are far too long to repeat", "It saves a little screen space", "One update fixes it, and copies cannot disagree", "Databases can only hold one email"], a=2, why="Storing each fact once avoids contradictions."),
              dict(q="What does an index help with?", o=["Making backups much smaller", "Finding rows faster in a search or join", "Hiding private data from users", "Writing new rows faster"], a=1, why="An index lets the database jump to matching rows instead of reading every row."),
              dict(q="What does a transaction guarantee?", o=["Faster queries on big tables", "Free extra storage space", "Shorter names for the columns", "A group of changes all succeed or none do"], a=3, why="Transactions prevent half-finished changes, like money leaving one account and never arriving.")],
    ),
    5: dict(
        minutes=16,
        hook="A bank that checks your identity at the door but then lets you walk into any customer's safe deposit box has failed at security even though the guard did his job. Real security in an application has two separate questions. Who are you, and what are you allowed to do? And it must also survive people who deliberately try to break it. This is the lesson that protects your users' data, your reputation and, under Nigerian law, possibly you. Take it slowly, because mistakes here are expensive.",
        sections=[
            ("Authentication: proving who you are", """**Authentication** answers “who are you?”. Common methods:

- **Passwords:** never store them as text. Store a **salted hash** made with a slow, purpose-built function such as bcrypt or Argon2. A hash cannot be turned back into the password, and the salt makes two identical passwords produce different hashes.
- **One-time codes (OTP):** the user receives a short-lived code by email or SMS. No password to leak. Make codes expire in minutes, limit attempts and store only a hash of the code.
- **Sessions or tokens:** after login, the server gives the browser a **session cookie** or a **token**. Every later request carries it, so the user does not log in each time. Cookies should be marked **HttpOnly** (JavaScript cannot read them), **Secure** (HTTPS only) and **SameSite**.

Always use HTTPS, and limit login attempts to slow down guessing."""),
            ("Authorization: what are you allowed to do?", """**Authorization** answers “what may this user do?”. It must be checked **on every request, on the server**. The most common serious bug in apps is a user who can see another user's data by changing an id in the address.

> [Python]
> note = db.get_note(note_id)
> if note is None or note["user_id"] != current_user_id:
>     return jsonify(error="Not found"), 404

This makes a route **owner-only**. Notice that it answers 404, not “this belongs to someone else”, so the response does not even confirm that the note exists. Apply the same idea with roles, such as admin and student: check the role on the server for every protected action."""),
            ("SQL injection", """In **SQL injection**, an attacker types SQL into a form field and your code runs it as a command.

> [Python]
> # DANGEROUS: the user's text becomes part of the command
> db.execute("SELECT * FROM users WHERE email = '" + email + "'")
> # SAFE: the value travels separately, as data
> db.execute("SELECT * FROM users WHERE email = ?", (email,))

With the dangerous version, an email like `x' OR '1'='1` returns every user. The safe version, called a **parameterised query**, treats the text only as data. The placeholder style differs by library (`?` or `%s`), but the rule never changes: never build SQL by joining strings."""),
            ("XSS, CSRF and the rest", """Two more attacks every full-stack developer must know:

- **XSS (cross-site scripting):** an attacker gets a script into your page, usually through user-written text that you show to others. Defence: escape output (frameworks do this by default), avoid `innerHTML` with user text and use a content security policy.
- **CSRF (cross-site request forgery):** another website tricks a logged-in user's browser into sending a request to yours, using the cookie automatically. Defence: **SameSite cookies**, CSRF tokens for state-changing requests and checking the request's origin.

Add the basics: **rate limiting**, up-to-date libraries, secrets only in the environment and logging of suspicious events. If you store personal data of people in Nigeria, the **Nigeria Data Protection Act 2023** expects you to protect it, collect only what you need and handle it lawfully."""),
        ],
        diagram=compare(("Authentication", ["Who are you?", "Password, code or token", "Done at login", "Failure: 401 Not signed in"]), ("Authorization", ["What may you do?", "Ownership and roles", "Checked on every request", "Failure: 403 or 404"]), vs="then", colors=("#00F0FF", "#8A2BE2")),
        caption="First prove who you are, then check what you are allowed to do, every time.",
        terms=[("Authentication", "Proving who a user is."), ("Authorization", "Deciding what a user is allowed to do."), ("Salted hash", "A scrambled form of a password that cannot be reversed and differs per user."), ("SQL injection", "An attack that sneaks SQL commands through user input."),
               ("XSS", "An attack that runs an attacker's script in other users' browsers."), ("CSRF", "An attack that makes a user's browser send an unwanted request to your site.")],
        mistakes=["Storing passwords as plain text or with a fast, simple hash.", "Checking permissions only in the front end.", "Building SQL by joining strings with user input.", "Returning data for any id without checking who owns it."],
        quiz=[dict(q="How should a password be stored?", o=["As plain text", "As a salted hash made with a slow function like bcrypt", "Encrypted with a key kept beside it", "As the first letters only"], a=1, why="A salted, slow hash cannot be reversed, so a leak does not reveal passwords."),
              dict(q="A user changes the id in the address and sees another person's note. What is missing?", o=["A bigger and faster server", "A nicer looking error page", "A server-side authorization check", "More images on the page"], a=2, why="Every request must check that the signed-in user owns the record."),
              dict(q="What is the safest way to put user text into a SQL command?", o=["Join the strings together", "Use a parameterised query with placeholders", "Remove all spaces", "Convert it to capital letters"], a=1, why="Placeholders keep the text as data, so it can never become a command."),
              dict(q="What does the HttpOnly flag on a cookie do?", o=["Speeds up the cookie", "Makes the cookie bigger", "Deletes the cookie after a day", "Stops JavaScript from reading the cookie"], a=3, why="HttpOnly cookies cannot be stolen by scripts, which limits the damage of an XSS attack.")],
    ),
    6: dict(
        minutes=14,
        hook="A single carpenter can build a stool alone. A team of ten building a house needs drawings, an agreed order of work, someone checking measurements and notes that explain what was done. The same applies to software. The moment more than one person touches a codebase, or the moment you return to your own code after six months, you depend on tests, a clear workflow and good documentation. This lesson covers those practices, which together make code something other people can safely change.",
        sections=[
            ("Tests that protect you", """Automatic tests check that your code still works after every change. Two kinds matter most:

- **Unit tests:** check one small function, such as one that decides whether a title is valid.
- **API tests:** call your real endpoints and check the status code and the response.

> [Python]
> def test_create_note_requires_title(client, auth):
>     res = client.post("/api/notes", json={"title": ""}, headers=auth)
>     assert res.status_code == 400
> 
> def test_cannot_read_someone_elses_note(client, auth_ada, tunde_note_id):
>     res = client.get(f"/api/notes/{tunde_note_id}", headers=auth_ada)
>     assert res.status_code == 404

Notice that the second test protects a security rule. Test the **unhappy paths** as much as the happy ones: empty input, missing sign-in, someone else's data. Every time you fix a bug, first write a test that fails because of it, so it can never return."""),
            ("A Git workflow for teams", """Teams avoid chaos with a simple, shared routine:

1. **Branch:** create a branch from main for one task, with a clear name such as fix-login-error.
2. **Commit:** make small commits with clear messages.
3. **Pull request:** open a pull request describing what changed and why, and how to test it.
4. **Review:** a teammate reads the changes and comments.
5. **Merge:** after approval, and after the automatic tests pass, merge into main.

Keep pull requests **small**. A review of 50 lines is careful. A review of 2,000 lines is a rubber stamp. Never push straight to main, and never leave a branch unmerged for weeks, or merge conflicts pile up."""),
            ("Code review: kind and useful", """A review is a conversation about the code, not about the person. Good reviewers:

- **Understand first,** then judge. Ask questions: “What happens if this list is empty?”
- **Comment on the code, not the coder.** “This function could be shorter” is better than “you wrote this badly”.
- **Separate must-fix from nice-to-have,** so the author knows what blocks the merge.
- **Praise good work.** It shows what to repeat.

As the author, read your own pull request before asking anyone else. You will often catch the mistake yourself. And be grateful for feedback: every review is free teaching."""),
            ("Documentation people actually read", """Three documents are worth the time:

- **README:** what the project is, how to run it, how to run the tests and how to deploy. A new teammate should get it running in under 30 minutes using only the README.
- **API documentation:** each endpoint, what it needs, what it returns and the possible errors. Even a simple table works.
- **Decision notes:** short records of why you chose something, such as “We use sessions, not tokens, because the app runs in one domain.”

Keep them next to the code, in the repository, and update them in the same pull request that changes the behaviour. Old documentation is worse than none."""),
        ],
        diagram=flow([("BRANCH", "One task,|one branch"), ("TEST", "Run the|checks"), ("OPEN PR", "Explain the|change"), ("REVIEW", "A teammate|reads it"), ("MERGE", "Into main|when approved")], "f6", "Comments from the review loop back into the branch", loop=True),
        caption="Small steps, checked by machines and by people, keep a team fast and safe.",
        terms=[("Unit test", "An automatic test of one small piece of code."), ("API test", "An automatic test that calls an endpoint and checks the response."), ("Pull request", "A proposal to merge a branch, open for review and discussion."), ("Code review", "Teammates reading and commenting on changes before they are merged."),
               ("README", "The main document that explains a project and how to run it."), ("Regression", "A bug that returns after having been fixed.")],
        mistakes=["Only testing the happy path.", "Pushing straight to main with no review.", "Opening huge pull requests that nobody can review properly.", "Letting the documentation drift away from the code."],
        quiz=[dict(q="What is the purpose of writing a failing test before fixing a bug?", o=["It makes the code run slower", "It proves the bug exists and stops its return", "It removes the need for any review", "It changes the database structure"], a=1, why="The test captures the bug, and then guards against its return."),
              dict(q="Why keep pull requests small?", o=["Git limits their size", "Small ones are easier to review carefully", "Reviewers prefer less code to exist", "Large ones are not allowed on GitHub"], a=1, why="Reviewers can understand and check a small change much better."),
              dict(q="Which review comment is most helpful?", o=["You always write bad code", "This is wrong", "What happens if this list is empty?", "Fix it"], a=2, why="A specific question about the code helps without blaming the person."),
              dict(q="Where should project documentation live?", o=["In one person's head", "On a loose sheet of paper", "In a chat group that scrolls away", "In the repository, next to the code"], a=3, why="Keeping docs in the repository lets them change together with the code.")],
    ),
    7: dict(
        minutes=15,
        hook="Opening day for a restaurant is not the end of the work. It is the start of a different kind of work: keeping the gas on, the fridge cold, the books straight, and noticing at once when something goes wrong. Software is the same. Getting your app onto a server where real people can use it is one step. Keeping it running, updating it without drama and finding out about problems before your users do is the discipline called operations. This lesson shows you how a modern team does it.",
        sections=[
            ("Environments and configuration", """Real teams run the same app in several **environments**:

- **Development:** your own computer, where you experiment.
- **Staging (test):** a copy of the live setup, used to test before release.
- **Production:** the real one, with real users and real data.

The code is the same in all three. What changes is the **configuration**: database addresses, secret keys, email settings. Keep configuration in **environment variables**, never in the code, so you can deploy the same build anywhere. And never test on the production database."""),
            ("Running the app for real", """The small server that Flask starts for development is not meant for the public. In production, use a proper application server, such as gunicorn on Linux or waitress on Windows, behind HTTPS:

> [Terminal]
> gunicorn app:app --workers 2 --bind 0.0.0.0:8000

Several workers let the app handle more than one request at a time. Where does it run? Options range from a virtual machine you manage yourself, to a platform that runs your code or container for you. A platform is simpler for a first project. Whatever you choose, add a **health endpoint**, such as /health, that returns 200 when the app is alive, so the platform and your monitor can check it."""),
            ("CI/CD: automate the release", """A **pipeline** runs the same steps every time, so releases are boring, which is exactly what you want:

1. **Push** your code.
2. **Test:** the automatic tests run. If any fail, the pipeline stops.
3. **Build:** the app is packaged.
4. **Deploy:** the package is released to staging, and then to production.
5. **Monitor:** you watch the result.

Database changes need care. Run **migrations** as part of the deploy, and write them so that the **old version of the code still works** while the new one starts. Then a deploy can be rolled back without breaking the data."""),
            ("Logs, monitoring and rollbacks", """You cannot fix what you cannot see:

- **Logs:** a written record of what the app does, including errors, with times. Write them to standard output so the platform can collect them. Never log passwords, tokens or full personal details.
- **Metrics and alerts:** watch error rate, response time and uptime. Alert on things that need action, not on every blip.
- **Rollback:** the ability to return to the previous good version quickly. When a release breaks things, **roll back first, investigate after**.

Afterwards, write a short, blame-free **post-mortem**: what happened, why, how you noticed and what will prevent it next time. Teams that learn from failures stop repeating them."""),
        ],
        diagram=flow([("PUSH", "Code goes|to GitHub"), ("TEST", "Checks run|automatically"), ("BUILD", "Package|the app"), ("DEPLOY", "Staging, then|production"), ("MONITOR", "Logs and|alerts")], "f7", "If monitoring shows trouble: roll back first"),
        caption="A pipeline makes every release the same, and every failure reversible.",
        terms=[("Environment", "A separate setup where the app runs, such as development, staging or production."), ("Configuration", "Settings that change between environments, kept outside the code."), ("Pipeline", "An automatic series of steps from code push to release."), ("Health endpoint", "A URL that reports whether the app is running properly."),
               ("Rollback", "Returning to the previous working version."), ("Post-mortem", "A blame-free write-up of what went wrong and how to prevent it.")],
        mistakes=["Running the development server in production.", "Testing new code directly on the live database.", "Logging passwords or tokens.", "Investigating a broken release for hours instead of rolling back first."],
        quiz=[dict(q="Where should secret keys and database addresses be stored?", o=["In the source code of the app", "In the title of the page", "In environment variables, per environment", "In the README of the project"], a=2, why="Configuration outside the code lets the same build run safely in every environment."),
              dict(q="What does staging give you?", o=["A live-like copy to test before release", "A place for the public users", "A faster database for the team", "A way to skip the tests"], a=0, why="Staging lets you catch problems in a safe copy, not on real users."),
              dict(q="A release breaks the site. What should you do first?", o=["Write a long email", "Roll back to the previous good version", "Delete the logs", "Blame the last developer"], a=1, why="Restoring service quickly comes first. Investigate once users are safe."),
              dict(q="Why avoid logging tokens and passwords?", o=["Logs are always deleted at night", "They make logs look too colourful", "Logs are not able to hold text", "Anyone with log access could misuse them"], a=3, why="Logs are widely readable, so secrets in them become a security leak.")],
    ),
    8: dict(
        minutes=16,
        hook="By now you have learned each room of the house. This capstone asks you to build the whole house and let the visitor walk through it: a deployed application in which people log in, save their own data, see it again tomorrow and cannot see anyone else's. It is the project that proves you are a full-stack developer. Choose something small enough to finish and real enough to be proud of, and use every habit from this course: plan, test, review, document and deploy.",
        sections=[
            ("The brief", """Build and deploy a **complete application** where users can sign in and manage their own data. For example: a notes app, a small shop with orders, a study planner or a booking tool. It must have:

- **A database** with at least two related tables.
- **An API** with create, read, update and delete endpoints, with validation and consistent errors.
- **A front end** with the main screens that call the API and handle loading and error states.
- **Login,** and data that is **private** to each user, enforced on the server.
- **At least five automated tests,** including one for a security rule.
- **Deployment** with environment variables for secrets, plus logging and one alert.
- **A README** with setup steps and API documentation."""),
            ("Plan the architecture first", """Before writing code, write a short **architecture note** of one page:

1. **The idea** in one sentence, and who uses it.
2. **The data:** a diagram of your tables and how they link.
3. **The API:** a list of endpoints with method, path, what it needs and what it returns.
4. **The screens:** a rough sketch of each.
5. **Security rules:** who may see or change what.
6. **Risks:** the two things most likely to go wrong, and what you will do about them.

This note will save you days. It is also the first thing you show in your demo, to prove you planned the system instead of stumbling into it."""),
            ("Build in thin slices", """Do not build all the database, then all the API, then all the screens. Build **thin vertical slices**: one small feature all the way from screen to database, working end to end, then the next. For example:

1. Register and log in, with a protected page.
2. Create a note and see it in the list.
3. Edit and delete a note.
4. Make sure a second user cannot see the first user's notes.
5. Add validation, error messages and loading states.
6. Deploy, then add logging and the alert.

After each slice, commit, run the tests and, from step 1 on, keep a working version. Then at any moment you have something that runs, even if it is small."""),
            ("Demo and grading", """In your five-minute live demo:

- **One minute:** the idea and the architecture diagram.
- **Two minutes:** the live app. Register two users and show that each sees only their own data.
- **One minute:** the tests running, the pipeline or deploy, and a log line or alert.
- **One minute:** one hard decision and one bug you fixed.

Be ready for questions: “Where is this checked?”, “What if the database is down?”, “How do you stop another user reading this?” You will be marked on the brief, the quality of the build, testing, documentation and presentation. If you used an AI assistant, you must be able to explain every line."""),
        ],
        diagram=timeline([("Plan", "One-page|architecture"), ("Slice 1", "Login and a|protected page"), ("Slice 2", "Create, read,|update, delete"), ("Slice 3", "Private data|per user"), ("Harden", "Tests, errors,|validation"), ("Ship", "Deploy, monitor,|demo")], note="Always keep a working version"),
        caption="Build thin slices that work end to end, instead of whole layers one at a time.",
        terms=[("Architecture note", "A short document that describes the data, API, screens and rules before building."), ("Vertical slice", "One small feature built through every layer, from screen to database."), ("Private data", "Data that only its owner may see, enforced on the server."), ("Deployment", "Putting the app on a server where real users can use it."),
               ("Demo", "A short live walk-through of the finished project.")],
        mistakes=["Building every layer completely before connecting them.", "Skipping the test that proves one user cannot read another's data.", "Writing the README on the last night.", "Presenting code you cannot explain."],
        quiz=[dict(q="What is a vertical slice?", o=["All the database tables at once", "One feature built through every layer", "A picture of the whole app", "A server located in another country"], a=1, why="Slices give you a working app early and reveal problems between layers sooner."),
              dict(q="How should private data be protected?", o=["By hiding the link in the page", "By a note telling users to be honest", "By checks on the server for every request", "By a long password only for you"], a=2, why="Only server-side checks reliably stop users from reading others' data."),
              dict(q="What should the architecture note contain?", o=["The data, API, screens, security rules and risks", "Only a logo and a project name", "A list of favourite tools and fonts", "Nothing, because the code is enough"], a=0, why="Planning the system before coding prevents rework."),
              dict(q="Why register two users in the demo?", o=["To use more storage", "To test the sign-in page layout", "To make the demo longer", "To show that each user sees only their own data"], a=3, why="It proves your privacy rules work in practice.")],
    ),
}