"""Cloud Computing Masterclass: deep lesson pages 1 to 8.
Same format as lessons_prompt_engineering.py: hook, sections, diagram, terms, mistakes, quiz. Quiz "a" = index of the right option.
Provider names are used as examples only. Prices and free tiers change, so lessons tell students to check the provider's own pricing page."""
from diagrams import flow, compare, timeline, bars, grid, stack, cycle, rings, responsibility, network

LESSONS = {
    1: dict(
        minutes=14,
        hook="In many Nigerian homes there are two ways to get light. You can buy a generator, fuel it, repair it and listen to it all night. Or you can use the grid and pay for the power you use. Cloud computing is the second idea applied to computers. Instead of buying servers, housing them, cooling them and replacing them when they break, you rent computing power from a provider's huge data centres over the internet and pay for what you use. This lesson explains what that means, the three main ways to rent, and why it changes how software is built.",
        sections=[
            ("What the cloud really is", """“The cloud” is not a mysterious place. It is **someone else's computers**, in large buildings called **data centres**, that you reach over the internet. A provider such as Amazon Web Services (AWS), Microsoft Azure or Google Cloud owns the machines. You rent a slice of them in minutes, use it, and stop paying when you switch it off.

Three ideas make it different from owning your own server:

- **On demand:** you start a computer in minutes, not weeks.
- **Pay-as-you-go:** you pay for usage, not for a machine that sits idle.
- **Scalable:** you can add more power when many users arrive and remove it afterwards.

Think of a wedding caterer who hires extra pots and chairs for one big day, instead of buying 500 chairs and storing them all year."""),
            ("IaaS, PaaS and SaaS: how much do you manage?", """Cloud services come in three main levels. The difference is how much work stays with you.

- **IaaS (Infrastructure as a Service):** you rent raw computers, storage and networks, and you set up everything on top. Like renting an empty kitchen: you bring the cooks and the recipes.
- **PaaS (Platform as a Service):** you bring your code, and the provider runs the servers, the operating system and the runtime. Like a catering kitchen with equipment ready: you only cook.
- **SaaS (Software as a Service):** you use finished software in your browser, such as Gmail or Google Docs. Like ordering a meal: you only eat.

The picture above shows who manages each layer. As you move from left to right, you give up control but gain speed and less maintenance. Neither is better. A start-up often picks PaaS to move fast, and a bank may pick IaaS to control every detail."""),
            ("Regions and availability zones", """A provider's computers are spread around the world in **regions**, which are geographic areas such as “Frankfurt” or “Johannesburg”. Each region has several **availability zones (AZs)**, which are separate data centres a short distance apart with their own power and cooling.

Why it matters:

- **Distance means delay.** The farther your users are from the region, the slower the app feels. This delay is called **latency**.
- **Spreading across zones means safety.** If one data centre has a fire or a power failure, a copy in another zone keeps running.
- **Laws about data.** Some information must stay inside certain countries. Check the rules before choosing a region.

Providers keep adding regions, and the nearest one to Nigeria changes over time, so always check the provider's current list of regions before you choose."""),
            ("Pay-as-you-go: the good and the careful", """Paying only for what you use can save a lot of money. A small company that needs a powerful server for two hours a week pays for two hours, not for a whole month. But the same model has risks:

- **Forgotten resources keep charging.** A virtual machine you left on over the weekend still costs money.
- **Bills are usually in US dollars.** If the naira weakens, your bill grows even if your usage does not. Check how your card is charged.
- **Some things cost extra.** Moving data out of the cloud, called egress, and some network features can add charges that surprise beginners.

Two habits protect you from day one: set a **budget alert**, and **delete what you no longer use**. You will practise both in lesson 7."""),
            ("The shared responsibility idea", """Security in the cloud is split between you and the provider. The provider protects the physical buildings, the hardware and the core services. **You** are responsible for what you put in the cloud: who can sign in, how your data is configured and which services are open to the internet.

Many famous data leaks happened not because a provider was hacked, but because a customer left a storage folder open to everyone. When something goes wrong because of your settings, it is your problem. Always ask: “Which part is mine?”"""),
        ],
        diagram=responsibility(), caption="The further right you go, the more the provider runs for you, and the less you control.",
        terms=[("Cloud computing", "Renting computing power over the internet and paying for what you use."), ("Data centre", "A large building full of servers, power and cooling that a provider runs."), ("IaaS, PaaS, SaaS", "Three service levels: rent infrastructure, rent a platform, or use finished software."),
               ("Region", "A geographic area where a provider has data centres."), ("Availability zone", "One separate data centre inside a region."), ("Latency", "The delay between a user's action and the response."), ("Shared responsibility", "The split of security duties between the provider and the customer.")],
        mistakes=["Thinking the cloud is automatically safe and needs no care from you.", "Leaving test resources running and paying for them for weeks.", "Choosing a region far from your users and then wondering why the app is slow.", "Not checking how a dollar bill will be charged to your card or account."],
        quiz=[dict(q="Which service level gives you the most control?", o=["SaaS", "PaaS", "IaaS", "None of them"], a=2, why="With IaaS you manage the operating system and everything above it, so you control the most."),
              dict(q="You use Google Docs in your browser. Which model is this?", o=["IaaS", "SaaS", "PaaS", "A private data centre"], a=1, why="Finished software used through a browser is SaaS."),
              dict(q="Why spread an app across availability zones?", o=["To make it cheaper to start", "To make it faster to code", "To keep it running if one data centre fails", "To hide it from users"], a=2, why="Zones have separate power and cooling, so a failure in one does not stop the others."),
              dict(q="A storage folder is accidentally left open to everyone. Whose responsibility is it?", o=["The customer who set it up", "The electricity company", "The internet provider", "Nobody"], a=0, why="Under shared responsibility, the customer controls their own settings and data access.")],
    ),
    2: dict(
        minutes=14,
        hook="When you need to move goods from Lagos to Ibadan you can buy a truck, hire a driver with a truck, or book space on a bus that already makes the trip. Each choice trades control, cost and effort. Cloud compute has the same three choices, and storage has its own three kinds of containers. This lesson helps you pick the right one for the job instead of always choosing the biggest and most expensive.",
        sections=[
            ("Virtual machines: a full computer for rent", """A **virtual machine (VM)** is a complete computer, with its own operating system, that runs inside a real server. You choose the size (how many CPUs and how much memory) and the operating system, then connect and install what you like.

- **Good for:** software that needs full control, old applications, and anything that must look like a normal server.
- **Cost:** you pay while it is running, even when it is idle.
- **Work for you:** you update the operating system, install security patches and manage the software.

A VM is the most flexible choice, and the one that needs the most care."""),
            ("Containers: a packed lunchbox for your app", """A **container** packages your application with everything it needs, its libraries and settings, into one sealed unit. Containers share the host's operating system, so they are much smaller and faster to start than VMs. A tool called **Docker** is the most common way to build them.

Why teams love containers: the app runs the same on your laptop, a test server and the cloud. “It works on my machine” stops being an excuse.

When you run many containers, a system called an **orchestrator**, such as Kubernetes, starts them, restarts them if they crash and adds more when traffic grows. For small projects, a managed service that runs your container for you is much simpler than running Kubernetes yourself."""),
            ("Serverless: pay only when code runs", """In **serverless**, you upload a small function. The provider runs it only when something triggers it, such as a web request, a new file or a timer, and you pay only for the time it runs. There are still servers, but you never see or manage them.

- **Good for:** short tasks, unpredictable traffic, and glue between services. For example: “when a photo is uploaded, make a thumbnail.”
- **Watch out for:** a **cold start**, the small delay when a function that has not run recently starts again, and for time limits on how long one run may last.

A simple rule for choosing:

> [Rule of thumb]
> Need full control or special software? Use a VM.
> Want your app to run the same everywhere? Use a container.
> Have short, event-driven jobs? Use serverless."""),
            ("Three kinds of storage", """Cloud storage is not one thing. Match the type to the job:

- **Object storage:** files stored as objects with a name, reached by a web address. Excellent for photos, videos, backups and website files. It is cheap and nearly unlimited. Amazon S3 is the best-known example.
- **Block storage:** a virtual hard disk that attaches to one VM. Fast, and best for operating systems and databases.
- **File storage:** a shared folder many computers can open at the same time, for example documents that several servers need.

Two more ideas: **storage classes** let you move rarely used files to cheaper, slower storage, and **durability** (will the data survive?) is different from **availability** (can I reach it right now?). Always keep a **backup** in a separate place, because deleting a file by mistake deletes it everywhere."""),
        ],
        diagram=flow([("VIRTUAL MACHINE", "Full computer|You manage most"), ("CONTAINER", "Packed app|Shares the OS"), ("SERVERLESS", "Just a function|Provider manages")], "c2", "More control on the left. Less work on the right"),
        caption="Pick the lightest option that still does the job.",
        terms=[("Virtual machine", "A complete computer, with its own operating system, running inside a real server."), ("Container", "A sealed package with an app and everything it needs, sharing the host's operating system."), ("Serverless", "Running small functions on demand, with the provider managing all servers."),
               ("Cold start", "The small delay when a function that has not run recently starts again."), ("Object storage", "Storage for files kept as named objects and reached by web address."), ("Block storage", "A virtual disk attached to a machine."), ("Durability", "How unlikely stored data is to be lost.")],
        mistakes=["Choosing a big VM for a job a small function could do.", "Leaving a VM on all weekend with nobody using it.", "Keeping the only copy of important files in one place.", "Putting user uploads on a VM's disk instead of object storage."],
        quiz=[dict(q="Which is best for storing user-uploaded photos cheaply?", o=["Block storage", "Object storage", "RAM", "A serverless function"], a=1, why="Object storage is cheap, huge and built for files like photos and videos."),
              dict(q="What does a container give you?", o=["A full second computer inside your laptop", "A bigger screen for your server", "An app packed with what it needs, so it runs the same anywhere", "Free storage for all your files"], a=2, why="Containers package an app with its dependencies so it behaves the same on every machine."),
              dict(q="What is a cold start?", o=["A frozen disk that cannot be read", "A delay when a rarely used function starts up", "A cooling problem in the data centre", "A type of backup that runs at night"], a=1, why="A function that has not run recently may take a moment longer to start."),
              dict(q="When does serverless fit best?", o=["Always-on heavy software", "Old apps needing full control", "A game server running 24 hours", "Short jobs triggered by events"], a=3, why="Serverless runs small tasks on demand, so you pay only when they run.")],
    ),
    3: dict(
        minutes=15,
        hook="Picture a big compound in Lagos. There is a gate to the street, a front shop that anyone can walk into, and back rooms where the accounts and the safe are kept. Visitors never wander into the back rooms, and the people inside leave through one controlled door. A cloud network is built the same way. You build your own private compound inside the provider's data centre and decide what is open to the public and what is hidden. This lesson teaches the layout, and the rules that guard each door.",
        sections=[
            ("VPC and subnets: your private compound", """A **VPC (Virtual Private Cloud)** is your own private network in the cloud. Nobody else can use it. Inside it you carve out smaller parts called **subnets**.

- **Public subnet:** things that must be reachable from the internet, such as a load balancer or a web server.
- **Private subnet:** things that must stay hidden, such as databases and internal services. They have no public address.

The golden rule: **put only what must be public in a public subnet**, and keep everything else private. A database should almost never be reachable straight from the internet."""),
            ("IP addresses and CIDR", """Every device on a network has an **IP address**, such as 10.0.1.25. When you create a VPC you give it a range of addresses written in **CIDR notation**, for example 10.0.0.0/16. The number after the slash says how many addresses you get: the **smaller** the number, the **bigger** the range.

- 10.0.0.0/16 gives about 65,000 addresses for the whole VPC.
- 10.0.1.0/24 gives 256 addresses for one subnet.

You do not need to calculate in your head. You need to know that subnets are slices of the VPC range, and that ranges must not overlap with each other or with your office network if you plan to connect them later."""),
            ("Routing and the gates", """**Route tables** are the road signs of a network. They say where traffic for each destination should go.

- An **internet gateway** is the door between your VPC and the internet. A subnet whose route table points to it is public.
- A **NAT gateway** lets machines in a private subnet reach out to the internet, for example to download updates, without letting the internet reach in. It is a one-way door.

Look at the picture: users reach the load balancer in the public subnet. The load balancer passes requests to the app server in the private subnet, which talks to the database. The app server can fetch updates through the NAT gateway, but nobody outside can start a connection to it."""),
            ("Firewalls, DNS and load balancers", """Three more tools finish the picture:

- **Security groups** are firewalls attached to a resource. They list which traffic is allowed in and out, for example “allow web traffic on port 443 from anywhere” and “allow database traffic only from the app server”. By default, everything not allowed is blocked.
- **DNS** turns a name like myshop.ng into an IP address. Cloud DNS services also route users to the nearest or healthiest copy of your app.
- **A load balancer** shares incoming requests among several servers, and stops sending traffic to a server that is unhealthy. It is what lets you add servers without users noticing.

A common beginner mistake is opening a port to “anywhere” (0.0.0.0/0) just to make something work. Open only what you need, and only to who needs it."""),
        ],
        diagram=network(), caption="Only the load balancer faces the internet. The app and the database stay in the private subnet.",
        terms=[("VPC", "Your own private network inside the cloud."), ("Subnet", "A smaller section of a VPC, public or private."), ("CIDR", "A way of writing an address range, such as 10.0.0.0/16."), ("Internet gateway", "The door between a VPC and the internet."),
               ("NAT gateway", "A one-way door that lets private machines reach out to the internet."), ("Security group", "A firewall that lists which traffic may reach a resource."), ("Load balancer", "A service that spreads requests across several servers.")],
        mistakes=["Putting the database in a public subnet with a public address.", "Opening every port to the whole internet to “make it work”.", "Choosing overlapping address ranges and failing to connect networks later.", "Forgetting that private servers also need a route out for updates."],
        quiz=[dict(q="Where should a database normally live?", o=["In a public subnet", "In a private subnet", "On the load balancer", "Outside the VPC"], a=1, why="A database should not be reachable from the internet, so it belongs in a private subnet."),
              dict(q="What does a NAT gateway do?", o=["Lets private machines reach out without being reachable", "Makes a subnet public to the internet", "Encrypts the database at rest", "Stores backups in another region"], a=0, why="NAT allows outbound connections only, like a one-way door."),
              dict(q="Which is bigger: 10.0.0.0/16 or 10.0.1.0/24?", o=["10.0.1.0/24", "They are the same", "10.0.0.0/16", "You cannot compare them"], a=2, why="A smaller number after the slash means a bigger range. /16 has far more addresses than /24."),
              dict(q="What is a security group?", o=["A team of cloud security engineers", "A kind of cheap storage service", "A table of routes between subnets", "A firewall that controls which traffic is allowed in"], a=3, why="Security groups list the allowed traffic in and out, and block the rest.")],
    ),
    4: dict(
        minutes=15,
        hook="Imagine the manager of a bank. Does the manager give every staff member the key to the vault? No. The cashier gets the till, the guard gets the front door, and only two people can open the vault together. Giving each person only the access they need is called least privilege, and it is the heart of cloud security. In the cloud a single leaked password can empty an account and send you a huge bill, so this is the lesson that protects everything else you build.",
        sections=[
            ("Identity and access management (IAM)", """**IAM** is the system that decides **who** can do **what** on **which** resource. It has four main parts:

- **User:** a person or program with its own sign-in.
- **Group:** a collection of users with the same job, so you manage permissions once.
- **Role:** a set of permissions that someone or something can temporarily take on, for example a server that needs to read from storage.
- **Policy:** a written rule that allows or denies actions on resources.

Here is a small policy in the style used by AWS. It allows reading files from one storage bucket and nothing else:

> [JSON]
> {
>   "Effect": "Allow",
>   "Action": ["s3:GetObject"],
>   "Resource": "arn:aws:s3:::my-school-files/*"
> }

Read it as: allow (Effect) the action “get object” (Action) on the files in my-school-files (Resource). Other providers use different words for the same ideas."""),
            ("Least privilege in practice", """**Least privilege** means giving every person and program the smallest set of permissions that still lets them do their job. Start with nothing and add only what is needed. Never start with “admin for everyone” and plan to tighten it later, because later never comes.

Good habits:

- Create a separate user for each person. **Never share one login.**
- Give programs **roles**, not permanent passwords.
- Review permissions regularly and remove those nobody uses.
- Test a new role by trying to do something it should **not** be able to do. If it succeeds, the role is too wide."""),
            ("Protect the account itself", """The most powerful login in any cloud account is the **root account**, the one created when you sign up. Protect it like the key to the whole bank:

1. Turn on **multi-factor authentication (MFA)**. A password plus a code from your phone or a security key. This single step blocks most account takeovers.
2. Use the root account only for the few tasks that need it, then create normal users for daily work.
3. Never put **access keys** or passwords in your code, in a chat or on GitHub. Bots scan public code for keys within minutes and use them to start expensive computers.
4. Turn on activity logs, so you can see who did what and when."""),
            ("Encryption: locking the data", """**Encryption** scrambles data so that only someone with the right key can read it. You need it in two situations:

- **At rest:** when data is stored on a disk or in a bucket. Most cloud services can encrypt it for you with one setting.
- **In transit:** when data travels over the network. Use HTTPS, which means the connection is encrypted, for every website and API.

Keys must be guarded too. Cloud providers offer key-management services that store and rotate keys safely. If you keep the key next to the locked data, the lock does nothing. Finally, remember that in Nigeria the Nigeria Data Protection Act 2023 expects organisations to protect personal data, and encryption and access control are basic ways to do so."""),
        ],
        diagram=rings(["Account and MFA", "Network and firewalls", "Identity and permissions (IAM)", "Application", "Your data, encrypted"], note="Each layer protects the one inside it"),
        caption="Security works in layers. If one layer fails, the next one still stands.",
        terms=[("IAM", "The system that controls who can do what on which resource."), ("Role", "A set of permissions that a person or program can temporarily take on."), ("Policy", "A written rule that allows or denies actions."), ("Least privilege", "Giving only the permissions that are needed for the job."),
               ("MFA", "Signing in with a password plus a second proof, such as a code from your phone."), ("Encryption", "Scrambling data so only someone with the key can read it."), ("Access key", "A secret used by programs to sign in to a cloud account.")],
        mistakes=["Using the root account for everyday work.", "Sharing one login between several people.", "Committing access keys to a public GitHub repository.", "Giving a program full admin rights when it only needs to read one folder."],
        quiz=[dict(q="What does least privilege mean?", o=["Give only the permissions needed for the job", "Give everyone admin rights", "Use the cheapest cloud plan", "Share one login for simplicity"], a=0, why="Start with nothing and grant only what is needed, so mistakes and attacks do less damage."),
              dict(q="Which single step blocks most account takeovers?", o=["A longer username", "Turning on multi-factor authentication", "Choosing a faraway region", "Using more storage"], a=1, why="Even if a password leaks, the attacker also needs the second factor."),
              dict(q="Where must you never put access keys?", o=["In a password manager", "In an environment variable on a server", "In public code on GitHub", "In a secrets service"], a=2, why="Bots scan public code for keys within minutes and use them to run up costs."),
              dict(q="What does encryption in transit protect?", o=["Backups on a shelf", "Files in an office", "The colour of a website", "Data travelling across the network"], a=3, why="Encryption in transit, such as HTTPS, stops people on the network from reading the data.")],
    ),
    5: dict(
        minutes=14,
        hook="A restaurant could grow its own vegetables, raise its own chickens and build its own cooking gas supply. Most do not. They buy vegetables from the market, order gas from a supplier and spend their energy on cooking. Cloud providers offer the same bargain for software. Databases, message queues, caches and API gateways all come as ready-made, managed services. You use them, the provider runs them. This lesson shows what each does and when to reach for it.",
        sections=[
            ("Managed databases", """A **managed database** is a database that the provider installs, backs up, updates and keeps running for you. You choose the type and size, and connect from your app. Two big families exist:

- **Relational (SQL):** data in tables with rows and columns, linked by keys. Good when your data has clear structure and relations, such as customers, orders and payments. Examples: PostgreSQL and MySQL services.
- **NoSQL:** flexible stores for documents, key-value pairs or very large, fast-changing data. Good for things like sessions, shopping carts or activity feeds.

If you are not sure, start with relational. It is easier to reason about, and it fits most business apps. Managed services also offer **automatic backups** and **multi-zone copies**, which would take you days to build yourself."""),
            ("Queues and events: do not make users wait", """Imagine a user uploads a video. Making three sizes of it takes a minute. Should the user wait? No. The app puts a **message** in a **queue**: “process video 123”. A separate **worker** picks messages from the queue and does the work in the background.

Why this is powerful:

- **The user is not kept waiting.** The app replies at once.
- **Spikes are absorbed.** If 1,000 uploads arrive together, they wait in the queue instead of crashing the server.
- **Parts are decoupled.** The app and the worker do not need to know each other, so one can fail or be updated without stopping the other.

An **event** or **publish/subscribe** service is similar: something happens, such as “order paid”, and several services that care about it each receive a copy."""),
            ("APIs and caching", """An **API gateway** is a front door for your backend. It receives every request, checks who is calling, limits how often they can call, and forwards the request to the right service. It means each service does not have to rebuild those checks.

A **cache** stores answers that are asked for again and again, in very fast memory, so the database is not asked every time. For example, a product page viewed 10,000 times a day does not need 10,000 database queries. The trade-off is that cached data can become **stale**, an old copy, so you give each item an expiry time. Redis is a very popular cache."""),
            ("Putting the pieces together", """A typical flow for an online shop looks like this: the user's request goes through the API gateway, the app checks the cache, then reads or writes the database. When an order is placed, a message goes into a queue and workers send the email, update stock and print the invoice.

When choosing a managed service, ask four questions:

1. What does it cost at my expected usage, and at ten times that usage?
2. How do I back it up and recover it?
3. How hard would it be to move to another provider? This is called **vendor lock-in**.
4. Can I secure it properly, with private access, encryption and logs?"""),
        ],
        diagram=flow([("USER", "Sends a|request"), ("API GATEWAY", "Checks and|routes"), ("QUEUE", "Holds jobs|until ready"), ("WORKER", "Does the|slow work"), ("DATABASE", "Stores the|result")], "c5", "A cache sits beside the database and answers repeat questions fast"),
        caption="Managed services turn big jobs into small, replaceable parts.",
        terms=[("Managed service", "A service the provider installs, updates and keeps running for you."), ("Relational database", "A database of linked tables, queried with SQL."), ("Queue", "A waiting line of jobs for workers to pick up."), ("Worker", "A program that takes jobs from a queue and does them."),
               ("API gateway", "A front door that checks and routes requests to your services."), ("Cache", "Fast storage that keeps answers to repeated questions."), ("Vendor lock-in", "Being so tied to one provider's services that moving is hard.")],
        mistakes=["Making users wait for slow jobs instead of using a queue.", "Caching data with no expiry, so users see old information.", "Running your own database server when a managed one would do.", "Never asking what a service will cost at ten times today's traffic."],
        quiz=[dict(q="Why put slow work in a queue?", o=["Queues make every app free to run", "The user is not kept waiting, and spikes are absorbed", "Queues delete errors automatically", "Workers never fail when they use queues"], a=1, why="The app replies at once and workers handle the jobs at their own pace."),
              dict(q="What is a cache for?", o=["Storing backups safely for many years", "Encrypting passwords for user sign-in", "Keeping fast copies of answers that are asked often", "Sending emails to every customer"], a=2, why="A cache avoids repeating the same slow work."),
              dict(q="Which database family stores data in tables linked by keys?", o=["Relational (SQL)", "Key-value", "Object storage", "File storage"], a=0, why="Relational databases use tables, rows, columns and keys to link records."),
              dict(q="What is vendor lock-in?", o=["A security feature of firewalls", "A type of network firewall rule", "A pricing plan with a discount", "Being so tied to one provider that moving is hard"], a=3, why="The more you use one provider's special services, the harder it is to leave.")],
    ),
    6: dict(
        minutes=15,
        hook="A bakery that bakes well on a good day is not impressive. A bakery that has fresh bread every morning for ten years, whether or not the generator fails, whether or not the baker is sick, is. That is reliability, and in software it is built, not hoped for. This lesson covers the practices that let a team ship changes often without breaking things, notice problems before customers do and recover quickly when something does fail.",
        sections=[
            ("CI/CD: ship small changes safely", """**Continuous Integration (CI)** means every time a developer pushes code, an automatic system builds the project and runs the tests. **Continuous Delivery or Deployment (CD)** means that once the tests pass, the change is released automatically, or at the push of a button.

Why it works:

- **Small changes** are easy to understand and easy to undo.
- **Automatic checks** catch mistakes in minutes, not weeks.
- **A repeatable process** means releases do not depend on one person remembering twelve steps.

A simple pipeline: push code, build, run tests, deploy to a test environment, then deploy to the live one. If any step fails, the pipeline stops and tells you."""),
            ("Infrastructure as code", """Clicking buttons in a web console to build servers is fine for learning, but it is hard to repeat and easy to forget. **Infrastructure as code (IaC)** means you describe your servers, networks and permissions in text files, with tools such as Terraform or the provider's own templates. You can then:

- **Recreate** the whole system in minutes.
- **Review** changes like any other code.
- **Keep history** of who changed what.

It turns “nobody remembers how this server was set up” into a file in a repository."""),
            ("Monitoring: logs, metrics and alerts", """You cannot fix what you cannot see. Cloud monitoring has three parts:

- **Metrics:** numbers over time, such as CPU use, response time and error rate.
- **Logs:** a written record of what happened, with times and details.
- **Alerts:** a message sent to a person when a metric crosses a limit.

Good alerts are **actionable**. “Error rate above 5 percent for 5 minutes” is useful. An alert that fires fifty times a day teaches the team to ignore alerts, and then the one real problem is missed. Set a few that matter, and write down what to do when each one fires."""),
            ("Reliability numbers and recovery", """Reliability is measured. When a provider promises **99.9 percent availability**, that allows about 8.8 hours of downtime in a year. At **99.99 percent** it is about 53 minutes a year. Each extra “9” costs much more to achieve, so ask what your users really need.

Two numbers guide your recovery plan:

- **RTO (recovery time objective):** how long can we be down before it hurts badly?
- **RPO (recovery point objective):** how much recent data can we afford to lose?

If your RPO is one hour, you need backups at least every hour. Then practise: a backup you have never restored is only a hope. Run a restore test, and keep copies in a second zone or region."""),
        ],
        diagram=cycle([("PLAN", "What to build"), ("CODE", "Small changes"), ("BUILD + TEST", "Automatic"), ("DEPLOY", "Release safely"), ("MONITOR", "Watch and alert")], "c6", center="DevOps loop|learn from every release"),
        caption="DevOps is a loop. What you learn from monitoring feeds the next plan.",
        terms=[("CI/CD", "Automatically building, testing and releasing every change."), ("Infrastructure as code", "Describing servers and networks in files that tools can run."), ("Metric", "A number measured over time, such as response time."), ("Log", "A written record of events in a system."),
               ("Alert", "An automatic message sent when something crosses a limit."), ("RTO", "How long a system may be down before it causes serious harm."), ("RPO", "How much recent data you can afford to lose.")],
        mistakes=["Releasing big batches of changes once a month.", "Setting so many alerts that the team ignores them.", "Keeping backups but never testing a restore.", "Building servers by hand and never writing down the steps."],
        quiz=[dict(q="What does CI mean?", o=["Cloud Internet service provider", "Constant Inspection of the servers", "Continuous Integration: testing every push", "Customer Information about usage"], a=2, why="CI runs automatic builds and tests on every change to catch mistakes early."),
              dict(q="What makes a good alert?", o=["It fires every minute, day and night", "It is actionable and rare enough to be taken seriously", "It has a funny name that people remember", "It only fires on Sunday mornings"], a=1, why="Alerts that fire constantly get ignored. Useful ones point to a real problem and a clear action."),
              dict(q="Roughly how much downtime per year does 99.9 percent allow?", o=["About 8.8 hours", "None", "About 9 days", "About 5 minutes"], a=0, why="0.1 percent of a year is about 8.8 hours."),
              dict(q="What is RPO?", o=["How fast a page loads for the user", "The price of a monthly plan", "A type of backup file format", "How much recent data you can afford to lose"], a=3, why="If RPO is one hour, you must be able to restore data that is no more than one hour old.")],
    ),
    7: dict(
        minutes=14,
        hook="Many young Nigerian developers have a story: a free trial, a forgotten server, and a surprise bill in dollars that arrives when the naira is weak. It does not have to happen to you. Cloud money is a skill like any other, and the habits are simple: know what you are paying for, set limits that warn you, tag things so you can find them, and switch off what you do not use. This lesson also covers the rules that govern what you may store and where.",
        sections=[
            ("Where cloud money goes", """Most bills come from five areas:

- **Compute:** servers and functions, usually the biggest part.
- **Storage:** disks and buckets, billed by size and sometimes by access.
- **Databases:** managed databases are often the second-biggest item.
- **Data transfer:** moving data **out** of the provider, or between regions, is usually charged. Moving data in is often free.
- **Forgotten things:** unattached disks, old snapshots, idle load balancers and test servers that nobody switched off.

Look at the picture. In this made-up app, forgotten resources cost almost as much as the storage and transfer together. Those are the easiest savings."""),
            ("Budgets and alerts: your safety net", """The first thing to do in a new account, before building anything, is to create a **budget** with **alerts**. For example: warn me by email at 50, 80 and 100 percent of 20 dollars a month. Providers have a built-in budget tool for this. Also:

- Check how your card will be charged. A card that fails a payment can leave you with a suspended account.
- Remember that prices are normally in US dollars. Exchange rate changes affect your cost in naira.
- Read each service's pricing page before you use it. Free tiers have limits and time periods, and they change, so check the provider's current terms rather than relying on an old blog post."""),
            ("Tags and right-sizing", """**Tags** are labels you attach to resources, such as project=school-app and owner=ada. They let you filter your bill by project, find who created something and delete everything for a finished project. Decide the tag names early and use them on everything.

**Right-sizing** means matching the size of a resource to what it really uses. Check the metrics: if a server's CPU is at 5 percent all month, it is too big. Move to the next size down and watch. Other common savings:

- **Schedule shutdowns** for test machines at night and at weekends.
- **Commit to usage** with reserved or savings plans for steady workloads, which gives a discount for a longer promise.
- **Use cheaper storage classes** for files you rarely open.
- **Delete** what is no longer needed."""),
            ("Governance and compliance", """**Governance** means the rules that keep a growing cloud account under control: who may create what, which regions are allowed, and which settings are forbidden. Providers let you write these as **policies**, for example “nobody may create a public storage bucket”.

**Compliance** means following laws and standards. In Nigeria, the **Nigeria Data Protection Act 2023** sets rules for handling personal data, and some industries have extra rules, such as for banks and health records. Ask three questions about any data you store: **Is it personal? Who may see it? Where is it stored?** If you handle other people's data, learn the law that applies to you before you build, not after."""),
        ],
        diagram=bars([("Compute", 60), ("Database", 45), ("Data transfer", 25), ("Storage", 15), ("Forgotten resources", 30, "#FFB86B")], note="A sample monthly bill in US dollars (made-up numbers)", unit=" $"),
        caption="Forgotten resources are often the easiest savings.",
        terms=[("Budget", "A spending limit you set in the cloud account, with alerts."), ("Egress", "Data moving out of a provider's network, which is usually charged."), ("Tag", "A label attached to a resource to track project, owner or cost."), ("Right-sizing", "Matching a resource's size to what it really uses."),
               ("Governance", "Rules that control who may do what in a cloud account."), ("Compliance", "Following laws and standards about how you handle data.")],
        mistakes=["Building first and setting up a budget alert never.", "Leaving test servers and old disks running after a project ends.", "Assuming a free tier lasts forever with no limits.", "Storing personal data without knowing which law applies."],
        quiz=[dict(q="What should you set up first in a new cloud account?", o=["A budget with alerts", "A giant database", "Ten servers", "A public bucket"], a=0, why="Alerts warn you before costs grow out of control."),
              dict(q="A server's CPU sits at 5 percent all month. What is the best action?", o=["Make it bigger to be safe", "Move it to a smaller size and watch", "Ignore it and leave it as it is", "Add a second server beside it"], a=1, why="That is right-sizing: matching size to real use to cut cost."),
              dict(q="Which data movement is usually charged?", o=["Moving data into the cloud", "Reading your own bill", "Creating a tag", "Moving data out of the provider"], a=3, why="Egress, data leaving the provider, normally costs money."),
              dict(q="Why use tags?", o=["To make servers run much faster", "To find, group and track the cost of resources", "To encrypt data when it is stored", "To remove firewalls from a network"], a=1, why="Tags let you see which project or person a cost belongs to, and clean up quickly.")],
    ),
    8: dict(
        minutes=15,
        hook="A builder shows a client the finished house and the plans: the structure, the wiring, the safety checks and the cost. A cloud engineer does the same with an architecture diagram, a running app, a security note and a cost estimate. Your portfolio project is where you prove you can do the full job, not just talk about it. This lesson is your brief, with a clear checklist and a way to present it that impresses a teacher, a client or an employer.",
        sections=[
            ("The brief", """Deploy a **real application** to the cloud, securely and cheaply, and document it. The application can be small: a simple website, a notes app, or a to-do app with a database. What matters is that you deliver the six items below.

- **Deployed app** with a public link that works.
- **Architecture diagram** showing every part and how they connect.
- **Security setup:** a limited-permission user (not root), MFA on, and nothing public that should not be.
- **Monitoring:** at least one alert that you have tested.
- **Cost estimate and budget alert:** what it costs per month and what you did to keep it low.
- **README** that lets someone else understand and rebuild the project."""),
            ("Draw an architecture diagram", """A clear diagram answers four questions: **What are the parts? How do they connect? What is public? What is private?**

Use simple boxes and arrows, and label each arrow with what travels on it. Show the user, the entry point (such as a load balancer or a static site), the app, the database and storage. Draw a line around the private part of the network. Add a short note for each box: what it is, why you chose it and the rough monthly cost.

Free tools like diagrams.net work well. A neat hand drawing, photographed clearly, is also fine. Clarity beats beauty."""),
            ("Write a README people will read", """A good **README** is short and structured:

1. **What it is:** one paragraph on the app and who it is for.
2. **Architecture:** your diagram and the key choices, with reasons.
3. **How to deploy it:** numbered steps someone else can follow.
4. **Security:** permissions, MFA, encryption and what is private.
5. **Monitoring and alerts:** what you watch and what to do when an alert fires.
6. **Cost:** monthly estimate and your budget alert.
7. **Recovery plan:** what to do if the app goes down, and how to restore from backup.
8. **Clean-up:** how to delete everything so no cost remains."""),
            ("Demo, clean-up and grading", """Prepare a five-minute demo: show the diagram for one minute, the live app for two, the monitoring and alert for one, and the cost and lessons learned for one. Be ready to explain **one decision** and **one thing that went wrong** and how you fixed it. Teachers value honesty about mistakes more than a perfect story.

When the course is finished, **delete the resources** you no longer need, so the bill stops. Keep the diagram, screenshots and README for your portfolio. You will be marked on whether the project meets the brief, the quality of the build, testing, documentation and your presentation."""),
        ],
        diagram=grid([("Deployed app", "A public link|that works"), ("Architecture", "A clear diagram"), ("Security", "Least privilege|and MFA"), ("Monitoring", "One tested alert"), ("Cost", "Estimate and|budget alert"), ("README", "Deploy, recover,|clean up")], 3, note="Six deliverables, all required"),
        caption="A cloud project is more than a running app. It is the app, the proof and the plan.",
        terms=[("Architecture diagram", "A drawing of the parts of a system and how they connect."), ("README", "A document that explains a project and how to run it."), ("Recovery plan", "Steps to restore a system after a failure."), ("Clean-up", "Deleting resources you no longer need so costs stop."),
               ("Demo", "A short live walk-through of your finished project.")],
        mistakes=["Delivering a running app with no diagram, README or cost estimate.", "Using the root account for the whole project.", "Forgetting to delete resources after the demo.", "Presenting only successes and skipping what went wrong."],
        quiz=[dict(q="Which is NOT one of the six deliverables?", o=["A deployed app with a public link", "An architecture diagram", "A cost estimate", "A paid advertising campaign"], a=3, why="The six items are app, diagram, security, monitoring, cost and README."),
              dict(q="What should an architecture diagram show?", o=["The parts, how they connect, what is public", "Only the logo of your school", "The names of your classmates", "The colour palette of the app"], a=0, why="A diagram must answer what the parts are, how they connect and what is exposed."),
              dict(q="Why delete resources after the project?", o=["To lose the diagram", "To make the demo longer", "So that costs stop", "Because the grader asks for it"], a=2, why="Running resources keep charging until you delete them."),
              dict(q="What do teachers value about problems you faced?", o=["They prefer that you hide every problem", "Honest explanation of what went wrong and the fix", "Long excuses about why it failed", "A list of people to blame for it"], a=1, why="Debugging and honesty show real understanding.")],
    ),
}