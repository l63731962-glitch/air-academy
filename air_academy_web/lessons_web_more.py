"""Web Development Masterclass: lessons 9 to 24, added when the course grew into a full course (course_plan.py says where each one sits on screen).
Same format as lessons_web.py plus one "activity" sentence per lesson. Quiz "a" = index of the right option."""
from diagrams import bars, compare, cycle, flow, grid, hub, pyramid, rings, seq, stack, timeline, tree, triangle   # noqa: F401

LESSONS = {}

LESSONS[9] = dict(   # HTML structure and semantic tags
    minutes=13,
    hook="Every web page you have ever opened, from a news site to a banking app, starts as plain text that a browser reads and turns into a page. That text is HTML, and the way you structure it decides whether a page is easy to maintain, easy to find on Google and usable by people who cannot see the screen. A beginner often builds pages from a pile of generic boxes. A professional uses tags that say what each part is. In this lesson you will build a proper page skeleton and learn why the choice of tag matters.",
    sections=[
        ("The skeleton of every page", """Every HTML page has the same outer shape:

> [HTML]
> <!doctype html>
> <html lang="en">
>   <head>
>     <meta charset="utf-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1">
>     <title>Ada's Bakery, Yaba</title>
>   </head>
>   <body>
>     <h1>Welcome to Ada's Bakery</h1>
>   </body>
> </html>

The **head** holds information about the page that visitors do not see on the page itself: the character set, the title in the browser tab, and the viewport setting that makes the page work on phones. The **body** holds everything people see. The `lang` attribute tells browsers and screen readers which language to expect, so pronunciation and translation work properly."""),
        ("Headings: the outline of your page", """Headings go from `h1` to `h6`. Think of them as the table of contents of a book:

- Use **one `h1`** for the main title of the page.
- Use `h2` for the main sections, `h3` for parts of a section, and so on.
- **Do not skip levels** just to get a smaller font. Choose the level by meaning and change the size with CSS.

Screen-reader users often jump from heading to heading to scan a page, the way sighted users skim. Search engines also use headings to understand what a page is about. A page with headings chosen only for size is like a book whose chapter titles are all in the wrong order."""),
        ("Semantic landmarks instead of anonymous boxes", """The `div` tag means nothing. It is just a box. **Semantic** tags carry meaning:

- `header`: the introduction or top of a page or section (logo, title).
- `nav`: a group of main navigation links.
- `main`: the unique main content of the page. Use it once.
- `section`: a themed group of content, usually with its own heading.
- `article`: a self-contained piece, such as a blog post or a product card.
- `aside`: related side content, such as a tip box.
- `footer`: closing information such as contact links and copyright.

Using them costs nothing. In return, assistive technology can jump straight to the navigation or the main content, and your code becomes easier to read. Use `div` and `span` only when no semantic tag fits."""),
        ("Text, lists and links", """Choose text tags by meaning:

- `p` for paragraphs, `ul` for lists where order does not matter, `ol` for steps and rankings, and `li` for each item.
- `strong` for important text and `em` for stress. They look bold and italic by default, but mean importance and emphasis.
- `blockquote` for a long quotation, and `code` for computer code.

Links use the `a` tag with an `href`. Write link text that makes sense on its own: “Read our delivery policy”, not “click here”. If a link opens a new tab, add `rel="noopener"` for safety. Use relative links (`about.html`) inside your own site and full addresses for other sites."""),
        ("Check your work", """Good habits make HTML reliable:

1. **View it without CSS.** A well-structured page should still read in a sensible order.
2. **Validate it.** The free W3C validator at validator.w3.org finds unclosed tags and mistakes.
3. **Use your browser's developer tools** (press F12) to inspect the structure the browser actually built.
4. **Indent your code** so you can see which tags sit inside which.

Most layout and accessibility problems that beginners fight later start with careless HTML at the beginning. Spending ten extra minutes here saves hours."""),
    ],
    diagram=tree("PAGE (body)", [("header", ["Logo", "nav"]), ("main", ["h1 title", "section", "article"]), ("footer", ["Contact", "Copyright"])],
                 note="Tags that say what each part is."),
    caption="A semantic page has a header, a main area and a footer, each made of meaningful tags.",
    terms=[("Head", "The part of a page holding information about it, such as the title and character set."), ("Heading", "A title tag from h1 to h6 that shows the outline of the page."),
           ("Semantic tag", "A tag that says what its content is, such as nav or footer, instead of being a plain box."), ("Landmark", "A page region that screen readers can jump to, such as main or nav."),
           ("Attribute", "Extra information inside a tag, such as href or lang.")],
    mistakes=["Using many div tags where header, nav and main would say what they are.", "Choosing a heading level for its font size.", "Writing “click here” as link text.", "Forgetting the viewport meta tag, so the page looks tiny on phones."],
    quiz=[dict(q="How many h1 headings should a normal page have?", o=["None", "One main h1 for the page title", "Ten", "As many as there are paragraphs"], a=1,
               why="One h1 gives the page a clear main title, and lower levels build the outline under it."),
          dict(q="What does the viewport meta tag do?", o=["It adds a title", "It changes the colour", "It protects the page from hackers", "It makes the page scale properly on phones"], a=3,
               why="Without it, phones show a zoomed-out desktop layout."),
          dict(q="Which tag is best for the main navigation links?", o=["div", "nav", "span", "aside"], a=1,
               why="nav tells browsers and screen readers that these links are the main navigation."),
          dict(q="Which link text is best?", o=["Click here", "Read our delivery policy", "Link", "Here"], a=1,
               why="Link text should make sense on its own, especially for screen-reader users who list links.")],
    activity="Build a one-page bakery or shop site using only HTML: a header with nav, a main with two sections, and a footer. Validate it at validator.w3.org and fix every error.",
)

LESSONS[10] = dict(   # Forms, tables, images and media
    minutes=14,
    hook="A website that only displays things is a brochure. The moment someone can type their name, choose a delivery option or upload a photo, it becomes a tool. Forms are how visitors talk back to your site, and tables, images and media are how you show information properly. They are also where most accessibility and usability problems hide: a form field without a label, a table used for layout, an image that is five megabytes. In this lesson you will learn to build each of these correctly.",
    sections=[
        ("Forms: every field needs a label", """A form collects information. The basic building blocks are:

> [HTML]
> <form action="/order" method="post">
>   <label for="name">Full name</label>
>   <input id="name" name="name" type="text" required autocomplete="name">
>
>   <label for="phone">Phone number</label>
>   <input id="phone" name="phone" type="tel" autocomplete="tel">
>
>   <label for="size">Size</label>
>   <select id="size" name="size">
>     <option>Small</option>
>     <option>Large</option>
>   </select>
>
>   <button type="submit">Place order</button>
> </form>

The `label` is joined to its field by `for` and `id`, so clicking the label focuses the field and screen readers announce it. The `name` attribute is the key the server receives. Never use the placeholder text as a replacement for a label, because it disappears as soon as someone types."""),
        ("Choose the right input type", """The `type` attribute gives phones the right keyboard and lets the browser check the value:

- `email`, `tel`, `number`, `url`, `date`, `password`, `search`.
- `checkbox` for yes or no, and for choosing several options.
- `radio` for choosing exactly one option from a group, with the same `name`.
- `textarea` for long text, and `select` for a list of choices.

Add built-in checks with `required`, `min`, `max`, `minlength` and `pattern`. These give instant feedback, but they are only a convenience. A server must always check again, because anyone can bypass the browser. Use `method="post"` for forms that change data or send private information, and `get` only for searches, because GET puts the values in the address."""),
        ("Tables are for data, not for layout", """Use a table when you have rows and columns of related data, such as a price list or a timetable:

> [HTML]
> <table>
>   <caption>Bread prices</caption>
>   <thead>
>     <tr><th scope="col">Item</th><th scope="col">Price (₦)</th></tr>
>   </thead>
>   <tbody>
>     <tr><td>Sliced bread</td><td>1,500</td></tr>
>     <tr><td>Meat pie</td><td>700</td></tr>
>   </tbody>
> </table>

`th` marks header cells and `scope` says whether they head a column or a row, which lets screen readers read each cell together with its heading. The `caption` names the table. Never build page layout with tables. That is what CSS Grid and Flexbox are for."""),
        ("Images that load fast and make sense", """Images are usually the heaviest part of a page, and many visitors in Nigeria and elsewhere pay for every megabyte. Follow these rules:

- **Always write alt text** that describes the image's purpose: `alt="Ada pulling a tray of meat pies from the oven"`. For purely decorative images use an empty `alt=""`.
- **Set width and height** so the browser reserves space and the page does not jump while loading.
- **Compress images** and choose formats well: JPEG for photos, PNG for graphics needing transparency, SVG for logos and icons, and WebP or AVIF for smaller files where supported.
- **Lazy-load** images below the fold with `loading="lazy"`.
- **Serve the right size.** `srcset` lets the browser pick a smaller file on a small screen. A 4000-pixel photo on a phone is a waste."""),
        ("Video, audio and embeds", """Use the built-in tags:

> [HTML]
> <video controls width="640" poster="cover.jpg">
>   <source src="tour.mp4" type="video/mp4">
>   <track kind="captions" src="tour.vtt" srclang="en" label="English">
> </video>

Always add `controls`, and captions for speech, for deaf users, for people watching in noisy places and for those who watch with the sound off. Do not autoplay sound, because browsers often block it and it annoys users. For embedded content such as a YouTube video or a map, use an `iframe` with a descriptive `title`. Remember that heavy media costs data: offer a link to download, or load the video only when the visitor presses play."""),
    ],
    diagram=grid([("FORMS", "Label + input|+ button"), ("TABLES", "Rows of data,|th and td"), ("IMAGES", "Alt text, size,|lazy loading"), ("VIDEO", "Controls and|captions"), ("AUDIO", "Controls,|no autoplay"), ("EMBEDS", "iframe with|a title")], cols=3,
                 note="Each element has one correct job."),
    caption="Forms, tables, images, video, audio and embeds: each has a correct, accessible way to build it.",
    terms=[("Label", "Text joined to a form field so everyone knows what to type and clicking it focuses the field."), ("Input type", "An attribute such as email or date that sets the keyboard and the browser's checks."),
           ("alt text", "A short description of an image's purpose for people who cannot see it."), ("srcset", "A list of image files in different sizes so the browser can choose the best one."),
           ("Captions", "Text of the spoken words in a video, shown on screen.")],
    mistakes=["Using placeholder text instead of a label.", "Relying on browser checks only and not validating on the server.", "Building a page layout with a table.", "Uploading a 5 MB photo straight from the phone camera."],
    quiz=[dict(q="Why must every form field have a label?", o=["Labels are decoration", "They make the form longer", "They tell users and screen readers what to enter, and clicking them focuses the field", "They stop spam"], a=2,
               why="A label is the accessible name of the field."),
          dict(q="Which method should a form that sends a password use?", o=["get", "post", "put", "any, they are all the same"], a=1,
               why="GET puts the data in the address. Use POST for private or data-changing forms."),
          dict(q="What is a table for?", o=["Page layout", "Spacing", "Rows and columns of related data", "Decoration"], a=2,
               why="Tables are for data. Use CSS for layout."),
          dict(q="Which is best for a logo that must stay sharp at any size?", o=["A huge JPEG", "SVG", "A screenshot", "A GIF"], a=1,
               why="SVG is drawn with shapes so it stays sharp and is usually tiny.")],
    activity="Build an order form with five fields, each with a label, a sensible input type and required where needed. Then add a price table and a compressed image with alt text.",
)

LESSONS[11] = dict(   # Accessibility basics
    minutes=13,
    hook="Think about the people who will use your site: someone whose eyes are tired on a night bus, a grandmother who needs large text, a student on a cracked phone screen in bright sun, a customer who is blind and uses a screen reader, a person with a broken arm who can only use a keyboard. Accessibility means building so all of them can use what you made. It is also good business, because more people can buy from you, and good engineering, because accessible sites are usually cleaner and easier to maintain. The basics are not hard, and you will learn them all in this lesson.",
    sections=[
        ("Who accessibility is for", """Accessibility covers permanent, temporary and situational needs: blindness or low vision, deafness, limited movement, cognitive differences such as dyslexia or ADHD, a broken arm, bright sunlight, a slow connection, or a first language that is not the language of the site.

The international guidelines, **WCAG**, group the goals into four principles, often remembered as POUR:

- **Perceivable:** people can see or hear the content (text alternatives, captions, contrast).
- **Operable:** people can use it with a mouse, keyboard or other devices.
- **Understandable:** the content and controls are clear and predictable.
- **Robust:** it works with different browsers and assistive technology."""),
        ("The essentials that fix most problems", """A short checklist covers a large share of real-world problems:

1. **Alt text** on meaningful images.
2. **Proper headings** in order, and semantic landmarks such as `main` and `nav`.
3. **Labels** on every form field, with clear error messages that say what went wrong and how to fix it.
4. **Colour contrast:** at least 4.5 to 1 for normal text, and 3 to 1 for large text, against its background.
5. **Do not use colour alone** to carry meaning. Pair a red border with an icon and text.
6. **Meaningful link text**, and buttons that say what they do.
7. **Captions** for videos with speech.

None of these needs special tools. They are habits you apply as you build."""),
        ("Keyboard access", """Many people never use a mouse. Test your page with only the keyboard:

- `Tab` moves forward through links, buttons and fields, and `Shift+Tab` goes back.
- `Enter` activates links and buttons, `Space` toggles checkboxes and buttons.
- The **focus outline** must always be visible so users know where they are. Never write `outline: none` without giving a clear replacement.
- The tab order should follow the visual order.
- Add a **skip link** at the top (“Skip to main content”) so keyboard users can jump past a long menu.

Use real `button` and `a` elements. A clickable `div` does not work with the keyboard until you add a great deal of extra code, while a real button works for free."""),
        ("ARIA: use it carefully", """**ARIA** attributes add extra information for assistive technology, such as `aria-label` for a button that only shows an icon, or `aria-expanded` for a menu that opens and closes. The first rule of ARIA is: **if a native HTML element does the job, use it instead.** A `button` is better than a `div role="button"`, and a `nav` is better than `div role="navigation"`.

Bad ARIA is worse than none, because it can tell a screen reader something untrue. Use it only for custom widgets that HTML cannot express, and test them."""),
        ("How to test", """You can test accessibility in about fifteen minutes:

1. **Keyboard only:** can you reach and use everything, and always see where you are?
2. **Zoom to 200%:** does the page still work without sideways scrolling?
3. **Run an automatic check:** Lighthouse in Chrome developer tools, or the free axe extension. These find about a third to a half of issues, so they are a start, not the finish.
4. **Try a screen reader:** NVDA is free on Windows, VoiceOver is built into Apple devices and TalkBack on Android. Listen to the first screen of your page.
5. Respect **reduced motion:** use the `prefers-reduced-motion` media query to turn off big animations for people who ask for it.

If possible, ask real users with different needs to try your site. They will teach you more than any checklist."""),
    ],
    diagram=hub(("ACCESSIBLE SITE", "works for everyone"), [("Perceivable", "See or hear it"), ("Operable", "Use by keyboard"), ("Understandable", "Clear and predictable"), ("Robust", "Works with assistive tech")],
                note="The four WCAG principles: POUR."),
    caption="Perceivable, Operable, Understandable and Robust: the four principles of accessibility.",
    terms=[("WCAG", "The Web Content Accessibility Guidelines, the international standard for accessible websites."), ("Contrast ratio", "How different a text colour is from its background. 4.5 to 1 is the minimum for normal text."),
           ("Screen reader", "Software that reads the screen aloud for people who cannot see it."), ("Focus outline", "The visible mark showing which element the keyboard is on."),
           ("ARIA", "Extra attributes that describe custom controls to assistive technology.")],
    mistakes=["Removing the focus outline for looks.", "Using colour alone to show an error.", "Using a div as a button.", "Running only an automatic checker and calling the site accessible."],
    quiz=[dict(q="What does the O in POUR stand for?", o=["Original", "Optional", "Operable", "Online"], a=2,
               why="Operable means people can use the site with different devices, including the keyboard."),
          dict(q="What is the minimum contrast ratio for normal body text under WCAG?", o=["2 to 1", "4.5 to 1", "10 to 1", "There is none"], a=1,
               why="WCAG asks for at least 4.5 to 1 for normal text."),
          dict(q="Which is the better choice for a clickable control?", o=["A div with a click handler", "A span styled as a button", "A real button element", "An image"], a=2,
               why="A native button works with the keyboard and screen readers for free."),
          dict(q="Why is an automatic accessibility checker not enough on its own?", o=["It finds only some of the problems, so you must also test by hand", "It is illegal", "It breaks the site", "It only works on Mondays"], a=0,
               why="Automatic tools catch a portion of issues. Keyboard and screen-reader tests find the rest.")],
    activity="Unplug your mouse and use only the keyboard on your own page. Fix anything you cannot reach or cannot see focus on, then run Lighthouse and fix its accessibility warnings.",
)

LESSONS[12] = dict(   # Flexbox and Grid layouts
    minutes=14,
    hook="Not long ago, web designers built layouts with tables and clever hacks, and getting a simple three-column page to behave on every screen could take a day. Today two tools in CSS solve almost every layout problem: Flexbox for arranging things in a line, and Grid for arranging them in rows and columns. Once you understand when to use each, you can build a navigation bar, a product grid and a whole page layout in a few lines, and they adapt to phones, tablets and laptops by themselves.",
    sections=[
        ("Flexbox: arranging items in one direction", """Flexbox lays children out in a row or a column. Put `display: flex` on the **parent**:

> [CSS]
> .nav {
>   display: flex;
>   justify-content: space-between;   /* spread along the main axis */
>   align-items: center;              /* centre across the other axis */
>   gap: 16px;
> }

The important ideas: `flex-direction` chooses row or column. `justify-content` places items along the main direction and `align-items` across it. `gap` adds space between items. `flex-wrap: wrap` lets items move to the next line when space runs out. `flex: 1` on an item tells it to share the spare space. Flexbox is perfect for navigation bars, button rows, a card's header, and centring something both ways."""),
        ("Grid: rows and columns together", """Grid controls both directions at once. Define the columns on the parent:

> [CSS]
> .cards {
>   display: grid;
>   grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
>   gap: 20px;
> }

This single line means: “make as many columns as fit, each at least 220 pixels wide, and share the leftover space equally.” On a phone you get one column, on a tablet two, on a laptop four, with no media query at all. That is the power of Grid.

Use `fr` units to split free space (`1fr 2fr` makes the second column twice as wide), `gap` for spacing, and `grid-column: span 2` to make an item cover two columns."""),
        ("Page layouts with named areas", """Grid can describe a whole page by name, which is easy to read:

> [CSS]
> .page {
>   display: grid;
>   grid-template-columns: 220px 1fr;
>   grid-template-areas:
>     "header header"
>     "side   main"
>     "footer footer";
> }
> header { grid-area: header; }
> aside  { grid-area: side; }
> main   { grid-area: main; }
> footer { grid-area: footer; }

For small screens, change the template inside a media query so everything stacks into one column. The names make the layout almost self-explanatory, even months later."""),
        ("Which should you use?", """A simple rule:

- **Flexbox** when you are laying out **one row or one column** and the content should decide the sizes (menus, toolbars, form rows, a line of buttons).
- **Grid** when you are laying out **rows and columns together** and the layout should decide the sizes (card galleries, dashboards, whole pages).

They work well together. A grid can place cards, and inside each card a flex container can line up a title and a button. Do not choose one forever. Choose per component."""),
        ("Common problems and fixes", """When a layout misbehaves, check these first:

1. **You put the display property on the wrong element.** `display: flex` goes on the parent, not on the children you want to arrange.
2. **Text or images overflow.** A flex child may refuse to shrink. Add `min-width: 0` to it, and give images `max-width: 100%`.
3. **Things squash on small screens.** Use `flex-wrap: wrap`, or `auto-fit` in Grid.
4. **You cannot tell what is happening.** Open developer tools (F12). Chrome and Firefox show Flexbox and Grid overlays that draw the lines and gaps.
5. **Using fixed pixel widths everywhere.** Prefer `fr`, percentages, `minmax()` and `max-width` so the layout flexes."""),
    ],
    diagram=compare(("FLEXBOX", ["One direction at a time", "Menus, toolbars, button rows", "Content decides the size"]), ("GRID", ["Rows and columns together", "Card galleries, whole pages", "Layout decides the size"]), vs="or",
                    note="Use both: a grid of cards, each card a flex row."),
    caption="Flexbox arranges in one direction, Grid in two. Use each where it fits.",
    terms=[("Flexbox", "A CSS layout system for arranging items in a row or a column."), ("Grid", "A CSS layout system for arranging items in rows and columns at the same time."),
           ("fr unit", "A share of the free space in a grid, such as 1fr or 2fr."), ("gap", "The space between flex or grid items."), ("minmax()", "A grid size that is never smaller than the first value or larger than the second.")],
    mistakes=["Putting display: flex on the children instead of the parent.", "Using fixed pixel widths that break on phones.", "Using Grid for a one-line menu where Flexbox is simpler.", "Not opening the layout overlay in developer tools when stuck."],
    quiz=[dict(q="Where does display: flex go?", o=["On every child", "On the parent that holds the items", "On the body only", "On the image"], a=1,
               why="Flexbox is switched on at the container, and it then arranges its children."),
          dict(q="What does repeat(auto-fit, minmax(220px, 1fr)) do?", o=["Makes exactly three columns", "Hides columns", "Makes as many columns as fit, each at least 220 pixels wide, sharing the leftover space", "Sets the font size"], a=2,
               why="It creates a responsive grid that adapts to the available width."),
          dict(q="Which fits a horizontal navigation bar best?", o=["Flexbox", "A table", "A video tag", "A form"], a=0,
               why="A single row of items is exactly what Flexbox is for."),
          dict(q="Which is a good way to build a whole page with header, sidebar, main and footer?", o=["Many nested tables", "Grid with named areas", "Only inline styles", "Images of text"], a=1,
               why="Grid template areas describe a page layout clearly.")],
    activity="Build a responsive card gallery with auto-fit Grid, and a Flexbox navigation bar above it. Resize the window and open the Grid overlay in developer tools.",
)

LESSONS[13] = dict(   # Transitions, animation and modern CSS
    minutes=13,
    hook="A page that jumps from one state to another feels cheap. A button that eases to a new colour when you hover, a menu that slides open, a card that lifts slightly when you point at it: these small movements tell users that something happened and make a site feel finished. Modern CSS can do all of this without a single line of JavaScript, and it has also gained powerful tools for colour, sizing and layout that remove old hacks. In this lesson you will learn transitions, keyframe animations and the modern CSS features worth using every day.",
    sections=[
        ("Transitions: smooth change between two states", """A **transition** animates a property when it changes, for example on hover:

> [CSS]
> .button {
>   background: #0b6e4f;
>   transform: translateY(0);
>   transition: background 0.2s ease, transform 0.2s ease;
> }
> .button:hover,
> .button:focus-visible {
>   background: #0d8a63;
>   transform: translateY(-2px);
> }

You choose the property, the duration and the easing. Keep durations short: 150 to 300 milliseconds feels responsive, while a full second feels slow. Use `:focus-visible` as well as `:hover`, so keyboard users get the same feedback. Avoid `transition: all`, because it can animate properties you did not intend and costs performance."""),
        ("Keyframe animations", """When something must move by itself, or follow several steps, use `@keyframes`:

> [CSS]
> @keyframes fade-up {
>   from { opacity: 0; transform: translateY(12px); }
>   to   { opacity: 1; transform: translateY(0); }
> }
> .card {
>   animation: fade-up 0.4s ease-out both;
> }

You can set how many times it repeats (`animation-iteration-count`), a delay (`animation-delay`) and whether it runs forward or back. Staggering delays on a list of cards makes them appear one after another. Spinners and loading skeletons are also built with keyframes. Use animation to guide attention or show a process, not to decorate every element."""),
        ("Animate the right properties", """Browsers can animate some properties cheaply and others expensively. **`transform` and `opacity`** are handled by the graphics card and stay smooth even on a modest phone. Changing `width`, `height`, `top`, `left` or `margin` forces the browser to recalculate the layout on every frame, which can stutter.

So to move something, use `transform: translate()`. To grow it, use `transform: scale()`. To fade it, use `opacity`. This matters in Nigeria and other places where many users have budget phones. A smooth, simple animation beats a fancy one that lags.

Also respect users who get dizzy or distracted by motion:

> [CSS]
> @media (prefers-reduced-motion: reduce) {
>   * { animation: none !important; transition: none !important; }
> }"""),
        ("Modern CSS you should be using", """CSS has gained many features that replace old tricks:

- **Custom properties (variables):** `--brand: #0b6e4f;` then `color: var(--brand);`. Change one value and the whole theme updates, which also makes dark mode easy.
- **`clamp()`:** `font-size: clamp(1rem, 2.5vw, 1.5rem)` gives text that grows with the screen but stays within limits.
- **`aspect-ratio`:** `aspect-ratio: 16 / 9;` keeps video and image boxes in shape.
- **`:has()`:** style a parent based on its children, such as a form group that contains an invalid field.
- **Container queries:** a component changes layout based on the width of its own container, not the whole screen.
- **`gap`, `min()`, `max()`, `inset`** and logical properties such as `margin-inline` for cleaner code.

Check support on caniuse.com before relying on a very new feature, and give older browsers a sensible fallback."""),
        ("Keep CSS organised", """CSS grows quickly and can become a tangle. A few habits keep it healthy:

1. **Name things by purpose,** such as `.card` or `.nav-link`, not by looks, such as `.red-big`.
2. **Keep specificity low.** Avoid long selector chains and `!important`. If you keep needing them, your structure needs attention.
3. **Put colours, spacing and font sizes in variables,** so a design change is a one-line edit.
4. **Order the file:** variables, base styles, layout, components, then special cases.
5. **Remove dead code** from time to time. Unused CSS still downloads.

Use your browser's developer tools to try changes live, then copy the final values back into your file."""),
    ],
    diagram=flow([("Trigger", "hover, focus|or page load"), ("Change", "a property|gets a new value"), ("Transition", "the browser|animates between"), ("Result", "smooth, not|a sudden jump")], "cssmotion",
                 note="Animate transform and opacity for smooth results."),
    caption="A trigger changes a property and the browser animates smoothly between the old and new values.",
    terms=[("Transition", "CSS that animates a property smoothly when it changes from one value to another."), ("Keyframes", "A set of steps that describe how an animation changes over time."),
           ("Custom property", "A CSS variable such as --brand that you can reuse across the stylesheet."), ("clamp()", "A CSS function that picks a value between a minimum and a maximum."),
           ("prefers-reduced-motion", "A media query that detects users who asked their device to reduce movement.")],
    mistakes=["Writing transition: all and animating things you did not mean to.", "Animating width or top instead of transform.", "Ignoring users who prefer reduced motion.", "Using hover effects with no keyboard focus equivalent."],
    quiz=[dict(q="Which two properties are cheapest to animate?", o=["width and height", "transform and opacity", "margin and padding", "top and left"], a=1,
               why="They are handled by the graphics card and avoid layout recalculation."),
          dict(q="What does @keyframes define?", o=["The steps of an animation", "A font", "A media query", "A grid"], a=0,
               why="Keyframes describe how properties change across the animation."),
          dict(q="Why add a prefers-reduced-motion rule?", o=["To make pages load faster", "To respect users who are sensitive to movement", "To hide images", "To change the font"], a=1,
               why="Some people get dizzy or distracted by animation and ask their device to reduce it."),
          dict(q="What is a CSS custom property?", o=["A browser bug", "A reusable value such as --brand, used with var()", "A JavaScript library", "A kind of image"], a=1,
               why="Custom properties let you define a value once and reuse it everywhere.")],
    activity="Add a hover and focus transition to your buttons, a fade-up animation on your cards, and a prefers-reduced-motion rule. Then move your colours into CSS variables.",
)

LESSONS[14] = dict(   # Mini project: a responsive landing page
    minutes=18,
    hook="Time to put the first half of the course to work. A landing page is a single page with one clear job: to make a visitor take one action, such as ordering, booking or signing up. It is the most useful first project, because small businesses everywhere need one, and it uses everything you have learned: semantic HTML, forms, accessibility, Flexbox, Grid and modern CSS. In this project lesson you will plan, build and test a responsive landing page for a real or imaginary business, such as a bakery, a tailor, a barber or a tutoring service.",
    sections=[
        ("Plan before you code", """Write a one-paragraph brief first:

- **Who is it for?** For example, people in Lagos who want cakes for birthdays.
- **What is the one action?** For example, “Order via WhatsApp”.
- **What makes this business different?** For example, same-day delivery in Yaba.

Then sketch the sections on paper, from top to bottom: header with logo and menu, **hero** (headline, one sentence, one button), **benefits or services** (three to four cards), **proof** (photos, reviews with real permission), **price or how it works**, a **contact or order form**, and a footer. Plan the phone layout first, because that is how most of your visitors will see it."""),
        ("Build the structure in HTML", """Start with HTML only, with no styling at all:

1. The page skeleton and a descriptive `title` and meta description.
2. A `header` with `nav`, a `main` containing a `section` for each part of your sketch, and a `footer`.
3. One `h1` in the hero, `h2` for each section.
4. Real text, not “lorem ipsum”. Writing the real words first shows what the design needs.
5. Images with alt text and sizes, and a form with labels.

Open the page with no CSS and read it from top to bottom. If it makes sense in that raw form, your structure is good."""),
        ("Style it mobile first", """Now add CSS, starting with the phone size:

1. **Variables** for your two or three brand colours, spacing and font sizes.
2. **Base styles:** a readable font, a comfortable line height, `max-width` on text blocks, and `img { max-width: 100%; height: auto; }`.
3. **Mobile layout** in a single column with generous spacing.
4. **A button style** that is large enough to tap (at least 44 pixels high) with a clear focus style.
5. **Then widen:** use `@media (min-width: 768px)` to switch the cards to a Grid with auto-fit and the header to a Flexbox row.

Keep colour contrast high, especially on the hero button and over images. Add a subtle hover and focus transition for polish."""),
        ("Make the call to action work", """The whole page exists for one action, so make it effortless:

- Put the main button **in the hero and again near the end**.
- For a WhatsApp order, use a link such as `https://wa.me/234XXXXXXXXXX?text=Hello%2C%20I%20want%20to%20order` with the business's own number. Never put a stranger's number in a public project.
- If you use a form, make it short (name, phone, message), validate it, and show a clear success message.
- Show real trust signals: location, opening hours, a phone number the business agrees to publish, and clear prices where possible.

A visitor should always know what to do next, and the button text should say what happens, such as “Order a cake” rather than “Submit”."""),
        ("Test, fix and publish", """Before you call it done:

1. **Resize** the browser from 320 pixels wide to a large desktop and fix anything that breaks.
2. **Test on a real phone**, ideally an older Android with a slower connection.
3. **Keyboard test** the whole page, and run Lighthouse for performance, accessibility and best practice. Aim for 90 or more in each.
4. **Compress images** so the page loads in a few seconds on mobile data.
5. **Validate the HTML** and read every word for typing mistakes.
6. **Publish free** on GitHub Pages, Netlify or Cloudflare Pages and send the link to the business owner for feedback.

Save it in your portfolio with a short note on the problem, your decisions and what you would improve."""),
    ],
    diagram=timeline([("Plan", "Brief and sketch"), ("HTML", "Structure and real text"), ("CSS", "Mobile first"), ("Action", "Button or form"), ("Test", "Phone and keyboard"), ("Publish", "Free hosting")],
                     note="Six steps from idea to live page."),
    caption="Plan, write the HTML, style mobile first, make the action work, test and publish.",
    terms=[("Landing page", "A single page built to make visitors take one clear action."), ("Hero", "The large top section of a page with the main headline and button."),
           ("Call to action", "The button or link that asks the visitor to do the one important thing."), ("Mobile first", "Designing for the smallest screen first and adding layout for bigger screens."),
           ("Lighthouse", "A free tool in Chrome that scores performance, accessibility and best practice.")],
    mistakes=["Starting to style before the real content and structure exist.", "Having three competing buttons instead of one clear action.", "Testing only on a big laptop screen.", "Using a photo of a real person or a phone number without permission."],
    quiz=[dict(q="What is a landing page for?", o=["Showing every product the business sells", "Getting visitors to take one clear action", "Playing a video", "Replacing a database"], a=1,
               why="A landing page has one job, and everything on it supports that action."),
          dict(q="Why build the HTML with real text first?", o=["It is faster to type", "Lorem ipsum is illegal", "Real words show what the design really needs", "Browsers need it"], a=2,
               why="Real content reveals the true length of headings and paragraphs."),
          dict(q="What does mobile first mean?", o=["Designing for phones first and adding layout for larger screens", "Using only mobile apps", "Making the site slow", "Testing only on desktop"], a=0,
               why="You start with the smallest screen and enhance upward."),
          dict(q="Which button text is best?", o=["Submit", "Click", "Order a cake", "OK"], a=2,
               why="Button text should say what will happen.")],
    activity="Build a complete responsive landing page for a real or imaginary local business with a hero, three benefit cards, a short form and a footer. Publish it free and score at least 90 in Lighthouse accessibility.",
)

LESSONS[15] = dict(   # Functions, arrays and objects
    minutes=14,
    hook="Almost every real JavaScript program is built from three ideas. Functions package a job so you can reuse it. Arrays hold lists of things, such as products or messages. Objects hold the details of one thing, such as a product's name, price and photo. Put them together and you can represent a shop, filter it, total a cart and show the result. In this lesson you will learn to write functions properly, to loop over lists with modern array methods, and to shape your data with objects, which is exactly how data arrives from servers.",
    sections=[
        ("Functions: write once, use many times", """A function takes inputs (**parameters**), does a job and gives back a result (**return value**):

> [JavaScript]
> function addVat(price, rate = 0.075) {
>   return price + price * rate;
> }
>
> const total = addVat(10000);          // 10750
>
> // Arrow function: same idea, shorter
> const double = (n) => n * 2;

Keep each function small and focused on one job, and give it a name that says what it does, such as `calculateDeliveryFee`. A function that does one thing is easy to test and easy to reuse. Prefer returning a value over changing things outside the function, because that keeps your code predictable."""),
        ("Arrays: ordered lists", """An array holds values in order, counted from zero:

> [JavaScript]
> const prices = [1500, 700, 2500];
> prices[0];            // 1500
> prices.length;        // 3
> prices.push(900);     // add to the end

You will use these methods constantly, and each one takes a small function:

- `map` makes a new array by changing every item: `prices.map((p) => p * 1.075)`.
- `filter` keeps only items that pass a test: `prices.filter((p) => p > 1000)`.
- `reduce` boils the list to one value: `prices.reduce((sum, p) => sum + p, 0)`.
- `find` returns the first match, and `some` or `every` answer yes or no questions.
- `forEach` runs a function for each item without building a new array.

Learning `map`, `filter` and `reduce` well changes how you think about data."""),
        ("Objects: the details of one thing", """An object holds named properties:

> [JavaScript]
> const product = {
>   id: 12,
>   name: "Meat pie",
>   price: 700,
>   inStock: true,
>   tags: ["snack", "baked"],
> };
>
> product.name;            // "Meat pie"
> product["price"];        // 700
> const { name, price } = product;   // destructuring

You can put objects inside arrays and arrays inside objects, which is how real data looks. Copy and update with the spread operator: `const sale = { ...product, price: 600 }` creates a new object and leaves the original unchanged."""),
        ("Putting them together: a small shop", """Here is the idea in action:

> [JavaScript]
> const cart = [
>   { name: "Meat pie", price: 700, qty: 3 },
>   { name: "Zobo", price: 500, qty: 2 },
> ];
>
> const total = cart.reduce((sum, item) => sum + item.price * item.qty, 0);
> const names = cart.map((item) => item.name);
> const bigItems = cart.filter((item) => item.qty > 2);

This is the same pattern you will use to show orders, lessons, messages and search results. Notice that the data is **separate from the display**: first you shape the data with functions, then you show it on the page. That separation is the secret to code that stays manageable as it grows."""),
        ("Habits and common errors", """A few habits prevent most beginner bugs:

1. Use `const` by default, `let` when a value must change, and avoid `var`.
2. Use `===` (strict equality), not `==`.
3. Remember that array indexes start at **0**, so the last item is `arr[arr.length - 1]`.
4. `undefined` often means a property name is misspelled or the data has not arrived yet. Check with `console.log`.
5. Functions that do not `return` give back `undefined`.
6. Do not change an array while you loop over it. Build a new one with `map` or `filter` instead.

Use `console.log` and the browser console freely. Printing a value is the quickest way to learn what your code is really doing."""),
    ],
    diagram=flow([("Data", "array of|objects"), ("filter", "keep only|what you need"), ("map", "change each|item"), ("reduce", "one final|value"), ("Show", "put it on|the page")], "jsdata",
                 note="Shape the data with functions, then display it."),
    caption="Shape an array of objects with filter, map and reduce, then show the result.",
    terms=[("Function", "A reusable block of code that takes inputs and can return a result."), ("Array", "An ordered list of values, counted from zero."),
           ("Object", "A collection of named properties describing one thing."), ("Arrow function", "A shorter way to write a function using =>."),
           ("Destructuring", "Pulling values out of an object or array into variables in one line.")],
    mistakes=["Forgetting that array indexes start at zero.", "Using == instead of ===.", "Forgetting the return keyword in a function.", "Changing an array while looping over it."],
    quiz=[dict(q="Which array method builds a new array by changing each item?", o=["filter", "reduce", "map", "find"], a=2,
               why="map returns a new array with the result of a function on each item."),
          dict(q="What does arr[0] return?", o=["The last item", "The first item", "The length", "undefined always"], a=1,
               why="Arrays are counted from zero, so index 0 is the first item."),
          dict(q="Which method would you use to add up all prices in a cart?", o=["reduce", "push", "forEach with no variable", "includes"], a=0,
               why="reduce boils a list down to a single value such as a total."),
          dict(q="What does the spread operator in { ...product, price: 600 } do?", o=["Deletes the product", "Copies the product into a new object with a changed price", "Freezes the product", "Sorts the product"], a=1,
               why="Spread copies properties into a new object, and later properties override earlier ones.")],
    activity="Write a cart in an array of objects and use reduce for the total, filter for items above 1,000 naira and map to list the names. Print each result with console.log.",
)

LESSONS[16] = dict(   # The DOM and events
    minutes=14,
    hook="HTML is what the browser starts with. The moment the page loads, the browser turns it into a live tree of objects called the DOM, and JavaScript can read and change that tree while the visitor is looking at it. That is how a click adds an item to a cart, how typing filters a list, and how a menu opens. The part you already know from your first JavaScript lesson is the idea. In this lesson you will go further: selecting elements properly, reacting to clicks, typing and form submissions, and updating the page safely and efficiently.",
    sections=[
        ("The page is a tree you can change", """The **DOM** (Document Object Model) represents every element as an object in a tree. JavaScript finds elements with selectors, the same ones you use in CSS:

> [JavaScript]
> const title = document.querySelector("h1");
> const buttons = document.querySelectorAll(".buy");
>
> title.textContent = "Welcome back";
> title.classList.add("highlight");
> title.setAttribute("data-id", "12");

`querySelector` returns the first match and `querySelectorAll` returns all of them. Change text with `textContent`, change appearance by adding or removing CSS classes with `classList` (cleaner than writing styles in JavaScript), and set attributes with `setAttribute`. Remember to load your script after the HTML it needs, or use the `defer` attribute."""),
        ("Events: reacting to the visitor", """An **event** is something that happens: a click, a key press, a form submission, the page finishing loading. You listen for it and run a function:

> [JavaScript]
> const form = document.querySelector("#signup");
>
> form.addEventListener("submit", (event) => {
>   event.preventDefault();          // stop the page reloading
>   const email = form.elements.email.value.trim();
>   console.log("Signing up", email);
> });

Common events are `click`, `input` (every keystroke), `change`, `submit`, `keydown` and `scroll`. The function receives an **event object** that tells you what happened and which element it happened on (`event.target`). Always call `preventDefault()` on a form submit when you handle it yourself."""),
        ("Creating and updating elements", """To add content, create elements and put them into the page:

> [JavaScript]
> const list = document.querySelector("#items");
>
> function render(items) {
>   list.replaceChildren();                 // clear
>   for (const item of items) {
>     const li = document.createElement("li");
>     li.textContent = `${item.name}: ₦${item.price}`;
>     list.append(li);
>   }
> }

Use `textContent` to put text in, **not `innerHTML`**, whenever the text comes from users or from a server. If it contains a `<script>` or a broken tag, `innerHTML` will run or build it, which is how cross-site scripting attacks happen. If you must use HTML, clean it first. A good pattern: keep your data in a variable and write a `render` function that rebuilds the view from the data."""),
        ("Event delegation", """If you have a list with 100 buttons, do not attach 100 listeners. Attach **one** to the parent and check what was clicked:

> [JavaScript]
> list.addEventListener("click", (event) => {
>   const btn = event.target.closest("button[data-remove]");
>   if (!btn) return;
>   removeItem(Number(btn.dataset.remove));
> });

This also works for items you add later, because the listener sits on the parent that never changes. `data-` attributes (such as `data-remove="12"`) let you attach an id to an element and read it back with `dataset`. Event delegation is faster, simpler and the standard way to handle dynamic lists."""),
        ("Keeping interfaces usable", """When you change the page with JavaScript, remember the people who use it:

1. Use real `button` and `a` elements, so keyboard and screen readers work.
2. After an action, **tell the user.** Show a clear message in an element with `aria-live="polite"` so screen readers announce it.
3. Move focus sensibly, for example to the first field of a dialog that just opened.
4. Do not make the page jump or lose the user's typed text.
5. Keep work in the event handler small. If it must do heavy work, show a loading state.

Test with the keyboard and with the browser's developer tools (Elements and Console tabs), which let you watch the DOM change in real time."""),
    ],
    diagram=seq(["Visitor", "Your code", "DOM"], [(0, 1, "click event: Add item"), (1, 2, "create li and append it"), (2, 0, "the new item appears")], "domevents",
                note="An event triggers code that changes the DOM."),
    caption="A click becomes an event, your code runs, and the DOM updates what the visitor sees.",
    terms=[("DOM", "The live tree of objects the browser builds from your HTML, which JavaScript can change."), ("Event", "Something that happens on the page, such as a click or a key press."),
           ("preventDefault", "A method that stops the browser's default action, such as reloading on form submit."), ("Event delegation", "Listening on a parent element to handle events from many children."),
           ("textContent", "A safe way to set text on an element without interpreting it as HTML.")],
    mistakes=["Putting user text into innerHTML.", "Forgetting preventDefault so the form reloads the page.", "Attaching one listener per item in a long list.", "Loading the script before the elements exist."],
    quiz=[dict(q="What does event.preventDefault() do on a form submit?", o=["Deletes the form", "Stops the page from reloading so your code can handle it", "Makes the form faster", "Sends the form twice"], a=1,
               why="Otherwise the browser performs its default submit and reloads the page."),
          dict(q="Which is safer for putting user-provided text on the page?", o=["innerHTML", "textContent", "document.write", "eval"], a=1,
               why="textContent treats the value as plain text, so scripts do not run."),
          dict(q="What is event delegation?", o=["Deleting events", "Sending events to a server", "Listening on a parent to handle clicks from its children", "Using only keyboard events"], a=2,
               why="One listener on the parent handles many children, including ones added later."),
          dict(q="Which method finds ALL elements matching a selector?", o=["getElement", "querySelector", "find", "querySelectorAll"], a=3,
               why="querySelectorAll returns every match, while querySelector returns only the first.")],
    activity="Build a to-do list: a form that adds items, a button on each item that removes it using event delegation, and a polite aria-live message saying what changed.",
)

LESSONS[17] = dict(   # Fetching data from APIs
    minutes=14,
    hook="Most useful websites do not contain their own data. A weather widget asks a weather service, a shop page asks its own server for products, and a payment button asks Paystack to confirm a transaction. They all talk to **APIs** over the internet, and the browser tool for that conversation is `fetch`. You already met fetch and JSON in an earlier lesson. Here you go further, into what separates a demo from a dependable page: handling loading and errors, sending data, understanding why the browser sometimes refuses a request, and keeping secrets out of the front end.",
    sections=[
        ("A reliable fetch, step by step", """The simple version works only when everything goes right. A reliable version expects trouble:

> [JavaScript]
> async function loadProducts() {
>   try {
>     const res = await fetch("/api/products");
>     if (!res.ok) {
>       throw new Error(`Server said ${res.status}`);
>     }
>     return await res.json();
>   } catch (err) {
>     console.error("Could not load products", err);
>     return null;
>   }
> }

Two things matter. First, `fetch` only fails by itself when the network breaks. A 404 or 500 still arrives as a normal response, so you must check `res.ok`. Second, wrap the call in `try` and `catch` so an unexpected problem cannot crash the page."""),
        ("Loading, success and error states", """Every request has at least four moments, and a good page shows each one:

1. **Loading:** show a spinner or a skeleton so users know something is happening.
2. **Success:** show the data.
3. **Empty:** the call worked but there is nothing to show. Say so kindly: “No orders yet”.
4. **Error:** say what went wrong in plain words and offer a **Try again** button.

On Nigerian mobile networks, slow and failing requests are normal, not rare. A page that shows a blank screen or a frozen button feels broken, while a page that shows a loading state and a retry feels reliable. Also disable the submit button while a request is running, so that a nervous double click does not send the order twice."""),
        ("Sending data: POST and headers", """To send data to an API, choose the method and send JSON:

> [JavaScript]
> const res = await fetch("/api/orders", {
>   method: "POST",
>   headers: { "Content-Type": "application/json" },
>   body: JSON.stringify({ item: "Meat pie", qty: 3 }),
> });
> const data = await res.json();

`GET` reads, `POST` creates, `PUT` or `PATCH` updates and `DELETE` removes. The `Content-Type` header tells the server how to read the body. Many APIs also need an `Authorization` header with a token that proves who you are. Read the API's documentation carefully, because every API has its own rules for addresses, parameters, limits and error messages."""),
        ("CORS and keeping secrets safe", """Sometimes the browser blocks a request with a **CORS** error. CORS is a safety rule: by default, a page on one website may not read responses from a different website unless that other server says it is allowed (with `Access-Control-Allow-Origin`). The fix is on the **server**, not in your front-end code. If you control the server, allow the right origin. If you do not, call the API from your own backend, which then passes the data on.

The same idea protects secrets. **Anything in front-end JavaScript can be read by anyone**, by opening developer tools. So never put a secret API key, a Paystack secret key or a database password in your browser code. Keep it on a server and let the server call the API. Only public keys, designed for the browser, belong in the front end."""),
        ("Practical habits", """A few habits make API code pleasant to work with:

- **Put request code in small functions** (`getProducts`, `createOrder`) instead of scattering fetch calls around the page.
- **Cache what does not change**, and do not request the same data again and again.
- **Debounce search boxes:** wait 300 milliseconds after the last keystroke before sending a request.
- **Cancel old requests** with `AbortController` when the user moves on.
- **Respect rate limits.** Many APIs allow only a number of requests per minute.
- **Test with a tool** such as the browser's Network tab, which shows every request, its status, its timing and the data.

Free practice APIs include JSONPlaceholder and the Open-Meteo weather API, which need no key."""),
    ],
    diagram=seq(["Page", "Your server", "Other API"], [(0, 1, "GET /api/weather?city=Lagos"), (1, 2, "request with the secret key"), (2, 1, "weather data"), (1, 0, "JSON for the page")], "fetchapi",
                note="The secret key stays on the server."),
    caption="The page asks your server, your server asks the other API with the secret key, and only the data comes back.",
    terms=[("API", "A set of addresses and rules that lets one program ask another for data or actions."), ("res.ok", "A fetch response property that is true when the status code means success."),
           ("CORS", "A browser safety rule that decides whether a page may read responses from another website."), ("Debounce", "Waiting for a pause before running something, such as a search request."),
           ("Rate limit", "A cap on how many requests an API allows in a period of time.")],
    mistakes=["Assuming fetch fails on a 404 or 500 response.", "Putting a secret API key in front-end code.", "Showing a blank page while loading or after an error.", "Sending a request on every keystroke."],
    quiz=[dict(q="Does fetch throw an error on a 404 response?", o=["Yes, always", "No, you must check res.ok yourself", "Only on Mondays", "Only for POST"], a=1,
               why="fetch rejects only on network failure. HTTP errors arrive as normal responses."),
          dict(q="Where should a secret API key live?", o=["In the HTML", "In front-end JavaScript", "On a server, never in browser code", "In the page title"], a=2,
               why="Anything in the browser can be read by anyone."),
          dict(q="A CORS error is fixed mainly...", o=["by restarting the computer", "on the server that sends the response", "by using a bigger image", "by clearing the cache only"], a=1,
               why="The other server must allow your origin, or you route the call through your own backend."),
          dict(q="Which of these is NOT one of the four moments of a request?", o=["Loading", "Empty", "Error", "Celebrating"], a=3,
               why="Good pages handle loading, success, empty and error states.")],
    activity="Fetch a free API such as Open-Meteo, and show a loading state, the result, an empty message and an error with a Try again button. Break the address on purpose to test the error state.",
)

LESSONS[18] = dict(   # Components and thinking in state
    minutes=14,
    hook="When a page grows beyond a few interactions, plain JavaScript turns into a tangle of selectors and manual updates: if the count changes, you must remember to update the header, the cart icon and the checkout button. Modern front-end development solves this with two ideas that you will use for the rest of your career. **Components** split the interface into small reusable pieces. **State** is the data that describes what the page should look like right now, so that the screen is simply a result of the state. Once you think this way, frameworks such as React and Vue make sense.",
    sections=[
        ("Components: small reusable pieces", """A **component** is a self-contained piece of interface that takes inputs and produces a piece of the page. A product card, a button, a navigation bar, a comment: each can be a component. In React it looks like this:

> [JSX]
> function ProductCard({ name, price }) {
>   return (
>     <article className="card">
>       <h3>{name}</h3>
>       <p>₦{price}</p>
>     </article>
>   );
> }

The inputs are called **props**. Write the component once and use it many times with different props. Components can contain other components, so your page becomes a tree: a `Page` holds a `ProductList`, which holds many `ProductCard`s. A change in one component does not break the others."""),
        ("State: the data behind the screen", """**State** is data that can change while the page is open: the items in a cart, whether a menu is open, the text in a search box, whether data is loading. The central idea is:

**The screen is a function of the state.** You do not manually edit the page. You change the state, and the framework redraws whatever is needed.

> [JSX]
> function Counter() {
>   const [count, setCount] = React.useState(0);
>   return (
>     <button onClick={() => setCount(count + 1)}>
>       Clicked {count} times
>     </button>
>   );
> }

Here `count` is the state, and `setCount` is how you change it. Clicking does not touch the page directly. It changes the state, and the button text follows."""),
        ("Where should state live?", """A key design decision is **where each piece of state belongs**:

1. If only one component uses it (such as whether a dropdown is open), keep it **inside that component**.
2. If two sibling components need the same data (such as the cart count in the header and the cart list), move it **up to their nearest common parent** and pass it down as props. This is called *lifting state up*.
3. If many distant components need it (such as the logged-in user), use a shared tool such as React **context** or a small store.
4. **Do not copy state.** Keep one source of truth. If the total can be calculated from the items, calculate it, rather than storing it separately and risking it going out of sync.

Good state design keeps programs simple. Poor state design is the main reason front-end code becomes confusing."""),
        ("Data flows in one direction", """In component frameworks, data normally flows **down** (parent to child through props) and events flow **up** (child to parent through functions):

- The parent owns the cart and passes `items` to `CartList`.
- When the user clicks remove, `CartList` calls the function `onRemove(id)` that the parent gave it.
- The parent updates its state, and everything redraws with the new data.

This one-way flow makes problems easy to trace: if something shows the wrong value, you follow the data upward to find where it was set. The pattern is also the same in React, Vue, Svelte and Angular, with small differences in syntax."""),
        ("Why use a framework at all?", """You do not need a framework for a landing page. Reach for one when your interface has **a lot of changing data and many interactions**, such as dashboards, shops with carts, chat, or tools used for hours.

Benefits: reusable components, predictable updates, a large community and plenty of jobs. Costs: a build step, more to learn, larger downloads and constant upgrades. Start with the **ideas** (components and state), which transfer between all tools. If you can explain what the state is and where it lives, you can learn any framework quickly."""),
    ],
    diagram=cycle([("State", "the data"), ("Screen", "drawn from state"), ("Event", "click or typing"), ("Update", "change the state")], "statecycle", center="One source|of truth",
                  note="Change the state and the screen follows."),
    caption="State produces the screen, an event changes the state, and the screen is redrawn.",
    terms=[("Component", "A reusable piece of interface that takes inputs and returns part of the page."), ("Props", "The inputs a parent passes down to a component."),
           ("State", "Data that can change while the page is open and decides what the screen shows."), ("Lifting state up", "Moving shared state to the nearest common parent of the components that need it."),
           ("Single source of truth", "Keeping each piece of data in one place so copies cannot disagree.")],
    mistakes=["Editing the page directly instead of changing state.", "Copying the same data into two states that drift apart.", "Putting everything in one giant component.", "Reaching for a framework for a simple static page."],
    quiz=[dict(q="What does the idea “the screen is a function of the state” mean?", o=["The screen decides the state", "You change the state and the screen follows", "State is only for colours", "The state is stored on the screen"], a=1,
               why="You update data, and the framework redraws the interface from it."),
          dict(q="What are props?", o=["Inputs passed from a parent to a child component", "A kind of image", "Server settings", "CSS rules"], a=0,
               why="Props flow down from a parent so a component can be reused with different data."),
          dict(q="Two sibling components need the same data. What should you do?", o=["Copy the data into both", "Lift the state up to their common parent", "Use global variables everywhere", "Delete one component"], a=1,
               why="Keep one source of truth in the nearest common parent."),
          dict(q="When is a framework most worth it?", o=["A one-page brochure", "An interface with lots of changing data and interactions", "A printed flyer", "A text file"], a=1,
               why="Frameworks shine when state and interactions get complicated.")],
    activity="Plan a shopping cart on paper: list the components, decide what the state is and where it lives, and draw arrows for the data going down and the events going up.",
)

LESSONS[19] = dict(   # Building a small app with a modern framework
    minutes=18,
    hook="Reading about components and state is one thing. Building something that works is where it clicks. In this lesson you will build a small but real application, a menu and cart for a food stall, using a modern framework such as React with Vite. You will set up the project, create components, manage state, load data and run a production build. The exact commands change over time, so you will also learn how to check the official documentation, which is a skill that never goes out of date.",
    sections=[
        ("Set up the project", """You need Node.js installed (check with `node -v`). Then create a project with Vite, a fast build tool:

> [Terminal]
> npm create vite@latest food-stall -- --template react
> cd food-stall
> npm install
> npm run dev

The last command starts a local development server, usually at `http://localhost:5173`, and refreshes the page whenever you save a file. Look at what was created: `index.html`, a `src` folder with `main.jsx` and `App.jsx`, and `package.json`, which lists your dependencies and scripts. Commands change between versions, so when in doubt, follow the current steps at vite.dev and react.dev."""),
        ("Plan the components", """Before writing code, decide the structure:

- `App` owns the state: the menu items and the cart.
- `MenuList` shows all items and receives `items` and `onAdd` as props.
- `MenuItem` shows one item with an **Add** button.
- `Cart` shows the chosen items with quantities and the total, with a **Remove** button.

The state lives in `App`, because both `MenuList` and `Cart` need it. Write the structure on paper first. If you can say what each component receives and what it tells its parent, you are ready to code."""),
        ("Write the state and the components", """In `App.jsx`:

> [JSX]
> import { useState } from "react";
>
> export default function App() {
>   const [cart, setCart] = useState([]);
>
>   function addItem(item) {
>     setCart((old) => {
>       const found = old.find((x) => x.id === item.id);
>       if (found) {
>         return old.map((x) => x.id === item.id ? { ...x, qty: x.qty + 1 } : x);
>       }
>       return [...old, { ...item, qty: 1 }];
>     });
>   }
>
>   const total = cart.reduce((s, x) => s + x.price * x.qty, 0);
>   return (/* MenuList and Cart go here */);
> }

Notice that you never change the old array. You create a new one, which is what lets React notice the change. The `total` is calculated from the cart, not stored."""),
        ("Load data and handle states", """Real apps load data. Use `useEffect` to fetch the menu when the page opens, and keep `loading` and `error` states, as you learned in the fetching lesson:

> [JSX]
> const [menu, setMenu] = useState([]);
> const [status, setStatus] = useState("loading");
>
> useEffect(() => {
>   fetch("/menu.json")
>     .then((r) => r.ok ? r.json() : Promise.reject())
>     .then((data) => { setMenu(data); setStatus("ready"); })
>     .catch(() => setStatus("error"));
> }, []);

Show a loading message, an error with a retry button, or the menu depending on `status`. Give each list item a stable `key` (its id), so React can keep track of items. Keep components small and move repeated logic into helper functions."""),
        ("Build, deploy and keep learning", """When it works, create the production build:

> [Terminal]
> npm run build
> npm run preview

This makes optimised files in a `dist` folder, which you can upload to a free host such as Netlify, Vercel, Cloudflare Pages or GitHub Pages. Add a `README` explaining what the project does and how to run it.

Then improve it: save the cart in `localStorage`, add a quantity stepper, add a WhatsApp order button, write tests, and make it accessible with proper buttons and focus. Compare with Vue or Svelte, and notice that the ideas (components, props, state, effects) are the same, so you are learning concepts, not just one tool."""),
    ],
    diagram=tree("App (owns state)", [("MenuList", ["MenuItem", "MenuItem", "Add button"]), ("Cart", ["Cart rows", "Remove button", "Total"])],
                 note="State lives in App, because both children need it."),
    caption="App owns the cart state and passes data and functions down to MenuList and Cart.",
    terms=[("Vite", "A fast build tool and development server for modern front-end projects."), ("package.json", "The file that lists a project's dependencies and scripts."),
           ("useState", "A React function that gives a component a piece of state and a way to change it."), ("useEffect", "A React function for running code, such as fetching data, after the page draws."),
           ("Production build", "An optimised version of your app made for the real website.")],
    mistakes=["Changing the existing array instead of creating a new one.", "Storing the total separately instead of calculating it.", "Forgetting a key when showing a list.", "Following an old tutorial whose commands no longer work, instead of the current docs."],
    quiz=[dict(q="Why does the cart state live in the App component?", o=["It looks nicer", "Because both the menu and the cart need it", "Because App is the largest", "React requires it"], a=1,
               why="Shared state belongs in the nearest common parent."),
          dict(q="What does npm run build create?", o=["A backup of your code", "A new project", "An optimised version of your app in the dist folder", "A database"], a=2,
               why="The build step prepares the files you deploy."),
          dict(q="Why should you create a new array instead of changing the old one?", o=["React notices the change and redraws", "It uses less memory", "JavaScript forbids changes", "It is required by Node"], a=0,
               why="A new array tells React that state changed."),
          dict(q="Where should you look when a tutorial's commands do not work?", o=["Give up", "A random forum from five years ago", "Delete Node.js", "The current official documentation"], a=3,
               why="Tools change, and the official docs show the current way.")],
    activity="Build the food stall menu and cart in React with Vite, with add, remove and a calculated total. Run the production build and publish it on a free host.",
)

LESSONS[20] = dict(   # Performance and SEO basics
    minutes=14,
    hook="A beautiful website that takes twelve seconds to load on a phone loses its visitor before the page appears. A website that Google cannot understand never gets found at all. Performance and search engine optimisation (SEO) are two sides of the same goal: help the right people reach your page quickly. Both are much simpler than their reputation suggests. In this lesson you will learn what to measure, the handful of changes that give the biggest gains, and how to help search engines understand your pages.",
    sections=[
        ("Why speed matters and what to measure", """Slow pages lose visitors, sales and search ranking. In Nigeria, where many people use mid-range phones and pay for data, a light page is a real competitive advantage.

Google measures the experience with the **Core Web Vitals**:

- **LCP (Largest Contentful Paint):** how fast the main content appears. Aim for under 2.5 seconds.
- **INP (Interaction to Next Paint):** how quickly the page reacts to taps and clicks. Aim for under 200 milliseconds.
- **CLS (Cumulative Layout Shift):** how much the page jumps around while loading. Aim for under 0.1.

Measure with **Lighthouse** in Chrome developer tools and **PageSpeed Insights** online. Test with a throttled, slow connection, not only your fast home Wi-Fi."""),
        ("The biggest wins", """Most slow pages share the same causes, and the fixes are straightforward:

1. **Shrink images.** They are usually the heaviest part. Resize them, compress them, use WebP or AVIF, and add `loading="lazy"` for images below the fold.
2. **Set image width and height** so the page does not jump (better CLS).
3. **Send less JavaScript.** Remove libraries you do not use. Load scripts with `defer`.
4. **Minify and compress.** Build tools minify, and the server should send files compressed with gzip or Brotli.
5. **Cache static files** with proper headers so returning visitors do not download them again.
6. **Use a CDN** to serve files from a location near the visitor.
7. **Limit fonts.** Use one or two families, only the weights you need, and `font-display: swap`.

Fix the biggest item first, then measure again."""),
        ("How search engines work", """A search engine **crawls** pages by following links, **indexes** what it finds, and then **ranks** results when someone searches. You help in four ways:

- **Clear content:** write pages that really answer what people search for, using the words they use.
- **Good HTML:** a unique `title` and `meta description` on each page, one `h1`, logical headings, descriptive link text and alt text.
- **Crawlable pages:** real links, a `sitemap.xml` that lists your pages, and a `robots.txt` that does not block what you want found. Pages built only with JavaScript can be harder to index, so for content sites use server-side rendering or static generation.
- **Trust and speed:** HTTPS, a fast site and a good mobile experience."""),
        ("On-page SEO in practice", """For each page, ask: what would someone type to find this?

> [HTML]
> <title>Fresh Cakes in Yaba, Lagos | Ada's Bakery</title>
> <meta name="description" content="Order birthday cakes with same-day delivery in Yaba. See prices and flavours.">
> <link rel="canonical" href="https://example.com/cakes">
> <meta property="og:title" content="Fresh Cakes in Yaba">
> <meta property="og:image" content="https://example.com/cake.jpg">

Keep the title under about 60 characters and the description under about 160. The `og:` tags control how the link looks when shared on WhatsApp, Facebook and X, which brings traffic too. For a local business, create a **Google Business Profile** with the same name, address and phone as the site. Use clean, readable addresses such as `/cakes` instead of `/page?id=482`."""),
        ("Be honest about SEO", """No one can promise “number one on Google in a week”. Be wary of anyone who does. Real results come from useful content, a fast and trustworthy site, and time. Avoid tricks that break search engine rules, such as hidden text, buying links or copying other sites, because they can get a site penalised.

A sensible routine: set up **Google Search Console** (free) to see which searches bring visitors and which pages have problems, publish helpful pages regularly, check Lighthouse after each big change, and keep improving what real users need."""),
    ],
    diagram=bars([("Slow page", 10), ("After resizing images", 5), ("After removing unused JS", 3.5), ("After caching and CDN", 2)], note="Illustrative load times in seconds", unit="s"),
    caption="Each fix, such as smaller images, less JavaScript and caching, cuts the load time. These numbers are an illustration.",
    terms=[("Core Web Vitals", "Google's measures of loading, responsiveness and visual stability."), ("Lazy loading", "Loading images or content only when they are about to be seen."),
           ("Sitemap", "A file listing the pages of a site so search engines can find them."), ("Meta description", "A short summary of a page that search engines often show under its title."),
           ("CDN", "A network of servers that delivers your files from a location near each visitor.")],
    mistakes=["Uploading full-size camera photos.", "Testing speed only on fast Wi-Fi.", "Giving every page the same title.", "Believing promises of instant number one ranking."],
    quiz=[dict(q="Which Core Web Vital measures how much the page jumps while loading?", o=["LCP", "INP", "CLS", "CDN"], a=2,
               why="Cumulative Layout Shift measures visual stability."),
          dict(q="What is usually the heaviest part of a web page?", o=["The title", "Images", "The footer", "Comments in the code"], a=1,
               why="Unoptimised images often account for most of a page's weight."),
          dict(q="What does a sitemap.xml do?", o=["Speeds up the CPU", "Lists your pages to help search engines find them", "Blocks visitors", "Stores passwords"], a=1,
               why="It gives crawlers a list of the pages you want found."),
          dict(q="Which is an honest SEO promise?", o=["Number one on Google in one week", "Useful content, a fast site and time can improve results", "Guaranteed 10,000 visitors", "A secret trick Google hates"], a=1,
               why="No one controls rankings, but quality, speed and time help.")],
    activity="Run Lighthouse on your landing page, fix the two biggest performance warnings, add a unique title, meta description and share image, and write down the before and after scores.",
)

LESSONS[21] = dict(   # Forms, validation and user accounts
    minutes=15,
    hook="The day your website lets people create accounts, you take on a serious responsibility: you are now holding other people's email addresses, passwords and personal details. Sign-up and login forms look simple, but they are where careless code does the most damage. In this lesson you will build the full path correctly: designing forms people can finish, validating on both the browser and the server, storing passwords safely so they cannot be read even by you, keeping people logged in with sessions, and handling the awkward cases such as forgotten passwords.",
    sections=[
        ("Forms people can actually complete", """Many sign-ups fail because the form is annoying. Ask only for what you truly need, because every extra field loses people. Then:

- Label every field, and show the label all the time, not only as a placeholder.
- Use the right `type` and `autocomplete` values (`email`, `new-password`, `current-password`), so phones and password managers can help.
- Let people **show the password** with a toggle button.
- Show errors **next to the field**, in plain words: “Password must be at least 8 characters”, not “Invalid input”.
- Keep what the user typed when there is an error.
- Mark the button as busy during the request to prevent double submissions."""),
        ("Validate in the browser and on the server", """Validation happens in two places for two reasons:

1. **In the browser** (HTML attributes such as `required`, `type="email"`, `minlength`, plus JavaScript for custom rules) for **speed and kindness**: users learn about a mistake immediately.
2. **On the server** for **security**: a browser check can be skipped by anyone using developer tools or a script. The server must check every value again and never trust what arrives.

On the server, check the type, the length and the format, remove extra spaces, make emails lowercase, and confirm that the email is not already used. Return a clear error message and a 400 or 422 status for bad input. The server is the real gatekeeper. The browser is only a helpful assistant."""),
        ("Passwords: never store them as text", """You must **never** store a password as it was typed, and never email it back. If your database leaks, every password leaks with it, and people reuse passwords across sites.

The correct approach is to store only a **hash** made with a slow, purpose-built algorithm such as **bcrypt, scrypt or Argon2**, which includes a random **salt**:

> [Python]
> from werkzeug.security import generate_password_hash, check_password_hash
>
> stored = generate_password_hash(password)        # on sign-up
> ok = check_password_hash(stored, typed_password)  # on login

Do not use plain MD5 or SHA-256 for passwords, because they are too fast and can be attacked quickly. Require a sensible minimum length (at least 8, and longer is better) and allow long passphrases. Block the most common passwords, and never print passwords in logs."""),
        ("Sessions: staying logged in", """HTTP has no memory, so after login the server must recognise the visitor on later requests. The usual way is a **session**: the server creates a random session id (or a signed token), sends it in a **cookie**, and looks it up on each request.

Protect the cookie with these flags: **`HttpOnly`** (JavaScript cannot read it, which limits theft by XSS), **`Secure`** (only sent over HTTPS), and **`SameSite=Lax`** (helps against CSRF). Make sessions expire, rotate the session id after login, and delete the session on logout. Always check on the **server** who the user is and whether they may do the action. Hiding a button in the page does not protect anything."""),
        ("Handling the awkward cases", """Real accounts need more than login and sign-up:

- **Forgotten password:** send a one-time link with a random token that expires in an hour. Never reveal whether an email exists. Say “If that email has an account, we sent a link.”
- **Email verification:** confirm that people own the address before trusting it.
- **Slow down guessing:** limit failed logins per account and per address, and add a short delay.
- **Generic login errors:** “Email or password is wrong”, not which one.
- **Consider “Sign in with Google”** or a similar service, so you store fewer passwords yourself.
- **Respect privacy law:** collect minimal data, explain why, and let people delete their account. In Nigeria, the NDPA 2023 sets rules for handling personal data."""),
    ],
    diagram=seq(["Browser", "Server", "Database"], [(0, 1, "POST email and password"), (1, 2, "find user, compare hash"), (2, 1, "match"), (1, 0, "set a secure session cookie")], "loginflow",
                note="Only the hash is stored. The password never is."),
    caption="Login compares the typed password to a stored hash, then the server gives the browser a secure session cookie.",
    terms=[("Hash", "A one-way scrambled version of a password that cannot be turned back into the original."), ("Salt", "Random extra data added before hashing so identical passwords give different hashes."),
           ("Session", "The server's memory of a logged-in visitor between requests."), ("HttpOnly cookie", "A cookie that JavaScript cannot read, which protects it from some attacks."),
           ("Server-side validation", "Checking every submitted value on the server, because the browser check can be bypassed.")],
    mistakes=["Storing passwords as plain text or with fast hashes like MD5.", "Validating only in the browser.", "Telling attackers whether an email address exists.", "Hiding admin buttons but not checking permissions on the server."],
    quiz=[dict(q="How should a password be stored?", o=["As typed", "Encrypted with a key kept beside it", "Only as a slow salted hash such as bcrypt or Argon2", "In a cookie"], a=2,
               why="A slow salted hash cannot be reversed and resists guessing."),
          dict(q="Why must the server validate input even if the browser already did?", o=["Browsers are always wrong", "Anyone can bypass the browser's checks", "It is faster", "Servers like extra work"], a=1,
               why="Attackers send requests directly. Never trust what arrives."),
          dict(q="What does the HttpOnly flag on a cookie do?", o=["Makes it expire", "Stops JavaScript from reading it", "Makes it larger", "Encrypts the database"], a=1,
               why="It helps keep the session cookie from being stolen by injected scripts."),
          dict(q="A good response when someone requests a password reset for an unknown email is...", o=["“No such user”", "“If that email has an account, we sent a link.”", "Show the user list", "Send the password"], a=1,
               why="A generic answer does not reveal which emails have accounts.")],
    activity="Sketch the full sign-up, login and forgot-password flow on paper, marking where each value is validated, where the password is hashed and which cookie flags you would set.",
)

LESSONS[22] = dict(   # Testing and debugging websites
    minutes=14,
    hook="Every developer writes bugs. What separates professionals from beginners is not that they write fewer of them, but that they find them faster and stop them coming back. Testing is how you check that your site works before your visitors do. Debugging is the calm, step-by-step skill of finding out why something is not working. In this lesson you will build a practical testing routine that does not need a big team: testing by hand properly, using the browser developer tools, writing your first automated tests and fixing bugs methodically.",
    sections=[
        ("Test like a visitor: a manual checklist", """Before any automated tools, test by hand with a checklist:

1. **Devices:** a phone (ideally an older Android), a tablet size and a desktop.
2. **Browsers:** Chrome, Safari and Firefox. Edge usually matches Chrome.
3. **Connection:** throttle to Slow 4G in developer tools. Does a loading state appear?
4. **Keyboard:** can you reach and use everything without a mouse?
5. **Bad input:** empty fields, very long text, emoji, a script tag, a wrong password.
6. **Main journeys:** sign up, log in, order, pay, log out.
7. **Reload and back button:** does the page behave?

Write the checklist down and repeat it before every release. A checklist catches the boring bugs that would otherwise embarrass you."""),
        ("Debugging with browser developer tools", """Press **F12** to open the tools. These are the most useful tabs:

- **Console:** shows errors and your `console.log` messages, with the file and line number.
- **Elements:** shows the live DOM and the CSS applied. Change values and see the result immediately.
- **Network:** shows every request, its status code, timing and response. Look for red failed requests.
- **Sources:** lets you set a **breakpoint**, which pauses code on a line so you can look at the variables step by step.
- **Application:** shows cookies, local storage and the service worker.

When the console says `Cannot read properties of undefined`, read it carefully: it tells you exactly what was undefined and on which line."""),
        ("A method for fixing bugs", """Panic and random changes waste time. Use a method:

1. **Reproduce it.** Find the exact steps that always cause the bug. If you cannot reproduce it, you cannot fix it.
2. **Read the error message** all the way through.
3. **Narrow it down.** Is it the front end or the back end? Check the Network tab. Which function? Add `console.log` or a breakpoint.
4. **Form one hypothesis** and test it by changing **one thing at a time**.
5. **Fix the cause, not the symptom.**
6. **Check that the fix works** and that nothing else broke.
7. **Write a test or a checklist item** so it cannot silently return.

If you are stuck, explain the problem aloud to a friend or a rubber duck. Often you find the answer while explaining. When you ask for help, share the error, the steps and what you already tried."""),
        ("Automated tests", """Automated tests are small programs that check your code and run in seconds, as often as you like. The main kinds:

- **Unit tests** check one function, such as `calculateTotal`.
- **Integration tests** check that parts work together, such as a route and its database.
- **End-to-end tests** act like a visitor in a real browser. Tools such as Playwright or Cypress click through your site.

A tiny example with Vitest or Jest:

> [JavaScript]
> import { calculateTotal } from "./cart.js";
>
> test("adds up price times quantity", () => {
>   const cart = [{ price: 700, qty: 3 }, { price: 500, qty: 2 }];
>   expect(calculateTotal(cart)).toBe(3100);
> });

Test the important and risky things first: money, login, permissions and anything that has broken before."""),
        ("Quality checks and monitoring", """Add automatic checks that keep quality up:

- A **linter** (ESLint) finds mistakes and bad habits while you type.
- A **formatter** (Prettier) keeps code tidy.
- **Lighthouse** and an accessibility checker such as axe run on every important page.
- **CI** (for example GitHub Actions) runs your tests and checks on every push, so a broken change is caught before it reaches visitors.
- **Error monitoring** (a free tier of a tool such as Sentry) tells you when real users hit an error, with details.

Quality is a habit, not a final step. Small checks done every day beat a giant clean-up before launch."""),
    ],
    diagram=cycle([("Reproduce", "find the steps"), ("Narrow down", "where is it"), ("Fix", "one change"), ("Verify", "retest and add a test")], "debugloop", center="Debugging|method",
                  note="Never change many things at once."),
    caption="Reproduce the bug, narrow it down, fix one thing, verify it and add a test.",
    terms=[("Breakpoint", "A marker that pauses code on a line so you can inspect variables."), ("Unit test", "An automated check of one small piece of code."),
           ("End-to-end test", "An automated test that behaves like a real visitor in a browser."), ("Linter", "A tool that scans code for mistakes and bad habits."),
           ("Reproduce", "To find the exact steps that always make a bug happen.")],
    mistakes=["Changing many things at once while debugging.", "Testing only on your own fast laptop.", "Ignoring the console error message.", "Fixing the symptom without finding the cause."],
    quiz=[dict(q="What is the first step in fixing a bug?", o=["Rewrite everything", "Reproduce it with exact steps", "Blame the browser", "Delete the file"], a=1,
               why="If you cannot reproduce a bug, you cannot know when you fixed it."),
          dict(q="Which developer tools tab shows failed requests and status codes?", o=["Elements", "Application", "Lighthouse", "Network"], a=3,
               why="The Network tab lists every request with its status and timing."),
          dict(q="What is a unit test?", o=["An automated check of one small piece of code", "A test of the whole company", "A test on one phone", "A test of the internet"], a=0,
               why="Unit tests check small pieces, such as one function."),
          dict(q="Why change only one thing at a time while debugging?", o=["It is traditional", "It uses less electricity", "So you know which change fixed or broke it", "To annoy others"], a=2,
               why="Single changes make the cause clear.")],
    activity="Write a manual test checklist for your landing page or app, test it on a real phone with throttled Slow 4G, and use a breakpoint in the Sources tab to step through one function.",
)

LESSONS[23] = dict(   # Domains, hosting and HTTPS
    minutes=14,
    hook="A website on your own computer is a secret. To share it with the world you need three things: a place where its files live and run (hosting), a name people can type (a domain) and a padlock that proves the connection is private (HTTPS). Together they decide whether customers find you, trust you and stay on your page. In this lesson you will learn how they fit together, how to choose between free and paid options, and how to go from a project on your laptop to a live address, including how to connect a domain, set up DNS and fix the common mistakes.",
    sections=[
        ("Hosting: where your site lives", """**Hosting** means a computer that is always on and connected, serving your files or running your code. The main options:

- **Static hosting** (GitHub Pages, Netlify, Cloudflare Pages, Vercel): for HTML, CSS and JavaScript sites with no server code. Often free, fast and simple.
- **App hosting / PaaS** (Render, Railway, Fly.io): runs a backend such as Flask or Node with a database. You push code, and the platform builds and runs it.
- **VPS** (a virtual server from DigitalOcean, Hetzner, AWS): full control, but you manage updates, security and backups yourself.
- **Shared hosting:** cheap and easy for WordPress and similar tools.

Match the tool to the job. A landing page needs static hosting. A shop with accounts needs an app host and a database. Note that free tiers may sleep when idle or limit usage, so check before depending on them for a business."""),
        ("Domains and DNS", """A **domain name** (such as `adasbakery.ng`) is bought from a **registrar** for a yearly fee. Prices vary: `.com` is usually modest, and `.ng` domains are available through accredited Nigerian registrars. Buy from a well-known registrar, use a strong password and two-factor login, turn on auto-renew, and make sure **you** are the registered owner, not the person who built your site for you.

**DNS** is the phone book that turns a name into an address. You set records:

- **A record:** points a name to an IPv4 address.
- **AAAA record:** the same for IPv6.
- **CNAME:** points a name to another name, such as your host's address.
- **MX:** where email for the domain goes.
- **TXT:** verification and email security records.

Changes can take from minutes up to a day to spread (propagation)."""),
        ("HTTPS: the padlock", """**HTTPS** encrypts the traffic between a visitor and your server, so nobody on the café Wi-Fi can read or change it. It uses a **TLS certificate** that proves the site is really yours. Today certificates are free through **Let's Encrypt**, and most hosts issue and renew them automatically.

HTTPS is not optional:

- Browsers warn visitors on plain HTTP pages and block some features.
- Passwords, forms and payments must never travel unencrypted.
- Search engines prefer HTTPS.
- Payment providers such as Paystack require it.

After you enable it, **redirect all HTTP traffic to HTTPS** and check that no images or scripts still load from `http://` addresses, which causes the “mixed content” warning."""),
        ("Going live step by step", """A typical path from laptop to live site:

1. Put your code on **GitHub**.
2. Connect the repository to your host and set the **build command** and **start command**.
3. Add **environment variables** (secrets) in the host's dashboard, never in the code.
4. Deploy, and test the temporary address the host gives you.
5. Buy the domain and add the DNS records the host tells you to add.
6. Add the custom domain in the host, and wait for the certificate to be issued.
7. Test: HTTPS works, `www` and the plain domain both work, forms work and the pages load quickly.
8. Add **uptime monitoring** (a free service that alerts you if the site goes down).

Keep a note of where each thing is: registrar, DNS, host and email provider."""),
        ("Common mistakes and good habits", """Watch out for these:

- **Domain and email expire** because the card on file failed. Turn on auto-renew and reminders.
- **Losing access** because the web designer owns the domain account.
- **Wrong DNS record** type, or a typo, so the site does not load.
- **Forgetting backups.** Hosts can fail. Keep your code in Git and your database backed up.
- **Hard-coding secrets** in code that goes to a public repository.
- **Ignoring cost.** Read the pricing page, and set spending alerts where available.

Treat your domain like a business asset: it is your address, and customers and search engines remember it."""),
    ],
    diagram=flow([("Your code", "on GitHub"), ("Host", "builds and|runs it"), ("DNS", "name points|to the host"), ("HTTPS", "certificate|and padlock"), ("Visitor", "types your|domain")], "golive",
                 note="Code, host, domain, HTTPS: then you are live."),
    caption="Code goes to a host, DNS points your domain to it, HTTPS secures it, and visitors can find you.",
    terms=[("Hosting", "An always-on computer that serves your files or runs your code."), ("Registrar", "A company that sells and registers domain names."),
           ("DNS", "The system that turns a domain name into an address."), ("TLS certificate", "A digital proof that lets browsers connect to your site privately over HTTPS."),
           ("Propagation", "The time it takes for a DNS change to spread across the internet.")],
    mistakes=["Letting someone else own your domain account.", "Forgetting auto-renew so the domain expires.", "Leaving mixed content (http images) on an HTTPS page.", "Putting secrets in a public GitHub repository."],
    quiz=[dict(q="What does DNS do?", o=["Encrypts traffic", "Turns a domain name into an address", "Compresses images", "Stores passwords"], a=1,
               why="DNS is the internet's phone book."),
          dict(q="Which hosting type is simplest for a landing page of HTML and CSS?", o=["A VPS you manage fully", "A supercomputer", "A printer", "Static hosting"], a=3,
               why="Static hosts serve plain files, often free and fast."),
          dict(q="What does HTTPS protect?", o=["The privacy and integrity of traffic between visitor and server", "Only the colours", "The domain price", "The logo"], a=0,
               why="It encrypts the connection so it cannot be read or changed on the way."),
          dict(q="Who should be the registered owner of a business's domain?", o=["The web designer", "A random stranger", "The business owner", "Nobody"], a=2,
               why="You must control your own domain account, or you can lose your website and email.")],
    activity="Deploy a project to a free static or app host, then write down which registrar, DNS provider, host and email provider you would use for a real business, and what each costs per year.",
)

LESSONS[24] = dict(   # Web security basics
    minutes=15,
    hook="Attackers do not need to be geniuses. They run automated tools that try the same well-known tricks against millions of websites, and they find the sites where a developer forgot one simple rule. The good news is that a short list of habits protects against most of what goes wrong. In this lesson you will learn the most common web attacks in plain language, including cross-site scripting, SQL injection, cross-site request forgery and broken access control, the defences that stop them, and a checklist you can apply to every project. This is defence only: you will learn to protect your own sites.",
    sections=[
        ("Think like a defender", """Start with one rule: **never trust anything that comes from outside your server.** That includes form fields, URL parameters, cookies, headers, uploaded files and even data from other APIs. All of it can be changed by someone who wants to cause harm.

The standard list of the most serious web risks is the **OWASP Top 10**, published for free at owasp.org. Many entries come down to the same causes: trusting input, forgetting to check permissions, and leaving secrets or defaults exposed.

Security is also layered. No single protection is perfect, so you combine several: validation, safe code, correct permissions, HTTPS, updates and monitoring."""),
        ("Cross-site scripting (XSS)", """**XSS** happens when an attacker's text, such as a comment containing a `<script>` tag, is shown on a page as real HTML, so their code runs in other people's browsers and can steal sessions or change the page.

Defences:

- **Escape output.** Show user text as text. In JavaScript use `textContent`, not `innerHTML`. Template engines such as Jinja escape by default, so do not disable that.
- **Sanitise** any HTML you truly must allow, with a trusted library.
- Set a **Content-Security-Policy** header to limit which scripts may run.
- Use `HttpOnly` cookies, so injected code cannot read the session cookie.

Treat every piece of user text as dangerous until it is escaped for the place where it is shown."""),
        ("SQL injection", """**SQL injection** happens when user input is glued into a database query as text, so the user can change the query itself. For example, building `"SELECT * FROM users WHERE email = '" + email + "'"` lets someone type quote marks and extra commands.

The cure is **parameterised queries** (also called prepared statements), which send the query and the values separately:

> [Python]
> cur.execute("SELECT id, name FROM users WHERE email = %s", (email,))

The database treats the value strictly as data, never as code. Use this for **every** query, and use an ORM or query builder correctly. Also give your database user only the permissions it needs, so a mistake cannot drop your tables."""),
        ("CSRF and broken access control", """**CSRF** (cross-site request forgery) tricks a logged-in user's browser into sending an unwanted request, such as changing an email, because the browser automatically attaches the cookie. Defences: use **`SameSite=Lax` or Strict** cookies, send a **CSRF token** with each state-changing form or request, and use POST rather than GET for actions that change things.

**Broken access control** is the number-one risk in many studies. It means a user can do or see something they should not, for example by changing `/orders/101` to `/orders/102` and reading someone else's order. Defences: on **every** request, the server checks that the signed-in user owns or may access that exact record. Never rely on hidden buttons or secret URLs. Use unpredictable ids where helpful, and test your own site by trying to open another user's data."""),
        ("A security checklist for every project", """Before you launch, check:

1. **HTTPS everywhere,** with redirects from HTTP.
2. **Secrets** in environment variables, never in Git, and rotate any that leaked.
3. **Input validated on the server,** output escaped, queries parameterised.
4. **Passwords hashed** with bcrypt or Argon2, with sensible login limits.
5. **Permissions checked on the server** for every action and record.
6. **Cookies** set with HttpOnly, Secure and SameSite.
7. **Security headers** (Content-Security-Policy, X-Content-Type-Options, frame protection).
8. **Dependencies updated.** Run `npm audit` or a similar tool regularly.
9. **Uploads limited** by type and size, and stored safely.
10. **Backups and logs,** and a plan for what to do if something goes wrong.

Only test security on systems you own or have written permission to test. Hacking other people's sites is illegal, even for fun."""),
    ],
    diagram=rings(["Secure hosting and HTTPS", "Validation and escaping", "Authentication and permissions", "Updates, logs and backups", "YOUR USERS' DATA"],
                  note="Layers: if one fails, another still protects."),
    caption="Security works in layers, from HTTPS on the outside to permission checks around your users' data.",
    terms=[("XSS", "An attack where an attacker's script runs in other users' browsers through unescaped text."), ("SQL injection", "An attack that changes a database query by slipping commands into user input."),
           ("Parameterised query", "A query that sends the values separately from the command so input cannot change it."), ("CSRF", "An attack that tricks a logged-in browser into sending an unwanted request."),
           ("Access control", "Checks that decide who may see or change each record.")],
    mistakes=["Building SQL queries by joining strings together.", "Using innerHTML with user text.", "Checking permissions only by hiding buttons.", "Committing secrets or keys to a public repository."],
    quiz=[dict(q="What stops SQL injection most reliably?", o=["Hiding the database", "Parameterised queries", "Long variable names", "A bigger server"], a=1,
               why="Parameterised queries keep values separate from the command."),
          dict(q="What is XSS?", o=["A fast CSS trick", "A database backup", "A type of cookie", "An attack where injected scripts run in other users' browsers"], a=3,
               why="Unescaped user text can become code in someone else's page."),
          dict(q="A user changes /orders/101 to /orders/102 and sees another person's order. What is this?", o=["Good caching", "A CDN feature", "Broken access control", "A CSS bug"], a=2,
               why="The server did not check that the signed-in user owns that record."),
          dict(q="When is it acceptable to test security attacks on a website?", o=["Only sites you own or have written permission to test", "Any site you like", "Competitors' sites", "Never, even on your own"], a=0,
               why="Testing without permission is illegal.")],
    activity="Review one of your own projects against the ten-point checklist, write which items pass and fail, and fix the two most important failures this week.",
)
