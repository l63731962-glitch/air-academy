"""Schema check for a lessons_*.py file. Usage: python check_lessons.py lessons_2d_animation 5
For the files that add lessons to a course that already had some: python check_lessons.py lessons_web_more 24 9   (keys 9 to 24, each with an "activity")
Exits non-zero and prints every problem it finds, so a content writer can fix them all in one pass."""
import importlib, sys, xml.etree.ElementTree as ET

mod, count = sys.argv[1], int(sys.argv[2])
start = int(sys.argv[3]) if len(sys.argv) > 3 else 1
m = importlib.import_module(mod)
L, bad = m.LESSONS, []
def need(cond, msg):
    if not cond: bad.append(msg)

need(sorted(L) == list(range(start, count + 1)), f"LESSONS keys must be {start}..{count}, got {sorted(L)}")
KEYS = {"minutes", "hook", "sections", "diagram", "caption", "terms", "mistakes", "quiz"}
for n, c in sorted(L.items()):
    p = f"lesson {n}: "
    keys = KEYS | ({"activity"} if "activity" in c or start > 1 else set())
    need(set(c) == keys, p + f"keys differ: missing {keys - set(c)} extra {set(c) - keys}")
    if set(c) != keys: continue
    if "activity" in c:
        need(isinstance(c["activity"], str) and 30 <= len(c["activity"]) <= 300 and "|" not in c["activity"], p + "activity must be one sentence of 30-300 characters with no | in it")
        need("|" not in c["caption"] and all("|" not in h and ";" not in h for h, _ in c["sections"] if isinstance(h, str)), p + "caption and section headings must not contain | or ; (they build the lesson note)")
    need(isinstance(c["minutes"], int) and 8 <= c["minutes"] <= 20, p + "minutes must be an int from 8 to 20")
    need(isinstance(c["hook"], str) and 250 <= len(c["hook"]) <= 900, p + f"hook length {len(c['hook'])} should be 250-900 characters")
    need(isinstance(c["sections"], list) and 4 <= len(c["sections"]) <= 6, p + "4 to 6 sections")
    for i, s in enumerate(c["sections"]):
        need(isinstance(s, tuple) and len(s) == 2 and all(isinstance(x, str) and x.strip() for x in s), p + f"section {i+1} must be a (heading, body) tuple of strings")
        if isinstance(s, tuple) and len(s) == 2: need(len(s[1]) >= 350, p + f"section {i+1} body is thin ({len(s[1])} chars, want 350+)")
    total = sum(len(s[1]) for s in c["sections"] if isinstance(s, tuple) and len(s) == 2)
    need(total >= 2100, p + f"sections total only {total} chars, want 2100+ (aim for about 3000)")
    try:
        ET.fromstring(c["diagram"]); need(c["diagram"].lstrip().startswith("<svg"), p + "diagram must start with <svg")
    except Exception as e:
        bad.append(p + f"diagram is not valid SVG/XML: {e}")
    need(isinstance(c["caption"], str) and 20 <= len(c["caption"]) <= 200, p + "caption 20-200 chars")
    need(isinstance(c["terms"], list) and 5 <= len(c["terms"]) <= 8 and all(isinstance(t, tuple) and len(t) == 2 and all(isinstance(x, str) and x for x in t) for t in c["terms"]), p + "5-8 terms, each a (term, meaning) tuple")
    need(isinstance(c["mistakes"], list) and 3 <= len(c["mistakes"]) <= 5 and all(isinstance(x, str) and x for x in c["mistakes"]), p + "3-5 mistakes (strings)")
    q = c["quiz"]
    need(isinstance(q, list) and len(q) == 4, p + "exactly 4 quiz questions")
    for i, x in enumerate(q if isinstance(q, list) else []):
        ok = isinstance(x, dict) and set(x) == {"q", "o", "a", "why"} and isinstance(x["o"], list) and len(x["o"]) == 4 and all(isinstance(o, str) and o for o in x["o"]) and isinstance(x["a"], int) and 0 <= x["a"] <= 3 and isinstance(x["q"], str) and isinstance(x["why"], str) and x["q"] and x["why"]
        need(ok, p + f"quiz {i+1} must be dict(q=str, o=[4 strings], a=0..3, why=str)")
        if ok: need(len(set(o.strip().lower() for o in x["o"])) == 4, p + f"quiz {i+1} has duplicate options")
    need(len({x["a"] for x in q if isinstance(x, dict) and "a" in x}) >= 2, p + "quiz answers should not all be the same position")
    blob = repr(c)
    need("—" not in blob and "–" not in blob, p + "no em or en dashes: use commas, colons or full stops")
if hasattr(m, "NOTES") and start == 1:
    N = m.NOTES
    need(isinstance(N, list) and len(N) == count and all(isinstance(s, str) and s.count("|") == 2 for s in N), f"NOTES must be a list of {count} strings shaped 'goal | point; point; point | activity'")
print("\n".join(bad) if bad else f"OK: {mod} has {count} valid lessons")
sys.exit(1 if bad else 0)
