'use strict';
/* ═══════════ Air Omega everywhere: it knows the app, opens places and sets things up ═══════════
   Two ways in, both end in the same places:
   1. Quick commands ("open the cloud playground") are understood right here, instantly, with no AI call.
   2. Everything else goes to the AI, which answers with actions. The server checks every action against a fixed list first. */

const AIR_WAIT = (ms) => new Promise((r) => setTimeout(r, ms));
const AIR_COURSES = {
  'prompt-engineering': ['prompt engineering', 'prompts', 'prompt'], animation: ['3d animation', 'animation', 'animate'], 'cloud-computing': ['cloud computing', 'cloud'],
  'web-development': ['web development', 'web dev', 'websites', 'website', 'web'], 'app-development': ['app development', 'app dev', 'mobile apps', 'mobile app', 'apps', 'app'],
  'full-stack': ['full stack', 'fullstack', 'full-stack', 'back end', 'backend'], 'agentic-ai': ['agentic ai', 'agentic', 'ai agents', 'ai agent', 'agents', 'agent'],
  'game-development': ['game development', 'game dev', 'games', 'game'],
};
const AIR_PLAY_NAMES = { 'prompt lab': 'prompt-engineering', 'code studio': 'web-development', 'keyframe studio': 'animation', 'traffic surge simulator': 'cloud-computing', 'traffic simulator': 'cloud-computing',
  'cloud simulator': 'cloud-computing', 'screen builder': 'app-development', 'api lab': 'full-stack', 'agent lab': 'agentic-ai', 'game tuner': 'game-development' };
const AIR_NUM = { one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8 };
const AIR_WHERE = { dashboard: 'the dashboard', leaderboard: 'the weekly leaderboard', parent_updates: 'Parent updates', class_groups: 'Class groups', project_studio: 'Project Studio' };
const airTitle = (id) => ((S.courses || []).find((c) => c.id === id) || {}).title || id;
const airNorm = (t) => String(t).toLowerCase().replace(/[’']/g, '').replace(/[^a-z0-9\s-]/g, ' ').replace(/\s+/g, ' ').trim();

/* ───────────── Quick commands, understood on the spot ───────────── */
function airQuick(text, ctx = {}) {
  let t = airNorm(text); if (!t || t.length > 90) return null;
  t = t.replace(/^(hey|hi|hello|ok|okay|yo)\s+/, '').replace(/^(air omega|omega)\s*/, '');
  for (let i = 0; i < 3; i++) t = t.replace(/^(please|kindly|can you|could you|would you|will you|i want to|i wanna|i would like to|id like to|lets|let us|just)\s+/, '');
  t = t.replace(/\s+(please|now|for me|thanks|thank you)$/, '');
  const out = (action) => ({ actions: [action], say: airSay(action) });
  if (/^(stop|be quiet|quiet|silence|stop talking|stop reading|stop listening)$/.test(t)) return out({ type: 'stop_audio' });
  if (/^(go back|back|take me back)$/.test(t)) return out({ type: 'back' });
  if (/^(close|close this|close it|exit|go to the dashboard|go home)$/.test(t)) return out(t.startsWith('go') ? { type: 'open', where: 'dashboard' } : { type: 'close' });
  if (ctx.view === 'lesson' && /^(read|read out|read aloud|narrate|listen to)\s+(this|it|the lesson|this lesson|this page|it to me|this to me)$/.test(t)) return out({ type: 'listen' });
  const V = /^(open|go to|go|take me to|take me|bring me to|show me|show|launch|start|bring up|navigate to|switch to|visit|jump to|load|view|see)\s+/, m = V.exec(t);
  if (!m) return null;
  let rest = t.slice(m[0].length).replace(/^(me|us)\s+/, '');
  if (/^(my|unlocked)\s+(tracks|courses)(\s+(page|screen))?$/.test(rest)) return out({ type: 'tracks', filter: 'mine' });   // before "my" is dropped as filler
  for (let i = 0; i < 3; i++) rest = rest.replace(/^(the|my|a|an|to|up|on|into)\s+/, '');
  rest = rest.replace(/\s+(page|screen|section|tab|area)$/, '');
  if (!rest || rest.split(' ').length > 8 || /^(how|what|why|when|where|who|which|if|something|anything)\b/.test(rest) || /\b(and|then|also|explain|tell|because|about|so|while|after|before|with|using)\b/.test(rest)) return null;   // anything more than a plain command is for the AI
  for (const [re, where] of [[/^(dashboard|home|home page|main page|main screen|start page)$/, 'dashboard'], [/^(leaderboard|leader board|rankings?|weekly leaderboard|class leaderboard)$/, 'leaderboard'],
    [/^(parent updates?|parents?|parent emails?|parent reports?)$/, 'parent_updates'], [/^(class groups?|groups?|classes|class)$/, 'class_groups'], [/^(project studio|projects?|studio)$/, 'project_studio']]) if (re.test(rest)) return out({ type: 'open', where });
  if (/^(all )?(tracks|courses)$/.test(rest)) return out({ type: 'tracks', filter: 'all', search: '' });
  if (/^(my|unlocked) (tracks|courses)$/.test(rest)) return out({ type: 'tracks', filter: 'mine' });
  if (/^locked (tracks|courses)$/.test(rest)) return out({ type: 'tracks', filter: 'locked' });
  const pad = ` ${rest} `;
  for (const [name, cid] of Object.entries(AIR_PLAY_NAMES)) if (pad.includes(` ${name} `)) return out({ type: 'open_playground', course: cid });
  let alias = null, cid = null;
  for (const [a, id] of Object.entries(AIR_COURSES).flatMap(([id, list]) => list.map((a) => [a, id])).sort((x, y) => y[0].length - x[0].length)) if (pad.includes(` ${a} `)) { alias = a; cid = id; break; }
  const other = alias ? pad.replace(` ${alias} `, ' ').trim() : rest;
  cid = cid || ctx.course || null;
  const has = (re) => re.test(other), lesson = /\blesson (\d+|one|two|three|four|five|six|seven|eight)\b/.exec(other);
  let a = null;
  if (has(/\b(playground|lab|sandbox|simulator|builder)\b/)) a = cid && { type: 'open_playground', course: cid };
  else if (has(/\bcertificates?\b/)) a = cid && { type: 'open_certificate', course: cid };
  else if (has(/\b(exam|final exam)\b/) && !lesson) a = cid && { type: 'open_exam', course: cid };
  else if (has(/\b(weak spots?|practice|practise)\b/)) a = cid && { type: 'open_practice', course: cid };
  else if (has(/\b(ca|c a|continuous assessment|grades?|results?|scores?)\b/)) a = cid && { type: 'open_ca', course: cid };
  else if (lesson || has(/\b(assignment|quiz|mentor|pictures?)\b/)) {
    const n = lesson ? (AIR_NUM[lesson[1]] || +lesson[1]) : ctx.lesson, sec = (/\b(assignment|quiz|mentor|pictures?)\b/.exec(other) || [])[1];
    if (cid && n >= 1 && n <= 8) a = { type: 'open_lesson', course: cid, lesson: n, ...(sec ? { section: sec.startsWith('picture') ? 'pictures' : sec } : {}) };
  } else if (cid && /^(lessons?|courses?|tracks?|classes|masterclass|course page|track page|lesson list)?$/.test(other)) a = { type: 'open_course', course: cid };
  return a ? out(a) : null;
}

function airLabel(a) {
  const c = a.course ? airTitle(a.course) : '';
  switch (a.type) {
    case 'open': return `Opened ${AIR_WHERE[a.where] || a.where}`;
    case 'open_course': return `Opened ${c}`;
    case 'open_lesson': return `Opened ${c}, lesson ${a.lesson}${a.section && a.section !== 'top' ? ` (${a.section})` : ''}`;
    case 'open_playground': return `Opened the ${(PG[a.course] || {}).name || 'playground'}${a.set ? ' and set it up' : ''}`;
    case 'open_ca': return `Opened the CA record for ${c}`;
    case 'open_exam': return `Opened the final exam for ${c}`;
    case 'open_certificate': return `Opened the certificate for ${c}`;
    case 'open_practice': return `Opened weak-spot practice for ${c}`;
    case 'listen': return 'Reading the lesson aloud';
    case 'stop_audio': return 'Stopped the audio';
    case 'back': return 'Went back';
    case 'close': return 'Closed this screen';
    case 'voice': return 'Changed the voice settings';
    case 'tracks': return a.filter === 'locked' ? 'Showing locked tracks' : a.filter === 'mine' ? 'Showing my tracks' : 'Showing the tracks';
    case 'sign_out': return 'Sign out';
    default: return a.type;
  }
}
const airSay = (a) => airLabel(a).replace(/^Opened /, 'Opening ').replace(/^Reading/, 'Reading').replace(/^Stopped/, 'Okay, stopped').replace(/^Went back/, 'Going back').replace(/^Closed/, 'Closing').replace(/^Showing/, 'Showing') + '.';

/* ───────────── Where the student is, so Air Omega can answer "explain this" ───────────── */
function airWhere() {
  const sh = $('#sheet'), hidden = !sh || sh.hidden, v = hidden ? 'dashboard' : S.view;
  return { view: v, course: hidden ? '' : (S.openId || ''), lesson: v === 'lesson' && S.lesson ? S.lesson.n : 0 };
}
const airCtx = () => { const w = airWhere(); return { course: w.course || null, lesson: w.lesson || 0, view: w.view }; };
const airContext = () => (S.view === 'play' && pgRun && !$('#sheet').hidden && pgRun.context ? pgRun.context() : '');

/* ───────────── Changing things inside a playground ───────────── */
const airSet = (el, v) => { if (!el) return; if (el.type === 'checkbox') el.checked = !!v; else el.value = v; el.dispatchEvent(new Event(el.tagName === 'SELECT' || el.type === 'checkbox' ? 'change' : 'input', { bubbles: true })); };
const PG_CONTROL = {
  'prompt-engineering': (el, p) => { if (p.challenge !== undefined) airSet(el.querySelector('#pl-ch'), p.challenge); if (p.prompt) airSet(el.querySelector('#pl-p'), p.prompt); },
  'web-development': (el, p) => { if (p.template) airSet(el.querySelector('#cs-t'), p.template); },
  animation: (el, p) => { if (p.preset) airSet(el.querySelector('#an-pre'), p.preset); if (p.easing) airSet(el.querySelector('#an-ease'), p.easing); if (p.duration) airSet(el.querySelector('#an-dur'), p.duration); },
  'cloud-computing': (el, p) => { [['scenario', '#cl-sc'], ['size', '#cl-sz'], ['servers', '#cl-n'], ['replicas', '#cl-r'], ['max', '#cl-m'], ['lb', '#cl-lb'], ['auto', '#cl-au'], ['cdn', '#cl-cdn']].forEach(([k, s]) => { if (p[k] !== undefined) airSet(el.querySelector(s), p[k]); }); },
  'app-development': (el, p) => { if (p.template) airSet(el.querySelector('#ab-tpl'), p.template); if (p.dark !== undefined) airSet(el.querySelector('#ab-dark'), p.dark); },
  'full-stack': (el, p) => { if (p.request !== undefined) { const b = el.querySelector(`[data-q="${p.request}"]`); if (b) b.click(); } if (p.send) el.querySelector('#al-send').click(); },
  'agentic-ai': (el, p) => { if (p.goal) airSet(el.querySelector('#ag-g'), p.goal); if (p.tools) el.querySelectorAll('.agtool input').forEach((i) => { i.checked = p.tools.includes(i.value); }); if (p.run) el.querySelector('#ag-run').click(); },
  'game-development': (el, p) => { if (p.preset) airSet(el.querySelector('#gm-pre'), p.preset); if (p.play) el.querySelector('#gm-go').click(); },
};

/* ───────────── The action engine ───────────── */
const airNarrow = () => !!(window.matchMedia && matchMedia('(max-width: 700px)').matches);
async function airCourse(cid) { closeSheet(); await openCourse(cid); return isOwned(cid); }
async function airScroll(section) {
  const id = { mentor: '#mentor', pictures: '#imgs', quiz: '#quiz', assignment: '#assign' }[section]; if (!id) return;
  await AIR_WAIT(150); const el = $(id); if (el && el.scrollIntoView) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
const airLocked = () => toast('That track is locked. I opened its page, where you can unlock it.', 'bad');

async function airDo(a) {
  try {
    switch (a.type) {
      case 'open':
        if (a.where === 'dashboard') { closeSheet(); return true; }
        if (a.where === 'leaderboard') { closeSheet(); await openBoard(); return true; }
        if (a.where === 'parent_updates') { closeSheet(); await openParents(); return true; }
        if (a.where === 'project_studio') { closeSheet(); openStudio(); return true; }
        if (a.where === 'class_groups') { if (!S.canCreate) { toast('Class groups are for teachers. Ask your teacher for an invite link to join one.', 'bad'); return false; } closeSheet(); await openGroups(); return true; }
        return false;
      case 'open_course': return (await airCourse(a.course), true);
      case 'open_lesson': if (!(await airCourse(a.course))) { airLocked(); return false; } await openLesson(a.lesson); if (a.section) await airScroll(a.section); return true;
      case 'open_playground': {
        if (!(await airCourse(a.course))) { airLocked(); return false; }
        openPlayground(); await AIR_WAIT(60); const box = $('#pgbox'); if (a.set && box && PG_CONTROL[a.course]) PG_CONTROL[a.course](box, a.set); return true;
      }
      case 'open_ca': case 'open_exam': case 'open_certificate': {
        if (!(await airCourse(a.course))) { airLocked(); return false; }
        await openCA(); await AIR_WAIT(60);
        if (a.type === 'open_exam') { const ex = $('#ex'); if (ex && !ex.disabled) ex.click(); else { toast('The final exam opens after you have taken every lesson quiz in this track.', 'bad'); return false; } }
        if (a.type === 'open_certificate') { const gc = $('#gc'); if (gc) gc.click(); else { toast('The certificate comes after you pass the final exam.', 'bad'); return false; } }
        return true;
      }
      case 'open_practice': if (!(await airCourse(a.course))) { airLocked(); return false; } await openPractice(); return true;
      case 'listen':
        if (S.view !== 'lesson' || !S.lesson || $('#sheet').hidden) { toast('Open a lesson first, then I can read it to you.', 'bad'); return false; }
        if (!canSpeak()) { toast('This browser cannot read aloud.', 'bad'); return false; }
        voStop(); startListening(S.lesson); return true;
      case 'stop_audio': voStop(); stopListening(); return true;
      case 'back': if (['lesson', 'ca', 'practice', 'play', 'exam', 'cert'].includes(S.view) && S.openId) goView('course'); else closeSheet(); return true;
      case 'close': closeSheet(); return true;
      case 'voice': {
        const p = voPrefs(); if (a.voice) p.voice = 'ai:' + a.voice; if (a.speed) p.rate = a.speed; if (a.speak_replies !== undefined) p.speak = a.speak_replies; voSave(p);
        airDock.syncVoice(); document.querySelectorAll('.v-voice').forEach((s) => { s.value = p.voice; });
        if (a.conversation !== undefined) airDock.setConversation(a.conversation);
        return true;
      }
      case 'tracks': closeSheet(); if (a.filter) S.filter = a.filter; if (a.search !== undefined) S.q = a.search; renderDashboard(false); return true;
      case 'sign_out': if (!confirm('Sign out of Open Air Tech Space?')) return false; closeSheet(); { const out = $('#out'); if (out) out.click(); } return true;
      default: return false;
    }
  } catch (x) { toast(x && x.message ? x.message : 'I could not do that.', 'bad'); return false; }
}

async function airRun(actions) {
  let moved = false;
  for (const a of actions) { const ok = await airDo(a); if (ok && !['voice', 'listen', 'stop_audio'].includes(a.type)) moved = true; await AIR_WAIT(180); }
  if (moved && airNarrow()) airDock.collapse();   // on a phone, get out of the way so the student can see what was opened
}

/* ───────────── The floating Air Omega, on every screen ───────────── */
const airDock = (() => {
  let root = null, chat = null, opened = false, mounting = false;
  const q = (s) => root && root.querySelector(s);
  function build() {
    if (root) return;
    root = document.createElement('div'); root.id = 'airdock'; root.className = 'airdock'; root.hidden = true;
    root.innerHTML = `<button id="airfab" class="airfab" aria-label="Open Air Omega, your AI assistant" aria-expanded="false"><span aria-hidden="true">🎙</span><b>Air Omega</b></button>
      <section id="airpanel" class="airpanel" role="dialog" aria-label="Air Omega" hidden>
        <header><strong>🎙 Air Omega</strong><span class="grow"></span><button id="airmem" aria-label="What Air Omega remembers about me" title="What Air Omega remembers about me">🧠</button><button id="airmin" aria-label="Minimise" title="Minimise">–</button></header>
        <div id="airmemo" class="airmemo" hidden></div><div id="airchat" class="airchat"></div></section>`;
    document.body.append(root);
    q('#airfab').onclick = () => (opened ? close() : open());
    q('#airmin').onclick = close; q('#airmem').onclick = toggleMemory;
    root.addEventListener('keydown', (e) => { if (e.key === 'Escape' && opened) { e.stopPropagation(); close(); } });
  }
  function show() { build(); root.hidden = false; }
  function hide() { if (chat) chat.destroy(); chat = null; opened = false; if (root) { root.hidden = true; q('#airpanel').hidden = true; q('#airchat').innerHTML = ''; q('#airmemo').hidden = true; q('#airfab').setAttribute('aria-expanded', 'false'); } }
  async function open() {
    show(); opened = true; q('#airpanel').hidden = false; q('#airfab').setAttribute('aria-expanded', 'true');
    if (!chat && !mounting) {
      mounting = true;
      try { chat = await pgChat(q('#airchat'), { url: '/api/talk', persist: true, compact: true, quick: ['What should I do next?', 'Explain this page', 'Show my tracks'], placeholder: 'Say or type what you want. Try: open the Prompt Lab' }); }
      finally { mounting = false; }
    } else if (chat) chat.refresh();
    const t = q('.c-q'); if (t && !airNarrow()) t.focus();
  }
  function close() { if (chat) chat.pause(); if (root) { q('#airpanel').hidden = true; q('#airfab').setAttribute('aria-expanded', 'false'); } opened = false; }
  async function toggleMemory() {
    const box = q('#airmemo'); if (!box.hidden) { box.hidden = true; return; }
    box.hidden = false; box.innerHTML = '<p class="meta">Loading…</p>';
    const paint = (notes) => {
      box.innerHTML = `<h4>What Air Omega remembers about you</h4>${notes.length ? `<ul>${notes.map((n) => `<li><span>${esc(n.note)}</span><button data-f="${n.id}" aria-label="Forget this">✕</button></li>`).join('')}</ul><button class="pill" id="airforget">Forget everything</button>`
        : '<p class="meta">Nothing yet. As you chat, Air Omega may remember useful things, like your goals, so it can help you better. You can see and delete everything here.</p>'}`;
      box.querySelectorAll('[data-f]').forEach((b) => (b.onclick = async () => { try { paint((await post('/api/talk/memory/forget', { id: +b.dataset.f })).notes); } catch (x) { toast(x.message, 'bad'); } }));
      const fa = box.querySelector('#airforget'); if (fa) fa.onclick = async () => { try { paint((await post('/api/talk/memory/forget', { all: true })).notes); } catch (x) { toast(x.message, 'bad'); } };
    };
    try { paint((await api('/api/talk/memory')).notes); } catch (x) { box.innerHTML = `<p class="err">${esc(x.message)}</p>`; }
  }
  return {
    show, hide, open, close, collapse: () => { if (opened) close(); }, isOpen: () => opened,
    syncVoice: () => { if (chat) chat.syncVoice(); }, setConversation: (on) => { if (chat) chat.setConversation(on); },
  };
})();
