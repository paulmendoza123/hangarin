// Service Worker for Hangarin PWA
const CACHE_NAME = 'hangarin-cache-v1';
const urlsToCache = [
  '/static/img/icon-192.png',
  '/static/img/icon-512.png',
];

// Install Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Activate SW - delete old caches
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => 
      Promise.all(cacheNames.map(name => {
        if (!cacheWhitelist.includes(name)) return caches.delete(name);
      }))
    )
  );
});

// Fetch from cache - bypass dynamic/auth pages
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // NEVER cache / or /accounts/ (login/logout)
  if (url.pathname === '/' || url.pathname.startsWith('/accounts/') || url.pathname.startsWith('/logout/')) {
    event.respondWith(fetch(event.request));
    return;
  }

  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});