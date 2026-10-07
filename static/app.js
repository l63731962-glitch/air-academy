'use strict';
const $ = (s, r = document) => r.querySelector(s);
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const PRICE = 3500;
const money = (n) => '₦' + n.toLocaleString('en-NG');
const ICONS = { 'prompt-engineering': '🧠', animation: '🎬', 'cloud-computing': '☁️', 'web-development': '🌐',
  'app-development': '📱', 'full-stack': '🧩', 'agentic-ai': '🤖', 'game-development': '🎮' };
const LOCK = '<svg viewBox="0 0 24 24"><path d="M12 1a5 5 0 0 0-5 5v3H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-1V6a5 5 0 0 0-5-5zm-3 8V6a3 3 0 1 1 6 0v3H9z"/></svg>';
const CHECK = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-1.3 14.7-4-4 1.4-1.4 2.6 2.6 5.6-5.6 1.4 1.4-7 7z"/></svg>';

// Single source of truth. Every view renders from this, so the UI updates without a reload.
const S = { user: null, courses: [], openId: null, detail: null, paying: false, status: '' };
const isOwned = (id) => !!S.user && S.user.enrolledCourses.includes(id);

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

/* ───────────── Login (passwordless, 6-digit code) ───────────── */
let resendTimer;
function renderLogin(step = 'email', email = '', secs = 60) {
  clearInterval(resendTimer);
  closeSheet();
  const emailStep = step === 'email';
  $('#app').innerHTML = `
  <section class="login"><div class="login-box">
    <div class="logo">⬡</div><h1>AIR ACADEMY</h1><p class="sub">Learn tech skills. Build real projects.</p>
    <form class="glass panel" id="f" novalidate>
      ${emailStep ? `
        <h2>Sign in or create account</h2><p>Enter your email and we'll send a 6-digit code.</p>
        <label for="em">Email address</label>
        <input id="em" type="email" inputmode="email" autocomplete="email" placeholder="you@example.com" required>
        <p class="err" id="e"></p><button class="btn" id="go">SEND CODE</button>`
      : `
        <h2>Check your inbox</h2><p>We sent a code to <b>${esc(email)}</b>. It expires in 10 minutes.</p>
        <label for="cd">6-digit code</label>
        <input id="cd" class="code" inputmode="numeric" autocomplete="one-time-code" maxlength="6" placeholder="••••••">
        <p class="err" id="e"></p><button class="btn" id="go">VERIFY &amp; ENTER</button>
        <div style="display:flex;justify-content:space-between;margin-top:8px">
          <button type="button" class="linkbtn" id="rs" disabled>Resend in ${secs}s</button>
          <button type="button" class="linkbtn" id="ch">Change email</button>
        </div>`}
    </form>
    <p class="note">No passwords. Ever.</p>
  </div></section>`;

  const f = $('#f'), e = $('#e'), go = $('#go');
  const busy = (b, label) => { go.disabled = b; go.innerHTML = b ? '<span class="spin"></span>' : label; };

  if (emailStep) {
    $('#em').value = email; $('#em').focus();
    f.onsubmit = async (ev) => {
      ev.preventDefault(); e.textContent = '';
      const v = $('#em').value.trim().toLowerCase();
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)) { e.textContent = 'Enter a valid email address.'; return; }
      busy(true);
      try { await api('/api/auth/request-code', { method: 'POST', body: { email: v } }); renderLogin('code', v, 60); }
      catch (x) { e.textContent = x.message; busy(false, 'SEND CODE'); }
    };
  } else {
    const cd = $('#cd'); cd.focus();
    const submit = async () => {
      e.textContent = '';
      if (!/^\d{6}$/.test(cd.value)) { e.textContent = 'Enter the 6-digit code.'; return; }
      busy(true);
      try {
        const d = await api('/api/auth/verify-code', { method: 'POST', body: { email, code: cd.value } });
        S.user = d.user; await enter();
      } catch (x) { e.textContent = x.message; busy(false, 'VERIFY &amp; ENTER'); cd.select(); }
    };
    cd.oninput = () => { cd.value = cd.value.replace(/\D/g, '').slice(0, 6); if (cd.value.length === 6) submit(); };
    f.onsubmit = (ev) => { ev.preventDefault(); submit(); };
    $('#ch').onclick = () => renderLogin('email', email);
    const rs = $('#rs'); let left = secs;
    resendTimer = setInterval(() => {
      left -= 1;
      if (left <= 0) { clearInterval(resendTimer); rs.disabled = false; rs.textContent = 'Resend code'; }
      else rs.textContent = `Resend in ${left}s`;
    }, 1000);
    rs.onclick = async () => {
      rs.disabled = true;
      try { await api('/api/auth/request-code', { method: 'POST', body: { email } }); renderLogin('code', email, 60); toast('New code sent.'); }
      catch (x) { e.textContent = x.message; rs.disabled = false; }
    };
  }
}

/* ───────────── Dashboard ───────────── */
function cardHTML(c, i, animate) {
  const open = isOwned(c.id);
  const cover = c.coverImage ? `style="background-image:url('${esc(c.coverImage)}')"` : '';
  return `
  <button class="glass card ${open ? 'open' : ''} ${animate ? '' : 'still'}" style="--i:${i}" data-id="${esc(c.id)}"
          aria-label="${esc(c.title)}, ${open ? 'unlocked' : 'locked'}">
    <div class="cover" ${cover}>${c.coverImage ? '' : ICONS[c.id] || '📘'}</div>
    <div class="card-body">
      <h3>${esc(c.title)}</h3><div class="meta">${c.lessonsCount} lessons</div>
      <span class="chip">${open ? CHECK + 'Unlocked' : LOCK + 'Locked'}</span>
    </div>
  </button>`;
}

function renderDashboard(animate = true) {
  const n = S.courses.filter((c) => isOwned(c.id)).length, t = S.courses.length;
  $('#app').innerHTML = `
  <header class="glass head">
    <div class="head-top"><span class="badge"><i></i>SECURE SESSION</span><span class="spacer"></span>
      <button class="ghost" id="out">Sign out</button></div>
    <p class="welcome">Welcome back,</p><div class="email">${esc(S.user.email)}</div>
    <div class="meter"><i style="width:${t ? (n / t) * 100 : 0}%"></i></div>
    <div class="meta">${n} of ${t} tracks unlocked</div>
  </header>
  <section class="grid">${S.courses.map((c, i) => cardHTML(c, i, animate)).join('')}</section>`;
  $('#out').onclick = async () => { try { await api('/api/auth/logout', { method: 'POST' }); } catch (_) {} S.user = null; S.courses = []; renderLogin(); };
  $('#app').querySelectorAll('.card').forEach((b) => (b.onclick = () => openCourse(b.dataset.id)));
}

/* ───────────── Course sheet + paywall ───────────── */
function closeSheet() { const s = $('#sheet'); s.hidden = true; s.innerHTML = ''; document.body.classList.remove('lock'); S.openId = null; S.detail = null; }

async function openCourse(id) {
  S.openId = id; S.detail = null; S.status = '';
  $('#sheet').hidden = false; document.body.classList.add('lock');
  renderSheet();
  if (isOwned(id)) { await loadDetail(id); renderSheet(); }
}
async function loadDetail(id) {
  try { S.detail = await api('/api/courses/' + encodeURIComponent(id)); } catch (x) { toast(x.message, 'bad'); }
}

function renderSheet() {
  const c = S.courses.find((x) => x.id === S.openId); if (!c) return;
  const open = isOwned(c.id);
  const lessons = open
    ? (S.detail && S.detail.lessons) || []
    : Array.from({ length: c.lessonsCount }, (_, i) => ({ n: i + 1, title: 'Premium lesson content' }));
  const rows = lessons.map((l, i) => `
    <div class="glass lesson ${open ? '' : 'locked'}" style="--i:${i}">
      <span class="num">${l.n}</span><span>${esc(l.title)}</span><span>${open ? '▶' : '🔒'}</span>
    </div>`).join('') || '<p class="meta">Loading lessons…</p>';

  $('#sheet').innerHTML = `
  <div class="sheet-in">
    <button class="ghost back" id="bk">← All tracks</button>
    <div class="glass intro"><h2>${esc(c.title)}</h2><p>${esc(c.description)}</p></div>
    <div class="wrap">
      <div class="lessons">${rows}</div>
      ${open ? '' : `
      <div class="paywall" id="pw"><div class="glass pay-card">
        <div class="lockorb">${LOCK}</div>
        <h3>Premium course</h3><p>One-time payment. Lifetime access to all ${c.lessonsCount} lessons.</p>
        <button class="btn premium" id="buy">UNLOCK PREMIUM COURSE<small>Access for ${money(PRICE)}</small></button>
        <div class="status" id="st">${esc(S.status)}</div>
        <div class="secure">🔒 Secured by Flutterwave</div>
      </div></div>`}
    </div>
  </div>`;
  $('#bk').onclick = closeSheet;
  const buy = $('#buy'); if (buy) { buy.onclick = () => unlock(c); setPaying(S.paying); }
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
    customizations: { title: 'Air Academy', description: course.title },
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

// Lift the paywall, show real lessons, flip the dashboard card: no reload.
async function celebrate(course) {
  await loadDetail(course.id);
  const pw = $('#pw'); if (pw) pw.classList.add('lift');
  S.paying = false; S.status = '';
  await new Promise((r) => setTimeout(r, 650));
  renderSheet(); renderDashboard(false);
  toast('Payment verified. Course unlocked!');
}

/* ───────────── Boot ───────────── */
async function enter() {
  const d = await api('/api/courses'); S.courses = d.courses;
  renderDashboard();
}
(async function boot() {
  try { await syncMe(); if (!S.user) throw 0; await enter(); }
  catch (_) { S.user = null; renderLogin(); }
})();
