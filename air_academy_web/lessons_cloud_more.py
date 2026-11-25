"""Cloud Computing Masterclass: lessons 9 to 24, added when the course grew into a full course (course_plan.py says where each one sits on screen).
Same format as lessons_cloud.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option.
Prices, free plans, regions and exam fees change often, so every lesson that mentions them tells the learner to check the provider's current page."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[9] = dict(   # Cloud service models: IaaS, PaaS and SaaS
    minutes=14,
    hook="Suppose you want to serve pizza. You could build a kitchen, buy ovens and hire cooks. You could rent a fully equipped kitchen and bring your own recipes. You could use a delivery kitchen that bakes to your menu. Or you could simply order from a restaurant. In each case, someone else does more of the work, and you keep less control. Cloud computing offers exactly these choices for software, and the names are IaaS, PaaS and SaaS. You have met the three terms. In this lesson you will use them as a practical decision tool, learn the newer models in between, understand how deployment choices such as public, private and hybrid fit in, and learn how to decide who should run what.",
    sections=[
        ("The stack of things someone must run", """Every application sits on a stack of layers, and **someone** must look after each one:

1. **Your data and settings.**
2. **The application code.**
3. **The runtime** (Python, Node, the web server).
4. **The operating system** (Linux or Windows, with its updates).
5. **Virtualisation** (the software that shares one physical machine among many customers).
6. **Servers, storage and networking hardware,** and the building, power and cooling.

In your own office server room, you do all six. In the cloud, the provider takes over layers from the bottom up, and the service model tells you **where the line is** between what they run and what you run."""),
        ("IaaS, PaaS and SaaS as a dividing line", """Each model moves the line higher:

- **IaaS (Infrastructure as a Service):** the provider runs layers 5 and 6. You get a virtual machine, a disk and a network, and you manage the operating system, the runtime, the app and the data. Examples: Amazon EC2, Azure Virtual Machines, Google Compute Engine. **Most control, most work.**
- **PaaS (Platform as a Service):** the provider also runs the operating system and runtime. You deploy your code and data. Examples: Azure App Service, Google App Engine, AWS Elastic Beanstalk, and platforms such as Render. **Faster to launch, less control.**
- **SaaS (Software as a Service):** the provider runs everything. You only configure and use it. Examples: Gmail, Microsoft 365, Zoho, Paystack's dashboard. **Least work, least control.**

A useful question for any system is: **“What would I have to fix at 3 a.m. if it broke?”** That is the part you run."""),
        ("The models in between", """The real world has more than three boxes:

- **CaaS (Containers as a Service):** you provide a container image and the provider runs it, for example AWS Fargate, Google Cloud Run or Azure Container Apps.
- **FaaS (Functions as a Service, serverless):** you provide small functions and the provider runs them when an event happens, such as AWS Lambda. You pay for the time they run.
- **DBaaS (Database as a Service):** a managed database, with backups and patching handled for you, such as Amazon RDS or Supabase.
- **Managed AI and data services:** speech, vision, search and analytics offered as ready-to-call interfaces.

These sit between IaaS and SaaS. The trend is clear: providers offer more and more **managed services,** so teams can spend their time on the product instead of the plumbing."""),
        ("Deployment models: where the cloud lives", """The service model says **what** you rent. The deployment model says **where** it runs:

- **Public cloud:** shared data centres owned by a provider such as AWS, Azure or Google Cloud, with your resources logically separated from others.
- **Private cloud:** cloud-style technology running only for one organisation, in its own or a rented data centre. Often chosen for strict control or regulation.
- **Hybrid cloud:** a mix, such as keeping sensitive records in a private system while using the public cloud for websites and bursts of demand.
- **Multi-cloud:** using more than one public provider. It can reduce dependence on one vendor, but it adds complexity and cost, so beginners should usually **start with one.**

Nigeria has data centres in Lagos and elsewhere that offer colocation and local cloud services, which some organisations use for latency or data-location reasons."""),
        ("Choosing and migrating", """Match the model to your situation:

- **Small team, standard web app:** choose PaaS, containers or serverless first. Less to maintain.
- **Special software, custom networking or full control needed:** IaaS.
- **A common business need** (email, accounting, CRM): buy SaaS instead of building.
- **Strict data rules:** check where data is stored and what the law requires, including the **NDPA 2023** for personal data.

When moving an existing system, there are broad routes. **Lift and shift** moves it as it is, which is quick but gains little. **Refactor** changes it to use managed services, which takes longer and gives more benefit. **Replace** swaps it for SaaS. The cloud is **not always cheaper or better:** a steady, predictable workload on hardware you already own, or an app with unusual hardware needs, may stay on premises. Decide with numbers and requirements."""),
    ],
    diagram=grid([("ON PREMISES", "You run all six layers,|building to app"), ("IaaS", "You run OS, runtime,|app and data"), ("PaaS", "You run the app|and its data"), ("SaaS", "You configure it|and use it")], cols=2,
                 note="The higher the service, the less you run and control."),
    caption="From your own server room to IaaS, PaaS and SaaS: the line of what you run moves up while control goes down.",
    terms=[("IaaS", "Renting basic computing, storage and network, and managing everything above them yourself."), ("PaaS", "Renting a platform where you deploy code and the provider runs the system underneath."),
           ("SaaS", "Using finished software that the provider runs completely."), ("FaaS", "Serverless functions that run only when an event triggers them."),
           ("Hybrid cloud", "A mix of private systems and public cloud."), ("Lift and shift", "Moving an existing system to the cloud with few changes.")],
    mistakes=["Choosing IaaS by habit when a managed service would save months of work.", "Moving to multi-cloud before mastering one provider.", "Assuming the cloud is always cheaper.", "Forgetting that you still run everything above the provider's line."],
    quiz=[dict(q="In IaaS, what do you usually manage?", o=["The operating system, runtime, app and data", "Only your settings", "The data centre building", "The cables"], a=0,
               why="IaaS gives you machines and network. Everything above that is yours."),
          dict(q="Which is an example of SaaS?", o=["A virtual machine", "A container image", "Gmail", "A bare disk"], a=2,
               why="SaaS is finished software that the provider runs end to end."),
          dict(q="What is hybrid cloud?", o=["A cloud in the sky", "A mix of private systems and public cloud", "Only one public cloud", "A type of laptop"], a=1,
               why="Hybrid combines private and public environments."),
          dict(q="Which question helps you see what you run?", o=["What colour is the logo?", "How old is the provider?", "How many pages is the contract?", "What would I have to fix at 3 a.m. if it broke?"], a=3,
               why="Whatever you would have to repair is the part you manage.")],
    activity="Take a system you know, such as a shop website with email and a database. For each part, write whether it should be IaaS, PaaS, serverless or SaaS, and who would fix it at 3 a.m. in each case.",
)

LESSONS[10] = dict(   # AWS, Azure and Google Cloud compared
    minutes=14,
    hook="Three companies, Amazon, Microsoft and Google, run most of the world's public cloud, and beginners often waste weeks asking which one is best. The honest answer is that they are all excellent, they offer almost the same building blocks under different names, and the concepts you learn on one carry over to the others within days. What differs is where each is strongest, how its pricing and tools feel, and which one your future employer or customers use. In this lesson you will learn the translation between their names, their real strengths, how the market looks, other providers worth knowing, and a calm way to choose.",
    sections=[
        ("The big three at a glance", """In broad terms:

- **Amazon Web Services (AWS)** is the oldest and largest, with the widest range of services and a huge community. Many tutorials, jobs and tools assume AWS.
- **Microsoft Azure** is very strong in organisations that already use Microsoft products such as Windows Server, Microsoft 365 and Active Directory (now Microsoft Entra ID). It is popular with enterprises and governments.
- **Google Cloud (GCP)** is known for data analytics, machine learning, Kubernetes (which Google created) and clean developer tools.

Market shares move over time, but AWS, Azure and Google Cloud together serve the large majority of public cloud customers. Which is "best" depends on your workload, skills and customers, not on a ranking."""),
        ("A translation table", """The same idea has different names. Learn the concept once, then look up the name:

> [Names]
> Virtual machine       AWS EC2            Azure Virtual Machines     Compute Engine
> Object storage        AWS S3             Azure Blob Storage         Cloud Storage
> Serverless function   AWS Lambda         Azure Functions            Cloud Run functions
> Containers (managed)  ECS and Fargate    Container Apps             Cloud Run
> Kubernetes            EKS                AKS                        GKE
> Managed SQL           RDS and Aurora     Azure SQL                  Cloud SQL
> Identity and access   IAM                Entra ID and RBAC          Cloud IAM
> CDN                   CloudFront         Front Door                 Cloud CDN
> Monitoring            CloudWatch         Azure Monitor              Cloud Monitoring

Names and products change, so treat this as a map and not a promise. Each provider's documentation has a page that compares its services with the others."""),
        ("How they feel different", """Beyond the names, there are differences in style:

- **Breadth versus focus:** AWS has the largest catalogue, which can feel overwhelming. Google Cloud's is smaller and often simpler to start with.
- **Console and tools:** each has a web console and a command line (`aws`, `az`, `gcloud`). Try all three, as personal preference matters.
- **Pricing:** all use pay as you go, with discounts for commitments. Prices, free plans and credits change often, so compare **your own workload** with each provider's calculator.
- **Identity and enterprise integration:** Azure's link to Microsoft sign-in is a major reason companies choose it.
- **Regions near you:** as far as is known at the time of writing, the closest major regions for Nigeria are in South Africa (AWS Cape Town, Azure Johannesburg, Google Cloud Johannesburg). Check each provider's current region list, because new ones are announced.
- **Support and training:** all offer free learning paths, and communities exist in Lagos and online."""),
        ("Other providers worth knowing", """The big three are not the only choices, and for small projects they may not be the best:

- **Developer-friendly platforms:** Render, Railway, Fly.io, Vercel and Netlify let you deploy an app with very little setup, and are popular for startups and portfolios.
- **Simple cloud providers:** DigitalOcean, Linode (Akamai), Hetzner and Vultr offer straightforward virtual servers with predictable prices.
- **Cloudflare:** a global network with a CDN, security, DNS and a growing set of developer services.
- **Local and regional providers:** companies with data centres in Nigeria and Africa can offer lower latency, local support and help with data-location rules.

Using a simpler provider for a small shop's website, and learning a big cloud for your career, is a perfectly sensible plan."""),
        ("How to choose and what to avoid", """Use a short decision process:

1. **Job market and customers:** look at job adverts in your target market and ask which cloud your clients use. AWS has the most listings in many places, and Azure dominates some enterprise sectors.
2. **Your existing skills:** a Microsoft shop will find Azure natural.
3. **Workload:** heavy data and machine learning may lean to Google Cloud, Windows and .NET to Azure, general web and anything else to AWS.
4. **Cost and credits:** compare using the calculators and check start-up and student programmes.
5. **Pick one and go deep.** Concepts such as networking, identity, storage and monitoring transfer easily.

Avoid **multi-cloud too early,** avoid choosing by hype, and avoid **lock-in surprises** by understanding how hard it would be to leave. Write down why you chose, and review it after your first real project."""),
    ],
    diagram=grid([("COMPUTE", "EC2, Azure VMs,|Compute Engine"), ("OBJECT STORAGE", "S3, Blob Storage,|Cloud Storage"), ("SERVERLESS", "Lambda, Functions,|Cloud Run functions"), ("MANAGED SQL", "RDS, Azure SQL,|Cloud SQL"), ("KUBERNETES", "EKS, AKS, GKE"), ("MONITORING", "CloudWatch, Monitor,|Cloud Monitoring")], cols=3,
                 note="Same ideas, different names."),
    caption="AWS, Azure and Google Cloud offer the same building blocks under different names. Learn the idea, then the name.",
    terms=[("AWS", "Amazon Web Services, the largest public cloud with the widest range of services."), ("Azure", "Microsoft's cloud, strong with enterprises and Microsoft products."),
           ("Google Cloud", "Google's cloud, known for data, machine learning and Kubernetes."), ("Region", "A geographic area where a provider runs data centres."),
           ("CLI", "A command line tool for controlling a cloud, such as aws, az or gcloud."), ("Lock-in", "Being so tied to one provider that switching is difficult and costly.")],
    mistakes=["Spending weeks debating which cloud is best instead of learning one.", "Going multi-cloud as a beginner.", "Comparing prices from old blog posts instead of current calculators.", "Ignoring where your customers' data must be stored."],
    quiz=[dict(q="Which provider is especially popular in organisations that already use Microsoft products?", o=["Azure", "AWS only", "None", "Google Cloud only"], a=0,
               why="Azure integrates closely with Windows, Microsoft 365 and Entra ID."),
          dict(q="What is the AWS name for object storage?", o=["Lambda", "EC2", "S3", "RDS"], a=2,
               why="Amazon S3 is AWS's object storage service."),
          dict(q="What transfers easily between clouds?", o=["The names of services", "The concepts, such as networking, identity and storage", "The prices", "The console buttons"], a=1,
               why="Concepts are shared. Names and screens differ."),
          dict(q="What is a sensible approach for a beginner?", o=["Use all three clouds at once", "Pick one cloud and learn it well", "Avoid clouds", "Wait for a perfect one"], a=1,
               why="Depth in one provider builds skills that carry over to others.")],
    activity="Choose three services you know (a virtual machine, object storage and a managed database) and find their names in all three clouds. Then look at ten job adverts in your target market and count which cloud is requested most.",
)

LESSONS[11] = dict(   # Opening a free cloud account safely
    minutes=15,
    hook="Every year, beginners open a cloud account, follow a tutorial, forget to switch something off, and find a bill of hundreds of dollars a month later. Others reuse a weak password, skip two-factor login and discover that someone has started mining cryptocurrency on their account. Almost all of this is preventable with about an hour of careful setup. In this lesson you will open an account the right way: choosing a plan, protecting the most powerful login, creating a safe everyday user, setting budgets and alarms before you build anything, and forming the cleanup habits that keep practice free. Never share your card details with anyone, and never paste them anywhere except the provider's own secure sign-up page.",
    sections=[
        ("Choose your free option and read the small print", """All three big providers have ways to learn without paying much, but the offers **change often**, so read the current pages:

- **Free plans and credits:** new accounts may receive credits to spend for a limited time, or a free plan with limits.
- **Always-free tiers:** some services stay free up to a small monthly allowance, such as a limited number of function calls.
- **Time-limited free tiers:** some resources are free only for the first 12 months, and then are billed.
- **Student programmes:** the GitHub Student Developer Pack and provider education offers can add credits for students.

Before you begin, find out: **how long does the offer last, which services does it cover, and what happens when it ends?** Some accounts continue to bill your card when credits run out. Write the end date in your calendar."""),
        ("Preparing and paying safely", """Prepare before you sign up:

1. **Use a dedicated email address** that only you can access, with its own strong password and two-factor login. This email can reset everything, so protect it.
2. **Use a payment method the provider accepts.** Most require a card that is enabled for international online payments, and may make a small temporary verification charge. Some Nigerian bank cards need international transactions switched on, and some people use a virtual dollar card from a licensed provider. Check the provider's rules and your bank's terms.
3. **Enter card details only on the provider's own secure website.** Never send card numbers, expiry dates, CVV codes or PINs to anyone, and ignore anybody offering to “set up a free account” for a fee.
4. **Use a spending cap if your card offers one,** such as a virtual card funded with a small amount.
5. **Use your real details,** since fake information can get an account locked."""),
        ("Lock down the root account", """The first login creates the most powerful identity, often called the **root user** (AWS) or the **global administrator** (Azure) or the **owner** (Google Cloud). Whoever holds it can do anything and spend anything. So:

1. Set a **long, unique password** in a password manager.
2. Turn on **multi-factor authentication (MFA)** at once, using an authenticator app or a security key, not just SMS if you can avoid it.
3. **Do not create access keys** for the root user.
4. **Do not use it for daily work.** Log in with it only for rare account tasks, such as billing changes.
5. Save the **recovery codes** somewhere safe and offline.
6. Add an **alternative contact** and keep the account email current.

A stolen root login is the worst case, and MFA stops the large majority of takeovers."""),
        ("Create a safe everyday user and set budgets", """Next, create an identity for daily work, with only the permissions you need:

1. In **IAM** (or Identity Center, or Entra ID), create an **administrator user or role** for yourself, protected by MFA. For learning, broad permissions are acceptable, but for anything real, use **least privilege.**
2. Sign out of root, and **sign in as this user** from now on.

Now the step that protects your wallet. **Before building anything,** open **Billing and Cost Management** and:

- Create a **budget** of a small amount, such as 5 US dollars, with email alerts at 50%, 80% and 100%.
- Turn on **free tier usage alerts** and **cost anomaly detection** if available.
- Check the **billing dashboard** daily during your first weeks.

Budgets send **alerts,** they do not always stop spending, so you must still act when an alert arrives."""),
        ("Habits that keep practice free", """Good habits matter more than any single setting:

- **Tag** everything you create (`project=learning`) so you can find and delete it.
- **Pick one region,** preferably the same each time, so resources do not hide elsewhere.
- **Delete after each lab:** stop and **terminate** virtual machines, delete disks, snapshots, load balancers, NAT gateways, databases and unused public IP addresses. Stopped machines can still cost money for their disks.
- **Keep a cleanup checklist** and a **weekly review** of the resources list in every region you used.
- **Never put access keys in code or GitHub.** Bots find leaked keys within minutes and can run up huge bills.
- **Be careful with services that cost by the hour,** such as NAT gateways, load balancers, and large databases.
- **Watch for scams:** only follow instructions from the provider's official site.

If a surprise bill happens, contact the provider's support quickly. Many will help new customers with genuine mistakes, but it is not guaranteed."""),
    ],
    diagram=timeline([("Own email", "strong password"), ("Sign up", "official site only"), ("Protect root", "MFA, no access keys"), ("Daily user", "admin user with MFA"), ("Budget alerts", "before building"), ("Clean up", "delete after labs")],
                     note="Six steps before your first real lab."),
    caption="Use a dedicated email, create the account, protect root with MFA, make a daily user, set budget alerts, then practise and clean up.",
    terms=[("Root user", "The all-powerful first identity of a cloud account, to be used rarely."), ("MFA", "Multi-factor authentication: a second proof of identity such as an authenticator app code."),
           ("Budget alert", "A notification sent when spending reaches a limit you set."), ("Access key", "A long-term credential for programs, which must never be put in code."),
           ("Tag", "A label attached to a resource so you can find and manage it."), ("Free tier", "A limited amount of service offered at no charge, often for a limited time.")],
    mistakes=["Using the root account for daily work.", "Skipping MFA on the root account.", "Building before setting any budget alert.", "Leaving resources running after the lab."],
    quiz=[dict(q="What should you set up before building anything?", o=["A logo", "A budget with alerts", "A giant database", "A video"], a=1,
               why="Budget alerts warn you before costs grow."),
          dict(q="Why avoid using the root user daily?", o=["It is slow", "It has unlimited power, so a theft would be disastrous", "It costs more", "It is forbidden to log in"], a=1,
               why="The root identity is the most powerful and the most attractive target."),
          dict(q="What should you do with card details?", o=["Enter them only on the provider's own secure page, never send them to others", "Send them to a friend who sets it up", "Post them in a group", "Write them in code"], a=0,
               why="Card data belongs only on the provider's secure sign-up page."),
          dict(q="Which resources can keep costing money even when a virtual machine is stopped?", o=["Nothing", "Attached disks and snapshots", "The keyboard", "The browser"], a=1,
               why="Storage and some network items are billed even when compute is off.")],
    activity="Open a free account on one provider, turn on MFA for the root user, create an everyday admin user, set a 5 dollar budget with three alerts, and write your own cleanup checklist before you start any lab.",
)

LESSONS[12] = dict(   # Virtual machines hands-on
    minutes=16,
    hook="Reading about virtual machines is not the same as having one. In the next twenty minutes you will rent a real Linux computer in a data centre, connect to it from your own laptop, install a web server and see a page appear at its public address. It is the cloud's most basic trick, and doing it once removes the mystery forever. You will also learn what it costs, how to secure it and, most important, how to switch it off properly. The screens and button names differ between providers and change over time, so the steps below use AWS EC2 as the example and focus on the ideas that apply everywhere.",
    sections=[
        ("Plan the machine", """Before clicking, decide five things:

1. **Image (operating system):** Ubuntu Server LTS is a friendly, widely documented choice.
2. **Size (instance type):** for practice, the smallest general-purpose size that is marked free-plan eligible, such as `t3.micro` or the one the console recommends. Small machines have little CPU and memory, but are enough to learn.
3. **Region:** choose one, and use the same region for every lab.
4. **Storage:** the default root disk of 8 to 30 GB is fine.
5. **Access:** a **key pair** (a private key file you keep, and a public key the server holds) for logging in, instead of a password.

Also think about **cost:** a running small machine is billed for each hour, plus its disk and any public IP address. Free plans and credits change, so check the current terms."""),
        ("Launch it and lock it down", """In the console, choose **Launch instance** and fill in:

- **Name and tags:** `lab-web-1`, `project=learning`.
- **Image:** Ubuntu Server LTS.
- **Instance type:** the small, free-eligible one.
- **Key pair:** create a new one, **download the `.pem` file once** and store it safely. It cannot be downloaded again.
- **Network and firewall (security group):** allow **SSH (port 22) only from your own IP address** (choose “My IP”), and **HTTP (port 80)** from anywhere, so people can see the page. **Never open port 22 to 0.0.0.0/0** (the whole internet): bots scan for it constantly.
- **Storage:** keep the default.

Click **Launch.** After a minute the instance shows **Running** and has a **public IP address** (or a public DNS name)."""),
        ("Connect and install a web server", """From your laptop's terminal (PowerShell works on Windows 10 and 11):

> [Terminal]
> # keep the key private (macOS and Linux)
> chmod 400 lab-key.pem
>
> ssh -i lab-key.pem ubuntu@YOUR_PUBLIC_IP
>
> # now on the server
> sudo apt update
> sudo apt install -y nginx
> systemctl status nginx
> echo "Hello from my first cloud server" | sudo tee /var/www/html/index.html

Open `http://YOUR_PUBLIC_IP` in your browser. You should see your message. If you do not, check, in order: the instance is **running**, the security group allows **port 80**, `nginx` is **active**, and you used **http**, not https. On Windows, if SSH complains about key permissions, restrict the file's access to your user. When in doubt, read the exact error, because it usually names the problem."""),
        ("Keep it healthy and safe", """A server on the internet needs ongoing care:

- **Update regularly:** `sudo apt update && sudo apt upgrade`. Unpatched software is a main cause of break-ins.
- **Use SSH keys only,** and keep password login disabled. Do not share the private key.
- **Do not run applications as root.** Create a normal user for your app.
- **Open only the ports you need,** and restrict administration to your IP or to a managed access service such as AWS Systems Manager Session Manager or a VPN.
- **Use HTTPS** with a free certificate (Let's Encrypt) before putting a real site on it.
- **Monitor** basic health: CPU, disk space, and failed login attempts in `/var/log/auth.log`.
- **Take snapshots** of the disk before risky changes, so you can roll back.
- **Never store secrets** in files on the server without protection.

A public IP address receives attack attempts within minutes. This is normal, and it is why the basics matter."""),
        ("Stop, terminate and understand the bill", """Learn the difference, because it affects your bill:

- **Stop:** the machine is switched off. You stop paying for compute, but **you still pay for its disk** (and for an unattached static IP). The public IP address often changes when it restarts.
- **Terminate (delete):** the machine and, by default, its root disk are removed. **This stops the charges** but destroys your data unless you took a snapshot.
- **Snapshot or image:** a saved copy of the disk. It is cheap, and lets you create a new identical machine later.

When your lab is finished: **terminate the instance, delete any extra volumes and snapshots you no longer need, release unused IP addresses, and delete the key pair if you will not use it.** Then check the billing page the next day. Practise this routine every time.

> [Habit]
> Start lab -> work -> snapshot if needed -> terminate -> check billing tomorrow."""),
    ],
    diagram=flow([("Choose", "Ubuntu, small|size"), ("Protect", "key pair,|my IP only"), ("Launch", "wait for Running"), ("Connect", "ssh and install|nginx"), ("Clean up", "terminate and|check the bill")], "cl12",
                 note="Every lab ends with clean-up."),
    caption="Choose the image and size, protect access, launch, connect and install, then terminate to stop the charges.",
    terms=[("Instance", "A running virtual machine in the cloud."), ("Key pair", "A private key you keep and a public key the server holds, used instead of a password."),
           ("Security group", "A virtual firewall that controls which traffic may reach a machine."), ("SSH", "A secure way to log in to a remote computer from a terminal."),
           ("Snapshot", "A saved copy of a disk at a moment in time."), ("Terminate", "Delete a machine, which stops its charges and usually removes its disk.")],
    mistakes=["Opening SSH to the whole internet.", "Losing the key file, which cannot be downloaded again.", "Stopping the machine and forgetting that the disk is still billed.", "Running everything as root and never applying updates."],
    quiz=[dict(q="Which source should be allowed to connect over SSH?", o=["The whole internet", "Only your own IP address", "Nobody and everybody", "A random address"], a=1,
               why="Restricting SSH to your IP shuts out most automated attacks."),
          dict(q="What happens to the bill when you only stop a machine?", o=["Everything stops", "You still pay for the disk and some network items", "It doubles", "It becomes free forever"], a=1,
               why="Storage and static IPs are billed even if compute is off."),
          dict(q="Which action actually ends the charges for the machine and disk?", o=["Closing the browser", "Stopping it", "Terminating it and deleting extra volumes and snapshots", "Renaming it"], a=2,
               why="Terminate removes the instance, and you must also remove leftovers."),
          dict(q="What is a snapshot useful for?", o=["Saving a copy of the disk so you can recover or clone", "Taking a photo", "Opening ports", "Hiding costs"], a=0,
               why="Snapshots let you roll back or create a new machine from a saved state.")],
    activity="Launch a small Ubuntu machine, restrict SSH to your IP, install nginx and serve your own page. Take a snapshot, terminate everything, and check the next day that no resources and no charges remain.",
)

LESSONS[13] = dict(   # Object, block and file storage
    minutes=15,
    hook="A school keeps its records in three very different ways. There is a huge archive room where every box has a label and you ask the clerk for box 4821. There is the hard drive inside the principal's computer, fast and private to that one machine. And there is the shared folder that every teacher can open at once. Cloud storage comes in the same three shapes, called object, block and file storage, and choosing the wrong one is a common and costly mistake. In this lesson you will learn what each is, what each is good at, how to use object storage safely for uploads and backups, and how storage is priced, including the charges that surprise people.",
    sections=[
        ("Three shapes of storage", """Each shape stores data differently:

- **Object storage** (Amazon S3, Azure Blob Storage, Google Cloud Storage): files are stored as **objects** in a flat container called a **bucket**, each with a **key** (name) and metadata, and reached over the web (HTTP). Almost unlimited, very durable and cheap. You cannot edit part of an object in place. You replace the whole object.
- **Block storage** (Amazon EBS, Azure Managed Disks, Google Persistent Disk): a **virtual hard disk** attached to one virtual machine. Fast, with low delay. It holds the operating system and databases.
- **File storage** (Amazon EFS and FSx, Azure Files, Google Filestore): a **shared network folder** that many machines can open at the same time, using standard file protocols.

A short rule: **objects for files at scale, blocks for a machine's disk, files for a shared folder.**"""),
        ("Working with object storage", """Object storage is the workhorse of the cloud: user uploads, images, videos, backups, logs, website files and data lakes. A few commands with the AWS CLI show the idea:

> [Terminal]
> aws s3 mb s3://yaba-bakes-uploads-example --region af-south-1
> aws s3 cp receipt.pdf s3://yaba-bakes-uploads-example/receipts/2026/receipt.pdf
> aws s3 ls s3://yaba-bakes-uploads-example/receipts/
> aws s3 presign s3://yaba-bakes-uploads-example/receipts/2026/receipt.pdf --expires-in 600

Bucket names must be **globally unique.** Keys that contain slashes look like folders, but the storage is flat. The **presign** command makes a **temporary link** that lets someone download one private file for ten minutes without logging in. This is the safe way to share private files, rather than making the bucket public."""),
        ("Keeping buckets safe", """Misconfigured buckets have caused some of the largest data leaks in history. Follow these rules:

1. **Block public access** at the account and bucket level unless you are deliberately hosting a public website, and even then serve it through a CDN.
2. **Use IAM policies** that give each application access to **only its own bucket or folder**, and only the actions it needs.
3. **Turn on encryption** (usually on by default now) and use HTTPS only.
4. **Turn on versioning** so an overwritten or deleted object can be recovered, and consider **object lock** for important records.
5. **Enable access logging** and alerts for unusual activity.
6. **Check uploads:** do not trust file names, limit size and type, and scan if needed.
7. **Never put secrets or personal data** in file names, because names appear in logs.

Regularly review which buckets are public. Cloud tools can warn you automatically."""),
        ("Storage classes and lifecycle rules", """Not all data is used equally, and cloud providers price accordingly:

- **Hot (standard):** frequently accessed, highest storage price, lowest access price.
- **Cool or infrequent access:** cheaper to store, with a charge for retrieval and a minimum storage time.
- **Archive (Glacier and similar):** very cheap to store, but retrieval takes minutes to hours and costs extra. Good for old backups and records you must keep.

A **lifecycle rule** moves data automatically: for example, move logs to cool storage after 30 days, archive them after 180 days, and delete them after two years. This can cut costs sharply with no effort once set. Always check the current minimum storage durations and retrieval fees, because moving data too early or too often can cost more, not less."""),
        ("Choosing, protecting and paying", """To choose quickly:

> [Guide]
> User uploads, images, backups, static files   -> Object storage
> A database or the operating system disk       -> Block storage
> Several servers sharing the same files        -> File storage

**Durability** (how unlikely data is to be lost) is very high for object storage, but it is **not a backup** against your own mistakes or attacks. Use versioning, copies in another region and the **3-2-1 rule:** three copies, on two kinds of storage, one stored elsewhere.

**Costs** have several parts: the **amount stored** per month, the **requests** made (reads and writes), and **data transfer out** to the internet (egress). Moving data in is usually free, and moving it out is not. Watch egress when serving large files to many users, which is one reason to use a CDN. For a small project in Nigeria, remember that your own upload speed may be the real limit."""),
    ],
    diagram=grid([("OBJECT", "Buckets and keys|web access, near unlimited"), ("BLOCK", "A virtual disk for|one machine"), ("FILE", "A shared folder for|many machines"), ("BEST FOR OBJECT", "Uploads, backups,|images, logs"), ("BEST FOR BLOCK", "Databases and|operating systems"), ("BEST FOR FILE", "Shared content|and home folders")], cols=3,
                 note="Pick the shape that fits the job."),
    caption="Object storage holds files at scale, block storage is a machine's disk, and file storage is a shared folder.",
    terms=[("Bucket", "A container in object storage that holds objects."), ("Object", "A stored file together with its key and metadata."),
           ("Presigned URL", "A temporary web link that gives access to one private object."), ("Versioning", "Keeping older versions of an object so it can be recovered."),
           ("Lifecycle rule", "A rule that moves or deletes data automatically as it ages."), ("Egress", "Data transferred out of the cloud, which usually costs money.")],
    mistakes=["Making a bucket public to share a file instead of using a temporary link.", "Treating object storage durability as a backup strategy.", "Archiving data too early and paying heavy retrieval fees.", "Forgetting egress charges for popular large files."],
    quiz=[dict(q="Which storage type is a virtual disk attached to one machine?", o=["Block storage", "Object storage", "File storage", "Archive"], a=0,
               why="Block storage acts like a hard disk for one virtual machine."),
          dict(q="What is a safe way to share one private file temporarily?", o=["Make the whole bucket public", "Send the password", "A presigned URL", "Email the key"], a=2,
               why="A presigned URL grants short, limited access to a single object."),
          dict(q="What does a lifecycle rule do?", o=["Moves or deletes data automatically as it ages", "Encrypts the browser", "Creates users", "Opens ports"], a=0,
               why="Lifecycle rules reduce cost by changing storage class or removing old data."),
          dict(q="What does the 3-2-1 backup rule mean?", o=["Three clouds", "Three copies, two kinds of storage, one stored elsewhere", "Three users", "Three passwords"], a=1,
               why="It protects against many kinds of loss, including disasters and mistakes.")],
    activity="Create a bucket with public access blocked and versioning on. Upload a file, create a ten minute presigned link, overwrite the file and recover the old version, then add a lifecycle rule and delete everything.",
)

LESSONS[14] = dict(   # Containers and serverless functions
    minutes=15,
    hook="Two ideas changed how software runs in the cloud. Containers package an application with everything it needs, so it runs the same everywhere. Serverless functions go further: you hand the cloud a small piece of code, and it runs it only when something happens and charges you for the milliseconds it uses. You have met both in outline. In this lesson you will go deeper, learning how containers are run without managing servers, when Kubernetes is worth its complexity, how a serverless function is written and triggered, what its limits are, and how to choose between a virtual machine, a container service and a function for a real project.",
    sections=[
        ("Running containers without running servers", """You can build a container image on your laptop, but production needs somewhere to run it. Options, from simplest to most powerful:

- **Container platforms** (Google Cloud Run, Azure Container Apps, AWS App Runner): give the platform an image, and it runs it, handles HTTPS, scales up and down, even to zero when idle. Often the **easiest way** to run a web app.
- **Managed container services** (Amazon ECS with Fargate, Azure Container Instances): you define tasks and services, and the provider manages the servers underneath.
- **Kubernetes** (Amazon EKS, Azure AKS, Google GKE): a powerful system for running many containers across many machines, with rich features, and a steep learning curve.

The steps are similar everywhere: **build the image, push it to a registry** (a store for images), **deploy it with settings** (port, memory, environment variables, health check), and **scale** by running more copies."""),
        ("Do you need Kubernetes?", """Kubernetes is impressive, and it is often unnecessary. It gives you automatic restarts, rolling updates, scaling, service discovery and a common way to run many services. It also brings a lot to learn and operate: networking, storage, configuration, upgrades and security.

A sensible guide:

- **One app or a few services, a small team:** use a container platform or a PaaS. You will move faster.
- **Many services, several teams, complex needs, or a job that asks for it:** Kubernetes is worth learning. Use a **managed** version, so the provider runs the control plane.
- **Learning:** it is a valuable career skill, and you can practise cheaply with a local tool such as kind or minikube.

Do not choose Kubernetes because it sounds professional. Choose it when a simpler tool can no longer do the job."""),
        ("Serverless functions", """A **function** is a small piece of code that the cloud runs **in response to an event.** You write a handler, upload it and connect a trigger. In Python on AWS Lambda:

> [Python]
> import json
>
> def lambda_handler(event, context):
>     name = (event.get("queryStringParameters") or {}).get("name", "friend")
>     return {
>         "statusCode": 200,
>         "headers": {"Content-Type": "application/json"},
>         "body": json.dumps({"message": f"Hello, {name}!"}),
>     }

Triggers include a **web request** (through an API gateway), a **file arriving** in a bucket, a **message** in a queue, a **schedule** (every night at 2 a.m.) or a **database change.** You pay per request and per millisecond, with a generous free allowance, and there are no servers to patch. That makes functions excellent for small APIs, image processing, scheduled jobs and glue between services."""),
        ("Limits and design rules for functions", """Functions are powerful, with trade-offs you must design around:

- **Time limit:** a function must finish within a maximum duration (minutes, not hours). Long jobs need a different tool.
- **Cold starts:** after being idle, the first call can be slower while the environment starts. Keep functions small, and choose runtimes and memory sizes carefully.
- **Stateless:** a function may run in a new environment each time, so **store state in a database or storage**, not in memory.
- **Concurrency:** many copies can run at once, which can overwhelm a database. Set limits and use connection pooling or a queue.
- **Memory and CPU:** sizes are linked. More memory often means faster execution, and sometimes lower total cost.
- **Idempotency:** events can be delivered more than once, so write handlers that are safe to repeat.
- **Observability:** use logs and traces, because debugging distributed functions is harder.
- **Cost surprises:** a bug causing endless loops of triggers can cost a lot. Set budgets and alarms."""),
        ("Choosing between VM, container and function", """Compare them by what you need:

> [Guide]
> Virtual machine   Full control, any software, long-running work.   You patch and scale it.
> Container service Your own packaged app, steady web traffic.        Simple scaling, you manage the image.
> Function          Short, event-driven jobs, spiky or low traffic.   Least operations, time and style limits.

Examples: a **legacy application** with special software suits a VM. A **web API** that you built with Flask suits a container platform. A job that **resizes a photo when it is uploaded** suits a function. A **long video conversion** suits a container job or a batch service. Many systems **mix** them. Start with the simplest option that meets the needs, measure the cost and performance, and change only when the evidence says so."""),
    ],
    diagram=compare(("CONTAINERS", ["Your own packaged app", "Runs as long as needed", "Scales by copies", "Any language and library"]), ("FUNCTIONS", ["A small handler", "Runs only on events", "Scales per request", "Time and size limits"]), vs="or",
                    note="Start simple, and mix when it helps."),
    caption="Containers run your packaged app for as long as needed. Functions run small handlers only when events happen.",
    terms=[("Container registry", "A store for container images that platforms pull from."), ("Kubernetes", "A system for running and managing many containers across many machines."),
           ("Serverless function", "Code the cloud runs on demand, billed for the time it runs."), ("Trigger", "The event that starts a function, such as a web request or an uploaded file."),
           ("Cold start", "The extra delay when a function starts after being idle."), ("Concurrency", "How many copies of a function run at the same time.")],
    mistakes=["Choosing Kubernetes for a small app that needs a simple container platform.", "Keeping state in a function's memory.", "Ignoring concurrency limits and overwhelming the database.", "Writing handlers that break when an event arrives twice."],
    quiz=[dict(q="What is a good first way to run a containerised web app without managing servers?", o=["Build a data centre", "A container platform such as Cloud Run", "A tape drive", "A spreadsheet"], a=1,
               why="Container platforms run your image and handle scaling and HTTPS."),
          dict(q="Where should a function keep data that must last?", o=["In its memory", "In a database or storage", "In a comment", "Nowhere"], a=1,
               why="Functions are stateless, and their environment can disappear."),
          dict(q="Which workload suits a serverless function?", o=["Resizing an image when it is uploaded", "A ten-hour video render", "A database server", "A desktop game"], a=0,
               why="Short, event-driven jobs are ideal for functions."),
          dict(q="Why might you not need Kubernetes?", o=["It does not exist", "A simpler platform may do the job with less to learn and run", "It is free", "It is illegal"], a=1,
               why="Kubernetes adds operational complexity that small teams often do not need.")],
    activity="Write a small function that returns a greeting, deploy it behind an HTTP trigger, and measure the cold start time. Then package the same logic as a container and deploy it to a container platform, comparing cost and effort.",
)

LESSONS[15] = dict(   # Virtual networks, subnets and routing
    minutes=16,
    hook="Your virtual network is the layout of a gated compound. It decides which buildings face the street and which are tucked behind walls, who can walk where, and where the guard stands. A badly designed network is slow to fix and dangerous to leave: databases sitting on the open street, servers that cannot reach the internet to update, or two networks that cannot be joined because they used the same address range. You already know VPCs, subnets and CIDR. In this lesson you will design a real three-tier network, learn how traffic is routed, how to connect to other networks and services privately, and how to find out why something cannot connect.",
    sections=[
        ("A standard three-tier design", """Most web applications use the same safe layout:

- **Public subnets:** things that must be reachable from the internet, such as a **load balancer** and a **NAT gateway.** They have a route to an internet gateway.
- **Private application subnets:** the application servers or containers. They are **not** reachable from the internet. They receive traffic only from the load balancer.
- **Private data subnets:** databases and caches. They accept connections only from the application tier.

Spread each tier across **at least two availability zones,** so one data centre failing does not take the app down. The principle is **layers of exposure:** only the minimum is public, and each tier talks only to the next one. A typical address plan might use `10.0.0.0/16` for the network, with `/24` blocks for each subnet."""),
        ("Planning addresses and avoiding overlap", """Address planning feels dull until it goes wrong:

- Choose a **private range** (such as `10.0.0.0/8`, `172.16.0.0/12` or `192.168.0.0/16`) and give every network its own **non-overlapping CIDR block.** Two networks with the same range **cannot be connected** to each other without painful workarounds.
- **Leave room to grow.** It is hard to resize a subnet later. A `/16` network with `/24` subnets gives plenty of space for most projects.
- Remember that providers **reserve a few addresses** in each subnet.
- Keep a simple **address register** (a table) for your organisation: which range belongs to which network, region and team.
- **IPv6** is increasingly supported and useful, and can avoid some NAT costs.

Document the plan in a diagram. The person who joins your team next year will be grateful, and it may be you."""),
        ("Route tables decide where traffic goes", """Each subnet is linked to a **route table,** a short list of rules that says “traffic for this destination goes to that target.”

> [Routes]
> Public subnet:
>   10.0.0.0/16   -> local              (inside the network)
>   0.0.0.0/0     -> internet gateway   (everything else goes out to the internet)
>
> Private app subnet:
>   10.0.0.0/16   -> local
>   0.0.0.0/0     -> NAT gateway        (outbound only, for updates)
>
> Private data subnet:
>   10.0.0.0/16   -> local              (no route to the internet at all)

A subnet is **public** only because its route table points to an internet gateway. A **NAT gateway** lets private servers start connections to the internet (for patches and APIs) while staying unreachable from outside. NAT gateways are **charged by the hour and by data,** so they are a common cost surprise in small projects."""),
        ("Private connections and joining networks", """You often need networks to talk to each other, or to cloud services, without crossing the public internet:

- **VPC peering and transit gateways** connect networks (the address ranges must not overlap).
- **VPN** connections create an encrypted tunnel between your office or home and the cloud over the internet.
- **Dedicated connections** (such as AWS Direct Connect, Azure ExpressRoute) give a private line, for organisations with heavy or strict needs.
- **Private endpoints** (for example, VPC endpoints for S3 and other services) let your servers reach a cloud service **without a public path,** which is more secure and can lower NAT costs.
- **Private DNS** lets resources find each other by name inside the network.

A hybrid design may connect a company's Lagos office to its cloud network through a VPN, so staff can reach private systems without exposing them."""),
        ("Finding out why something cannot connect", """Network problems are common and solvable with a checklist. Start at the source and move toward the destination:

1. **Is the destination running and listening** on the right port? (Check from inside the server.)
2. **Security group (or firewall) rules:** does the destination allow traffic from the source, on that port?
3. **Route tables:** does the source subnet have a route to the destination? Is there an internet gateway or NAT when needed?
4. **Network ACLs:** these are stateless subnet filters. Do they allow both the request and the reply?
5. **DNS:** does the name resolve to the right address?
6. **The operating system firewall** on the server.
7. **Overlapping address ranges** or a missing peering route.

Use the provider's tools: **flow logs** show accepted and rejected traffic, and **reachability analysers** trace a path and point to the blocking rule. Change **one thing at a time,** and write down the fix."""),
    ],
    diagram=tree("VPC 10.0.0.0/16", [("Public subnets", ["Load balancer", "NAT gateway"]), ("Private app subnets", ["App servers", "Containers"]), ("Private data subnets", ["Database", "Cache"])],
                 note="Layers of exposure across two availability zones."),
    caption="A three-tier network: public load balancers, private application servers and private databases, spread across zones.",
    terms=[("Three-tier network", "A design with public, application and data layers separated into subnets."), ("Route table", "A list of rules that sends traffic to the right target."),
           ("NAT gateway", "A service that lets private servers reach the internet without being reachable from it."), ("VPC peering", "A direct connection between two virtual networks."),
           ("VPC endpoint", "A private path from your network to a cloud service."), ("Flow logs", "Records of the network traffic that was accepted or rejected.")],
    mistakes=["Choosing overlapping address ranges for networks that must be joined.", "Putting the database in a public subnet.", "Forgetting that NAT gateways cost money every hour.", "Changing many network settings at once while troubleshooting."],
    quiz=[dict(q="What makes a subnet public?", o=["Its name", "A route to an internet gateway", "Its size", "Its colour"], a=1,
               why="Public simply means the route table sends internet traffic to an internet gateway."),
          dict(q="Where should a database normally live?", o=["A public subnet", "A private data subnet", "On the load balancer", "Outside the network"], a=1,
               why="Databases should be reachable only from the application tier."),
          dict(q="What is a NAT gateway used for?", o=["Letting private servers start connections to the internet while staying unreachable from it", "Storing files", "Encrypting disks", "Naming domains"], a=0,
               why="NAT provides outbound-only internet access for private resources."),
          dict(q="Why must connected networks avoid overlapping CIDR ranges?", o=["It is tradition", "Traffic could not tell which network an address belongs to", "It makes them faster", "Providers charge more"], a=1,
               why="Overlapping ranges make routing ambiguous, so they cannot be joined cleanly.")],
    activity="Design a three-tier network on paper with CIDR blocks for two availability zones, the route table for each subnet and the security rules between tiers. Then build it in your cloud account and clean it up.",
)

LESSONS[16] = dict(   # Load balancers, DNS and CDNs
    minutes=15,
    hook="On a market day, hundreds of customers arrive at once. A shop with one counter and one till collapses. A shop with a person at the door sending customers to the shortest queue, a sign that tells people where to find you, and branch stalls close to every neighbourhood copes easily. Websites handle crowds the same way, with three tools. A load balancer shares requests across many servers. DNS tells people where your site is. A content delivery network, or CDN, keeps copies of your content near your visitors. Together they decide whether a site is fast, available and resilient. In this lesson you will learn how each works and how they combine.",
    sections=[
        ("Load balancers: sharing the work", """A **load balancer** receives incoming requests and passes each to one of several healthy servers. This gives you:

- **Scale:** add more servers behind it as traffic grows.
- **Availability:** if a server fails, traffic goes to the others.
- **Safe updates:** replace servers one at a time with no downtime.

Two main kinds: **Layer 7 (application) load balancers** understand HTTP, so they can route by address or header (`/api` to one group, `/images` to another), handle HTTPS certificates and add security rules. **Layer 4 (network) load balancers** work with raw connections, and are very fast and used for non-HTTP traffic. Typical examples are the AWS Application Load Balancer, Azure Application Gateway and Google Cloud Load Balancing."""),
        ("Health checks and scaling", """A load balancer must know which servers are healthy. It sends a **health check** (for example `GET /health`) every few seconds and removes servers that fail it, adding them back when they recover. Design a good `/health` endpoint: it should confirm the app is running and, if appropriate, that it can reach its database.

Combine the load balancer with **auto scaling:** a rule that adds servers when CPU or request counts rise, and removes them when traffic falls. For this to work, servers must be **stateless:** sessions and files stored in a shared database, cache or storage, not on a single machine. Other settings include **connection draining** (let current requests finish before removing a server), **sticky sessions** (send a user to the same server, best avoided), and the **algorithm** (round robin, least connections)."""),
        ("DNS: the address book", """**DNS** turns a name such as `yabakes.ng` into an address. Important records:

- **A and AAAA:** a name to an IPv4 or IPv6 address.
- **CNAME:** a name that points to another name, such as your load balancer's address.
- **ALIAS or ANAME:** a way to point the bare domain to a cloud service where CNAME is not allowed.
- **MX:** where email goes. **TXT:** verification and email security (SPF, DKIM).
- **NS:** which servers answer for the domain.

Every record has a **TTL** (time to live), how long others may remember the answer. A long TTL is faster and cheaper, a short one lets changes spread quickly, so **lower the TTL before a planned move.** Cloud DNS services (Amazon Route 53, Azure DNS, Google Cloud DNS, Cloudflare) can also do **routing policies,** such as sending users to the nearest region, splitting traffic by weight, or failing over to a backup site when a health check fails."""),
        ("CDNs: content close to users", """The speed of light matters. A visitor in Lagos requesting a file from a server in Europe or the United States waits for every round trip. A **CDN** keeps **cached copies** of your files on servers in many cities (**edge locations**), and serves a visitor from the closest one. Benefits:

- **Faster pages,** especially for images, scripts, video and downloads.
- **Less load** on your origin server and **lower data costs.**
- **Protection:** many CDNs absorb **DDoS attacks** and include a **web application firewall.**
- **HTTPS handled at the edge.**

Set **cache headers** (`Cache-Control`) so the CDN knows how long to keep each file, and use **versioned file names** (`app.4f2a9c.css`) so updates show instantly. Never cache **private or personalised** pages publicly. Examples: Amazon CloudFront, Azure Front Door, Google Cloud CDN and Cloudflare. Check where each provider has edge locations near your users, since coverage in Africa is growing."""),
        ("Putting the three together", """A common production flow:

1. A visitor types `www.yabakes.ng`. **DNS** returns the address of the CDN.
2. The **CDN** answers from its cache if it can (images, scripts), or passes the request to the origin.
3. The **load balancer** receives it, terminates HTTPS and picks a healthy server.
4. The **application servers** (in two or more availability zones) handle it, using a **database** and a **cache.**
5. The response travels back, and the CDN may store it for the next visitor.

Think about **failures** at each layer: a server dies (the load balancer routes around it), a zone fails (the other zone serves), a region fails (DNS failover to another region, for the most critical systems), the origin is slow (the CDN serves cached copies). Test these deliberately, rather than hoping."""),
    ],
    diagram=flow([("Visitor", "types the name"), ("DNS", "where is it?"), ("CDN", "cached copy|if it has one"), ("Load balancer", "picks a healthy|server"), ("App servers", "in two zones")], "cl16",
                 note="Each layer adds speed or resilience."),
    caption="DNS finds the CDN, the CDN serves cached files, and the load balancer sends the rest to healthy servers.",
    terms=[("Load balancer", "A service that shares incoming requests across several servers."), ("Health check", "A regular test that tells a load balancer whether a server is working."),
           ("TTL", "How long a DNS answer may be remembered before it is checked again."), ("CDN", "A network of servers that cache and serve content close to users."),
           ("Edge location", "A CDN site close to users where cached copies are kept."), ("Auto scaling", "Adding or removing servers automatically as demand changes.")],
    mistakes=["Keeping user sessions in one server's memory behind a load balancer.", "Caching personalised pages in a public CDN.", "Forgetting to lower DNS TTL before a planned move.", "Writing a health check that always says OK."],
    quiz=[dict(q="What does a load balancer do when a server fails its health check?", o=["Sends traffic to it anyway", "Stops sending traffic to it until it recovers", "Deletes it", "Changes the domain"], a=1,
               why="Unhealthy servers are removed from rotation and added back when healthy."),
          dict(q="What does a CDN mainly do?", o=["Stores passwords", "Serves cached content from locations close to users", "Writes code", "Replaces databases"], a=1,
               why="Edge caching reduces delay and load on your origin."),
          dict(q="Why must servers behind a load balancer be stateless?", o=["Any server may handle any request", "It is cheaper", "The law requires it", "It makes them slower"], a=0,
               why="If state lives on one server, other servers cannot serve that user correctly."),
          dict(q="What does a short DNS TTL allow?", o=["Changes spread quickly", "Free hosting", "Better colours", "Bigger files"], a=0,
               why="Short TTLs let updates take effect faster, which helps during migrations.")],
    activity="Put two small servers behind a load balancer with a /health check, point a domain at it using DNS, add a CDN in front for static files, and then stop one server to watch the traffic continue.",
)

LESSONS[17] = dict(   # Firewalls and network security
    minutes=15,
    hook="Within minutes of switching on a server with a public address, strangers start knocking. They are not targeting you personally. Automated tools sweep the entire internet, trying doors on every machine, looking for an open database, a forgotten remote login, an unpatched web application. Most attacks that succeed do not use clever techniques. They walk through a door that someone left open. Network security in the cloud is the craft of closing every door you do not need, guarding the ones you do, and noticing when someone tries the handle. In this lesson you will learn the cloud's firewalls, how to layer defences, how to reach servers without exposing them and the mistakes that cause real breaches.",
    sections=[
        ("Security groups: the firewall on every resource", """A **security group** (AWS), **network security group** (Azure) or **firewall rule** (Google Cloud) is a virtual firewall attached to a resource. It lists what traffic may **come in** and go out:

> [Rules]
> Load balancer:  allow TCP 443 from anywhere (0.0.0.0/0)
> App servers:    allow TCP 8000 only from the load balancer's group
> Database:       allow TCP 5432 only from the app servers' group
> Admin access:   no SSH at all, use Session Manager

Key ideas: security groups are **stateful** (a reply to an allowed request is allowed automatically) and **deny by default** (anything not allowed is blocked). Best practice is to **reference other groups** rather than address ranges, so only the right tier can talk to the next. Keep rules **narrow** and **named clearly.** Review them often, because the “temporary” wide-open rule is the one that gets forgotten."""),
        ("Network ACLs, web firewalls and DDoS protection", """Several other layers add protection:

- **Network ACLs:** rules at the **subnet** edge, usually **stateless** (you must allow requests and replies). A coarse extra layer, mostly left at defaults unless you need to block specific addresses.
- **Web application firewall (WAF):** examines web requests for attacks such as SQL injection and cross-site scripting, bad bots and abusive rates. Examples: AWS WAF, Azure WAF, Google Cloud Armor, Cloudflare WAF.
- **DDoS protection:** attackers flood a site with traffic to knock it over. Cloud providers and CDNs absorb a lot of this automatically, and extra paid plans exist for critical sites.
- **Rate limiting** on logins and APIs.
- **Geo or IP rules** for known bad sources, used carefully.

A WAF is a **helpful extra layer,** not a replacement for writing secure code."""),
        ("Reaching servers without exposing them", """Administrators need access, and the safest access is the one that is **not open to the internet:**

- **Managed session tools** such as AWS Systems Manager Session Manager, Azure Bastion or Google Identity-Aware Proxy let you open a shell **without any inbound port** and with logging and IAM-based permission.
- **A bastion host** (jump server) is a hardened machine that is the only way in. It must itself be well protected.
- **A VPN** gives you a private route into the network, with MFA.
- **Allow-list your own IP** if you must open SSH or RDP, and **close it when finished.**
- **Never expose** databases, admin panels, Redis, Docker, Kubernetes dashboards or remote desktop to the whole internet.

The most common cause of cloud compromise is a remote access port or a database open to `0.0.0.0/0`."""),
        ("Defence in depth and zero trust", """No single wall is enough, so build **layers**: edge protection, network rules, host hardening, application security and data encryption. If one layer fails, another still stands.

**Zero trust** is the modern mindset: **never assume something is safe just because it is inside the network.** Instead:

- **Verify identity** for every request, between people and services.
- **Give least privilege** to each workload.
- **Encrypt traffic everywhere,** including between internal services.
- **Segment** networks, so a compromised machine cannot reach everything.
- **Log and watch** all access.

Also keep the **hosts** healthy: patch operating systems and dependencies, remove unused software, use hardened images, and run applications with minimal permissions. Remember the **shared responsibility** rule: the provider secures the data centre, you secure your configuration."""),
        ("Watch, detect and respond", """Prevention will sometimes fail, so detect early:

1. **Turn on logging:** VPC flow logs, load balancer and WAF logs, cloud audit logs (who did what in your account), and operating system logs.
2. **Use the provider's threat detection** (such as Amazon GuardDuty, Microsoft Defender for Cloud, Google Security Command Center) to flag suspicious behaviour.
3. **Set alerts** for risky changes: a security group opened to the world, a new admin created, a public bucket, logins from unusual places.
4. **Scan regularly:** check for open ports and misconfigurations using the provider's tools. Only scan systems you own or have written permission to test.
5. **Have a response plan:** how to isolate a machine (change its security group), rotate keys, preserve evidence, notify people and restore from clean backups.
6. **Practise:** run a tabletop exercise once a year.

If personal data is involved, you may have legal duties to report a breach, under the **NDPA 2023** in Nigeria and other laws."""),
    ],
    diagram=rings(["Edge: DDoS protection, CDN and WAF", "Network: security groups and segmentation", "Hosts: patched, hardened, least privilege", "Application: validation and authentication", "YOUR DATA, encrypted"],
                  note="Layers: if one fails, another still protects."),
    caption="Defence in depth: edge protection, network rules, hardened hosts and application security around encrypted data.",
    terms=[("Security group", "A virtual firewall attached to a resource that allows only listed traffic."), ("Stateful", "Remembering a connection so that replies to allowed requests are allowed automatically."),
           ("WAF", "A web application firewall that inspects web requests for attacks."), ("Bastion host", "A hardened server that is the only entry point to a private network."),
           ("Zero trust", "Never trusting something just because it is inside the network."), ("Threat detection", "A service that flags suspicious activity in your cloud account.")],
    mistakes=["Opening SSH, RDP or a database to 0.0.0.0/0.", "Leaving a temporary wide-open rule in place.", "Assuming a firewall replaces secure code.", "Turning on no logging, so an attack leaves no trace."],
    quiz=[dict(q="What does stateful mean for a security group?", o=["Replies to allowed requests are allowed automatically", "It is slow", "It stores files", "It encrypts data"], a=0,
               why="The firewall remembers the connection, so return traffic is permitted."),
          dict(q="Which is the safest way to administer a server?", o=["SSH open to everyone", "A managed session tool with no inbound ports", "Password login", "A public database"], a=1,
               why="Managed access avoids opening ports and logs every session."),
          dict(q="What is zero trust?", o=["Trust everything inside the network", "Never assume something is safe just because it is inside the network", "No passwords", "No firewalls"], a=1,
               why="Every request is verified, even from inside."),
          dict(q="What is the most common cause of cloud compromise mentioned in this lesson?", o=["Cold weather", "A remote access port or database left open to the whole internet", "Too many users", "Large files"], a=1,
               why="Simple misconfigurations are exploited far more often than clever hacks.")],
    activity="Review the security groups of one of your own practice projects. List every rule open to 0.0.0.0/0, justify or remove each, switch admin access to a managed session tool and turn on flow and audit logging.",
)

LESSONS[18] = dict(   # Encryption, keys and secrets
    minutes=15,
    hook="Locks are only as good as the care taken of the keys. A bank vault with a perfect door and the key taped to the wall is not secure. In cloud security, encryption scrambles your data so a thief who steals it cannot read it, but only if the keys are protected. Likewise, passwords, tokens and database credentials, called secrets, are a favourite target, and the most common way they leak is painfully ordinary: a developer pastes one into code, and it ends up on a public GitHub page. In this lesson you will learn what encryption protects, how cloud key management works, how to store and use secrets safely, and the habits that keep keys from becoming the weak link.",
    sections=[
        ("Encryption in transit and at rest", """Data needs protection in two states:

- **In transit:** moving across a network. Protect it with **TLS** (HTTPS). Never send passwords or personal data over plain HTTP. Use TLS between your own services too.
- **At rest:** stored on disks, in databases and in backups. Protect it with **encryption at rest,** which is **on by default** for many cloud storage and database services today, and can be turned on for the rest.

Encryption defends against several threats: a stolen disk, a leaked backup, a misconfigured storage bucket and a curious insider at the provider. It does **not** protect against a logged-in attacker who has legitimate access, or a bug in your application. So encryption is **one layer,** working together with access control. And do not confuse **encryption** (reversible with a key) with **hashing** (one-way, used for passwords)."""),
        ("Keys and the key management service", """Encryption needs keys, and keys need a safe home. Cloud providers offer a **Key Management Service (KMS):** AWS KMS, Azure Key Vault and Google Cloud KMS. They keep keys in specially protected hardware, control who may use them, and record every use.

A common design is **envelope encryption:**

1. A **data key** encrypts your data (fast, done locally).
2. The data key itself is **encrypted by a master key** held in KMS and never leaving it.
3. The encrypted data and the encrypted data key are stored together.
4. To read the data, you ask KMS to unlock the data key, **if your identity is allowed.**

You choose between **provider-managed keys** (simple, automatic), **customer-managed keys** (you control the policy and rotation) and, in special cases, **keys you bring yourself.** Turn on **automatic key rotation,** and understand that **deleting a key makes the data it protects permanently unreadable,** so use deletion waiting periods."""),
        ("Secrets: what they are and where they must not be", """A **secret** is any value that grants access: database passwords, API keys, payment secret keys, tokens, private certificates, signing keys. They must **never** be:

- Written in **source code,** even in a private repository.
- Committed to **Git,** including old history. Deleting the file later does not remove it from history.
- Stored in **chat messages,** screenshots, tickets or documents.
- Placed in **front-end or mobile app code,** which anyone can extract.
- Left in **container images** or logs.
- **Shared between people and environments:** test and production should have different secrets.

Bots scan public repositories continuously. A leaked cloud key can be abused within minutes. If a secret leaks, **rotate it immediately** (create a new one, switch over, delete the old), and check the logs for misuse."""),
        ("A secrets manager and workload identity", """Store secrets in a **secrets manager:** AWS Secrets Manager or Parameter Store, Azure Key Vault, Google Secret Manager. Benefits: encryption, **access control by identity,** **audit logs,** versioning and **automatic rotation** for some databases.

Even better, **avoid long-lived secrets** altogether by using **workload identity:** instead of giving an application an access key, **attach a role to the server, container or function.** The platform gives it short-lived credentials automatically, and no key exists to leak.

> [Python]
> import boto3
>
> # No access key in the code. The attached role provides temporary credentials.
> secrets = boto3.client("secretsmanager", region_name="af-south-1")
> value = secrets.get_secret_value(SecretId="prod/db-password")["SecretString"]

The app asks for the secret **at start-up or when needed,** keeps it only in memory, and never prints it. Developers on their laptops should use **short-lived sign-ins** (single sign-on) instead of permanent keys."""),
        ("Habits that keep keys safe", """Practical routines:

1. **Scan for secrets** in your code with tools such as gitleaks or GitHub secret scanning, and add a **pre-commit hook.** Treat any alert as urgent.
2. **Use `.gitignore`** for `.env` files and key files from the first commit.
3. **Give each application its own credentials,** with least privilege, so one leak has a small reach.
4. **Rotate regularly,** and have a documented procedure to rotate fast.
5. **Restrict who can read secrets** and who can use keys, and review it.
6. **Use TLS certificates** from the provider (such as AWS Certificate Manager) or Let's Encrypt, with automatic renewal, so they never expire unnoticed.
7. **Encrypt backups** and protect the keys separately from the backups.
8. **Document** where each secret lives and who owns it.
9. **Meet your legal duties:** protecting personal data with suitable security measures is required under the **NDPA 2023** and similar laws.

Security is a habit, and every shortcut with a secret becomes a story that starts with “we found the key on GitHub”."""),
    ],
    diagram=stack([("YOUR DATA", "encrypted with a data key"), ("DATA KEY", "itself encrypted by the master key"), ("MASTER KEY IN KMS", "never leaves the protected service"), ("ACCESS POLICY AND AUDIT LOG", "who may use the key, and a record of each use")], "cl18",
                  note="Envelope encryption."),
    caption="Envelope encryption: data is encrypted with a data key, which a master key in KMS protects, under a strict access policy.",
    terms=[("Encryption at rest", "Scrambling stored data so it cannot be read without the key."), ("TLS", "The protocol that encrypts data moving across a network."),
           ("KMS", "A key management service that stores and controls encryption keys."), ("Envelope encryption", "Encrypting data with a data key that a master key then protects."),
           ("Secrets manager", "A service that stores credentials securely and controls who may read them."), ("Workload identity", "Giving a server or function a role so it gets short-lived credentials without stored keys.")],
    mistakes=["Committing a secret to Git and thinking deleting the file fixes it.", "Using the same secrets for testing and production.", "Deleting an encryption key without a waiting period.", "Putting secret keys in front-end or mobile code."],
    quiz=[dict(q="What happens to data if its encryption key is permanently deleted?", o=["It becomes faster", "It becomes permanently unreadable", "It is copied", "Nothing"], a=1,
               why="Without the key, the encrypted data cannot be decrypted."),
          dict(q="Where should an application's database password be kept?", o=["In the code", "In a secrets manager", "In a chat message", "In the page source"], a=1,
               why="A secrets manager encrypts it, controls access and logs reads."),
          dict(q="What is the advantage of workload identity?", o=["No long-lived key exists to leak, because the platform issues short-lived credentials", "It is louder", "It uses no network", "It removes the need for IAM"], a=0,
               why="Short-lived, automatically issued credentials reduce the risk of leaks."),
          dict(q="What should you do first if a secret is leaked?", o=["Wait", "Rotate it immediately and check the logs", "Delete the repository only", "Tell nobody"], a=1,
               why="Replace the secret straight away and look for misuse.")],
    activity="Scan one of your repositories for secrets with gitleaks. Move any secret into a secrets manager, replace access keys with a role, turn on key rotation and write a one-page procedure for rotating a leaked key.",
)

LESSONS[19] = dict(   # Managed databases, queues and APIs
    minutes=16,
    hook="Running your own database server is like running your own power station. It is possible, and you will spend your nights on backups, patches, failovers and disk space instead of on your product. Cloud providers sell managed versions of these hard parts: databases that back themselves up, message queues that never lose a message, API gateways that guard your front door. Choosing and using them well is the heart of cloud application design. In this lesson you will learn which kind of database fits which job, what you get from a managed database, how queues and events keep systems steady under pressure and how an API gateway protects and organises your services.",
    sections=[
        ("Choosing the right kind of database", """There is no single best database. Match the type to the data and the questions:

- **Relational (SQL):** PostgreSQL, MySQL, Amazon RDS and Aurora, Azure SQL, Cloud SQL. Tables with relations, strong consistency and transactions. **The default choice** for most business applications: orders, customers, payments.
- **Document:** MongoDB, DynamoDB (also key-value), Firestore. Flexible JSON-like records, good for varied or fast-changing structures and huge scale.
- **Key-value and cache:** Redis, Memcached. Extremely fast lookups for sessions, counters and cached results.
- **Search:** OpenSearch or Elasticsearch for full-text search and log analysis.
- **Data warehouse:** BigQuery, Redshift, Snowflake. For analysing large volumes of data, not for running the live app.

If you are unsure, **start with PostgreSQL.** It is reliable, popular and does most jobs well. Add specialised stores only when a clear need appears."""),
        ("What a managed database gives you", """With a managed relational database, the provider handles:

- **Automated backups** and **point-in-time recovery** (restore to a chosen minute).
- **Patching** of the engine and the operating system.
- **High availability:** a standby copy in another zone (**multi-AZ**), with automatic failover when the main one fails.
- **Read replicas:** extra copies that serve reads and spread the load.
- **Monitoring, encryption and scaling** options.

You still own: the **schema,** the **queries,** the **indexes,** the **users and permissions,** the **connections,** and testing that restores work. Also remember **cost:** a database is billed while it runs, with its storage and backups, so delete practice databases. Place it in a **private subnet,** never on the open internet, and give each application its own limited account."""),
        ("Queues and events: keeping the user from waiting", """A **queue** is a waiting line for jobs. The web app drops a message ("send the receipt for order 88") and answers the user immediately. A separate **worker** picks messages up and does the slow work. Services: Amazon SQS, Azure Service Bus and Storage Queues, Google Pub/Sub.

Benefits: **smoothing spikes** (the queue absorbs a rush while workers catch up), **isolating failures** (a broken email service does not break checkout) and **independent scaling.**

Important behaviours to design for:

- **At-least-once delivery:** a message may arrive **twice,** so handlers must be **idempotent.**
- **Visibility timeout and retries:** if a worker fails, the message returns to the queue.
- **Dead-letter queue (DLQ):** messages that fail repeatedly are set aside for inspection.
- **Ordering and duplicates:** strict order needs special queue types, with trade-offs."""),
        ("Topics, events and fan-out", """A **topic** (publish and subscribe) sends one message to **many subscribers:** Amazon SNS, EventBridge, Pub/Sub, Event Grid. When an order is placed, one event can trigger the email service, the stock service and the analytics service, **without the order service knowing about any of them.**

This is **event-driven design:** services react to facts that happened ("OrderPlaced"), rather than calling each other directly. It makes systems flexible and loosely coupled, but it also makes flows harder to follow, so:

- **Name events clearly** and document their fields.
- **Version your event formats.**
- **Trace** requests across services with a shared id.
- **Keep it simple:** a queue between two services is often enough."""),
        ("API gateways and putting it together", """An **API gateway** (Amazon API Gateway, Azure API Management, Google Cloud API Gateway) sits in front of your services and gives you one front door. It can:

- **Authenticate** callers (API keys, tokens, JWT checks).
- **Throttle** and apply **quotas** to protect your backend.
- **Route** paths to different services or functions.
- **Validate** requests, transform data, **cache** responses and write **logs.**
- Manage **versions** (`/v1`, `/v2`) and publish **documentation.**

A typical order system: the **client** calls the **API gateway,** which calls a **function or container.** The app saves the order in the **managed database,** puts a message on a **queue,** and returns “received.” **Workers** process payment confirmation and email, and a **cache** speeds up product lookups. Each part is managed, scalable and replaceable. Remember the downside: **lock-in** to provider-specific services, so keep business logic portable and the glue thin."""),
    ],
    diagram=flow([("Client", "app or browser"), ("API gateway", "auth, limits,|routing"), ("App", "function or|container"), ("Queue", "slow jobs wait"), ("Workers", "email, payment|follow-up")], "cl19",
                 note="The user never waits for the slow parts."),
    caption="The client calls an API gateway, the app answers quickly and queues slow jobs for workers, with a managed database behind.",
    terms=[("Managed database", "A database whose backups, patching and failover are handled by the provider."), ("Multi-AZ", "A setup with a standby copy in another availability zone for automatic failover."),
           ("Queue", "A waiting line of messages for workers to process."), ("Dead-letter queue", "A queue for messages that failed repeatedly, kept for inspection."),
           ("Event-driven", "A design where services react to events instead of calling each other directly."), ("API gateway", "A front door that authenticates, limits and routes API requests.")],
    mistakes=["Choosing an exotic database before trying PostgreSQL.", "Putting a database on the public internet.", "Writing queue consumers that break when a message arrives twice.", "Never testing a restore from backup."],
    quiz=[dict(q="Which database type is the usual default for orders and customers?", o=["Relational such as PostgreSQL", "A spreadsheet", "A cache only", "A tape"], a=0,
               why="Relational databases give strong consistency and transactions for business data."),
          dict(q="What does a dead-letter queue hold?", o=["Old logs", "Messages that failed repeatedly, for inspection", "Passwords", "Backups"], a=1,
               why="It keeps problem messages from blocking the main queue and lets you investigate."),
          dict(q="Why must queue handlers be idempotent?", o=["Messages may be delivered more than once", "It is faster", "Queues are slow", "It is optional"], a=0,
               why="At-least-once delivery means duplicates can occur."),
          dict(q="What can an API gateway do?", o=["Replace the internet", "Authenticate, throttle and route requests", "Store your data", "Write your code"], a=1,
               why="A gateway protects and organises access to your services.")],
    activity="Sketch an order system using a managed PostgreSQL database, an API gateway, a queue with a dead-letter queue and a worker. Then build the queue and worker part and test what happens when the worker fails.",
)

LESSONS[20] = dict(   # CI/CD pipelines for cloud apps
    minutes=16,
    hook="Releasing software by hand is how mistakes get into production: someone forgets a step, deploys the wrong branch, or fixes a bug directly on the live server and then nobody remembers how. A pipeline turns the release into a repeatable, automatic machine. Every change is tested, built and deployed the same way, every time, and a failed test stops it before customers are affected. You know what CI and CD mean. In this lesson you will build a real pipeline for a cloud application, understand its stages, handle credentials safely, choose a deployment strategy that lets you release without downtime and roll back fast when something goes wrong.",
    sections=[
        ("The stages of a pipeline", """A typical pipeline runs these stages, each only if the previous one passes:

1. **Trigger:** a push or a pull request starts it.
2. **Checks:** formatting, linting and **unit tests.**
3. **Build:** create the deployable **artifact,** such as a container image, tagged with the commit id.
4. **Security checks:** scan dependencies and the image for known vulnerabilities, and look for leaked secrets.
5. **Publish:** push the image to a **registry.**
6. **Deploy to staging:** a test environment that mirrors production.
7. **Smoke tests:** a few quick checks that the deployed app really works.
8. **Approval** (if needed), then **deploy to production.**
9. **Post-deploy checks and monitoring,** with automatic rollback if they fail.

Build **once** and deploy the **same artifact** to every environment. Rebuilding for production means you are not shipping what you tested."""),
        ("A working example with GitHub Actions", """GitHub Actions, GitLab CI, Azure DevOps and Google Cloud Build all follow the same idea. A pipeline is a file stored in your repository:

> [YAML]
> name: ci-cd
> on:
>   push:
>     branches: [main]
> permissions:
>   id-token: write      # lets the job get short-lived cloud credentials
>   contents: read
> jobs:
>   test-build-deploy:
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v4
>       - run: pip install -r requirements.txt
>       - run: pytest
>       - uses: aws-actions/configure-aws-credentials@v4
>         with:
>           role-to-assume: arn:aws:iam::123456789012:role/github-deploy
>           aws-region: af-south-1
>       - run: ./deploy.sh ${{ github.sha }}

Action versions change, so check the current documentation. The account number above is a placeholder. The pipeline lives in version control, so changes to it are reviewed like code."""),
        ("Credentials: no long-lived keys in the pipeline", """The pipeline can deploy to your production cloud, which makes it a prime target. Protect it:

- **Prefer short-lived credentials through OpenID Connect (OIDC):** the pipeline proves its identity to the cloud and receives a temporary token for a **specific role,** as in the example above. No permanent access key is stored.
- If you must store a secret, use the CI system's **encrypted secrets,** and never print them in logs.
- Give the deployment role **least privilege:** only what is needed to deploy this app, in this environment.
- **Separate roles** for staging and production, and require **manual approval** for production.
- **Protect the main branch:** required reviews and passing checks before merging.
- **Be careful with third-party actions** and dependencies: pin them to a specific version, since a compromised pipeline step can steal secrets.
- **Do not run untrusted code** from forks with access to secrets."""),
        ("Deployment strategies", """How you swap the old version for the new matters:

- **Recreate:** stop the old, start the new. Simple, with downtime.
- **Rolling update:** replace servers a few at a time. No downtime, but old and new run together briefly, so they must be compatible.
- **Blue/green:** run the new version (green) alongside the old (blue), test it, then switch traffic over at once. Instant **rollback** by switching back. Costs extra capacity during the change.
- **Canary:** send a small share of users (such as 5%) to the new version, watch errors, then increase. Safest for risky changes.
- **Feature flags:** deploy code switched off, then turn features on for chosen users without a new deployment.

**Database changes** are the hard part: use **backward-compatible migrations** (add first, remove later) so old and new code both work during the switch. Always have a **tested rollback** plan."""),
        ("Make the pipeline good", """A pipeline is software too. Keep it healthy:

1. **Keep it fast.** Over ten minutes, people stop waiting. Cache dependencies and run tests in parallel.
2. **Keep it reliable.** Flaky tests destroy trust, so fix or remove them.
3. **Fail clearly:** messages should say what broke and where.
4. **Version everything:** the pipeline file, scripts and infrastructure code.
5. **Deploy small and often.** Many small releases are safer than a big one every month.
6. **Track the numbers:** deployment frequency, lead time, failure rate and time to recover.
7. **Watch the costs:** build minutes and artifact storage are billed.
8. **Document** how to release, roll back and fix the pipeline itself.

The goal is boring releases. When deploying is easy and safe, teams ship improvements constantly instead of fearing release day."""),
    ],
    diagram=flow([("Push", "code reaches|the repository"), ("Test", "lint, unit tests,|scans"), ("Build", "one image,|tagged"), ("Staging", "deploy and|smoke test"), ("Production", "approve, canary,|monitor")], "cl20",
                 note="Build once, deploy the same artifact everywhere."),
    caption="A pipeline tests, builds once, deploys to staging, then releases to production with checks and an easy rollback.",
    terms=[("Pipeline", "An automated series of stages that tests, builds and deploys code."), ("Artifact", "The built, deployable output of a pipeline, such as a container image."),
           ("OIDC", "A way for a pipeline to get short-lived cloud credentials without stored keys."), ("Blue/green deployment", "Running old and new versions side by side and switching traffic between them."),
           ("Canary release", "Sending a small share of users to a new version before everyone."), ("Feature flag", "A switch that turns a feature on or off without a new deployment.")],
    mistakes=["Rebuilding the artifact for production instead of promoting the tested one.", "Storing long-lived cloud keys in the pipeline.", "Making breaking database changes in the same release as the code.", "Ignoring flaky tests until nobody trusts the pipeline."],
    quiz=[dict(q="Why build the artifact only once?", o=["It is faster", "You deploy exactly what you tested", "Builds are illegal", "Servers require it"], a=1,
               why="Promoting the same artifact removes differences between tested and deployed code."),
          dict(q="What is a safer alternative to storing a cloud access key in CI?", o=["Print it in the logs", "Email it", "Use the root key", "Short-lived credentials through OIDC"], a=3,
               why="Temporary role credentials leave no long-lived key to leak."),
          dict(q="Which strategy lets you roll back instantly by switching traffic?", o=["Blue/green", "Recreate", "Delete everything", "Manual copy"], a=0,
               why="The old version stays running until you are sure."),
          dict(q="What is a canary release?", o=["A bird", "Deploying to everyone at once", "Sending a small share of users to the new version first", "A backup"], a=2,
               why="A small exposure limits the damage if the release is bad.")],
    activity="Write a pipeline for a small app that runs tests, builds a container image tagged with the commit id, deploys to a staging environment with short-lived credentials, runs a smoke test and requires approval for production.",
)

LESSONS[21] = dict(   # Infrastructure as code
    minutes=16,
    hook="Imagine building a house by walking around with a hammer and improvising, and then being asked to build an identical second house next door. You cannot, because nobody wrote anything down. That is what clicking through a cloud console feels like after a few months. Nobody remembers which settings were changed, the test environment differs from production in ten invisible ways, and a lost server cannot be recreated. Infrastructure as code, or IaC, solves this by describing your cloud in text files that a tool reads and builds. The files live in Git, get reviewed like any code and can be run again to produce an identical environment. In this lesson you will learn how it works, write a first Terraform file, understand state and the plan and apply cycle, and learn safe habits.",
    sections=[
        ("Why write infrastructure down", """Clicking in a console is fine for learning. For anything that matters, IaC gives you:

- **Repeatability:** build the same environment again in minutes, in another region or account.
- **Consistency:** testing and production are made from the same code, so they stay alike.
- **History and review:** every change is a Git commit with an author, a reason and a reviewer.
- **Speed and safety:** no forgotten manual steps, and mistakes are caught in review before they reach production.
- **Documentation:** the code **is** the description of what exists.
- **Disaster recovery:** if an environment is lost, run the code and rebuild.

Tools: **Terraform** and **OpenTofu** (work across many providers), **AWS CloudFormation and CDK,** **Azure Bicep,** **Google Cloud Deployment Manager** and **Pulumi** (write infrastructure in a normal programming language). The ideas are the same in all of them."""),
        ("Declarative: describe what you want", """IaC is usually **declarative.** You describe the **end state,** and the tool works out the steps. In Terraform:

> [Terraform]
> terraform {
>   required_providers {
>     aws = { source = "hashicorp/aws" }       # pin a version, see the docs
>   }
> }
>
> provider "aws" {
>   region = "af-south-1"
> }
>
> variable "bucket_name" {
>   type = string
> }
>
> resource "aws_s3_bucket" "uploads" {
>   bucket = var.bucket_name
>   tags   = { project = "yaba-bakes", env = "staging" }
> }
>
> output "uploads_bucket" {
>   value = aws_s3_bucket.uploads.bucket
> }

A **provider** connects to a platform. A **resource** is a thing to create. **Variables** make the code reusable, and **outputs** report useful values. Provider versions change, so always check the current documentation for exact settings."""),
        ("Plan, review, apply", """The Terraform workflow has a safety step built in:

> [Terminal]
> terraform init                       # download providers
> terraform fmt                        # tidy the code
> terraform validate                   # check for mistakes
> terraform plan -var bucket_name=yaba-uploads-staging
> terraform apply -var bucket_name=yaba-uploads-staging
> terraform destroy -var bucket_name=yaba-uploads-staging

**`plan`** shows exactly what will be **created, changed or destroyed** before anything happens. **Read it carefully.** A plan that says “1 to destroy” on a database deserves a pause. **`apply`** makes the changes. **`destroy`** removes everything the code created, which is perfect for practice labs, and keeps your bill small. In a team, plans are produced automatically on a pull request and **reviewed,** and apply runs after approval."""),
        ("State: Terraform's memory", """Terraform records what it has built in a **state file.** It compares your code, the state and the real cloud to decide what to change. The state is vital and sensitive:

- **Never edit it by hand.** Use `terraform state` commands when you must.
- **Store it remotely** (an S3 bucket, Azure Storage, Terraform Cloud) so the team shares one copy, with **locking** so two people cannot apply at once.
- **Protect it:** state can contain **secrets** such as database passwords. Encrypt it, restrict access, and never commit it to Git.
- **Back it up** and turn on versioning.
- **Split state** by environment and by area (network, database, apps), so a mistake has a small reach.

**Drift** happens when someone changes the cloud by hand. A plan will show the difference. Decide whether to update the code to match, or let Terraform put things back, and discourage manual changes in production."""),
        ("Good habits and next steps", """Practices that keep IaC healthy:

1. **Keep everything in Git,** with pull requests and reviews.
2. **Use modules:** reusable packages such as a “web app network” you can call for each environment.
3. **One code base, several environments,** using variables for the differences (size, count).
4. **Tag every resource** with project, environment and owner, which helps with cost tracking.
5. **No secrets in code.** Read them from a secrets manager.
6. **Start small:** manage one area first, such as the network, and grow.
7. **Test and scan:** `terraform validate`, linters, and policy tools such as Checkov, tfsec or Open Policy Agent that block insecure settings like public buckets.
8. **Plan and apply from a pipeline** with least-privilege credentials.
9. **Import** existing resources into code gradually.
10. **Destroy practice environments** when you finish.

Infrastructure as code is one of the most valuable and best paid skills in cloud work."""),
    ],
    diagram=cycle([("Write", "describe it"), ("Plan", "preview"), ("Review", "teammate reads"), ("Apply", "build it"), ("Drift check", "compare")], "cl21", center="Infrastructure|in Git",
                  note="Never change production by hand."),
    caption="Write the code, plan, review, apply and watch for drift. The infrastructure lives in Git like any other code.",
    terms=[("Infrastructure as code", "Describing cloud resources in files that a tool turns into real infrastructure."), ("Declarative", "Describing the desired end state and letting the tool work out the steps."),
           ("Terraform plan", "A preview of the changes that an apply would make."), ("State file", "The record of what the tool has built, used to decide what to change."),
           ("Drift", "A difference between your code and what actually exists in the cloud."), ("Module", "A reusable package of infrastructure code.")],
    mistakes=["Running apply without reading the plan.", "Committing the state file or secrets to Git.", "Changing production by hand and creating drift.", "Keeping all infrastructure in one huge state file."],
    quiz=[dict(q="What does terraform plan do?", o=["Deletes everything", "Shows the changes that would be made, without making them", "Builds the app", "Encrypts the disk"], a=1,
               why="The plan lets you review changes before anything happens."),
          dict(q="Where should Terraform state be stored for a team?", o=["On one laptop", "In Git", "In remote storage with locking", "In an email"], a=2,
               why="Shared, locked remote state prevents conflicts and loss."),
          dict(q="What is drift?", o=["A fast network", "A kind of backup", "A new region", "A difference between your code and the real cloud"], a=3,
               why="Manual changes make the real environment differ from the code."),
          dict(q="Why is terraform destroy useful in practice labs?", o=["It removes everything the code created, which stops charges", "It speeds the network", "It hides logs", "It opens ports"], a=0,
               why="Removing practice resources avoids surprise bills.")],
    activity="Write Terraform for a private bucket with versioning and tags, run plan, apply and destroy, and store the state remotely. Then add a policy check that fails if a bucket is public.",
)

LESSONS[22] = dict(   # Monitoring, logging and backups
    minutes=16,
    hook="At 2 a.m. the site is down. Who finds out first, your monitoring or your customers? And if a mistake, a failed update or an attacker wipes your database, how much do you lose, an hour of data or a year? These two questions separate hobby projects from professional services. Monitoring and logging tell you what is happening and why. Backups and recovery plans decide what survives a disaster. You already know the basic ideas, including RTO and RPO. In this lesson you will go further, learning what to monitor and how to set alerts people will not ignore, how to read logs and traces, how to design backups that really restore and how recovery strategies trade cost against speed.",
    sections=[
        ("Observability: metrics, logs and traces", """Three kinds of signals describe a running system:

- **Metrics:** numbers over time, such as CPU, memory, requests per second, error rate and latency. Cheap, fast, ideal for dashboards and alerts.
- **Logs:** records of events with details, such as an error message or a request. Rich, and larger and costlier to keep.
- **Traces:** the path of one request through many services, showing where time was spent.

Cloud tools collect these automatically: Amazon CloudWatch, Azure Monitor, Google Cloud Monitoring and Logging, plus open tools such as Prometheus, Grafana and OpenTelemetry. The goal is **observability:** being able to ask a new question about the system and answer it from your data."""),
        ("What to measure and how to alert", """Watch what users feel, not only what machines do:

- **The four golden signals:** latency, traffic, errors and saturation (how full resources are).
- **User-facing checks:** a **synthetic monitor** that loads your site or logs in every minute from outside, and alerts when it fails.
- **Business metrics:** orders per hour and failed payments.

Define **SLIs and SLOs:** a **service level indicator** is a measurement, such as “the share of requests answered successfully in under 500 ms.” A **service level objective** is the target, such as 99.9% over 30 days. The gap is your **error budget.** Alert on **symptoms** (users are failing) more than on every cause (CPU is 80%). Good alerts are **actionable, urgent, and rare,** and include a link to a **runbook.** Too many alerts lead to alert fatigue and missed real problems."""),
        ("Logging that helps", """Logs are only useful if you can find the right line:

1. **Use structured logs** (JSON with fields such as time, level, request id, user id, message) so tools can filter and count.
2. **Include a request id** that travels through every service.
3. **Use levels sensibly:** debug, info, warning and error.
4. **Centralise logs** in one searchable place, instead of logging in to each server.
5. **Set retention:** keep detailed logs for a period such as 30 to 90 days, and archive important audit logs longer, since storage is billed.
6. **Protect privacy:** never log passwords, tokens or card data, and mask personal data. Logs of personal data fall under the **NDPA 2023** too.
7. **Keep audit logs** of who changed what in the cloud (CloudTrail, Activity Log), and protect them from tampering.

Learn a query language, such as CloudWatch Logs Insights or Kusto, since this saves hours during an incident."""),
        ("Backups that actually restore", """A backup you have never restored is only a hope. Follow these rules:

- **The 3-2-1 rule:** three copies, on two kinds of storage, with one stored elsewhere (another region or account).
- **Automate** backups, such as database snapshots and point-in-time recovery, and **file versioning.**
- **Protect backups from attackers:** store a copy in a **separate account** with restricted access, and use **immutable (write-once) storage** or object lock so ransomware cannot delete them.
- **Encrypt backups** and guard the keys separately.
- **Test restores regularly,** at least every quarter, and time them. Record the steps in a runbook.
- **Back up configuration too:** infrastructure code in Git, secrets in a vault, DNS records.
- **Set retention:** daily for a week, weekly for a month, monthly for a year, or as the law and business require.

Remember that **replication is not backup.** If you delete data, the copy deletes it too."""),
        ("Disaster recovery: cost versus speed", """**RPO** is how much data you can afford to lose, and **RTO** is how long you can afford to be down. The tighter the targets, the more it costs. Common strategies, from cheapest to most expensive:

1. **Backup and restore:** keep backups, rebuild with infrastructure code after a disaster. Slowest, cheapest. Hours of downtime.
2. **Pilot light:** a minimal copy of the core (such as the database) always running in another region, with the rest switched off until needed.
3. **Warm standby:** a smaller but fully working copy running all the time, scaled up in an emergency. Minutes of downtime.
4. **Active-active (multi-region):** several regions serving users at once. Nearly no downtime, highest cost and complexity.

Choose by asking what an hour of downtime really costs your business. **Rehearse** a failover, write the **incident roles,** and run a **post-incident review** after every real event, focused on learning."""),
    ],
    diagram=pyramid([("ACTIVE-ACTIVE", "near-zero downtime, highest cost"), ("WARM STANDBY", "minutes of downtime"), ("PILOT LIGHT", "core always running, rest on demand"), ("BACKUP AND RESTORE", "hours of downtime, lowest cost")], note="Faster recovery costs more."),
    caption="Four recovery strategies from backup and restore to active-active: the faster the recovery, the higher the cost.",
    terms=[("Observability", "The ability to understand what is happening inside a system from its data."), ("SLO", "A service level objective: the target for how reliable a service should be."),
           ("Error budget", "The amount of unreliability allowed by the SLO."), ("Synthetic monitor", "A scheduled test that behaves like a user to check a site from outside."),
           ("Immutable backup", "A backup that cannot be changed or deleted for a set time."), ("Pilot light", "A recovery setup with only the core running, scaled up when a disaster occurs.")],
    mistakes=["Never testing a restore.", "Alerting on every small blip until alerts are ignored.", "Keeping backups in the same account that an attacker could delete.", "Believing replication is the same as backup."],
    quiz=[dict(q="What is an SLO?", o=["A reliability target such as 99.9% of requests succeeding", "A server model", "A kind of cable", "A log file"], a=0,
               why="An SLO is the goal for how well the service should perform."),
          dict(q="Why is replication not a backup?", o=["It is slow", "A deletion or corruption is copied to the replica too", "It is illegal", "It costs nothing"], a=1,
               why="A backup keeps separate, earlier versions that survive mistakes."),
          dict(q="What does RTO measure?", o=["How much data you can lose", "How long you can be down", "The price", "The speed of the CPU"], a=1,
               why="Recovery time objective is the acceptable downtime."),
          dict(q="Which is the cheapest recovery strategy?", o=["Active-active", "Warm standby", "Backup and restore", "Pilot light with three regions"], a=2,
               why="Backup and restore costs least, with the slowest recovery.")],
    activity="Add monitoring to a practice app: a dashboard of the four golden signals, an alert with a runbook link and a synthetic check. Then take a database backup, restore it to a new instance, and time the restore.",
)

LESSONS[23] = dict(   # Cloud architecture patterns and design reviews
    minutes=16,
    hook="Anyone can launch a server. The skill that is valued, and well paid, is designing a whole system that is secure, reliable, fast and affordable, and being able to explain why it is built that way. Architects do not memorise answers. They know a small set of patterns, they ask good questions and they review designs for weak points before money is spent. Cloud providers publish frameworks for this, built around a handful of pillars. In this lesson you will learn those pillars, the most common architecture patterns, how to think through failure and cost, and how to run a design review that finds problems early, using the kind of case a Nigerian online business might bring you.",
    sections=[
        ("The pillars of a good design", """Major providers describe good architecture through similar pillars, such as the AWS Well-Architected Framework, Azure Well-Architected and Google's Architecture Framework:

- **Security:** protect data and systems, with least privilege, encryption and logging.
- **Reliability:** keep working when parts fail, and recover quickly.
- **Performance efficiency:** use resources well and meet speed needs.
- **Cost optimisation:** deliver the value for the lowest sensible cost.
- **Operational excellence:** run, monitor and improve the system with automation.
- **Sustainability:** use less energy and fewer resources.

Every design is a set of **trade-offs** between these. More reliability costs more. More security may slow development. A good architect makes the trade-offs **visible and deliberate,** and records the reasoning."""),
        ("Patterns you will meet again and again", """A short list of well-known patterns:

- **Three-tier web app:** load balancer, application servers, database, with a cache and storage. The standard starting point.
- **Serverless and event-driven:** functions, queues and managed services, scaling with demand and charging per use. Great for variable traffic.
- **Queue-based load levelling:** a queue between the front and slow back-end work to absorb spikes.
- **Cache-aside and CDN:** put copies of read-heavy data close to users.
- **Microservices:** several small independently deployed services. Powerful for large teams, and costly in complexity. **Start with a well-organised monolith,** and split only when you feel the pain.
- **Strangler fig:** migrate an old system piece by piece, by routing a growing share of traffic to new components.
- **Multi-region:** serve from several regions for resilience or global speed.
- **Backend for frontend / API gateway:** a tailored API layer for each kind of client.

Patterns are tools. Use the **simplest one that meets the requirements.**"""),
        ("Ask the failure questions", """The best way to test a design is to try to break it on paper. For each component, ask:

1. **What if it fails?** A server, a database, a whole availability zone, a region, a third-party API such as the payment provider.
2. **What if load jumps ten times?** During a sale, after a viral post, or on salary day.
3. **What if it is attacked?** Stolen credentials, a leaked key, a DDoS, a malicious upload.
4. **What if data is lost or corrupted?** How do we know, and how do we recover?
5. **What if someone makes a mistake?** A bad deployment, a deleted table, a wrong setting.
6. **What if the network is slow or fails** between components, or between users and the system?
7. **Where is the single point of failure?** Find it, then decide whether to remove it or accept it knowingly.

In Nigeria, also consider **power and connectivity** for offices, and the **latency** from users to the nearest region."""),
        ("Costs and sizing", """Estimate before you build:

- Use the provider's **pricing calculator,** with realistic numbers: users, requests, storage, data transfer.
- Include the **hidden costs:** data egress, NAT gateways, load balancers, logging and monitoring, backups, support plans, and people's time.
- **Start small and scale up,** and use auto scaling and serverless for variable load.
- Consider **commitment discounts** (reserved capacity, savings plans) only once usage is steady.
- **Right-size:** pick the smallest instance that meets the need, and review monthly.
- **Tag and track** costs per project and team.
- **Compare against alternatives,** including a simple platform for a small app.

A design that is perfect and unaffordable is not a good design. Costs are a requirement like any other, so write the budget at the top of the document."""),
        ("Running a design review", """A design review is a structured conversation that finds problems **before** they are built. A good format:

1. **State the problem and requirements:** users, features, expected load, uptime goal, budget, legal and data rules (including the NDPA 2023).
2. **Present the architecture** as a clear diagram, with data flows and trust boundaries.
3. **Explain the key decisions** and the alternatives you rejected. Many teams keep short **architecture decision records.**
4. **Walk through the failure, security and cost questions** above.
5. **Record risks and actions** with owners.
6. **Agree on how to validate:** a load test, a security review, a recovery drill.

Reviewers should be **curious and kind:** ask “what happens if…” and “why this and not that?” Authors should welcome the questions. A one-page design with a diagram, a risk list and a cost estimate is a powerful portfolio piece and a standard interview exercise."""),
    ],
    diagram=hub(("WELL-ARCHITECTED DESIGN", "trade-offs made visible"), [("Security", "least privilege, encryption"), ("Reliability", "survive failures"), ("Performance", "right-sized and fast"), ("Cost", "worth what it costs"), ("Operations", "automation and monitoring"), ("Sustainability", "less waste")],
                note="Every design balances these pillars."),
    caption="A well-architected design balances security, reliability, performance, cost, operations and sustainability.",
    terms=[("Well-Architected Framework", "A provider's set of pillars and questions for reviewing cloud designs."), ("Trade-off", "Gaining one quality, such as reliability, at the expense of another, such as cost."),
           ("Single point of failure", "A component whose failure stops the whole system."), ("Strangler fig", "A migration pattern that replaces an old system gradually."),
           ("Architecture decision record", "A short note explaining an important design decision and its reasons."), ("Right-sizing", "Choosing the smallest resource size that meets the need.")],
    mistakes=["Starting with microservices when a simple monolith would do.", "Ignoring hidden costs such as egress and NAT.", "Never asking what happens when a component fails.", "Presenting a design without stating the requirements."],
    quiz=[dict(q="What is a single point of failure?", o=["A part whose failure stops the whole system", "A fast server", "A backup", "A cheap plan"], a=0,
               why="If it fails, everything depends on it, so it must be removed or accepted knowingly."),
          dict(q="Which approach to microservices suits most beginners?", o=["Start with many microservices", "Start with a well-organised monolith and split later if needed", "Never use servers", "Use ten databases"], a=1,
               why="Microservices add complexity that small teams rarely need at first."),
          dict(q="Why record the alternatives you rejected?", o=["To fill pages", "So others understand the reasoning and trade-offs", "Rules require it", "To hide costs"], a=1,
               why="Decision records preserve the why behind a design."),
          dict(q="Which is a hidden cloud cost to include in an estimate?", o=["Data egress and NAT gateways", "The colour of the console", "The logo", "Nothing"], a=0,
               why="Transfer, networking and monitoring often surprise people.")],
    activity="Design and review an architecture for an online shop that expects 5,000 orders on a sale day. Draw it, write the requirements, answer the seven failure questions, estimate the cost and list the three biggest risks.",
)

LESSONS[24] = dict(   # Cloud careers and certification roadmap
    minutes=14,
    hook="Cloud skills are among the most portable and best paid in technology. A cloud engineer in Lagos can work for a local bank, a fintech, a telecom, a start-up, or remotely for a company on another continent, and the same knowledge applies in all of them. But the path is confusing: dozens of job titles, a forest of certifications and endless advice. In this lesson you will map the main roles, see how skills build on each other, learn what certifications are worth, plan a portfolio that proves what you can do and get honest guidance on finding work. No course can promise you a job, but a clear plan and visible work make a big difference.",
    sections=[
        ("The main cloud roles", """Cloud work has several paths, and they overlap:

- **Cloud engineer or administrator:** builds and runs cloud environments: networks, servers, storage, access.
- **DevOps or platform engineer:** automates deployment and infrastructure, builds pipelines and tools for developers.
- **Site reliability engineer (SRE):** keeps systems reliable, using monitoring, automation and incident response.
- **Solutions or cloud architect:** designs systems, reviews trade-offs, and talks to customers and teams.
- **Cloud security engineer:** protects cloud environments, identities and data.
- **Data or machine learning engineer:** builds data pipelines and platforms in the cloud.
- **FinOps specialist:** manages and optimises cloud spending.
- **Cloud support and technical account roles:** helping customers, a common entry route.

Entry roles often start in **IT support, system administration, software development or networking,** and grow from there."""),
        ("A skills ladder", """Build skills in layers:

1. **Foundations:** Linux and the command line, networking basics (IP, DNS, HTTP), Git, and one programming language, such as Python.
2. **One cloud platform:** compute, storage, networking, identity, databases and monitoring.
3. **Automation:** infrastructure as code (Terraform), scripting and CI/CD pipelines.
4. **Containers and orchestration:** Docker, then Kubernetes if your target roles ask for it.
5. **Security and reliability:** least privilege, encryption, logging, backups and incident handling.
6. **Cost and architecture:** pricing, design reviews and trade-offs.
7. **Soft skills:** writing clearly, explaining technical ideas, working in a team and learning continuously.

Depth in one platform plus solid fundamentals beats shallow knowledge of everything. You do not have to master it all before applying for a first role."""),
        ("Certifications: useful, with limits", """Certifications are exams that prove knowledge of a platform. They can **structure your learning** and help your CV get noticed, especially for your first cloud role. They are not a substitute for **hands-on experience.** Typical paths (names and codes change, so check the current lists):

- **AWS:** Cloud Practitioner (foundations), then Solutions Architect Associate, Developer Associate or SysOps/CloudOps Administrator, then Professional and specialty exams.
- **Microsoft Azure:** AZ-900 (fundamentals), then AZ-104 (administrator), AZ-204 (developer), AZ-305 (architect) and security tracks.
- **Google Cloud:** Cloud Digital Leader, Associate Cloud Engineer, then Professional exams.
- **Others:** HashiCorp Terraform Associate, Certified Kubernetes Administrator (CKA), and security certifications such as CompTIA Security+.

**Be careful with cost:** exam fees are paid in foreign currency, and some provide discounts, free vouchers or learning programmes. Use official free training first. Avoid “exam dump” sites. They break the rules, can get your certification cancelled, and teach you nothing."""),
        ("Build a portfolio that proves your skills", """Employers want evidence. Build three to five small projects, with a public repository and a clear README for each:

1. **A static website with a CDN, HTTPS and a custom domain,** built with infrastructure as code.
2. **A three-tier application** in a private network, with a managed database, a load balancer and auto scaling.
3. **A CI/CD pipeline** that tests, builds and deploys with short-lived credentials.
4. **A monitoring and alerting setup** with a dashboard and a documented recovery plan, including a tested restore.
5. **A cost and security review** of an example environment, with the problems you found and fixed.

For each, include an **architecture diagram, the cost, the security choices and what you would improve.** Write about your projects in short posts. Always **destroy** resources after demos and never publish keys or personal data. Your portfolio from this course can be the start."""),
        ("Finding work: realistic guidance", """Practical, honest advice:

- **Apply widely and prepare for interviews:** expect questions on networking, IAM, storage and scenarios such as “a website is slow, how do you investigate?”
- **Use your network:** community groups, meetups and developer events in Lagos and other cities, and online communities. Contribute, help others and ask for advice.
- **Consider routes in:** support roles, internships, junior sysadmin posts, freelance projects for small businesses, and open source contributions.
- **Remote work for international companies** is possible, but competition is strong, and you must show communication skills and reliability. Check that contracts, payments and taxes are handled legally, and beware of scams that ask you to pay to get a job or to receive and forward money.
- **Keep learning:** providers release new services constantly. Follow official blogs and release notes.
- **Be patient.** A first role can take months. Treat every rejection as feedback.

No one can guarantee employment, and salaries vary widely. A clear plan, visible projects and steady practice give you the best chance."""),
    ],
    diagram=timeline([("Foundations", "Linux, networking, Git"), ("One cloud", "learn it well"), ("First certificate", "optional, structured"), ("Portfolio", "3 to 5 projects"), ("Specialise", "DevOps, security, data"), ("Work", "apply, interview, grow")],
                     note="A roadmap, not a promise."),
    caption="Foundations, one cloud, a first certificate, a portfolio, a specialty and then work: a realistic roadmap.",
    terms=[("Cloud engineer", "A person who builds and runs cloud environments."), ("DevOps", "A way of working that joins development and operations through automation."),
           ("SRE", "Site reliability engineer: someone who keeps systems reliable using software and automation."), ("Certification", "An exam that proves knowledge of a platform or skill."),
           ("Portfolio", "A set of projects that show what you can build."), ("FinOps", "The practice of managing and optimising cloud costs.")],
    mistakes=["Collecting certificates without building anything.", "Using exam dump sites.", "Learning three clouds shallowly instead of one deeply.", "Leaving demo resources running and exposing keys in a public portfolio."],
    quiz=[dict(q="What matters most alongside certifications?", o=["Nothing", "Hands-on projects that prove your skills", "A long CV", "A fancy font"], a=1,
               why="Employers want evidence that you can build and operate real systems."),
          dict(q="Which role focuses on keeping systems reliable using monitoring and automation?", o=["SRE", "Graphic designer", "Receptionist", "Accountant"], a=0,
               why="Site reliability engineers specialise in reliability."),
          dict(q="Why avoid exam dump sites?", o=["They are free", "They break exam rules and teach you nothing", "They are too hard", "They are too short"], a=1,
               why="Cheating can get a certification cancelled and does not build real skill."),
          dict(q="What is a sensible plan for learning cloud?", o=["Learn all three clouds shallowly at once", "Build solid foundations, then one cloud deeply, with projects", "Only read blogs", "Wait to feel ready"], a=1,
               why="Depth in one platform plus fundamentals is the most effective base.")],
    activity="Write your own six-month cloud roadmap with the role you want, the foundations to learn, one cloud to master, three portfolio projects with dates and one optional certification, and share it with a mentor.",
)
