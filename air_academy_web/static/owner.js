'use strict';
/* Control Room: the owner's private page (live users, running costs, sales).
 * It only loads when the owner taps the button, and every number comes from /api/owner/*, which answers 404 to everyone else.
 * Costs are estimates built from the provider price lists; the Render, Supabase and Resend figures are the plans you enter under Plans. */
(function () {
  const PLAN_NOTE = 'OpenAI amounts are estimated from token counts at the public price list, so check platform.openai.com for the exact bill.';
  const num = (n) => Number(n || 0).toLocaleString('en-US');
  const usd = (n) => { n = Number(n || 0); return '$' + n.toLocaleString('en-US', { minimumFractionDigits: n > 0 && n < 1 ? 3 : 2, maximumFractionDigits: n > 0 && n < 1 ? 3 : 2 }); };
  const ngn = (n, rate) => '₦' + Math.round(Number(n || 0) * rate).toLocaleString('en-NG');
  const both = (n) => `${usd(n)} <small>${ngn(n, D.money.usdNgn)}</small>`;
  const mb = (b) => b >= 1073741824 ? (b / 1073741824).toFixed(2) + ' GB' : (b / 1048576).toFixed(b < 1e7 ? 1 : 0) + ' MB';
  const ago = (s) => (s < 5 ? 'just now' : s < 90 ? s + 's ago' : Math.round(s / 60) + ' min ago');
  const when = (iso) => { try { return new Date(iso).toLocaleString('en-GB', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' }); } catch (_) { return iso || ''; } };
  const CHIP = { ok: 'OK', warn: 'Watch', bad: 'Act now' };
  let D = null, root = null, tLive = null, tAll = null, tWi = null, wiN = 3, wiBuy = 10, popped = false;
  const STEPS = [10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000];
  const q = (s) => root.querySelector(s);
  const put = (id, html) => { const e = q('#' + id); if (e) e.innerHTML = html; };
  const level = (used, limit) => (!limit ? 'ok' : used >= limit ? 'bad' : used >= 0.8 * limit ? 'warn' : 'ok');

  function gauge(label, used, limit, fmt, sub) {
    const lv = level(used, limit), pct = limit ? Math.min(100, (used / limit) * 100) : 0;
    return `<div class="cr-g ${lv}"><div class="cr-gt"><span>${label}</span><span class="cr-chip ${lv}">${CHIP[lv]}</span></div>
      <div class="cr-gv">${fmt(used)}${limit ? ` <em>of ${fmt(limit)}</em>` : ''}</div>
      <div class="cr-bar" role="progressbar" aria-label="${esc(label)}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${Math.round(pct)}"><i style="width:${pct}%"></i></div>
      <small>${sub || ''}</small></div>`;
  }

  function spark(series) {
    const w = 290, h = 54, max = Math.max(3, ...series), step = w / (series.length - 1);
    const pts = series.map((v, i) => `${(i * step).toFixed(1)},${(h - 2 - (v / max) * (h - 8)).toFixed(1)}`);
    return `<svg class="cr-spark" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" role="img" aria-label="Students online over the last 24 hours, busiest ${Math.max(0, ...series)}">
      <polygon points="0,${h} ${pts.join(' ')} ${w},${h}" fill="rgba(0,240,255,.16)"/><polyline points="${pts.join(' ')}" fill="none" stroke="var(--cyan)" stroke-width="1.6" vector-effect="non-scaling-stroke"/></svg>
      <div class="cr-axis"><span>24 hours ago</span><span>12 hours</span><span>now</span></div>`;
  }

  function bars(rows, key, fmt, label) {
    if (!rows.length) return '<p class="cr-none">Nothing yet this month.</p>';
    const max = Math.max(...rows.map((r) => r[key]), 0.0001), w = 290, h = 64, bw = Math.min(14, Math.max(3, w / rows.length - 2));
    return `<svg class="cr-bars" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" role="img" aria-label="${label}">${rows.map((r, i) =>
      `<rect x="${(i * (w / rows.length)).toFixed(1)}" y="${(h - 2 - (r[key] / max) * (h - 6)).toFixed(1)}" width="${bw.toFixed(1)}" height="${((r[key] / max) * (h - 6) + 1).toFixed(1)}" rx="1.5" fill="var(--cyan)"><title>${esc(r.day)}: ${fmt(r[key])}</title></rect>`).join('')}</svg>
      <div class="cr-axis"><span>${esc(rows[0].day.slice(5))}</span><span>${esc(rows[rows.length - 1].day.slice(5))}</span></div>`;
  }

  /* ── sections that change as numbers change ── */
  function liveHTML(L) {
    const people = L.people.length ? `<ul class="cr-people">${L.people.map((p) => `<li><b>${esc(p.name)}</b><span>${esc(p.place || '')}</span><em>${ago(p.ago)}</em></li>`).join('')}</ul>`
      : '<p class="cr-none">Nobody signed in right now.</p>';
    return `<div class="cr-live"><div class="cr-big"><i class="ld"></i><b>${L.now}</b><span>${L.now === 1 ? 'person' : 'people'} using the app right now</span></div>
      <div class="cr-sub"><span><b>${L.signedIn}</b> signed in</span><span><b>${L.visitors}</b> on the sign-in page</span><span>Busiest today: <b>${L.peakToday}</b></span></div>
      ${spark(L.series)}${people}
      <p class="cr-hint">${L.ownerCounted ? 'You are counted too (handy for testing).' : 'You are not counted. To test, open the app in a private window without signing in: you will appear as a visitor.'}
      <button class="linkbtn" id="cr-me">${L.ownerCounted ? 'Stop counting me' : 'Count me too'}</button></p></div>`;
  }

  function alertsHTML() {
    const ws = D.warnings, ic = { bad: '⛔', warn: '⚠️', info: 'ℹ️' };
    if (!ws.length) return '<p class="cr-clear">✅ All clear. Nothing needs your attention.</p>';
    return `<ul class="cr-warns">${ws.map((w) => `<li class="${w.level}"><b>${ic[w.level]} ${esc(w.title)}</b><p>${esc(w.detail)}</p></li>`).join('')}</ul>`;
  }

  function kpiHTML() {
    const m = D.money, s = D.sales;
    const profit = m.profitProjected, pl = profit < 0 ? 'bad' : 'ok';
    return `<div class="cr-kpis">
      <div class="cr-kpi"><span>Sales this month</span><b>${both(m.revenueMtd)}</b><small>${s.count} sale${s.count === 1 ? '' : 's'}${s.otherCurrencies.length ? ` (${esc(s.otherCurrencies.join(', '))} not counted)` : ''}</small></div>
      <div class="cr-kpi"><span>Costs this month so far</span><b>${both(m.costMtd)}</b><small>Heading for ${usd(m.costProjected)}</small></div>
      <div class="cr-kpi ${pl}"><span>Profit if this pace holds</span><b>${profit < 0 ? '−' : ''}${both(Math.abs(profit))}</b><small>Sales ${usd(m.revenueProjected)} minus costs ${usd(m.costProjected)}</small></div></div>`;
  }

  function metersHTML() {
    const o = D.openai, r = D.resend, sb = D.supabase, S_ = D.settings;
    return `<div class="cr-gauges">
      ${o.on ? gauge('OpenAI this month', o.mtd, o.budget, usd, `Today ${usd(o.today)}. On pace for ${usd(o.projected)}.`) : '<div class="cr-g"><div class="cr-gt"><span>OpenAI</span></div><div class="cr-gv">Off</div><small>OPENAI_API_KEY is not set.</small></div>'}
      ${r.on ? gauge('Emails today (last 24h)', r.day, r.dayLimit, num, r.dayLimit ? 'Sign-in codes stop when this fills.' : 'Your plan has no daily cap.') : ''}
      ${r.on ? gauge('Emails this month', r.month, r.monthLimit, num, r.kinds.map((k) => `${esc(k.name)} ${k.n}`).join(', ') || 'None sent yet.') : ''}
      ${gauge('Database size', sb.dbBytes, S_.supabase_db_mb * 1048576, mb, sb.imagesN ? `Lesson pictures use ${mb(sb.imagesBytes)} (${sb.imagesN} pictures).` : 'Includes everything Supabase keeps for this project.')}
      ${gauge('Server: busiest this week', D.peak7, S_.render_live_capacity, num, 'Most students online together in the last 7 days, against what your Render plan is rated for.')}
    </div>`;
  }

  function billHTML() {
    const m = D.money, o = D.openai, p = m.plans, f = D.sales.stripeFeesUsd;
    const row = (n, a, b, note) => `<tr><td>${n}${note ? `<small>${note}</small>` : ''}</td><td>${both(a)}</td><td>${both(b)}</td></tr>`;
    return `<div class="cr-table"><table><thead><tr><th>Service</th><th>So far</th><th>Whole month</th></tr></thead><tbody>
      ${row('OpenAI', o.mtd, o.projected, 'pays per use')}${row('Render', p.render, p.render, 'your plan')}${row('Supabase', p.supabase, p.supabase, 'your plan')}${row('Resend', p.resend, p.resend, 'your plan')}
      ${row('Stripe fees', f, m.feesProjected, '2.9% + 30 cents per sale, unless you changed it')}
      <tr class="tot"><td>Total</td><td>${both(m.costMtd)}</td><td>${both(m.costProjected)}</td></tr></tbody></table></div><p class="cr-hint">${PLAN_NOTE}</p>`;
  }

  function openaiHTML() {
    const o = D.openai, max = Math.max(...o.features.map((f) => f.usd), 0.0001);
    const feats = o.features.length ? `<ul class="cr-feat">${o.features.map((f) => `<li><span>${esc(f.name)}<small>${num(f.calls)} calls</small></span><div class="cr-bar"><i style="width:${(f.usd / max) * 100}%"></i></div><b>${usd(f.usd)}</b></li>`).join('')}</ul>` : '<p class="cr-none">No AI calls yet this month.</p>';
    const heavy = o.heavy.length ? `<h4>Biggest users this month</h4><ul class="cr-people">${o.heavy.map((h) => `<li><b>${esc(h.name)}</b><span>${num(h.calls)} calls</span><em>${usd(h.usd)}</em></li>`).join('')}</ul><p class="cr-hint">If one person is far above the rest, check they are not abusing the AI.</p>` : '';
    return `<h4>Where the OpenAI money goes</h4>${feats}<h4>Spend by day</h4>${bars(o.days, 'usd', usd, 'OpenAI spend by day this month')}${heavy}`;
  }

  function salesHTML() {
    const s = D.sales;
    const recent = s.recent.length ? `<ul class="cr-people">${s.recent.map((r) => `<li><b>${esc(r.name)}</b><span>${esc(r.course)} · ${esc(r.provider)}${r.status !== 'verified' ? ` · <u>${esc(r.status)}</u>` : ''}</span><em>${esc(r.text)}<small>${when(r.when)}</small></em></li>`).join('')}</ul>` : '<p class="cr-none">No sales yet.</p>';
    return `<div class="cr-sub"><span><b>${s.count}</b> sales</span><span><b>${s.refunds}</b> refunded</span><span><b>${s.disputes}</b> disputed</span><span>Stripe fees <b>${usd(s.stripeFeesUsd)}</b></span></div>
      <h4>Sales by day (last 30 days)</h4>${bars(s.days.map((d) => ({ day: d.day, usd: d.usd })), 'usd', usd, 'Sales by day')}<h4>Latest</h4>${recent}`;
  }

  function studentsHTML() {
    const t = D.students, top = Math.max(t.total, 1), since = t.countingSince ? `Daily activity has been counted since ${esc(t.countingSince)}.` : 'Daily activity counting starts with the first student who opens the app.';
    return `<div class="cr-sub"><span><b>${num(t.total)}</b> students</span><span>New: <b>${t.signups.today}</b> today, <b>${t.signups.week}</b> this week, <b>${t.signups.month}</b> in 30 days</span></div>
      <div class="cr-sub"><span>Active today <b>${t.dau}</b></span><span>this week <b>${t.wau}</b></span><span>this month <b>${t.mau}</b></span></div><p class="cr-hint">${since}</p>
      <h4>From sign-up to paying</h4><ul class="cr-feat">${t.funnel.map((f) => `<li><span>${esc(f.name)}</span><div class="cr-bar"><i style="width:${(f.n / top) * 100}%"></i></div><b>${num(f.n)}<small>${Math.round((f.n / top) * 100)}%</small></b></li>`).join('')}</ul>`;
  }

  function healthHTML() {
    const p = D.pay, st = { ok: '✅', warn: '⚠️', bad: '⛔' };
    return `<p class="cr-hint">Payments run on <b>${p.provider ? esc(p.provider) : 'nothing'}</b> at ${esc(p.price)}.${p.lastWebhook ? ` Stripe last called the webhook ${esc(when(p.lastWebhook))}.` : ''}</p>
      ${p.lastError ? (() => { const m = /^(\S+)\s+([\s\S]*)$/.exec(p.lastError) || [0, '', p.lastError]; return `<p class="cr-warn1">Last Stripe problem${m[1] ? ' (' + esc(when(m[1])) + ')' : ''}: ${esc(m[2])}</p>`; })() : ''}
      <ul class="cr-check">${D.setup.map((i) => `<li class="${i.state}"><b>${st[i.state]} ${esc(i.label)}</b>${i.hint ? `<p>${esc(i.hint)}</p>` : ''}</li>`).join('')}</ul>`;
  }

  function paintAll() {
    put('cr-alerts', alertsHTML()); put('cr-kpi', kpiHTML()); put('cr-meters', metersHTML()); put('cr-bill', billHTML()); put('cr-openai', openaiHTML());
    put('cr-sales', salesHTML()); put('cr-students', studentsHTML()); put('cr-health', healthHTML());
    paintLive(D.live); paintAudit();
    const t = q('#cr-time'); if (t) t.textContent = 'Updated ' + new Date().toLocaleTimeString('en-GB');
  }
  function paintLive(L) { D.live = L; put('cr-livebox', liveHTML(L)); const m = q('#cr-me'); if (m) m.onclick = toggleMe; const n = document.getElementById('ow-n'); if (n) n.textContent = L.now; }
  function paintAudit() { put('cr-audit', D.audit.length ? `<ul class="cr-people">${D.audit.map((a) => `<li><b>${esc(a.action)}</b><span>${esc(a.detail)}</span><em>${when(a.when)}</em></li>`).join('')}</ul>` : '<p class="cr-none">Nothing yet.</p>'); }

  /* ── what if ── */
  async function runWhatIf() {
    clearTimeout(tWi);
    tWi = setTimeout(async () => {
      const n = STEPS[wiN];
      try {
        const w = await api('/api/owner/whatif', { method: 'POST', body: { students: n, buyPct: wiBuy } });
        const flag = (x) => (x.tooSmall ? ' <span class="cr-chip bad">too big for the biggest plan listed</span>' : '');
        put('wi-out', `<div class="cr-kpis">
          <div class="cr-kpi"><span>Running costs a month</span><b>${both(w.totalUsd)}</b><small>${usd(w.perStudentUsd)} per student</small></div>
          <div class="cr-kpi"><span>Sales a month</span><b>${both(w.revenueUsd)}</b><small>${num(w.sales)} sales at ${usd(w.priceUsd)}</small></div>
          <div class="cr-kpi ${w.profitUsd < 0 ? 'bad' : 'ok'}"><span>Left over</span><b>${w.profitUsd < 0 ? '−' : ''}${both(Math.abs(w.profitUsd))}</b><small>Break-even at ${num(w.breakEvenSales)} sales a month</small></div></div>
          <ul class="cr-check"><li class="ok"><b>~${num(w.live)} students online at the same time</b></li>
          <li class="${w.render.tooSmall ? 'bad' : 'ok'}"><b>Render: ${esc(w.render.plan)} (${usd(w.render.usd)})</b>${flag(w.render)}</li>
          <li class="${w.supabase.tooSmall ? 'warn' : 'ok'}"><b>Supabase: ${esc(w.supabase.plan)} (${usd(w.supabase.usd)})</b> <small>${num(w.supabase.mb)} MB of data</small>${flag(w.supabase)}</li>
          <li class="ok"><b>Resend: ${esc(w.resend.plan)} (${usd(w.resend.usd)})</b> <small>${num(w.resend.emails)} emails</small>${flag(w.resend)}</li>
          <li class="ok"><b>OpenAI: ${usd(w.openai)}</b></li><li class="ok"><b>Stripe fees: ${usd(w.stripeFees)}</b></li></ul>`);
      } catch (x) { put('wi-out', `<p class="cr-warn1">${esc(x.message)}</p>`); }
    }, 180);
  }
  function whatIfHTML() {
    return `<p class="cr-hint">Slide to see what your monthly bill would be with more students. It starts from ${D.per.measured ? 'what your real students cost so far' : 'typical numbers (about 30 cents of AI and 3 emails a student) until you have 10 active students to measure'}.</p>
      <label class="cr-r">Active students a month: <b id="wi-nl">${num(STEPS[wiN])}</b><input id="wi-n" type="range" min="0" max="${STEPS.length - 1}" step="1" value="${wiN}"></label>
      <label class="cr-r">Share who buy a track each month: <b id="wi-bl">${wiBuy}%</b><input id="wi-b" type="range" min="0" max="50" step="1" value="${wiBuy}"></label>
      <div class="pills">${[100, 1000, 5000, 25000].map((n) => `<button class="pill" data-n="${STEPS.indexOf(n)}">${num(n)}</button>`).join('')}</div><div id="wi-out" aria-live="polite"></div>`;
  }

  /* ── plans and settings ── */
  function settingsHTML() {
    const s = D.settings, P = D.presets, opt = (list, cur, v) => `<option value="">Pick a plan…</option>${list.map((p, i) => `<option value="${i}">${esc(p.name)} (${usd(p.usd)}/month)</option>`).join('')}`;
    const f = (id, label, val, step = 'any', hint = '') => `<label class="cr-f">${label}<input id="${id}" type="number" inputmode="decimal" min="0" step="${step}" value="${val}">${hint ? `<small>${hint}</small>` : ''}</label>`;
    return `<p class="cr-hint">Tell the Control Room what you pay for. Pick a plan to fill the boxes, or type your own numbers.</p>
      <div class="cr-form"><h4>Render (server)</h4><select id="p-render">${opt(P.render)}</select>${f('s-render_usd', 'Cost a month ($)', s.render_usd)}${f('s-render_live_capacity', 'Students online at once it handles', s.render_live_capacity, '1')}
      <h4>Supabase (database)</h4><select id="p-supabase">${opt(P.supabase)}</select>${f('s-supabase_usd', 'Cost a month ($)', s.supabase_usd)}${f('s-supabase_db_mb', 'Database size included (MB)', s.supabase_db_mb, '1')}
      <h4>Resend (email)</h4><select id="p-resend">${opt(P.resend)}</select>${f('s-resend_usd', 'Cost a month ($)', s.resend_usd)}${f('s-resend_month_limit', 'Emails a month included', s.resend_month_limit, '1')}${f('s-resend_day_limit', 'Emails a day allowed (0 = no cap)', s.resend_day_limit, '1')}
      <h4>OpenAI and money</h4>${f('s-openai_budget_usd', 'Most you want to spend on OpenAI a month ($)', s.openai_budget_usd)}${f('s-usd_ngn', 'Naira for one US dollar', s.usd_ngn, '1', 'Used to show costs in naira and to price what-if sales.')}
      ${f('s-stripe_fee_pct', 'Stripe fee (%)', s.stripe_fee_pct)}${f('s-stripe_fee_fixed_usd', 'Stripe fixed fee per sale ($)', s.stripe_fee_fixed_usd)}
      <label class="cr-ck"><input id="s-alert_emails" type="checkbox" ${s.alert_emails ? 'checked' : ''}> Email me when something needs attention</label></div>
      <div class="pills"><button class="btn" id="cr-save">SAVE PLANS</button><button class="pill" id="cr-test">Send a test alert</button></div><p class="err" id="cr-serr" role="alert"></p>`;
  }
  function bindSettings() {
    const pick = (id, list, map) => { const e = q('#' + id); if (e) e.onchange = () => { const p = list[+e.value]; if (!p || e.value === '') return; Object.entries(map).forEach(([k, v]) => { const i = q('#s-' + k); if (i) i.value = p[v]; }); }; };
    pick('p-render', D.presets.render, { render_usd: 'usd', render_live_capacity: 'live' });
    pick('p-supabase', D.presets.supabase, { supabase_usd: 'usd', supabase_db_mb: 'mb' });
    pick('p-resend', D.presets.resend, { resend_usd: 'usd', resend_month_limit: 'month', resend_day_limit: 'day' });
    q('#cr-save').onclick = async () => {
      const body = {}; q('#cr-settings').querySelectorAll('input[id^="s-"]').forEach((i) => { body[i.id.slice(2)] = i.type === 'checkbox' ? (i.checked ? 1 : 0) : i.value; });
      try { const r = await api('/api/owner/settings', { method: 'POST', body: { settings: body } }); D.settings = r.settings; toast('Saved.'); q('#cr-serr').textContent = ''; await refresh(); runWhatIf(); }
      catch (x) { q('#cr-serr').textContent = x.message; }
    };
    q('#cr-test').onclick = async () => { try { const r = await api('/api/owner/test-alert', { method: 'POST', body: {} }); toast(r.sent ? 'Test alert sent. Check your inbox and spam folder.' : 'Email is not set up, so the test was printed in the server log.'); } catch (x) { toast(x.message, 'bad'); } };
  }
  async function toggleMe() {
    try { await api('/api/owner/settings', { method: 'POST', body: { settings: { count_owner: D.live.ownerCounted ? 0 : 1 } } }); await pollLive(); } catch (x) { toast(x.message, 'bad'); }
  }

  /* ── tools ── */
  function toolsHTML() {
    return `<h4>Give a student a track</h4><p class="cr-hint">For a giveaway, or a student who paid but did not get access. They must have signed up already.</p>
      <label class="cr-f">Student email<input id="g-email" type="email" autocomplete="off" placeholder="student@example.com"></label>
      <label class="cr-f">Track<select id="g-course">${D.courses.map((c) => `<option value="${esc(c.id)}">${esc(c.title)}</option>`).join('')}</select></label>
      <div class="pills"><button class="btn" id="g-go">GIVE ACCESS</button></div><p class="err" id="g-err" role="alert"></p>
      <h4>Recent changes</h4><div id="cr-audit"></div>`;
  }
  function bindTools() {
    q('#g-go').onclick = async () => {
      const b = q('#g-go'); b.disabled = true; q('#g-err').textContent = '';
      try { const r = await api('/api/owner/grant', { method: 'POST', body: { email: q('#g-email').value, courseId: q('#g-course').value } }); toast(r.already ? `${r.name} already had ${r.course}.` : `${r.name} now has ${r.course}.`); await refresh(); }
      catch (x) { q('#g-err').textContent = x.message; }
      b.disabled = false;
    };
  }

  /* ── loading and the shell ── */
  async function refresh() { try { D = await api('/api/owner/overview'); paintAll(); } catch (x) { toast(x.message, 'bad'); } }
  async function pollLive() { if (document.hidden || !root) return; try { paintLive(await api('/api/owner/live')); } catch (_) {} }

  function section(id, title, inner, note = '') {
    return `<section class="glass cr-card" id="cr-s-${id}"><h3>${title}</h3>${note ? `<p class="cr-note">${note}</p>` : ''}${inner}</section>`;
  }

  window.crOpen = async function crOpen() {
    if (root) return;
    root = document.createElement('div'); root.id = 'cr'; root.className = 'cr'; root.setAttribute('role', 'dialog'); root.setAttribute('aria-modal', 'true'); root.setAttribute('aria-label', 'Control Room');
    root.innerHTML = '<div class="cr-in"><p class="cr-none"><span class="spin"></span> Loading…</p></div>';
    document.body.append(root); document.body.classList.add('lock');
    try { D = await api('/api/owner/overview'); } catch (x) { toast(x.message, 'bad'); return crClose(); }
    root.innerHTML = `<div class="cr-in">
      <div class="cr-top"><div><h2>Control Room</h2><span class="cr-note">${esc(D.month.label)}, day ${D.month.day} of ${D.month.days}. Only you can see this page. <span id="cr-time"></span></span></div>
        <span class="spacer"></span><button class="ghost" id="cr-ref">Refresh</button><button class="ghost" id="cr-x" aria-label="Close Control Room">Close ✕</button></div>
      <nav class="cr-nav" aria-label="Jump to">${[['live', 'Live'], ['alerts', 'Alerts'], ['costs', 'Costs'], ['whatif', 'What if'], ['sales', 'Sales'], ['students', 'Students'], ['plans', 'Plans'], ['setup', 'Setup']].map(([k, l]) => `<a href="#cr-s-${k}" data-go="${k}">${l}</a>`).join('')}</nav>
      ${section('live', 'Live now', '<div id="cr-livebox"></div>')}
      ${section('alerts', 'Needs attention', '<div id="cr-alerts"></div>')}
      <div id="cr-kpi"></div>
      ${section('costs', 'The meter', '<div id="cr-meters"></div><h4>This month\'s bill</h4><div id="cr-bill"></div><div id="cr-openai"></div>', 'Each bar turns amber at 80% and red at 100%.')}
      ${section('whatif', 'What if I had more students?', whatIfHTML())}
      ${section('sales', 'Sales', '<div id="cr-sales"></div>')}
      ${section('students', 'Students', '<div id="cr-students"></div>')}
      ${section('plans', 'Plans and settings', '<div id="cr-settings">' + settingsHTML() + '</div>')}
      ${section('setup', 'Setup check and tools', '<div id="cr-health"></div>' + toolsHTML())}
    </div>`;
    paintAll(); bindSettings(); bindTools(); runWhatIf();
    q('#cr-x').onclick = () => crClose(); q('#cr-ref').onclick = refresh;
    root.querySelectorAll('.cr-nav a').forEach((a) => (a.onclick = (e) => { e.preventDefault(); const t = q('#cr-s-' + a.dataset.go); if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' }); }));
    q('#wi-n').oninput = (e) => { wiN = +e.target.value; q('#wi-nl').textContent = num(STEPS[wiN]); runWhatIf(); };
    q('#wi-b').oninput = (e) => { wiBuy = +e.target.value; q('#wi-bl').textContent = wiBuy + '%'; runWhatIf(); };
    root.querySelectorAll('[data-n]').forEach((b) => (b.onclick = () => { wiN = +b.dataset.n; q('#wi-n').value = wiN; q('#wi-nl').textContent = num(STEPS[wiN]); runWhatIf(); }));
    tLive = setInterval(pollLive, 8000); tAll = setInterval(() => { if (!document.hidden) refresh(); }, 60000);
    document.addEventListener('keydown', onKey);
    try { history.pushState({ cr: 1 }, ''); popped = false; } catch (_) {}
    addEventListener('popstate', onPop);
    root.scrollTop = 0;
  };

  function onKey(e) { if (e.key === 'Escape' && root && !document.getElementById('pwm')) crClose(); }
  function onPop() { if (root) { popped = true; crClose(); } }   // the phone's back button closes the page
  function crClose() {
    clearInterval(tLive); clearInterval(tAll); clearTimeout(tWi); document.removeEventListener('keydown', onKey); removeEventListener('popstate', onPop);
    if (root) { root.remove(); root = null; }
    document.body.classList.remove('lock');
    if (!popped && history.state && history.state.cr) history.back();   // our listener is already off, so this only removes the spare history entry
    popped = false;
  }
})();
