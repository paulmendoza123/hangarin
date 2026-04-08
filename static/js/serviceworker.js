const CACHE_NAME = 'projectsite-cache-v1';
const OFFLINE_URL = '/offline/';
const ASSETS_TO_CACHE = [
    '/',
];

// INSTALL - cache assets
self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            return cache.addAll(ASSETS_TO_CACHE);
        })
    );
    self.skipWaiting();
});

// ACTIVATE - clean old caches
self.addEventListener('activate', function(e) {
    e.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(name) {
                    if (name !== CACHE_NAME) {
                        return caches.delete(name);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

// FETCH - serve from cache, fallback to network
self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            if (response) {
                return response;
            }
            return fetch(e.request).catch(function() {
                return caches.match('/');
            });
        })
    );
});