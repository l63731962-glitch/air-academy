'use strict';
/* Open Air Tech Space: sign-in, lesson reader, quizzes, CA record, exams, certificates, project studio.
   Loaded after app.js and shares its globals (S, api, $, esc, toast, money, MARK, enter, isOwned, ...). */

const THEMES = ['School', 'Church', 'Farm', 'Clinic', 'Fintech startup', 'Online market', 'Logistics company', 'Football club'];
S.studio = { cid: null, theme: 'School', level: 'beginner', brief: null };
const post = (url, body) => api(url, { method: 'POST', body });
const EMAIL_RX = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

/* ───────────── Text helpers ───────────── */
const fmt = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
function rich(t) {
  return t.split(/\n{2,}/).map((blk) => {
    const L = blk.split('\n');
    if (L.every((l) => l.startsWith('> '))) return `<div class="pbox"><small>Example prompt</small>${L.map((l) => fmt(l.slice(2))).join('<br>')}</div>`;
    if (L.every((l) => l.startsWith('- '))) return `<ul>${L.map((l) => `<li>${fmt(l.slice(2))}</li>`).join('')}</ul>`;
    if (L.every((l) => /^\d+\. /.test(l))) return `<ol>${L.map((l) => `<li>${fmt(l.replace(/^\d+\. /, ''))}</li>`).join('')}</ol>`;
    return `<p>${L.map(fmt).join('<br>')}</p>`;
  }).join('');
}

/* ───────────── Sign in / create account ───────────── */
let resendTimer;
function renderLogin(mode = 'signin', d = {}) {
  clearInterval(resendTimer); closeSheet();
  const today = new Date().toISOString().slice(0, 10);
  const inp = (id, label, type = 'text', ac = '', more = '') => `<label for="${id}">${label}</label><input id="${id}" type="${type}" autocomplete="${ac}" ${more}>`;
  const pass = (id, label, ac) => `<label for="${id}">${label}</label><div class="pw"><input id="${id}" type="password" autocomplete="${ac}"><button type="button" class="eye" data-for="${id}">Show</button></div>`;
  const tabs = `<div class="tabs"><button type="button" data-m="signin" aria-pressed="${mode === 'signin'}">Sign in</button><button type="button" data-m="signup" aria-pressed="${mode === 'signup'}">Create account</button></div>`;
  const code = '<label for="cd">6-digit code</label><input id="cd" class="code" inputmode="numeric" autocomplete="one-time-code" maxlength="6" placeholder="••••••">';
  const err = '<p class="err" id="e"></p>';
  const labels = { signin: 'SIGN IN', signup: 'CREATE ACCOUNT', code: 'VERIFY &amp; ENTER', forgot: 'SEND CODE', reset: 'SAVE &amp; SIGN IN' };
  const forms = {
    signin: `${tabs}<h2>Welcome back</h2><p>Sign in to continue learning.</p>${inp('em', 'Email address', 'email', 'email', 'inputmode="email"')}${pass('pw', 'Password', 'current-password')}${err}
      <button class="btn" id="go">${labels.signin}</button><div class="row"><button type="button" class="linkbtn" id="fg">Forgot password?</button></div>`,
    signup: `${tabs}<h2>Create your account</h2><p>Your name appears on your certificate, so use your real full name.</p>
      ${inp('fn', 'Full name', 'text', 'name', 'placeholder="Ada Okafor"')}
      <div class="two"><div>${inp('dob', 'Date of birth', 'date', 'bday', `max="${today}"`)}</div>
      <div><label for="gn">Gender</label><select id="gn"><option value="">Choose</option><option value="female">Female</option><option value="male">Male</option><option value="other">Prefer not to say</option></select></div></div>
      ${inp('em', 'Email address', 'email', 'email', 'inputmode="email"')}${pass('pw', 'Create password', 'new-password')}<p class="hint">At least 8 characters, with letters and a number.</p>${err}
      <button class="btn" id="go">${labels.signup}</button>`,
    code: `<h2>Check your inbox</h2><p>We sent a code to <b>${esc(d.email)}</b>. It expires in 10 minutes.</p>${code}${err}
      <button class="btn" id="go">${labels.code}</button><div class="row"><button type="button" class="linkbtn" id="rs" disabled>Resend in 60s</button><button type="button" class="linkbtn" id="back">Change details</button></div>`,
    forgot: `<h2>Reset your password</h2><p>Enter your email and we will send a 6-digit code.</p>${inp('em', 'Email address', 'email', 'email', 'inputmode="email"')}${err}
      <button class="btn" id="go">${labels.forgot}</button><div class="row"><button type="button" class="linkbtn" id="back">Back to sign in</button></div>`,
    reset: `<h2>Choose a new password</h2><p>Enter the code sent to <b>${esc(d.email)}</b> and your new password.</p>${code}${pass('pw', 'New password', 'new-password')}<p class="hint">At least 8 characters, with letters and a number.</p>${err}
      <button class="btn" id="go">${labels.reset}</button>`,
  };
  $('#app').innerHTML = `
  <section class="login"><div class="login-box">
    <div class="logo">${MARK}</div><h1>Open Air<br>Tech Space</h1><p class="sub">Learn tech skills. Build real projects.</p>
    ${S.invite ? `<div class="invite"><b>You are invited to join ${esc(S.invite.name)}</b><span>Create an account or sign in and you will join automatically. Classes in this group: ${S.invite.steps.map((s) => esc(s.title)).join(', ')}.</span></div>` : ''}
    <form class="glass panel" id="f" novalidate>${forms[mode]}</form>
    <ul class="perks"><li>8 tracks</li><li>${money(PRICE)} once per track</li><li>Lifetime access</li></ul>
  </div></section>`;

  const e = $('#e'), go = $('#go'), v = (id) => $('#' + id).value, email = () => v('em').trim().toLowerCase();
  const busy = (b) => { go.disabled = b; go.innerHTML = b ? '<span class="spin"></span>' : labels[mode]; };
  const strong = (p) => p.length >= 8 && /[A-Za-z]/.test(p) && /\d/.test(p);
  const steps = {
    signin: async () => { S.user = (await post('/api/auth/login', { email: email(), password: v('pw') })).user; await enter(); },
    signup: async () => {
      const name = v('fn').trim().replace(/\s+/g, ' ');
      if (!/\S+\s+\S+/.test(name)) throw new Error('Enter your full name (first and last name).');
      if (!v('dob')) throw new Error('Enter your date of birth.');
      if (!v('gn')) throw new Error('Choose a gender option.');
      if (!EMAIL_RX.test(email())) throw new Error('Enter a valid email address.');
      if (!strong(v('pw'))) throw new Error('Use at least 8 characters, with letters and a number.');
      await post('/api/auth/register', { fullName: name, dob: v('dob'), gender: v('gn'), email: email(), password: v('pw') });
      renderLogin('code', { email: email() });
    },
    code: async () => {
      if (!/^\d{6}$/.test(v('cd'))) throw new Error('Enter the 6-digit code.');
      S.user = (await post('/api/auth/verify-code', { email: d.email, code: v('cd') })).user; await enter();
    },
    forgot: async () => {
      if (!EMAIL_RX.test(email())) throw new Error('Enter a valid email address.');
      await post('/api/auth/request-code', { email: email() }); renderLogin('reset', { email: email() });
    },
    reset: async () => {
      if (!/^\d{6}$/.test(v('cd'))) throw new Error('Enter the 6-digit code.');
      if (!strong(v('pw'))) throw new Error('Use at least 8 characters, with letters and a number.');
      S.user = (await post('/api/auth/reset', { email: d.email, code: v('cd'), password: v('pw') })).user; await enter();
    },
  };
  $('#f').onsubmit = async (ev) => { ev.preventDefault(); e.textContent = ''; busy(true); try { await steps[mode](); } catch (x) { e.textContent = x.message; busy(false); } };
  document.querySelectorAll('.tabs button').forEach((b) => (b.onclick = () => renderLogin(b.dataset.m)));
  document.querySelectorAll('.eye').forEach((b) => (b.onclick = () => {
    const i = $('#' + b.dataset.for), show = i.type === 'password'; i.type = show ? 'text' : 'password'; b.textContent = show ? 'Hide' : 'Show';
  }));
  const fg = $('#fg'); if (fg) fg.onclick = () => renderLogin('forgot');
  const back = $('#back'); if (back) back.onclick = () => renderLogin(mode === 'code' ? 'signup' : 'signin');
  const cd = $('#cd');
  if (cd) cd.oninput = () => { cd.value = cd.value.replace(/\D/g, '').slice(0, 6); if (mode === 'code' && cd.value.length === 6) $('#f').requestSubmit(); };
  if (mode === 'code') {
    const rs = $('#rs'); let left = 60;
    resendTimer = setInterval(() => { left -= 1; if (left <= 0) { clearInterval(resendTimer); rs.disabled = false; rs.textContent = 'Resend code'; } else rs.textContent = `Resend in ${left}s`; }, 1000);
    rs.onclick = async () => {
      rs.disabled = true;
      try { await post('/api/auth/request-code', { email: d.email }); renderLogin('code', d); toast('New code sent.'); } catch (x) { e.textContent = x.message; rs.disabled = false; }
    };
  }
  (($('#fn') || $('#em') || $('#cd')) || {}).focus?.();
}

/* ───────────── Course sheet: router + shared bits ───────────── */
const sheet = (html, onBack, backLabel) => {
  $('#sheet').innerHTML = `<div class="sheet-in"><button class="ghost back" id="bk">${backLabel}</button>${html}</div>`;
  $('#bk').onclick = onBack;
};
const goView = (view) => { S.view = view; renderSheet(); $('#sheet').scrollTop = 0; };
const cap = (s) => s[0].toUpperCase() + s.slice(1);

function renderSheet() {
  if (S.view === 'projects') return viewStudio();
  if (S.view === 'groups') return viewGroups();
  const c = S.courses.find((x) => x.id === S.openId); if (!c) return;
  ({ course: viewCourse, lesson: viewLesson, ca: viewCA, exam: viewExam, cert: viewCert }[S.view] || viewCourse)(c);
}

async function markDone(c, n) {
  const on = !S.detail.done.includes(n);
  try { const r = await post('/api/progress', { courseId: c.id, n, done: on }); S.detail.done = r.done; c.doneCount = r.done.length; return true; }
  catch (x) { toast(x.message, 'bad'); return false; }
}

function viewCourse(c) {
  const open = isOwned(c.id), ready = open && S.detail;
  const L = open ? (S.detail && S.detail.lessons) || [] : Array.from({ length: c.lessonsCount }, (_, i) => ({ n: i + 1, title: 'Premium lesson content' }));
  const done = ready ? S.detail.done : [], total = L.length, dn = done.filter((n) => n <= total).length;
  const noteKey = (n) => `oats:note:${S.user.uid}:${c.id}:${n}`;
  const rows = L.map((l, i) => open && l.deep ? `
    <button class="glass lesson deep ${done.includes(l.n) ? 'done' : ''}" style="--i:${i}" data-n="${l.n}">
      <span class="num">${l.n}</span><span class="t">${esc(l.title)}</span><span class="tag">Full lesson</span><span class="tick">${done.includes(l.n) ? '✓' : '○'}</span><span class="chev">▶</span>
    </button>` : open ? `
    <details class="glass les ${done.includes(l.n) ? 'done' : ''}" style="--i:${i}"${i === 0 ? ' open' : ''}>
      <summary><span class="num">${l.n}</span><span class="t">${esc(l.title)}</span><span class="tick">${done.includes(l.n) ? '✓' : '○'}</span><span class="chev">▶</span></summary>
      <div class="body">
        ${l.goal ? `<h4>Learning goal</h4><p>${esc(l.goal)}</p>` : ''}
        ${l.points && l.points.length ? `<h4>Points to teach</h4><ul>${l.points.map((p) => `<li>${esc(p)}</li>`).join('')}</ul>` : ''}
        ${l.activity ? `<div class="act"><h4>Class activity</h4><p>${esc(l.activity)}</p></div>` : ''}
        <label for="nt${l.n}">Your own notes for lesson ${l.n} (saved on this device)</label>
        <textarea id="nt${l.n}" data-n="${l.n}" placeholder="Objectives, examples, exercises, timing">${esc((() => { try { return localStorage.getItem(noteKey(l.n)) || ''; } catch (_) { return ''; } })())}</textarea>
        <button class="pill markdone" data-n="${l.n}" aria-pressed="${done.includes(l.n)}">${done.includes(l.n) ? 'Marked as done' : 'Mark lesson as done'}</button>
      </div>
    </details>` : `
    <div class="glass lesson locked" style="--i:${i}"><span class="num">${l.n}</span><span>${esc(l.title)}</span><span>🔒</span></div>`).join('') || '<p class="meta">Loading lessons…</p>';

  sheet(`
    <div class="glass intro"><h2>${esc(c.title)}</h2><p>${esc(c.description)}</p>
      ${ready && total ? `<div class="prog" id="prog"><i style="width:${(dn / total) * 100}%"></i></div><p class="meta" id="pt">${dn} of ${total} lessons done.</p>
      <div class="pills"><button class="pill hot" id="ca">My CA and certificate</button><button class="pill" id="stu">Project Studio</button>${L.some((l) => !l.deep) ? '<button class="pill" id="ex">Expand all lessons</button>' : ''}<button class="pill" id="cp">Copy outline</button><button class="pill" id="pr">Print or save as PDF</button></div>` : ''}</div>
    <div class="wrap${open ? '' : ' locked'}">
      <div class="lessons">${rows}</div>
      ${open ? '' : payCard(c)}
    </div>`, closeSheet, '← All tracks');

  const sh = $('#sheet'), buy = $('#buy'); if (buy) { buy.onclick = () => unlock(c); setPaying(S.paying); }
  const rq = $('#req'); if (rq) rq.onclick = () => requestAccess(c);
  const ck = $('#chk2'); if (ck) ck.onclick = async () => { await refreshCourses().catch(() => {}); renderSheet(); };
  if (!ready) return;
  sh.querySelectorAll('.deep').forEach((b) => (b.onclick = () => openLesson(+b.dataset.n)));
  sh.querySelectorAll('.markdone').forEach((b) => (b.onclick = async () => {
    const n = +b.dataset.n; if (!(await markDone(c, n))) return;
    const on = S.detail.done.includes(n), k = S.detail.done.filter((x) => x <= total).length, d = b.closest('.les');
    d.classList.toggle('done', on); d.querySelector('.tick').textContent = on ? '✓' : '○';
    b.setAttribute('aria-pressed', on); b.textContent = on ? 'Marked as done' : 'Mark lesson as done';
    $('#prog').firstElementChild.style.width = (k / total) * 100 + '%'; $('#pt').textContent = `${k} of ${total} lessons done.`;
  }));
  sh.querySelectorAll('.les textarea').forEach((t) => (t.oninput = () => { try { t.value ? localStorage.setItem(noteKey(t.dataset.n), t.value) : localStorage.removeItem(noteKey(t.dataset.n)); } catch (_) {} }));
  $('#ca').onclick = openCA; $('#stu').onclick = () => openStudio(c.id);
  const ex = $('#ex');
  if (ex) ex.onclick = () => { const ds = [...sh.querySelectorAll('.les')], o = ds.some((d) => !d.open); ds.forEach((d) => (d.open = o)); ex.textContent = o ? 'Collapse all lessons' : 'Expand all lessons'; };
  $('#cp').onclick = async () => {
    try { await navigator.clipboard.writeText(c.title + '\n' + L.map((l) => `${l.n}. ${l.title}`).join('\n')); toast('Outline copied.'); }
    catch (_) { toast('Copy is blocked here. Select the lessons and copy by hand.', 'bad'); }
  };
  $('#pr').onclick = () => { sh.querySelectorAll('.les').forEach((d) => (d.open = true)); window.print(); };
}

/* ───────────── Full lesson reader + quiz ───────────── */
async function openLesson(n) {
  $('#sheet').innerHTML = '<div class="sheet-in"><p class="meta" style="padding:40px 0;text-align:center">Opening lesson…</p></div>';
  try { S.lesson = await api(`/api/courses/${encodeURIComponent(S.openId)}/lessons/${n}`); S.lesson.result = null; goView('lesson'); }
  catch (x) { toast(x.message, 'bad'); goView('course'); }
}

function quizHTML(l) {
  const r = l.result;
  return `<h3>Check your understanding</h3>
    <p class="meta">${l.best != null ? `Your best score so far: ${l.best} of ${l.quiz.length}. ` : ''}Your score is saved to your CA record, and you can retake it to improve.</p>` +
    l.quiz.map((q, i) => `
    <fieldset class="q ${r ? (r.results[i].ok ? 'ok' : 'no') : ''}"><legend>${i + 1}. ${esc(q.q)}</legend>
      ${q.o.map((o, j) => `<label class="opt ${r && j === r.results[i].answer ? 'right' : ''}"><input type="radio" name="q${i}" value="${j}" ${r ? 'disabled' : ''} ${r && l.picks[i] === j ? 'checked' : ''}><span>${esc(o)}</span></label>`).join('')}
      ${r ? `<p class="why"><b>${r.results[i].ok ? 'Correct.' : 'Not quite.'}</b> ${esc(r.results[i].why)}</p>` : ''}
    </fieldset>`).join('') +
    (r ? `<p class="score">You scored ${r.score} of ${r.max}.</p><button class="pill" id="retake">Try the quiz again</button>`
       : '<p class="err" id="qe"></p><button class="btn" id="chk">CHECK MY ANSWERS</button>');
}

function bindQuiz(c) {
  const l = S.lesson, q = $('#quiz');
  const chk = $('#chk'), rt = $('#retake');
  if (chk) chk.onclick = async () => {
    const picks = l.quiz.map((_, i) => { const x = q.querySelector(`input[name=q${i}]:checked`); return x ? +x.value : null; });
    if (picks.includes(null)) { $('#qe').textContent = 'Answer every question first.'; return; }
    chk.disabled = true;
    try { l.result = await post(`/api/quiz/${encodeURIComponent(c.id)}/${l.n}`, { answers: picks }); l.picks = picks; l.best = Math.max(l.best ?? 0, l.result.score); }
    catch (x) { $('#qe').textContent = x.message; chk.disabled = false; return; }
    q.innerHTML = quizHTML(l); bindQuiz(c);
  };
  if (rt) rt.onclick = () => { l.result = null; q.innerHTML = quizHTML(l); bindQuiz(c); q.scrollIntoView({ behavior: 'smooth', block: 'start' }); };
}

function viewLesson(c) {
  const l = S.lesson, total = S.detail.lessons.length, done = S.detail.done.includes(l.n);
  sheet(`
  <article class="reader">
    <p class="crumb"><span>Lesson ${l.n} of ${total}</span><span>${l.minutes} minute read</span></p>
    <h2>${esc(l.title)}</h2>
    <p class="lead">${fmt(l.hook)}</p>
    <figure class="fig">${l.diagram}<figcaption>${esc(l.caption)}</figcaption></figure>
    ${l.sections.map(([h, b], i) => `<section><h3><span>${i + 1}</span>${esc(h)}</h3>${rich(b)}</section>`).join('')}
    <section class="terms"><h3>Key terms</h3><dl>${l.terms.map(([t, d]) => `<dt>${esc(t)}</dt><dd>${esc(d)}</dd>`).join('')}</dl></section>
    <section class="oops"><h3>Common mistakes to avoid</h3><ul>${l.mistakes.map((m) => `<li>${esc(m)}</li>`).join('')}</ul></section>
    ${l.activity ? `<section><div class="act"><h4>Try it yourself</h4><p>${esc(l.activity)}</p></div></section>` : ''}
    <section class="quiz" id="quiz">${quizHTML(l)}</section>
    <section><h3>Your notes</h3><textarea id="mynote" placeholder="What you learned, questions to ask, ideas for your project"></textarea><p class="meta">Saved on this device.</p></section>
    <div class="pills"><button class="pill markdone" id="md" aria-pressed="${done}">${done ? 'Marked as done' : 'Mark lesson as done'}</button>
      ${l.next ? '<button class="pill hot" id="nx">Next lesson</button>' : ''}<button class="pill" id="ca2">My CA and certificate</button></div>
  </article>`, () => goView('course'), '← Back to lessons');
  bindQuiz(c);
  const nk = `oats:note:${S.user.uid}:${c.id}:${l.n}`, nt = $('#mynote');
  try { nt.value = localStorage.getItem(nk) || ''; } catch (_) {}
  nt.oninput = () => { try { nt.value ? localStorage.setItem(nk, nt.value) : localStorage.removeItem(nk); } catch (_) {} };
  $('#md').onclick = async () => { if (!(await markDone(c, l.n))) return; const on = S.detail.done.includes(l.n); $('#md').setAttribute('aria-pressed', on); $('#md').textContent = on ? 'Marked as done' : 'Mark lesson as done'; };
  const nx = $('#nx'); if (nx) nx.onclick = () => openLesson(l.n + 1);
  $('#ca2').onclick = openCA;
}

/* ───────────── CA record, exam, certificate ───────────── */
async function openCA() {
  try { S.ca = await api('/api/ca/' + encodeURIComponent(S.openId)); goView('ca'); } catch (x) { toast(x.message, 'bad'); }
}

function viewCA(c) {
  const r = S.ca, w = r.weights;
  const intro = `<div class="glass intro"><h2>My CA and certificate</h2><p>${esc(c.title)}. Continuous assessment (CA) is the average of your best lesson quiz scores and counts for ${w.ca}%. The final exam counts for ${w.exam}%. Pass mark: ${w.pass}%.</p></div>`;
  if (!r.lessons.length) { sheet(`${intro}<p class="empty">Quizzes, the final exam and the certificate for this course are being prepared. Your lessons and projects are available now.</p>`, () => goView('course'), '← Back to lessons'); return; }
  sheet(`${intro}
    <div class="stats"><div><strong>${r.ca}%</strong><span>CA average</span></div><div><strong>${r.exam == null ? '–' : r.exam + '%'}</strong><span>Final exam</span></div><div class="${r.passed ? 'pass' : ''}"><strong>${r.total}%</strong><span>Overall</span></div></div>
    <div class="glass tablewrap"><table><thead><tr><th>Lesson quiz</th><th>Best score</th><th>Tries</th></tr></thead><tbody>
      ${r.lessons.map((l) => `<tr><td>${l.n}. ${esc(l.title)}</td><td>${l.pct == null ? 'Not taken' : l.pct + '%'}</td><td>${l.tries}</td></tr>`).join('')}
    </tbody></table></div>
    <div class="glass intro next"><h3>${r.cert ? 'You earned this certificate' : r.passed ? 'You passed. Your certificate is ready.' : r.exam != null ? 'Almost there' : 'Your next step'}</h3>
      <p>${r.cert || r.passed ? 'Download it, share it, and anyone can verify it online with its ID.' : !r.examReady ? 'Take every lesson quiz first. The final exam opens when your CA record is complete.' : r.exam != null ? `Your overall score is ${r.total}%. You need ${w.pass}% to earn the certificate. Retake the exam to improve.` : 'Your CA record is complete. Take the final exam to earn your certificate.'}</p>
      <div class="pills">${r.cert || r.passed ? `<button class="btn" id="gc">${r.cert ? 'VIEW AND DOWNLOAD CERTIFICATE' : 'GET MY CERTIFICATE'}</button>` : ''}
        <button class="pill ${r.cert || r.passed ? '' : 'hot'}" id="ex" ${r.examReady ? '' : 'disabled'}>${r.exam == null ? 'Take the final exam' : 'Retake the final exam'}</button></div></div>`,
    () => goView('course'), '← Back to lessons');
  const gc = $('#gc'); if (gc) gc.onclick = async () => {
    gc.disabled = true;
    try { S.cert = await post('/api/certificate/' + encodeURIComponent(c.id), {}); goView('cert'); } catch (x) { toast(x.message, 'bad'); gc.disabled = false; }
  };
  $('#ex').onclick = async () => {
    try { S.exam = await api('/api/exam/' + encodeURIComponent(c.id)); S.exam.result = null; goView('exam'); } catch (x) { toast(x.message, 'bad'); }
  };
}

function viewExam(c) {
  const ex = S.exam, r = ex.result;
  sheet(`
    <div class="glass intro"><h2>Final exam</h2><p>${esc(c.title)}. ${ex.questions.length} questions drawn from your lessons. Answer every question, then submit. You can retake it later.</p></div>
    <div class="glass exam" id="exq">${ex.questions.map((q, i) => `
      <fieldset class="q ${r ? (r.results[i].ok ? 'ok' : 'no') : ''}"><legend>${i + 1}. ${esc(q.q)}</legend>
        ${q.o.map((o, j) => `<label class="opt ${r && j === r.results[i].answer ? 'right' : ''}"><input type="radio" name="x${i}" value="${j}" ${r ? 'disabled' : ''} ${r && ex.picks[i] === j ? 'checked' : ''}><span>${esc(o)}</span></label>`).join('')}
        ${r ? `<p class="why"><b>${r.results[i].ok ? 'Correct.' : 'Not quite.'}</b> ${esc(r.results[i].why)}</p>` : ''}
      </fieldset>`).join('')}
      ${r ? `<p class="score">Exam score: ${r.score} of ${r.max}. Overall: ${r.ca.total}% ${r.ca.passed ? '(passed)' : '(pass mark ' + r.ca.weights.pass + '%)'}.</p><button class="btn" id="back2">BACK TO MY CA RECORD</button>`
         : '<p class="err" id="xe"></p><button class="btn" id="sub">SUBMIT EXAM</button>'}
    </div>`, () => openCA(), '← My CA record');
  const sub = $('#sub'); if (sub) sub.onclick = async () => {
    const picks = ex.questions.map((_, i) => { const x = document.querySelector(`input[name=x${i}]:checked`); return x ? +x.value : null; });
    if (picks.includes(null)) { $('#xe').textContent = 'Answer every question first.'; return; }
    sub.disabled = true;
    try { ex.result = await post('/api/exam/' + encodeURIComponent(c.id), { answers: picks }); ex.picks = picks; }
    catch (x) { $('#xe').textContent = x.message; sub.disabled = false; return; }
    renderSheet(); $('#sheet').scrollTop = 0;
  };
  const b2 = $('#back2'); if (b2) b2.onclick = openCA;
}

async function drawCert(ct) {
  try { await Promise.all([document.fonts.load('700 64px "Chakra Petch"'), document.fonts.load('400 28px Sora')]); } catch (_) {}
  const W = 1600, H = 1130, cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  const x = cv.getContext('2d'), F = (w, s) => `${w} ${s}px "Chakra Petch", sans-serif`, B = (s) => `400 ${s}px Sora, sans-serif`;
  const bg = x.createLinearGradient(0, 0, W, H); bg.addColorStop(0, '#0D0E15'); bg.addColorStop(.55, '#161033'); bg.addColorStop(1, '#0b1a2b');
  x.fillStyle = bg; x.fillRect(0, 0, W, H);
  const glow = x.createRadialGradient(W / 2, H * 1.05, 40, W / 2, H * 1.05, 720); glow.addColorStop(0, 'rgba(0,240,255,.32)'); glow.addColorStop(1, 'rgba(0,240,255,0)');
  x.fillStyle = glow; x.fillRect(0, 0, W, H);
  x.strokeStyle = '#00F0FF'; x.lineWidth = 6; x.strokeRect(40, 40, W - 80, H - 80);
  x.strokeStyle = 'rgba(138,43,226,.85)'; x.lineWidth = 2; x.strokeRect(64, 64, W - 128, H - 128);
  x.textAlign = 'center';
  x.strokeStyle = '#00F0FF'; x.lineWidth = 5; x.beginPath(); [[0, -46], [40, -23], [40, 23], [0, 46], [-40, 23], [-40, -23]].forEach(([a, b], i) => x[i ? 'lineTo' : 'moveTo'](W / 2 + a, 160 + b)); x.closePath(); x.stroke();
  x.strokeStyle = '#fff'; x.lineWidth = 5; x.lineCap = 'round'; x.beginPath(); x.arc(W / 2, 170, 20, Math.PI, 0); x.moveTo(W / 2 - 30, 170); x.lineTo(W / 2 + 30, 170); x.stroke();
  x.fillStyle = '#00F0FF'; x.font = F(700, 38); x.fillText('OPEN AIR TECH SPACE', W / 2, 270);
  x.fillStyle = '#fff'; x.font = F(700, 92); x.fillText('Certificate of Completion', W / 2, 400);
  x.fillStyle = '#8A93AD'; x.font = B(32); x.fillText('This certifies that', W / 2, 490);
  let size = 112; x.fillStyle = '#fff'; x.font = F(700, size);
  while (x.measureText(ct.fullName).width > 1250 && size > 44) { size -= 4; x.font = F(700, size); }
  x.fillText(ct.fullName, W / 2, 620);
  x.strokeStyle = 'rgba(0,240,255,.6)'; x.lineWidth = 2; x.beginPath(); x.moveTo(W / 2 - 480, 658); x.lineTo(W / 2 + 480, 658); x.stroke();
  x.fillStyle = '#8A93AD'; x.font = B(32); x.fillText('has successfully completed the course', W / 2, 735);
  size = 64; x.fillStyle = '#8defff'; x.font = F(700, size);
  while (x.measureText(ct.course).width > 1250 && size > 34) { size -= 3; x.font = F(700, size); }
  x.fillText(ct.course, W / 2, 825);
  const grade = ct.score >= 80 ? 'Distinction' : ct.score >= 65 ? 'Merit' : 'Pass';
  x.fillStyle = '#E8ECF5'; x.font = B(34); x.fillText(`Overall score ${ct.score}%   |   ${grade}`, W / 2, 900);
  x.textAlign = 'left'; x.fillStyle = '#8A93AD'; x.font = B(26);
  x.fillText('Date issued', 130, 955); x.fillStyle = '#fff'; x.font = B(30); x.fillText(ct.issuedAt, 130, 995);
  x.textAlign = 'right'; x.fillStyle = '#8A93AD'; x.font = B(26); x.fillText('Certificate ID', W - 130, 955); x.fillStyle = '#fff'; x.font = F(700, 32); x.fillText(ct.certId, W - 130, 995);
  x.textAlign = 'center'; x.fillStyle = '#8A93AD'; x.font = B(22); x.fillText(`Verify this certificate: ${ct.verifyUrl}`, W / 2, 1036);
  return cv;
}

async function viewCert(c) {
  const ct = S.cert;
  sheet(`<div class="glass intro"><h2>Your certificate</h2><p>Share it with employers or schools. Anyone can check it is real by opening the verification link printed on it.</p>
    <div class="pills"><button class="btn" id="dl">DOWNLOAD (PNG)</button><button class="pill" id="pc">Print or save as PDF</button><button class="pill" id="cl">Copy verification link</button></div></div>
    <div class="certbox" id="cb"><p class="meta">Preparing your certificate…</p></div>`, openCA, '← My CA record');
  const cv = await drawCert(ct); if (S.view !== 'cert') return;
  cv.setAttribute('aria-label', `Certificate of completion for ${ct.fullName}, ${ct.course}`); $('#cb').innerHTML = ''; $('#cb').append(cv);
  $('#dl').onclick = () => cv.toBlob((b) => { const a = document.createElement('a'); a.href = URL.createObjectURL(b); a.download = `Certificate-${ct.certId}.png`; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 4000); });
  $('#pc').onclick = () => {
    const d = document.createElement('div'); d.id = 'certprint'; const im = new Image(); im.src = cv.toDataURL('image/png'); d.append(im); document.body.append(d);
    document.body.classList.add('printcert'); im.onload = () => { window.print(); document.body.classList.remove('printcert'); d.remove(); };
  };
  $('#cl').onclick = async () => { try { await navigator.clipboard.writeText(ct.verifyUrl); toast('Verification link copied.'); } catch (_) { toast(ct.verifyUrl); } };
}

/* ───────────── Project Studio ───────────── */
function openStudio(cid) {
  if (cid) S.studio.cid = cid;
  S.openId = cid || null; S.view = 'projects';
  $('#sheet').hidden = false; document.body.classList.add('lock'); renderSheet();
}

function briefHTML({ project: p, rubric }) {
  const ol = (a) => `<ol>${a.map((x) => `<li>${esc(x)}</li>`).join('')}</ol>`, ul = (a) => `<ul>${a.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`;
  return `<article class="glass brief"><p class="meta">${p.ai ? 'Tailored by AI' : 'Project brief'}. About ${esc(p.hours)} hours of work.</p><h2>${esc(p.title)}</h2>
    <h4>The situation</h4><p>${esc(p.scenario)}</p><h4>Your objective</h4><p>${esc(p.objective)}</p>
    <h4>Requirements</h4>${ol(p.requirements)}<h4>Steps to follow</h4>${ol(p.steps)}<h4>What to hand in</h4>${ul(p.deliverables)}
    <h4>Marking guide (100 marks)</h4><table><tbody>${rubric.map((r) => `<tr><td>${esc(r.item)}</td><td>${r.points}</td></tr>`).join('')}</tbody></table>
    <h4>Stretch goals</h4>${ul(p.stretch)}
    <div class="pills"><button class="pill" id="pp">Print or save as PDF</button><button class="pill" id="cbf">Copy brief</button><button class="pill hot" id="gen2">Generate another</button></div></article>`;
}

function viewStudio() {
  const st = S.studio, mine = S.courses.filter((c) => isOwned(c.id));
  if (!mine.length) { sheet('<div class="glass intro"><h2>Project Studio</h2><p>Unlock a course to get class projects made for you.</p></div>', closeSheet, '← All tracks'); return; }
  if (!st.cid || !isOwned(st.cid)) st.cid = mine[0].id;
  sheet(`
    <div class="glass intro"><h2>Project Studio</h2><p>Pick a course, a theme and a level. You get a real-world project brief with requirements, steps, what to hand in and a marking guide. Make as many as you like.</p></div>
    <div class="glass panel studio">
      <label for="sc">Course</label><select id="sc">${mine.map((c) => `<option value="${esc(c.id)}" ${c.id === st.cid ? 'selected' : ''}>${esc(c.title)}</option>`).join('')}</select>
      <label>Who is the project for?</label>
      <div class="chips">${THEMES.map((t) => `<button type="button" class="chipb" aria-pressed="${st.theme === t}">${t}</button>`).join('')}</div>
      <input id="th" placeholder="Or type your own, for example Barber shop" maxlength="40" value="${THEMES.includes(st.theme) ? '' : esc(st.theme)}">
      <label>Level</label>
      <div class="seg">${['beginner', 'intermediate', 'advanced'].map((l) => `<button type="button" data-l="${l}" aria-pressed="${st.level === l}">${cap(l)}</button>`).join('')}</div>
      <p class="err" id="e"></p><button class="btn" id="gen">GENERATE MY PROJECT</button>
    </div>
    <div id="brief">${st.brief ? briefHTML(st.brief) : ''}</div>`, closeSheet, '← All tracks');
  const sh = $('#sheet');
  $('#sc').onchange = (ev) => { st.cid = ev.target.value; st.brief = null; $('#brief').innerHTML = ''; };
  sh.querySelectorAll('.chipb').forEach((b) => (b.onclick = () => { st.theme = b.textContent; $('#th').value = ''; sh.querySelectorAll('.chipb').forEach((x) => x.setAttribute('aria-pressed', x === b)); }));
  $('#th').oninput = (ev) => { st.theme = ev.target.value.trim() || 'School'; sh.querySelectorAll('.chipb').forEach((x) => x.setAttribute('aria-pressed', x.textContent === st.theme)); };
  sh.querySelectorAll('.seg button').forEach((b) => (b.onclick = () => { st.level = b.dataset.l; sh.querySelectorAll('.seg button').forEach((x) => x.setAttribute('aria-pressed', x === b)); }));
  const gen = async () => {
    const g = $('#gen'); g.disabled = true; g.innerHTML = '<span class="spin"></span>'; $('#e').textContent = '';
    try {
      st.brief = await post('/api/projects/generate', { courseId: st.cid, theme: st.theme, level: st.level });
      $('#brief').innerHTML = briefHTML(st.brief); bindBrief(gen); $('#brief').scrollIntoView({ behavior: 'smooth', block: 'start' });
    } catch (x) { $('#e').textContent = x.message; }
    g.disabled = false; g.textContent = 'GENERATE MY PROJECT';
  };
  $('#gen').onclick = gen;
  if (st.brief) bindBrief(gen);
}

function bindBrief(gen) {
  const p = S.studio.brief.project;
  $('#pp').onclick = () => window.print();
  $('#gen2').onclick = gen;
  $('#cbf').onclick = async () => {
    const t = `${p.title}\n\n${p.scenario}\n\nObjective: ${p.objective}\n\nRequirements:\n${p.requirements.map((r, i) => `${i + 1}. ${r}`).join('\n')}\n\nHand in:\n${p.deliverables.map((r) => `- ${r}`).join('\n')}`;
    try { await navigator.clipboard.writeText(t); toast('Brief copied.'); } catch (_) { toast('Copy is blocked here.', 'bad'); }
  };
}

/* ───────────── Class groups: student side ───────────── */
async function refreshCourses() {
  const d = await api('/api/courses'); S.courses = d.courses; S.group = d.group; S.pending = d.pending || 0; S.canCreate = !!d.canCreate;
}

// The card on a locked class. Inside a class group it explains whose turn it is and asks the teacher for permission.
function payCard(c) {
  const a = c.access || { state: 'open' }, nxt = a.next && (S.courses.find((x) => x.id === a.next) || {}).title;
  const card = (title, text, btn, extra = '') => `<div class="paywall" id="pw"><div class="glass pay-card"><div class="lockorb">${LOCK}</div><h3>${title}</h3><p>${text}</p>${btn}<div class="status" id="st">${esc(S.status)}</div>${extra}</div></div>`;
  if (a.state === 'later') return card('Not your turn yet', `Your class unlocks one step at a time. Finish ${nxt ? `<b>${esc(nxt)}</b>` : 'your earlier class'} first.`, '');
  if (a.state === 'pending') return card('Waiting for your teacher', 'Your request was sent. This class opens for payment as soon as your teacher allows it.', '<button class="btn" id="chk2">CHECK AGAIN</button>');
  if (a.state === 'denied') return card('Not allowed yet', 'Your teacher has not allowed this class yet. You can ask again.', '<button class="btn" id="req">ASK AGAIN</button>');
  if (a.state === 'needs_request') return card('Ask your teacher', 'Your teacher approves each new class. Send a request, and when it is allowed you can unlock this class.', '<button class="btn premium" id="req">ASK MY TEACHER</button>');
  return card('Premium course', `One-time payment. Lifetime access to all ${c.lessonsCount} lessons, quizzes, CA record and certificate.`,
    `<button class="btn premium" id="buy">UNLOCK PREMIUM COURSE<small>Access for ${money(PRICE)}</small></button>`, '<div class="secure">🔒 Secured by Flutterwave</div>');
}

async function requestAccess(c) {
  try { const r = await post('/api/groups/request', { courseId: c.id }); c.access = r.access; toast('Your teacher has been notified.'); }
  catch (x) { toast(x.message, 'bad'); }
  renderSheet();
}

/* ───────────── Class groups: teacher side ───────────── */
S.groups = { catalog: [], canCreate: true, mine: [], pick: [], name: '', made: null, loaded: false };

async function openGroups() {
  S.openId = null; S.view = 'groups'; S.groups.loaded = false;
  $('#sheet').hidden = false; document.body.classList.add('lock'); renderSheet();
  try {
    const [c, m] = await Promise.all([api('/api/groups/catalog'), api('/api/groups/mine')]);
    Object.assign(S.groups, { catalog: c.courses, canCreate: c.canCreate, mine: m.groups, loaded: true });
  } catch (x) { toast(x.message, 'bad'); }
  if (S.view === 'groups') renderSheet();
}

const linkRow = (label, url) => `<div class="linkrow"><span>${label}</span><input readonly value="${esc(url)}" aria-label="${label}"><button type="button" class="pill" data-copy="${esc(url)}">Copy</button></div>`;
function bindCopy(root) {
  root.querySelectorAll('[data-copy]').forEach((b) => (b.onclick = async () => {
    try { await navigator.clipboard.writeText(b.dataset.copy); toast('Link copied.'); } catch (_) { b.previousElementSibling.select(); toast('Press Ctrl+C to copy the selected link.'); }
  }));
}
const stepChips = (steps) => `<ol class="steps">${steps.map((s) => `<li>${esc(s.title)}</li>`).join('')}</ol>`;

function viewGroups() {
  const G = S.groups, no = (id) => (G.catalog.find((c) => c.id === id) || {}).classNo;
  const form = !G.loaded ? '<p class="meta" style="text-align:center;padding:30px 0">Loading…</p>' : !G.canCreate ? '<p class="empty">Only approved teachers can create class groups.</p>' : `
    <div class="glass panel studio">
      <label for="gname">Group name</label><input id="gname" maxlength="60" placeholder="Lagos evening class" value="${esc(G.name)}">
      <label>Pick the classes in the order students must take them. Tap to add, tap again to remove.</label>
      <div class="picks">${G.catalog.map((c) => { const i = G.pick.indexOf(c.id); return `<button type="button" class="pick" data-id="${esc(c.id)}" aria-pressed="${i >= 0}"><span class="ord">${i >= 0 ? i + 1 : ''}</span><span><small>Class ${c.classNo}</small>${esc(c.title)}</span></button>`; }).join('')}</div>
      <p class="meta" id="order">${G.pick.length ? 'Order: ' + G.pick.map((id) => 'Class ' + no(id)).join(' → ') : 'No classes picked yet.'}</p>
      <div class="pills"><button type="button" class="pill" id="pall">Pick all in order</button><button type="button" class="pill" id="pclr">Clear</button></div>
      <p class="err" id="e"></p><button class="btn" id="mk">CREATE GROUP</button>
    </div>`;
  const made = G.made ? `<div class="glass intro made"><h3>Group created: ${esc(G.made.name)}</h3>
      <p>Send the invite link to your students. Keep the admin link for yourself: anyone who has it can approve purchases and see your students.</p>
      ${linkRow('Invite link', G.made.joinUrl)}${linkRow('Admin link', G.made.adminUrl)}${stepChips(G.made.steps)}
      <div class="pills"><a class="pill hot" href="${esc(G.made.adminUrl)}" target="_blank" rel="noopener">Open admin page</a></div></div>` : '';
  const mine = G.mine.length ? `<h3 class="sec">Your groups</h3>` + G.mine.map((m) => `<div class="glass intro mygroup"><h3>${esc(m.name)}</h3>
      <p>${m.students} student${m.students === 1 ? '' : 's'}${m.pending ? `, <b class="waiting">${m.pending} waiting for your answer</b>` : ''}</p>${stepChips(m.steps)}
      ${linkRow('Invite link', m.joinUrl)}${linkRow('Admin link', m.adminUrl)}<div class="pills"><a class="pill hot" href="${esc(m.adminUrl)}" target="_blank" rel="noopener">Open admin page</a></div></div>`).join('') : '';
  sheet(`<div class="glass intro"><h2>Class groups</h2><p>Make a group for your students. They join with your invite link, can only buy the next class in your order, and you approve every new class after the first.</p></div>${form}${made}${mine}`, closeSheet, '← All tracks');
  bindCopy($('#sheet'));
  if (!G.loaded || !G.canCreate) return;
  $('#gname').oninput = (ev) => { G.name = ev.target.value; };
  $('#sheet').querySelectorAll('.pick').forEach((b) => (b.onclick = () => { const i = G.pick.indexOf(b.dataset.id); if (i >= 0) G.pick.splice(i, 1); else G.pick.push(b.dataset.id); renderSheet(); }));
  $('#pall').onclick = () => { G.pick = G.catalog.map((c) => c.id); renderSheet(); };
  $('#pclr').onclick = () => { G.pick = []; renderSheet(); };
  $('#mk').onclick = async () => {
    const e = $('#e'), b = $('#mk'); e.textContent = '';
    if (G.name.trim().length < 3) { e.textContent = 'Give the group a name of at least 3 characters.'; return; }
    if (!G.pick.length) { e.textContent = 'Pick at least one class.'; return; }
    b.disabled = true; b.innerHTML = '<span class="spin"></span>';
    try {
      G.made = (await post('/api/groups', { name: G.name.trim(), courses: G.pick })).group;
      G.mine = (await api('/api/groups/mine')).groups; G.name = ''; G.pick = []; renderSheet(); $('#sheet').scrollTop = 0;
    } catch (x) { e.textContent = x.message; b.disabled = false; b.textContent = 'CREATE GROUP'; }
  };
}

/* The teacher's private page. Opened from the admin link, it needs no sign-in. */
async function renderAdmin(token) {
  document.title = 'Class admin | ' + APP;
  const load = async () => {
    try { paintAdmin(token, await api('/api/groups/admin/' + encodeURIComponent(token))); }
    catch (x) { $('#app').innerHTML = `<section class="login"><div class="login-box"><div class="logo">${MARK}</div><h1>Admin link<br>not valid</h1><p class="sub">${esc(x.message)}</p></div></section>`; }
  };
  await load(); setInterval(() => { if (!document.hidden) load(); }, 30000);
}

function paintAdmin(token, d) {
  const g = d.group, waiting = d.requests.filter((r) => r.status === 'pending');
  const tag = { pending: 'Waiting', allowed: 'Allowed', denied: 'Not allowed' };
  $('#app').innerHTML = `<div class="admin">
    <header class="hero"><div class="hero-top"><span class="brandmark">${MARK}<b>${APP}</b></span><span class="spacer"></span><span class="badge"><i></i>Class admin</span></div>
      <div class="hero-body"><div><p class="welcome">Class group</p><h1 class="adminh">${esc(g.name)}</h1><p class="lede">Keep this page's link private. It lets you approve classes and see your students.</p></div></div></header>
    <section class="glass intro"><h3>Invite students</h3><p>Students who open this link and sign in join your group automatically.</p>${linkRow('Invite link', g.joinUrl)}
      <h3 class="sec">Class order</h3>${stepChips(g.steps)}</section>
    <section class="glass intro"><h3>Requests ${waiting.length ? `<b class="waiting">${waiting.length} waiting</b>` : ''}</h3>
      ${d.requests.length ? d.requests.map((r) => `<div class="reqrow ${r.status}"><div><b>${esc(r.student)}</b> wants to unlock <b>${esc(r.course)}</b><small>${esc(r.email)}, ${esc(r.at)}</small></div>
        ${r.status === 'pending' ? `<div class="pills"><button class="pill hot" data-rid="${r.id}" data-allow="1">Allow</button><button class="pill" data-rid="${r.id}" data-allow="0">Do not allow</button></div>` : `<span class="tag ${r.status}">${tag[r.status]}</span>`}</div>`).join('') : '<p class="meta">No requests yet. When a student asks to unlock the next class, it appears here and you get an email.</p>'}</section>
    <section class="glass intro"><h3>Students (${d.students.length})</h3>${d.students.length ? `<div class="tablewrap"><table><thead><tr><th>Student</th>${g.steps.map((s, i) => `<th>Step ${i + 1}: ${esc(s.title)}</th>`).join('')}<th></th></tr></thead><tbody>
      ${d.students.map((s) => `<tr><td><b>${esc(s.name)}</b><br><small>${esc(s.email)}<br>Joined ${esc(s.joinedAt)}</small></td>${s.classes.map((c) => `<td>${c.owned ? `Unlocked<br><small>${c.done} of ${c.total} lessons${c.score ? `<br>CA ${c.score.ca}%, exam ${c.score.exam == null ? 'not taken' : c.score.exam + '%'}${c.score.passed ? ', passed' : ''}` : ''}</small>` : '<small>Not yet</small>'}</td>`).join('')}
        <td><button class="pill" data-rm="${esc(s.uid)}" data-name="${esc(s.name)}">Remove</button></td></tr>`).join('')}</tbody></table></div>` : '<p class="meta">No students yet. Send them the invite link.</p>'}</section></div>`;
  bindCopy($('#app'));
  $('#app').querySelectorAll('[data-rid]').forEach((b) => (b.onclick = async () => {
    b.disabled = true;
    try { await post(`/api/groups/admin/${encodeURIComponent(token)}/requests/${b.dataset.rid}`, { allow: b.dataset.allow === '1' }); toast(b.dataset.allow === '1' ? 'Allowed. The student can now unlock it.' : 'Not allowed.'); }
    catch (x) { toast(x.message, 'bad'); }
    paintAdmin(token, await api('/api/groups/admin/' + encodeURIComponent(token)));
  }));
  $('#app').querySelectorAll('[data-rm]').forEach((b) => (b.onclick = async () => {
    if (!confirm(`Remove ${b.dataset.name} from this group? They keep any classes they already bought, but are no longer limited to your class order.`)) return;
    try { await post(`/api/groups/admin/${encodeURIComponent(token)}/students/${encodeURIComponent(b.dataset.rm)}/remove`, {}); } catch (x) { toast(x.message, 'bad'); }
    paintAdmin(token, await api('/api/groups/admin/' + encodeURIComponent(token)));
  }));
}
