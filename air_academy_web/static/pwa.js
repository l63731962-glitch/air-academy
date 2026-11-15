/* Air Academy: "install it like an app" layer.
 *
 *  1. Registers the service worker (/sw.js) so Chrome, Edge and Android offer installation.
 *  2. Shows a small, dismissible install banner (Android / Windows / Mac), or an "Add to Home Screen" hint on iPhone/iPad.
 *  3. Makes the Android Back button (and browser Back) close the open course / lesson / assistant instead of leaving the app.
 *  4. Small installed-app polish (no accidental pull-to-refresh, assistant button clear of the iPhone home bar).
 *
 * Load it last, after assistant.js. It only reads existing globals (S, airDock, closeSheet, toast) and never redeclares them.
 * window.AirPWA.canInstall() / .install() are there if you later want an "Install app" menu item.
 */
(() => {
  'use strict';

  const DAY = 864e5;
  const KEY = 'air.pwa.dismissed';
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (_) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (_) { /* private mode: just ask again next time */ } },
  };
  const media = (q) => { try { return matchMedia(q).matches; } catch (_) { return false; } };
  const isInstalled = () =>
    ['standalone', 'fullscreen', 'minimal-ui', 'window-controls-overlay'].some((m) => media(`(display-mode: ${m})`)) || navigator.standalone === true;
  const recentlyDismissed = (days) => { const t = +store.get(KEY); return !!t && Date.now() - t < days * DAY; };
  const say = (msg) => { if (typeof toast === 'function') toast(msg); };

  if (isInstalled()) document.documentElement.classList.add('is-app');

  /* ───────── styles ───────── */
  const css = document.createElement('style');
  css.textContent = `
    .airdock{right:max(16px,env(safe-area-inset-right));bottom:max(16px,env(safe-area-inset-bottom))}
    html.is-app,html.is-app body{overscroll-behavior-y:contain}
    .airpwa{position:fixed;left:50%;top:max(12px,env(safe-area-inset-top));transform:translateX(-50%);z-index:60;width:min(460px,calc(100% - 24px));
      display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:16px;background:#12131c;
      box-shadow:0 12px 34px rgba(0,0,0,.5),0 0 0 1px rgba(0,240,255,.28);animation:airpwa-in .35s both}
    .airpwa img{width:40px;height:40px;border-radius:10px;flex:none}
    .airpwa p{margin:0;flex:1;min-width:0;font-size:14px;line-height:1.35}
    .airpwa small{display:block;margin-top:2px;color:var(--mut);font-size:12.5px;line-height:1.35}
    .airpwa .btn{width:auto;flex:none;padding:10px 16px;font-size:13px;letter-spacing:1px}
    .airpwa .ghost{flex:none;padding:6px 11px}
    .airpwa svg{width:14px;height:14px;vertical-align:-2px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
    @keyframes airpwa-in{from{opacity:0;transform:translate(-50%,-12px)}to{opacity:1;transform:translate(-50%,0)}}
    @media (prefers-reduced-motion:reduce){.airpwa{animation:none}}
    @media print{.airpwa{display:none!important}}`;
  document.head.append(css);

  /* ───────── service worker ───────── */
  if ('serviceWorker' in navigator) {
    const reg = () => navigator.serviceWorker.register('/sw.js', { scope: '/' }).catch(() => { /* not https, or blocked: the site still works normally */ });
    document.readyState === 'complete' ? reg() : addEventListener('load', reg);
  }

  /* ───────── install banner ───────── */
  let deferred = null;   // Chrome/Edge/Android: the browser's saved install prompt
  let banner = null;
  let timer = null;

  function closeBanner(remember) {
    if (banner) { banner.remove(); banner = null; }
    if (remember) store.set(KEY, String(Date.now()));
  }

  function showBanner(kind) {
    if (banner || isInstalled()) return;
    banner = document.createElement('div');
    banner.className = 'airpwa';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-label', 'Install Air Academy');
    banner.innerHTML = kind === 'ios'
      ? `<img src="/static/icons/icon-192.png" alt="" width="40" height="40">
         <p><b>Install Air Academy</b><small>Tap <svg viewBox="0 0 24 24" aria-label="Share"><path d="M12 3v12M8 7l4-4 4 4M6 11H5v10h14V11h-1"/></svg> Share, then “Add to Home Screen”.</small></p>
         <button type="button" class="ghost" data-a="later">Got it</button>`
      : `<img src="/static/icons/icon-192.png" alt="" width="40" height="40">
         <p><b>Install Air Academy</b><small>Opens in its own window, like an app.</small></p>
         <button type="button" class="btn" data-a="install">INSTALL</button>
         <button type="button" class="ghost" data-a="later" aria-label="Not now">✕</button>`;
    banner.addEventListener('click', (e) => {
      const b = e.target.closest('[data-a]');
      if (!b) return;
      if (b.dataset.a === 'install') install();
      else closeBanner(true);
    });
    document.body.append(banner);
  }

  async function install() {
    if (!deferred) return;
    const prompt = deferred; deferred = null;
    closeBanner(false);
    try {
      prompt.prompt();
      const { outcome } = await prompt.userChoice;
      if (outcome !== 'accepted') store.set(KEY, String(Date.now()));
    } catch (_) { /* prompt already used */ }
  }

  function scheduleBanner(kind, days, delayMs) {
    if (timer || isInstalled() || recentlyDismissed(days)) return;
    // Wait a little so we don't greet a brand-new visitor with a banner before they've seen the app.
    timer = setTimeout(() => { timer = null; if (kind === 'ios' || deferred) showBanner(kind); }, delayMs);
  }

  addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();          // keep Chrome's own mini-bar away; we show ours instead
    deferred = e;
    scheduleBanner('chrome', 14, 15000);
  });

  addEventListener('appinstalled', () => {
    deferred = null; clearTimeout(timer); timer = null; closeBanner(false);
    say('Air Academy is installed. Open it from your home screen or apps list.');
  });

  // iPhone / iPad have no install prompt API, so explain the Share-menu route (not inside Facebook/Instagram-style in-app browsers).
  const ua = navigator.userAgent || '';
  const onIOS = /iPad|iPhone|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  if (onIOS && !/FBAN|FBAV|Instagram|TikTok|Snapchat|Line\//.test(ua)) scheduleBanner('ios', 30, 20000);

  window.AirPWA = {
    canInstall: () => !!deferred,
    install: () => { if (deferred) return install(); },
  };

  /* ───────── Back button ─────────
   * Courses, lessons and the assistant open as overlays and add no browser history, so Back would exit the app.
   * While any overlay is open we keep exactly one spare history entry; pressing Back consumes it, and we use that moment
   * to step back inside the app (the screen's own "‹ Back" button, or close the assistant panel).
   */
  let guard = false;   // our spare history entry is currently on the stack
  let skip = 0;        // popstate events we caused ourselves and must ignore

  const sheetOpen = () => { const s = document.getElementById('sheet'); return !!s && !s.hidden; };
  const panelOpen = () => { const p = document.getElementById('airpanel'); return !!p && !p.closest('[hidden]'); };
  const overlayOpen = () => sheetOpen() || panelOpen();

  function sync() {
    const open = overlayOpen();
    if (open && !guard) {
      history.pushState({ air: 1 }, '');
      guard = true;
    } else if (!open && guard) {
      guard = false;
      if (history.state && history.state.air) { skip++; history.back(); }   // the app closed it by itself: drop our spare entry
    }
  }

  addEventListener('popstate', () => {
    if (skip > 0) { skip--; return; }
    if (!guard) return;
    guard = false;   // the browser just used up our spare entry

    // Never abandon a payment that is in progress (Flutterwave's own window has its close button).
    const paying = typeof S !== 'undefined' && S && S.paying;
    if (!paying) {
      if (panelOpen()) {
        if (typeof airDock !== 'undefined') airDock.close();
      } else if (sheetOpen()) {
        const back = document.getElementById('bk');
        if (back) back.click();
        else if (typeof closeSheet === 'function') closeSheet();
      }
    }
    // Lesson -> course keeps the overlay open, so put the spare entry back for the next Back press.
    sync(); setTimeout(sync, 0); setTimeout(sync, 250);
  });

  new MutationObserver(sync).observe(document.body, { subtree: true, attributes: true, attributeFilter: ['hidden'] });
  sync();
})();
