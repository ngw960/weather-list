self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open('weather-list-cache').then((cache) => {
            return cache.addAll([
                '/',
                '/static/css/weather-list.css',
                '/static/image/default.webp',
                '/static/image/Clear.webp',
                '/static/image/Clouds.webp',
                '/static/image/Rain.webp',
                '/static/icon/192x192.png',
                '/static/icon/512x512.png',
                '/static/manifest.json',
            ]);
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            return cachedResponse || fetch(event.request);
        })
    );
});
