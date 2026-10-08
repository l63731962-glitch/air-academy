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