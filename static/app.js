'use strict';
const $ = (s, r = document) => r.querySelector(s);
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const PRICE = 3500;
const APP = 'Open Air Tech Space';
const money = (n) => '₦' + n.toLocaleString('en-NG');
const ICONS = { 'prompt-engineering': '🧠', animation: '🎬', 'cloud-computing': '☁️', 'web-development': '🌐',
  'app-development': '📱', 'full-stack': '🧩', 'agentic-ai': '🤖', 'game-development': '🎮' };
const LOCK = '<svg viewBox="0 0 24 24"><path d="M12 1a5 5 0 0 0-5 5v3H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-1V6a5 5 0 0 0-5-5zm-3 8V6a3 3 0 1 1 6 0v3H9z"/></svg>';
const CHECK = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-1.3 14.7-4-4 1.4-1.4 2.6 2.6 5.6-5.6 1.4 1.4-7 7z"/></svg>';

// Single source of truth. Every view renders from this, so the UI updates without a reload.
const S = { user: null, courses: [], openId: null, detail: null, paying: false, status: '', q: '', filter: 'all', view: 'course', lesson: null, ca: null, exam: null, cert: null, group: null, pending: 0, canCreate: false, joinCode: null, invite: null };
const isOwned = (id) => !!S.user && S.user.enrolledCourses.includes(id);
const MARK = '<svg class="mk" viewBox="0 0 32 32" aria-hidden="true"><path class="hx" d="M16 2l12 7v14l-12 7L4 23V9z"/><path class="sn" d="M9.5 21a6.5 6.5 0 0 1 13 0M7 21h18M16 9.5v2.5M9.5 12.5l1.8 1.8M22.5 12.5l-1.8 1.8"/></svg>';
const HUES = { 'prompt-engineering': 275, animation: 330, 'cloud-computing': 200, 'web-development': 160,
  'app-development': 35, 'full-stack': 245, 'agentic-ai': 185, 'game-development': 350 };
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
const accessLabel = (c) => ({ needs_request: 'Ask teacher', pending: 'Waiting', denied: 'Not allowed', later: 'Not yet' }[(c.access || {}).state] || money(PRICE));
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
          aria-label="${esc(c.title)}, ${open ? 'unlocked' : 'locked'}">
    <div class="cover" ${cover}><span class="cno">Class ${c.classNo}</span>${c.step ? `<span class="cstep">Step ${c.step}</span>` : ''}<span class="ico">${c.coverImage ? '' : ICONS[c.id] || '📘'}</span></div>
    <div class="card-body">
      <h3>${esc(c.title)}</h3>
      <p class="blurb">${esc(c.description)}</p>
      <div class="foot">
        <span class="meta">${open ? `${done} of ${c.lessonsCount} lessons done` : `${c.lessonsCount} lessons`}</span>
        <span class="chip">${open ? CHECK + 'Unlocked' : LOCK + accessLabel(c)}</span>
      </div>
      ${open ? `<div class="mini"><i style="width:${c.lessonsCount ? (done / c.lessonsCount) * 100 : 0}%"></i></div>` : ''}
    </div>
  </button>`;
}

function visibleCourses() {
  const q = S.q.trim().toLowerCase();
  return S.courses.filter((c) => (S.filter === 'all' || (S.filter === 'mine') === isOwned(c.id))
    && (!q || (c.title + ' ' + c.description).toLowerCase().includes(q)));
}

function renderGrid(animate = false) {
  const list = visibleCourses(), g = $('#grid');
  g.innerHTML = list.length ? list.map((c, i) => cardHTML(c, i, animate)).join('')
    : '<p class="empty">No tracks match. Clear the search or switch the filter.</p>';
  g.querySelectorAll('.card').forEach((b) => (b.onclick = () => openCourse(b.dataset.id)));
}

function renderDashboard(animate = true) {
  const n = S.courses.filter((c) => isOwned(c.id)).length, t = S.courses.length;
  const tabs = [['all', 'All tracks'], ['mine', 'My tracks'], ['locked', 'Locked']];
  $('#app').innerHTML = `
  <header class="hero">
    <div class="hero-top"><span class="brandmark">${MARK}<b>${APP}</b></span><span class="spacer"></span>
      <span class="badge"><i></i>Secure session</span>${S.canCreate ? `<button class="ghost" id="cg">Class groups${S.pending ? ` <b class="dot">${S.pending}</b>` : ''}</button>` : ''}<button class="ghost" id="ps">Project Studio</button><button class="ghost" id="out">Sign out</button></div>
    <div class="hero-body">
      <div>
        <p class="welcome">Welcome back, ${esc((S.user.fullName || S.user.email).split(' ')[0])}</p>
        <h1>Learn it.<br>Build it.<br>Ship it.</h1>
        <p class="lede">${S.group ? `Your group has ${S.group.steps.length} class${S.group.steps.length === 1 ? '' : 'es'}, unlocked one step at a time.` : 'Eight hands-on tracks. Pay once per track and keep it for life.'}</p>
      </div>
      <div class="ring" style="--p:${t ? Math.round((n / t) * 100) : 0}" role="img" aria-label="${n} of ${t} tracks unlocked">
        <div><strong>${n}</strong><span>of ${t} unlocked</span></div>
      </div>
    </div>
  </header>
  ${S.group ? `<div class="classbar"><b>${esc(S.group.name)}</b><span>${classbarText()}</span></div>` : ''}
  <div class="toolbar">
    <input id="q" type="search" placeholder="Search tracks" aria-label="Search tracks" value="${esc(S.q)}">
    <div class="seg">${tabs.map(([f, l]) => `<button data-f="${f}" aria-pressed="${S.filter === f}">${l}</button>`).join('')}</div>
  </div>
  <section class="grid" id="grid"></section>`;
  renderGrid(animate);
  $('#q').oninput = (ev) => { S.q = ev.target.value; renderGrid(); };
  $('#app').querySelectorAll('.seg button').forEach((b) => (b.onclick = () => {
    S.filter = b.dataset.f;
    $('#app').querySelectorAll('.seg button').forEach((x) => x.setAttribute('aria-pressed', x === b));
    renderGrid();
  }));
  $('#ps').onclick = () => openStudio();
  const cg = $('#cg'); if (cg) cg.onclick = () => openGroups();
  $('#out').onclick = async () => { try { await api('/api/auth/logout', { method: 'POST' }); } catch (_) {} S.user = null; S.courses = []; S.q = ''; S.filter = 'all'; S.group = null; S.pending = 0; renderLogin(); };
}

/* ───────────── Course sheet + paywall ───────────── */
function closeSheet() { const s = $('#sheet'); s.hidden = true; s.innerHTML = ''; document.body.classList.remove('lock'); S.openId = null; S.detail = null; S.view = 'course'; S.lesson = null;
  if (S.user && $('#grid')) renderGrid();
}

async function openCourse(id) {
  S.openId = id; S.detail = null; S.status = ''; S.view = 'course';
  $('#sheet').hidden = false; document.body.classList.add('lock');
  renderSheet();
  if (isOwned(id)) { await loadDetail(id); renderSheet(); }
  else { await refreshCourses().catch(() => {}); renderSheet(); }   // a teacher may have decided since the page loaded
}
async function loadDetail(id) {
  try { S.detail = await api('/api/courses/' + encodeURIComponent(id)); } catch (x) { toast(x.message, 'bad'); }
}

function setPaying(on, msg = '') {
  S.paying = on; S.status = msg;
  const b = $('#buy'), st = $('#st');
  if (st) st.textContent = msg;
  if (b) { b.disabled = on; if (on) b.innerHTML = '<span class="spin"></span>'; else b.innerHTML = `UNLOCK PREMIUM COURSE<small>Access for ${money(PRICE)}</small>`; }
}

/* ───────────── Flutterwave payment ───────────── */
async function unlock(course) {
  if (S.paying) return;
  setPaying(true, 'Opening secure checkout…');
  let init;
  try { init = await api('/api/payments/init', { method: 'POST', body: { courseId: course.id } }); }
  catch (x) { setPaying(false); toast(x.message, 'bad'); if (x.status === 409) await syncMe(); return; }

  let settled = false;
  const modal = FlutterwaveCheckout({
    public_key: init.publicKey,
    tx_ref: init.txRef,
    amount: init.amount,          // 3500, set by the server
    currency: init.currency,      // NGN
    payment_options: 'card, banktransfer, ussd',
    customer: { email: init.email, name: init.email.split('@')[0] },
    customizations: { title: APP, description: course.title },
    callback: async (r) => {
      if (settled) return; settled = true;
      if (modal && modal.close) modal.close();
      if (r.status !== 'successful' && r.status !== 'completed') { setPaying(false); toast('Payment was not completed.', 'bad'); return; }
      setPaying(true, 'Verifying your payment…');
      try {
        const d = await api('/api/payments/verify', { method: 'POST', body: { txRef: init.txRef, transactionId: r.transaction_id } });
        S.user = d.user;
        await celebrate(course);
      } catch (x) { setPaying(false); toast(x.message, 'bad'); }
    },
    onclose: async () => {
      if (settled) return;
      // User closed the sheet. A webhook may still have completed the payment, so re-check once.
      setPaying(false);
      if (await syncMe() && isOwned(course.id)) await celebrate(course);
    },
  });
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
  await loadDetail(course.id);
  const pw = $('#pw'); if (pw) pw.classList.add('lift');
  S.paying = false; S.status = '';
  await new Promise((r) => setTimeout(r, 650));
  await refreshCourses().catch(() => {}); renderSheet(); renderDashboard(false);
  burst();
  toast('Payment verified. Course unlocked!');
}

/* ───────────── Boot ───────────── */
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && S.openId) closeSheet(); });

async function enter() {
  if (S.joinCode) {          // arrived through a class invite link: join the group, then show the dashboard
    try { const r = await post('/api/groups/join/' + encodeURIComponent(S.joinCode), {}); toast(`You joined ${r.group.name}.`); }
    catch (x) { toast(x.message, 'bad'); }
    S.joinCode = null; S.invite = null; history.replaceState(null, '', '/');
  }
  await refreshCourses();
  renderDashboard();
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
