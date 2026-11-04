import { createMap } from "../map/map.js";

const API_BASE = window.EJ_API_BASE || "http://127.0.0.1:8000";
const map = createMap("map");

const markersLayer = L.layerGroup().addTo(map);
let searchCircle = null;

function escapeHtml(str) {
  return String(str).replace(/[&<>"']/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[m]));
}

async function fetchJSON(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

function renderMarker(s) {
  if (s.latitude == null || s.longitude == null) return;
  const marker = L.marker([s.latitude, s.longitude]);
  marker.bindPopup(`
    <strong>${escapeHtml(s.name)}</strong><br/>
    ${escapeHtml(s.description || "")}<br/>
    <em>${escapeHtml(s.category)}</em><br/>
    Autor: ${escapeHtml(s.author || "—")}<br/>
    Licencia: ${escapeHtml(s.license || "—")}<br/>
    Precisión: ${escapeHtml(s.location_precision || "—")}<br/>
    ${s.audio_url ? `<audio controls src="${s.audio_url}" style="width:220px"></audio>` : ""}
  `);
  markersLayer.addLayer(marker);
}

async function loadGeoSounds() {
  try {
    const items = await fetchJSON("/api/geo/sounds");
    markersLayer.clearLayers();
    items.forEach(renderMarker);
    const emptyEl = document.getElementById("map-empty");
    emptyEl.hidden = items.length > 0;
    renderResults(items);
  } catch (e) {
    console.error(e);
  }
}

function renderResults(items) {
  const el = document.getElementById("results");
  el.innerHTML = "";
  items.forEach((s) => {
    const card = document.createElement("article");
    card.className = "card";
    card.innerHTML = `<h3>${escapeHtml(s.name)}</h3><p>${escapeHtml(s.description || "")}</p>`;
    el.appendChild(card);
  });
}

async function search() {
  const lat = parseFloat(document.getElementById("lat").value);
  const lon = parseFloat(document.getElementById("lon").value);
  const radius = parseFloat(document.getElementById("radius").value);
  if (Number.isNaN(lat) || Number.isNaN(lon)) return;
  try {
    const data = await fetchJSON(`/api/geo/search?lat=${lat}&lon=${lon}&radius_km=${radius}`);
    markersLayer.clearLayers();
    data.items.forEach(renderMarker);
    if (searchCircle) map.removeLayer(searchCircle);
    searchCircle = L.circle([lat, lon], { radius: radius * 1000, color: "#4fd1ff", fillOpacity: 0.05 }).addTo(map);
    map.setView([lat, lon], 6);
    document.getElementById("map-empty").hidden = data.items.length > 0;
    renderResults(data.items);
  } catch (e) {
    console.error(e);
  }
}

document.getElementById("search-btn").addEventListener("click", search);

loadGeoSounds();
