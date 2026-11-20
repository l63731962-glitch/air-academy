/* Welcome video: plays full screen the moment the app opens, then an EXPLORE button pops up to continue.
 *
 * It is loaded in <head> so the video starts downloading at once and the app never flashes underneath.
 * To change the video: replace static/intro.mp4 (H.264 video + AAC sound, under about 2 MB, under about 10 seconds),
 * then add 1 to VERSION below so phones that already saved the old one fetch the new one.
 *
 * It never gets in the way:
 *   - If the video is missing, cannot play, or has not started after 7 seconds, it quietly steps aside.
 *   - There is a Skip button from the first second.
 *   - It is not shown for Data Saver / slow 2G connections, for people who asked their phone for reduced motion,
 *     or when a student is coming back from a payment page.
 */
(function () {
  var VERSION = 1;                         // add 1 whenever you replace static/intro.mp4
  var SHOW = "session";                    // "session": once each time the app is opened. "always": on every page load. "day": once a day.
  var START_TIMEOUT_MS = 7000;             // give up if the first picture has not appeared by then (slow data)
  var STALL_TIMEOUT_MS = 6000;             // if it freezes part-way for this long, just show Explore
  var KEY = "oats_intro_seen";

  function safe(fn, otherwise) { try { return fn(); } catch (_) { return otherwise; } }

  // ---- decide whether to play at all
  var q = location.search;
  if (location.pathname !== "/" || /[?&](reference|trxref|nointro)=?/i.test(q)) return;   // only the front page; never over a payment return
  if (safe(function () { return matchMedia("(prefers-reduced-motion: reduce)").matches; }, false)) return;
  var conn = navigator.connection || {};
  if (conn.saveData || /(^|-)2g$/.test(conn.effectiveType || "")) return;
  var today = new Date().toISOString().slice(0, 10);
  if (SHOW === "session" && safe(function () { return sessionStorage.getItem(KEY); }, null)) return;
  if (SHOW === "day" && safe(function () { return localStorage.getItem(KEY); }, null) === today) return;
  safe(function () { sessionStorage.setItem(KEY, "1"); localStorage.setItem(KEY, today); });

  // ---- the overlay (a child of <html>, so it exists before the page body is even read)
  var css = document.createElement("style");
  css.textContent =
    "#intro{position:fixed;inset:0;z-index:2147483000;background:radial-gradient(70% 50% at 85% -10%,rgba(138,43,226,.38),transparent),radial-gradient(50% 45% at -10% 25%,rgba(0,240,255,.2),transparent),#05060d;" +
    "display:flex;align-items:center;justify-content:center;opacity:1;transition:opacity .35s ease;overflow:hidden}" +
    "#intro.out{opacity:0;pointer-events:none}" +
    "#intro video{width:100%;height:100%;object-fit:contain;display:block;background:transparent}" +
    "#intro .bar{position:absolute;left:0;right:0;bottom:0;padding:16px 18px calc(18px + env(safe-area-inset-bottom));display:flex;justify-content:space-between;align-items:center;gap:12px}" +
    "#intro .bar button{font:600 13px Sora,system-ui,sans-serif;color:#e8ecf5;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);border-radius:99px;padding:9px 16px;cursor:pointer;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}" +
    "#intro .bar button:hover{background:rgba(255,255,255,.18)}" +
    "#intro .go{position:absolute;left:50%;bottom:calc(11% + env(safe-area-inset-bottom));transform:translateX(-50%);border:0;border-radius:16px;padding:16px 44px;cursor:pointer;" +
    "font:700 17px 'Chakra Petch',system-ui,sans-serif;letter-spacing:3px;color:#fff;background:linear-gradient(90deg,#8a2be2,#5b8cff);" +
    "box-shadow:0 0 0 1px rgba(255,255,255,.25) inset,0 10px 40px rgba(91,140,255,.55);animation:introPop .6s cubic-bezier(.2,1.4,.4,1) both,introGlow 2s ease-in-out .6s infinite}" +
    "#intro .go:active{transform:translateX(-50%) scale(.96)}" +
    "#intro .go:focus-visible,#intro .bar button:focus-visible{outline:3px solid #00f0ff;outline-offset:3px}" +
    "@keyframes introPop{0%{opacity:0;transform:translateX(-50%) translateY(26px) scale(.5)}100%{opacity:1;transform:translateX(-50%) translateY(0) scale(1)}}" +
    "@keyframes introGlow{0%,100%{box-shadow:0 0 0 1px rgba(255,255,255,.25) inset,0 10px 40px rgba(91,140,255,.45)}50%{box-shadow:0 0 0 1px rgba(255,255,255,.35) inset,0 10px 56px rgba(0,240,255,.7)}}" +
    "html[data-intro=on],html[data-intro=on] body{overflow:hidden}";
  document.head.appendChild(css);

  var box = document.createElement("div");
  box.id = "intro"; box.setAttribute("role", "dialog"); box.setAttribute("aria-modal", "true"); box.setAttribute("aria-label", "Welcome to Open Air Tech Space");
  var v = document.createElement("video");
  v.setAttribute("playsinline", ""); v.setAttribute("webkit-playsinline", ""); v.setAttribute("disablepictureinpicture", ""); v.setAttribute("disableremoteplayback", "");
  v.setAttribute("controlslist", "nodownload noplaybackrate"); v.preload = "auto"; v.playsInline = true;
  var mp4 = document.createElement("source"); mp4.src = "/static/intro.mp4?v=" + VERSION; mp4.type = "video/mp4";
  var webm = document.createElement("source"); webm.src = "/static/intro.webm?v=" + VERSION; webm.type = "video/webm";   // optional: only used if this file exists and the mp4 cannot play
  v.appendChild(mp4); v.appendChild(webm);
  var bar = document.createElement("div"); bar.className = "bar";
  var sound = document.createElement("button"); sound.type = "button"; sound.hidden = true;
  var skip = document.createElement("button"); skip.type = "button"; skip.textContent = "Skip"; skip.setAttribute("aria-label", "Skip the welcome video");
  bar.appendChild(sound); bar.appendChild(skip);
  box.appendChild(v); box.appendChild(bar);
  document.documentElement.setAttribute("data-intro", "on");
  document.documentElement.appendChild(box);
  function lockPage(on) { if (document.body) document.body.inert = on; }   // keyboard users cannot wander into the app behind the video
  if (document.body) lockPage(true); else document.addEventListener("DOMContentLoaded", function () { if (document.getElementById("intro")) lockPage(true); });

  // ---- finishing
  var done = false, timers = [];
  function later(fn, ms) { var t = setTimeout(fn, ms); timers.push(t); return t; }
  function close() {
    if (done) return; done = true;
    timers.forEach(clearTimeout);
    document.removeEventListener("keydown", onKey, true);
    box.classList.add("out");
    lockPage(false);
    document.documentElement.removeAttribute("data-intro");
    safe(function () { v.pause(); });
    setTimeout(function () { safe(function () { v.removeAttribute("src"); v.load(); }); box.remove(); css.remove(); }, 400);
  }
  function showExplore() {
    if (done || box.querySelector(".go")) return;
    timers.forEach(clearTimeout);
    skip.hidden = true; sound.hidden = true;
    var go = document.createElement("button"); go.type = "button"; go.className = "go"; go.textContent = "EXPLORE"; go.setAttribute("aria-label", "Explore Open Air Tech Space");
    go.addEventListener("click", close);
    box.appendChild(go);
    safe(function () { go.focus({ preventScroll: true }); });
  }
  function onKey(e) {
    if (e.key === "Escape") { e.preventDefault(); close(); }
    else if (e.key === "Enter" && box.querySelector(".go")) { e.preventDefault(); close(); }
  }
  document.addEventListener("keydown", onKey, true);
  skip.addEventListener("click", close);

  // ---- sound: browsers only allow sound to start by itself in a few cases, so try it and fall back to silent with a button
  function paintSound() { sound.textContent = v.muted ? "🔇 Tap for sound" : "🔊 Sound on"; sound.setAttribute("aria-pressed", v.muted ? "false" : "true"); }
  sound.addEventListener("click", function () { v.muted = !v.muted; if (!v.muted && v.paused && !v.ended) safe(function () { v.play(); }); paintSound(); });

  // ---- give up quietly if it cannot start
  var started = false;
  later(function () { if (!started) close(); }, START_TIMEOUT_MS);
  mp4.addEventListener("error", function () { /* the webm source (if any) gets its turn */ });
  webm.addEventListener("error", function () { if (!started) close(); });   // neither file is usable
  v.addEventListener("error", function () { if (!started) close(); else showExplore(); });
  v.addEventListener("playing", function () {
    started = true; timers.forEach(clearTimeout); sound.hidden = false; paintSound();
  });
  var stall;
  v.addEventListener("waiting", function () { if (started) stall = later(showExplore, STALL_TIMEOUT_MS); });
  v.addEventListener("playing", function () { clearTimeout(stall); });
  v.addEventListener("ended", showExplore);

  v.muted = false;
  var p = v.play();
  if (p && p.catch) {
    p.catch(function () {                       // sound was not allowed to start by itself: play it silent instead
      v.muted = true;
      var again = v.play();
      if (again && again.catch) again.catch(function () { if (!started) close(); });   // not even silent (for example iPhone Low Power Mode)
    });
  }
})();
