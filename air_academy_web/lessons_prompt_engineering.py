"""AI Prompt Engineering: deep lesson pages 3 to 8 (lessons 1 and 2 live in course_content.py).
Same format as there: hook, sections, diagram, terms, mistakes, quiz. Quiz "a" = index of the right option."""
from diagrams import flow, formats

LESSONS = {
    3: dict(
        minutes=13,
        hook="Ask three different people the same question: “How do I save money?” A banker, a market trader and a secondary-school teacher will each answer differently. Not because one is smarter, but because of who they are and who they think they are talking to. The AI works the same way. In this lesson you will learn to decide who is speaking, what the job is, and what the AI needs to know about the situation.",
        sections=[
            ("Role: choosing who is speaking", """A **role** tells the AI whose point of view to take. It changes the vocabulary, the level of detail and what the answer focuses on.

A weak role is just a title: “You are an expert.” An expert in what? Talking to whom? A strong role has a job and an audience:

> You are a Nigerian secondary-school chemistry teacher preparing students for their final exams.

Three tips for roles:

- **Give the role a real job and a reader.** “A patient maths tutor for 12-year-olds” works better than “a genius”.
- **Match the role to the result you want.** A lawyer's tone and a friend's tone are very different.
- **Remember the limit.** A role changes style and focus. It does not make the facts true, so you still check important claims."""),
            ("Task: one clear job", """The **task** is the exact thing you want done. Start with a strong verb: summarise, compare, rewrite, classify, explain, plan, translate, brainstorm.

Compare these two:

> Help me with my business.

> List five low-cost ways a new hair salon in Surulere can attract customers in its first month.

The second one has a clear finish line: you can see when it is done. If you have several jobs, do not squeeze them into one prompt. Chain them: first brainstorm ideas, then pick the best two, then write the message. Each step gets its own prompt, and the result of one feeds the next."""),
            ("Context: what the AI cannot guess", """**Context** is everything the AI would otherwise have to guess. Five questions find most of it:

1. **Who** will read or use the answer?
2. **What** is the situation, and what has already happened?
3. **Why** do you need it, and what is the goal?
4. **What** have you already tried or decided?
5. **Which facts** must the answer use?

That last one matters a lot. If you want the AI to use your own facts, such as your price list, your school rules or your meeting notes, **paste them into the prompt**. This is called giving **source material**. The AI cannot read your files or your mind unless you share the text."""),
            ("Putting the three together", """Start with a lazy prompt:

> Help me with my CV.

Now add a role, a task and context:

> You are a career coach who helps Nigerian graduates get their first job. Rewrite the three CV bullet points below so each one shows a result. I am applying for a junior data analyst job at a bank. I studied Statistics and did a six-month internship at a retail company. Keep each bullet under 20 words.

The second prompt tells the AI who is helping, what to do, who the CV is for and what background to use. The answer will be far more useful because almost nothing is left to guesswork."""),
            ("The ten-second test", """Before you press send, imagine handing your prompt to a smart stranger who knows nothing about you. **Could they do the job without asking you a single question?**

If they would ask “For whom?” or “How long?” or “What do you mean?”, then the AI will have to guess those answers too. Add them to the prompt. This one habit fixes more weak prompts than any trick."""),
        ],
        diagram=flow([("ROLE", "Who is speaking"), ("TASK", "What to do"), ("CONTEXT", "Why and for whom"), ("ANSWER", "Focused and useful")], "a3", "Role, task and context together leave almost nothing to guess"),
        caption="Three short pieces of information turn a vague request into a focused one.",
        terms=[("Role", "The point of view you ask the AI to take."), ("Task", "The exact job to be done, started with a strong verb."), ("Context", "Background the AI cannot guess: situation, reader, goal."),
               ("Audience", "The person who will read or use the answer."), ("Source material", "Text you paste in so the AI uses your facts, not guesses.")],
        mistakes=["Using a vague role such as “expert” with no job or audience.", "Hiding the real task in the middle of a long story.", "Assuming the AI knows your company, school or city.", "Expecting the AI to use facts you never gave it."],
        quiz=[dict(q="Why give the AI a role?", o=["It unlocks secret features", "It sets the point of view, vocabulary and level of the answer", "It makes every fact correct", "It makes the reply longer"], a=1,
                   why="A role shapes style and focus. It does not make facts true."),
              dict(q="Which task is the strongest?", o=["Help me with my business", "Tell me about marketing", "List five low-cost ways a new hair salon can attract customers in its first month", "Something about salons"], a=2,
                   why="It has a strong verb, a clear subject and a visible finish line."),
              dict(q="You want the AI to use your own price list. What should you do?", o=["Hope it already knows it", "Paste the price list into the prompt", "Only write “use my prices”", "Give it a role"], a=1,
                   why="The AI cannot see your files. Paste the text in as source material."),
              dict(q="What is the ten-second test?", o=["Keep the prompt under ten words", "Wait ten seconds before sending", "Send the prompt ten times", "Ask whether a smart stranger could do the job without asking you questions"], a=3,
                   why="Anything the stranger would ask about is something the AI would otherwise guess.")],
    ),
    4: dict(
        minutes=13,
        hook="When you order food, the menu gives you choices: small or large, with pepper or without, eat here or take away. If you just say “food”, you get whatever the cook decides. A prompt without limits and a format is the same. Constraints and output formats are your menu choices. They decide how long the answer is, how it sounds and what shape it takes.",
        sections=[
            ("Constraints: the fences around the answer", """A **constraint** is a limit or rule the answer must respect. The most useful kinds:

- **Length:** “at most five bullet points”, “three short paragraphs”.
- **Tone:** formal, friendly, calm, encouraging.
- **Reading level:** “simple English a 15-year-old can follow”.
- **Scope:** “use only the text below”, “do not mention prices”.
- **Must include or avoid:** “include one real example”, “no jargon”.

Two practical notes. First, say what **to do** as well as what to avoid: “use plain words” is clearer than only “no jargon”. Second, models follow structure limits such as “five bullet points” more reliably than exact word counts, which they only follow roughly. If the count really matters, check it yourself."""),
            ("Output format: choosing the shape", """The **output format** is the shape of the answer. Pick the shape that fits where the answer will be used.

- **Paragraph:** for explanations and stories.
- **Bullet list or numbered steps:** for quick reading and instructions.
- **Table:** for comparing options side by side.
- **Message or email:** with greeting, body and sign-off.
- **JSON:** for apps and automations, because a program can read it reliably.

Here is a table request:

> Compare solar panels and a petrol generator for a small shop. Return a table with these columns: Option, Upfront cost, Running cost, Noise, Best for. Under the table, add a one-sentence recommendation.

And here is a JSON request that an app could use:

> Read the customer message below and return JSON only, with the keys name, problem and urgency (low, medium or high). Do not add any other text."""),
            ("Why “JSON only” matters", """**JSON** is a way of writing information so programs can read it: names and values inside curly braces. When an app asks the AI for a reply, the app cannot guess what to do with a friendly paragraph. It needs predictable text.

That is why app builders add lines like “return JSON only” and “do not add any other text”. Prompt engineering is not only for chatting. It is also how developers make AI behave like a reliable part of a product."""),
            ("Before and after", """Before:

> Explain inflation.

After:

> Explain inflation to a 15-year-old in Nigeria, using the price of garri as the example. Use at most 120 words and simple English. End with one question that checks understanding.

The second prompt sets the audience, an example, a length limit, a reading level and an ending. The answer will be shorter, clearer and easier to use in a class."""),
            ("When limits clash, say which one wins", """Sometimes two limits pull against each other: “very detailed, but only 20 words”. The AI will compromise in a way you did not choose. Say which limit wins:

> Be as detailed as possible, but if you must choose, stay under 100 words.

Finally, format for where the answer will live. WhatsApp needs short lines and no tables. An email needs a subject and a greeting. A spreadsheet needs a table. A slide needs three bullets."""),
        ],
        diagram=formats(), caption="Same facts, four shapes. Choose the one that fits where the answer will be used.",
        terms=[("Constraint", "A limit or rule the answer must respect."), ("Tone", "How the answer sounds: formal, friendly, calm and so on."),
               ("Output format", "The shape of the answer: paragraph, list, table, message or JSON."),
               ("JSON", "A way of writing information, in names and values inside curly braces, that programs can read."), ("Scope", "What the AI may and may not use or talk about.")],
        mistakes=["Asking for an exact word count and trusting it without checking.", "Giving limits that fight each other, such as “very detailed in 20 words”.", "Forgetting to name the format, then fighting messy text in a spreadsheet.",
                  "Only saying what to avoid and never what to do."],
        quiz=[dict(q="Which instruction do models follow most reliably?", o=["Write exactly 143 words", "Be perfect", "Use at most five bullet points", "Make it nice"], a=2,
                   why="Clear structure limits work better than exact word counts, which models only follow roughly."),
              dict(q="Why ask for JSON when an app will use the reply?", o=["JSON is always shorter", "The AI only understands JSON", "JSON makes the answer more polite", "A program can read a predictable structure far more easily than free text"], a=3,
                   why="Apps need predictable text. A friendly paragraph is hard for a program to process."),
              dict(q="“Be very detailed, but use only 20 words.” This is an example of:", o=["A good constraint", "Clashing constraints", "An output format", "A role"], a=1,
                   why="The two limits pull against each other. Say which one wins."),
              dict(q="Your reply will be sent on WhatsApp. Which format instruction fits best?", o=["A table with five columns", "A formal letter with headings", "JSON only", "Short lines in a friendly tone, with no tables"], a=3,
                   why="Format for where the answer will live. WhatsApp suits short, simple lines.")],
    ),
    5: dict(
        minutes=14,
        hook="A new cook watches you make jollof rice once and copies your style better than any long explanation could describe. Showing beats telling. In this lesson you will teach the AI by example, and give it a checklist so it can mark its own work before you ever see it.",
        sections=[
            ("Why examples work", """Language models are pattern followers. An example shows tone, length and structure, which are hard to describe in words but easy to copy.

You will meet three names:

- **Zero-shot:** no examples, only instructions.
- **One-shot:** one example.
- **Few-shot:** two to five examples.

Zero-shot is fine for simple tasks. When the style or format really matters, add examples."""),
            ("How to write a good example", """Show pairs: an input and the answer you want. Then end with the new input and leave the answer blank, so the AI continues the pattern.

> Classify each customer message as Positive, Neutral or Negative.
> Message: “The delivery came a day early, thank you!” → Positive
> Message: “I am still waiting for my refund.” → Negative
> Message: “Please send me your opening hours.” → Neutral
> Message: “The app keeps crashing since the update.” →

The AI sees the pattern and completes the last line (Negative). Notice that the examples use the same layout every time. Consistent format in the examples gives consistent format in the answer."""),
            ("Choose examples carefully", """- **Cover different cases.** If every example is positive, the AI leans positive.
- **Include a tricky case.** One edge case teaches the AI how to handle awkward inputs.
- **Keep them correct and consistent.** A wrong example teaches a wrong habit.
- **Do not make them too similar.** If all examples have the same length and words, the AI may copy them too closely.
- **Two to five is usually enough.**
- **Use made-up or anonymised data** in examples. Never put real customers' private details in a prompt."""),
            ("Quality criteria: a checklist the answer must pass", """**Quality criteria** tell the AI how you will judge the answer. You write them as a short checklist and ask the AI to check its work before showing you:

> Write the reply to the customer. Before you show it, check it against this list and fix anything that fails: 1. Under 90 words. 2. Apologises once. 3. States the 7-day policy. 4. Ends with one clear next step. Show only the final reply.

This does two good things. The AI can fix its own mistakes, and you get a ready-made list to check the result yourself. Remember, the AI checking its own work helps but is not a guarantee. You still read the answer."""),
            ("Which tool for which job?", """- **Simple task:** instructions alone (zero-shot).
- **Style or format matters:** add one to three examples.
- **Quality must be consistent:** add a checklist of criteria.
- **Important and repeated work:** use examples and criteria together."""),
        ],
        diagram=flow([("ZERO-SHOT", "No examples"), ("ONE-SHOT", "One example"), ("FEW-SHOT", "Two to five|examples"), ("+ CHECKLIST", "AI marks|its own work")], "a5", "More guidance usually means a more predictable answer"),
        caption="Examples show the pattern. A checklist shows the standard.",
        terms=[("Zero-shot", "A prompt with instructions only and no examples."), ("One-shot", "A prompt with one example."), ("Few-shot", "A prompt with two to five examples."),
               ("Quality criteria", "The checklist you will use to judge the answer."), ("Edge case", "An unusual or tricky input that tests whether the prompt really works.")],
        mistakes=["Giving only perfect, very similar examples, so the AI copies them too closely.", "Mixing different layouts between examples.", "Putting real customers' names or private data inside examples.",
                  "Trusting the AI's own check and not reading the result yourself."],
        quiz=[dict(q="A prompt with instructions only and no examples is called:", o=["Few-shot", "Zero-shot", "One-shot", "Many-shot"], a=1, why="Zero examples means zero-shot."),
              dict(q="Why include an edge case among your examples?", o=["To confuse the AI", "Because examples must be long", "It teaches the AI how to handle tricky inputs", "Edge cases are always wrong"], a=2,
                   why="A tricky example shows how to behave when the input is awkward."),
              dict(q="What goes at the end of a few-shot prompt?", o=["The new input, with the answer left blank for the AI to complete", "The answer to the new input", "A thank-you message", "A different task"], a=0,
                   why="Ending with the new input lets the AI continue the pattern you set."),
              dict(q="What is the purpose of quality criteria?", o=["To make the prompt shorter", "To guarantee the answer is always correct", "To replace your own reading of the result", "To tell the AI how you will judge the answer so it can check its own work"], a=3,
                   why="A checklist helps the AI revise, and helps you review. It is not a guarantee.")],
    ),
    6: dict(
        minutes=13,
        hook="A baker does not bake one loaf, declare the recipe perfect and sell it to the whole street. She bakes, tastes, adjusts the salt and bakes again. A prompt is a recipe. If it will be used again and again, you must test it on more than one input, and improve it step by step.",
        sections=[
            ("One good answer is not proof", """AI replies can change from one run to the next, and a prompt that works on one input may fail on another. One lucky answer proves nothing.

The fix is a small **test set**: about five inputs that cover different situations.

- A **typical** input
- A **short** one
- A **long** one
- A **messy** one, with typing mistakes or unclear wording
- A **tricky** one, the kind that could break your prompt

If your prompt handles all five, you can trust it much more."""),
            ("The improve loop", """Improving a prompt is a loop you repeat:

1. **Run** the prompt on every input in your test set.
2. **Mark** each result pass or fail against your quality checklist.
3. **Find the pattern** in what failed.
4. **Change one thing** in the prompt.
5. **Run again** and compare.

Why only one change? If you change five things and the result improves, you will not know which change helped. If it gets worse, you will not know which one hurt."""),
            ("Reading failures: what to change", """- **Too long:** add a length limit.
- **Wrong tone:** add a role and audience, or a short example of the tone.
- **Missing facts:** add context, or paste the source text.
- **Wrong format:** name the format and show a small example.
- **Makes things up:** tell it to use only the text you provided and to say “I do not know” when the answer is not there.
- **Ignores a rule:** put the important rules in a short numbered list so they stand out."""),
            ("Keep a prompt log", """A **prompt log** records what you changed and what happened. It saves you from repeating old mistakes.

- Version 1: basic prompt. Score 2 of 5. Replies are too long.
- Version 2: added “at most 90 words”. Score 3 of 5. Tone is too cold.
- Version 3: added a role and one example of the tone. Score 5 of 5.

Now you can show exactly why version 3 is better than version 1."""),
            ("Know when to stop", """Stop when your prompt passes the whole test set consistently and extra tweaks stop making a difference. Then keep two habits:

- **Re-test when anything changes:** a new AI model, a new kind of input or an edited prompt. A **regression** is when a change fixes one problem but breaks something that used to work.
- **Keep a human check** for anything important. Testing makes a prompt reliable, not perfect."""),
        ],
        diagram=flow([("RUN", "On your|test set"), ("MARK", "Pass or fail"), ("FIND", "The pattern|in failures"), ("CHANGE", "Only one|thing")], "a6", "Repeat until your whole test set passes", loop=True),
        caption="Good prompts are built in loops, not in one go.",
        terms=[("Test set", "A small group of varied inputs used to check a prompt."), ("Iteration", "One round of run, mark, change and run again."),
               ("Prompt log", "A record of each version, what changed and how it scored."), ("Regression", "A change that fixes one problem but breaks something that used to work."),
               ("Pass or fail", "Whether a result meets your quality checklist.")],
        mistakes=["Judging a prompt by one lucky answer.", "Changing five things at once, so you cannot tell what helped.", "Testing only easy inputs.", "Forgetting to re-test after you edit the prompt."],
        quiz=[dict(q="Why test a prompt on several inputs?", o=["To use more of the AI", "Because the AI gets tired", "One good answer may be luck, and different inputs reveal weak spots", "Because five is a rule of law"], a=2,
                   why="A prompt must work across varied inputs, not just one."),
              dict(q="What is the best way to improve a prompt that fails?", o=["Rewrite everything", "Change one thing, then test again", "Change five things at once", "Switch AI tools every time"], a=1,
                   why="One change at a time shows you what actually helped."),
              dict(q="The replies are too long. Which change fits best?", o=["Add a length limit such as at most 90 words", "Add a role", "Paste more context", "Remove the task"], a=0,
                   why="Match the fix to the failure. Too long means add a length limit."),
              dict(q="What is a regression?", o=["A longer prompt", "A type of output format", "A smarter model", "A change that fixes one problem but breaks something that used to work"], a=3,
                   why="That is why you re-test the whole test set after every change.")],
    ),
    7: dict(
        minutes=15,
        hook="A lab is a place to try things, get them wrong safely and learn fast. This lesson is a guided workout, not a lecture. You will practise on three real tasks against the clock, then swap prompts with a classmate. Everything you need comes from lessons 1 to 6.",
        sections=[
            ("How a lab round works", """Each task runs in three short rounds, about ten minutes in total:

1. **Draft and run (4 minutes).** Write your prompt using the building blocks and run it.
2. **Mark and fix (3 minutes).** Check the result against the task checklist. Change one thing.
3. **Test (3 minutes).** Run the improved prompt on two more inputs.

Save your best version and a note on what changed in your prompt library."""),
            ("Task A: a study plan", """**Scenario:** A student has six weeks before an important exam and can study three hours each evening. Write a prompt that produces a realistic week-by-week study plan.

**Checklist:**

- The plan fits the time available
- It includes revision and rest
- It is a table
- It has no more than eight rows

**Hint:** give the AI the subjects, the weak areas and the daily hours. It cannot guess them."""),
            ("Task B: product descriptions", """**Scenario:** A small online shop sells handmade soap. Write a prompt that creates product descriptions in one consistent style from a product name and two details.

**Checklist:**

- Under 60 words
- One clear benefit and one concrete detail
- A short call to action
- No health claims you cannot prove

**Hint:** include one example description. This is the best moment to use few-shot prompting. Watch the last item: AI loves to overpromise, and false health claims can mislead customers."""),
            ("Task C: a customer reply", """**Scenario:** A customer's delivery is three days late and they are upset. Write a prompt that produces a calm WhatsApp reply.

**Checklist:**

- Apologises once
- Explains the next step
- Promises nothing the business cannot do
- Short lines, friendly tone

**Hint:** use all seven building blocks, then test on a second angry message and a polite one."""),
            ("Peer review: giving feedback that helps", """Swap prompts with a classmate. Run **their prompt on your input** and **yours on theirs**. Then give feedback in three parts:

1. **What worked:** one specific thing.
2. **What failed:** name the input and the problem. “On input 2 the reply ignored the 60-word limit.”
3. **One change to try:** “Put the limit in a numbered rule.”

Be kind and specific. “It is good” and “I do not like it” help nobody. Finish by saving your best prompts, with their logs, into your library."""),
        ],
        diagram=flow([("PICK", "A task"), ("DRAFT", "Use the|blocks"), ("RUN", "On three|inputs"), ("FIX", "One change|at a time"), ("SWAP", "Peer|review")], "a7", "Short rounds, honest marking, one change at a time"),
        caption="The lab is a loop of draft, test, fix and share.",
        terms=[("Lab round", "A short timed cycle of draft, run, mark and fix."), ("Peer review", "Testing and giving feedback on a classmate's prompt."),
               ("Prompt library", "Your saved collection of tested prompts and notes."), ("Task checklist", "The pass-or-fail list for one task.")],
        mistakes=["Spending the whole time on the first draft.", "Changing many things between rounds.", "Giving vague feedback such as “it is good”.", "Letting the AI invent health or money claims in product text and posting them unchecked."],
        quiz=[dict(q="In a lab round, what should you do after your first draft?", o=["Change one thing, run it, and mark the result against your checklist", "Write the longest prompt you can", "Skip testing", "Copy a classmate's final answer"], a=0,
                   why="Short loops of one change and one test teach you the fastest."),
              dict(q="Which peer feedback is most useful?", o=["It is good", "I do not like it", "On input 2 the reply ignored the 60-word limit. Try putting the limit in a numbered rule", "Try harder"], a=2,
                   why="Good feedback names the input, the problem and one change to try."),
              dict(q="A product description says “cures skin disease”. What should you do?", o=["Post it, it sounds strong", "Remove or rephrase unsupported health claims and check the facts", "Make it longer", "Ask the AI to repeat it"], a=1,
                   why="AI can overpromise. You are responsible for what you publish."),
              dict(q="Where should your best prompts end up?", o=["In your head only", "In a chat you will never find again", "Deleted after use", "In your prompt library, with notes on what changed and how it scored"], a=3,
                   why="A library with a log lets you and others reuse proven prompts.")],
    ),
    8: dict(
        minutes=15,
        hook="Everything you have learned comes together here. You will build something other people can use: a reusable prompt template, which is a prompt with blanks that anyone can fill in. Think of a school-fees reminder that works for every parent by changing only the name, class and amount.",
        sections=[
            ("What is a prompt template?", """A **prompt template** is a prompt with fixed instructions and **variables**: blanks written in brackets that change each time.

> Role: You are a friendly accounts officer at [SCHOOL NAME].
> Task: Write a reminder message to a parent.
> Context: Student: [STUDENT NAME], class [CLASS]. Outstanding fees: [AMOUNT], due on [DATE].
> Constraints: Maximum 80 words. Polite, never threatening. Do not mention other families.
> Output format: A WhatsApp message signed “[SCHOOL NAME] Accounts”.

Fill the blanks and run it. Every parent gets a consistent, polite message, and a new staff member can use it on day one. This is also how developers store prompts inside apps."""),
            ("Choose a real use case", """A good template solves a task that:

- **Repeats** often, with only some details changing
- Has a **clear user**
- Has a **clear success test**

Ideas: fee reminders for a school, order confirmations for a shop, weekly newsletters for a church, price updates for a farm, appointment reminders for a clinic, proposal replies for a freelancer.

Open **Project Studio** from your dashboard, choose this course and a theme, and you will get a full project brief to follow."""),
            ("Build it in five steps", """1. **Write a prompt** that works for one real case.
2. **Replace the parts that change** with [BRACKETS].
3. **Add an example and a checklist** (lesson 5).
4. **Test it on five different inputs** (lesson 6).
5. **Write a how-to-use note** so anyone can use it."""),
            ("The how-to-use note", """A template nobody understands is a template nobody uses. Your note should say:

- **What it is for** and who should use it
- **The blanks** to fill in, with one filled-in example
- **One warning:** check facts, and never put private details in
- **When not to use it**"""),
            ("Present your work", """Give a three-minute demo:

1. The problem you solved
2. Your template
3. A live run on two different inputs
4. Your test log
5. One thing you learned

Your project is marked on five things: **meets the brief (30), quality of the work (25), testing and improvement (20), documentation (15) and presentation (10).** The Project Studio brief shows the same marking guide, so you always know what a strong project looks like."""),
        ],
        diagram=flow([("TEMPLATE", "Fixed text|and [blanks]"), ("FILL IN", "Name, class,|amount"), ("RESULT", "A ready,|consistent message")], "a8", "One template, many correct results"),
        caption="Fix the parts that stay the same. Leave blanks for the parts that change.",
        terms=[("Prompt template", "A prompt with fixed instructions and blanks that can be filled in."), ("Variable", "A blank in a template, written in brackets, that changes each time."),
               ("How-to-use note", "A short guide that tells others how to fill in and use the template."), ("Demo", "A short live presentation of your work.")],
        mistakes=["Adding so many blanks that the template is hard to fill.", "Never testing the template on real, different inputs.", "No how-to-use note, so nobody else can use it.", "Leaving real private details inside a shared template."],
        quiz=[dict(q="What is a prompt template?", o=["A prompt with fixed instructions and blanks that can be filled in", "A long essay", "An AI model", "A type of image"], a=0, why="Fixed instructions plus variables make a reusable prompt."),
              dict(q="Which belongs in a how-to-use note?", o=["Only your name", "The blanks to fill in, a filled-in example and a warning to check facts", "A secret password", "Nothing at all"], a=1, why="Others need to know the blanks, see an example and know the risks."),
              dict(q="Why test a template on five different inputs?", o=["Because five looks neat", "To make the template longer", "To find where it fails before other people rely on it", "Because the AI requires it"], a=2, why="Testing varied inputs finds weak spots early."),
              dict(q="Which is a good use case for a template?", o=["A task you will only do once", "A task with no clear user", "A task nobody needs", "A task that repeats with changing details, like fee reminders"], a=3, why="Templates pay off when a task repeats and only the details change.")],
    ),
}