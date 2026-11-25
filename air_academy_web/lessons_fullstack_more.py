"""Full Stack Masterclass: lessons 9 to 24, added when the course grew into a full course (course_plan.py says where each one sits on screen).
Same format as lessons_fullstack.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[9] = dict(   # How the web works: requests, servers and the full journey
    minutes=14,
    hook="You type a shop's address, press Enter, and a page full of products appears a second later. Between that key press and the picture on your screen, your request crosses your phone, a mobile network, the internet, a data centre, a web server, an application and a database, and then all of it travels back. A full stack developer must understand every stop on that road, because a bug or a slowdown can hide at any of them. In this lesson you will follow one request from end to end, learn exactly what is inside it, and learn where the time goes.",
    sections=[
        ("The journey from address to page", """Follow what happens when someone opens `https://myshop.ng/products`:

1. **DNS lookup:** the browser asks a DNS server which address `myshop.ng` has, for example `203.0.113.7`.
2. **Connection:** it opens a TCP connection to that address, then performs a **TLS handshake** so the traffic is encrypted (HTTPS).
3. **HTTP request:** it sends `GET /products` with headers such as the cookie and the language.
4. **Server and application:** a web server (or the hosting platform) receives it and passes it to your application code.
5. **Database:** your code asks the database for the products.
6. **Response:** your code sends back a status code, headers and a body (HTML or JSON).
7. **Rendering:** the browser reads the HTML, finds more files (CSS, JavaScript, images) and requests those too, then draws the page.

Every one of these steps can be slow, fail or be attacked, which is why knowing the whole chain makes you a better engineer."""),
        ("What is inside an HTTP request and response", """HTTP is plain text with a strict shape. A request has a **method**, a **path**, **headers** and sometimes a **body**:

> [HTTP request]
> POST /api/orders HTTP/1.1
> Host: myshop.ng
> Content-Type: application/json
> Cookie: session=abc123
>
> {"item": "Meat pie", "qty": 3}

> [HTTP response]
> HTTP/1.1 201 Created
> Content-Type: application/json
> Set-Cookie: session=abc123; HttpOnly; Secure
>
> {"id": 88, "status": "received"}

The **status code** tells the client what happened: 2xx success, 3xx redirect, 4xx the client made a mistake (400 bad input, 401 not signed in, 403 not allowed, 404 not found), 5xx the server failed. **Headers** carry information about the message, such as the format, cookies, caching rules and security settings."""),
        ("HTTP is stateless", """Each request stands alone. The server does not remember that you asked for `/products` a moment ago. That simple rule explains many design decisions:

- To recognise a returning user, the browser sends a **cookie or token** with every request.
- Because any request can arrive at any server, a **stateless** application is easy to copy and spread across many servers.
- State that must last (carts, orders, accounts) lives in a **database**, not in the server's memory.
- A page that shows a different result per user must be careful with **caching**, so one person never sees another person's data.

When you design an application, always ask: where does this piece of state live, and who is allowed to see it?"""),
        ("Where the time goes", """A page that feels slow is slow somewhere specific. The usual suspects:

- **Network distance and round trips.** Every extra request costs time, especially on mobile networks with high latency. Fewer, smaller requests help.
- **Large files.** Images and JavaScript bundles often make up most of the download.
- **Slow server work.** A heavy calculation or an external API call inside the request.
- **Slow database queries.** Missing indexes or too many queries per page.
- **Cold starts.** Free hosting that sleeps when idle needs time to wake up.

You find the culprit by measuring, not guessing. The **Network tab** in browser developer tools shows each request with its timing, and server logs show how long your own code took."""),
        ("Tools for seeing the journey", """Get comfortable with these, because you will use them every day:

1. **Browser developer tools, Network tab:** see every request, its status code, size, timing, headers and response.
2. **curl** in the terminal: `curl -i https://myshop.ng/api/products` shows the raw response including headers. It lets you test the API without the front end.
3. **A request tool** such as Postman, Insomnia or Bruno for building and saving API requests.
4. **`nslookup` or `dig`** to check DNS.
5. **Your server logs** to see what the backend received.

When something is broken, ask first: did the request leave the browser, did it arrive, what did the server answer, and what did the browser do with the answer? That one habit solves most problems."""),
    ],
    diagram=seq(["Browser", "DNS", "Server", "Database"], [(0, 1, "Where is myshop.ng?"), (1, 0, "It is at 203.0.113.7"), (0, 2, "HTTPS: GET /api/products"), (2, 3, "SELECT products"), (3, 2, "the rows"), (2, 0, "200 OK and JSON")], "fs9",
                note="One page view is a chain of conversations."),
    caption="A page view crosses DNS, the server and the database, and each trip is a place where time can be lost.",
    terms=[("DNS", "The system that turns a domain name into a server address."), ("TLS", "The encryption layer that makes HTTPS private."),
           ("Status code", "A number in the response that says whether the request worked."), ("Header", "A line of extra information sent with a request or response."),
           ("Stateless", "A server that does not remember earlier requests on its own."), ("Latency", "The delay before data starts to arrive.")],
    mistakes=["Guessing where a slowdown is instead of measuring in the Network tab.", "Keeping important state in the memory of one server.", "Treating every 4xx and 5xx error the same.", "Testing the API only through the front end."],
    quiz=[dict(q="What does HTTP being stateless mean?", o=["It is not secure", "The server does not remember earlier requests by itself", "It only works offline", "It has no status codes"], a=1,
               why="Each request stands alone, so identity is carried by a cookie or token."),
          dict(q="Which status code family means the server failed?", o=["2xx", "3xx", "4xx", "5xx"], a=3,
               why="5xx codes mean the server had a problem. 4xx means the client sent a bad request."),
          dict(q="Where should a shopping cart that must survive a server restart live?", o=["In one server's memory", "In the database", "In a console message", "In a CSS file"], a=1,
               why="Durable state belongs in a database, so any server can read it."),
          dict(q="What is the first step when a page feels slow?", o=["Rewrite the app", "Buy a bigger server", "Measure where the time goes", "Ignore it"], a=2,
               why="Measure first, so you fix the real cause.")],
    activity="Open any website with the Network tab, reload, and list the five biggest requests by size and the slowest by time. Then use curl -i on one API address and read each header.",
)

LESSONS[10] = dict(   # Choosing a stack and setting up your project
    minutes=14,
    hook="Beginners lose weeks arguing online about which technology is best. Professionals ask a different question: what will let this team ship a working product, safely, with the skills it already has? A stack is simply the set of tools you choose for the front end, back end, database and hosting. There is no perfect one, but there are sensible ways to choose and a proper way to set up the project so that it stays clean when it grows. In this lesson you will compare popular stacks, decide using clear criteria and set up a project the way a professional team would.",
    sections=[
        ("What a stack is", """A **stack** is the combination of technologies that together make an application:

- **Front end:** what runs in the browser (HTML, CSS, JavaScript, often with React, Vue or Svelte).
- **Back end:** the code on the server (Python with Flask or Django, Node.js with Express, PHP with Laravel, and others).
- **Database:** where data lives (PostgreSQL, MySQL, SQLite, MongoDB).
- **Hosting and services:** where it runs and the extras it uses (Render, Railway, AWS, email, payments, storage).

Popular named stacks include MERN (MongoDB, Express, React, Node), a Python stack (Flask or Django with Postgres and a JavaScript front end), and meta-frameworks such as Next.js that blend front end and back end in one project."""),
        ("How to choose: criteria that matter", """Judge each option against facts, not fashion:

1. **Your skills and your team's skills.** The best stack is usually the one you can already use well.
2. **Time to first working version.** A boring, familiar tool beats an exciting one you must learn first.
3. **Community and documentation.** Can you find answers, tutorials and people to hire?
4. **Fit for the job.** A content site, a real-time chat, a data-heavy dashboard and a payment app have different needs.
5. **Hosting and cost.** Does it run cheaply on the platforms you can afford?
6. **Longevity.** Is it maintained and widely used, so it will not vanish next year?
7. **Integrations.** Do the libraries you need (payments, email, authentication) exist for it?

Write the decision and the reasons in a short note, so you can explain it later."""),
        ("Compare, then commit", """Two sensible examples show how the trade-offs look:

- **Python (Flask) with PostgreSQL and a small JavaScript front end:** simple, readable, excellent for APIs, data and AI work. One person can understand the whole project. Needs a deliberate choice for the front end.
- **JavaScript everywhere (Node, Express or Next.js, React, PostgreSQL):** one language across the stack, a huge ecosystem and many jobs. More moving parts and more choices to make.

Both work. What matters is **to commit** for this project, and avoid rewriting later without a real reason. Switching stacks half way is among the most expensive mistakes a team can make."""),
        ("Set up the project properly", """A clean start saves pain later:

1. **Create a Git repository** and make the first commit.
2. **Add `.gitignore`** to keep out secrets, `node_modules`, virtual environments and build files.
3. **Choose a folder structure,** for example `frontend/`, `backend/`, `docs/`, with a `README.md` at the top that explains how to run everything.
4. **Isolate dependencies:** a Python virtual environment with `requirements.txt`, or `package.json` with a lock file.
5. **Keep configuration in environment variables,** with a `.env.example` that lists the names (never the values).
6. **Add a linter and formatter** (Ruff or Black, ESLint and Prettier).
7. **Write a first test** and a command that runs everything.

Anyone should be able to clone the project and run it by following the README in ten minutes."""),
        ("Prove the whole chain with a first slice", """Before building features, prove that every layer is connected. Build the smallest possible thing that goes **all the way through**:

1. A page with one button, labelled “Check server”.
2. Clicking it calls `GET /api/health` on your back end.
3. The back end runs a simple query against the database.
4. The answer comes back and shows “Server and database are working”.

Deploy this tiny slice early, even before it is useful. It reveals problems with hosting, environment variables, CORS and database connections while the project is still small, and it gives you a working base for every feature after it."""),
    ],
    diagram=compare(("PYTHON STACK", ["Flask or Django", "PostgreSQL", "Simple JS or React front end"]), ("JAVASCRIPT STACK", ["Node with Express or Next.js", "PostgreSQL or MongoDB", "React front end"]), vs="or",
                    note="Both work. Choose by skills, time and fit, then commit."),
    caption="Two sound stacks: choose by your skills, time to ship and fit for the job, then commit.",
    terms=[("Stack", "The set of technologies used for the front end, back end, database and hosting."), ("Dependency", "A library your project needs in order to run."),
           ("Lock file", "A file that records the exact versions of dependencies so everyone gets the same ones."), (".env.example", "A file that lists the names of needed settings without their secret values."),
           ("Vertical slice", "A thin piece of a feature that goes through every layer from screen to database.")],
    mistakes=["Choosing a tool only because it is trending.", "Switching stacks half way through the project.", "Committing .env files or secrets to Git.", "Building many features before proving the layers are connected."],
    quiz=[dict(q="What is the best way to choose a stack?", o=["Pick whatever is newest", "Copy a stranger's choice", "Pick the longest name", "Weigh skills, time to ship, community, fit and cost"], a=3,
               why="Facts about your project and team beat fashion."),
          dict(q="Why add a .env.example file?", o=["To store real passwords", "To list the names of needed settings without secret values", "To speed up the CPU", "To replace the README"], a=1,
               why="It tells teammates which variables to set, without exposing secrets."),
          dict(q="What is a good first thing to build?", o=["A tiny slice that runs through every layer", "Every feature at once", "The logo", "The final report"], a=0,
               why="A thin end-to-end slice reveals connection problems early."),
          dict(q="Which belongs in .gitignore?", o=["The README", "The main source code", "Secrets, node_modules and virtual environments", "The tests"], a=2,
               why="Secrets and generated folders must stay out of Git.")],
    activity="Write a half-page decision note choosing a stack for a small shop app, scoring two options against the seven criteria. Then create the Git repository, .gitignore, README and .env.example.",
)

LESSONS[11] = dict(   # Planning an application: requirements and data flow
    minutes=15,
    hook="Many projects fail not because the code is bad but because nobody was clear about what they were building. A week of planning can save a month of rebuilding. Planning an application means answering four questions in writing: who is it for, what must it do, what information does it hold, and how does that information move? In this lesson you will turn a vague idea, such as “an app for my tailoring business”, into requirements, a simple data model, a list of screens and endpoints, and a plan of small steps you can actually finish.",
    sections=[
        ("Start with people and goals", """Write down **who** will use the application and **what they are trying to achieve**. A **user story** is a one-sentence form:

> [Example]
> As a customer, I want to see my order status, so that I know when to expect my clothes.
> As a tailor, I want to record a measurement, so that I do not lose it.
> As an admin, I want to see unpaid orders, so that I can follow up.

Keep stories short and in the user's words. Then sort them with **MoSCoW**: **Must** have (the app is useless without it), **Should** have, **Could** have, and **Won't** have this time. The Must list is your first release. Be strict: a small product that works beats a large one that never ships."""),
        ("Requirements and limits", """Besides what the app does, write what it must **be**:

- **Functional requirements:** features, such as “a customer can place an order”.
- **Non-functional requirements:** speed (pages load in under three seconds on mobile data), security (passwords hashed, data private), availability, accessibility and cost.
- **Constraints:** budget, deadline, team size, the payment provider, laws about personal data (in Nigeria, the NDPA 2023).
- **Out of scope:** a short list of what you will not build now. This protects you from endless additions.

Write acceptance criteria for each Must story: “Given a signed-in customer, when they open Orders, then they see only their own orders, newest first.” This is a test you can check later."""),
        ("Find the data", """Read your stories and underline the **nouns**. They are your candidate entities: user, customer, order, measurement, payment. For each, list its **attributes** and how entities **relate**:

> [Example]
> User: id, name, email, password_hash, role
> Order: id, user_id, status, total_kobo, created_at
> OrderItem: id, order_id, description, price_kobo
> Payment: id, order_id, reference, status, paid_at

Relationships: one user has many orders, one order has many items, one order has payments. Draw it as boxes and lines (an **entity relationship diagram**). Decide early what is **private** and who may see it. Also decide which values must never be trusted from the client, such as prices and totals."""),
        ("Follow the data flow", """For each important action, trace **what moves where**:

1. The user fills a form on screen X.
2. The front end checks the input and sends `POST /api/orders` with JSON.
3. The back end checks who the user is, validates the data and calculates the total itself.
4. It saves the order and items in a single database transaction.
5. It calls the payment provider, then waits for a confirmation callback.
6. It sends an email, and returns the new order to the screen.

Draw this as a **flow diagram**. Doing it on paper exposes missing pieces: What if the payment fails? What if the same request arrives twice? Who gets notified? It is much cheaper to find these on paper than in production."""),
        ("Turn the plan into small slices", """Convert the Must stories into a list of **thin vertical slices**, each one a working piece from screen to database:

1. Sign up and log in.
2. Create an order with one item.
3. See my orders.
4. Pay for an order.
5. Admin sees all orders.

Estimate each slice honestly, **add a buffer**, and build them in order of value and risk. Put risky or unknown parts (payments, file uploads) early, so surprises come while there is still time. Keep a simple board with To do, Doing and Done. After each slice, demo it, test it and adjust the plan."""),
    ],
    diagram=flow([("People", "who and why"), ("Stories", "Must, Should,|Could"), ("Data", "entities and|relations"), ("Flows", "screens and|endpoints"), ("Slices", "small steps|that ship")], "fs11",
                 note="Plan on paper first. It is the cheapest place to find mistakes."),
    caption="From people and stories to data, flows and thin slices: planning before coding saves weeks.",
    terms=[("User story", "A one-sentence description of what a user wants and why."), ("MoSCoW", "A way to sort features into Must, Should, Could and Won't."),
           ("Acceptance criteria", "Clear checks that tell you a feature is really done."), ("Entity", "A thing your app stores information about, such as an order."),
           ("Non-functional requirement", "A quality the app must have, such as speed or security."), ("Scope", "The set of things you have agreed to build.")],
    mistakes=["Starting to code with no written requirements.", "Calling everything a Must so nothing gets cut.", "Forgetting failure cases such as a failed payment.", "Planning one huge release instead of small slices."],
    quiz=[dict(q="What does MoSCoW help you do?", o=["Choose a colour", "Sort features into Must, Should, Could and Won't", "Write SQL", "Deploy faster"], a=0,
               why="It forces honest priorities, so the first release stays small."),
          dict(q="A good way to find entities for your data model is to...", o=["Guess randomly", "Underline the nouns in your user stories", "Copy another app", "Wait until launch"], a=1,
               why="Nouns in stories usually become tables or entities."),
          dict(q="Why put risky parts such as payments early in the plan?", o=["They are easy", "Surprises appear while you still have time to react", "Customers prefer it", "It saves electricity"], a=1,
               why="Early risk discovery keeps the schedule safe."),
          dict(q="Which is an acceptance criterion?", o=["Make it good", "Given a signed-in customer, when they open Orders, they see only their own orders", "Use blue", "Be fast"], a=1,
               why="Acceptance criteria are specific, testable statements.")],
    activity="Pick an app idea. Write six user stories, sort them with MoSCoW, list the entities with attributes, and draw the data flow for one action, including what happens when it fails.",
)

LESSONS[12] = dict(   # Components, routing and state
    minutes=14,
    hook="A single-page application feels like a native app: you click a link, and the screen changes instantly with no full page reload. Behind that smoothness are three ideas working together. Components build the screens from reusable pieces. Routing makes the address bar and the screen agree, so that links, the back button and bookmarks work. State holds the data that changes. You met components and state earlier in this course. Now you will add routing and see how all three fit together into the structure of a real front end, including pages that need a login and the different kinds of state.",
    sections=[
        ("Routing: the address decides the screen", """A **router** maps a URL to a component. In a React app using React Router, it looks like this:

> [JSX]
> <Routes>
>   <Route path="/" element={<Home />} />
>   <Route path="/products" element={<ProductList />} />
>   <Route path="/products/:id" element={<ProductDetail />} />
>   <Route path="/account" element={<RequireLogin><Account /></RequireLogin>} />
>   <Route path="*" element={<NotFound />} />
> </Routes>

The **`:id` parameter** lets one component show any product. Use real `<Link to="/products">` elements, not buttons that change the screen secretly, so people can open links in new tabs, share them and bookmark them. The `*` route handles addresses that do not exist."""),
        ("Why the URL is part of your state", """The address in the browser is **state that users can share**. Put in it anything that should survive a reload or a share:

- Which page or item is open: `/orders/88`.
- Filters, search and page number as **query parameters**: `/products?category=cakes&page=2`.
- Not in the URL: secrets, tokens and private personal data.

If a user filters a list and reloads, they should see the same filtered list. If they copy the link to a friend, the friend should see it too. Components read the values from the router (`useParams`, `useSearchParams`) and change them with navigation, rather than keeping a hidden copy in a variable."""),
        ("Layouts, nested routes and protected pages", """Most apps repeat the same frame, such as a header and a sidebar, around different content. **Nested routes** put the shared **layout** around a changing area (`<Outlet />`), so the header does not rebuild when you move between pages.

**Protected routes** wrap pages that need a login: the wrapper checks whether the user is signed in, and if not, redirects to `/login`, remembering where they wanted to go. Remember the important truth: this check only improves the **experience**. The **server** must still verify permissions on every API call, because anyone can change front-end code in their own browser."""),
        ("Kinds of state and where each belongs", """Not all state is the same, and sorting it makes the app simpler:

1. **UI state** (is the menu open, which tab is selected): local to a component.
2. **Form state** (what is being typed): local to the form, or a form library.
3. **URL state** (filters, page, selected item): in the address.
4. **Server state** (products, orders fetched from the API): owned by the server. Use a data-fetching library such as **TanStack Query** to cache and refresh it, instead of copying it into your own variables.
5. **Global app state** (the signed-in user, theme): in a context or a small store.

The most common mistake is putting everything in one global store. Keep state as close as possible to where it is used, and only lift it up when needed."""),
        ("Organising a front-end project", """A structure that scales, organised by **feature** rather than by file type:

> [Folders]
> src/
>   components/       small shared pieces: Button, Modal
>   features/
>     orders/         OrderList, OrderForm, api.js, hooks.js
>     auth/           LoginForm, useAuth.js
>   pages/            one component per route
>   lib/              api client, helpers
>   App.jsx           routes and layout

Keep components small and named for what they show. Move repeated logic into **custom hooks** such as `useOrders()`. Handle three situations in every screen: loading, error and empty. And keep accessibility in mind: after navigation, move focus to the page heading and update the page `title`, so screen-reader users know where they are."""),
    ],
    diagram=tree("Router", [("/ and /products", ["Home", "ProductList", "ProductDetail /:id"]), ("/account  (login needed)", ["RequireLogin", "Account", "Orders"]), ("* (anything else)", ["NotFound page"])],
                 note="The address decides which component is shown."),
    caption="The router maps each address to a component, wraps private pages in a login check and shows a Not Found page for the rest.",
    terms=[("Router", "Code that decides which component to show for each address."), ("Route parameter", "A part of the address, such as :id, that changes which item is shown."),
           ("Query parameter", "A value after the question mark in an address, often used for filters."), ("Layout route", "A route that wraps child pages in a shared frame such as a header."),
           ("Server state", "Data that belongs to the server and is only cached in the front end."), ("Custom hook", "A reusable function that packages stateful logic for components.")],
    mistakes=["Using buttons instead of real links for navigation.", "Keeping filters in hidden variables so a reload loses them.", "Thinking a protected route means the data is protected.", "Putting all state in one global store."],
    quiz=[dict(q="Why use real Link elements for navigation?", o=["They are blue", "People can open, share and bookmark them", "They are faster to type", "Routers require buttons"], a=1,
               why="Real links work with new tabs, the back button and sharing."),
          dict(q="Which belongs in the URL?", o=["A password", "Filters and the page number of a list", "A secret token", "A credit card number"], a=1,
               why="Shareable view state belongs in the URL. Secrets never do."),
          dict(q="Does a front-end protected route secure the data?", o=["Yes, completely", "No, the server must still check permissions", "Only on phones", "Only with a VPN"], a=1,
               why="Front-end checks can be bypassed. The server must enforce access."),
          dict(q="What is a good tool for caching data fetched from an API?", o=["A TanStack Query style library", "An image", "A CSS file", "A cookie banner"], a=0,
               why="Such libraries handle caching, refreshing and loading states for server state.")],
    activity="Build a small app with routes for home, a list, a detail page and a login-protected account page. Put the list's filter and page number in the URL and test the back button and reload.",
)

LESSONS[13] = dict(   # Forms, validation and error handling
    minutes=14,
    hook="Forms are where your users meet your system, and where most things go wrong: someone types a phone number with spaces, a card is declined, the network drops while they press Submit, or the server rejects a value the screen accepted. Good full stack work makes those moments calm. The user always knows what is wrong, how to fix it and that nothing was lost. In this lesson you will build a form flow that handles validation in the browser, errors from the server, network failures and unexpected crashes, so that your application feels dependable even when things fail.",
    sections=[
        ("The state of a form", """A real form is more than its fields. At any time it is in one of these conditions:

- **Idle:** the user is typing.
- **Invalid:** a value fails a rule, and an error message is shown next to it.
- **Submitting:** the request is in flight. The button is disabled and shows a busy label, so nothing is sent twice.
- **Success:** confirm clearly, and move the user on.
- **Failed:** the server or network said no. Explain what happened and keep what the user typed.

Plan these conditions before you write the code. A form library such as React Hook Form tracks values, errors and submitting status for you, so you write rules instead of plumbing."""),
        ("When and how to validate", """Timing changes how a form feels:

- **Do not scold while typing.** Showing “invalid email” after the first letter is irritating.
- **Validate when the user leaves the field (on blur)** and again **on submit**. Once a field has shown an error, re-check it as the user types, so the message disappears as soon as it is fixed.
- On submit with errors, **move focus to the first invalid field** and summarise the problems.

Write rules in one place using a **schema library** such as Zod or Yup:

> [JavaScript]
> const orderSchema = z.object({
>   name: z.string().trim().min(2, "Enter your full name"),
>   phone: z.string().regex(/^0\\d{10}$/, "Use an 11-digit number, like 08012345678"),
>   qty: z.number().int().min(1).max(50),
> });

The same schema idea works on the server, which keeps the two sides consistent."""),
        ("Messages people can act on", """An error message has one job: help the user fix the problem. Good messages are:

- **Specific:** “Password needs at least 8 characters”, not “Invalid input”.
- **Polite and blame-free:** “We could not find that email”, not “You entered a wrong email”.
- **Next to the problem,** linked to the field with `aria-describedby`, and announced to screen readers.
- **Not colour only:** add an icon or text as well as red.
- **Accompanied by a way forward:** a Try again button, a link to reset the password, or a phone number for help.

Avoid technical words such as “500 Internal Server Error” or stack traces. Log those for yourself and show the user a friendly sentence."""),
        ("Handling server and network errors", """The browser check passing does not mean the server will accept. Handle every outcome:

> [JavaScript]
> async function submitOrder(values) {
>   try {
>     const res = await fetch("/api/orders", {
>       method: "POST",
>       headers: { "Content-Type": "application/json" },
>       body: JSON.stringify(values),
>     });
>     if (res.status === 422) {
>       const { errors } = await res.json();   // { phone: "Already used" }
>       return { fieldErrors: errors };
>     }
>     if (!res.ok) return { message: "Something went wrong. Please try again." };
>     return { order: await res.json() };
>   } catch {
>     return { message: "No connection. Your details are saved, try again." };
>   }
> }

Map the server's field errors back onto the matching fields. For a network failure, keep the data and offer a retry. For a **timeout**, make sure that retrying cannot create a duplicate (the server side of this is called idempotency)."""),
        ("When something crashes", """Even careful code has bugs. Make sure a crash in one component does not turn the whole page white:

- Use an **error boundary** around major parts of the screen, which shows a fallback message and a reload button instead of a blank page.
- Send crashes to an **error tracking service** (a free tier of Sentry is common) so you learn about them before users complain.
- Keep a **global handler** for 401 responses: if the session expired, send the user to the login page with a clear note, and return them afterwards.
- Test the sad paths on purpose: switch off the network in developer tools, return a 500 from the API, and submit empty and extreme values.

Resilient software is not software that never fails. It is software that fails gracefully."""),
    ],
    diagram=compare(("IN THE BROWSER", ["Quick feedback while filling in", "Types, lengths, formats", "Can be bypassed"]), ("ON THE SERVER", ["The real gatekeeper", "Rules, permissions, duplicates", "Cannot be bypassed"]), vs="and",
                    note="You need both: one for kindness, one for safety."),
    caption="Browser checks give quick, kind feedback. Server checks are the real protection. A good form uses both.",
    terms=[("Schema", "A written description of what valid data looks like, used to check values."), ("On blur", "The moment a user leaves a field, a good time to validate it."),
           ("aria-describedby", "An attribute that links an error message to its field for screen readers."), ("Error boundary", "A component that catches a crash and shows a fallback instead of a blank page."),
           ("Idempotent", "An action that has the same result however many times it is repeated."), ("422", "A status code meaning the data was understood but failed validation.")],
    mistakes=["Showing errors while the user is still typing the first letter.", "Clearing the form after a failed submission.", "Showing raw server errors to users.", "Allowing the submit button to be clicked twice."],
    quiz=[dict(q="When is a good time to first validate a field?", o=["Before the page loads", "After every single keystroke from the start", "When the user leaves the field and again on submit", "Never"], a=2,
               why="Validating on blur and on submit avoids nagging while still giving quick feedback."),
          dict(q="Why disable the submit button while the request is running?", o=["To save electricity", "To prevent duplicate submissions", "To hide errors", "It is required by HTML"], a=1,
               why="Double clicks can create duplicate orders."),
          dict(q="What should you do with the user's typed data when the network fails?", o=["Clear it", "Keep it and offer to retry", "Send it to a friend", "Print it"], a=1,
               why="Losing typed data is one of the most frustrating failures."),
          dict(q="What does an error boundary do?", o=["Catches a component crash and shows a fallback", "Checks the user's age", "Blocks hackers", "Compresses images"], a=0,
               why="It stops one crash from blanking the whole page.")],
    activity="Build an order form with schema validation on blur and submit, server field errors mapped to fields, a disabled busy button and an error boundary. Test it with the network switched off.",
)

LESSONS[14] = dict(   # Connecting the front end to an API
    minutes=14,
    hook="The front end and the back end are written by the same person on a small project, but they behave like two separate programs that only communicate through requests. How you connect them decides whether the code stays tidy or turns into fetch calls scattered across fifty files. In this lesson you will build the connection properly: one API client, one place for the base address and authentication, shared handling of loading and errors, caching that avoids needless requests, and the local setup that avoids confusing browser errors while you develop.",
    sections=[
        ("One API client, not fetch everywhere", """Create a single module that knows how to talk to your back end, and have every screen use it:

> [JavaScript]
> // lib/api.js
> const BASE = import.meta.env.VITE_API_URL || "/api";
>
> export async function api(path, { method = "GET", body } = {}) {
>   const res = await fetch(BASE + path, {
>     method,
>     credentials: "include",           // send the session cookie
>     headers: body ? { "Content-Type": "application/json" } : {},
>     body: body ? JSON.stringify(body) : undefined,
>   });
>   if (res.status === 401) window.location.assign("/login");
>   if (!res.ok) throw await toError(res);
>   return res.status === 204 ? null : res.json();
> }

Now the base address, the credentials, the headers and the error handling are written **once**. Feature code becomes short: `api("/orders")`, `api("/orders", { method: "POST", body })`."""),
        ("Configuration for each environment", """Your app talks to different back ends in different places: your laptop, a test copy and the live site. Keep the address in **environment variables**, never typed into components. In Vite, variables that start with `VITE_` are available in the browser. Remember the rule: **everything in front-end code is public**, so only put harmless values there, such as the API address and public keys. Secret keys belong on the server.

During development, a **dev proxy** forwards `/api` requests from the front-end dev server to your back end, which avoids CORS errors and means the same relative address works locally and in production. If you do need cross-origin calls, configure CORS on the **server** to allow exactly your front-end origin, and never use `*` together with cookies."""),
        ("Fetching, caching and refreshing", """Calling the API inside every component leads to repeated requests and inconsistent screens. A data library such as **TanStack Query** manages **server state** for you:

> [JSX]
> const { data, isLoading, error } = useQuery({
>   queryKey: ["orders"],
>   queryFn: () => api("/orders"),
> });
>
> const create = useMutation({
>   mutationFn: (values) => api("/orders", { method: "POST", body: values }),
>   onSuccess: () => queryClient.invalidateQueries({ queryKey: ["orders"] }),
> });

You get caching, loading and error flags, retries, and automatic refreshing. After a successful change, you **invalidate** the related query so the list updates. Handle the loading, empty and error states in every screen, and consider **optimistic updates** for actions that almost always succeed."""),
        ("Pagination, search and big lists", """Never load thousands of records at once. Agree a convention with the back end:

- **Pagination:** `/orders?page=2&per_page=20`, and the response includes the total count or a next-page marker.
- **Search and filters:** `/orders?status=paid&q=ada`, read from the URL so they can be shared.
- **Debounce** the search box (wait about 300 milliseconds after the last key) so you do not send a request on every letter.
- **Infinite scroll or a Load more button** for feeds, with a normal pagination fallback for accessibility.

Show the user where they are (“Page 2 of 14”), keep previous results visible while the next page loads, and cancel outdated requests so a slow old answer cannot overwrite a newer one."""),
        ("Keeping both sides in agreement", """Most front-end and back-end bugs are misunderstandings about the data shape: a field renamed on one side, a number that arrives as text, a missing value. Reduce them:

1. **Write the contract first.** Describe each endpoint's request and response in an **OpenAPI** file or a shared document, and build against it.
2. **Generate or share types** (TypeScript types from the OpenAPI file) so mistakes are caught while typing.
3. **Use the same names and formats on both sides.** Use ISO 8601 timestamps in UTC and integer amounts in the smallest currency unit (kobo).
4. **Test the contract** with a few API tests and a mock server such as MSW, so the front end can be built before the back end is ready.
5. **Version your API** so old clients keep working when you change things.

The cleaner the agreement, the fewer late-night surprises."""),
    ],
    diagram=stack([("SCREENS AND COMPONENTS", "Ask for data, show loading, error and empty"), ("DATA LAYER", "Queries, mutations, cache"), ("API CLIENT", "Base address, cookies or token, errors"), ("THE NETWORK", "HTTPS requests to your back end")], "fs14",
                  note="Each layer has one job.", both=True),
    caption="Screens use a data layer, which uses one API client, which talks to the network. Each layer has one job.",
    terms=[("API client", "A single module through which the front end makes all requests to the back end."), ("Dev proxy", "A development setting that forwards API requests to the back end to avoid CORS problems."),
           ("Query invalidation", "Marking cached data as outdated so it is fetched again after a change."), ("Debounce", "Waiting for a pause before sending a request, such as for a search box."),
           ("OpenAPI", "A standard format for describing an API's endpoints, requests and responses."), ("Contract", "The agreed shape of requests and responses between front end and back end.")],
    mistakes=["Scattering fetch calls with hard-coded addresses across many files.", "Putting secret keys in VITE_ variables.", "Loading every record at once instead of paginating.", "Letting a slow old response overwrite a newer one."],
    quiz=[dict(q="Why create one API client module?", o=["It makes the app slower", "Base address, credentials and error handling are written once", "Browsers require it", "To avoid HTTPS"], a=1,
               why="Central code is easier to change and keeps behaviour consistent."),
          dict(q="Which value is safe to put in front-end environment variables?", o=["A database password", "A secret Paystack key", "The public API address", "An admin token"], a=2,
               why="Front-end code is public, so only harmless values belong there."),
          dict(q="What does invalidating a query do?", o=["Deletes the database", "Marks cached data as outdated so it is fetched again", "Logs the user out", "Disables caching forever"], a=1,
               why="After a change, invalidation refreshes what the screen shows."),
          dict(q="Why debounce a search box?", o=["To avoid sending a request on every keystroke", "To change the colour", "To log users out", "To enlarge the text"], a=0,
               why="Waiting for a pause reduces needless requests.")],
    activity="Create an api.js client and use it on three screens. Add a dev proxy, a paginated list read from the URL, a debounced search box, and refresh the list after creating an item.",
)

LESSONS[15] = dict(   # Designing a REST API
    minutes=15,
    hook="Once other people, or other parts of your own system, depend on your API, you cannot change it freely. Mobile apps in the wild keep calling old addresses for years. A well-designed API feels obvious: the addresses are guessable, the errors are helpful and the behaviour is consistent from one endpoint to the next. A poorly designed one produces confusion, bugs and angry messages. You already know what REST is. In this lesson you will learn how to design the details well: naming, methods, status codes, pagination, error shapes, versioning, safe retries and documentation.",
    sections=[
        ("Resources and clear names", """Design around **resources** (things), not actions. Use plural nouns for collections, and let the HTTP method be the verb:

> [Endpoints]
> GET    /api/v1/orders            list orders
> POST   /api/v1/orders            create an order
> GET    /api/v1/orders/88         read one order
> PATCH  /api/v1/orders/88         change some fields
> DELETE /api/v1/orders/88         remove it
> GET    /api/v1/orders/88/items   the items of an order

Avoid verbs in addresses such as `/getAllOrders` or `/createOrder`. For real actions that do not fit CRUD, a small sub-resource is fine: `POST /orders/88/cancel`. Be consistent: lowercase, plural, hyphens for words, and the same names that your database and front end use."""),
        ("Methods, status codes and safety", """Use each method for its meaning:

- **GET** reads and must never change data. It is safe to cache and repeat.
- **POST** creates, or triggers an action.
- **PUT** replaces a whole resource, **PATCH** changes part of it.
- **DELETE** removes. Repeating it should not cause harm.

Return the **right status code**: `200` OK, `201` Created (with the new resource), `204` No Content, `400` bad request, `401` not signed in, `403` not allowed, `404` not found, `409` conflict (such as a duplicate), `422` validation failed, `429` too many requests, `500` the server broke. Never return `200` with an error hidden in the body, because clients, monitors and caches all rely on the status code."""),
        ("Lists: pagination, filtering and sorting", """Collections grow, so design lists carefully from day one:

> [Request]
> GET /api/v1/orders?status=paid&sort=-created_at&page=2&per_page=20

> [Response]
> { "data": [ ... ], "page": 2, "per_page": 20, "total": 137 }

Set a **default and maximum page size** (for example 20 and 100) so nobody can ask for a million rows. For very large or fast-changing data, **cursor pagination** (`?after=ORDER_ID`) is more reliable than page numbers. Whitelist the fields people may sort and filter by, and make sure the database has indexes for them. Return only fields the client needs, never private ones such as `password_hash`."""),
        ("One consistent error shape", """Errors should look the same everywhere, so the front end can handle them with one piece of code:

> [JSON]
> {
>   "error": {
>     "code": "validation_failed",
>     "message": "Some fields need attention.",
>     "fields": { "phone": "Use an 11-digit number", "qty": "Must be at least 1" }
>   }
> }

Give each error a **stable machine-readable code** and a **human-friendly message**. Do not leak stack traces, SQL or file paths. Make **retries safe**: for payments and orders, accept an **idempotency key** header, so that a repeated request after a timeout returns the original result instead of creating a second order. Add **rate limits** and return `429` with a `Retry-After` header."""),
        ("Versioning, documentation and review", """Plan for change:

- **Version in the address** (`/api/v1/`). When you must break compatibility, release `/v2/` and keep `/v1/` working for a period.
- **Prefer additive changes:** adding a field is safe, renaming or removing one is breaking.
- **Document with OpenAPI** and publish it with a page such as Swagger UI, including examples of requests, responses and errors.
- **Design review checklist:** Are names consistent? Are methods and status codes right? Are lists paginated? Is the error shape uniform? Is authorisation checked on every endpoint? Are private fields excluded? Are retries safe?

Have a teammate try to use the API from the documentation alone. Wherever they get stuck, the design or the docs need work."""),
    ],
    diagram=compare(("WEAK DESIGN", ["POST /getAllProducts", "Always returns 200", "Different error formats", "No pagination"]), ("GOOD DESIGN", ["GET /api/v1/products", "Correct status codes", "One error shape", "Pagination and filters"]), vs="vs",
                    note="Predictable beats clever."),
    caption="A good API uses nouns, the right methods and status codes, one error shape and pagination.",
    terms=[("Resource", "A thing your API exposes, such as an order, named with a plural noun."), ("Idempotency key", "A unique value that lets the server recognise and ignore a repeated request."),
           ("Cursor pagination", "Paging through results using a marker of the last item instead of page numbers."), ("Rate limit", "A cap on how many requests a client may make in a period."),
           ("Breaking change", "A change that makes existing clients stop working."), ("OpenAPI", "A standard way of describing an API so tools can document and test it.")],
    mistakes=["Putting verbs in endpoint names.", "Returning 200 with an error message inside.", "Returning unlimited rows from a list endpoint.", "Renaming or removing a field without versioning."],
    quiz=[dict(q="Which endpoint name is best?", o=["GET /orders", "GET /getOrders", "POST /fetchAllTheOrders", "GET /Orders_List"], a=0,
               why="Plural nouns with the method as the verb are clean and predictable."),
          dict(q="Which status code means the resource was created?", o=["200", "404", "201", "301"], a=2,
               why="201 Created is the standard answer to a successful POST that makes something new."),
          dict(q="Why use an idempotency key?", o=["To make URLs shorter", "So a repeated request does not create a duplicate", "To encrypt the body", "To speed up the database"], a=1,
               why="After a timeout, a retry returns the original result instead of charging twice."),
          dict(q="Which change is safe without a new API version?", o=["Renaming a field", "Removing a field", "Adding a new optional field", "Changing a field's type"], a=2,
               why="Adding optional fields does not break existing clients.")],
    activity="Design a complete REST API for an order system on paper: list the endpoints with methods and status codes, the list parameters, one error example and where an idempotency key is needed.",
)

LESSONS[16] = dict(   # Middleware, validation and error handling on the server
    minutes=14,
    hook="Think of a busy bank branch. Before a customer reaches the cashier, a guard checks the door, a desk records who came in, and a clerk checks the forms. The cashier only does the actual transaction. Server middleware works the same way. It is a line of small functions that every request passes through before and after your main code, handling jobs such as logging, authentication, validation, rate limiting and error formatting. Done well, your route handlers stay short and your safety rules are applied everywhere, not just where you remembered them.",
    sections=[
        ("The request pipeline", """A request does not jump straight into your handler. It travels through a **pipeline**:

1. **Request ID and logging:** give the request a unique id and note when it started.
2. **Security headers and CORS.**
3. **Rate limiting:** refuse clients that send too many requests.
4. **Authentication:** work out who is calling.
5. **Authorisation:** check that this user may do this action.
6. **Validation:** check the shape and values of the input.
7. **The handler:** do the real work.
8. **Error handling and response logging:** turn any problem into a clean response and record the result.

Each stage can **stop** the request early with a proper response (for example `401`), so later stages never run on bad or unauthorised input."""),
        ("Middleware in practice", """In Flask the building blocks are decorators and hooks:

> [Python]
> import time, uuid
> from flask import g, request
>
> @app.before_request
> def start():
>     g.request_id = uuid.uuid4().hex[:12]
>     g.t0 = time.perf_counter()
>
> @app.after_request
> def finish(resp):
>     ms = (time.perf_counter() - g.t0) * 1000
>     resp.headers["X-Request-Id"] = g.request_id
>     app.logger.info("%s %s %s %.0fms id=%s", request.method, request.path, resp.status_code, ms, g.request_id)
>     return resp

In Express the same idea is `app.use((req, res, next) => { ... next(); })`. The order matters: logging first, then protections, then your routes, with the error handler last."""),
        ("Validate at the door", """Validation belongs at the edge, before any real work happens. Define a **schema** for each endpoint's input and reject anything that does not match, using a library such as Pydantic, Marshmallow or Zod:

> [Python]
> from pydantic import BaseModel, Field
>
> class OrderIn(BaseModel):
>     item_id: int
>     qty: int = Field(ge=1, le=50)
>     note: str = Field(default="", max_length=200)

Check the **type, range, length and format**, ignore unknown fields, trim whitespace and normalise values (lowercase email). Never trust the client for money: take the product id and quantity, then look up the price and calculate the total on the server. Return `422` with field messages, using the same error shape as the rest of the API."""),
        ("Central error handling", """Do not wrap every handler in its own try and except. Raise meaningful errors and handle them in **one place**:

> [Python]
> class ApiError(Exception):
>     def __init__(self, status, code, message, fields=None):
>         self.status, self.code, self.message, self.fields = status, code, message, fields or {}
>
> @app.errorhandler(ApiError)
> def handle_api_error(e):
>     return {"error": {"code": e.code, "message": e.message, "fields": e.fields}}, e.status
>
> @app.errorhandler(Exception)
> def handle_unexpected(e):
>     app.logger.exception("Unhandled error id=%s", g.get("request_id"))
>     return {"error": {"code": "server_error", "message": "Something went wrong."}}, 500

Expected problems (not found, not allowed, invalid) become clear 4xx responses. Unexpected ones are logged **in full with the request id** and shown to the user as a short, safe message with no stack trace."""),
        ("Keep handlers thin and safe", """With middleware doing the cross-cutting work, a handler can focus on the business:

- **Handler:** read the validated input, call a **service function**, return the result.
- **Service:** the business rules, easy to test without HTTP.
- **Data access:** the queries, using parameterised SQL.

A few extra safeguards: set **timeouts** on calls to other services, limit request body size, return `405` for wrong methods, and make sure the error handler cannot itself crash. Test the pipeline by sending bad input, expired sessions, huge bodies and repeated requests, and check that each gives a clean, logged, consistent response."""),
    ],
    diagram=flow([("Request", "arrives"), ("Logging", "id and limits"), ("Auth", "who are you?"), ("Validate", "is it valid?"), ("Handler", "real work"), ("Response", "sent and|logged")], "fs16",
                 note="Each stage can stop the request early."),
    caption="Every request passes through logging, authentication and validation before the handler, and errors are handled in one place.",
    terms=[("Middleware", "A function that runs before or after your route code for every request."), ("Pipeline", "The ordered chain of middleware a request passes through."),
           ("Schema validation", "Checking input against a written description of valid data."), ("Request ID", "A unique value attached to each request so its logs can be traced together."),
           ("Service layer", "Functions that hold business rules, separate from HTTP code."), ("Central error handler", "One place that turns every error into a consistent response.")],
    mistakes=["Writing authentication checks separately in every route and forgetting one.", "Trusting prices or totals sent by the client.", "Showing stack traces to users.", "Wrapping every handler in its own try and except instead of one central handler."],
    quiz=[dict(q="Why does the order of middleware matter?", o=["It does not", "Alphabetical order is required", "Earlier stages can stop a request before later ones run", "Browsers choose the order"], a=2,
               why="For example, authentication must run before the handler, and the error handler must come last."),
          dict(q="Who should calculate the total of an order?", o=["The client", "The server, from prices it looks up itself", "The user", "The browser extension"], a=1,
               why="Never trust money values from the client."),
          dict(q="What should an unexpected error show the user?", o=["The full stack trace", "A short safe message, while the details are logged", "The database password", "Nothing at all, not even a response"], a=1,
               why="Details help attackers, so log them privately and show a friendly sentence."),
          dict(q="What is the benefit of a request ID?", o=["All log lines from one request can be traced together", "Faster images", "Better colours", "Smaller cookies"], a=0,
               why="It lets you follow a single request through your logs.")],
    activity="Add to a Flask or Express app: a request id with timing logs, schema validation on one endpoint, an ApiError class and a central error handler. Test with bad input and a forced crash.",
)

LESSONS[17] = dict(   # Background jobs, email and file uploads
    minutes=15,
    hook="Some jobs are too slow or too unreliable to do while a customer waits. Sending an email, generating a PDF receipt, resizing an uploaded photo or calling a slow external service can take seconds, and sometimes fail. If your server does them inside the web request, the page hangs, and a failure can ruin the whole order. Professional applications hand these jobs to a background worker and answer the user at once. In this lesson you will learn how queues and workers work, how to send email that actually reaches inboxes, and how to accept file uploads without opening a door for attackers.",
    sections=[
        ("Why background jobs exist", """A web request should be quick, ideally well under a second. Anything slow or unreliable should be moved out of it:

- Sending emails or SMS messages.
- Generating reports, PDFs and exports.
- Processing images, audio or video.
- Calling slow or flaky third-party APIs.
- Cleaning old data and other **scheduled** work.

The pattern: the request saves what is needed, **adds a job to a queue**, and returns immediately (`202 Accepted` or the created resource). A separate **worker** process takes jobs from the queue and does the work. The customer sees “Order received” in a moment, and the email arrives a few seconds later."""),
        ("Queues, workers and retries", """The parts are simple:

1. **Producer:** your web app, which creates a job such as `send_receipt(order_id=88)`.
2. **Queue (broker):** a list of waiting jobs, stored safely in Redis or a database.
3. **Worker:** a separate process that runs the jobs. Tools include Celery or RQ for Python, and BullMQ for Node.

Real systems fail, so design jobs to be safe:

- **Retries with a delay that grows** (back-off), up to a maximum number of attempts.
- **Idempotent jobs:** running the same job twice must not send two emails or charge twice. Store a “sent” flag and check it first.
- **Pass ids, not whole objects,** and load fresh data in the worker.
- A **dead-letter list** for jobs that keep failing, so you can inspect them.
- **Scheduled jobs** (cron style) for daily tasks, such as reminders."""),
        ("Sending email that reaches the inbox", """Use a transactional email service such as Resend, Postmark or SendGrid, rather than sending directly from your own server. To avoid the spam folder:

- **Authenticate your domain** with **SPF**, **DKIM** and **DMARC** records in DNS. This proves the mail really comes from you.
- Send from a **real address on your own domain**, such as `hello@yourdomain.com`.
- Send **only expected messages:** receipts, confirmations, password resets. For anything promotional, get consent and include an unsubscribe link.
- **Handle bounces and complaints:** stop sending to addresses that bounce.
- Keep the content **simple and honest**, with a clear subject line and a plain text version.
- Always send in the **background job**, and log the provider's message id.

Test with a real inbox on Gmail and another provider before launch."""),
        ("Accepting file uploads safely", """Uploads are risky, because the file, its name and its type all come from an untrusted user. Defend in layers:

1. **Limit the size** at the web server and in your code.
2. **Check the type by content,** not by the file extension or the `Content-Type` the client claims. Allow only the types you need (for example JPEG, PNG, PDF).
3. **Never use the original filename** to store the file. Generate a random name, and keep the original only as display text.
4. **Do not store uploads inside your code folder or serve them as executable files.**
5. **Store files in object storage** (S3, Cloudflare R2, Supabase Storage) rather than on the app server, whose disk may vanish on redeploy.
6. **Serve private files through short-lived signed links,** and check permissions before creating one.
7. **Process images in the background:** resize them and remove location data from photos.

Where possible, scan files for malware and set strict limits per user."""),
        ("Telling the user what is happening", """Background work changes the user experience, so design for it:

- Show a clear state: “Receipt on its way”, “Processing your photo…”.
- For long jobs, store a **status** (`queued`, `running`, `done`, `failed`) in the database and let the front end **poll** an endpoint or listen for updates.
- If a job fails permanently, tell the user and offer a fix, and **alert yourself**.
- Keep an **admin view** of failed jobs so nothing is lost silently.
- Remember privacy: emails and uploads often contain personal data, so log ids, not content.

The principle is to make slow things invisible when possible, and honest when not."""),
    ],
    diagram=seq(["Browser", "Web app", "Queue", "Worker"], [(0, 1, "POST /orders"), (1, 2, "add job: send receipt"), (1, 0, "201 Created at once"), (2, 3, "worker takes the job"), (3, 0, "email arrives")], "fs17",
                note="The customer never waits for the email."),
    caption="The web app saves the order, queues the slow job and answers at once, while a worker sends the email.",
    terms=[("Queue", "A list of jobs waiting to be done by workers."), ("Worker", "A separate process that takes jobs from a queue and runs them."),
           ("Back-off", "Waiting longer after each failed attempt before retrying."), ("SPF, DKIM and DMARC", "DNS records that prove an email really comes from your domain."),
           ("Signed link", "A temporary web address that gives access to a private file."), ("Object storage", "A service for storing files, such as S3, separate from your app server.")],
    mistakes=["Sending email inside the web request so the page hangs.", "Writing jobs that send twice if they run twice.", "Trusting the file extension or the original filename.", "Storing uploads on a server disk that disappears on redeploy."],
    quiz=[dict(q="Why move email sending into a background job?", o=["Emails are illegal otherwise", "The user does not wait and a failure does not ruin the request", "It makes emails longer", "It avoids DNS"], a=1,
               why="Slow or flaky work should not block or break the web request."),
          dict(q="What should a job be, so retries are safe?", o=["Random", "Idempotent", "Secret", "Very long"], a=1,
               why="Running it twice must not double-send or double-charge."),
          dict(q="How should you check an uploaded file's type?", o=["Trust the extension", "Trust the browser's Content-Type", "Check the file's actual content", "Skip checking"], a=2,
               why="Both name and declared type can be faked."),
          dict(q="Which DNS records help your email reach inboxes?", o=["SPF, DKIM and DMARC", "A and AAAA only", "Only MX", "TXT is never used"], a=0,
               why="They authenticate your sending domain.")],
    activity="Add a background job to a small app: on order creation, queue a receipt email with retries and a sent flag. Add an image upload with a size limit, a content type check and a random stored name.",
)

LESSONS[18] = dict(   # SQL in depth: joins, indexes and transactions
    minutes=15,
    hook="Most real applications are really databases with a user interface on top. The speed, correctness and safety of your product depend heavily on how well you can talk to your data. You already know basic SQL. This lesson takes you to the level used in real jobs: combining tables with joins, summarising with grouping, structuring complex queries with common table expressions, making queries fast with indexes and the EXPLAIN tool, and protecting data integrity with transactions. Every example is in PostgreSQL, which is the database most professional teams choose.",
    sections=[
        ("Joins: combining tables", """Data is split across tables, and a **join** connects rows by a shared key:

> [SQL]
> SELECT o.id, u.name, o.total_kobo
> FROM orders o
> JOIN users u ON u.id = o.user_id
> WHERE o.status = 'paid'
> ORDER BY o.created_at DESC;

The common types:

- **INNER JOIN** (just `JOIN`): only rows that have a match on both sides.
- **LEFT JOIN:** every row from the left table, with empty values (NULL) where the right has no match. Use it for “all customers, including those with no orders”.
- **RIGHT JOIN** and **FULL JOIN** exist but are rarely needed.

Always join on the **key columns**, and double check the result count. A wrong join condition can silently multiply rows."""),
        ("Summarising: GROUP BY, HAVING and more", """To answer business questions, group rows and calculate:

> [SQL]
> SELECT u.id, u.name,
>        COUNT(o.id)          AS orders,
>        COALESCE(SUM(o.total_kobo), 0) AS spent_kobo
> FROM users u
> LEFT JOIN orders o ON o.user_id = u.id AND o.status = 'paid'
> GROUP BY u.id, u.name
> HAVING COUNT(o.id) >= 3
> ORDER BY spent_kobo DESC
> LIMIT 10;

`WHERE` filters rows **before** grouping. `HAVING` filters groups **after**. Aggregate functions are `COUNT`, `SUM`, `AVG`, `MIN` and `MAX`. `COALESCE` replaces NULL with a default. **Window functions** (such as `ROW_NUMBER() OVER (PARTITION BY ...)`) rank or total rows without collapsing them, and they are worth learning next."""),
        ("Readable complex queries", """When a query grows, break it into named steps with a **CTE** (common table expression):

> [SQL]
> WITH paid AS (
>   SELECT user_id, SUM(total_kobo) AS spent
>   FROM orders WHERE status = 'paid'
>   GROUP BY user_id
> )
> SELECT u.name, paid.spent
> FROM paid JOIN users u ON u.id = paid.user_id
> WHERE paid.spent > 5000000;

Other useful tools: **subqueries** (`WHERE id IN (SELECT ...)`), `EXISTS` for “does a related row exist?”, `DISTINCT`, `CASE WHEN` for conditional values, and `UNION`. Write SQL for people to read: uppercase keywords, one clause per line, clear aliases. And always use **parameters** for values from users (`%s`), never string joining."""),
        ("Indexes and EXPLAIN", """Without an index, the database reads **every row** of a table to find matches. An **index** is like a book's index: it jumps straight to the rows. Create one for columns you often filter, join or sort by:

> [SQL]
> CREATE INDEX idx_orders_user_created ON orders (user_id, created_at DESC);
>
> EXPLAIN ANALYZE
> SELECT * FROM orders WHERE user_id = 7 ORDER BY created_at DESC LIMIT 20;

`EXPLAIN ANALYZE` shows how the query ran. A **Seq Scan** on a big table is a warning sign, while an **Index Scan** is good. Foreign keys are not indexed automatically in PostgreSQL, so index them. But indexes are not free: each one slows writes and takes space, so add them where measurements show a need. Also beware of the **N+1 problem**: loading 100 orders and then running 100 more queries for their items. Fix it with a join or one query using `IN`."""),
        ("Transactions: all or nothing", """A **transaction** groups several changes so they either **all happen or none do**. Consider placing an order: create the order, create its items, reduce stock, record the payment. If the third step fails and the first two stay, your data is wrong.

> [Python]
> with conn.transaction():
>     order_id = conn.execute("INSERT INTO orders (...) VALUES (...) RETURNING id", ...).fetchone()[0]
>     conn.execute("INSERT INTO order_items (...) VALUES (...)", ...)
>     conn.execute("UPDATE stock SET qty = qty - %s WHERE id = %s AND qty >= %s", ...)

The ideas behind it are called **ACID**: atomic, consistent, isolated and durable. Two requests changing the same rows can collide, so keep transactions **short**, lock rows in a **consistent order** to avoid deadlocks, and use constraints (`CHECK (qty >= 0)`) as a final safety net. Never hold a transaction open while waiting for a slow external API."""),
    ],
    diagram=compare(("INNER JOIN", ["Only rows with a match on both sides", "Customers who have orders"]), ("LEFT JOIN", ["All rows from the left table", "Customers, even with no orders"]), vs="or",
                    note="Pick the join that matches the question you are asking."),
    caption="An inner join keeps only matching rows. A left join keeps every row from the left table.",
    terms=[("Join", "Combining rows from two tables using a shared key."), ("GROUP BY", "A clause that groups rows so you can count, add or average each group."),
           ("CTE", "A named temporary result, written with WITH, that makes complex queries readable."), ("Index", "A structure that lets the database find rows without reading the whole table."),
           ("EXPLAIN ANALYZE", "A command that shows how the database ran a query and how long each step took."), ("Transaction", "A group of changes that either all succeed or all are undone.")],
    mistakes=["Joining on the wrong column and multiplying rows.", "Adding indexes everywhere without measuring.", "Running one query per row in a loop (the N+1 problem).", "Keeping a transaction open while calling a slow external API."],
    quiz=[dict(q="Which join keeps every row from the left table?", o=["INNER JOIN", "LEFT JOIN", "CROSS only", "No join does"], a=1,
               why="A LEFT JOIN keeps all left rows, filling NULL where the right side has no match."),
          dict(q="What is the difference between WHERE and HAVING?", o=["WHERE filters groups after grouping, HAVING filters rows before", "They are the same", "HAVING filters groups after grouping, WHERE filters rows before", "HAVING only works on text"], a=2,
               why="WHERE runs before grouping on rows. HAVING runs after on the groups."),
          dict(q="What does a Seq Scan on a very large table in EXPLAIN often suggest?", o=["Perfect speed", "A missing index may be needed", "The table is empty", "A syntax error"], a=1,
               why="It means the database read every row, which can be slow."),
          dict(q="What does a transaction guarantee?", o=["Faster queries", "All changes happen together or none do", "Free storage", "No errors ever"], a=1,
               why="Atomicity keeps your data consistent when one step fails.")],
    activity="Create users, orders and order_items tables locally. Write a LEFT JOIN with GROUP BY showing every user's total spent, add an index, and compare EXPLAIN ANALYZE before and after.",
)

LESSONS[19] = dict(   # Schema design and migrations
    minutes=15,
    hook="Code can be rewritten in a weekend. A badly designed database schema can haunt a company for years, because the data is already there, people depend on it and changing it risks losing it. Good schema design is therefore one of the highest-value skills in full stack work. In this lesson you will learn how to model real things as tables, how to remove repetition with normalisation, how constraints protect your data from bad values, how to choose types (including money), and how to change a live database safely using migrations.",
    sections=[
        ("From things to tables", """Start with the entities from your plan and give each its own table. Each table needs a **primary key** (`id`), and tables point to each other with **foreign keys**:

> [SQL]
> CREATE TABLE users (
>   id          BIGSERIAL PRIMARY KEY,
>   email       TEXT NOT NULL UNIQUE,
>   name        TEXT NOT NULL,
>   created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
> );
>
> CREATE TABLE orders (
>   id          BIGSERIAL PRIMARY KEY,
>   user_id     BIGINT NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
>   status      TEXT NOT NULL CHECK (status IN ('pending','paid','cancelled')),
>   total_kobo  BIGINT NOT NULL CHECK (total_kobo >= 0),
>   created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
> );

Use **one row per thing**, one column per fact, plain clear names (`created_at`, not `dt`), and the same naming style everywhere."""),
        ("Relationships and normalisation", """There are three kinds of relationship:

- **One to many:** one user has many orders. Put the foreign key on the “many” side.
- **Many to many:** students and courses. Use a **join table** (`enrollments`) holding both keys, plus extra facts such as `enrolled_at`.
- **One to one:** a user and a profile. Rare, and often better as columns on one table.

**Normalisation** means storing each fact **once**. If a customer's name is copied into every order row, a change must be made in hundreds of places and they will disagree. Move it to its own table and refer to it by id. In practice, aim for the **third normal form**: every column describes the key, the whole key and nothing but the key. Sometimes you copy a value on purpose, such as the **price at the time of purchase** in an order item, because history must not change when the product price changes."""),
        ("Constraints and types protect your data", """Do not rely only on application code to keep data valid. Let the **database enforce rules**, because every code path, script and future developer must obey it:

- `NOT NULL` for required values, `UNIQUE` for emails and references.
- `CHECK` for rules such as `qty >= 0`.
- **Foreign keys** with a chosen `ON DELETE` behaviour (restrict, cascade or set null).

Choose types carefully:

- **Money:** store as an **integer in the smallest unit** (kobo), never floating point, which causes rounding errors.
- **Time:** use `TIMESTAMPTZ` and store in UTC. Convert to Lagos time only when showing it.
- **Ids:** `BIGINT` or UUID. **Text:** `TEXT`. **Flexible extras:** `JSONB`, used sparingly.

Also add `created_at` and `updated_at` to most tables, and consider **soft delete** (a `deleted_at` column) when history matters."""),
        ("Migrations: changing the structure safely", """Your schema will change as the product grows. A **migration** is a small, versioned script that moves the database from one structure to the next. Tools: **Alembic** (with Flask or SQLAlchemy), Django migrations, Prisma Migrate, Flyway.

> [Terminal]
> flask db migrate -m "add phone to users"
> flask db upgrade

Rules for healthy migrations:

1. **Keep every migration in Git,** and never edit one that has already run on a shared database.
2. **Test on a copy** of real-looking data first.
3. **Back up before** a risky change.
4. Write a **downgrade** where you can.
5. Run migrations as a **separate deploy step,** not hidden inside app start-up on every instance."""),
        ("Zero-downtime changes", """Changing a live database while people use the app needs care. The safe approach is **expand and contract**:

1. **Expand:** add the new column or table, allowing NULL or with a default. Old code still works.
2. **Migrate data:** copy or fill the new values in small batches.
3. **Switch the app** to use the new structure, and deploy.
4. **Contract:** after you are sure nothing uses the old column, remove it in a later release.

Dangerous in one step: renaming a column, dropping a column, adding `NOT NULL` without a default to a big table, and creating an index on a huge table without `CONCURRENTLY`. Plan each of these as several smaller releases. Treat the database as the most valuable thing you own, and **practise restoring a backup** before you ever need to."""),
    ],
    diagram=hub(("orders", "id, user_id, status, total_kobo"), [("users", "one user has many orders"), ("order_items", "one order has many items"), ("payments", "one order, many payments"), ("products", "items point to a product")],
                note="Each fact lives in one table and tables link by keys."),
    caption="An orders table linked by keys to users, order items, payments and products, with each fact stored once.",
    terms=[("Primary key", "A column that uniquely identifies each row in a table."), ("Foreign key", "A column that refers to the primary key of another table."),
           ("Normalisation", "Organising tables so each fact is stored once."), ("Constraint", "A rule enforced by the database, such as NOT NULL or UNIQUE."),
           ("Migration", "A versioned script that changes the database structure."), ("Expand and contract", "A safe way to change a live schema in several small releases.")],
    mistakes=["Storing money as floating point numbers.", "Copying the same fact into many rows.", "Editing a migration that already ran in production.", "Dropping or renaming a column in one step on a live system."],
    quiz=[dict(q="How should you store naira amounts?", o=["As floating point", "As text with a symbol", "As integers in kobo", "As images"], a=2,
               why="Integers avoid rounding errors."),
          dict(q="How do you model a many-to-many relationship such as students and courses?", o=["With a join table holding both keys", "With one huge text column", "You cannot", "With two copies of each table"], a=0,
               why="A join table links the two sides and can hold extra facts."),
          dict(q="Why enforce rules with database constraints?", o=["The database is slower", "Every code path must obey them, not just one app", "Constraints are decoration", "They replace backups"], a=1,
               why="Constraints protect data from bugs, scripts and future developers."),
          dict(q="What is the first step of expand and contract?", o=["Drop the old column", "Add the new structure without breaking old code", "Delete the backup", "Restart the server"], a=1,
               why="Expanding first keeps the existing application working during the change.")],
    activity="Design a schema for a course shop with users, courses, enrollments, payments and lessons. Write the CREATE TABLE statements with constraints, then a migration that adds a phone column in two safe steps.",
)

LESSONS[20] = dict(   # Caching and performance
    minutes=14,
    hook="The fastest request is the one you never have to make. Caching means remembering the answer to something expensive, so the next person who asks gets it instantly. It is the single most powerful tool for making an application fast and for cutting hosting costs, and also a famous source of confusing bugs, because a cache can show yesterday's data. In this lesson you will learn the layers where caching happens, how to control it with HTTP headers and Redis, how to measure before optimising, and how to keep a cache correct.",
    sections=[
        ("Measure first, then optimise", """Do not guess. Performance work follows a loop:

1. **Set a target:** for example, the products page should respond in under 300 milliseconds on the server.
2. **Measure:** use server timing logs, a **profiler**, `EXPLAIN ANALYZE` on slow queries, and browser Lighthouse and Network tabs.
3. **Find the biggest cost.** It is usually the database, an external API or too much data, not the clever code you were worried about.
4. **Fix one thing,** then measure again.

Look at **percentiles** (p95, the time that 95 out of 100 requests beat), not just the average, because a few slow requests hurt real users. A famous warning applies: premature optimisation wastes time. Make it correct, make it measurable, then make it fast where it matters."""),
        ("The layers of caching", """A request can be answered at several levels, and each one you reach saves work below it:

1. **Browser cache:** files stored on the user's device (images, CSS, JavaScript).
2. **CDN:** servers near the user store copies of public pages and files.
3. **Application cache:** results kept in memory or in **Redis**, shared by all your servers.
4. **Database cache:** the database remembers recent data pages and query plans.

Match the layer to the data. A logo never changes, so cache it for a year. A product list changes now and then, so cache it for a minute. A user's private account page should **not** be cached in shared places at all. Use your head about **who** can see the cached copy."""),
        ("HTTP caching headers", """The server tells browsers and CDNs how long to keep a response:

> [HTTP]
> Cache-Control: public, max-age=31536000, immutable      (versioned files)
> Cache-Control: public, max-age=60                       (a product list)
> Cache-Control: private, no-store                        (an account page)
> ETag: "a1b2c3"

- **`max-age`:** keep it for this many seconds without asking again.
- **`public`** may be stored by shared caches. **`private`** only by the user's own browser. **`no-store`** means do not keep it at all.
- **`ETag`:** a fingerprint of the content. The browser asks “has it changed?”, and the server answers **304 Not Modified** with no body, which saves bandwidth.
- For files with names that include a content hash (`app.4f2a9c.js`), cache them forever. When the content changes, the name changes."""),
        ("Caching in your application", """For expensive results you compute often, store them in **Redis** (or even in process memory for small things):

> [Python]
> def get_top_products():
>     key = "top_products:v1"
>     cached = redis.get(key)
>     if cached:
>         return json.loads(cached)
>     rows = db.query("SELECT ... ORDER BY sold DESC LIMIT 10")
>     redis.setex(key, 60, json.dumps(rows))      # keep for 60 seconds
>     return rows

This is the **cache-aside** pattern: look in the cache, and if it is missing, load from the database and store it. Other useful tricks: avoid **N+1 queries**, add **indexes**, **paginate** big lists, **compress** responses with gzip or Brotli, move slow work to **background jobs**, and use **connection pooling** so each request does not open a new database connection."""),
        ("The hard part: keeping caches correct", """There is an old joke: the two hard things in computing are naming things and cache invalidation. Cached data can become **stale**. Your options:

- **Time to live (TTL):** accept slightly old data for a short, fixed time. It is simple and often good enough.
- **Invalidate on change:** when an order is saved, delete the cache entry it affects.
- **Version the key:** change `top_products:v1` to `v2` when the format changes.
- **Never cache what is private or personal** under a shared key. Include the user id in the key if it is per-user.

Protect against a **cache stampede**, where a popular entry expires and 500 requests rebuild it at once, by using a lock or a slightly randomised TTL. And always make the app work correctly, if more slowly, when the cache is empty or down."""),
    ],
    diagram=flow([("Browser", "cached files"), ("CDN", "copies near|the user"), ("Redis", "app results"), ("Database", "the slowest|place")], "fs20",
                 note="Each layer you reach saves work for the one below."),
    caption="Browser cache, CDN and Redis each answer some requests, so fewer reach the slowest layer, the database.",
    terms=[("Cache", "A saved copy of an expensive result for quick reuse."), ("TTL", "Time to live: how long a cached item may be kept before it expires."),
           ("ETag", "A fingerprint of content used to ask whether a resource changed."), ("Cache-aside", "A pattern where code checks the cache first and loads and stores on a miss."),
           ("Percentile (p95)", "The time that 95 percent of requests are faster than."), ("Cache invalidation", "Removing or refreshing cached data when the real data changes.")],
    mistakes=["Optimising before measuring.", "Caching private pages in a shared cache or CDN.", "Never expiring cached data.", "Relying on the cache so the app breaks when it is empty."],
    quiz=[dict(q="What should you do before optimising?", o=["Rewrite everything", "Measure where the time actually goes", "Add Redis everywhere", "Buy a bigger server"], a=1,
               why="Measurement points to the real bottleneck."),
          dict(q="Which header tells everyone not to store a response at all?", o=["max-age=60", "public", "ETag", "no-store"], a=3,
               why="no-store prevents any cache from keeping the response."),
          dict(q="What is cache-aside?", o=["Check the cache first, and on a miss load from the source and store it", "Delete all data", "Always skip the cache", "Cache only images"], a=0,
               why="The code looks aside at the cache, then fills it when needed."),
          dict(q="Why look at p95 rather than just the average?", o=["It is easier", "A few slow requests can hurt real users even if the average looks fine", "Averages are illegal", "p95 is always smaller"], a=1,
               why="Percentiles reveal the slow tail that users actually feel.")],
    activity="Pick one slow page or query in a small app. Measure it, add either a Cache-Control header or a 60 second Redis cache-aside, and measure again. Note how you would invalidate it when data changes.",
)

LESSONS[21] = dict(   # Sessions, tokens and roles
    minutes=15,
    hook="Once users can log in, three questions follow every single request: who is this, how do I know, and what are they allowed to do? Getting the answers wrong is how companies leak customer data. Two popular designs answer the first two questions: server-side sessions and signed tokens such as JWT. Neither is automatically better, and many tutorials teach the risky parts without warning you. In this lesson you will compare them honestly, learn where to store credentials in the browser, build roles and permission checks that cannot be bypassed, and add the extras that real products need: refresh, logout, multi-factor authentication and social login.",
    sections=[
        ("Server-side sessions", """With a **session**, the server keeps the memory. After login it creates a random **session id**, stores `session id → user` on the server (in the database or Redis), and sends the id to the browser in a **cookie**. On every request the browser returns the cookie, and the server looks the user up.

Strengths: you can **end a session instantly** (delete it), see who is logged in, and the browser holds nothing but a meaningless random id. Weaknesses: the server must store sessions, and every server in a cluster must share the store. For most websites with a browser front end, **cookie sessions are the simplest and safest choice**, and Flask, Django and Rails support them out of the box."""),
        ("Tokens and JWT", """A **token** carries its own proof. A **JWT** (JSON Web Token) is a signed bundle of claims such as `{"sub": 42, "role": "customer", "exp": 1767225600}`. The server checks the **signature**, not a database, so it can verify requests without storing sessions. That suits **mobile apps**, **APIs used by other services**, and systems with many separate servers.

The costs are real:

- A stolen token works until it **expires**, and it is hard to revoke before that.
- So use **short-lived access tokens** (about 15 minutes) with a longer-lived **refresh token** stored safely and rotated on use.
- Always verify the signature and the **expiry**, fix the allowed algorithm, and keep the signing secret private.
- Do not put sensitive data inside: a JWT is encoded, **not encrypted**, so anyone can read it."""),
        ("Where to keep credentials in the browser", """This choice matters for security:

- **`localStorage` or `sessionStorage`:** easy, but readable by any JavaScript on the page, so one **XSS** bug lets an attacker steal the token.
- **HttpOnly cookie:** JavaScript cannot read it, so XSS cannot copy it. Add **`Secure`** (HTTPS only) and **`SameSite=Lax`** or `Strict`, and protect state-changing requests against **CSRF** with a token or by checking the origin.

For a browser-based app, an **HttpOnly, Secure, SameSite cookie** is usually the stronger choice. For mobile apps, use the phone's secure storage (Keychain or Keystore), not plain files. Whichever you choose, send everything over **HTTPS only**."""),
        ("Roles and permissions", """**Authentication** proves who you are. **Authorisation** decides what you may do. A common model is **RBAC** (role-based access control): users have roles such as `customer`, `staff` and `admin`, and roles carry permissions.

Rules that keep it safe:

1. **Check on the server, on every request.** Hiding a button is only decoration.
2. **Check ownership,** not only the role. A customer may read `/orders/88` only if order 88 is theirs. Missing this check is the most common real-world flaw, often called **broken object-level authorisation**.
3. **Deny by default.** Allow only what is explicitly permitted.
4. **Use the least privilege:** give people and services only the access they need.
5. **Centralise the checks** in decorators or middleware, such as `@require_role("admin")`, so no route is forgotten.
6. **Log sensitive actions** (role changes, data exports) for audit."""),
        ("The extras real products need", """Plan for these early:

- **Logout and revocation:** deleting the session, and invalidating refresh tokens. Offer “log out of all devices”.
- **Multi-factor authentication (MFA):** a second proof, such as an authenticator app code. It stops most account takeovers.
- **Social login** with Google or similar (OAuth 2.0 and OpenID Connect). You store fewer passwords, but you must handle the case where the provider is unavailable or the email changes.
- **Rate limiting and lockouts** on login and reset endpoints.
- **Session hygiene:** new session id after login, idle timeout, and re-ask for the password before sensitive actions.
- **Passwordless links or codes** can reduce password problems, but they need the same care with expiry and one-time use.

Prefer a well-tested library or service over inventing your own security code."""),
    ],
    diagram=compare(("SERVER SESSION", ["Random id in an HttpOnly cookie", "Server stores who it is", "Easy to revoke instantly", "Great for websites"]), ("SIGNED TOKEN (JWT)", ["Token carries signed claims", "Server only checks the signature", "Hard to revoke early", "Good for mobile and APIs"]), vs="or",
                    note="Neither is magic. Match the tool to the app."),
    caption="Sessions keep the memory on the server and are easy to revoke. Tokens carry signed claims and suit mobile apps and APIs.",
    terms=[("Session", "Server-side memory of a logged-in user, found through a random id."), ("JWT", "A signed token whose contents are readable but cannot be changed without detection."),
           ("Refresh token", "A longer-lived token used to get new short-lived access tokens."), ("RBAC", "Role-based access control: permissions are given to roles, and users get roles."),
           ("Least privilege", "Giving each person or service only the access it needs."), ("MFA", "Multi-factor authentication: a second proof of identity beyond the password.")],
    mistakes=["Storing long-lived tokens in localStorage.", "Checking the role but not whether the record belongs to the user.", "Thinking a JWT is encrypted.", "Hiding admin buttons without server checks."],
    quiz=[dict(q="What is a big advantage of server-side sessions?", o=["They need no storage", "You can end a session instantly", "They work without cookies", "They are encrypted by default"], a=1,
               why="Deleting the session record logs the user out immediately."),
          dict(q="Is the content of a standard JWT encrypted?", o=["Yes, always", "No, it is signed but readable", "Only on Fridays", "Only with HTTPS"], a=1,
               why="Anyone can decode it, so never put secrets inside."),
          dict(q="A customer changes /orders/88 to /orders/89 and sees another person's order. Which check was missing?", o=["Ownership check on the server", "A bigger font", "Compression", "A CDN"], a=0,
               why="The server must confirm that the record belongs to the signed-in user."),
          dict(q="Which storage protects a token from XSS theft best?", o=["localStorage", "An HttpOnly cookie", "A global variable", "The page URL"], a=1,
               why="HttpOnly cookies cannot be read by JavaScript.")],
    activity="Add login to a small app using a cookie session with HttpOnly, Secure and SameSite flags. Then add roles and a decorator, and prove with two test users that one cannot open the other's order.",
)

LESSONS[22] = dict(   # Git workflows, code review and teamwork
    minutes=14,
    hook="Writing code alone is one skill. Building software with other people is another, and it is the one most jobs actually test. When two developers change the same file, or a teammate merges something that breaks the live site, or nobody knows who is doing what, the problem is not the code. It is the workflow. In this lesson you will learn how teams use Git branches and pull requests without chaos, how to write commits others can understand, how to resolve conflicts calmly, how to review code kindly, and how to communicate so a team of any size, including one spread across time zones, stays in step.",
    sections=[
        ("Choosing a branching workflow", """A workflow is an agreement about how changes enter the main branch:

- **Feature branch workflow (the usual choice):** `main` is always working. Each task gets a short-lived branch (`feature/order-status`), which is merged through a **pull request**.
- **Trunk-based development:** very small changes merged into `main` many times a day, usually with feature flags. Great for experienced teams with strong automated tests.
- **GitFlow:** long-lived `develop` and `release` branches. Heavy, and suited only to products with formal release cycles.

For most small teams, use feature branches off `main`, keep them **short-lived** (days, not weeks), and **protect `main`** so nobody pushes to it directly and merges require passing checks and a review."""),
        ("Commits and pull requests people enjoy reading", """A good history lets you answer “why did this change?” years later.

- **Commit small and often,** each commit doing one thing.
- **Write clear messages:** a short summary in the imperative (“Add order status filter”), then a blank line, then why if needed. Many teams use the **Conventional Commits** style: `feat:`, `fix:`, `docs:`.
- **Keep pull requests small,** ideally under 300 lines. Large ones are rarely reviewed well.
- **Describe the pull request:** what changed, why, how to test it, screenshots for UI, and what to look at carefully.
- **Link it to the issue** it solves, and run the tests before asking for a review.

Never commit secrets, and if you do, **rotate them** at once, since deleting the commit does not make the leaked key safe."""),
        ("Merge conflicts without panic", """A **conflict** happens when two branches change the same lines. Git cannot guess which is right, so it marks both:

> [Git]
> <<<<<<< HEAD
> status = "paid"
> =======
> status = "confirmed"
> >>>>>>> feature/order-status

Stay calm and follow a routine:

1. Update your branch often: `git fetch` then `git rebase origin/main` (or merge `main` into your branch).
2. Open the conflicted file, **read both sides**, and decide what the code should really be. Ask the other author if unsure.
3. Remove the markers, run the **tests**, then `git add` and continue.

Conflicts shrink when branches are short-lived, tasks are split sensibly and people **talk** about who is touching which files. `git rebase` makes a tidy straight history, `git merge` keeps exact history. Pick one team convention and never rebase a branch others have already pulled."""),
        ("Code review: kind and useful", """Review is for the **code and the team**, not for showing who is smartest.

**As an author:** make it easy. Keep changes small, explain them, review your own diff first, and welcome feedback without defensiveness.

**As a reviewer:**
- Read for **correctness, security, clarity and tests.** Is anything missing, risky or confusing?
- **Ask questions** rather than giving orders: “What happens if the list is empty?”
- **Separate** must-fix issues from optional ideas (prefix suggestions with “nit:”).
- Praise good work. Say what is good, not only what is wrong.
- Review **promptly**, ideally within a day, since waiting blocks the author.

Automated tools (linters, tests, formatters) should catch the boring things, so humans can discuss design."""),
        ("Working as a team", """Habits that make teams effective:

- **Track work** on a board (GitHub Projects, Trello, Jira): To do, Doing, Review, Done. Everyone can see who owns what.
- Agree a **definition of done:** code reviewed, tests pass, documented, deployed to staging.
- Hold a short **daily or async update:** what I did, what I will do, what blocks me. Ask for help early.
- **Write things down:** decisions, setup steps and the reasons behind choices, in the README or a docs folder.
- **Communicate across time zones** with clear, complete messages that need no reply to be understood.
- Hold **blameless retrospectives** after problems: focus on how the system allowed the mistake.

A team that communicates well ships more than a team of faster individual coders."""),
    ],
    diagram=cycle([("Issue", "one clear task"), ("Branch", "short-lived"), ("Commit", "small and clear"), ("Pull request", "tests run"), ("Review", "kind and fast")], "fs22", center="Merge to|main",
                  note="A repeatable loop keeps a team calm."),
    caption="A task becomes a short-lived branch, small commits, a pull request, a review and a merge to main.",
    terms=[("Pull request", "A proposal to merge a branch, which teammates can review and discuss."), ("Branch protection", "Rules that stop direct pushes and require checks and reviews before merging."),
           ("Merge conflict", "A situation where two branches changed the same lines and Git needs a human decision."), ("Rebase", "Replaying your commits on top of another branch to keep a straight history."),
           ("Conventional Commits", "A style for commit messages such as feat: and fix:."), ("Definition of done", "The agreed checklist that a task must meet to count as finished.")],
    mistakes=["Keeping a branch alive for weeks, so conflicts pile up.", "Opening a 2,000-line pull request.", "Writing commit messages like “update” or “fix”.", "Making review comments that attack the person."],
    quiz=[dict(q="Why keep feature branches short-lived?", o=["Git deletes old branches", "Smaller differences mean fewer and easier conflicts", "It saves disk space", "Branches expire"], a=1,
               why="Long-lived branches drift away from main and collide with other work."),
          dict(q="What makes a good commit message?", o=["update", "fix stuff", "A short imperative summary such as Add order status filter", "asdf"], a=2,
               why="Clear messages explain what changed and help future debugging."),
          dict(q="You committed an API key by mistake. What must you do?", o=["Nothing, delete the commit", "Rotate the key immediately", "Email it to the team", "Make the repo public"], a=1,
               why="Once a secret has been pushed, treat it as leaked and replace it."),
          dict(q="Which review comment is better?", o=["This is stupid", "What happens here if the list is empty?", "Rewrite it", "Whoever wrote this should be fired"], a=1,
               why="Specific, respectful questions improve code and keep the team healthy.")],
    activity="With a friend, create a repository, protect main, and each make a branch that edits the same line. Open pull requests, create and resolve a merge conflict, and review each other's code kindly.",
)

LESSONS[23] = dict(   # Containers, environments and configuration
    minutes=15,
    hook="“It works on my machine” is the most famous sentence in software, and the most expensive. Your laptop has one version of Python, certain libraries and a particular operating system. The server has others, and a small difference is enough to break an application. Containers solve this by packaging your app together with everything it needs to run, so it behaves the same on your laptop, on a teammate's computer and in production. In this lesson you will learn what containers are, write a Dockerfile, run an app with its database using Docker Compose, and manage configuration and secrets the way professional teams do.",
    sections=[
        ("What a container is", """A **container** is a lightweight, isolated box that runs your application with its own files, libraries and settings. It is not a full virtual machine: containers share the host's operating system kernel, so they start in seconds and use little memory.

Two words to keep straight:

- An **image** is the **recipe and the packaged result**: a read-only template containing your code, dependencies and runtime.
- A **container** is a **running copy** of an image.

You can build an image once and run it anywhere Docker (or a compatible tool) is installed. The same image goes from your laptop to testing to production, which removes “works on my machine” problems."""),
        ("Writing a Dockerfile", """A **Dockerfile** lists the steps to build the image:

> [Dockerfile]
> FROM python:3.12-slim
> WORKDIR /app
>
> COPY requirements.txt .
> RUN pip install --no-cache-dir -r requirements.txt
>
> COPY . .
> RUN useradd -m app && chown -R app /app
> USER app
>
> EXPOSE 8000
> CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

Good habits: use a **small, specific base image** and a version, copy the dependency file and install **before** copying your code (so Docker can reuse that layer), run as a **non-root user**, and add a `.dockerignore` listing files that must not enter the image (`.git`, `.env`, `node_modules`, local databases). Build with `docker build -t shop-api .` and run with `docker run -p 8000:8000 shop-api`."""),
        ("Docker Compose: the whole app locally", """Real apps need a database, a cache, a worker. **Docker Compose** describes them together in one file:

> [YAML]
> services:
>   api:
>     build: .
>     ports: ["8000:8000"]
>     env_file: .env
>     depends_on: [db]
>   db:
>     image: postgres:16
>     environment:
>       POSTGRES_PASSWORD: ${DB_PASSWORD}
>     volumes: ["dbdata:/var/lib/postgresql/data"]
> volumes:
>   dbdata:

One command, `docker compose up`, starts everything. A new teammate can run the whole project in minutes. The **volume** keeps database files outside the container, so your data survives restarts. Never rely on a container's own disk for anything you want to keep."""),
        ("Configuration and secrets", """The rule from the **Twelve-Factor App** method is to keep **configuration in the environment**, separate from code. The same image runs in every environment, and only the settings change:

- **Environment variables:** `DATABASE_URL`, `APP_ENV`, `PAYSTACK_SECRET_KEY`.
- **Local development:** a `.env` file that is **ignored by Git**, and a `.env.example` listing the names.
- **Production:** set variables in your host's dashboard or secret manager (Render, AWS Secrets Manager, Doppler, and others).
- **Never bake secrets into an image or commit them.** Anyone with the image can read them.
- **Validate configuration on start-up:** if a required variable is missing, fail immediately with a clear message.

Different settings, **same code**: development, staging and production should be as similar as possible, so a bug found in staging really predicts production."""),
        ("Health, size and security of containers", """Make containers good citizens:

1. **Health checks:** a `/health` endpoint that confirms the app and database are reachable, so the platform can restart a broken instance.
2. **Log to standard output,** not to files, so the platform collects the logs.
3. **Handle shutdown signals** properly, finishing current requests.
4. **Keep images small** with slim base images and multi-stage builds. Smaller images build, ship and start faster, and have fewer vulnerabilities.
5. **Pin versions** and **scan images** for known vulnerabilities, and update base images regularly.
6. **One process per container,** with workers and the web server as separate containers.
7. Remember that many platforms (such as Render) can build and run your Dockerfile directly, so you may not need to manage servers at all."""),
    ],
    diagram=stack([("YOUR APP CODE", "app.py, routes, templates"), ("DEPENDENCIES", "Flask, psycopg, gunicorn"), ("RUNTIME", "Python 3.12"), ("OS LIBRARIES", "a small Linux base image")], "fs23",
                  note="Image layers: the same box runs anywhere."),
    caption="An image packages your code, dependencies, runtime and base system into layers, so it runs the same everywhere.",
    terms=[("Image", "A read-only package containing your app, its dependencies and its runtime."), ("Container", "A running, isolated copy of an image."),
           ("Dockerfile", "A text file of steps that builds an image."), ("Docker Compose", "A tool that starts several containers, such as app and database, from one file."),
           ("Volume", "Storage kept outside a container so data survives restarts."), ("Twelve-Factor App", "A set of habits for building apps that are easy to deploy and configure.")],
    mistakes=["Baking secrets into the image or committing .env files.", "Running the container as the root user.", "Storing the database inside the container with no volume.", "Never updating the base image."],
    quiz=[dict(q="What is the difference between an image and a container?", o=["An image is a running copy, a container is the recipe", "An image is the packaged template, a container is a running copy of it", "They are the same", "Containers are only for databases"], a=1,
               why="You build an image once and run many containers from it."),
          dict(q="Where should production secrets be kept?", o=["Inside the Docker image", "In Git", "In environment variables or a secret manager", "In the README"], a=2,
               why="Secrets must stay out of images and repositories."),
          dict(q="Why does the Dockerfile copy requirements.txt and install before copying the code?", o=["So Docker can reuse the cached dependency layer when only code changes", "It looks neater", "Docker requires it", "To hide the code"], a=0,
               why="Layer caching makes rebuilds much faster."),
          dict(q="What does a volume do?", o=["Makes the app louder", "Keeps data outside the container so it survives restarts", "Compresses images", "Blocks hackers"], a=1,
               why="Container disks are temporary, so durable data needs a volume or an external database.")],
    activity="Write a Dockerfile and docker-compose.yml for a small Flask or Node app with Postgres, add a .dockerignore and .env.example, and start it with one docker compose up command.",
)

LESSONS[24] = dict(   # Monitoring, logging and scaling
    minutes=15,
    hook="Launching is not the finish line. It is the day the real work starts, because now real people depend on your application, and it will break at the worst time: during a sale, a class, on a Sunday night. The question is whether you find out from your monitoring or from an angry customer. In this lesson you will learn what to log and what never to log, which numbers to watch, how to set alerts that wake you only when it matters, how to respond to an incident calmly, and how to grow an application from a hundred users to a hundred thousand without rewriting it.",
    sections=[
        ("Logs: the story of what happened", """A **log** is a record of events. Make yours useful:

- Use **levels:** `DEBUG` for details, `INFO` for normal events, `WARNING` for odd things, `ERROR` for failures.
- Write **structured logs** (JSON with fields such as `request_id`, `user_id`, `path`, `status`, `ms`) so tools can search and filter them.
- Include the **request id** from your middleware, so you can follow one request across the system.
- Log to **standard output** and let the platform collect it. Tools include Better Stack, Grafana Loki, Datadog and your host's own logs.

**Never log** passwords, tokens, full card details or private personal data. Logs are copied around and kept for a long time, and a leaked log is a data breach. Log ids instead of content."""),
        ("Metrics and the four golden signals", """**Metrics** are numbers over time. Google's engineers recommend four **golden signals** for any service:

1. **Latency:** how long requests take (watch p95, not only the average).
2. **Traffic:** how many requests per minute.
3. **Errors:** the share of requests that fail (5xx).
4. **Saturation:** how full your resources are (CPU, memory, database connections, queue length).

Add **business metrics** too: sign-ups, orders, failed payments. A sudden fall in orders can be the first sign of a problem that no error log shows. Dashboards (Grafana, your host's charts) let you see these at a glance, and compare today with last week."""),
        ("Uptime, errors and alerts", """Three layers of watching:

- **Uptime monitoring:** a free service (UptimeRobot, Better Stack) that checks your `/health` endpoint every minute **from outside** and messages you if it fails.
- **Error tracking:** a tool such as **Sentry** groups crashes, shows the stack trace, the user's browser and the release, so you can fix them quickly.
- **Alerts:** notifications for things that need action.

Good alerts are **actionable and rare.** Alert when users are hurt (high error rate, site down, payments failing), not on every small blip. If alerts fire constantly, people ignore them, which is dangerous. Send them to a place you will actually see, such as phone notifications for the critical few. Write a short **runbook** for each alert: what it means and what to try first."""),
        ("When things go wrong: incidents", """Every system has incidents. A calm routine beats panic:

1. **Confirm and assess:** is it real, how many users, since when?
2. **Communicate:** tell users briefly on a status page or social channel. “We know about the payment issue and are working on it.”
3. **Stabilise first:** **roll back** the last release, switch off the broken feature flag, or restore from backup. Find the root cause later.
4. **Fix and verify** with real checks.
5. **Hold a blameless post-mortem:** timeline, root causes, what worked, and concrete actions with owners.

Also rehearse the boring protections: **test restoring backups,** keep access credentials safe, and know who to call. In Nigeria also remember practical risks, such as power cuts and network problems at your office, and make sure you can reach your dashboards from a phone."""),
        ("Scaling without a rewrite", """Scaling means handling more users. Do it in order, from cheap to complex:

1. **Fix the obvious:** slow queries, missing indexes, N+1 queries, caching, compressed assets and a CDN. This alone often gives 10 times.
2. **Scale up (vertical):** a bigger server. It is simple, and fine for a long time.
3. **Scale out (horizontal):** run several copies of a **stateless** app behind a **load balancer.** This is why sessions and files must not live in one server's memory or disk.
4. **Relieve the database:** connection pooling, read replicas for heavy reads, and cleaning or archiving old data.
5. **Move slow work to queues and workers.**
6. **Load test** (k6, Locust) to find limits before users do, and set **autoscaling** and **spending alerts** so a traffic spike does not bring a surprise bill.

Do not build for a million users on day one. Build cleanly, measure, and scale the part that is actually the bottleneck."""),
    ],
    diagram=hub(("HEALTHY APP", "watched all day"), [("Latency", "how slow is it?"), ("Traffic", "how many requests?"), ("Errors", "how often does it fail?"), ("Saturation", "how full are we?")],
                note="The four golden signals."),
    caption="Watch latency, traffic, errors and saturation. Together they show whether an app is healthy.",
    terms=[("Structured log", "A log entry written as fields, such as JSON, so tools can search it."), ("Golden signals", "Latency, traffic, errors and saturation, the four core measures of a service."),
           ("Runbook", "A short guide that says what an alert means and what to try first."), ("Post-mortem", "A blameless review after an incident to learn and prevent a repeat."),
           ("Horizontal scaling", "Running more copies of an app behind a load balancer."), ("Load test", "A test that sends many simulated users to find the limits of a system.")],
    mistakes=["Logging passwords, tokens or personal data.", "Alerting on every small blip until nobody reads alerts.", "Finding out about an outage from customers.", "Building for a million users before having a hundred."],
    quiz=[dict(q="Which is one of the four golden signals?", o=["Colour", "Saturation", "Font size", "Logo"], a=1,
               why="Saturation, along with latency, traffic and errors, shows how healthy a service is."),
          dict(q="What should you do first during an incident when a new release broke the site?", o=["Roll back, then find the cause", "Write a long report", "Blame someone", "Wait and see"], a=0,
               why="Stabilise first by rolling back, then investigate."),
          dict(q="Why must an app be stateless to scale horizontally?", o=["Any copy behind the load balancer can serve any request", "It is a legal rule", "It makes logs smaller", "State is slow"], a=0,
               why="If state lives in one server's memory, other copies cannot see it."),
          dict(q="What should never appear in logs?", o=["Request ids", "Status codes", "Passwords and tokens", "Timings"], a=2,
               why="Logs travel widely and last long, so secrets in them are a breach waiting to happen.")],
    activity="Add structured request logs and a /health endpoint to a project, set up a free uptime monitor and Sentry, and write a one-page runbook for what you would do if the site returned errors.",
)
