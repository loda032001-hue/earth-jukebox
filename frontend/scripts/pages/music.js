import { AudioEngine } from "../audio/engine.js";

const API_BASE = window.EJ_API_BASE || "http://127.0.0.1:8000";
const engine = new AudioEngine();

// Integración con el mapa: si viene de "Sonificar esta ubicación", usar esas coordenadas.
const presetLat = sessionStorage.getItem("ej-sonify-lat");
const presetLon = sessionStorage.getItem("ej-sonify-lon");
if (presetLat) document.getElementById("lat").value = presetLat;
if (presetLon) document.getElementById("lon").value = presetLon;
sessionStorage.removeItem("ej-sonify-lat");
sessionStorage.removeItem("ej-sonify-lon");

const LAYER_DEFS = [
  { id: "oceans", name: "Océanos", type: "noise", baseFreq: 400, volume: 0.4, enabled: true },
  { id: "atmosphere", name: "Atmósfera", type: "sine", baseFreq: 110, volume: 0.3, enabled: true },
  { id: "temperature", name: "Temperatura", type: "triangle", baseFreq: 440, volume: 0.3, enabled: true },
  { id: "wind", name: "Viento", type: "noise", baseFreq: 1200, volume: 0.25, enabled: false },
  { id: "geology", name: "Actividad geológica", type: "sawtooth", baseFreq: 80, volume: 0.3, enabled: false },
  { id: "fauna", name: "Fauna", type: "square", baseFreq: 660, volume: 0.2, enabled: false },
  { id: "synthetic", name: "Sonidos sintéticos", type: "sine", baseFreq: 880, volume: 0.25, enabled: false },
];

LAYER_DEFS.forEach((d) => engine.addLayer(d.id, d));

function escapeHtml(str) {
  return String(str).replace(/[&<>"']/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[m]));
}

async function fetchJSON(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

let lastNormalized = null;

// Sonificación
document.getElementById("run").addEventListener("click", async () => {
  const lat = document.getElementById("lat").value;
  const lon = document.getElementById("lon").value;
  const start = document.getElementById("start").value;
  const end = document.getElementById("end").value;
  try {
    const data = await fetchJSON(`/api/scientific/sonify?latitude=${lat}&longitude=${lon}&start=${start}&end=${end}`);
    const rulesEl = document.getElementById("rules");
    rulesEl.innerHTML = "";
    data.rules.forEach((r) => {
      const card = document.createElement("article");
      card.className = "card";
      card.innerHTML = `<h3>${escapeHtml(r.variable)}</h3><p><strong>${escapeHtml(r.musical_parameter)}</strong></p><p>${escapeHtml(r.description)}</p>`;
      rulesEl.appendChild(card);
    });
    lastNormalized = data.normalized;
    document.getElementById("normalized").textContent = JSON.stringify(data.normalized, null, 2);
  } catch (e) {
    document.getElementById("normalized").textContent = `Error: ${e.message}`;
  }
});

// Capas
const layersEl = document.getElementById("layers");
LAYER_DEFS.forEach((d) => {
  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `
    <h3>${escapeHtml(d.name)}</h3>
    <label><input type="checkbox" data-layer="${d.id}" class="layer-toggle" ${d.enabled ? "checked" : ""} /> Activar</label>
    <label>Volumen <input type="range" min="0" max="1" step="0.01" value="${d.volume}" data-vol="${d.id}" class="layer-vol" /></label>
  `;
  layersEl.appendChild(card);
});

layersEl.addEventListener("change", (e) => {
  if (e.target.classList.contains("layer-toggle")) {
    engine.setLayerEnabled(e.target.dataset.layer, e.target.checked);
  }
  if (e.target.classList.contains("layer-vol")) {
    engine.setLayerVolume(e.target.dataset.vol, parseFloat(e.target.value));
  }
});

// Transporte
document.getElementById("play").addEventListener("click", () => engine.play());
document.getElementById("pause").addEventListener("click", () => engine.pause());
document.getElementById("stop").addEventListener("click", () => engine.stop());

document.getElementById("master-vol").addEventListener("input", (e) => {
  engine.setMasterVolume(parseFloat(e.target.value));
});

// Guardar / cargar
document.getElementById("save-comp").addEventListener("click", async () => {
  const name = document.getElementById("comp-name").value.trim() || "Sin nombre";
  const state = engine.saveComposition(name);
  const token = localStorage.getItem("ej-token");
  if (token) {
    try {
      await fetch(`${API_BASE}/api/compositions`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token, name, data: state }),
      });
      alert("Composición guardada (local + Supabase)");
    } catch (e) {
      alert("Guardada localmente. Error al guardar en Supabase: " + e.message);
    }
  } else {
    alert("Composición guardada (solo local; inicia sesión para persistir)");
  }
});

document.getElementById("load-comp").addEventListener("click", () => {
  const list = document.getElementById("saved-list");
  list.innerHTML = "";
  const comps = engine.loadCompositions();
  if (!comps.length) {
    list.innerHTML = "<p class='muted'>No hay composiciones guardadas.</p>";
    return;
  }
  comps.forEach((c) => {
    const card = document.createElement("article");
    card.className = "card";
    card.innerHTML = `<h3>${escapeHtml(c.name)}</h3><p>Capas: ${c.layers.filter((l) => l.enabled).length}</p>`;
    list.appendChild(card);
  });
});

// Aplicar datos científicos a capas (modulación real)
document.getElementById("apply-data").addEventListener("click", () => {
  if (!lastNormalized) { alert("Primero sonifica datos."); return; }
  const t2m = lastNormalized.T2M ? Object.values(lastNormalized.T2M).filter((v) => v !== null) : [];
  if (t2m.length) {
    const avg = t2m.reduce((a, b) => a + b, 0) / t2m.length;
    engine.setLayerBaseFreq("temperature", 220 + avg * 440);
  }
  const ws = lastNormalized.WS10M ? Object.values(lastNormalized.WS10M).filter((v) => v !== null) : [];
  if (ws.length) {
    const avg = ws.reduce((a, b) => a + b, 0) / ws.length;
    engine.setLayerBaseFreq("wind", 600 + avg * 800);
  }
  const pr = lastNormalized.PRECTOTCORR ? Object.values(lastNormalized.PRECTOTCORR).filter((v) => v !== null) : [];
  if (pr.length) {
    const avg = pr.reduce((a, b) => a + b, 0) / pr.length;
    // modular volumen de océanos con precipitación
    engine.setLayerVolume("oceans", 0.2 + avg * 0.6);
  }
  alert("Datos aplicados a las capas.");
});

// Visualización
const canvas = document.getElementById("viz");
const ctx2d = canvas.getContext("2d");
function drawViz() {
  requestAnimationFrame(drawViz);
  const analyser = engine.getAnalyser();
  if (!analyser) return;
  const data = new Uint8Array(analyser.frequencyBinCount);
  analyser.getByteFrequencyData(data);
  ctx2d.fillStyle = "#0d1430";
  ctx2d.fillRect(0, 0, canvas.width, canvas.height);
  const barWidth = canvas.width / data.length;
  data.forEach((v, i) => {
    const h = (v / 255) * canvas.height;
    ctx2d.fillStyle = "#4fd1ff";
    ctx2d.fillRect(i * barWidth, canvas.height - h, barWidth - 2, h);
  });
}
drawViz();
