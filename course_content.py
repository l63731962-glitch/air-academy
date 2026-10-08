"""Deep lesson pages, quizzes (for CA and exams) and project templates.

A lesson page is: hook, sections [(heading, body)], diagram (SVG), terms, mistakes and quiz.
Body text: blank line = new paragraph, "- " = bullet, "1. " = numbered, "> " = example prompt box, **bold**.
Quiz answers ("a") are the 0-based index of the right option. They are only ever used on the server.
Lessons without a page here still show their short note card; add a page and it appears automatically.
"""

from diagrams import AR as _AR, COL as _COL, box as _box   # noqa: E402


_D1 = (f'<svg viewBox="0 0 640 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Your prompt goes into the AI model, which writes the output. Anything missing from the prompt becomes a guess.">{_AR.format(i="a1")}'
       '<g font-family="Sora,sans-serif" text-anchor="middle">'
       + _box(10, 30, 170, 80, "#00F0FF", "1. YOUR PROMPT", "The words you write", "#00F0FF")
       + _box(235, 30, 170, 80, "#8A2BE2", "2. THE AI MODEL", "Predicts a helpful reply", "#c79bff")
       + _box(460, 30, 170, 80, "#00F0FF", "3. THE OUTPUT", "The answer you get", "#00F0FF")
       + '<path d="M182 70H231" stroke="#8A93AD" stroke-width="2" marker-end="url(#a1)"/><path d="M407 70H456" stroke="#8A93AD" stroke-width="2" marker-end="url(#a1)"/>'
       '<path d="M320 112V128" stroke="#FFB86B" stroke-width="2" stroke-dasharray="4 4"/>'
       '<text x="320" y="150" fill="#FFB86B" font-size="13">Anything you leave out becomes a guess</text></g></svg>')

_BLOCKS = [("1 ROLE", "Who the AI is"), ("2 TASK", "The exact job"), ("3 CONTEXT", "Background, audience"), ("4 CONSTRAINTS", "Limits and rules"),
           ("5 FORMAT", "Shape of the answer"), ("6 EXAMPLES", "What good looks like"), ("7 QUALITY", "How it will be judged")]
_pos = [(10 + 160 * i, 14) for i in range(4)] + [(86 + 160 * i, 92) for i in range(3)]
_D2 = ('<svg viewBox="0 0 640 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The seven building blocks of a prompt: role, task, context, constraints, format, examples and quality criteria, leading to an output you can trust.">'
       f'{_AR.format(i="a2")}<g font-family="Sora,sans-serif" text-anchor="middle">'
       + "".join(_box(x, y, 148, 62, _COL[i % 3], t, s, _COL[i % 3] if i % 3 != 1 else "#c79bff") for i, ((x, y), (t, s)) in enumerate(zip(_pos, _BLOCKS)))
       + '<path d="M320 156V178" stroke="#8A93AD" stroke-width="2" marker-end="url(#a2)"/>'
       '<rect x="120" y="182" width="400" height="52" rx="16" fill="#00F0FF22" stroke="#00F0FF"/>'
       '<text x="320" y="214" fill="#E8ECF5" font-size="15" font-weight="700">An output you can trust and reuse</text></g></svg>')

CONTENT = {"prompt-engineering": {
    1: dict(
        minutes=12,
        hook="Imagine you walk up to a tailor in the market and say, “Sew me a shirt.” What do you get? Maybe the wrong size, the wrong cloth, the wrong style. Now say: “A short-sleeve shirt, plain blue cotton, chest size 42, two front pockets, ready by Friday.” Same tailor, completely different result. The tailor did not get smarter. You gave better instructions. That is the whole idea of this course, and this lesson shows you why it works.",
        sections=[
            ("What is a prompt?", """A **prompt** is the instruction you give an AI so it can do something for you. It can be a question (“What is inflation?”), a command (“Summarise this article”), or a longer brief with rules and examples. The reply the AI gives back is called the **output**.

The AI tools you may know, such as ChatGPT, Claude and Gemini, are built on **large language models**. A **model** is the program that reads your prompt and writes the output.

**Prompt engineering** is the skill of writing prompts so the output is useful, correct and in the shape you need, again and again, not just by luck."""),
            ("How the AI “reads” your words", """A language model has learned patterns from a huge amount of text. When you send a prompt, it writes the reply one small piece at a time, each time choosing a likely next piece that fits your words and the patterns it has learned.

Three facts follow from this, and they explain almost everything in this course:

- **It only knows what is in your prompt.** It cannot see your classroom, your business or your goal unless you say so.
- **Missing details get filled with guesses.** When you leave something out, the model fills the gap with the most typical answer, and typical answers are often generic.
- **It sounds confident even when it is wrong.** The model is built to write convincing text. That is not the same as checking facts, so you must verify important claims."""),
            ("See the difference: the tailor test", """Here are two prompts for the same job. First, the vague one:

> Write about farming.

The AI has to guess everything: how long, for whom, which crop, what angle, what tone. You will get a generic essay. Now a clear one:

> You are an agricultural extension officer in Nigeria. Write a 120-word explanation for smallholder maize farmers on why testing soil before planting saves money. Use simple English, no jargon, and end with one action they can take this week.

Look at what the second prompt added:

- **Who is speaking:** an agricultural extension officer
- **Who is listening:** smallholder maize farmers in Nigeria
- **What to do:** explain why soil testing saves money
- **Limits:** 120 words, simple English, no jargon
- **Ending:** one action for this week

Same AI. The second prompt leaves almost nothing to guesswork, so the output is far more likely to be useful on the first try. In the next lesson you will learn the proper names for these parts."""),
            ("Where prompt engineering is used", """- **Everyday work:** drafting emails, summarising reports, planning lessons, preparing for interviews.
- **Business:** customer-support replies, product descriptions, social media content, sorting customer feedback.
- **Software:** apps and automations that send prompts to an AI behind the scenes. Whoever writes those prompts decides how reliable the product is.
- **Learning:** asking for explanations at your level, practice questions and step-by-step examples.

You do not need to code to start. You need clear thinking and clear writing."""),
            ("Three habits to start today", """1. **Be specific.** Say who, what, how long and what style.
2. **Give context.** Tell the AI the situation and who will read the result.
3. **Check and improve.** Treat the first answer as a draft. Read it, spot what is missing, change your prompt and try again. Good prompters rarely stop at the first try.

One safety rule from day one: never paste passwords, bank details, national ID numbers or other people's private information into an AI chat."""),
        ],
        diagram=_D1, caption="Your words are all the AI has to work with. Whatever you leave out, it guesses.",
        terms=[("Prompt", "The instruction or question you give to an AI."), ("Output", "The reply the AI writes back."),
               ("Model", "The program that reads your prompt and writes the output (for example, a large language model)."),
               ("Context", "Background the AI cannot guess: the situation, the reader, your goal."),
               ("Iterate", "Improve a prompt step by step, using what the last answer got wrong."),
               ("Hallucination", "When an AI states something false as if it were true.")],
        mistakes=["Writing one short line and expecting the AI to read your mind.", "Asking for five different things in one prompt.",
                  "Copying the first answer without checking facts, names, numbers or dates.", "Pasting private information into a chat."],
        quiz=[dict(q="What is a prompt?", o=["The name of an AI company", "The instruction or question you give an AI", "The reply the AI writes", "A password for AI tools"], a=1,
                   why="A prompt is what you send to the AI. The reply is called the output."),
              dict(q="Why does “Write about farming.” usually give a weak result?", o=["AI cannot write about farming", "The prompt is too long", "It leaves out who, what and how, so the AI has to guess", "AI only works with questions"], a=2,
                   why="Missing details are filled with typical, generic guesses. A specific prompt leaves less to guess."),
              dict(q="Your first answer is close but not right. What should a good prompter do?", o=["Read it, spot what is missing and improve the prompt", "Accept it and move on", "Copy another AI's answer", "Send the same prompt again and hope"], a=0,
                   why="Treat the first answer as a draft, then adjust the prompt. This is called iterating."),
              dict(q="Which of these should you never paste into an AI chat?", o=["A maths question", "A recipe", "A draft email with no names", "Your passwords or ID numbers"], a=3,
                   why="Private details can be stored or exposed. Keep passwords, bank details and ID numbers out of AI chats.")],
    ),
    2: dict(
        minutes=14,
        hook="Think of the first day of a new assistant in your shop. You would not just say “help the customers.” You would explain who they are, what to do today, what is going on, the rules (“no discount above 10%”), how to report back, what a good job looks like, and how you will judge the work. A strong prompt does the same seven things. Each one is a building block, and once you know them you can write a good prompt for almost any job.",
        sections=[
            ("The seven blocks at a glance", """- **Role:** who the AI should act as.
- **Task:** the exact job to do.
- **Context:** background and audience.
- **Constraints:** limits and rules, such as length, tone and what to avoid.
- **Output format:** the shape of the answer, such as a list, table or email.
- **Examples:** a sample of what good looks like.
- **Quality criteria:** how the answer will be judged."""),
            ("Block by block", """**1. Role.** A role sets the point of view and the vocabulary. “You are a patient secondary-school maths teacher.” A role is not magic, but it nudges the AI toward the right level and style.

**2. Task.** Start with a strong verb: summarise, compare, rewrite, classify, explain, plan. One clear task per prompt works better than five.

**3. Context.** Facts the AI cannot guess: who the reader is, what has happened, what you already tried. “The reader is a first-time buyer with no technical background.”

**4. Constraints.** The fences around the answer: “Maximum 100 words. Friendly but professional. Do not mention prices.”

**5. Output format.** Say the shape: “Return a table with three columns: Problem, Cause, Fix.” or “Write it as a WhatsApp message.”

**6. Examples.** Show one or two samples of what you want. The AI copies the pattern. Lesson 5 goes deep on this.

**7. Quality criteria.** Tell the AI how you will judge the answer: “It must be accurate, include one real-life example and avoid jargon.” Now the AI can check its own work."""),
            ("All seven in one prompt", """Here is a full prompt for a phone-repair shop in Lagos. The labels are only there to show you the blocks.

> Role: You are a friendly customer-support agent for a phone-repair shop in Lagos.
> Task: Reply to the customer message below.
> Context: The customer's screen was repaired two days ago and has cracked again. Our policy gives a free re-repair within 7 days if the damage is not from a new drop.
> Constraints: Maximum 90 words. Warm, respectful tone. Do not promise a refund.
> Output format: A WhatsApp message with no subject line, signed “Tunde, FixIt Lagos”.
> Example of our tone: “Hello Mrs Bello, thanks for reaching out. We are glad to look at it again.”
> Quality criteria: Apologise once, explain the 7-day policy, and end with one clear next step.

You do not have to write the labels. Delete them and it still works as a normal paragraph. The labels simply help you check that you included each block."""),
            ("Do I need all seven every time?", """No. A quick personal question may need only a task and some context. Important work, such as customer replies, reports, or anything an app will repeat thousands of times, deserves more blocks.

A good rule: the more it matters, and the more often it will be used, the more blocks you add.

Before you press send, ask yourself:

1. Did I say who the AI is and what the job is?
2. Did I say who the answer is for and what is going on?
3. Did I set limits and the shape of the answer?
4. Did I show or describe what good looks like?"""),
        ],
        diagram=_D2, caption="Seven blocks. Use the ones the job needs, and add more when the work really matters.",
        terms=[("Role", "Who the AI should act as."), ("Task", "The exact job you want done."), ("Constraint", "A limit or rule the answer must respect."),
               ("Output format", "The shape of the answer: list, table, email, JSON and so on."),
               ("Example", "A sample of the style or pattern you want the AI to follow."),
               ("Quality criteria", "The checklist you will use to judge the answer.")],
        mistakes=["Stacking several tasks in one prompt (“write it, translate it and design a poster”). Split them up.", "Giving a role but no task.",
                  "Writing constraints that fight each other (“very detailed, in 20 words”).", "Forgetting the audience, so the tone comes out wrong."],
        quiz=[dict(q="Which building block tells the AI who to act as?", o=["Context", "Output format", "Role", "Quality criteria"], a=2,
                   why="The role sets the point of view, for example “You are a patient maths teacher.”"),
              dict(q="“Maximum 100 words, friendly tone, do not mention prices” belongs to which block?", o=["Examples", "Constraints", "Task", "Role"], a=1,
                   why="Limits and rules on the answer are constraints."),
              dict(q="You want every product description to match one style. Which block helps most?", o=["A longer task", "A different role", "Shorter constraints", "An example of the style you want"], a=3,
                   why="The AI copies patterns, so a good example is the strongest way to fix a style."),
              dict(q="Do you need all seven blocks in every prompt?", o=["Yes, always", "No. Use the blocks the job needs and add more for important or repeated work", "Only role and task are ever needed", "Only when coding"], a=1,
                   why="Quick questions need little. Important or repeated work deserves more blocks.")],
    ),
}}

THEMES = ["School", "Church", "Farm", "Clinic", "Fintech startup", "Online market", "Logistics company", "Football club"]

KINDS = {
    "prompt-engineering": dict(name="Prompt Toolkit", need="a reusable set of AI prompts its staff can use every day",
        out=["A prompt library of 5 to 8 tested prompts", "A one-page guide on when to use each prompt", "A test log with before-and-after results"],
        req=["Write 3 prompts that each use at least four of the seven building blocks.", "Test every prompt on at least three different inputs and record the results.",
             "Add a short how-to-use note for a non-technical colleague.", "Create one prompt that always returns a table or JSON.",
             "Add an example and a quality checklist to two prompts.", "Record three failures and show how you fixed each one.",
             "Add a safety note about private data and fact-checking."]),
    "animation": dict(name="Animated Story Clip", need="a short animated clip that explains one idea to its audience",
        out=["Script and storyboard", "A finished clip of 20 to 60 seconds", "A one-page making-of note"],
        req=["Write a one-sentence story idea and a 6-panel storyboard.", "Design one main character and draw it from three angles.",
             "Animate one clear action (walk, jump or wave) with smooth timing.", "Add music or sound effects at the right volume.",
             "Use at least two camera shots or moves.", "Add a title card and an end card.", "Export two versions: one for WhatsApp and one for YouTube."]),
    "cloud-computing": dict(name="Cloud Launchpad", need="its small web app moved onto the cloud safely and cheaply",
        out=["A deployed app with a public link", "An architecture diagram", "A one-page cost estimate"],
        req=["Deploy a simple app on a cloud provider's free or trial tier.", "Store files in object storage.", "Create a limited-permission user instead of using the root account.",
             "Turn on multi-factor authentication.", "Set a budget alert.", "Add monitoring and one alert.", "Write a recovery plan for when the app goes down."]),
    "web-development": dict(name="Website", need="a fast, mobile-friendly website that wins it more customers",
        out=["A live website link", "The code on GitHub", "A short case study"],
        req=["Build a home page and two more pages with semantic HTML.", "Make it work on phone, tablet and laptop.", "Add a contact or booking form with validation.",
             "Use JavaScript for one interactive feature.", "Meet accessibility basics: contrast, alt text and keyboard use.", "Deploy it with HTTPS.",
             "Score 90 or more on a Lighthouse check, or explain what holds it back."]),
    "app-development": dict(name="Mobile App", need="a simple mobile app its customers can use every day",
        out=["A working app (APK or web build)", "Screen designs", "A test report"],
        req=["Design 5 screens and the paths between them.", "Build the main screen and navigation.", "Show live or saved data in a list.", "Handle loading and error states.",
             "Add sign-in or a protected screen.", "Test on a real phone with 3 people and record the problems.", "Prepare a store listing with an icon and screenshots."]),
    "full-stack": dict(name="Full-Stack App", need="a complete system where users log in, save data and see it later",
        out=["A deployed app", "API documentation", "A README with setup steps"],
        req=["Design a database with at least two related tables.", "Build create, read, update and delete endpoints.", "Build the screens that call them.",
             "Add login and make some data private to each user.", "Write at least five automated tests.", "Deploy with environment variables for secrets.", "Add logging and one error alert."]),
    "agentic-ai": dict(name="AI Agent", need="an AI assistant that completes a real task using tools",
        out=["A working agent", "A test set of 10 cases with scores", "A safety and approval plan"],
        req=["Define the agent's single job and when it must stop.", "Write a system prompt with clear rules and a JSON output format.", "Give it two tools and describe each clearly.",
             "Add simple memory for one fact.", "Add a step limit and a human approval step for risky actions.", "Evaluate it on 10 test cases and record the score.",
             "Try a prompt-injection attack and add a guardrail."]),
    "game-development": dict(name="Playable Game", need="a small game its community can play and share",
        out=["A playable build", "A short design document", "A trailer or screenshots"],
        req=["Define the core loop in one sentence.", "Make the player move and interact.", "Add scoring and a win or lose rule.", "Add one enemy or obstacle.",
             "Add a menu, sound effects and visual feedback.", "Playtest with three people and fix the top three problems.", "Publish the build with a game page."]),
}
STEPS = ["Read the brief and write down who will use your work.", "Plan: list the tasks and decide what you will build first.", "Build the smallest working version.",
         "Test it with at least two real people.", "Improve it using their feedback.", "Present it: show the result and explain one decision you made."]
RUBRIC = [("Meets the brief", 30), ("Quality of the work", 25), ("Testing and improvement", 20), ("Documentation", 15), ("Presentation", 10)]

from lessons_prompt_engineering import LESSONS as _PE   # noqa: E402  lessons 3 to 8
CONTENT["prompt-engineering"].update(_PE)