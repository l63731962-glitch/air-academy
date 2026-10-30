'use strict';
/* ═══════════ Air Omega Live: voice, open chat and the playgrounds ═══════════ */
const PG = {};                          // one playground per course id, filled in further down
const pgCleanups = [];
const pgOnCleanup = (fn) => pgCleanups.push(fn);
function pgCleanup() { while (pgCleanups.length) { try { pgCleanups.pop()(); } catch (_) {} } voStop(); }

/* ───────────── Voice: Air Omega speaks (and listens) ───────────── */
const VO_KEY = 'oats:voice';
const voPrefs = () => { let p = {}; try { p = JSON.parse(localStorage.getItem(VO_KEY) || '{}'); } catch (_) {} return { voice: 'ai:coral', speak: false, rate: 1, ...p }; };
const voSave = (p) => { try { localStorage.setItem(VO_KEY, JSON.stringify(p)); } catch (_) {} };
const SILENT = 'data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQQAAAAAAA==';
let voAudio = null, voCtx = null, voToken = 0, voDone = null, voWarned = 0;
let voAI = { on: true, voices: [], left: {} };   // what the server says about voices and today's limits

function voUnlock() {   // call this from a tap: phones only let audio play later if it was started by a tap first
  try { if (!voAudio) { voAudio = new Audio(); voAudio.setAttribute('playsinline', ''); } voAudio.src = SILENT; const p = voAudio.play(); if (p && p.catch) p.catch(() => {}); } catch (_) {}
  try { const AC = window.AudioContext || window.webkitAudioContext; if (!voCtx && AC) voCtx = new AC(); if (voCtx && voCtx.resume) voCtx.resume(); } catch (_) {}
}

function voStop() {
  voToken++;
  try { if (voAudio) voAudio.pause(); } catch (_) {}
  try { if (window.speechSynthesis) { speechSynthesis.resume(); speechSynthesis.cancel(); } } catch (_) {}
  if (voDone) { const d = voDone; voDone = null; d(); }
}

const voClean = (t) => String(t).replace(/```[\s\S]*?```/g, ' the code is on your screen. ').replace(/https?:\/\/\S+/g, ' ').replace(/<\/?([A-Za-z][\w-]*)[^<>]{0,200}>/g, ' $1 tag ').replace(/[`*_#>~|]/g, '').replace(/\s+/g, ' ').trim().slice(0, 1100);

function voPlay(url, rate) {
  return new Promise((resolve) => {
    if (!voAudio) voAudio = new Audio();
    const a = voAudio; voDone = resolve; a.onended = a.onerror = () => resolve();
    a.src = url; a.playbackRate = rate || 1;
    const pr = a.play(); if (pr && pr.catch) pr.catch(() => resolve());
  });
}

function voDevice(text, name, rate) {   // the free voice already on the phone or computer
  return new Promise((resolve) => {
    if (!canSpeak()) return resolve();
    voDone = resolve;
    const voice = (speechSynthesis.getVoices() || []).find((v) => v.name === name) || pickVoice(), parts = sayChunks(text);
    speechSynthesis.resume();
    parts.forEach((t, i) => {
      const u = new SpeechSynthesisUtterance(t); u.lang = voice ? voice.lang : 'en-GB'; u.rate = (rate || 1) * 0.95; if (voice) u.voice = voice;
      u.onend = i === parts.length - 1 ? () => resolve() : null; u.onerror = () => resolve(); speechSynthesis.speak(u);
    });
  });
}

async function voSpeak(text) {   // resolves when Air Omega has finished speaking (or was stopped)
  voStop(); const my = voToken, p = voPrefs(), [kind, name] = String(p.voice).split(/:(.*)/s), clean = voClean(text);
  if (clean.length < 2) return;
  if (kind === 'ai' && voAI.on !== false) {
    try {
      const res = await fetch('/api/voice/speak', { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text, voice: name }) });
      if (my !== voToken) return;
      if (res.ok) {
        const url = URL.createObjectURL(await res.blob()); if (my !== voToken) { URL.revokeObjectURL(url); return; }
        await voPlay(url, p.rate); URL.revokeObjectURL(url); return;
      }
      const d = await res.json().catch(() => ({}));
      if (Date.now() - voWarned > 60000) { voWarned = Date.now(); toast((d.error || "Air Omega's voice is resting.") + ' Using your device voice instead.', 'bad'); }
    } catch (_) {}
  }
  if (my === voToken) await voDevice(clean, name, p.rate);
}

/* ───────────── Listening: record, notice when you stop talking, send to be turned into words ───────────── */
const voCanRecord = () => !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder);
const voMime = () => ['audio/webm;codecs=opus', 'audio/webm', 'audio/mp4', 'audio/ogg;codecs=opus'].find((m) => MediaRecorder.isTypeSupported && MediaRecorder.isTypeSupported(m)) || '';

function vadStep(st, rms, dtMs) {   // decides, every 100 ms, whether you have finished speaking
  if (rms > 0.02) { st.talked += dtMs; st.silent = 0; } else { st.silent += dtMs; if (st.talked < 250) st.idle += dtMs; }
  if (st.talked >= 250 && st.silent >= 1400) return 'stop';   // you spoke, then went quiet: send it
  if (st.talked < 250 && st.idle >= 9000) return 'abort';     // nothing but silence for 9 seconds: give up
  return 'go';
}

async function voStart({ vad = false, onLevel } = {}) {
  voUnlock();   // runs inside the tap, before the permission question
  const stream = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: true, noiseSuppression: true } });
  const mime = voMime(), mr = new MediaRecorder(stream, mime ? { mimeType: mime } : undefined), chunks = [];
  let resolveDone, cancelled = false, timer = null, maxT = null, source = null;
  const done = new Promise((r) => { resolveDone = r; });
  mr.ondataavailable = (e) => { if (e.data && e.data.size) chunks.push(e.data); };
  mr.onstop = () => {
    clearInterval(timer); clearTimeout(maxT); try { if (source) source.disconnect(); } catch (_) {}
    stream.getTracks().forEach((t) => t.stop());
    resolveDone(cancelled || !chunks.length ? null : new Blob(chunks, { type: mr.mimeType || mime || 'audio/webm' }));
  };
  const ctl = { done, stop() { if (mr.state !== 'inactive') mr.stop(); }, cancel() { cancelled = true; ctl.stop(); } };
  mr.start();
  maxT = setTimeout(() => ctl.stop(), 30000);   // never record for more than 30 seconds
  if ((vad || onLevel) && voCtx) {
    try {
      const an = voCtx.createAnalyser(); an.fftSize = 1024; source = voCtx.createMediaStreamSource(stream); source.connect(an);
      const buf = new Uint8Array(an.fftSize), st = { talked: 0, silent: 0, idle: 0 };
      timer = setInterval(() => {
        an.getByteTimeDomainData(buf);
        let sum = 0; for (let i = 0; i < buf.length; i++) { const v = (buf[i] - 128) / 128; sum += v * v; }
        const rms = Math.sqrt(sum / buf.length); if (onLevel) onLevel(rms);
        if (vad) { const d = vadStep(st, rms, 100); if (d === 'stop') ctl.stop(); else if (d === 'abort') ctl.cancel(); }
      }, 100);
    } catch (_) {}
  }
  return ctl;
}

async function voTranscribe(blob) {
  const t = (blob.type || '').split(';')[0], ext = { 'audio/webm': 'webm', 'audio/ogg': 'ogg', 'audio/mp4': 'mp4' }[t] || 'webm', fd = new FormData();
  fd.append('audio', blob, 'speech.' + ext);
  const res = await fetch('/api/voice/transcribe', { method: 'POST', credentials: 'same-origin', headers: { 'X-Requested-With': 'oats' }, body: fd });
  const d = await res.json().catch(() => ({}));
  if (!res.ok) { const e = new Error(d.error || 'Could not understand that recording.'); e.status = res.status; throw e; }
  return d.text;
}

/* ───────────── Voice settings (shared by every chat) ───────────── */
function voiceSettingsHTML(ai) {
  const p = voPrefs(), dev = canSpeak() ? (speechSynthesis.getVoices() || []).filter((v) => /^en/i.test(v.lang)) : [];
  const opt = (val, label) => `<option value="${esc(val)}" ${p.voice === val ? 'selected' : ''}>${esc(label)}</option>`;
  return `<div class="vopts">
    <label class="vchk"><input type="checkbox" class="v-speak" ${p.speak ? 'checked' : ''}> Speak replies</label>
    <select class="v-voice" aria-label="Air Omega's voice">
      ${ai && ai.on !== false ? `<optgroup label="Air Omega voices">${(ai.voices || []).map((v) => opt('ai:' + v.id, `${v.id[0].toUpperCase()}${v.id.slice(1)}: ${v.label}`)).join('')}</optgroup>` : ''}
      ${dev.length ? `<optgroup label="Free voices on this device">${dev.map((v) => opt('dev:' + v.name, v.name)).join('')}</optgroup>` : ''}
    </select>
    <select class="v-rate" aria-label="Speaking speed">${[[0.85, 'Slower'], [1, 'Normal speed'], [1.15, 'Faster']].map(([v, t]) => `<option value="${v}" ${p.rate === v ? 'selected' : ''}>${t}</option>`).join('')}</select>
    <button class="pill v-test">▶ Test voice</button></div>`;
}

/* ───────────── The chat box: type or talk, hear the answer ───────────── */
function pgFmt(t) {
  return String(t).split('```').map((part, i) => {
    if (i % 2) { const nl = part.indexOf('\n'), body = nl >= 0 && /^[\w+#-]{0,12}$/.test(part.slice(0, nl).trim()) ? part.slice(nl + 1) : part; return `<pre class="pgcode"><code>${esc(body.replace(/\n$/, ''))}</code></pre>`; }
    return esc(part).replace(/`([^`\n]+)`/g, '<code>$1</code>').replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/\n/g, '<br>');
  }).join('');
}

async function pgChat(el, cfg) {
  const ch = { messages: [], left: 0, limit: 0, busy: false, rec: null, hearing: false, speaking: false, conv: false, err: '', draft: '', ai: null, intro: '' };
  let gone = false; pgOnCleanup(() => { gone = true; if (ch.rec) ch.rec.cancel(); });
  el.innerHTML = '<p class="meta" style="padding:14px 0">Loading…</p>';
  try { const d = await api(cfg.url); ch.messages = d.talk.messages; ch.left = d.talk.left; ch.limit = d.talk.limit; ch.intro = d.talk.intro; ch.ai = d.ai; voAI = d.ai; }
  catch (x) { el.innerHTML = `<p class="err">${esc(x.message)}</p>`; return null; }
  if (gone) return null;
  if (!ch.ai.unlocked || !ch.ai.on) { el.innerHTML = `<p class="meta">${!ch.ai.unlocked ? 'Unlock a track to talk with Air Omega.' : 'Air Omega is not switched on yet.'}</p>`; return null; }

  el.innerHTML = `<div class="pgchat ${cfg.compact ? 'compact' : ''}"><p class="meta c-left"></p><div class="mchat c-msgs" aria-live="polite"></div><p class="c-status meta"></p><p class="err c-err"></p>
    <div class="m-row"><button class="mic c-mic" aria-label="Talk to Air Omega">🎤</button><textarea class="c-q" rows="2" maxlength="600" aria-label="Your message" placeholder="${esc(cfg.placeholder || 'Type a message, or tap the microphone and talk')}"></textarea><button class="btn c-send">SEND</button></div>
    ${voiceSettingsHTML(ch.ai)}<div class="vopts"><label class="vchk"><input type="checkbox" class="c-conv"> Conversation mode (hands-free)</label><button class="pill c-new">New chat</button></div></div>`;
  const $$ = (s) => el.querySelector(s), msgs = $$('.c-msgs'), q = $$('.c-q'), mic = $$('.c-mic'), send = $$('.c-send');

  const paintMsgs = () => {
    msgs.innerHTML = bubble('assistant', ch.intro + (cfg.intro || ' Ask me anything, or tap the microphone and talk to me.')) + ch.messages.map((m, i) =>
      m.role === 'user' ? bubble('user', m.content).replace('class="bub me"', 'class="bub me"')
        : `<div class="bub bot"><small>Air Omega</small>${pgFmt(m.content)}<button class="say" data-say="${i}" aria-label="Hear this answer">🔊</button></div>`).join('')
      + (ch.busy ? '<div class="bub bot"><small>Air Omega</small><span class="dots"><i></i><i></i><i></i></span></div>' : '');
    msgs.scrollTop = msgs.scrollHeight;
    msgs.querySelectorAll('[data-say]').forEach((b) => (b.onclick = async () => { voUnlock(); ch.speaking = true; paintState(); await voSpeak(ch.messages[+b.dataset.say].content); ch.speaking = false; paintState(); }));
  };
  const paintState = () => {
    $$('.c-left').textContent = `${ch.left} of ${ch.limit} messages left today.`;
    $$('.c-err').textContent = ch.err;
    $$('.c-status').textContent = ch.rec ? (ch.conv ? 'Listening… just talk, I will answer when you stop.' : 'Listening… tap the microphone again when you are done.')
      : ch.hearing ? 'Working out what you said…' : ch.busy ? 'Air Omega is thinking…' : ch.speaking ? 'Air Omega is speaking. Tap the microphone to interrupt.' : '';
    mic.classList.toggle('on', !!ch.rec); mic.textContent = ch.rec ? '⏹' : '🎤';
    mic.hidden = !voCanRecord(); send.disabled = ch.busy || ch.left <= 0; q.disabled = ch.left <= 0;
    $$('.c-conv').checked = ch.conv;
  };

  async function sendMsg(text, viaVoice) {
    text = text.trim(); if (text.length < 2 || ch.busy) return;
    const speak = viaVoice || voPrefs().speak;
    ch.busy = true; ch.err = ''; ch.draft = ''; q.value = ''; ch.messages.push({ role: 'user', content: text }); paintMsgs(); paintState();
    try {
      const r = await post(cfg.url, { message: text, context: cfg.context ? cfg.context() : '', voice: !!speak });
      ch.messages.push({ role: 'assistant', content: r.reply }); ch.left = r.left; ch.busy = false; paintMsgs(); paintState();
      if (speak && !gone) { ch.speaking = true; paintState(); await voSpeak(r.reply); ch.speaking = false; paintState(); }
      if (ch.conv && !gone) listen(true);
    } catch (x) { ch.messages.pop(); ch.err = x.message; ch.busy = false; ch.conv = false; q.value = text; paintMsgs(); paintState(); }
  }

  async function listen(auto) {
    if (gone || ch.rec || ch.busy) return;
    if (!voCanRecord()) { ch.err = 'This browser cannot record your voice. You can still type.'; paintState(); return; }
    try { ch.rec = await voStart({ vad: auto || ch.conv }); } catch (_) { ch.err = 'Please allow the microphone so you can talk with Air Omega.'; ch.conv = false; ch.rec = null; paintState(); return; }
    ch.err = ''; paintState();
    const blob = await ch.rec.done; ch.rec = null; paintState();
    if (gone) return;
    if (!blob || blob.size < 1200) { if (auto) { ch.conv = false; paintState(); } return; }
    ch.hearing = true; paintState();
    try { const text = await voTranscribe(blob); ch.hearing = false; await sendMsg(text, true); }
    catch (x) { ch.hearing = false; ch.conv = false; ch.err = x.message; paintState(); }
  }

  mic.onclick = () => { voUnlock(); if (ch.rec) { ch.rec.stop(); return; } if (ch.speaking) { voStop(); ch.speaking = false; } listen(false); };
  send.onclick = () => { voUnlock(); sendMsg(q.value, false); };
  q.onkeydown = (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); voUnlock(); sendMsg(q.value, false); } };
  $$('.c-conv').onchange = (e) => { ch.conv = e.target.checked; if (ch.conv) { voUnlock(); const p = voPrefs(); p.speak = true; voSave(p); $$('.v-speak').checked = true; listen(true); } else if (ch.rec) ch.rec.cancel(); paintState(); };
  $$('.c-new').onclick = async () => { try { await post(cfg.url + '/clear', {}); ch.messages = []; voStop(); ch.speaking = false; paintMsgs(); paintState(); } catch (x) { ch.err = x.message; paintState(); } };
  $$('.v-speak').onchange = (e) => { const p = voPrefs(); p.speak = e.target.checked; voSave(p); };
  $$('.v-voice').onchange = (e) => { const p = voPrefs(); p.voice = e.target.value; voSave(p); };
  $$('.v-rate').onchange = (e) => { const p = voPrefs(); p.rate = +e.target.value; voSave(p); };
  $$('.v-test').onclick = async () => { voUnlock(); await voSpeak(ch.intro); };
  if (canSpeak()) speechSynthesis.onvoiceschanged = () => { const sel = $$('.v-voice'); if (sel && !gone) { const keep = voPrefs().voice; const tmp = document.createElement('div'); tmp.innerHTML = voiceSettingsHTML(ch.ai); sel.innerHTML = tmp.querySelector('.v-voice').innerHTML; sel.value = keep; } };
  paintMsgs(); paintState();
  return { say: sendMsg };
}

/* ───────────── Talk to Air Omega (a screen of its own) ───────────── */
function openTalk() { S.openId = null; S.view = 'talk'; $('#sheet').hidden = false; document.body.classList.add('lock'); renderSheet(); }

function viewTalk() {
  sheet(`<div class="glass intro"><h2>Talk to Air Omega</h2><p>Ask about tech, coding, your courses or your homework. Type, or tap the microphone and just talk. Air Omega can talk back in the voice you choose.</p></div>
    <div class="glass panel"><div id="talkbox"></div></div>`, closeSheet, '← Back');
  pgChat($('#talkbox'), { url: '/api/talk' });
}

/* ───────────── Playgrounds: one for every course ───────────── */
function openPlayground() { goView('play'); }

function viewPlay(c) {
  const pg = PG[c.id];
  if (!pg) { sheet('<p class="empty">This course does not have a playground yet.</p>', () => goView('course'), '← Back to lessons'); return; }
  sheet(`<div class="glass intro"><h2>${pg.icon} ${esc(pg.name)}</h2><p>${esc(pg.blurb)}</p></div>
    <div class="pg" id="pgbox"></div>
    <div class="glass panel"><h3>Ask Air Omega about your work</h3><p class="meta">Air Omega can see what you have built here, so it can explain, fix and improve it with you.</p><div id="pgchat"></div></div>`, () => goView('course'), '← Back to lessons');
  const run = pg.mount($('#pgbox'), c);
  pgChat($('#pgchat'), { url: '/api/talk', context: () => (run && run.context ? run.context() : ''), compact: true, placeholder: 'Ask about what you just built…', intro: ' Ask me about anything you are building in this playground.' });
}

/* small helpers the playgrounds share */
const pgRange = (id, label, min, max, step, val, unit = '') => `<label class="rng" for="${id}"><span>${esc(label)}</span><input type="range" id="${id}" min="${min}" max="${max}" step="${step}" value="${val}"><output id="${id}-o">${val}${unit}</output></label>`;
const pgCopy = async (text, msg = 'Copied.') => { try { await navigator.clipboard.writeText(text); toast(msg); } catch (_) { toast('Could not copy. Select the text and copy it yourself.', 'bad'); } };
const pgDownload = (name, text, type = 'text/html') => { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([text], { type })); a.download = name; document.body.append(a); a.click(); a.remove(); };

/* ═══════════ 1. Prompt Engineering: Prompt Lab (real AI, scored by Air Omega) ═══════════ */
const PL_CHALLENGES = [
  { title: 'Free practice', goal: '', starter: '' },
  { title: 'A product description for a Lagos bakery', goal: 'exactly 3 bullet points, a friendly tone, under 60 words', starter: 'Write a product description for a bakery in Lagos.' },
  { title: 'Explain the cloud to a 10-year-old', goal: 'uses one market or football comparison, under 80 words, no jargon', starter: 'Explain what the cloud is.' },
  { title: 'A polite email asking a teacher for more time', goal: 'has a subject line, a greeting and exactly 3 sentences', starter: 'Write an email to my teacher.' },
  { title: 'Turn the AI into a quiz master', goal: 'asks exactly 3 web development questions and does not reveal the answers', starter: 'Quiz me.' },
];

PG['prompt-engineering'] = {
  icon: '✍️', name: 'Prompt Lab', blurb: 'Write a prompt, run it for real, and Air Omega scores it on clarity, context, format and limits. Beat your own best score.',
  mount(el) {
    const st = { runs: [], busy: false, last: null };
    el.innerHTML = `<div class="pgcols"><div class="glass panel">
        <label for="pl-ch">Challenge</label><select id="pl-ch">${PL_CHALLENGES.map((c, i) => `<option value="${i}">${esc(c.title)}</option>`).join('')}</select>
        <p class="meta" id="pl-goal"></p>
        <label for="pl-p">Your prompt</label><textarea id="pl-p" rows="7" maxlength="1200" placeholder="Try: who the AI is + what to do + who it is for + how the answer should look + limits"></textarea>
        <p class="meta"><span id="pl-c">0</span> of 1200 characters</p><p class="err" id="pl-e"></p>
        <button class="btn" id="pl-run">RUN MY PROMPT</button>
        <details class="pgtip"><summary>A formula that works</summary><p><b>Role</b> (you are a…), <b>Task</b> (write…), <b>Context</b> (for whom and why), <b>Format</b> (3 bullets, a table…), <b>Limits</b> (under 60 words, friendly tone, no jargon).</p></details>
      </div><div class="glass panel" id="pl-out"><p class="meta">Run your prompt to see the AI's answer and Air Omega's score.</p></div></div>
      <div class="glass panel" id="pl-hist" hidden></div>`;
    const $$ = (s) => el.querySelector(s), p = $$('#pl-p');
    const goal = () => PL_CHALLENGES[+$$('#pl-ch').value].goal;
    const bar = (n, v) => `<div class="plbar"><span>${n}</span><i><b style="width:${v * 20}%"></b></i><em>${v}/5</em></div>`;
    $$('#pl-ch').onchange = () => { const c = PL_CHALLENGES[+$$('#pl-ch').value]; $$('#pl-goal').innerHTML = c.goal ? `<b>Goal:</b> ${esc(c.goal)}. Your prompt has to make the AI do this.` : ''; if (c.starter) p.value = c.starter; p.oninput(); };
    p.oninput = () => { $$('#pl-c').textContent = p.value.length; };
    const hist = () => { const h = $$('#pl-hist'); h.hidden = !st.runs.length; const best = Math.max(0, ...st.runs.map((r) => r.total));
      h.innerHTML = `<h3>Your runs</h3><p class="meta">Best score: <b>${best}/20</b>. Can you beat it?</p><ul class="plhist">${st.runs.map((r, i) => `<li><b>${r.total}/20</b> <span>${esc(r.prompt.slice(0, 70))}${r.prompt.length > 70 ? '…' : ''}</span></li>`).reverse().join('')}</ul>`; };
    $$('#pl-run').onclick = async () => {
      const prompt = p.value.trim(); $$('#pl-e').textContent = '';
      if (prompt.length < 5) { $$('#pl-e').textContent = 'Write a prompt first, at least 5 characters.'; return; }
      st.busy = true; const b = $$('#pl-run'); b.disabled = true; b.innerHTML = '<span class="spin"></span>';
      $$('#pl-out').innerHTML = '<p class="meta"><span class="spin"></span> Running your prompt, then Air Omega will score it. This takes a few seconds.</p>';
      try {
        const r = await post('/api/courses/prompt-engineering/playground/prompt', { prompt, goal: goal() });
        st.last = { prompt, output: r.output, review: r.review }; st.runs.push({ prompt, total: r.review.total });
        const v = r.review, sc = v.scores;
        $$('#pl-out').innerHTML = `<h3>The AI's answer</h3><div class="pgout">${pgFmt(r.output)}</div>
          <div class="plscore"><div class="scorebig"><b>${v.total}</b><span>/ 20</span></div><div>${bar('Clarity', sc.clarity)}${bar('Context', sc.context)}${bar('Format', sc.format)}${bar('Limits', sc.constraints)}</div></div>
          ${v.goalMet === true ? '<p class="plgoal ok">✅ Goal met. Nice work.</p>' : v.goalMet === false ? '<p class="plgoal no">🎯 Not quite the goal yet. Try again.</p>' : ''}
          ${v.tips.length ? `<h4>Air Omega's tips</h4><ul class="rub">${v.tips.map((t) => `<li>${esc(t)}</li>`).join('')}</ul>` : ''}
          ${v.rewrite ? `<h4>A stronger version</h4><div class="pgout">${esc(v.rewrite)}</div><button class="pill" id="pl-use">Use this version</button>` : ''}
          <p class="meta">${r.left} runs left today.</p>`;
        const use = $$('#pl-use'); if (use) use.onclick = () => { p.value = v.rewrite; p.oninput(); };
        hist();
      } catch (x) { $$('#pl-out').innerHTML = `<p class="err">${esc(x.message)}</p>`; }
      st.busy = false; b.disabled = false; b.textContent = 'RUN MY PROMPT';
    };
    return { context: () => `Challenge goal: ${goal() || 'none'}\nStudent prompt:\n${p.value}\n` + (st.last ? `\nLast AI output:\n${st.last.output}\nAir Omega's score: ${st.last.review.total}/20 (${JSON.stringify(st.last.review.scores)})` : '') };
  },
};

/* ═══════════ 2. Web Development: Code Studio (live HTML, CSS and JavaScript) ═══════════ */
const CS_TEMPLATES = {
  hello: { name: 'Hello page', html: '<h1>Hello, Lagos!</h1>\n<p>Change this text and watch the page update.</p>', css: 'body { font-family: sans-serif; text-align: center; padding: 2rem; }\nh1 { color: #0a8f9c; }', js: '' },
  counter: { name: 'Click counter', html: '<h1>Clicks: <span id="n">0</span></h1>\n<button id="b">Click me</button>', css: 'body { font-family: sans-serif; text-align: center; padding: 2rem; }\nbutton { font-size: 1.2rem; padding: .6rem 1.4rem; border-radius: 10px; border: 0; background: #0a8f9c; color: #fff; }', js: "let n = 0;\ndocument.getElementById('b').onclick = () => {\n  n++;\n  document.getElementById('n').textContent = n;\n  console.log('clicked', n);\n};" },
  card: { name: 'Profile card', html: '<div class="card">\n  <div class="avatar">A</div>\n  <h2>Ada Obi</h2>\n  <p>Learning to build apps in Lagos.</p>\n  <button>Follow</button>\n</div>', css: 'body { display: grid; place-items: center; min-height: 90vh; background: #eef6f8; font-family: sans-serif; }\n.card { background: #fff; padding: 2rem; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px #0002; }\n.avatar { width: 70px; height: 70px; margin: 0 auto 10px; border-radius: 50%; background: #0a8f9c; color: #fff; display: grid; place-items: center; font-size: 2rem; }\nbutton { padding: .5rem 1.2rem; border: 0; border-radius: 999px; background: #0a8f9c; color: #fff; }', js: '' },
  blank: { name: 'Blank', html: '', css: '', js: '' },
};
const CS_IDEAS = ['Make the heading red', 'Add a second button', 'Change the font', 'Make the button grow when you hover', 'Show an alert when the button is clicked', 'Add an image card'];

function csDoc(html, css, js, bridge) {
  const br = bridge ? `<script>addEventListener('error',function(e){parent.postMessage({oats:'error',m:e.message+' (line '+e.lineno+')'},'*')});['log','warn','error'].forEach(function(k){var o=console[k];console[k]=function(){parent.postMessage({oats:k,m:[].map.call(arguments,function(a){try{return typeof a==='object'?JSON.stringify(a):String(a)}catch(e){return String(a)}}).join(' ')},'*');o.apply(console,arguments)}});<\/script>` : '';
  return `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>My page</title><style>${css}</style></head><body>${html}${br}<script>${String(js).replace(/<\/script/gi, '<\\/script')}<\/script></body></html>`;
}

PG['web-development'] = {
  icon: '🌐', name: 'Code Studio', blurb: 'Write HTML, CSS and JavaScript and see your page come alive as you type. Errors and console.log show up below.',
  mount(el) {
    const T = CS_TEMPLATES, st = { html: T.hello.html, css: T.hello.css, js: T.hello.js, tab: 'html', log: [] };
    el.innerHTML = `<div class="glass panel"><div class="pills"><label class="inl">Start from <select id="cs-t">${Object.entries(T).map(([k, v]) => `<option value="${k}">${esc(v.name)}</option>`).join('')}</select></label>
        <button class="pill" id="cs-dl">⬇ Download page</button><button class="pill" id="cs-cp">Copy HTML</button></div>
        <p class="meta">Ideas to try: ${CS_IDEAS.map(esc).join(' · ')}</p></div>
      <div class="pgcols cs"><div class="glass panel"><div class="seg" id="cs-tabs">${['html', 'css', 'js'].map((t) => `<button data-t="${t}" aria-pressed="${t === 'html'}">${t === 'js' ? 'JavaScript' : t.toUpperCase()}</button>`).join('')}</div>
        ${['html', 'css', 'js'].map((t) => `<textarea class="code" id="cs-${t}" spellcheck="false" aria-label="${t} code" ${t === 'html' ? '' : 'hidden'}></textarea>`).join('')}</div>
        <div class="glass panel"><h3>Live preview</h3><iframe id="cs-f" class="csframe" title="Your page" sandbox="allow-scripts allow-modals"></iframe>
        <h4>Console</h4><div class="csconsole" id="cs-log"><span class="meta">console.log messages and errors appear here.</span></div></div></div>`;
    const $$ = (s) => el.querySelector(s), frame = $$('#cs-f');
    const fill = () => ['html', 'css', 'js'].forEach((t) => { $$('#cs-' + t).value = st[t]; });
    let timer = null;
    const run = () => { st.log = []; $$('#cs-log').innerHTML = '<span class="meta">Running…</span>'; frame.srcdoc = csDoc(st.html, st.css, st.js, true); };
    const later = () => { clearTimeout(timer); timer = setTimeout(run, 400); };
    ['html', 'css', 'js'].forEach((t) => { $$('#cs-' + t).oninput = (e) => { st[t] = e.target.value; later(); }; });
    $$('#cs-tabs').querySelectorAll('button').forEach((b) => (b.onclick = () => { st.tab = b.dataset.t; $$('#cs-tabs').querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', x === b)); ['html', 'css', 'js'].forEach((t) => { $$('#cs-' + t).hidden = t !== st.tab; }); }));
    $$('#cs-t').onchange = (e) => { const t = T[e.target.value]; st.html = t.html; st.css = t.css; st.js = t.js; fill(); run(); };
    $$('#cs-dl').onclick = () => pgDownload('my-page.html', csDoc(st.html, st.css, st.js, false));
    $$('#cs-cp').onclick = () => pgCopy(csDoc(st.html, st.css, st.js, false), 'Your page code is copied.');
    const onMsg = (e) => {
      if (e.source !== frame.contentWindow || !e.data || !e.data.oats) return;
      st.log.push({ k: e.data.oats, m: String(e.data.m).slice(0, 300) });
      $$('#cs-log').innerHTML = st.log.slice(-30).map((l) => `<div class="${l.k}">${l.k === 'log' ? '›' : l.k === 'warn' ? '⚠' : '✖'} ${esc(l.m)}</div>`).join('');
    };
    window.addEventListener('message', onMsg); pgOnCleanup(() => { window.removeEventListener('message', onMsg); clearTimeout(timer); });
    fill(); run();
    return { context: () => `HTML:\n${st.html}\n\nCSS:\n${st.css}\n\nJavaScript:\n${st.js}\n\nConsole:\n${st.log.map((l) => l.k + ': ' + l.m).join('\n') || '(empty)'}` };
  },
};

/* ═══════════ 3. Animation: Keyframe Studio ═══════════ */
const pgEase = {
  linear: (t) => t, easeIn: (t) => t * t * t, easeOut: (t) => 1 - Math.pow(1 - t, 3),
  easeInOut: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  back: (t) => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); },
  bounce: (t) => { const n = 7.5625, d = 2.75; if (t < 1 / d) return n * t * t; if (t < 2 / d) return n * (t -= 1.5 / d) * t + 0.75; if (t < 2.5 / d) return n * (t -= 2.25 / d) * t + 0.9375; return n * (t -= 2.625 / d) * t + 0.984375; },
  elastic: (t) => (t === 0 ? 0 : t === 1 ? 1 : Math.pow(2, -10 * t) * Math.sin(((t * 10 - 0.75) * (2 * Math.PI)) / 3) + 1),
};
const AN_EASINGS = [['linear', 'Linear (robotic)'], ['easeIn', 'Ease in (starts slow)'], ['easeOut', 'Ease out (ends slow)'], ['easeInOut', 'Ease in and out'], ['back', 'Back (overshoots)'], ['bounce', 'Bounce'], ['elastic', 'Elastic (springy)']];

function pgAnimAt(kfs, easing, time) {   // kfs: 4+ keyframes sorted by t (0..100); time 0..1 -> position, scale and rotation
  const T = time * 100; let i = 0; while (i < kfs.length - 2 && T > kfs[i + 1].t) i++;
  const a = kfs[i], b = kfs[i + 1], u = b.t === a.t ? 1 : Math.min(1, Math.max(0, (T - a.t) / (b.t - a.t))), e = (pgEase[easing] || pgEase.linear)(u);
  const L = (p, q) => p + (q - p) * e; return { x: L(a.x, b.x), y: L(a.y, b.y), s: L(a.s, b.s), r: L(a.r, b.r) };
}

function anCss(kfs, easing, dur) {
  const kw = { linear: 'linear', easeIn: 'ease-in', easeOut: 'ease-out', easeInOut: 'ease-in-out' }[easing];
  const fn = kw || `linear(${Array.from({ length: 25 }, (_, i) => +pgEase[easing](i / 24).toFixed(3)).join(', ')})`;
  return `@keyframes myMove {\n${kfs.map((k) => `  ${k.t}% { transform: translate(${Math.round(k.x)}px, ${Math.round(k.y)}px) rotate(${Math.round(k.r)}deg) scale(${(+k.s).toFixed(2)}); }`).join('\n')}\n}\n\n.ball {\n  animation: myMove ${dur}s ${fn} infinite;\n}`;
}

const AN_PRESETS = {
  bounce: { name: 'Bouncing ball', easing: 'bounce', dur: 2, kfs: [{ t: 0, x: -110, y: -70, s: 1, r: 0 }, { t: 35, x: -30, y: 70, s: 1, r: 120 }, { t: 65, x: 40, y: -20, s: 1, r: 240 }, { t: 100, x: 110, y: 70, s: 1, r: 360 }] },
  pendulum: { name: 'Pendulum swing', easing: 'easeInOut', dur: 2.4, kfs: [{ t: 0, x: -100, y: 10, s: 1, r: -40 }, { t: 40, x: 0, y: 50, s: 1, r: 0 }, { t: 60, x: 60, y: 30, s: 1, r: 20 }, { t: 100, x: 100, y: 10, s: 1, r: 40 }] },
  pop: { name: 'Pop in', easing: 'back', dur: 1.2, kfs: [{ t: 0, x: 0, y: 0, s: 0.3, r: -30 }, { t: 30, x: 0, y: 0, s: 1.4, r: 10 }, { t: 60, x: 0, y: 0, s: 0.9, r: -5 }, { t: 100, x: 0, y: 0, s: 1, r: 0 }] },
  jump: { name: 'Anticipation jump', easing: 'easeOut', dur: 1.8, kfs: [{ t: 0, x: -80, y: 60, s: 1, r: 0 }, { t: 25, x: -80, y: 80, s: 1.25, r: 0 }, { t: 55, x: 0, y: -70, s: 0.85, r: 180 }, { t: 100, x: 80, y: 60, s: 1, r: 360 }] },
};

PG['animation'] = {
  icon: '🎬', name: 'Keyframe Studio', blurb: 'Pose a shape at four keyframes, pick how it moves between them, and watch the motion. This is how every animation tool works.',
  mount(el) {
    const st = { kfs: JSON.parse(JSON.stringify(AN_PRESETS.bounce.kfs)), easing: 'bounce', dur: 2, sel: 0, playing: true, loop: true, onion: true, squash: true, time: 0 };
    el.innerHTML = `<div class="pgcols"><div class="glass panel"><div class="anstage" id="an-st"><div id="an-ghosts"></div><div class="anball" id="an-ball"></div></div>
        <div class="anline" id="an-line"></div><input type="range" id="an-scrub" min="0" max="1000" value="0" aria-label="Scrub through the animation">
        <div class="pills"><button class="pill hot" id="an-play">⏸ Pause</button><label class="vchk"><input type="checkbox" id="an-loop" checked> Loop</label><label class="vchk"><input type="checkbox" id="an-onion" checked> Onion skin</label><label class="vchk"><input type="checkbox" id="an-sq" checked> Squash and stretch</label></div>
        <svg viewBox="0 0 100 60" class="ancurve" id="an-curve" aria-label="The easing curve"></svg></div>
      <div class="glass panel"><label>Preset <select id="an-pre">${Object.entries(AN_PRESETS).map(([k, v]) => `<option value="${k}">${esc(v.name)}</option>`).join('')}</select></label>
        <div class="seg" id="an-ktabs">${[0, 1, 2, 3].map((i) => `<button data-k="${i}" aria-pressed="${i === 0}">Keyframe ${i + 1}</button>`).join('')}</div>
        <div id="an-sl"></div>
        <label for="an-ease">How it moves between keyframes</label><select id="an-ease">${AN_EASINGS.map(([k, t]) => `<option value="${k}" ${k === 'bounce' ? 'selected' : ''}>${t}</option>`).join('')}</select>
        ${pgRange('an-dur', 'Duration', 0.5, 4, 0.1, 2, 's')}
        <button class="pill" id="an-css">Copy as CSS</button></div></div>`;
    const $$ = (s) => el.querySelector(s), ball = $$('#an-ball'), ghosts = $$('#an-ghosts'); let raf = 0, t0 = null;
    const pose = (p) => {
      const sp = (() => { const a = pgAnimAt(st.kfs, st.easing, Math.max(0, (st.time * 100 - 1.5) / 100)), b = pgAnimAt(st.kfs, st.easing, Math.min(1, (st.time * 100 + 1.5) / 100)); return Math.hypot(b.x - a.x, b.y - a.y); })();
      const k = st.squash ? 1 + Math.min(0.6, sp * 0.03) : 1, sx = p.s / k, sy = p.s * k;
      return `translate(${p.x}px, ${p.y}px) rotate(${p.r}deg) scale(${sx.toFixed(3)}, ${sy.toFixed(3)})`;
    };
    const draw = () => {
      const p = pgAnimAt(st.kfs, st.easing, st.time); ball.style.transform = pose(p);
      ghosts.innerHTML = st.onion ? Array.from({ length: 12 }, (_, i) => { const g = pgAnimAt(st.kfs, st.easing, i / 11); return `<div class="anghost" style="transform:translate(${g.x}px,${g.y}px) rotate(${g.r}deg) scale(${g.s})"></div>`; }).join('') : '';
      $$('#an-line').innerHTML = st.kfs.map((k, i) => `<i class="${i === st.sel ? 'on' : ''}" style="left:${k.t}%" title="Keyframe ${i + 1}">${i + 1}</i>`).join('');
      $$('#an-scrub').value = Math.round(st.time * 1000);
      const f = pgEase[st.easing]; $$('#an-curve').innerHTML = `<path d="M${Array.from({ length: 41 }, (_, i) => `${(i / 40) * 100},${55 - f(i / 40) * 50}`).join(' L')}" fill="none" stroke="currentColor" stroke-width="2"/>`;
    };
    const sliders = () => {
      const k = st.kfs[st.sel], i = st.sel, mid = i === 1 || i === 2;
      $$('#an-sl').innerHTML = (mid ? pgRange('an-t', 'When (% of the animation)', i === 1 ? 5 : st.kfs[1].t, i === 1 ? st.kfs[2].t : 95, 1, k.t, '%') : `<p class="meta">Keyframe ${i + 1} is at ${k.t}%.</p>`)
        + pgRange('an-x', 'Left / right', -120, 120, 1, k.x) + pgRange('an-y', 'Up / down', -80, 90, 1, k.y) + pgRange('an-s', 'Size', 0.3, 2.2, 0.05, k.s) + pgRange('an-r', 'Rotation', -360, 360, 5, k.r, '°');
      [['t', 'an-t'], ['x', 'an-x'], ['y', 'an-y'], ['s', 'an-s'], ['r', 'an-r']].forEach(([key, id]) => { const inp = $$('#' + id); if (!inp) return; inp.oninput = () => { k[key] = +inp.value; $$('#' + id + '-o').textContent = inp.value + (key === 'r' ? '°' : key === 't' ? '%' : ''); if (key === 't') { st.kfs[1].t = Math.min(st.kfs[1].t, st.kfs[2].t); } draw(); }; });
    };
    const loop = (now) => { if (st.playing) { if (t0 === null) t0 = now - st.time * st.dur * 1000; let u = (now - t0) / (st.dur * 1000); if (u >= 1) { if (st.loop) { u %= 1; t0 = now - u * st.dur * 1000; } else { u = 1; st.playing = false; $$('#an-play').textContent = '▶ Play'; } } st.time = u; draw(); } raf = requestAnimationFrame(loop); };
    raf = requestAnimationFrame(loop); pgOnCleanup(() => cancelAnimationFrame(raf));
    $$('#an-play').onclick = () => { st.playing = !st.playing; if (st.playing && st.time >= 1) st.time = 0; t0 = null; $$('#an-play').textContent = st.playing ? '⏸ Pause' : '▶ Play'; };
    $$('#an-scrub').oninput = (e) => { st.playing = false; $$('#an-play').textContent = '▶ Play'; st.time = +e.target.value / 1000; draw(); };
    $$('#an-loop').onchange = (e) => { st.loop = e.target.checked; }; $$('#an-onion').onchange = (e) => { st.onion = e.target.checked; draw(); }; $$('#an-sq').onchange = (e) => { st.squash = e.target.checked; draw(); };
    $$('#an-ease').onchange = (e) => { st.easing = e.target.value; draw(); };
    $$('#an-dur').oninput = (e) => { st.dur = +e.target.value; $$('#an-dur-o').textContent = e.target.value + 's'; t0 = null; };
    $$('#an-ktabs').querySelectorAll('button').forEach((b) => (b.onclick = () => { st.sel = +b.dataset.k; $$('#an-ktabs').querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', x === b)); sliders(); draw(); }));
    $$('#an-pre').onchange = (e) => { const p = AN_PRESETS[e.target.value]; st.kfs = JSON.parse(JSON.stringify(p.kfs)); st.easing = p.easing; st.dur = p.dur; $$('#an-ease').value = p.easing; $$('#an-dur').value = p.dur; $$('#an-dur-o').textContent = p.dur + 's'; t0 = null; sliders(); draw(); };
    $$('#an-css').onclick = () => pgCopy(anCss(st.kfs, st.easing, st.dur), 'The CSS animation is copied. Paste it into Code Studio.');
    sliders(); draw();
    return { context: () => `Keyframes (t%, x, y, scale, rotation): ${JSON.stringify(st.kfs)}\nEasing: ${st.easing}\nDuration: ${st.dur}s\nSquash and stretch: ${st.squash}\n\nCSS version:\n${anCss(st.kfs, st.easing, st.dur)}` };
  },
};

/* ═══════════ 4. Cloud Computing: the Traffic Surge Simulator ═══════════ */
const CLOUD_SIZES = { small: { name: 'Small server', cap: 100, price: 20 }, medium: { name: 'Medium server', cap: 250, price: 45 }, large: { name: 'Large server', cap: 600, price: 100 } };
const CLOUD_SCENES = { normal: { name: 'A normal day', peak: 80, shape: 'gentle' }, viral: { name: 'Your app goes viral', peak: 2400, shape: 'spike' }, sale: { name: 'Black Friday sale', peak: 1500, shape: 'plateau' }, exam: { name: 'Exam results day', peak: 4000, shape: 'spike' } };

function cloudProfile(shape, i, n = 60) {   // how busy minute i is, from 0 to 1 of the peak
  const x = i / (n - 1);
  if (shape === 'spike') return x < 0.25 ? 0.15 : x < 0.4 ? 0.15 + 0.85 * ((x - 0.25) / 0.15) : x < 0.55 ? 1 : x < 0.8 ? 1 - 0.7 * ((x - 0.55) / 0.25) : 0.3;
  if (shape === 'plateau') return x < 0.2 ? 0.2 : x < 0.35 ? 0.2 + 0.8 * ((x - 0.2) / 0.15) : x < 0.8 ? 1 : 0.4;
  return 0.5 + 0.5 * Math.sin(x * Math.PI);
}

function pgCloudSim(cfg) {
  const size = CLOUD_SIZES[cfg.size] || CLOUD_SIZES.small, N = 60, ticks = [];
  let servers = Math.max(1, cfg.servers | 0), pending = [];
  for (let i = 0; i < N; i++) {
    servers += pending.filter((p) => p.at <= i).reduce((s, p) => s + p.n, 0); pending = pending.filter((p) => p.at > i);
    const demand = cfg.peak * cloudProfile(cfg.shape, i, N), web = demand * (cfg.cdn ? 0.4 : 1);   // a CDN answers pictures and files, so only 40% reaches your servers
    const active = cfg.lb ? servers : 1, cap = active * size.cap, util = web / cap;                  // with no load balancer, every visitor hits one machine
    if (cfg.lb && cfg.auto) {   // autoscaling reacts to busy servers, and new servers take 3 minutes to start
      const coming = pending.reduce((s, p) => s + p.n, 0);
      if (util > 0.7 && servers + coming < cfg.max) { const need = Math.min(cfg.max - servers - coming, Math.max(1, Math.ceil(web / (size.cap * 0.6)) - servers - coming)); if (need > 0) pending.push({ at: i + 3, n: need }); }
      else if (util < 0.3 && servers > cfg.servers) servers -= 1;
    }
    const dbCap = Math.max(1, cfg.replicas) * 300, dbUtil = (web * 0.5) / dbCap, worst = Math.max(util, dbUtil);
    const lat = Math.round(Math.min(8000, 90 * (1 + Math.pow(Math.max(0, worst - 0.6), 2) * 12)));
    const fail = web <= 0 ? 0 : Math.max(0, 1 - Math.min(cap, dbCap * 2) / web);
    ticks.push({ demand, web, cap, servers: active, lat, fail, util, dbUtil });
  }
  const sumD = ticks.reduce((s, t) => s + t.demand, 0) || 1, avgFail = ticks.reduce((s, t) => s + t.fail * t.demand, 0) / sumD, maxLat = Math.max(...ticks.map((t) => t.lat));
  const avgServers = ticks.reduce((s, t) => s + (cfg.lb ? t.servers : Math.max(1, cfg.servers | 0)), 0) / N;
  const cost = Math.round(avgServers * size.price + (cfg.lb ? 18 : 0) + (cfg.cdn ? 10 : 0) + 40 + (Math.max(1, cfg.replicas) - 1) * 30);
  const worstTick = ticks.reduce((w, t) => (Math.max(t.util, t.dbUtil) > Math.max(w.util, w.dbUtil) ? t : w), ticks[0]);
  const verdict = avgFail < 0.01 && maxLat < 700 ? 'ok' : avgFail < 0.08 ? 'slow' : 'down';
  const why = verdict === 'ok' ? 'Your setup handled the traffic. Now try to do it for less money.'
    : !cfg.lb && cfg.servers > 1 ? `You are paying for ${cfg.servers} servers, but without a load balancer only one of them ever gets visitors. Turn on the load balancer.`
    : worstTick.dbUtil > worstTick.util ? 'Your database was the bottleneck. Add read replicas, or turn on the CDN so fewer requests reach it.'
    : 'Your servers could not keep up at the busiest minutes. Add servers, use bigger ones, or turn on autoscaling.';
  return { ticks, avgFail, maxLat, cost, verdict, why, availability: Math.round((1 - avgFail) * 1000) / 10 };
}

PG['cloud-computing'] = {
  icon: '☁️', name: 'Traffic Surge Simulator', blurb: 'Your app is about to get a flood of visitors. Choose servers, a load balancer, a CDN and a database setup, then see whether your site survives and what it costs.',
  mount(el) {
    const cfg = { scene: 'viral', size: 'small', servers: 2, lb: false, auto: false, max: 10, cdn: false, replicas: 1, peak: 2400, shape: 'spike' };
    el.innerHTML = `<div class="glass panel"><div class="pgcols"><div>
        <label for="cl-sc">Scenario</label><select id="cl-sc">${Object.entries(CLOUD_SCENES).map(([k, v]) => `<option value="${k}" ${k === 'viral' ? 'selected' : ''}>${esc(v.name)}</option>`).join('')}</select>
        <label for="cl-sz">Server size</label><select id="cl-sz">${Object.entries(CLOUD_SIZES).map(([k, v]) => `<option value="${k}">${esc(v.name)}: handles ${v.cap} visits a second, $${v.price}/month</option>`).join('')}</select>
        ${pgRange('cl-n', 'Servers', 1, 20, 1, 2)}${pgRange('cl-r', 'Database read replicas', 1, 4, 1, 1)}</div><div>
        <label class="vchk"><input type="checkbox" id="cl-lb"> Load balancer (shares visitors between servers, $18)</label>
        <label class="vchk"><input type="checkbox" id="cl-au"> Autoscaling (adds servers when busy, takes 3 minutes to start)</label>
        ${pgRange('cl-m', 'Autoscaling maximum', 2, 30, 1, 10)}
        <label class="vchk"><input type="checkbox" id="cl-cdn"> CDN (answers pictures and files for you, $10)</label></div></div></div>
      <div class="glass panel" id="cl-out"></div>`;
    const $$ = (s) => el.querySelector(s);
    const chart = (title, vals, max, cls, line2) => { const W = 600, H = 120, x = (i) => (i / 59) * W, y = (v) => H - Math.min(1, v / max) * (H - 6) - 2;
      const pts = (a) => a.map((v, i) => `${x(i).toFixed(1)},${y(v).toFixed(1)}`).join(' ');
      return `<figure class="clchart"><figcaption>${title}</figcaption><svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none"><polyline class="${cls}" points="${pts(vals)}"/>${line2 ? `<polyline class="${line2.cls}" points="${pts(line2.vals)}"/>` : ''}</svg></figure>`; };
    const redraw = () => {
      const sc = CLOUD_SCENES[cfg.scene]; cfg.peak = sc.peak; cfg.shape = sc.shape;
      const r = pgCloudSim(cfg), t = r.ticks, maxRps = Math.max(1, ...t.map((x) => Math.max(x.web, x.cap)));
      const badge = { ok: ['✅ Your site survived', 'ok'], slow: ['🐢 Your site survived, but slowly', 'slow'], down: ['💥 Your site went down', 'down'] }[r.verdict];
      $$('#cl-out').innerHTML = `<div class="clverdict ${badge[1]}"><b>${badge[0]}</b><span>${esc(r.why)}</span></div>
        <div class="cltiles"><div><b>${r.availability}%</b><span>of visits worked</span></div><div><b>${r.maxLat >= 8000 ? 'timeout' : r.maxLat + ' ms'}</b><span>slowest response</span></div><div><b>$${r.cost}</b><span>per month, estimated</span></div></div>
        ${chart('Visitors per second (grey) against what your servers can handle (blue)', t.map((x) => x.web), maxRps, 'clw', { cls: 'clc', vals: t.map((x) => x.cap) })}
        ${chart('How long each visit takes, in milliseconds', t.map((x) => x.lat), 2500, 'cll')}
        <p class="meta">${cfg.lb ? '' : 'Tip: with no load balancer, extra servers sit idle. '}Goal: keep 99% of visits working and every response under 0.7 seconds, for the lowest cost.</p>`;
      pgCloudLast = r;
    };
    let pgCloudLast = null;
    const link = (id, key, num) => { const i = $$('#' + id); i.oninput = i.onchange = () => { cfg[key] = i.type === 'checkbox' ? i.checked : num ? +i.value : i.value; const o = $$('#' + id + '-o'); if (o) o.textContent = i.value; redraw(); }; };
    link('cl-sc', 'scene'); link('cl-sz', 'size'); link('cl-n', 'servers', 1); link('cl-r', 'replicas', 1); link('cl-lb', 'lb'); link('cl-au', 'auto'); link('cl-m', 'max', 1); link('cl-cdn', 'cdn');
    redraw();
    return { context: () => `Scenario: ${CLOUD_SCENES[cfg.scene].name} (peak ${cfg.peak} visits per second)\nServer size: ${cfg.size}, servers: ${cfg.servers}, load balancer: ${cfg.lb}, autoscaling: ${cfg.auto} (max ${cfg.max}), CDN: ${cfg.cdn}, database replicas: ${cfg.replicas}\nResult: ${pgCloudLast.verdict}, ${pgCloudLast.availability}% of visits worked, slowest ${pgCloudLast.maxLat} ms, about $${pgCloudLast.cost} a month.\nSimulator's diagnosis: ${pgCloudLast.why}` };
  },
};

/* ═══════════ 5. App Development: Screen Builder ═══════════ */
const AB_TYPES = {
  header: { name: 'Title bar', text: 'My App' }, text: { name: 'Text', text: 'Write something here' }, button: { name: 'Button', text: 'Tap me' },
  input: { name: 'Text box', text: 'Your email' }, card: { name: 'Image card', text: 'Jollof of the day' }, list: { name: 'List', text: 'Item one, Item two, Item three' },
  toggle: { name: 'Switch', text: 'Notifications' }, tabs: { name: 'Tab bar', text: 'Home, Search, Profile' },
};
const AB_COLORS = ['#00b8c4', '#8a2be2', '#ff4d8d', '#ff9f1c', '#2ec27e'];
const AB_TEMPLATES = {
  login: { name: 'Login screen', screens: [{ name: 'Login', comps: [{ type: 'header', text: 'Welcome back' }, { type: 'input', text: 'Email' }, { type: 'input', text: 'Password' }, { type: 'button', text: 'Log in', go: 1 }, { type: 'text', text: 'New here? Create an account' }] }, { name: 'Home', comps: [{ type: 'header', text: 'Home' }, { type: 'card', text: 'Your first lesson' }, { type: 'button', text: 'Log out', go: 0 }] }] },
  shop: { name: 'Shop home', screens: [{ name: 'Shop', comps: [{ type: 'header', text: 'Mama Put' }, { type: 'card', text: 'Jollof rice, ₦1,500' }, { type: 'card', text: 'Fried plantain, ₦700' }, { type: 'button', text: 'View cart', go: 1 }, { type: 'tabs', text: 'Menu, Orders, Me' }] }, { name: 'Cart', comps: [{ type: 'header', text: 'Your cart' }, { type: 'list', text: 'Jollof rice, Plantain' }, { type: 'button', text: 'Back to menu', go: 0 }] }] },
  todo: { name: 'To-do list', screens: [{ name: 'Tasks', comps: [{ type: 'header', text: 'Today' }, { type: 'list', text: 'Finish homework, Practise coding, Call grandma' }, { type: 'toggle', text: 'Remind me' }, { type: 'button', text: 'Add task' }] }] },
  blank: { name: 'Blank', screens: [{ name: 'Screen 1', comps: [] }] },
};
let abId = 0;
const abComp = (c) => ({ id: ++abId, type: c.type, text: c.text !== undefined ? c.text : AB_TYPES[c.type].text, go: c.go === undefined ? -1 : c.go, align: c.align || 'left' });
const abScreens = (tpl) => JSON.parse(JSON.stringify(tpl)).map((s) => ({ name: s.name, comps: s.comps.map(abComp) }));

function abCompHTML(c, st, test) {
  const t = esc(c.text);
  switch (c.type) {
    case 'header': return `<div class="ab-h">${t}</div>`;
    case 'text': return `<p class="ab-t" style="text-align:${c.align}">${t}</p>`;
    case 'button': return `<button class="ab-b" data-go="${c.go}" style="background:${st.accent}">${t}</button>`;
    case 'input': return `<input class="ab-i" placeholder="${t}" ${test ? '' : 'readonly tabindex="-1"'}>`;
    case 'card': return `<div class="ab-c"><div class="ab-img">🖼️</div><b>${t}</b></div>`;
    case 'list': return `<ul class="ab-l">${c.text.split(',').map((x) => `<li>${esc(x.trim())}</li>`).join('')}</ul>`;
    case 'toggle': return `<label class="ab-s"><span>${t}</span><input type="checkbox" ${test ? '' : 'tabindex="-1"'}><i style="--a:${st.accent}"></i></label>`;
    case 'tabs': return `<div class="ab-tabs">${c.text.split(',').map((x, i) => `<span class="${i === 0 ? 'on' : ''}" style="${i === 0 ? 'color:' + st.accent : ''}">${esc(x.trim())}</span>`).join('')}</div>`;
    default: return '';
  }
}

function abPhoneHTML(st, test) {
  const scr = st.screens[st.cur];
  return `<div class="ab-phone ${st.dark ? 'dark' : ''}"><div class="ab-notch"></div><div class="ab-screen">${scr.comps.length ? scr.comps.map((c) => test ? abCompHTML(c, st, true)
    : `<div class="ab-w ${c.id === st.sel ? 'sel' : ''}" data-id="${c.id}">${abCompHTML(c, st, false)}</div>`).join('') : '<p class="ab-empty">Add a component from the list to start building this screen.</p>'}</div></div>`;
}

function abCheck(st) {   // a usability checklist, worked out from what the student built
  const out = [], many = st.screens.length > 1;
  out.push({ ok: st.screens.every((s) => s.comps.some((c) => c.type === 'header')), text: 'Every screen has a title bar, so people know where they are.' });
  out.push({ ok: st.screens.every((s) => s.comps.filter((c) => c.type === 'button').length <= 3), text: 'No screen has more than 3 buttons, which keeps it simple.' });
  out.push({ ok: st.screens.every((s) => s.comps.length <= 7), text: 'No screen is crowded: 7 things or fewer.' });
  out.push({ ok: st.screens.every((s) => s.comps.filter((c) => c.type === 'button').every((c) => c.text.length > 0 && c.text.length <= 20)), text: 'Button labels are short and clear (20 letters or fewer).' });
  out.push({ ok: st.screens.every((s) => s.comps.every((c) => c.text.trim().length > 0)), text: 'Nothing is left empty.' });
  if (many) out.push({ ok: st.screens.every((s, i) => s.comps.some((c) => c.type === 'button' && c.go >= 0 && c.go !== i)), text: 'Every screen has a button that goes to another screen, so nobody gets stuck.' });
  return out;
}

PG['app-development'] = {
  icon: '📱', name: 'Screen Builder', blurb: 'Design real app screens on a phone. Add components, edit them, link buttons between screens, then switch to Test mode and use your app.',
  mount(el) {
    const st = { screens: abScreens(AB_TEMPLATES.login.screens), cur: 0, sel: null, accent: AB_COLORS[0], dark: false, test: false };
    el.innerHTML = `<div class="pgcols ab"><div class="glass panel abwrap"><div class="pills"><button class="pill" id="ab-mode">▶ Test my app</button><label class="vchk"><input type="checkbox" id="ab-dark"> Dark mode</label></div><div id="ab-phone"></div></div>
      <div class="glass panel" id="ab-side"></div></div><div class="glass panel" id="ab-check"></div>`;
    const $$ = (s) => el.querySelector(s), find = () => st.screens[st.cur].comps.find((c) => c.id === st.sel);
    const paint = () => {
      $$('#ab-phone').innerHTML = abPhoneHTML(st, st.test); $$('#ab-mode').textContent = st.test ? '✏️ Back to editing' : '▶ Test my app';
      $$('#ab-phone').querySelectorAll('.ab-w').forEach((w) => (w.onclick = () => { st.sel = +w.dataset.id; side(); paint(); }));
      $$('#ab-phone').querySelectorAll('.ab-b').forEach((b) => (b.onclick = (e) => { if (st.test && +b.dataset.go >= 0 && st.screens[+b.dataset.go]) { st.cur = +b.dataset.go; paint(); } else if (!st.test) e.preventDefault(); }));
      $$('#ab-check').innerHTML = `<h3>Usability check</h3><ul class="abcheck">${abCheck(st).map((c) => `<li class="${c.ok ? 'ok' : 'no'}">${c.ok ? '✅' : '⚠️'} ${esc(c.text)}</li>`).join('')}</ul>`;
    };
    const side = () => {
      const c = find(), scr = st.screens[st.cur];
      $$('#ab-side').innerHTML = `<div class="seg" id="ab-scr">${st.screens.map((s, i) => `<button data-i="${i}" aria-pressed="${i === st.cur}">${esc(s.name)}</button>`).join('')}${st.screens.length < 3 ? '<button id="ab-newscr">+ Screen</button>' : ''}</div>
        <label for="ab-sn">Screen name</label><input id="ab-sn" maxlength="20" value="${esc(scr.name)}">
        <h4>Add a component</h4><div class="pills">${Object.entries(AB_TYPES).map(([k, v]) => `<button class="pill" data-add="${k}">+ ${esc(v.name)}</button>`).join('')}</div>
        ${c ? `<h4>Edit: ${esc(AB_TYPES[c.type].name)}</h4><label for="ab-tx">${c.type === 'list' || c.type === 'tabs' ? 'Items, separated by commas' : 'Text'}</label><input id="ab-tx" maxlength="80" value="${esc(c.text)}">
          ${c.type === 'text' ? `<label for="ab-al">Alignment</label><select id="ab-al">${['left', 'center', 'right'].map((a) => `<option ${c.align === a ? 'selected' : ''}>${a}</option>`).join('')}</select>` : ''}
          ${c.type === 'button' ? `<label for="ab-go">When tapped, open</label><select id="ab-go"><option value="-1">Nothing</option>${st.screens.map((s, i) => `<option value="${i}" ${c.go === i ? 'selected' : ''}>${esc(s.name)}</option>`).join('')}</select>` : ''}
          <div class="pills"><button class="pill" id="ab-up">▲ Up</button><button class="pill" id="ab-dn">▼ Down</button><button class="pill" id="ab-dup">Duplicate</button><button class="pill" id="ab-del">Delete</button></div>` : '<p class="meta">Tap a component on the phone to edit it.</p>'}
        <h4>Look and feel</h4><div class="pills">${AB_COLORS.map((x) => `<button class="swatch ${x === st.accent ? 'on' : ''}" data-c="${x}" style="background:${x}" aria-label="Accent colour ${x}"></button>`).join('')}</div>
        <label>Start from <select id="ab-tpl">${Object.entries(AB_TEMPLATES).map(([k, v]) => `<option value="${k}">${esc(v.name)}</option>`).join('')}</select></label>
        <button class="pill" id="ab-json">Copy my design as JSON</button>`;
      const S$ = (s) => $$('#ab-side').querySelector(s);
      $$('#ab-side').querySelectorAll('#ab-scr [data-i]').forEach((b) => (b.onclick = () => { st.cur = +b.dataset.i; st.sel = null; side(); paint(); }));
      const ns = S$('#ab-newscr'); if (ns) ns.onclick = () => { st.screens.push({ name: 'Screen ' + (st.screens.length + 1), comps: [] }); st.cur = st.screens.length - 1; st.sel = null; side(); paint(); };
      S$('#ab-sn').oninput = (e) => { scr.name = e.target.value.slice(0, 20) || 'Screen'; paint(); };
      $$('#ab-side').querySelectorAll('[data-add]').forEach((b) => (b.onclick = () => { if (scr.comps.length >= 12) { toast('That screen is full. Delete something first.', 'bad'); return; } const n = abComp({ type: b.dataset.add }); scr.comps.push(n); st.sel = n.id; st.test = false; side(); paint(); }));
      if (c) {
        S$('#ab-tx').oninput = (e) => { c.text = e.target.value; paint(); };
        const al = S$('#ab-al'); if (al) al.onchange = (e) => { c.align = e.target.value; paint(); };
        const go = S$('#ab-go'); if (go) go.onchange = (e) => { c.go = +e.target.value; paint(); };
        const mv = (d) => () => { const i = scr.comps.indexOf(c), j = i + d; if (j >= 0 && j < scr.comps.length) { [scr.comps[i], scr.comps[j]] = [scr.comps[j], scr.comps[i]]; paint(); } };
        S$('#ab-up').onclick = mv(-1); S$('#ab-dn').onclick = mv(1);
        S$('#ab-dup').onclick = () => { if (scr.comps.length < 12) { const n = abComp(c); scr.comps.splice(scr.comps.indexOf(c) + 1, 0, n); st.sel = n.id; side(); paint(); } };
        S$('#ab-del').onclick = () => { scr.comps.splice(scr.comps.indexOf(c), 1); st.sel = null; side(); paint(); };
      }
      $$('#ab-side').querySelectorAll('.swatch').forEach((b) => (b.onclick = () => { st.accent = b.dataset.c; side(); paint(); }));
      S$('#ab-tpl').onchange = (e) => { st.screens = abScreens(AB_TEMPLATES[e.target.value].screens); st.cur = 0; st.sel = null; side(); paint(); };
      S$('#ab-json').onclick = () => pgCopy(JSON.stringify({ accent: st.accent, dark: st.dark, screens: st.screens.map((s) => ({ name: s.name, components: s.comps.map(({ type, text, go }) => ({ type, text, ...(type === 'button' ? { opens: go >= 0 ? st.screens[go] && st.screens[go].name : null } : {}) })) })) }, null, 2), 'Your design is copied as JSON.');
    };
    $$('#ab-mode').onclick = () => { st.test = !st.test; if (st.test) st.cur = 0; side(); paint(); };
    $$('#ab-dark').onchange = (e) => { st.dark = e.target.checked; paint(); };
    side(); paint();
    return { context: () => `App design (${st.dark ? 'dark' : 'light'} mode, accent ${st.accent}):\n` + st.screens.map((s) => `Screen "${s.name}": ` + s.comps.map((c) => `${AB_TYPES[c.type].name}("${c.text}"${c.type === 'button' && c.go >= 0 ? ` opens ${st.screens[c.go] && st.screens[c.go].name}` : ''})`).join(', ')).join('\n') + '\n\nUsability check:\n' + abCheck(st).map((c) => (c.ok ? 'pass: ' : 'fail: ') + c.text).join('\n') };
  },
};

/* ═══════════ 6. Full Stack: API Lab (a pretend server you can talk to) ═══════════ */
function apiHandle(db, req) {
  const H = {}; Object.entries(req.headers || {}).forEach(([k, v]) => { H[String(k).toLowerCase()] = String(v); });
  const m = String(req.method || 'GET').toUpperCase(), u = String(req.url || '').replace(/^https?:\/\/[^/]+/, ''), [rawPath, qs = ''] = u.split('?'), path = rawPath.replace(/\/+$/, '') || '/';
  const q = new URLSearchParams(qs), ms = 20 + ((u.length * 7) % 60), json = { 'Content-Type': 'application/json' };
  const res = (status, body, headers) => ({ status, headers: { ...(body === null ? {} : json), ...(headers || {}) }, body, ms });
  const parts = path.split('/').filter(Boolean);   // ['api','todos','1']
  if (parts[0] !== 'api') return res(404, { error: 'Route not found. Every route here starts with /api' });
  let body = null;
  if (['POST', 'PUT', 'PATCH'].includes(m) && String(req.body || '').trim()) {
    if (!(H['content-type'] || '').includes('application/json')) return res(415, { error: 'Send the header Content-Type: application/json with a JSON body' });
    try { body = JSON.parse(req.body); } catch (_) { return res(400, { error: 'The body is not valid JSON. Check your quotes and commas.' }); }
    if (body === null || typeof body !== 'object' || Array.isArray(body)) return res(400, { error: 'The body must be a JSON object, like {"title": "Learn Flask"}' });
  }
  if (path === '/api/health') return m === 'GET' ? res(200, { status: 'ok', service: 'todo-api' }) : res(405, { error: 'Method not allowed' }, { Allow: 'GET' });
  if (path === '/api/secret') {
    if (m !== 'GET') return res(405, { error: 'Method not allowed' }, { Allow: 'GET' });
    if (!H.authorization) return res(401, { error: 'You are not logged in. Send an Authorization header.' }, { 'WWW-Authenticate': 'Bearer' });
    return H.authorization === 'Bearer letmein' ? res(200, { secret: 'The treasure is under the mango tree 🥭' }) : res(403, { error: 'That token is not allowed.' });
  }
  if (parts[1] !== 'todos' || parts.length > 3) return res(404, { error: 'Route not found. Try /api/todos, /api/health or /api/secret' });
  const check = (b, need) => { if ((need || 'title' in b) && (typeof b.title !== 'string' || !b.title.trim() || b.title.length > 60)) return 'title is required (1 to 60 characters)'; if ('done' in b && typeof b.done !== 'boolean') return 'done must be true or false'; return ''; };
  if (parts.length === 2) {
    if (m === 'GET') { let l = db.todos; if (q.get('done') === 'true') l = l.filter((t) => t.done); if (q.get('done') === 'false') l = l.filter((t) => !t.done); return res(200, l); }
    if (m === 'POST') {
      if (!body) return res(400, { error: 'title is required (1 to 60 characters)' });
      const e = check(body, true); if (e) return res(400, { error: e });
      const t = { id: db.nextId++, title: body.title.trim(), done: !!body.done }; db.todos.push(t); return res(201, t, { Location: '/api/todos/' + t.id });
    }
    return res(405, { error: 'Method not allowed' }, { Allow: 'GET, POST' });
  }
  const id = parseInt(parts[2], 10), t = db.todos.find((x) => x.id === id);
  if (!/^\d+$/.test(parts[2])) return res(400, { error: 'The id in the URL must be a number' });
  if (m === 'GET') return t ? res(200, t) : res(404, { error: 'Todo not found' });
  if (m === 'DELETE') { if (!t) return res(404, { error: 'Todo not found' }); db.todos.splice(db.todos.indexOf(t), 1); return res(204, null); }
  if (m === 'PUT' || m === 'PATCH') {
    if (!t) return res(404, { error: 'Todo not found' }); if (!body) return res(400, { error: 'Send a JSON body with the fields to change' });
    const e = check(body, m === 'PUT'); if (e) return res(400, { error: e });
    if ('title' in body) t.title = body.title.trim(); if ('done' in body) t.done = body.done; return res(200, t);
  }
  return res(405, { error: 'Method not allowed' }, { Allow: 'GET, PUT, PATCH, DELETE' });
}

const AL_START = () => ({ nextId: 4, todos: [{ id: 1, title: 'Learn HTML', done: true }, { id: 2, title: 'Learn Flask', done: false }, { id: 3, title: 'Build my app', done: false }] });
const AL_CHALLENGES = [
  { t: 'Create a todo called "Ship it" (a POST that returns 201)', ok: (h) => h.some((x) => x.req.method === 'POST' && x.res.status === 201 && /ship it/i.test(x.res.body && x.res.body.title)) },
  { t: 'Mark todo 2 as done (a PUT or PATCH that returns 200)', ok: (h) => h.some((x) => ['PUT', 'PATCH'].includes(x.req.method) && x.res.status === 200 && x.res.body && x.res.body.id === 2 && x.res.body.done === true) },
  { t: 'Ask for only the finished todos (GET /api/todos?done=true)', ok: (h) => h.some((x) => x.req.method === 'GET' && /done=true/.test(x.req.url) && x.res.status === 200) },
  { t: 'See what a 404 looks like (ask for a todo that does not exist)', ok: (h) => h.some((x) => x.req.method === 'GET' && x.res.status === 404) },
  { t: 'Break it on purpose: POST a todo with no title (you should get 400)', ok: (h) => h.some((x) => x.req.method === 'POST' && x.res.status === 400) },
  { t: 'Delete todo 1 (a DELETE that returns 204)', ok: (h) => h.some((x) => x.req.method === 'DELETE' && x.res.status === 204) },
  { t: 'Unlock /api/secret with the right Authorization header (hint: Bearer letmein)', ok: (h) => h.some((x) => /secret/.test(x.req.url) && x.res.status === 200) },
];
const AL_QUICK = [
  ['GET all todos', { method: 'GET', url: '/api/todos', headers: '{}', body: '' }],
  ['GET one todo', { method: 'GET', url: '/api/todos/1', headers: '{}', body: '' }],
  ['POST a new todo', { method: 'POST', url: '/api/todos', headers: '{"Content-Type": "application/json"}', body: '{"title": "My first todo"}' }],
  ['PATCH todo 2', { method: 'PATCH', url: '/api/todos/2', headers: '{"Content-Type": "application/json"}', body: '{"done": true}' }],
  ['DELETE todo 3', { method: 'DELETE', url: '/api/todos/3', headers: '{}', body: '' }],
];

PG['full-stack'] = {
  icon: '🧩', name: 'API Lab', blurb: 'This is a pretend backend that lives in your browser. Send it requests like a real app does, read the status codes, and complete the challenges.',
  mount(el) {
    const st = { db: AL_START(), hist: [] };
    el.innerHTML = `<div class="pgcols"><div class="glass panel"><div class="pills">${AL_QUICK.map(([n], i) => `<button class="pill" data-q="${i}">${esc(n)}</button>`).join('')}</div>
        <div class="alreq"><select id="al-m" aria-label="Method">${['GET', 'POST', 'PUT', 'PATCH', 'DELETE'].map((x) => `<option>${x}</option>`).join('')}</select><input id="al-u" value="/api/todos" aria-label="URL" spellcheck="false"></div>
        <label for="al-h">Headers (JSON)</label><textarea id="al-h" class="code" rows="2" spellcheck="false">{}</textarea>
        <label for="al-b">Body (JSON)</label><textarea id="al-b" class="code" rows="4" spellcheck="false"></textarea>
        <button class="btn" id="al-send">SEND REQUEST</button><p class="err" id="al-e"></p></div>
      <div class="glass panel"><h3>Response</h3><div id="al-res" class="alres"><p class="meta">Send a request to see the server's answer.</p></div></div></div>
      <div class="pgcols"><div class="glass panel"><h3>Challenges <span id="al-prog" class="meta"></span></h3><ul class="abcheck" id="al-ch"></ul></div>
      <div class="glass panel"><h3>The database right now</h3><div id="al-db"></div></div></div>`;
    const $$ = (s) => el.querySelector(s);
    const paintDb = () => { $$('#al-db').innerHTML = `<table class="altable"><thead><tr><th>id</th><th>title</th><th>done</th></tr></thead><tbody>${st.db.todos.map((t) => `<tr><td>${t.id}</td><td>${esc(t.title)}</td><td>${t.done ? '✅' : '⬜'}</td></tr>`).join('') || '<tr><td colspan="3">No todos. Create one!</td></tr>'}</tbody></table>`; };
    const paintCh = () => { const d = AL_CHALLENGES.map((c) => c.ok(st.hist)); $$('#al-prog').textContent = `${d.filter(Boolean).length} of ${AL_CHALLENGES.length} done`;
      $$('#al-ch').innerHTML = AL_CHALLENGES.map((c, i) => `<li class="${d[i] ? 'ok' : 'no'}">${d[i] ? '✅' : '⬜'} ${esc(c.t)}</li>`).join('') + (d.every(Boolean) ? '<li class="ok">🏆 You completed every challenge. You think like a backend developer now.</li>' : ''); };
    const show = (x) => { const r = x.res, cls = r.status < 300 ? 'ok' : r.status < 500 ? 'warn' : 'bad';
      $$('#al-res').innerHTML = `<div class="alstat ${cls}"><b>${r.status}</b> ${esc({ 200: 'OK', 201: 'Created', 204: 'No Content', 400: 'Bad Request', 401: 'Unauthorized', 403: 'Forbidden', 404: 'Not Found', 405: 'Method Not Allowed', 415: 'Unsupported Media Type' }[r.status] || '')}<span>${r.ms} ms</span></div>
        <h4>Headers</h4><pre class="pgcode">${esc(Object.entries(r.headers).map(([k, v]) => `${k}: ${v}`).join('\n') || '(none)')}</pre><h4>Body</h4><pre class="pgcode">${r.body === null ? '(empty)' : esc(JSON.stringify(r.body, null, 2))}</pre>`; };
    const quick = (i) => { const q = AL_QUICK[i][1]; $$('#al-m').value = q.method; $$('#al-u').value = q.url; $$('#al-h').value = q.headers; $$('#al-b').value = q.body; };
    el.querySelectorAll('[data-q]').forEach((b) => (b.onclick = () => quick(+b.dataset.q)));
    $$('#al-send').onclick = () => {
      $$('#al-e').textContent = ''; let headers = {};
      try { headers = JSON.parse($$('#al-h').value || '{}'); if (!headers || typeof headers !== 'object' || Array.isArray(headers)) throw 0; } catch (_) { $$('#al-e').textContent = 'The headers box must be a JSON object, like {"Content-Type": "application/json"}.'; return; }
      const req = { method: $$('#al-m').value, url: $$('#al-u').value.trim(), headers, body: $$('#al-b').value };
      const res = apiHandle(st.db, req), x = { req, res }; st.hist.push(x); show(x); paintDb(); paintCh();
    };
    paintDb(); paintCh();
    return { context: () => `The student is practising REST requests against a pretend todo API (routes: /api/todos, /api/todos/:id, /api/health, /api/secret needing "Authorization: Bearer letmein").\nChallenges done: ${AL_CHALLENGES.filter((c) => c.ok(st.hist)).length} of ${AL_CHALLENGES.length}\nLast requests:\n` + st.hist.slice(-5).map((x) => `${x.req.method} ${x.req.url} headers=${JSON.stringify(x.req.headers)} body=${x.req.body || '(none)'} -> ${x.res.status} ${JSON.stringify(x.res.body)}`).join('\n') + `\nDatabase: ${JSON.stringify(st.db.todos)}` };
  },
};

/* ═══════════ 7. Agentic AI: Agent Lab (a real agent, with tools you choose) ═══════════ */
const AG_TOOLS = [['calculator', '🧮 Calculator', 'does exact arithmetic'], ['get_time', '🕒 Clock', 'knows the time in Lagos'], ['search_courses', '📚 Course search', 'finds lessons by topic'],
  ['write_note', '📝 Write note', 'saves a note to a scratchpad'], ['read_notes', '📖 Read notes', 'reads the scratchpad back'], ['word_count', '🔢 Word counter', 'counts the words in a text']];
const AG_GOALS = ['What is 15% of 8,400, plus 1,250?', 'What day is it in Lagos, and how many words are in "learn it build it ship it"?', 'Find a lesson about the cloud, save a note about it, then read my notes back to me.'];

PG['agentic-ai'] = {
  icon: '🤖', name: 'Agent Lab', blurb: 'Give an AI agent a goal and choose which tools it may use. Watch it think, act and observe, step by step. Then take a tool away and see what changes.',
  mount(el) {
    const st = { last: null, busy: false };
    el.innerHTML = `<div class="glass panel"><div class="agloop"><span>🎯 Goal</span>→<span>🧠 Think</span>→<span>🔧 Act (use a tool)</span>→<span>👁 Observe the result</span>→<span>↻ repeat</span>→<span>✅ Answer</span></div>
      <div class="pgcols"><div><label for="ag-g">The goal</label><textarea id="ag-g" rows="4" maxlength="300" placeholder="What should the agent do?"></textarea>
        <div class="pills">${AG_GOALS.map((g, i) => `<button class="pill" data-g="${i}">Example ${i + 1}</button>`).join('')}</div><p class="err" id="ag-e"></p>
        <button class="btn" id="ag-run">RUN THE AGENT</button></div>
      <div><h4>Tools the agent may use</h4>${AG_TOOLS.map(([k, n, d]) => `<label class="vchk agtool"><input type="checkbox" value="${k}" ${['calculator', 'get_time', 'search_courses', 'write_note', 'read_notes'].includes(k) ? 'checked' : ''}> <span><b>${n}</b> ${esc(d)}</span></label>`).join('')}</div></div></div>
      <div class="glass panel" id="ag-out"><p class="meta">Run the agent to see every step it takes.</p></div>`;
    const $$ = (s) => el.querySelector(s), tools = () => [...el.querySelectorAll('.agtool input:checked')].map((i) => i.value);
    el.querySelectorAll('[data-g]').forEach((b) => (b.onclick = () => { $$('#ag-g').value = AG_GOALS[+b.dataset.g]; }));
    $$('#ag-run').onclick = async () => {
      const goal = $$('#ag-g').value.trim(); $$('#ag-e').textContent = '';
      if (goal.length < 5) { $$('#ag-e').textContent = 'Tell the agent what to do, at least 5 characters.'; return; }
      const b = $$('#ag-run'); b.disabled = true; b.innerHTML = '<span class="spin"></span>';
      $$('#ag-out').innerHTML = '<p class="meta"><span class="spin"></span> The agent is thinking and using its tools. This can take up to a minute.</p>';
      try {
        const used = tools(), r = await post('/api/courses/agentic-ai/playground/agent', { goal, tools: used }); st.last = { goal, tools: used, r };
        $$('#ag-out').innerHTML = `<h3>What the agent did</h3><ol class="agsteps">${r.steps.map((s) => s.type === 'think' ? `<li class="think"><b>🧠 Thinks</b><p>${esc(s.text)}</p></li>`
          : `<li class="act"><b>🔧 Uses ${esc(s.tool)}</b><code>${esc(JSON.stringify(s.args))}</code><b>👁 Sees</b><p class="${/^error/.test(s.result) ? 'err' : ''}">${esc(s.result)}</p></li>`).join('')}
          <li class="done"><b>✅ Final answer</b><p>${pgFmt(r.answer)}</p></li></ol>${r.steps.length ? '' : '<p class="meta">With no tools the agent just answered from what it already knows. Try again with the tools switched on and compare.</p>'}<p class="meta">${r.left} runs left today.</p>`;
      } catch (x) { $$('#ag-out').innerHTML = `<p class="err">${esc(x.message)}</p>`; }
      b.disabled = false; b.textContent = 'RUN THE AGENT';
    };
    return { context: () => `Agent goal: ${$$('#ag-g').value}\nTools allowed: ${tools().join(', ') || 'none'}\n` + (st.last ? `Last run:\n${st.last.r.steps.map((s) => (s.type === 'think' ? 'thought: ' + s.text : `tool ${s.tool}(${JSON.stringify(s.args)}) -> ${s.result}`)).join('\n')}\nFinal answer: ${st.last.r.answer}` : '') };
  },
};

/* ═══════════ 8. Game Development: Game Tuner (play it, then change the physics) ═══════════ */
const GM_W = 600;
const GM_PRESETS = {
  classic: { name: 'Classic', gravity: 1800, jump: 720, speed: 320, obstacle: 40, gap: 1.4, size: 30 },
  easy: { name: 'Easy', gravity: 1400, jump: 650, speed: 220, obstacle: 30, gap: 1.8, size: 28 },
  insane: { name: 'Insane', gravity: 2200, jump: 760, speed: 540, obstacle: 55, gap: 1.0, size: 34 },
  moon: { name: 'Moon gravity', gravity: 500, jump: 380, speed: 300, obstacle: 45, gap: 2.2, size: 30 },
  broken: { name: 'Broken (can you fix it?)', gravity: 3000, jump: 400, speed: 400, obstacle: 70, gap: 0.8, size: 40 },
};

function pgFairness(cfg) {   // can a human actually beat these settings? worked out with simple physics
  const H = (cfg.jump * cfg.jump) / (2 * cfg.gravity), air = (2 * cfg.jump) / cfg.gravity, notes = [], w = 24;
  const clear = H > cfg.obstacle + 4; if (!clear) notes.push(`The jump only reaches ${Math.round(H)} px, but the obstacles are ${cfg.obstacle} px tall. Increase jump power or lower gravity.`);
  const disc = cfg.jump * cfg.jump - 2 * cfg.gravity * cfg.obstacle, above = disc > 0 ? (2 * Math.sqrt(disc)) / cfg.gravity : 0, long = above * cfg.speed >= cfg.size + w;
  if (clear && !long) notes.push('You are above the obstacle for too short a time, so you clip it on the way down. Slow the game down, or jump higher.');
  const room = cfg.gap * 0.8 * cfg.speed >= air * cfg.speed + cfg.size; if (clear && long && !room) notes.push('Obstacles arrive before you can land from the last jump. Make the gap bigger or the speed lower.');
  return { fair: clear && long && room, notes, height: Math.round(H), airtime: +air.toFixed(2) };
}

function pgGameStep(s, cfg, dt, rnd) {   // moves the game forward by dt seconds. Pure: no screen, so it can be tested.
  if (s.dead) return s;
  s.vy -= cfg.gravity * dt; s.y += s.vy * dt; if (s.y <= 0) { s.y = 0; s.vy = 0; }
  s.obs.forEach((o) => { o.x -= cfg.speed * dt; }); s.obs = s.obs.filter((o) => o.x + o.w > -10);
  s.next -= dt; if (s.next <= 0) { s.obs.push({ x: GM_W + 20, w: 24, h: cfg.obstacle, counted: false }); s.next = cfg.gap * (0.8 + rnd() * 0.7); }
  s.obs.forEach((o) => { if (!o.counted && o.x + o.w < 60) { o.counted = true; s.score++; } });
  if (s.obs.some((o) => 60 < o.x + o.w && 60 + cfg.size > o.x && s.y < o.h)) s.dead = true;
  s.time += dt; return s;
}
const gmNew = () => ({ y: 0, vy: 0, obs: [], next: 1, score: 0, dead: false, time: 0 });

PG['game-development'] = {
  icon: '🎮', name: 'Game Tuner', blurb: 'Play a small jumping game, then change gravity, jump power, speed and obstacles. Game designers call this tuning. A good game is hard but fair.',
  mount(el) {
    const cfg = { ...GM_PRESETS.classic }; let g = gmNew(), running = false, raf = 0, last = 0, best = 0;
    try { best = +localStorage.getItem('oats:game:best') || 0; } catch (_) {}
    el.innerHTML = `<div class="pgcols"><div class="glass panel"><div class="gmstage" id="gm-st" tabindex="0" aria-label="Game area. Press space or tap to jump."><div class="gmplayer" id="gm-pl"></div><div id="gm-ob"></div><div class="gmmsg" id="gm-msg">Tap here or press Space to start</div></div>
        <div class="pills"><button class="btn gmbtn" id="gm-go">START</button><span class="meta">Score <b id="gm-sc">0</b> · Best <b id="gm-best">${best}</b></span></div><div class="gmfair" id="gm-fair"></div></div>
      <div class="glass panel"><label>Preset <select id="gm-pre">${Object.entries(GM_PRESETS).map(([k, v]) => `<option value="${k}">${esc(v.name)}</option>`).join('')}</select></label>
        ${pgRange('gm-g', 'Gravity', 300, 3000, 50, cfg.gravity)}${pgRange('gm-j', 'Jump power', 300, 1200, 10, cfg.jump)}${pgRange('gm-s', 'Game speed', 150, 700, 10, cfg.speed)}
        ${pgRange('gm-o', 'Obstacle height', 20, 90, 1, cfg.obstacle)}${pgRange('gm-p', 'Gap between obstacles (seconds)', 0.6, 2.5, 0.1, cfg.gap)}${pgRange('gm-z', 'Player size', 20, 50, 1, cfg.size)}</div></div>`;
    const $$ = (s) => el.querySelector(s), stage = $$('#gm-st'), pl = $$('#gm-pl'), ob = $$('#gm-ob');
    const scale = () => (stage.clientWidth || GM_W) / GM_W;
    const draw = () => {
      const k = scale(); stage.style.height = Math.round(220 * k) + 'px';
      pl.style.cssText = `width:${cfg.size * k}px;height:${cfg.size * k}px;left:${60 * k}px;bottom:${(10 + Math.min(g.y, 400)) * k}px`;
      ob.innerHTML = g.obs.map((o) => `<i style="left:${o.x * k}px;width:${o.w * k}px;height:${o.h * k}px;bottom:${10 * k}px"></i>`).join('');
      $$('#gm-sc').textContent = g.score;
    };
    const fair = () => { const f = pgFairness(cfg); $$('#gm-fair').className = 'gmfair ' + (f.fair ? 'ok' : 'no');
      $$('#gm-fair').innerHTML = `<b>${f.fair ? '✅ Fair: a skilled player can beat this.' : '⚠️ Unfair: nobody can beat these settings.'}</b> Jump height ${f.height} px, in the air for ${f.airtime} s.${f.notes.map((n) => `<p>${esc(n)}</p>`).join('')}`; };
    const msg = (t) => { $$('#gm-msg').textContent = t; $$('#gm-msg').hidden = !t; };
    const jump = () => { if (!running) { start(); return; } if (g.y <= 0.5) g.vy = cfg.jump; };
    const start = () => { g = gmNew(); running = true; last = 0; msg(''); $$('#gm-go').textContent = 'RESTART'; cancelAnimationFrame(raf); raf = requestAnimationFrame(tick); stage.focus(); };
    const tick = (now) => {
      if (!running) return; const dt = last ? Math.min(0.05, (now - last) / 1000) : 0.016; last = now; pgGameStep(g, cfg, dt, Math.random); draw();
      if (g.dead) { running = false; if (g.score > best) { best = g.score; $$('#gm-best').textContent = best; try { localStorage.setItem('oats:game:best', best); } catch (_) {} } msg(`Crash! You scored ${g.score}. Tap to try again, or tune the settings.`); $$('#gm-go').textContent = 'PLAY AGAIN'; return; }
      raf = requestAnimationFrame(tick);
    };
    pgOnCleanup(() => { running = false; cancelAnimationFrame(raf); });
    stage.onpointerdown = (e) => { e.preventDefault(); jump(); }; stage.onkeydown = (e) => { if (e.code === 'Space' || e.key === ' ' || e.key === 'ArrowUp') { e.preventDefault(); jump(); } };
    $$('#gm-go').onclick = start;
    const link = (id, key) => { const i = $$('#' + id); i.oninput = () => { cfg[key] = +i.value; $$('#' + id + '-o').textContent = i.value; fair(); draw(); }; };
    link('gm-g', 'gravity'); link('gm-j', 'jump'); link('gm-s', 'speed'); link('gm-o', 'obstacle'); link('gm-p', 'gap'); link('gm-z', 'size');
    $$('#gm-pre').onchange = (e) => { Object.assign(cfg, GM_PRESETS[e.target.value]); [['gm-g', 'gravity'], ['gm-j', 'jump'], ['gm-s', 'speed'], ['gm-o', 'obstacle'], ['gm-p', 'gap'], ['gm-z', 'size']].forEach(([id, k]) => { $$('#' + id).value = cfg[k]; $$('#' + id + '-o').textContent = cfg[k]; }); fair(); draw(); };
    fair(); draw();
    return { context: () => { const f = pgFairness(cfg); return `Game settings: gravity ${cfg.gravity}, jump power ${cfg.jump}, speed ${cfg.speed}, obstacle height ${cfg.obstacle}, gap ${cfg.gap}s, player size ${cfg.size}. Best score ${best}.\nFairness check: ${f.fair ? 'fair' : 'unfair'}; jump height ${f.height}px; airtime ${f.airtime}s. ${f.notes.join(' ')}`; } };
  },
};
