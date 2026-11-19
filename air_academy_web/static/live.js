'use strict';
/* Live-user heartbeat.
 *
 * Every 30 seconds, while this tab is on screen, it tells the server "someone is here, on this screen". The server keeps that
 * for 75 seconds, which is how the owner's Control Room knows how many people are using the app right now.
 *
 * Privacy: the only thing stored on the device is a random id for this tab (sessionStorage, gone when the tab closes).
 * Only the owner can see the live list, and it shows short names ("Ada O.") and the screen, never an email address.
 * A hidden tab, or a phone that was put down, stops pinging and drops off the count within about a minute.
 */
(function () {
  const hex = () => {
    const a = new Uint8Array(12);
    if (window.crypto && crypto.getRandomValues) crypto.getRandomValues(a); else for (let i = 0; i < a.length; i++) a[i] = Math.floor(Math.random() * 256);
    return Array.from(a, (b) => b.toString(16).padStart(2, '0')).join('');
  };
  let pid = null;
  try { pid = sessionStorage.getItem('oats_pid'); } catch (_) {}
  if (!pid || !/^[A-Za-z0-9_-]{8,40}$/.test(pid)) { pid = hex(); try { sessionStorage.setItem('oats_pid', pid); } catch (_) {} }

  // Where the student is, in plain words. Kept short: the server keeps 40 letters.
  function place() {
    if (typeof S === 'undefined' || !S.user) return 'Sign-in page';
    if (document.getElementById('pwm')) return 'Looking at the price';
    const sheet = document.getElementById('sheet');
    if (!sheet || sheet.hidden) return 'Dashboard';
    const what = { lesson: 'Lesson', exam: 'Exam', ca: 'CA record', cert: 'Certificate', play: 'Playground', practice: 'Practice', talk: 'Air Omega',
      board: 'Leaderboard', parents: 'Parent updates', projects: 'Project Studio', groups: 'Class groups' }[S.view] || 'Track page';
    const c = (S.courses || []).find((x) => x.id === S.openId);
    return c ? what + ' - ' + c.title : what;
  }

  let busy = false;
  async function beat() {
    if (busy || document.hidden) return;
    busy = true;
    try {
      const r = await fetch('/api/ping', {
        method: 'POST', credentials: 'same-origin', keepalive: true,
        headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ pid, place: place() }),
      });
      const d = await r.json().catch(() => ({}));
      if (typeof d.live === 'number') {   // only an owner's answer carries the number
        window.LIVE_N = d.live;
        const el = document.getElementById('ow-n'); if (el) el.textContent = d.live;
        window.dispatchEvent(new CustomEvent('oats-live', { detail: d.live }));
      }
    } catch (_) { /* offline or the server is waking up: the next beat tries again */ }
    busy = false;
  }

  window.livePing = beat;
  setInterval(beat, 30000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) beat(); });
  addEventListener('online', beat);
  setTimeout(beat, 1500);
})();
