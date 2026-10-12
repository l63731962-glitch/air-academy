"""Small SVG builders shared by every course's lesson pages. Colours match the app theme."""
AR = '<defs><marker id="{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#8A93AD"/></marker></defs>'
COL = ["#00F0FF", "#8A2BE2", "#5b8cff"]
HEAD = '<svg viewBox="0 0 640 {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{a}"><g font-family="Sora,sans-serif" text-anchor="middle">'


def box(x, y, w, h, stroke, title, sub, tc):
    cx = x + w / 2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{stroke}22" stroke="{stroke}"/>'
            f'<text x="{cx}" y="{y + h / 2 - 4}" fill="{tc}" font-size="13" font-weight="700">{title}</text>'
            f'<text x="{cx}" y="{y + h / 2 + 16}" fill="#E8ECF5" font-size="12">{sub}</text>')


def flow(items, aid, note="", loop=False):
    """A row of boxes joined by arrows. items = [(title, 'line one|line two')]. loop=True adds a return arrow."""
    n, gap, h = len(items), 30, 84
    w = (620 - gap * (n - 1)) / n
    pos = [10 + i * (w + gap) for i in range(n)]
    aria = "; ".join(t for t, _ in items) + (". " + note if note else "")
    s = [AR.format(i=aid)] if False else []
    body = [AR.format(i=aid)]
    for i, (t, sub) in enumerate(items):
        c, cx = COL[i % 3], pos[i] + w / 2
        body.append(f'<rect x="{pos[i]:.0f}" y="20" width="{w:.0f}" height="{h}" rx="14" fill="{c}22" stroke="{c}"/>'
                    f'<text x="{cx:.0f}" y="48" fill="{c if i % 3 != 1 else "#c79bff"}" font-size="12.5" font-weight="700">{t}</text>')
        body += [f'<text x="{cx:.0f}" y="{70 + j * 16}" fill="#E8ECF5" font-size="11.5">{ln}</text>' for j, ln in enumerate(sub.split("|"))]
        if i < n - 1:
            body.append(f'<path d="M{pos[i] + w + 3:.0f} {20 + h / 2:.0f}H{pos[i] + w + gap - 3:.0f}" stroke="#8A93AD" stroke-width="2" marker-end="url(#{aid})"/>')
    if loop:
        a, b = pos[-1] + w / 2, pos[0] + w / 2
        body.append(f'<path d="M{a:.0f} {20 + h + 2}C{a:.0f} 150 {b:.0f} 150 {b:.0f} {20 + h + 4}" fill="none" stroke="#FFB86B" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#{aid})"/>')
    if note:
        body.append(f'<text x="320" y="{162 if loop else 142}" fill="#FFB86B" font-size="13">{note}</text>')
    return HEAD.format(h=176 if loop else 156 if note else 130, a=aria) + "".join(body) + "</g></svg>"


def formats():
    """The same facts in four shapes: paragraph, bullet list, table, JSON."""
    body = []
    for i, t in enumerate(["PARAGRAPH", "BULLET LIST", "TABLE", "JSON"]):
        x, c = 10 + i * 158, COL[i % 3]
        body.append(f'<rect x="{x}" y="10" width="146" height="140" rx="16" fill="{c}22" stroke="{c}"/>'
                    f'<text x="{x + 73}" y="34" fill="{c if i % 3 != 1 else "#c79bff"}" font-size="12.5" font-weight="700">{t}</text>')
        if i == 0:
            body += [f'<rect x="{x + 16}" y="{52 + k * 17}" width="{114 if k < 4 else 70}" height="7" rx="3.5" fill="#8A93AD88"/>' for k in range(5)]
        elif i == 1:
            for k in range(4):
                body.append(f'<circle cx="{x + 22}" cy="{59 + k * 22}" r="3.5" fill="{c}"/><rect x="{x + 34}" y="{55 + k * 22}" width="{96 - k * 8}" height="7" rx="3.5" fill="#8A93AD88"/>')
        elif i == 2:
            body.append(f'<rect x="{x + 16}" y="50" width="114" height="86" rx="6" fill="none" stroke="{c}"/><rect x="{x + 16}" y="50" width="114" height="22" rx="6" fill="{c}44"/>')
            body += [f'<path d="M{x + 16} {72 + k * 21}H{x + 130}" stroke="{c}" stroke-opacity=".6"/>' for k in range(3)]
            body += [f'<path d="M{x + 16 + 38 * k} 50V136" stroke="{c}" stroke-opacity=".6"/>' for k in (1, 2)]
        else:
            lines = ['{', '  "name": "Ada",', '  "urgency": "high",', '  "topic": "refund"', '}']
            body += [f'<text x="{x + 16}" y="{58 + k * 17}" text-anchor="start" fill="#8defff" font-family="monospace" font-size="11">{ln.replace(chr(34), "&quot;")}</text>' for k, ln in enumerate(lines)]
    return HEAD.format(h=160, a="The same information shown four ways: as a paragraph, a bullet list, a table and JSON.") + "".join(body) + "</g></svg>"


# ═════════════════════════════════════════════════════════════════════════════════════════════════
# More builders, used by the lesson pages of every other course. Same colours and fonts as above.
# Every builder returns one complete <svg> string. `aid` is a unique id for the arrow marker.
# Text inside boxes: use "|" to start a new line. Keep titles short; boxes are fixed width.
# ═════════════════════════════════════════════════════════════════════════════════════════════════
import html as _html   # noqa: E402
import math as _math   # noqa: E402

_TX, _MUT, _AMB = "#E8ECF5", "#8A93AD", "#FFB86B"


def _e(s):
    return _html.escape(str(s), quote=False)


def _a(s):
    return _html.escape(str(s), quote=True)


def _txc(c):
    return "#c79bff" if c == "#8A2BE2" else c


def _t(x, y, s, fill=_TX, size=11.5, weight=400, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x:.0f}" y="{y:.0f}" fill="{fill}" font-size="{size}" font-weight="{weight}"{a}>{_e(s)}</text>'


def _arrow(x1, y1, x2, y2, aid, color=_MUT, dash=False):
    d = ' stroke-dasharray="5 4"' if dash else ""
    return f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" fill="none" stroke="{color}" stroke-width="2"{d} marker-end="url(#{aid})"/>'


def _svg(h, aria, body, aid=None):
    defs = AR.format(i=aid) if aid else ""
    return (f'<svg viewBox="0 0 640 {h:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{_a(aria)}">{defs}'
            f'<g font-family="Sora,sans-serif" text-anchor="middle">{body}</g></svg>')


def _card(x, y, w, h, c, title, sub=""):
    """A rounded box with a bold title and up to three small lines (separated by |)."""
    cx, lines = x + w / 2, [s for s in sub.split("|") if s]
    out = f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="14" fill="{c}22" stroke="{c}"/>'
    if not lines:
        return out + _t(cx, y + h / 2 + 4, title, _txc(c), 12.5, 700)
    top = y + (h - (18 + 16 * len(lines))) / 2
    out += _t(cx, top + 13, title, _txc(c), 12.5, 700)
    return out + "".join(_t(cx, top + 31 + 16 * j, ln) for j, ln in enumerate(lines))


def stack(layers, aid, note="", both=False, arrows=True):
    """Layers from top to bottom, joined by arrows. both=True draws a down and an up arrow (two-way traffic)."""
    n, bh, gap, x, w = len(layers), 56, 26, 100, 440
    b = []
    for i, (t, s) in enumerate(layers):
        y = 12 + i * (bh + gap)
        b.append(_card(x, y, w, bh, COL[i % 3], t, s))
        if arrows and i < n - 1:
            y2 = y + bh
            if both:
                b += [_arrow(300, y2 + 2, 300, y2 + gap - 3, aid), _arrow(340, y2 + gap - 2, 340, y2 + 3, aid)]
            else:
                b.append(_arrow(320, y2 + 2, 320, y2 + gap - 3, aid))
    h = 12 + n * bh + (n - 1) * gap + 14
    if note:
        b.append(_t(320, h + 12, note, _AMB, 13))
        h += 28
    return _svg(h, "; ".join(t for t, _ in layers) + (". " + note if note else ""), "".join(b), aid)


def compare(left, right, vs="vs", colors=(_AMB, "#00F0FF"), note=""):
    """Two panels side by side. left and right are (title, [short lines])."""
    (lt, ll), (rt, rl) = left, right
    n = max(len(ll), len(rl))
    h = 58 + 24 * n
    b = []
    for x, c, t, lines in ((10, colors[0], lt, ll), (338, colors[1], rt, rl)):
        b.append(f'<rect x="{x}" y="12" width="292" height="{h}" rx="16" fill="{c}22" stroke="{c}"/>')
        b.append(_t(x + 146, 40, t, _txc(c), 13, 700))
        b.append(f'<path d="M{x + 16} 52H{x + 276}" stroke="{c}" stroke-opacity=".5"/>')
        for k, ln in enumerate(lines):
            yy = 76 + 24 * k
            b.append(f'<circle cx="{x + 22}" cy="{yy - 4}" r="3.5" fill="{c}"/>' + _t(x + 34, yy, ln, anchor="start"))
    b.append(f'<circle cx="320" cy="{12 + h / 2:.0f}" r="15" fill="#0D0E15" stroke="{_MUT}"/>' + _t(320, 12 + h / 2 + 4, vs, _MUT, 11, 700))
    hh = h + 24
    if note:
        b.append(_t(320, hh + 14, note, _AMB, 13))
        hh += 30
    return _svg(hh, f"{lt}: " + "; ".join(ll) + f". {rt}: " + "; ".join(rl), "".join(b))


def hub(center, spokes, note=""):
    """One idea in the middle with 2 to 6 related ideas around it. center = (title, sub); spokes = [(title, sub)]."""
    n = len(spokes)
    left_n = (n + 1) // 2
    rh, gap = 52, 16
    rows = max(left_n, n - left_n)
    H = 14 + rows * (rh + gap) - gap + 14
    cy = H / 2
    lines, cards = [], [_card(225, cy - 40, 190, 80, "#00F0FF", *center)]
    for side, items, x in ((0, spokes[:left_n], 10), (1, spokes[left_n:], 460)):
        m = len(items)
        y0 = cy - (m * rh + (m - 1) * gap) / 2
        for k, (t, s) in enumerate(items):
            y = y0 + k * (rh + gap)
            lines.append(f'<path d="M{x + 170 if side == 0 else x} {y + rh / 2:.0f}L{225 if side == 0 else 415} {cy:.0f}" stroke="{_MUT}" stroke-width="1.5" opacity=".75"/>')
            cards.append(_card(x, y, 170, rh, COL[(k + side + 1) % 3], t, s))
    h = H
    if note:
        cards.append(_t(320, H + 14, note, _AMB, 13))
        h += 30
    return _svg(h, f"{center[0]} connected to " + "; ".join(t for t, _ in spokes), "".join(lines) + "".join(cards))


def timeline(steps, note=""):
    """3 to 6 numbered steps along a line, labels alternating above and below. steps = [(title, sub)]."""
    n = len(steps)
    xs = [60 + i * (520 / (n - 1)) for i in range(n)]
    b = [f'<path d="M24 100H616" stroke="{_MUT}" stroke-width="2"/>']
    for i, ((t, s), x) in enumerate(zip(steps, xs)):
        c = COL[i % 3]
        up = i % 2 == 0
        b.append(f'<path d="M{x:.0f} {87 if up else 113}V{72 if up else 128}" stroke="{c}" stroke-width="1.5"/>')
        b.append(f'<circle cx="{x:.0f}" cy="100" r="13" fill="{c}33" stroke="{c}" stroke-width="2"/>' + _t(x, 105, str(i + 1), _txc(c), 12, 700))
        subs = [q for q in s.split("|") if q]
        ty = 64 - 16 * len(subs) if up else 148
        b.append(_t(x, ty, t, _txc(c), 12.5, 700) + "".join(_t(x, ty + 16 * (j + 1), q) for j, q in enumerate(subs)))
    h = 196
    if note:
        b.append(_t(320, h + 6, note, _AMB, 13))
        h += 28
    return _svg(h, "; ".join(f"{i + 1} {t}" for i, (t, _) in enumerate(steps)) + (". " + note if note else ""), "".join(b))


def grid(cards, cols=3, note=""):
    """A tidy grid of small cards. cards = [(title, 'line one|line two')]."""
    gap, ch = 14, 74
    w = (620 - gap * (cols - 1)) / cols
    rows = -(-len(cards) // cols)
    b = [_card(10 + (i % cols) * (w + gap), 12 + (i // cols) * (ch + gap), w, ch, COL[(i + i // cols) % 3], t, s) for i, (t, s) in enumerate(cards)]
    h = 12 + rows * (ch + gap)
    if note:
        b.append(_t(320, h + 6, note, _AMB, 13))
        h += 28
    return _svg(h, "; ".join(t for t, _ in cards) + (". " + note if note else ""), "".join(b))


def cycle(items, aid, center="", note=""):
    """3 to 6 steps around a loop. center text may use | for a second line."""
    n, cx, cy, rx, ry, bw, bh = len(items), 320, 126, 232, 88, 150, 46
    ang = [-_math.pi / 2 + i * 2 * _math.pi / n for i in range(n)]
    pt = lambda a: (cx + rx * _math.cos(a), cy + ry * _math.sin(a))
    d, b = 0.36, []
    for i in range(n):
        x1, y1 = pt(ang[i] + d)
        x2, y2 = pt(ang[(i + 1) % n] - d + (2 * _math.pi if i == n - 1 else 0))
        b.append(f'<path d="M{x1:.0f} {y1:.0f}A{rx} {ry} 0 0 1 {x2:.0f} {y2:.0f}" fill="none" stroke="{_MUT}" stroke-width="2" marker-end="url(#{aid})"/>')
    for i, (t, s) in enumerate(items):
        x, y = pt(ang[i])
        b.append(_card(x - bw / 2, y - bh / 2, bw, bh, COL[i % 3], t, s))
    for j, ln in enumerate(center.split("|") if center else []):
        b.append(_t(cx, cy - 4 + j * 18, ln, _AMB if j == 0 else _TX, 13 if j == 0 else 11.5, 700 if j == 0 else 400))
    h = 252
    if note:
        b.append(_t(320, h + 6, note, _AMB, 13))
        h += 28
    return _svg(h, "A loop: " + ", then ".join(t for t, _ in items) + (". " + note if note else ""), "".join(b), aid)


def seq(actors, msgs, aid, note=""):
    """A sequence diagram. actors = [names]; msgs = [(from_index, to_index, text)]. Right-to-left arrows are drawn dashed."""
    n = len(actors)
    xs = [100 + i * (440 / (n - 1)) for i in range(n)]
    h = 70 + 36 * len(msgs)
    b = []
    for i, (name, x) in enumerate(zip(actors, xs)):
        b.append(f'<path d="M{x:.0f} 46V{h - 10}" stroke="{_MUT}" stroke-width="1.5" stroke-dasharray="4 5" opacity=".7"/>')
        b.append(_card(x - 66, 10, 132, 36, COL[i % 3], name))
    for k, (f, t, text) in enumerate(msgs):
        y = 76 + 36 * k
        back = xs[t] < xs[f]
        x1, x2 = xs[f] + (-4 if back else 4), xs[t] + (4 if back else -4)
        b.append(_arrow(x1, y, x2, y, aid, "#FFB86B" if back else _MUT, dash=back))
        b.append(_t((xs[f] + xs[t]) / 2, y - 7, f"{k + 1}. {text}", _AMB if back else _TX, 11))
    if note:
        b.append(_t(320, h + 8, note, _AMB, 13))
        h += 30
    return _svg(h, " ".join(f"{k + 1}. {actors[f]} to {actors[t]}: {x}." for k, (f, t, x) in enumerate(msgs)), "".join(b), aid)


def rings(layers, note=""):
    """Layers of protection, outside to inside. The last item is the core being protected. Each is (title, sub-less)."""
    n = len(layers) - 1
    H = 90 + 44 * n
    b = []
    for k, t in enumerate(layers[:-1]):
        c = COL[k % 3]
        b.append(f'<rect x="{10 + 36 * k}" y="{10 + 30 * k}" width="{620 - 72 * k}" height="{H - 20 - 44 * k}" rx="{20 - k * 2}" fill="{c}14" stroke="{c}"/>')
        b.append(_t(320, 10 + 30 * k + 19, t, _txc(c), 12.5, 700))
    c = COL[n % 3]
    b.append(f'<rect x="{10 + 36 * n}" y="{10 + 30 * n}" width="{620 - 72 * n}" height="70" rx="14" fill="{c}33" stroke="{c}" stroke-width="2"/>')
    b.append(_t(320, 10 + 30 * n + 40, layers[-1], "#fff", 14, 700))
    h = H
    if note:
        b.append(_t(320, H + 8, note, _AMB, 13))
        h += 30
    return _svg(h, "Layers of protection from the outside in: " + ", ".join(layers) + (". " + note if note else ""), "".join(b))


def pyramid(levels, note=""):
    """A pyramid. levels = [(title, sub)] from the top (small) to the bottom (wide)."""
    n, lh = len(levels), 58
    b = []
    for i, (t, s) in enumerate(levels):
        c = COL[i % 3]
        y = 12 + i * (lh + 4)
        t0, t1 = 70 + i * (230 / n), 70 + (i + 1) * (230 / n)
        b.append(f'<path d="M{320 - t0:.0f} {y}H{320 + t0:.0f}L{320 + t1:.0f} {y + lh}H{320 - t1:.0f}z" fill="{c}22" stroke="{c}"/>')
        b.append(_t(320, y + 25, t, _txc(c), 12.5, 700) + _t(320, y + 43, s))
    h = 12 + n * (lh + 4) + 4
    if note:
        b.append(_t(320, h + 12, note, _AMB, 13))
        h += 30
    return _svg(h, "A pyramid from top to bottom: " + "; ".join(t for t, _ in levels) + (". " + note if note else ""), "".join(b))


def bars(items, note="", unit=""):
    """Horizontal bars. items = [(label, value)] or [(label, value, colour)]."""
    top = max(v for _, v, *_ in items)
    b = []
    for i, it in enumerate(items):
        lab, v = it[0], it[1]
        c = it[2] if len(it) > 2 else COL[i % 3]
        y = 14 + i * 44
        w = max(6, 360 * v / top)
        b.append(_t(176, y + 21, lab, _TX, 12, anchor="end"))
        b.append(f'<rect x="188" y="{y}" width="{w:.0f}" height="30" rx="8" fill="{c}44" stroke="{c}"/>')
        b.append(_t(188 + w + 10, y + 20, f"{v}{unit}", _txc(c), 12, 700, "start"))
    h = 14 + len(items) * 44
    if note:
        b.append(_t(320, h + 8, note, _AMB, 13))
        h += 30
    return _svg(h, "Bar chart: " + "; ".join(f"{it[0]} {it[1]}{unit}" for it in items) + (". " + note if note else ""), "".join(b))


def tree(root, kids, note=""):
    """A two-level tree. root = title; kids = [(title, [small leaf labels])]."""
    n, gap = len(kids), 16
    w = (620 - gap * (n - 1)) / n
    deepest = max(len(g) for _, g in kids)
    b = [f'<path d="M320 56V74" stroke="{_MUT}" stroke-width="1.5"/>']
    xs = [10 + i * (w + gap) + w / 2 for i in range(n)]
    b.append(f'<path d="M{xs[0]:.0f} 74H{xs[-1]:.0f}" stroke="{_MUT}" stroke-width="1.5"/>')
    b.append(_card(210, 12, 220, 44, COL[0], root))
    for i, ((t, leaves), x) in enumerate(zip(kids, xs)):
        c = COL[(i + 1) % 3]
        b.append(f'<path d="M{x:.0f} 74V92" stroke="{_MUT}" stroke-width="1.5"/>')
        b.append(_card(x - w / 2, 92, w, 44, c, t))
        for k, leaf in enumerate(leaves):
            y = 152 + k * 40
            b.append(f'<path d="M{x:.0f} {y - 16 if k else 136}V{y}" stroke="{_MUT}" stroke-width="1.2"/>')
            b.append(f'<rect x="{x - w / 2 + 8:.0f}" y="{y}" width="{w - 16:.0f}" height="30" rx="10" fill="{c}14" stroke="{c}" stroke-opacity=".7"/>' + _t(x, y + 19, leaf, _TX, 11))
    h = 152 + deepest * 40 + 4
    if note:
        b.append(_t(320, h + 10, note, _AMB, 13))
        h += 30
    return _svg(h, root + " contains " + "; ".join(t for t, _ in kids) + (". " + note if note else ""), "".join(b))


def triangle(corners, middle="", note=""):
    """A three-way trade-off. corners = [top, bottom-left, bottom-right] as (title, sub)."""
    b = [f'<path d="M320 58L118 198H522z" fill="#8A2BE211" stroke="{_MUT}" stroke-dasharray="5 4"/>']
    for (t, s), (x, y), c in zip(corners, ((245, 8), (28, 190), (462, 190)), COL):
        b.append(_card(x, y, 150, 50, c, t, s))
    for j, ln in enumerate(middle.split("|")):
        b.append(_t(320, 140 + j * 18, ln, _AMB if j == 0 else _TX, 12.5 if j == 0 else 11.5, 700 if j == 0 else 400))
    h = 252
    if note:
        b.append(_t(320, h + 6, note, _AMB, 13))
        h += 28
    return _svg(h, "A trade-off between " + ", ".join(t for t, _ in corners) + (". " + note if note else ""), "".join(b))


def curve(points, note="", ylabel="Intensity"):
    """A line over time. points = [(label, 0..1)]. Used for pacing and difficulty."""
    n = len(points)
    xs = [60 + i * (520 / (n - 1)) for i in range(n)]
    ys = [190 - 150 * v for _, v in points]
    line = "".join(("M" if i == 0 else "L") + f"{x:.0f} {y:.0f}" for i, (x, y) in enumerate(zip(xs, ys)))
    b = [f'<path d="M40 196H610" stroke="{_MUT}"/><path d="M40 30V196" stroke="{_MUT}"/>',
         f'<path d="{line}L{xs[-1]:.0f} 196L{xs[0]:.0f} 196z" fill="#00F0FF18"/>',
         f'<path d="{line}" fill="none" stroke="#00F0FF" stroke-width="3" stroke-linejoin="round"/>',
         _t(44, 24, ylabel, _MUT, 11, anchor="start")]
    for i, ((lab, v), x, y) in enumerate(zip(points, xs, ys)):
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="#0D0E15" stroke="{COL[i % 3]}" stroke-width="2.5"/>' + _t(x, 218, lab, _txc(COL[i % 3]), 11.5, 700))
    h = 232
    if note:
        b.append(_t(320, h + 8, note, _AMB, 13))
        h += 30
    return _svg(h, "A line over time: " + ", ".join(l for l, _ in points) + (". " + note if note else ""), "".join(b))


def fsm(nodes, edges, aid, note=""):
    """A state diagram. nodes = [(name, gx, gy)] with gx, gy between 0 and 1; edges = [(from, to, label)]."""
    bw, bh = 118, 40
    pos = [(80 + gx * 480, 34 + gy * 150) for _, gx, gy in nodes]
    b = []
    for i, (name, _, _) in enumerate(nodes):
        b.append(_card(pos[i][0] - bw / 2, pos[i][1] - bh / 2, bw, bh, COL[i % 3], name))
    both = {(f, t) for f, t, _ in edges}
    for f, t, lab in edges:
        (x1, y1), (x2, y2) = pos[f], pos[t]
        dx, dy = x2 - x1, y2 - y1
        L = _math.hypot(dx, dy) or 1
        k1 = min((bw / 2 + 3) / abs(dx) if dx else 9e9, (bh / 2 + 3) / abs(dy) if dy else 9e9)
        k2 = min((bw / 2 + 6) / abs(dx) if dx else 9e9, (bh / 2 + 6) / abs(dy) if dy else 9e9)
        ox, oy = (-dy / L * 9, dx / L * 9) if (t, f) in both else (0, 0)
        sx, sy, ex, ey = x1 + dx * k1 + ox, y1 + dy * k1 + oy, x2 - dx * k2 + ox, y2 - dy * k2 + oy
        b.append(_arrow(sx, sy, ex, ey, aid))
        b.append(_t((sx + ex) / 2 + ox * 1.6, (sy + ey) / 2 + oy * 1.6 - 5, lab, _AMB, 10.5))
    h = 34 + 150 + 40
    if note:
        b.append(_t(320, h + 6, note, _AMB, 13))
        h += 28
    return _svg(h, "States: " + ", ".join(n for n, _, _ in nodes) + (". " + note if note else ""), "".join(b), aid)


# ───────────── Illustrated scenes ─────────────

def spacing():
    """Animation: even spacing (robotic) against ease-in spacing (a ball speeding up as it falls)."""
    b = []
    for cx, title, sub, ease, c in ((165, "EVEN SPACING", "Looks robotic and floaty", False, _AMB), (495, "EASE IN", "Looks like gravity", True, "#00F0FF")):
        b.append(_t(cx, 22, title, _txc(c), 12.5, 700))
        b.append(f'<path d="M{cx} 36V214" stroke="{_MUT}" stroke-dasharray="3 5" opacity=".6"/><path d="M{cx - 90} 222H{cx + 90}" stroke="{_MUT}" stroke-width="2"/>')
        for k in range(8):
            y = 48 + (168 * (k / 7) ** 2 if ease else 24 * k)
            b.append(f'<circle cx="{cx}" cy="{y:.0f}" r="10" fill="{c}{"66" if k == 7 else "33"}" stroke="{c}"/>')
        b.append(_t(cx, 246, sub, _TX, 12))
    return _svg(262, "Two columns of falling balls. On the left the gaps are equal, which looks robotic. On the right the gaps grow as the ball falls, which looks like gravity.", "".join(b))


def keyframes():
    """2D animation: you draw the keys, the in-betweens fill the gaps."""
    b, xs = [], [48 + i * 68 for i in range(9)]
    for i, x in enumerate(xs):
        key = i % 4 == 0
        y = 118 - 78 * _math.sin(_math.pi * i / 8)
        c = "#00F0FF" if key else _MUT
        b.append(f'<circle cx="{x}" cy="{y:.0f}" r="{13 if key else 9}" fill="{c}{"44" if key else "11"}" stroke="{c}" stroke-width="{2.5 if key else 1.5}"{"" if key else " stroke-dasharray=" + chr(34) + "3 3" + chr(34)}/>')
        b.append(f'<rect x="{x - 24}" y="150" width="48" height="34" rx="8" fill="{c}{"33" if key else "11"}" stroke="{c}"/>' + _t(x, 172, str(i + 1), _txc(c), 12, 700 if key else 400))
        b.append(_t(x, 204, "KEY" if key else "between", _txc(c) if key else _MUT, 11 if key else 9.5, 700 if key else 400))
    b.append(_t(320, 232, "You draw the key poses first. The in-betweens fill the gaps and set the timing.", _AMB, 13))
    return _svg(246, "Nine frames in a row. Frames 1, 5 and 9 are key poses of a ball arc. The frames between them are in-betweens.", "".join(b))


def shots():
    """Cinematography: wide, medium and close-up."""
    b = []
    for i, (x, name, q) in enumerate(((10, "WIDE SHOT", "Where are we?"), (225, "MEDIUM SHOT", "Who is talking?"), (440, "CLOSE-UP", "How do they feel?"))):
        c = COL[i]
        b.append(f'<rect x="{x}" y="14" width="190" height="130" rx="12" fill="#0D0E15" stroke="{c}" stroke-width="2"/>')
        cx = x + 95
        if i == 0:
            b.append(f'<path d="M{x + 2} 118H{x + 188}" stroke="{_MUT}"/><path d="M{x + 12} 118L{x + 50} 92L{x + 86} 118M{x + 120} 118L{x + 150} 98L{x + 180} 118" fill="none" stroke="{_MUT}"/>')
            b.append(f'<circle cx="{cx}" cy="96" r="5" fill="{c}"/><path d="M{cx} 101V112M{cx - 5} 118L{cx} 112L{cx + 5} 118M{cx - 5} 105H{cx + 5}" stroke="{c}" stroke-width="2" fill="none"/>')
        elif i == 1:
            b.append(f'<circle cx="{cx}" cy="58" r="17" fill="{c}33" stroke="{c}" stroke-width="2"/><path d="M{cx - 34} 144V104Q{cx - 34} 82 {cx} 82Q{cx + 34} 82 {cx + 34} 104V144" fill="{c}22" stroke="{c}" stroke-width="2"/>')
        else:
            b.append(f'<circle cx="{cx}" cy="82" r="50" fill="{c}22" stroke="{c}" stroke-width="2"/><circle cx="{cx - 18}" cy="74" r="5" fill="{c}"/><circle cx="{cx + 18}" cy="74" r="5" fill="{c}"/><path d="M{cx - 16} 98Q{cx} 110 {cx + 16} 98" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>')
        b.append(_t(cx, 170, name, _txc(c), 12.5, 700) + _t(cx, 188, q))
    b.append(_t(320, 222, "Closer to make them feel. Wider to help them understand.", _AMB, 13))
    return _svg(236, "Three camera shots of the same person: a wide shot that shows the place, a medium shot that shows who is talking, and a close-up that shows emotion.", "".join(b))


def responsibility():
    """Cloud: who manages what in on-premises, IaaS, PaaS and SaaS."""
    cols = ["On-premises", "IaaS", "PaaS", "SaaS"]
    rows = [("Application", [1, 1, 1, 0]), ("Data", [1, 1, 1, 1]), ("Runtime", [1, 1, 0, 0]), ("Operating system", [1, 1, 0, 0]),
            ("Servers and storage", [1, 0, 0, 0]), ("Data centre and network", [1, 0, 0, 0])]
    b = [_t(105, 28, "Who manages it?", _MUT, 11, 700)]
    for j, name in enumerate(cols):
        b.append(_t(257 + j * 108, 28, name, _txc(COL[j % 3]), 12.5, 700))
    for i, (lab, vals) in enumerate(rows):
        y = 42 + i * 36
        b.append(_t(14, y + 21, lab, _TX, 12, anchor="start"))
        for j, v in enumerate(vals):
            c = _AMB if v else "#00F0FF"
            b.append(f'<rect x="{206 + j * 108}" y="{y}" width="100" height="30" rx="8" fill="{c}{"33" if v else "22"}" stroke="{c}"/>' + _t(256 + j * 108, y + 20, "You" if v else "Provider", _txc(c), 11.5, 700))
    b.append(_t(320, 276, "Further right: the provider runs more, and you control less.", _AMB, 13))
    return _svg(292, "A table showing who manages each layer for on-premises, IaaS, PaaS and SaaS. On premises you manage everything. In IaaS you manage the operating system and above. In PaaS you manage the application and data. In SaaS you only manage your data and settings.", "".join(b))


def network(aid="net"):
    """Cloud: a VPC with a public and a private subnet."""
    b = [f'<rect x="150" y="10" width="480" height="300" rx="20" fill="#5b8cff0d" stroke="#5b8cff" stroke-width="2"/>', _t(166, 32, "VPC  10.0.0.0/16", "#5b8cff", 12, 700, "start"),
         f'<rect x="172" y="46" width="436" height="118" rx="14" fill="#00F0FF14" stroke="#00F0FF" stroke-dasharray="5 4"/>', _t(186, 66, "PUBLIC SUBNET  10.0.1.0/24", "#00F0FF", 11, 700, "start"),
         f'<rect x="172" y="178" width="436" height="122" rx="14" fill="#8A2BE214" stroke="#8A2BE2" stroke-dasharray="5 4"/>', _t(596, 198, "PRIVATE SUBNET  10.0.2.0/24", "#c79bff", 11, 700, "end"),
         _card(10, 96, 100, 58, "#FFB86B", "INTERNET", "via gateway"),
         _card(196, 78, 160, 54, "#00F0FF", "Load balancer", "public entrance"), _card(424, 78, 160, 54, "#5b8cff", "NAT gateway", "outbound only"),
         _card(196, 212, 160, 54, "#8A2BE2", "App server", "no public address"), _card(424, 212, 160, 54, "#8A2BE2", "Database", "private data"),
         _arrow(112, 112, 194, 108, aid), _arrow(276, 134, 276, 210, aid), _arrow(358, 240, 422, 240, aid),
         _arrow(330, 212, 440, 134, aid, _AMB, True), _t(420, 180, "updates out", _AMB, 10)]
    return _svg(322, "A cloud network. Internet users reach a load balancer in the public subnet. The load balancer passes traffic to an app server in the private subnet, which talks to a database. A NAT gateway lets the private app server reach the internet for updates.", "".join(b), aid)


def phones():
    """App design: three screens joined by taps."""
    b = []
    names = [("1  LIST", "Home"), ("2  DETAIL", "One item"), ("3  NEW", "Add form")]
    for i, ((n, _), x) in enumerate(zip(names, (40, 255, 470))):
        c = COL[i]
        b.append(f'<rect x="{x}" y="10" width="130" height="236" rx="20" fill="#0D0E15" stroke="{c}" stroke-width="2"/><rect x="{x + 45}" y="17" width="40" height="5" rx="2.5" fill="{c}"/>')
        if i == 0:
            for k in range(4):
                b.append(f'<rect x="{x + 12}" y="{36 + k * 38}" width="106" height="30" rx="8" fill="{c}22" stroke="{c}" stroke-opacity=".7"/><circle cx="{x + 28}" cy="{51 + k * 38}" r="7" fill="{c}"/><rect x="{x + 42}" y="{47 + k * 38}" width="62" height="7" rx="3.5" fill="#8A93AD88"/>')
            b.append(f'<path d="M{x + 8} 196H{x + 122}" stroke="{c}" stroke-opacity=".5"/>' + "".join(f'<circle cx="{x + 30 + m * 35}" cy="220" r="8" fill="{c if m == 0 else "#8A93AD55"}"/>' for m in range(3)))
        elif i == 1:
            b.append(f'<rect x="{x + 12}" y="36" width="106" height="78" rx="10" fill="{c}22" stroke="{c}"/><path d="M{x + 24} 100L{x + 52} 70L{x + 74} 90L{x + 92} 76L{x + 106} 100" fill="none" stroke="{c}" stroke-width="2"/>')
            b.append("".join(f'<rect x="{x + 14}" y="{128 + k * 16}" width="{100 - k * 18}" height="7" rx="3.5" fill="#8A93AD88"/>' for k in range(3)))
            b.append(f'<rect x="{x + 14}" y="196" width="102" height="32" rx="16" fill="{c}" />' + _t(x + 65, 217, "ORDER", "#04121a", 11.5, 700))
        else:
            for k in range(3):
                b.append(f'<rect x="{x + 12}" y="{40 + k * 48}" width="106" height="34" rx="8" fill="none" stroke="{c}"/>' + _t(x + 22, 62 + k * 48, ["Name", "Price", "Photo"][k], _MUT, 10.5, anchor="start"))
            b.append(f'<rect x="{x + 14}" y="196" width="102" height="32" rx="16" fill="{c}"/>' + _t(x + 65, 217, "SAVE", "#04121a", 11.5, 700))
        b.append(_t(x + 65, 268, n, _txc(c), 12.5, 700))
    b += [_arrow(176, 128, 250, 128, "ph"), _t(213, 118, "tap item", _AMB, 10.5), _arrow(392, 150, 466, 150, "ph"), _t(429, 140, "tap Add", _AMB, 10.5)]
    return _svg(284, "Three phone screens. A list screen leads to a detail screen when an item is tapped, and a new item form when Add is tapped.", "".join(b), "ph")


def boxmodel():
    """CSS box model: content, padding, border, margin."""
    b = [f'<rect x="120" y="10" width="400" height="236" rx="14" fill="{_AMB}14" stroke="{_AMB}" stroke-dasharray="5 4"/>', _t(138, 32, "MARGIN  space outside the box", _AMB, 11, 700, "start"),
         '<rect x="160" y="46" width="320" height="168" rx="10" fill="#8A2BE222" stroke="#8A2BE2" stroke-width="3"/>', _t(176, 68, "BORDER", "#c79bff", 11, 700, "start"),
         '<rect x="190" y="78" width="260" height="106" rx="8" fill="#5b8cff22" stroke="#5b8cff"/>', _t(206, 98, "PADDING  space inside", "#5b8cff", 11, 700, "start"),
         '<rect x="226" y="110" width="188" height="48" rx="6" fill="#00F0FF33" stroke="#00F0FF" stroke-width="2"/>', _t(320, 131, "CONTENT", "#00F0FF", 12.5, 700), _t(320, 148, "text, image or button")]
    return _svg(258, "The CSS box model: content in the middle, then padding, then the border, then margin on the outside.", "".join(b))


def erd():
    """Databases: two tables joined by a foreign key."""
    def table(x, name, rows, c):
        out = f'<rect x="{x}" y="14" width="210" height="{34 + 28 * len(rows)}" rx="12" fill="{c}14" stroke="{c}"/><rect x="{x}" y="14" width="210" height="34" rx="12" fill="{c}44"/>' + _t(x + 105, 36, name, _txc(c), 13, 700)
        for k, (col, tag) in enumerate(rows):
            y = 48 + 28 * k
            out += f'<path d="M{x} {y}H{x + 210}" stroke="{c}" stroke-opacity=".4"/>' + _t(x + 14, y + 19, col, _TX, 12, anchor="start") + (_t(x + 196, y + 19, tag, _AMB, 11, 700, "end") if tag else "")
        return out
    b = [table(40, "users", [("id", "PK"), ("name", ""), ("email", "")], "#00F0FF"), table(390, "notes", [("id", "PK"), ("user_id", "FK"), ("title", ""), ("body", "")], "#8A2BE2"),
         f'<path d="M250 104H390" stroke="{_AMB}" stroke-width="2"/>', _t(262, 96, "1", _AMB, 13, 700), _t(374, 96, "many", _AMB, 12, 700, "end"),
         _t(320, 214, "One user has many notes. The user_id column links each note to its owner.", _AMB, 13)]
    return _svg(232, "Two database tables. The users table has id, name and email. The notes table has id, user_id, title and body. One user has many notes, linked through user_id.", "".join(b))
