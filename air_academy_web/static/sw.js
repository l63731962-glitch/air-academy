/* Air Academy service worker.
 *
 * Purpose: make the site installable and show a friendly page when the network is down.
 * It is served from /sw.js (see app.py) so its scope is the whole site.
 *
 * What it never touches, on purpose:
 *   - non-GET requests (login, payments, voice uploads)
 *   - /api/*  (private, per-user, already Cache-Control: no-store)
 *   - /join/* and /admin/*  (the URL itself is a secret token, never store it)
 *   - other origins (the payment pages, Google Fonts)
 * Lessons and paid content come from /api/*, so nothing paid is ever kept on the device by this file.
 *
 * Bump VERSION when you change this file's caching rules; old caches are deleted on activate.
 */
const VERSION = "v1";
const SHELL_CACHE = "air-shell-" + VERSION;
const STATIC_CACHE = "air-static-" + VERSION;
const OFFLINE_URL = "/static/offline.html";
const PRECACHE = [OFFLINE_URL, "/static/icons/icon-192.png", "/static/icons/icon-512.png"];
const NETWORK_TIMEOUT_MS = 4000; // on a slow connection, fall back to the saved copy of a script instead of waiting forever

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE)
      .then((cache) => cache.addAll(PRECACHE.map((u) => new Request(u, { cache: "reload" }))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const keep = new Set([SHELL_CACHE, STATIC_CACHE]);
    for (const key of await caches.keys()) if (key.startsWith("air-") && !keep.has(key)) await caches.delete(key);
    // Navigation preload lets the page request start while the worker boots, which matters on slow phones.
    if (self.registration.navigationPreload) { try { await self.registration.navigationPreload.enable(); } catch (_) {} }
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  const path = url.pathname;
  if (path.startsWith("/api/") || path === "/sw.js") return;

  if (req.mode === "navigate") { event.respondWith(handleNavigation(event)); return; }
  if (path.startsWith("/static/icons/")) { event.respondWith(cacheFirst(req)); return; }
  if (path.startsWith("/static/") && path !== OFFLINE_URL) { event.respondWith(networkFirst(req)); return; }
});

async function offlinePage() {
  const hit = await caches.match(OFFLINE_URL);
  return hit || new Response("Air Academy can't be reached right now. Check your connection and try again.",
    { status: 200, headers: { "Content-Type": "text/plain; charset=utf-8" } });
}

// Pages always come from the network. If the network is down, or the server is returning 5xx (for example a host waking up),
// show the offline page, which has a Retry button. Returning 200 here also keeps an installed Android app from treating it as a crash.
async function handleNavigation(event) {
  try {
    const res = (await event.preloadResponse) || (await fetch(event.request));
    return res.status >= 500 ? offlinePage() : res;
  } catch (_) {
    return offlinePage();
  }
}

// Icons never change between deploys of the same version: serve from the cache, fill it on first use.
async function cacheFirst(req) {
  const cache = await caches.open(SHELL_CACHE);
  const hit = await cache.match(req);
  if (hit) return hit;
  const res = await fetch(req);
  if (res.ok) cache.put(req, res.clone()).catch(() => {});
  return res;
}

// Scripts and styles are not fingerprinted, so always ask the server first (revalidating with ETag, which is cheap)
// and keep a copy only as the fallback for slow or missing networks.
async function networkFirst(req) {
  const cache = await caches.open(STATIC_CACHE);
  const net = fetch(req, { cache: "no-cache" }).then((res) => {
    if (res.ok) cache.put(req, res.clone()).catch(() => {});
    return res;
  });
  const slow = new Promise((resolve) => setTimeout(() => resolve(cache.match(req)), NETWORK_TIMEOUT_MS));
  try {
    const first = await Promise.race([net, slow]);
    return first || (await net);
  } catch (err) {
    const hit = await cache.match(req);
    if (hit) return hit;
    throw err;
  }
}
