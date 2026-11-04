// Inicialización del mapa Leaflet (Explorador Sonoro del Planeta).
export function createMap(containerId) {
  const map = L.map(containerId).setView([20, 0], 2);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);
  return map;
}
