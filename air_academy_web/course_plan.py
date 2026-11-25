"""The full syllabus of every course: modules, and the order lessons appear on screen.

A whole number is a lesson that already existed: it keeps that number forever, so nobody's progress, quiz scores or certificates move.
A string is a NEW lesson. New lessons are numbered 9, 10, 11 ... in the order they are listed here (15 and 5 in the three animation tracks
carry on from 5 the same way), and a number is never reused or changed. Where a lesson sits on screen is only decided by this list.

Keep this file and the lessons_*_more.py files in step: the Nth new lesson listed for a course is lesson number (old count + N).
"""

PLAN = {
    "prompt-engineering": [
        ("Foundations", [1, 2, "How AI reads your words: tokens, context and limits", "Your first great prompt, step by step"]),
        ("Core techniques", [3, 4, "Tone, voice and audience", "Structured output: tables, JSON and checklists"]),
        ("Examples and reasoning", [5, "Few-shot prompting: teaching by example", "Step-by-step reasoning: breaking big tasks into parts", "Fixing wrong, vague or made-up answers"]),
        ("Testing and your toolkit", [6, "Building your own prompt library and templates", "Prompting for research, summaries and studying", "Prompting for writing, business and marketing"]),
        ("Prompting at work", ["Prompting for code, data and spreadsheets", "Prompts for images and video", "Safety, privacy and honesty with AI", 7]),
        ("Real projects", ["Prompt chains and simple automations", "Writing system prompts for assistants and apps", 8, "Capstone: your personal prompt toolkit"]),
    ],
    "animation": [
        ("Foundations", [1, "The 12 principles of animation in action", "Timing, spacing and weight", "Choosing your software and setting up your workspace"]),
        ("Story and pre-production", [2, "Writing a short animation script", "Character and world design", "Storyboards and animatics"]),
        ("2D animation", [3, "Walk cycles and character acting in 2D", "Backgrounds, layers and effects", "Lip-sync and facial animation"]),
        ("3D animation", [4, "Modeling and texturing a simple character", "Rigging and posing", "Lighting, camera and rendering in 3D"]),
        ("Camera, sound and AI", [5, "Music, voice and sound design", 6, "Using AI tools responsibly: ethics, rights and credit"]),
        ("Production and portfolio", [7, "Editing, colour and final export", "Showreel, portfolio and finding work", 8]),
    ],
    "cloud-computing": [
        ("Cloud basics", [1, "Cloud service models: IaaS, PaaS and SaaS", "AWS, Azure and Google Cloud compared", "Opening a free cloud account safely"]),
        ("Compute and storage", [2, "Virtual machines hands-on", "Object, block and file storage", "Containers and serverless functions"]),
        ("Networking", [3, "Virtual networks, subnets and routing", "Load balancers, DNS and CDNs", "Firewalls and network security"]),
        ("Identity, security and data", [4, "Encryption, keys and secrets", 5, "Managed databases, queues and APIs"]),
        ("DevOps and reliability", [6, "CI/CD pipelines for cloud apps", "Infrastructure as code", "Monitoring, logging and backups"]),
        ("Cost, design and portfolio", [7, "Cloud architecture patterns and design reviews", "Cloud careers and certification roadmap", 8]),
    ],
    "web-development": [
        ("Foundations", [1, "HTML structure and semantic tags", "Forms, tables, images and media", "Accessibility basics"]),
        ("CSS and responsive design", [2, "Flexbox and Grid layouts", "Transitions, animation and modern CSS", "Mini project: a responsive landing page"]),
        ("JavaScript", [3, "Functions, arrays and objects", "The DOM and events", "Fetching data from APIs"]),
        ("Modern front-end", [4, "Components and thinking in state", "Building a small app with a modern framework", "Performance and SEO basics"]),
        ("Backend, data and quality", [5, 6, "Forms, validation and user accounts", "Testing and debugging websites"]),
        ("Git, launch and portfolio", [7, "Domains, hosting and HTTPS", "Web security basics", 8]),
    ],
    "app-development": [
        ("Foundations", [1, "Native, cross-platform and web apps: choosing your path", "Setting up your tools and your first running app", "Planning an app: idea, users and features"]),
        ("UI/UX", [2, "Wireframes and clickable prototypes", "Lists, forms and common screen patterns", "Responsive layouts and dark mode"]),
        ("Programming", [3, "Variables, logic and functions in practice", "Managing app state", "Device features: camera, location and notifications"]),
        ("Data and APIs", [4, "Local storage and working offline", "Connecting your app to a backend", "In-app purchases and payments"]),
        ("Security and quality", [5, "Protecting user data and privacy", 6, "Debugging, crashes and performance"]),
        ("Release and portfolio", [7, "App store listings, screenshots and review rules", "Updates, analytics and user feedback", 8]),
    ],
    "full-stack": [
        ("Foundations", [1, "How the web works: requests, servers and the full journey", "Choosing a stack and setting up your project", "Planning an application: requirements and data flow"]),
        ("Front-end", [2, "Components, routing and state", "Forms, validation and error handling", "Connecting the front end to an API"]),
        ("Backend", [3, "Designing a REST API", "Middleware, validation and error handling on the server", "Background jobs, email and file uploads"]),
        ("Databases", [4, "SQL in depth: joins, indexes and transactions", "Schema design and migrations", "Caching and performance"]),
        ("Security, testing and teamwork", [5, "Sessions, tokens and roles", 6, "Git workflows, code review and teamwork"]),
        ("Deployment and portfolio", [7, "Containers, environments and configuration", "Monitoring, logging and scaling", 8]),
    ],
    "agentic-ai": [
        ("Foundations", [1, "Chatbots, workflows and agents: what is the difference", "How large language models work, for builders", "Setting up your environment and making your first model call"]),
        ("Prompt and model design", [2, "System prompts and agent personas", "Structured outputs and schema validation", "Choosing models: cost, speed and quality"]),
        ("Tools and integrations", [3, "Writing good tool definitions", "Connecting to APIs, files and databases", "Connectors and the Model Context Protocol"]),
        ("Memory and planning", [4, "Retrieval and knowledge bases (RAG)", 5, "Multi-agent systems and handoffs"]),
        ("Reliability and safety", [6, "Building test sets and measuring agent quality", "Human approval checkpoints and guardrails", "Handling errors, retries and runaway loops"]),
        ("Security, launch and portfolio", [7, "Prompt injection and safe tool use", "Logging, monitoring and cost control for agents", 8]),
    ],
    "game-development": [
        ("Game design", [1, "Game loops, rules and player goals", "Writing a one-page game design document", "Choosing a game engine and creating your first project"]),
        ("Engine and programming", [2, "Player movement and input", "Collisions, physics and triggers", "Game state, saving and loading"]),
        ("Gameplay systems", [3, "Enemies and simple AI", "Health, scoring, inventory and progression", "Balancing difficulty and game feel"]),
        ("World and levels", [4, "Level design principles and flow", "2D art, sprites and animation for games", "Cameras, lighting and atmosphere"]),
        ("UI, audio and testing", [5, "Sound effects and music in your game", 6, "Bug hunting and playtesting with real players"]),
        ("Publishing and portfolio", [7, "Store pages, trailers and marketing your game", "Making money from games and staying legal", 8]),
    ],
    "2d-animation": [
        ("Core motion", [1, "Setting up free 2D animation software", 2, "The bouncing ball and the feeling of weight", 3]),
        ("Characters and acting", ["Arcs, overlap and secondary action", 4, "Run cycles and jumps", "Facial expressions and simple lip-sync", "Acting: showing emotion through movement"]),
        ("Scenes and finishing", ["Backgrounds, layers and camera moves", "Effects: smoke, water, fire and impact", 5, "Polishing, feedback and fixing common mistakes", "Final project: a 10-second animated scene"]),
    ],
    "3d-animation": [
        ("Modeling and looks", [1, "Installing Blender and setting up your first project", "Modeling a simple character, step by step", "UV unwrapping and texturing", 2]),
        ("Rigging and animating", [3, "Inverse kinematics and control rigs", 4, "Bouncing ball and body mechanics in 3D", "Facial rigs and expressions"]),
        ("Walk cycles, render and finish", [5, "Acting and performance shots", "Camera moves, lighting and render settings for polish", "Compositing, sound and exporting", "Final project: a rendered 3D character shot"]),
    ],
    "ai-animation": [
        ("Story", [1, "Choosing and testing AI tools: what each one is good at", "Story structure: hook, conflict and ending", "Writing dialogue and narration with AI", 2]),
        ("Characters and sound", [3, "Designing a character sheet and style guide", "Backgrounds, props and consistent settings", 4, "Music, sound effects and mixing audio"]),
        ("Motion and film", ["Animating images: image-to-video and motion tools", "Shot planning, editing and colour", 5, "Ethics, copyright and crediting AI work", "Final project: release your AI short film"]),
    ],
}


def build(base_titles, plan):
    """From a course's existing titles and its plan: (all titles by lesson number, display order of lesson numbers, modules [(name, [numbers])])."""
    titles, order, modules = list(base_titles), [], []
    for name, items in plan:
        ns = []
        for it in items:
            if isinstance(it, int):
                if not 1 <= it <= len(base_titles):
                    raise ValueError(f"plan names lesson {it}, which does not exist")
                n = it
            else:
                titles.append(it)
                n = len(titles)
            ns.append(n)
            order.append(n)
        modules.append((name, ns))
    if sorted(order) != list(range(1, len(titles) + 1)):
        raise ValueError("every lesson must appear in the plan exactly once")
    return titles, order, modules
