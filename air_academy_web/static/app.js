'use strict';
const $ = (s, r = document) => r.querySelector(s);
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const PRICE = 4000;   // only used until the server says what to show; the server decides the price and what is charged
const APP = 'Open Air Tech Space';
const money = (n) => '₦' + n.toLocaleString('en-NG');
const priceText = () => (S.pay && S.pay.text) || money(PRICE);   // '₦4,000', or whatever the server is charging in
const secureText = () => '🔒 Secured by Paystack';
const ICONS = { 'prompt-engineering': '🧠', animation: '🎬', 'cloud-computing': '☁️', 'web-development': '🌐',
  'app-development': '📱', 'full-stack': '🧩', 'agentic-ai': '🤖', 'game-development': '🎮',
  '2d-animation': '✏️', '3d-animation': '🧊', 'ai-animation': '✨' };
const LOCK = '<svg viewBox="0 0 24 24"><path d="M12 1a5 5 0 0 0-5 5v3H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-1V6a5 5 0 0 0-5-5zm-3 8V6a3 3 0 1 1 6 0v3H9z"/></svg>';
const CHECK = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-1.3 14.7-4-4 1.4-1.4 2.6 2.6 5.6-5.6 1.4 1.4-7 7z"/></svg>';

// Single source of truth. Every view renders from this, so the UI updates without a reload.
const S = { user: null, pay: null, courses: [], openId: null, detail: null, paying: false, status: '', q: '', filter: 'all', topic: 'all', demo: { available: false, on: false }, view: 'course', lesson: null, ca: null, exam: null, cert: null, group: null, pending: 0, canCreate: false, joinCode: null, invite: null };
const isOwned = (id) => !!S.user && S.user.enrolledCourses.includes(id);
const MARK = '<svg class="mk" viewBox="0 0 32 32" aria-hidden="true"><path class="hx" d="M16 2l12 7v14l-12 7L4 23V9z"/><path class="sn" d="M9.5 21a6.5 6.5 0 0 1 13 0M7 21h18M16 9.5v2.5M9.5 12.5l1.8 1.8M22.5 12.5l-1.8 1.8"/></svg>';
const HUES = { 'prompt-engineering': 275, animation: 330, 'cloud-computing': 200, 'web-development': 160,
  'app-development': 35, 'full-stack': 245, 'agentic-ai': 185, 'game-development': 350,
  '2d-animation': 305, '3d-animation': 215, 'ai-animation': 265 };
// Topic tabs on the dashboard. The older Animation Masterclass covers all three topics, so it shows under each one.
const TOPICS = [['all', 'All'], ['2d', '2D Animation'], ['3d', '3D Animation'], ['ai', 'AI Animation']];
const TOPIC_OF = { animation: ['2d', '3d', 'ai'], '2d-animation': ['2d'], '3d-animation': ['3d'], 'ai-animation': ['ai'] };
async function api(path, { method = 'GET', body } = {}) {
  const res = await fetch(path, {
    method, credentials: 'same-origin',
    headers: method === 'GET' ? {} : { 'Content-Type': 'application/json' },
    body: method === 'GET' ? undefined : JSON.stringify(body || {}),
  });
  let data = {};
  try { data = await res.json(); } catch (_) {}
  if (!res.ok) {
    const e = new Error(data.error || 'Something went wrong. Please try again.');
    e.status = res.status;
    throw e;
  }
  return data;
}

function toast(msg, kind = 'ok') {
  const t = document.createElement('div');
  t.className = 'toast ' + kind;
  t.textContent = msg;
  $('#toasts').append(t);
  setTimeout(() => t.remove(), 4200);
}

/* ───────────── Dashboard ───────────── */
// What a locked class says on its card. Outside a class group everything shows its price.
const accessLabel = (c) => ({ needs_request: 'Ask teacher', pending: 'Waiting', denied: 'Not allowed', later: 'Not yet' }[(c.access || {}).state] || priceText());
function classbarText() {
  if (!S.group) return '';
  const nx = S.group.steps.find((s) => !isOwned(s.id));
  return nx ? `Next class: ${esc(nx.title)}` : 'You have finished every class in your group.';
}

function cardHTML(c, i, animate) {
  const open = isOwned(c.id), done = open ? c.doneCount || 0 : 0;
  const cover = c.coverImage ? `style="background-image:url('${esc(c.coverImage)}')"` : `style="--h:${HUES[c.id] ?? 220}"`;
  return `
  <button class="glass card ${open ? 'open' : ''} ${animate ? '' : 'still'}" style="--i:${i}" data-id="${esc(c.id)}"
          aria-label="${esc(c.title)}, ${open ? 'unlocked' : c.free ? `locked, first ${c.free} lessons free` : 'locked'}">
    <div class="cover" ${cover}><span class="cno">Class ${c.classNo}</span>${c.isNew ? '<span class="cnew">NEW</span>' : ''}${!open && c.free ? '<span class="cfree">FREE PREVIEW</span>' : ''}${c.step ? `<span class="cstep">Step ${c.step}</span>` : ''}<span class="ico">${c.coverImage ? '' : ICONS[c.id] || '📘'}</span></div>
    <div class="card-body">
      <h3>${esc(c.title)}</h3>
      <p class="blurb">${esc(c.description)}</p>
      <div class="foot">
        <span class="meta">${open ? `${done} of ${c.lessonsCount} lessons done` : `${c.lessonsCount} lessons${c.free ? `, first ${c.free} free` : ''}`}</span>
        <span class="chip">${open ? CHECK + 'Unlocked' : LOCK + accessLabel(c)}</span>
      </div>
      ${open ? `<div class="mini"><i style="width:${c.lessonsCount ? (done / c.lessonsCount) * 100 : 0}%"></i></div>` : ''}
    </div>
  </button>`;
}

function visibleCourses() {
  const q = S.q.trim().toLowerCase();
  return S.courses.filter((c) => (S.filter === 'all' || (S.filter === 'mine') === isOwned(c.id))
    && (S.topic === 'all' || (TOPIC_OF[c.id] || []).includes(S.topic))
    && (!q || (c.title + ' ' + c.description).toLowerCase().includes(q)));
}

function renderGrid(animate = false) {
  const list = visibleCourses(), g = $('#grid');
  g.innerHTML = list.length ? list.map((c, i) => cardHTML(c, i, animate)).join('')
    : '<p class="empty">No tracks match. Clear the search or switch the filter or topic.</p>';
  g.querySelectorAll('.card').forEach((b) => (b.onclick = () => openCourse(b.dataset.id)));
}

function renderDashboard(animate = true) {
  const n = S.courses.filter((c) => isOwned(c.id)).length, t = S.courses.length;
  const tabs = [['all', 'All tracks'], ['mine', 'My tracks'], ['locked', 'Locked']];
  $('#app').innerHTML = `
  <header class="hero">
    <div class="hero-top"><span class="brandmark">${MARK}<b>${APP}</b></span><span class="spacer"></span>
      <span class="badge"><i></i>Secure session</span>${S.canCreate ? `<button class="ghost" id="cg">Class groups${S.pending ? ` <b class="dot">${S.pending}</b>` : ''}</button>` : ''}<button class="ghost talk" id="tk">🎙 Talk to Air Omega</button><button class="ghost" id="ps">Project Studio</button><button class="ghost" id="pu">Parent updates</button>${S.demo.available ? `<button class="ghost demo" id="dm" aria-pressed="${S.demo.on}">Demo Unlock Pro: ${S.demo.on ? 'ON' : 'OFF'}</button>` : ''}${S.user.isOwner ? `<button class="ghost owner" id="ow" title="Live users, costs and sales (only you can see this)"><i class="ld"></i><b id="ow-n">${window.LIVE_N == null ? '…' : window.LIVE_N}</b> live · Control Room</button>` : ''}<button class="ghost" id="out">Sign out</button></div>
    <div class="hero-body">
      <div>
        <p class="welcome">Welcome back, ${esc((S.user.fullName || S.user.email).split(' ')[0])}</p>
        <h1>Learn it.<br>Build it.<br>Ship it.</h1>
        <p class="lede">${S.group ? `Your group has ${S.group.steps.length} class${S.group.steps.length === 1 ? '' : 'es'}, unlocked one step at a time.` : `${S.courses.length || 11} hands-on tracks. Pay once per track and keep it for life.`}</p>
      </div>
      <div class="ring" style="--p:${t ? Math.round((n / t) * 100) : 0}" role="img" aria-label="${n} of ${t} tracks unlocked">
        <div><strong>${n}</strong><span>of ${t} unlocked</span></div>
      </div>
    </div>
  </header>
  ${S.group ? `<div class="classbar"><b>${esc(S.group.name)}</b><span>${classbarText()}</span><button class="pill hot" id="lb">Weekly leaderboard</button></div>` : ''}
  <div class="toolbar">
    <input id="q" type="search" placeholder="Search tracks" aria-label="Search tracks" value="${esc(S.q)}">
    <div class="seg">${tabs.map(([f, l]) => `<button data-f="${f}" aria-pressed="${S.filter === f}">${l}</button>`).join('')}</div>
  </div>
  <div class="topics" role="group" aria-label="Filter by topic"><span>Topic</span>${TOPICS.map(([t, l]) => `<button class="pill" data-t="${t}" aria-pressed="${S.topic === t}">${l}</button>`).join('')}</div>
  <section class="grid" id="grid"></section>`;
  renderGrid(animate);
  if (typeof airDock !== 'undefined') airDock.show();
  $('#q').oninput = (ev) => { S.q = ev.target.value; renderGrid(); };
  $('#app').querySelectorAll('.seg button').forEach((b) => (b.onclick = () => {
    S.filter = b.dataset.f;
    $('#app').querySelectorAll('.seg button').forEach((x) => x.setAttribute('aria-pressed', x === b));
    renderGrid();
  }));
  $('#app').querySelectorAll('.topics button').forEach((b) => (b.onclick = () => {
    S.topic = b.dataset.t;
    $('#app').querySelectorAll('.topics button').forEach((x) => x.setAttribute('aria-pressed', x === b));
    renderGrid();
  }));
  const dm = $('#dm'); if (dm) dm.onclick = () => toggleDemo();
  $('#ps').onclick = () => openStudio();
  $('#pu').onclick = () => openParents();
  $('#tk').onclick = () => openTalk();
  const lb = $('#lb'); if (lb) lb.onclick = () => openBoard();
  const cg = $('#cg'); if (cg) cg.onclick = () => openGroups();
  const ow = $('#ow'); if (ow) ow.onclick = () => openControlRoom();
  $('#out').onclick = async () => { try { await api('/api/auth/logout', { method: 'POST' }); } catch (_) {} S.user = null; S.courses = []; S.q = ''; S.filter = 'all'; S.topic = 'all'; S.demo = { available: false, on: false }; S.group = null; S.pending = 0; renderLogin(); if (window.livePing) livePing(); };
}

/* ───────────── Course sheet + paywall ───────────── */
function closeSheet() { if (typeof closePaywall === 'function') closePaywall(); if (window.speechSynthesis) speechSynthesis.cancel(); const s = $('#sheet'); s.hidden = true; s.innerHTML = ''; document.body.classList.remove('lock'); S.openId = null; S.detail = null; S.view = 'course'; S.lesson = null;
  if (S.user && $('#grid')) renderGrid();
}

async function openCourse(id) {
  S.openId = id; S.detail = null; S.status = ''; S.view = 'course';
  $('#sheet').hidden = false; document.body.classList.add('lock');
  renderSheet();
  if (isOwned(id)) { await loadDetail(id); renderSheet(); }
  else {
    await refreshCourses().catch(() => {});   // a teacher may have decided since the page loaded
    await loadDetail(id);   // before buying: the lesson titles, plus any free lessons in full (see FREE_LESSONS in app.py)
    renderSheet();
  }
}
async function loadDetail(id) {
  try { S.detail = await api('/api/courses/' + encodeURIComponent(id)); } catch (x) { toast(x.message, 'bad'); }
}

function setPaying(on, msg = '') {
  S.paying = on; S.status = msg;
  const b = $('#buy'), st = $('#st');
  if (st) st.textContent = msg;
  if (b) { b.disabled = on; if (on) b.innerHTML = '<span class="spin"></span>'; else b.innerHTML = `UNLOCK PREMIUM COURSE<small>Access for ${priceText()}</small>`; }
}

/* ───────────── Payment: Paystack checkout ───────────── */
function loadScript(src) {
  return new Promise((ok, no) => {
    if (document.querySelector(`script[src="${src}"]`)) return ok();
    const s = document.createElement('script'); s.src = src; s.onload = ok;
    s.onerror = () => no(new Error('Could not load this page. Check your connection and try again.'));
    document.head.append(s);
  });
}

async function unlock(course) {
  if (S.paying) return;
  setPaying(true, 'Opening secure checkout…');
  let init;
  try { init = await api('/api/payments/init', { method: 'POST', body: { courseId: course.id } }); }
  catch (x) { setPaying(false); toast(x.message, 'bad'); if (x.status === 409) await syncMe(); return; }
  // The student pays on Paystack's own page, then Paystack sends them back to this site with ?reference=... (see finishCheckout).
  if (!/^https:\/\//.test(init.url || '')) { setPaying(false); toast('Checkout could not be opened. Please try again.', 'bad'); return; }
  try { sessionStorage.setItem('oats_checkout', course.id); } catch (_) {}
  setPaying(true, 'Taking you to the secure payment page…');
  location.assign(init.url);
}

// The student is back from Paystack. Ask the server what really happened (it asks Paystack), then unlock or explain.
async function finishCheckout(ref) {
  let cid = null; try { cid = sessionStorage.getItem('oats_checkout'); sessionStorage.removeItem('oats_checkout'); } catch (_) {}
  toast('Confirming your payment…');
  for (let tries = 0; tries < 8; tries++) {   // a bank transfer can take a little while to clear, so keep checking for a short time
    try {
      const d = await api('/api/payments/verify', { method: 'POST', body: { txRef: ref } });
      if (d.pending) { await new Promise((r) => setTimeout(r, 4000)); continue; }   // the server answers 202 while the bank is still confirming
      S.user = d.user; cid = d.courseId || cid;
      await refreshCourses().catch(() => {});
      const c = S.courses.find((x) => x.id === cid);
      if (c) { renderDashboard(false); openCourse(c.id).then(() => celebrate(c)); }
      return;
    } catch (x) {
      toast(x.status === 402 ? 'That payment was not completed, so nothing was charged. If your bank did take the money, your track unlocks by itself once Paystack confirms it.' : x.message, 'bad');
      return;
    }
  }
  toast('Your payment is still being confirmed by the bank. Your track unlocks by itself as soon as it clears.');
}

async function openControlRoom() {   // the owner's page loads only when asked for, so students never download it
  try { await loadScript('/static/owner.js'); crOpen(); } catch (x) { toast(x.message, 'bad'); }
}

async function syncMe() {
  try { S.user = (await api('/api/me')).user; return true; } catch (_) { return false; }
}

function burst() {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const box = document.createElement('div'); box.className = 'confetti';
  for (let i = 0; i < 44; i++) {
    const p = document.createElement('i');
    p.style.cssText = `--x:${(Math.random() - .5) * 90}vw;--y:${35 + Math.random() * 50}vh;--r:${Math.random() * 720}deg;--d:${900 + Math.random() * 900}ms;left:${40 + Math.random() * 20}%;background:hsl(${Math.random() < .5 ? 185 : 275} 95% ${55 + Math.random() * 20}%)`;
    box.append(p);
  }
  document.body.append(box); setTimeout(() => box.remove(), 2000);
}

// Lift the paywall, show real lessons, flip the dashboard card: no reload.
async function celebrate(course) {
  S.view = 'course'; S.lesson = null;   // a purchase made from a free-lesson page lands on the unlocked course
  await loadDetail(course.id);
  const pw = $('#pw'); if (pw) pw.classList.add('lift');
  S.paying = false; S.status = '';
  await new Promise((r) => setTimeout(r, 650));
  await refreshCourses().catch(() => {}); renderSheet(); renderDashboard(false);
  burst();
  toast('Payment verified. Course unlocked!');
}

/* ───────────── Boot ───────────── */
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && S.openId && !$('#pwm')) closeSheet(); });   // the paywall pop-up closes itself first

window.addEventListener('pageshow', (e) => { if (e.persisted && S.paying) setPaying(false); });   // back from Paystack's page without paying

async function enter() {
  if (S.joinCode) {          // arrived through a class invite link: join the group, then show the dashboard
    try { const r = await post('/api/groups/join/' + encodeURIComponent(S.joinCode), {}); toast(`You joined ${r.group.name}.`); }
    catch (x) { toast(x.message, 'bad'); }
    S.joinCode = null; S.invite = null; history.replaceState(null, '', '/');
  }
  await refreshCourses();
  renderDashboard();
  if (window.livePing) livePing();
  const back = new URLSearchParams(location.search), ref = back.get('reference') || back.get('trxref');
  if (ref) {   // Paystack sent the student back here after the payment page
    history.replaceState(null, '', '/');
    if (/^OATS-[0-9a-f]{32}$/.test(ref)) finishCheckout(ref);
  }
}
window.addEventListener('load', async function boot() {
  const m = location.pathname.match(/^\/(join|admin)\/([\w-]+)\/?$/);
  if (m && m[1] === 'admin') return renderAdmin(m[2]);       // the teacher's private page needs no sign-in
  if (m) {
    S.joinCode = m[2];
    try { S.invite = (await api('/api/groups/join/' + encodeURIComponent(m[2]))).group; }
    catch (x) { S.joinCode = null; history.replaceState(null, '', '/'); toast(x.message, 'bad'); }
  }
  try { await syncMe(); if (!S.user) throw 0; await enter(); }
  catch (_) { S.user = null; renderLogin(); }
});