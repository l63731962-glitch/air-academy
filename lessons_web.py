"""Web Development Masterclass: deep lesson pages 1 to 8.
Same format as lessons_prompt_engineering.py: hook, sections, diagram, terms, mistakes, quiz. Quiz "a" = index of the right option.
Code goes in "> [HTML]" style boxes (a first line in square brackets names the box)."""
from diagrams import flow, timeline, grid, seq, tree, compare, boxmodel

LESSONS = {
    1: dict(
        minutes=14,
        hook="When you type a shop's address into your phone and the page appears, it feels like magic. It is actually a conversation that takes less than a second. Your browser asks a directory where the shop is, travels to that address, and asks for the page. A computer there hands back a file full of instructions, and your browser turns those instructions into what you see. Once you understand this conversation, every other part of web development has a place to sit.",
        sections=[
            ("What happens when you open a website", """Follow the journey in the picture above:

1. You type a **URL**, a web address such as https://myshop.ng/index.html.
2. The browser asks a **DNS** service, a kind of phone book, for the numeric address of myshop.ng.
3. The browser contacts the **server**, a computer that stores the website, and sends a **request**: “GET /index.html”.
4. The server sends back a **response**: a status code and the page.
5. The browser reads the page and draws it on your screen.

The language of this conversation is **HTTP**. When the address starts with https, the conversation is encrypted, so people on the network cannot read it. Every site you build should use HTTPS."""),
            ("HTML: the structure of a page", """**HTML** (HyperText Markup Language) describes what is on a page: headings, paragraphs, images, links and forms. It is not a programming language, it is a set of labels called **tags**. Most tags come in pairs, an opening and a closing tag, around the content.

> [HTML]
> <!doctype html>
> <html lang="en">
>   <head>
>     <meta charset="utf-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1">
>     <title>Ada's Bakery</title>
>   </head>
>   <body>
>     <h1>Ada's Bakery</h1>
>     <p>Fresh bread, baked every morning in Yaba.</p>
>   </body>
> </html>

The `head` holds information about the page, such as its title. The `body` holds what visitors see. The viewport line tells phones to show the page at the right size, and you will need it in every page you build."""),
            ("Semantic tags: say what things are", """You could build a whole page out of `div` tags, but then nothing says what each part is. **Semantic tags** describe the role of each part:

- `header` for the top of the page or a section, `nav` for the main menu, `main` for the central content, `section` and `article` for blocks of content, `footer` for the bottom.
- `h1` to `h6` for headings, with one `h1` per page and the others in order.
- `ul` and `li` for lists.

Why bother? Screen readers use these tags to help blind users move around. Search engines use them to understand your page. And your own code becomes easier to read."""),
            ("Links, images and forms", """Three tags make a page useful:

> [HTML]
> <a href="/menu.html">See our menu</a>
> <img src="bread.jpg" alt="A golden loaf of bread on a wooden board" width="600" height="400">
> <form action="/order" method="post">
>   <label for="name">Your name</label>
>   <input id="name" name="name" required>
>   <button type="submit">Order</button>
> </form>

Notice the details that beginners forget. Every image needs an **alt** text that describes it, for users who cannot see it and for slow connections. Every input needs a **label** linked by its id. Setting a width and height stops the page from jumping as the image loads. Keep images small: many visitors use mobile data, and big files cost them money."""),
        ],
        diagram=seq(["Browser", "DNS", "Server"], [(0, 1, "Where is myshop.ng?"), (1, 0, "It is at 203.0.113.7"), (0, 2, "GET /index.html"), (2, 0, "200 OK and the page")], "w1", note="Every page you visit starts as this four-step conversation"),
        caption="A web page is a request and a response, many times a day.",
        terms=[("URL", "A web address, such as https://myshop.ng/index.html."), ("DNS", "A directory that turns a name into the numeric address of a server."), ("HTTP / HTTPS", "The language browsers and servers use to talk. HTTPS is the encrypted version."), ("Server", "A computer that stores a website and answers requests."),
               ("HTML tag", "A label such as p or h1 that tells the browser what a piece of content is."), ("Semantic HTML", "Using tags that describe the meaning of each part of a page."), ("Alt text", "A text description of an image for people who cannot see it.")],
        mistakes=["Building the whole page from div tags with no meaning.", "Forgetting alt text on images.", "Leaving out the viewport line, so phones show a tiny page.", "Putting several h1 headings on one page and skipping heading levels."],
        quiz=[dict(q="What does DNS do?", o=["Draws the page on the screen", "Turns a name into the address of a server", "Stores the images of a site", "Encrypts the page content"], a=1, why="DNS works like a phone book, turning myshop.ng into a numeric address."),
              dict(q="Which tag is best for the main menu of a site?", o=["footer", "p", "nav", "img"], a=2, why="The nav tag labels the main navigation, which helps users and screen readers."),
              dict(q="Why does every image need alt text?", o=["It describes the image when it cannot be seen", "It makes the image load faster", "It changes the image colour", "It adds a border"], a=0, why="Alt text helps blind users, and shows when an image fails to load."),
              dict(q="What does the https at the start of an address tell you?", o=["The site is completely free to use", "The site has no images on any page", "The site is always very fast", "The connection to the site is encrypted"], a=3, why="HTTPS encrypts the conversation between browser and server.")],
    ),
    2: dict(
        minutes=15,
        hook="A good tailor measures the customer first. A page with no styling is a customer with no clothes: all the content is there but nothing fits. CSS is the clothing. It decides colours, sizes and layout, and the clever part is making one set of clothes fit a small phone in a danfo in Lagos traffic and a big desktop monitor in an office. Most of your visitors in Nigeria will arrive on a phone, so this lesson teaches you to design for the small screen first.",
        sections=[
            ("Selectors and the box model", """**CSS** is a list of rules. Each rule has a **selector** that says which elements to style, and **declarations** that say how.

> [CSS]
> .card {
>   padding: 16px;
>   border: 1px solid #ccc;
>   border-radius: 12px;
>   margin-bottom: 20px;
> }

Every element on a page is a rectangular **box**, with four layers shown in the picture: the **content**, then **padding** (space inside), then the **border**, then **margin** (space outside). Almost every layout problem is a question about one of these four layers. A helpful line to add at the top of your CSS is `box-sizing: border-box;` so that padding and border are counted inside the width you set, which makes sizes behave the way you expect."""),
            ("Flexbox and grid", """Two layout tools do most of the work:

- **Flexbox** lays items out in a **row or a column**, and spreads or aligns them. Perfect for menus, card rows and centring things.
- **Grid** lays items out in **rows and columns together**. Perfect for page layouts and photo galleries.

> [CSS]
> .cards {
>   display: grid;
>   grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
>   gap: 16px;
> }

This one rule is powerful: it fits as many 220-pixel-wide cards in each row as will fit, and the cards share any extra space. On a phone you get one column, on a laptop you get four, without writing a single media query."""),
            ("Responsive, mobile-first design", """**Responsive design** means one page that adapts to any screen. The method is **mobile-first**: write the styles for the small phone screen first, then add rules for bigger screens using a **media query**.

> [CSS]
> .menu { display: block; }
> @media (min-width: 768px) {
>   .menu { display: flex; gap: 24px; }
> }

Mobile-first has three advantages. Phones download less code. You are forced to decide what really matters. And the design fits the screens your visitors actually use. Always test by resizing the browser from 360 pixels wide, a common phone width, up to a full desktop. Use relative units such as `rem` and percentages for sizes, so the page respects the visitor's text-size setting."""),
            ("Contrast and focus: design for everyone", """Pretty is not enough. Pages must be **readable and usable**:

- **Contrast:** text must stand out from its background. Accessibility guidelines (WCAG) ask for a contrast ratio of at least 4.5 to 1 for normal text. Light grey on white fails. Free tools check this in seconds.
- **Focus states:** people who use a keyboard move through links and buttons with the Tab key. A visible outline shows where they are. Never write `outline: none` without adding a clear replacement.
- **Text size:** use at least 16 pixels for body text.
- **Tap targets:** make buttons large enough to touch with a thumb.

Accessible design helps everyone: a person squinting at a phone in bright sunshine benefits from good contrast too."""),
        ],
        diagram=boxmodel(), caption="Every element is a box: content, padding, border and margin.",
        terms=[("Selector", "The part of a CSS rule that says which elements to style."), ("Box model", "The idea that every element is a box with content, padding, border and margin."), ("Flexbox", "A layout tool for arranging items in a row or a column."), ("Grid", "A layout tool for arranging items in rows and columns."),
               ("Media query", "A CSS rule that applies only on certain screen sizes."), ("Mobile-first", "Designing for small screens first and adding rules for bigger ones."), ("Contrast ratio", "How strongly text stands out from its background.")],
        mistakes=["Designing only on a big laptop and never checking a phone width.", "Setting fixed pixel widths that overflow small screens.", "Removing the focus outline with nothing to replace it.", "Using light grey text on a white background."],
        quiz=[dict(q="Which order is correct, from the inside out, in the box model?", o=["Margin, border, padding, content", "Padding, content, margin, border", "Border, margin, content, padding", "Content, padding, border, margin"], a=3, why="Content is in the middle, then padding, then border, then margin on the outside."),
              dict(q="Which tool is best for laying out cards in rows and columns?", o=["CSS grid", "The alt attribute", "A title tag", "The head element"], a=0, why="Grid arranges items in both rows and columns."),
              dict(q="What does mobile-first mean?", o=["Styling desktop screens first, then phones", "Only supporting one phone model", "Styling small screens first, then larger ones", "Hiding the whole site on desktops"], a=2, why="Start with the small screen and use media queries to add layout for bigger screens."),
              dict(q="What is the minimum contrast ratio WCAG asks for in normal text?", o=["1 to 1", "10 to 1", "2 to 1", "4.5 to 1"], a=3, why="A ratio of at least 4.5 to 1 keeps normal text readable for most people.")],
    ),
    3: dict(
        minutes=15,
        hook="HTML is the shop's structure, CSS is the paint, and JavaScript is the shopkeeper who answers when you ask a question. It lets a page react: show a message when you click, add an item to a list, load the latest prices without reloading. You do not need to learn every feature. A handful of ideas are enough to build real, useful things, and this lesson gives you those ideas with a to-do list you can build today.",
        sections=[
            ("Variables and functions", """A **variable** is a labelled box that holds a value. Use `const` for values that will not be reassigned and `let` for values that will.

> [JavaScript]
> const price = 3500;
> let quantity = 2;
> function total(price, quantity) {
>   return price * quantity;
> }
> console.log(total(price, quantity)); // 7000

A **function** is a named set of steps you can run again and again with different inputs. The `console.log` line prints to the browser's **console**, a window you can open with the F12 key that shows messages and errors. When something does not work, the console is the first place to look."""),
            ("The DOM and events", """When the browser loads your HTML it builds a live tree of the page called the **DOM** (Document Object Model). JavaScript can read and change this tree, and the page updates at once.

An **event** is something that happens: a click, a key press, a form submission. You tell the page “when this happens, run this function”:

> [JavaScript]
> const form = document.querySelector("#add");
> const list = document.querySelector("#todos");
> form.addEventListener("submit", (event) => {
>   event.preventDefault();
>   const text = form.elements.task.value.trim();
>   if (!text) return;
>   const li = document.createElement("li");
>   li.textContent = text;
>   list.append(li);
>   form.reset();
> });

That is a working to-do list. Notice `textContent`. It adds the text as plain text, so if someone types a tag, it cannot run as code. Using `innerHTML` with user text is a classic security hole."""),
            ("Fetch and JSON: talking to a server", """Pages often need data that lives on a server. The **fetch** function asks for it, and **JSON** is the format the answer usually arrives in: names and values, easy for both people and programs to read.

> [JavaScript]
> async function loadPosts() {
>   try {
>     const res = await fetch("/api/posts");
>     if (!res.ok) throw new Error("Server said " + res.status);
>     const posts = await res.json();
>     console.log(posts);
>   } catch (err) {
>     showMessage("Could not load posts. Please try again.");
>   }
> }

Two things matter here. `await` pauses this function until the answer arrives, without freezing the page. And the `try` and `catch` handle the case where the network fails, which on a mobile connection happens often. Always show the user a friendly message when it does."""),
            ("Debugging: your most useful skill", """Everyone writes bugs. Good developers find them quickly. Follow this routine:

1. **Read the error message.** It names the file and line. Start there.
2. **Open the console** and the **Network tab** in the browser's developer tools to see what was requested and what came back.
3. **Print values** with `console.log` to check what you assumed.
4. **Shrink the problem.** Remove code until the bug disappears, then put it back piece by piece.
5. **Change one thing at a time**, and test after each change.

Copying and pasting an error into a search or an AI assistant is fine for learning, as long as you then read and understand the fix instead of pasting blindly."""),
        ],
        diagram=flow([("EVENT", "A click or|a key press"), ("FUNCTION", "Your code|runs"), ("DATA", "Update the|list in memory"), ("PAGE", "Show the|change")], "w3", "The page reacts, and waits for the next event", loop=True),
        caption="Interactive pages are a loop: wait for an event, run code, update the page.",
        terms=[("Variable", "A named box that holds a value."), ("Function", "A named set of steps you can run whenever you need."), ("DOM", "The live tree of the page that JavaScript can read and change."), ("Event", "Something that happens on the page, like a click."),
               ("Fetch", "A function that asks a server for data."), ("JSON", "A text format for data, made of names and values."), ("Console", "A developer tool window that shows messages and errors.")],
        mistakes=["Using innerHTML to insert text that a user typed.", "Not handling the case where fetch fails.", "Changing many things at once when debugging.", "Ignoring the console, where the error is usually written."],
        quiz=[dict(q="What is the DOM?", o=["A kind of web server program", "A programming language for pages", "The live tree of the page that code can change", "A CSS rule for styling boxes"], a=2, why="The browser turns your HTML into the DOM, and JavaScript can read and change it."),
              dict(q="Why prefer textContent over innerHTML for user text?", o=["It is much slower than innerHTML", "It adds plain text, so it cannot run as code", "It changes the colours of the text", "It needs no function to work at all"], a=1, why="Inserting user text with innerHTML can run malicious code. textContent cannot."),
              dict(q="What does await do in an async function?", o=["Pauses the function until the answer arrives", "Deletes the data that was fetched", "Reloads the whole page again", "Hides an error from the user"], a=0, why="It lets the function wait for a slow task such as a network request while the page stays responsive."),
              dict(q="Which key usually opens the browser developer tools?", o=["F12", "Escape", "Enter", "Caps Lock"], a=0, why="F12 opens the developer tools in most browsers, where the console and network tabs live.")],
    ),
    4: dict(
        minutes=14,
        hook="When a tailor has to sew 200 school uniforms, he does not draw every shirt from scratch. He makes one pattern and cuts 200 copies. As websites grow, the same idea saves your sanity: build a piece once, like a product card or a menu, and reuse it. Modern front-end tools are about this one idea, plus the machinery to keep the screen in step with your data. This lesson explains components, tooling and, just as important, when you do not need any of it.",
        sections=[
            ("Components: reusable pieces", """A **component** is a self-contained piece of the interface, with its own structure, style and behaviour. A shop page might be built from a `Header`, a `ProductCard` used twenty times, and a `Cart`. The picture shows how components nest inside each other like a family tree.

Here is a component in React, one of the most popular libraries:

> [JavaScript]
> function ProductCard({ name, price }) {
>   return (
>     <div className="card">
>       <h3>{name}</h3>
>       <p>₦{price}</p>
>     </div>
>   );
> }

Use it as `<ProductCard name="Bread" price={1500} />`. The values you pass in are called **props**. Change the props and you get a different card from the same code."""),
            ("State: the data behind the screen", """The hard part of interactive pages is keeping the screen in sync with the data. If the cart has three items, the screen must show three items, and when the user adds a fourth, the screen must change. Doing that by hand with the DOM gets messy fast.

Frameworks solve it with **state**: you keep the data in a variable that the framework watches. When the data changes, the framework redraws only the parts that depend on it. You describe **what the screen should look like for the current data**, and the framework does the updating. That single idea is why React, Vue and similar tools became so popular."""),
            ("Build tools and npm", """Real projects use a few helpers:

- **Node.js** runs JavaScript outside the browser, which developer tools need.
- **npm** is the package manager, a store of free libraries you install with one command.
- **A build tool** such as Vite bundles your files, compresses them and gives you a fast local test server.

Your project then has a `package.json` file that lists its libraries and a `node_modules` folder with the code itself. Never upload `node_modules` to GitHub: it is big and can be rebuilt with `npm install`. Libraries are other people's code, so only add ones you need, from trusted sources, and keep them updated."""),
            ("Do you really need a framework?", """Frameworks are powerful, and also heavy. They add more code for the visitor to download, more tools to learn and more to break. A good rule:

- **Plain HTML, CSS and a little JavaScript** is the right choice for a brochure site, a landing page or a small tool. It is fast and simple.
- **A framework** pays off when the interface has lots of changing data, many repeated pieces or several developers working together.

Ask: “What problem would this solve for **this** project?” If you cannot answer, start without it. You can always add one later. A fast, simple site that loads on a weak 3G connection beats a clever one that never finishes loading."""),
        ],
        diagram=tree("App", [("Header", ["Logo", "Menu"]), ("ProductList", ["ProductCard", "ProductCard"]), ("Cart", ["CartItem", "Total"])], note="Components nest inside components"),
        caption="Build a piece once, then reuse it wherever you need it.",
        terms=[("Component", "A reusable piece of the interface with its own structure and behaviour."), ("Props", "Values you pass into a component to customise it."), ("State", "Data that a component remembers and that changes the screen when it changes."), ("npm", "The package manager that installs JavaScript libraries."),
               ("Build tool", "A tool that bundles and compresses your files and runs a test server."), ("Framework", "A large library, such as React or Vue, that gives your app a structure.")],
        mistakes=["Choosing a framework for a one-page brochure site.", "Uploading node_modules to GitHub.", "Installing a library for something three lines of code could do.", "Updating the screen by hand when the framework could do it from state."],
        quiz=[dict(q="What are props?", o=["Values passed into a component to customise it", "A kind of web server program", "CSS colours used in the page", "Errors shown in the browser console"], a=0, why="Props are the inputs to a component, like arguments to a function."),
              dict(q="What problem does state management solve?", o=["Making images smaller to download", "Keeping the screen in sync with the data", "Choosing fonts for the headings", "Writing HTML tags more quickly"], a=1, why="When the data changes, the framework updates the parts of the screen that depend on it."),
              dict(q="What does npm do?", o=["Draws the page on the screen", "Hosts your site on the internet", "Installs and manages JavaScript libraries", "Writes the CSS for your site"], a=2, why="npm is the package manager that downloads libraries listed in package.json."),
              dict(q="When is plain HTML, CSS and a little JavaScript the better choice?", o=["For a huge app with many developers", "For a game with thousands of objects", "For an app with live data on every screen", "For a simple brochure site or landing page"], a=3, why="A simple site loads faster and has less to break without a framework.")],
    ),
    5: dict(
        minutes=15,
        hook="Think of a restaurant. The dining room is the front end, where customers see the menu and sit. The kitchen is the back end, where orders are checked, cooked and written into the day's records. Customers never walk into the kitchen. They place an order with a waiter, and the kitchen replies. A web server is that kitchen, and the waiter is a set of rules called HTTP. This lesson shows you how to build the kitchen's order window: a small server that your pages can call.",
        sections=[
            ("Routes, methods and status codes", """A server answers requests at **routes**, which are paths such as /api/todos. Each request carries a **method** that says what the client wants to do:

- **GET:** read data.
- **POST:** create something new.
- **PUT or PATCH:** update something.
- **DELETE:** remove something.

The server replies with a **status code**, a number that tells how it went:

- **200** OK, **201** Created.
- **400** Bad request (you sent something wrong), **401** Not signed in, **404** Not found.
- **500** Server error (our fault, not yours).

Using the right code matters because browsers, apps and other developers rely on them."""),
            ("A small server with Flask", """**Flask** is a small Python framework for building servers. This one stores to-do items in memory and has two routes:

> [Python]
> from flask import Flask, jsonify, request
> app = Flask(__name__)
> todos = []
> 
> @app.get("/api/todos")
> def list_todos():
>     return jsonify(todos)
> 
> @app.post("/api/todos")
> def add_todo():
>     data = request.get_json(silent=True) or {}
>     title = str(data.get("title", "")).strip()
>     if not title:
>         return jsonify(error="title is required"), 400
>     todo = {"id": len(todos) + 1, "title": title, "done": False}
>     todos.append(todo)
>     return jsonify(todo), 201

Run it, and your page can call `fetch("/api/todos")` to read the list or send a POST to add an item. If you prefer Node.js, Express offers the same ideas with different syntax."""),
            ("Never trust the client", """Anyone can send any request to your server, not only from your page. A tool, a script or a curious student can send nonsense or attacks. So the server must **validate every request**:

1. Check that required fields exist and are the right type.
2. Limit lengths, for example a title of at most 200 characters.
3. Reject anything unexpected with a clear 400 message.
4. Never build database commands by pasting user text into them. You will learn the safe way next lesson.

The code above already does the first step: it rejects an empty title with a 400. A good rule is that checks in the browser are for **friendliness** and checks on the server are for **safety**."""),
            ("Reading the conversation", """When you are stuck, look at the conversation itself. In the browser's **Network tab** you can see each request, its method, its status code and the response. Compare what you sent with what the server expected.

Common surprises:

- A **404** usually means the path is wrong, so check spelling and slashes.
- A **405** means the route exists but not for that method.
- A **500** means the server crashed. Look at the server's terminal for the error.
- A **CORS** error appears when a page on one address calls a server on another without permission. Fix it on the server, not in the page."""),
        ],
        diagram=seq(["Page", "API"], [(0, 1, "POST /api/todos  title: Buy bread"), (1, 0, "201 Created and the new todo"), (0, 1, "POST /api/todos  title: empty"), (1, 0, "400 title is required")], "w5", note="The same route gives different answers to good and bad requests"),
        caption="A server checks every request and answers with a clear status code.",
        terms=[("Route", "A path on the server that handles requests, such as /api/todos."), ("HTTP method", "The action a request asks for: GET, POST, PUT, PATCH or DELETE."), ("Status code", "A number in the response that shows how the request went."), ("API", "A set of routes that programs use to talk to your server."),
               ("Validation", "Checking that incoming data is complete, correct and safe."), ("Flask", "A small Python framework for building servers.")],
        mistakes=["Trusting data from the browser without checking it on the server.", "Returning 200 for every response, even for errors.", "Using GET to change data.", "Putting database commands together by pasting user text into them."],
        quiz=[dict(q="Which method is normally used to create a new item?", o=["GET", "DELETE", "HEAD", "POST"], a=3, why="POST sends new data to create a resource."),
              dict(q="What does a 404 status code mean?", o=["The server crashed unexpectedly", "The thing you asked for was not found", "You are not signed in yet", "Everything went fine and the page loaded"], a=1, why="404 means Not Found, often a wrong path."),
              dict(q="Why must the server validate requests even if the page already checks them?", o=["Because anyone can send requests without using your page", "Because browsers are always too slow", "Because servers enjoy doing extra work", "Because status codes need it to work"], a=0, why="Requests can come from any tool, so the server is the last line of defence."),
              dict(q="Which status code means the server itself had an error?", o=["200", "400", "201", "500"], a=3, why="5xx codes mean the problem is on the server side.")],
    ),
    6: dict(
        minutes=15,
        hook="A shopkeeper who writes sales on loose pieces of paper loses money the first time the wind blows. A proper ledger, with rows and columns, makes sure nothing gets lost and everything can be found. A database is that ledger for your app. But storing data is only half the job. You also have to be sure that what goes in is correct, and that the app still works tomorrow after you change it. This lesson covers data and quality together.",
        sections=[
            ("SQL: asking a database questions", """Most websites store their data in a **relational database**, which keeps information in **tables** of rows and columns. You talk to it with **SQL**. Five commands cover most of what you will need:

> [SQL]
> CREATE TABLE todos (
>   id INTEGER PRIMARY KEY,
>   title TEXT NOT NULL,
>   done INTEGER NOT NULL DEFAULT 0
> );
> INSERT INTO todos (title) VALUES ('Buy data bundle');
> SELECT id, title FROM todos WHERE done = 0;
> UPDATE todos SET done = 1 WHERE id = 1;
> DELETE FROM todos WHERE id = 1;

The `WHERE` part chooses which rows. Forgetting it on an UPDATE or DELETE changes **every** row, so read those lines twice before you run them. SQLite is a free, simple database stored in a single file, and a great way to start."""),
            ("Safe database access", """When your server puts user text into a SQL command, there is a serious danger: **SQL injection**. If you glue the text straight into the command, a user can type pieces of SQL and take control. The fix is simple: use **placeholders** and let the database library handle the values.

> [Python]
> cur.execute("INSERT INTO todos (title) VALUES (?)", (title,))

The question mark is a placeholder, and the title is passed separately, so it is always treated as data and never as a command. Never build SQL by adding strings together."""),
            ("Validation: client and server", """**Validation** checks that data is acceptable before using it. There are two places to do it, and you need both:

- **In the browser:** attributes such as `required`, `type="email"` and `maxlength` give users instant, friendly feedback.
- **On the server:** the real check, because browser checks can be bypassed.

Write error messages that help: “Enter an email address like name@example.com” is better than “Invalid input”. Keep the user's other answers in the form so they do not have to type everything again."""),
            ("Testing, debugging and quality checks", """Code that is not tested breaks the day you change something. Start small. A test calls your code and checks the result:

> [Python]
> def test_rejects_empty_title():
>     client = app.test_client()
>     res = client.post("/api/todos", json={"title": ""})
>     assert res.status_code == 400

Run it after every change. Then use the free **Lighthouse** tool built into Chrome's developer tools. It scores a page on **performance**, **accessibility**, **best practices** and **SEO**, and lists what to fix. Common easy wins: compress images, set image sizes, add alt text and improve contrast. Aim for 90 or more, and when you cannot, be ready to explain what holds the score back."""),
        ],
        diagram=grid([("Validate", "Browser for|friendliness"), ("Protect", "Placeholders|against injection"), ("Test", "Automatic checks|after each change"), ("Debug", "Console and|Network tab"), ("Performance", "Small images,|little code"), ("Accessibility", "Alt text, contrast,|keyboard use")], 3, note="Six habits that separate a project from a product"),
        caption="Quality is a set of habits, not a final step.",
        terms=[("Table", "A grid of rows and columns that holds one kind of data."), ("SQL", "The language used to read and change data in a relational database."), ("SQL injection", "An attack where user text is run as part of a database command."), ("Placeholder", "A marker in a SQL command that is replaced safely by a value."),
               ("Validation", "Checking data before using it."), ("Lighthouse", "A free tool that scores a page on performance, accessibility and more.")],
        mistakes=["Running an UPDATE or DELETE without a WHERE clause.", "Building SQL by joining strings with user input.", "Validating only in the browser.", "Never testing, and only finding bugs after users do."],
        quiz=[dict(q="What happens if you run DELETE FROM todos with no WHERE?", o=["Nothing", "Only the newest row is removed", "Every row in the table is deleted", "The table is renamed"], a=2, why="Without WHERE, the command applies to all rows."),
              dict(q="How do placeholders protect against SQL injection?", o=["They hide the names of your tables", "They encrypt the whole database file", "They make every query run faster", "The value is sent separately as data, not as a command"], a=3, why="With placeholders, user text can never change the meaning of the SQL."),
              dict(q="Why validate on the server as well as in the browser?", o=["Browser checks can be bypassed", "Servers prefer more rules", "Browsers cannot show errors", "It makes pages load faster"], a=0, why="Anyone can send requests without your page, so the server must check everything."),
              dict(q="Which free tool scores a page on performance and accessibility?", o=["Photoshop", "Lighthouse", "Excel", "Notepad"], a=1, why="Lighthouse is built into Chrome's developer tools.")],
    ),
    7: dict(
        minutes=14,
        hook="A farmer who grows excellent tomatoes but never brings them to the market earns nothing. A website that sits only on your laptop is the same: nobody can see it. Getting it online involves three skills. Saving your work safely so you can always go back, sharing it with others without overwriting each other, and putting it on a computer that is always switched on. This lesson covers Git, GitHub, hosting, domains and the secrets you must never publish.",
        sections=[
            ("Git: a time machine for your code", """**Git** records the history of your project. Each saved snapshot is a **commit**, with a short message that says what changed. If you break something, you can go back to the last good commit. Here are the core commands:

> [Terminal]
> git init
> git add .
> git commit -m "Add menu page"
> git switch -c feature/contact-form
> git push origin feature/contact-form

Write messages that say **what** and **why**, like “Fix broken order button on phones”, not “changes” or “asdf”. Commit often, in small steps, so each one is easy to understand and undo."""),
            ("Branches, GitHub and pull requests", """A **branch** is a separate line of work. You make a new branch for each feature or fix, so your half-finished work never breaks the working version, called **main**.

**GitHub** is a website that stores your Git projects online. It is your backup, your portfolio and the place where teams collaborate. When your feature is ready, you open a **pull request**: a proposal to merge your branch into main. Teammates read your changes, comment and approve. Even when you work alone, opening a pull request is a good habit, because reading your own changes often reveals mistakes.

If two people change the same lines, Git reports a **merge conflict**. It is not an emergency: you choose which version to keep, then continue."""),
            ("Hosting, domains and HTTPS", """To put your site online you need a **host**, a computer that is always connected.

- **Static hosting** serves ready-made HTML, CSS and JavaScript files. Several services offer a free plan, and they can update your site every time you push to GitHub.
- **App hosting** runs a server program, such as your Flask API, and usually has a free or low-cost starting plan with limits.

Terms and prices change, so read each provider's current plan before you choose.

A **domain name** such as myshop.ng is the address people type. You rent it yearly from a registrar. **HTTPS** is added with a certificate, and most modern hosts provide it free and automatically. Check that the padlock appears in the browser."""),
            ("Secrets and environment variables", """Some information must **never** be public: database passwords, payment secret keys, email service keys. If you commit them to GitHub, bots find them within minutes.

The safe method:

1. Put secrets in a file called `.env` on your own computer.
2. List `.env` in a file called `.gitignore` so Git never uploads it.
3. In your code, read the secret from an **environment variable**.
4. On the host, set the same variables in its settings page.

If a secret ever leaks, **do not just delete the file**. It stays in history. Change the secret at once by creating a new key and disabling the old one."""),
        ],
        diagram=flow([("EDIT", "Change|your code"), ("COMMIT", "Save a|snapshot"), ("PUSH", "Send it to|GitHub"), ("BUILD", "The host|checks it"), ("LIVE", "Visitors see|the update")], "w7", "Every push can update the live site automatically"),
        caption="From your laptop to the world in five steps.",
        terms=[("Commit", "A saved snapshot of your project with a message."), ("Branch", "A separate line of work that does not affect main until merged."), ("Pull request", "A proposal to merge a branch, which others can review."), ("Merge conflict", "When two changes touch the same lines and Git needs you to choose."),
               ("Domain name", "The readable address of a site, such as myshop.ng."), ("Environment variable", "A setting kept outside your code, used for secrets.")],
        mistakes=["Committing a .env file or a password to GitHub.", "Writing commit messages like “changes” or “asdf”.", "Working directly on main with no branch.", "Deleting a leaked secret from the code but not replacing the key."],
        quiz=[dict(q="What is a commit?", o=["A separate line of work in the project", "A saved snapshot of your project with a message", "A web host that serves the site", "A readable domain name for the site"], a=1, why="Commits record the history of your project step by step."),
              dict(q="Why use a branch for a new feature?", o=["It makes the finished site load faster", "It protects the working version until your feature is ready", "It removes the need to write tests", "It is required by every web browser"], a=1, why="A branch keeps unfinished work away from main."),
              dict(q="Where should a database password be kept?", o=["In an environment variable, not in Git", "In the HTML of your public page", "In a commit message on GitHub", "In the README of the project"], a=0, why="Secrets belong outside the code and outside Git history."),
              dict(q="A secret key leaked to GitHub. What is the best response?", o=["Delete the file and hope", "Change the repository name", "Make the repository bigger", "Create a new key and disable the old one"], a=3, why="Once published, a key must be treated as stolen. Replace it right away.")],
    ),
    8: dict(
        minutes=15,
        hook="Someone who wants to hire you will not read your list of lessons. They will open one link and decide in thirty seconds whether you can build things that work. This capstone gives you that link. You will plan, build, test and launch a real website for a real or realistic customer, and write a short case study that explains your thinking. It is the project that turns “I did the course” into “look what I made.”",
        sections=[
            ("The brief", """Build and launch a **real website** for a small business, church, school, club or community group. A real customer is best, but a realistic made-up one is fine. Your site must include:

- **A home page and at least two more pages**, using semantic HTML.
- **A layout that works** on a phone, tablet and laptop.
- **A form** with validation, for contact or bookings.
- **One interactive feature** built with JavaScript.
- **Accessibility basics:** contrast, alt text and keyboard use.
- **A live link** with HTTPS, with the code on GitHub.
- A **Lighthouse** score of 90 or more, or a clear note on what holds it back."""),
            ("Plan before you code", """Spend the first part of the time on four short documents:

1. **Who is it for?** Name the visitor and what they came to do: find opening hours, see prices, book, call.
2. **Pages and content:** list each page and what goes on it. Get real text and photos from the customer early, because waiting for content is the most common cause of delay.
3. **A sketch** of the home page on paper, for phone first.
4. **A task list** in order: structure, styling, form, interaction, testing, launch.

Show the sketch to the customer or a classmate before building. Changing a sketch takes five minutes."""),
            ("Build, test, launch", """Work in small steps and commit after each one.

1. Build the HTML structure of every page, with no styling.
2. Add the CSS, phone first, then widen.
3. Add the form and validation.
4. Add your JavaScript feature.
5. Test on a real phone, in two browsers, and with the keyboard only. Run Lighthouse and fix the easy wins.
6. Deploy, and test the live site again. Things often break only after launch, such as wrong file paths.

Ask two people who have never seen the site to find the opening hours. If they struggle, the design needs work, however nice it looks."""),
            ("The case study and the demo", """A **case study** is a one-page story of the project. It should answer:

- **The problem:** who the site is for and what they needed.
- **What you built:** a screenshot, the live link and the code link.
- **Decisions:** two or three choices you made and why, for example “I used plain JavaScript because the site is small”.
- **A bug you fixed:** what went wrong, how you found it and how you fixed it.
- **What you would improve** with more time.

In your five-minute demo, show the live site on a phone, explain one decision and show one bug you fixed. This is the page that goes at the top of your portfolio."""),
        ],
        diagram=timeline([("Plan", "Visitor, pages,|sketch"), ("Structure", "HTML for|every page"), ("Style", "Phone first,|then widen"), ("Interact", "Form and|JavaScript"), ("Test", "Phone, keyboard,|Lighthouse"), ("Launch", "Live link and|case study")], note="Small steps, tested often"),
        caption="Plan, build, test, deploy. Each step makes the next one easier.",
        terms=[("Case study", "A short story of a project: the problem, your decisions and the result."), ("Portfolio", "A collection of your best work that you show to clients and employers."), ("Deploy", "To put a site on a server so that anyone can visit it."), ("Content", "The real text and images that go on the site."),
               ("MVP", "The smallest version of a product that is useful and can be launched.")],
        mistakes=["Starting to code before knowing who the site is for.", "Waiting until the end to test on a real phone.", "Forgetting to test the live site after deploying.", "Writing a case study that lists features but not decisions."],
        quiz=[dict(q="Why get real content early from the customer?", o=["It makes the code much shorter", "Waiting for content is a common cause of delay", "Search engines require it first", "It improves the colour choices"], a=1, why="Without real text and photos you cannot finish or test the design properly."),
              dict(q="Where should you test the finished site?", o=["Only on your own laptop screen", "Nowhere, if the site looks fine", "On a real phone, two browsers and keyboard only", "Only inside the code editor"], a=2, why="Different devices and ways of using the site reveal different problems."),
              dict(q="What belongs in a case study?", o=["Only a list of the tools you used", "The problem, your decisions and a bug you fixed", "A full copy of all the code", "Only a screenshot of the home page"], a=1, why="A case study shows how you think, not just what you made."),
              dict(q="Why test the live site after deploying?", o=["Hosts delete files after launch", "It is required by GitHub", "Wrong file paths often break only after launch", "Browsers change after deployment"], a=2, why="The live environment can differ from your laptop, so check again.")],
    ),
}