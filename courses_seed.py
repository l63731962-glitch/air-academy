"""Course catalogue seed. Lessons are only ever sent to enrolled users."""

COURSES = [
    dict(id="prompt-engineering", title="AI Prompt Engineering",
         description="Talk to AI clearly and build with it: roles, constraints, structured output, labs and class projects.",
         lessons=["What prompt engineering is", "The 7 building blocks", "Roles, tasks and context", "Constraints and output formats",
                  "Examples and quality criteria", "Testing and improving prompts", "Prompt Lab", "Class projects"]),
    dict(id="animation", title="Animation Masterclass",
         description="From animation fundamentals to professional 2D/3D production, ending with a finished short film.",
         lessons=["Animation Foundations", "Story and Pre-production", "2D Animation", "3D Animation",
                  "Cinematography and Sound", "AI-Assisted Animation", "Production and Portfolio", "Capstone: animated short"]),
    dict(id="cloud-computing", title="Cloud Computing Masterclass",
         description="Cloud fundamentals to deployment and operations: compute, storage, networking, IAM, monitoring and cost control.",
         lessons=["Cloud Fundamentals", "Compute and Storage", "Networking", "Identity and Security",
                  "Data and Application Services", "DevOps and Reliability", "Cost and Governance", "Portfolio Project"]),
    dict(id="web-development", title="Web Development Masterclass",
         description="Build responsive, accessible, real-world websites with HTML, CSS, JavaScript, Git and deployment.",
         lessons=["Web Foundations", "CSS and Responsive Design", "JavaScript", "Modern Front-end",
                  "Backend Introduction", "Data and Quality", "Git and Deployment", "Portfolio Project"]),
    dict(id="app-development", title="App Development Masterclass",
         description="Plan, build, test and release mobile apps: UX, navigation, APIs, storage, testing and store release.",
         lessons=["App Development Foundations", "UI/UX and Navigation", "Programming Foundations", "Data and APIs",
                  "Accounts and Security", "Testing and Quality", "Release and Maintenance", "Portfolio Project"]),
    dict(id="full-stack", title="Full Stack Development Masterclass",
         description="Complete applications from front end to database: APIs, auth, testing, deployment and monitoring.",
         lessons=["Full Stack Foundations", "Front-end Engineering", "Backend Engineering", "Databases",
                  "Authentication and Security", "Testing and Collaboration", "Deployment and Operations", "Portfolio Project"]),
    dict(id="agentic-ai", title="Agentic AI Development Masterclass",
         description="Design reliable AI agents, tools and workflows with evaluation, guardrails and human approval checkpoints.",
         lessons=["Agentic AI Foundations", "Prompt and Model Design", "Tools and Integrations", "Memory and State",
                  "Planning and Orchestration", "Reliability and Evaluation", "Security and Deployment", "Portfolio Project"]),
    dict(id="game-development", title="Game Development Masterclass",
         description="From game design and prototyping to a playable release: loops, physics, UI, audio, testing and publishing.",
         lessons=["Game Design Foundations", "Engine and Programming", "Gameplay Systems", "World and Levels",
                  "UI, Audio, and Feedback", "Testing and Optimization", "Publishing", "Portfolio Project"]),
]

LESSONS = {c["id"]: c["lessons"] for c in COURSES}


# Lesson notes shown inside unlocked courses (and on teachers.html).
# One string per lesson, in order: "learning goal | point; point; point | class activity"
NOTES = {
  "prompt-engineering": [
    "Explain what a prompt is and why wording changes the result. | What a model does with text; Vague versus clear requests; Where prompts are used (chat, apps, automation) | Students rewrite one vague request three ways and compare the answers.",
    "Name and use the seven parts of a strong prompt. | Role; Task; Context; Constraints; Output format; Examples; Quality criteria | Build one prompt with all seven parts and label each one.",
    "Tell the model who it is, what to do and why. | Choosing a useful role; One clear task per prompt; Background the model cannot guess (audience, level, purpose) | Turn Write about farming into a prompt with a role, a task and context for a named reader.",
    "Control length, tone and structure. | Word limits and tone; Tables, bullet lists and JSON; Saying what to leave out | Request the same summary as a table, a JSON object and a 50-word paragraph.",
    "Show the model what good looks like. | One-shot and few-shot examples; A checklist the answer must meet; Examples that accidentally bias the answer | Add two examples and a three-point checklist to a prompt, then compare before and after.",
    "Treat prompts as drafts that get tested. | Run on several inputs; Spot failures; Change one thing at a time; Keep a prompt log | Test one prompt on five different inputs and record what broke.",
    "Practise on realistic tasks in a timed lab. | Pick a task (study plan, product description, customer reply); Three rounds of improvement; Peer review | Pairs swap prompts, run each other's, and give two specific improvements.",
    "Ship a small, reusable prompt tool. | Choose a real use case; Write a template with blanks; Document it with an example; Present it | Each student shows a template working on two different inputs."
  ],
  "animation": [
    "Understand motion and the core principles. | Persistence of vision and frame rate; Squash and stretch; Timing and spacing; Anticipation; Ease in and ease out | Animate a bouncing ball, 24 frames, on paper or in a free tool.",
    "Plan the film before animating. | Logline and short script; Character design sheet; Storyboard; Animatic | Write a 30-second story and storyboard it in 8 panels.",
    "Produce a short 2D clip. | Keyframes and in-betweens; Walk cycles; Layers and basic rigging | Animate a 2-second character walk cycle.",
    "Move through the 3D pipeline. | Modeling, rigging and skinning; Posing and the graph editor; Lighting and render basics | Pose and animate a simple object or character jumping.",
    "Use camera and sound to carry emotion. | Shot types and camera moves; Composition; Dialogue, music and effects; Mixing levels | Re-cut one scene with two camera choices and add sound to each.",
    "Use AI tools to speed up work while keeping control. | Idea and reference generation; AI for backgrounds, in-betweens and voice; Checking rights, quality and consistency | Use AI for one asset in the project and note what needed manual fixing.",
    "Finish and present work professionally. | Schedule and milestones; Export settings; Showreel; Portfolio page | Build a one-minute showreel from the course exercises.",
    "Deliver a finished short film. | Final script and animatic; Production; Picture and sound lock; Screening | Screen the short in class and collect feedback with a short rubric."
  ],
  "cloud-computing": [
    "Explain what cloud is and the main service models. | IaaS, PaaS and SaaS; Regions and availability zones; Pay-as-you-go pricing | Sort ten everyday apps into IaaS, PaaS or SaaS.",
    "Choose the right compute and storage. | Virtual machines, containers and serverless; Object, block and file storage | Launch a small VM or function and store a file in object storage.",
    "Build a basic cloud network. | VPCs and subnets; IP addressing; Security groups and firewalls; DNS and load balancers | Build a network with one public and one private subnet.",
    "Control who can do what. | Users, roles and least privilege; MFA; Encryption at rest and in transit | Create a read-only role and test what it can and cannot do.",
    "Use managed services instead of running everything yourself. | Managed databases; Queues and events; APIs and caching | Connect a small app to a managed database.",
    "Keep apps running and shippable. | CI/CD; Monitoring, logs and alerts; Backups, redundancy and recovery | Set up one alert and one automated deployment.",
    "Keep cost and risk under control. | Budgets and alerts; Tagging; Right-sizing; Policies and compliance | Estimate the monthly cost of a sample app and propose two savings.",
    "Deploy a real app with proper documentation. | Architecture diagram; Deployment; Monitoring; Cost estimate; README | Present the architecture and walk through a live demo."
  ],
  "web-development": [
    "Build the structure of a web page. | HTML structure and semantic tags; Links, images and forms; How browsers and servers talk | Build a one-page personal profile in plain HTML.",
    "Style pages that work on any screen. | Selectors and the box model; Flexbox and grid; Media queries and mobile-first; Contrast and focus states | Style the profile page and check it from 360px wide up to desktop.",
    "Make pages interactive. | Variables and functions; The DOM and events; Fetch and JSON | Add a to-do list that adds, completes and removes items.",
    "Know when and why to use modern tooling. | Components; Build tools and npm; What React and Vue solve | Rebuild one section as a reusable component.",
    "Understand what happens behind the page. | HTTP methods, routes and status codes; A simple server (Flask or Node); Validating requests | Create an API with two endpoints and call it from the page.",
    "Store data and check quality. | Database and SQL basics; Form validation; Testing and debugging; Performance and accessibility checks | Save the to-do items in a database and write one test.",
    "Share work and put it online. | Commits, branches and pull requests; Hosting; Domains and HTTPS; Environment variables and secrets | Push the project to GitHub and deploy it to a live URL.",
    "Build and launch a real website. | Plan, build, test, deploy; README and short case study | Present the live site, one decision and one bug you fixed."
  ],
  "app-development": [
    "Choose an app idea and the right approach. | Native versus cross-platform; App lifecycle; Users and problems | Write a one-page brief: user, problem and three core features.",
    "Design screens people can use. | Wireframes; Navigation patterns (tabs, stacks); Touch targets, spacing and readable text | Wireframe five screens and test them with a classmate.",
    "Learn the programming you need. | Variables, functions, lists and classes; State; Reading error messages | Build a counter or simple calculator screen.",
    "Connect the app to real data. | Calling an API; JSON; Local storage; Loading and error states | Show live data in a list with a loading state and an error state.",
    "Protect accounts and user data. | Sign-in flows; Storing tokens safely; Permissions; Privacy basics | Add email sign-in and protect one screen.",
    "Find problems before users do. | Manual test plans; Unit and widget tests; Real-device testing; Crash reporting | Write ten test cases and automate two.",
    "Release the app and keep improving it. | Icons and screenshots; Store listing; Signing and builds; Updates and feedback | Draft a store listing and a release checklist.",
    "Ship a working app. | Scoped MVP; Testing; Release candidate; Demo | Demo on a real phone and explain the code structure."
  ],
  "full-stack": [
    "See how the whole application fits together. | Front end, back end and database; Client-server flow; Project setup and tools | Draw the path of a login request from the click to the database and back.",
    "Build the user-facing side. | Component thinking; State; Forms; Accessibility; Calling an API | Build the main screen of a notes app.",
    "Build a clean, predictable API. | REST design; Routing; Validation; Error handling; Project structure | Implement create, read, update and delete endpoints.",
    "Model and query data. | Tables and relations; SQL queries; Migrations; Indexes and backups | Design a two-table schema and write three queries.",
    "Keep users and data safe. | Sessions or tokens; Code-based or password login; Authorization; Common attacks (injection, XSS, CSRF) | Add login and make one route owner-only.",
    "Work reliably as a team. | Unit and API tests; Git workflow; Code review; Documentation | Write three API tests and open a reviewed pull request.",
    "Run the app in the real world. | Environments and config; Hosting; CI/CD; Logs, monitoring and rollbacks | Deploy with an automated pipeline and trigger a test alert.",
    "Deliver a complete app from front end to database. | Scoped idea; Build; Tests; Deployment; README | Present it live and describe the architecture."
  ],
  "agentic-ai": [
    "Decide what an agent is and when to use one. | Chatbot versus workflow versus agent; The cost of autonomy; When not to use an agent | Classify five tasks as prompt, workflow or agent and defend each choice.",
    "Design prompts and pick models for agents. | System prompts; Structured outputs; Choosing a model by cost, speed and quality | Write a system prompt that returns validated JSON.",
    "Give agents tools they can use well. | Function calling; Clear tool descriptions; APIs, files and search; Handling tool errors | Give an agent two tools and observe how it chooses between them.",
    "Manage what the agent remembers. | Conversation history; Short-term versus long-term memory; Retrieval; What should never be stored | Add a simple memory and test that it recalls and forgets correctly.",
    "Plan and control multi-step work. | Breaking goals into steps; Loops and stop conditions; Multi-agent patterns; Human checkpoints | Build a plan-then-act loop with a step limit.",
    "Prove the agent works. | Test sets; Scoring; Tracing; Regression checks; Failure handling | Create ten test cases and score two versions of a prompt.",
    "Protect the agent and its users. | Prompt injection; Permissions; Secrets; Rate limits and cost caps; Approval for risky actions | Attack your own agent with an injection and add a guardrail.",
    "Ship a reliable agent with evaluation and guardrails. | Scope; Tools; Tests; Human approval; Demo | Demo the agent and show its evaluation results."
  ],
  "game-development": [
    "Design a game that is fun and finishable. | The core loop; Player goals and feedback; Scoping for beginners | Pitch a game in one sentence and draw its core loop.",
    "Get a character moving in an engine. | Engine tour (Unity, Godot or similar); Scenes and objects; Scripting basics; Input | Make a character move and jump.",
    "Add the systems that make it a game. | Collisions and physics; Health, score and enemies; State machines; Difficulty | Add an enemy, a hazard and a score.",
    "Build levels that teach and challenge. | Level design; Tilemaps or 3D blocking; Pacing; Camera | Build a short level with a clear start, challenge and goal.",
    "Make the game feel good. | Menus and HUD; Sound effects and music; Screen shake and particles | Add a menu, one sound and one visual effect.",
    "Test and tune the game. | Playtests; Bug tracking; Frame rate and memory; Balance | Run a playtest with three people and list the top fixes.",
    "Get the game to players. | Builds and platforms; Store pages and trailers; Publishing on itch.io; Feedback and updates | Export a build and publish a game page.",
    "Release a polished, playable game. | Scope; Build; Test; Publish; Postmortem | Present a trailer or live demo and a short postmortem."
  ]
}
