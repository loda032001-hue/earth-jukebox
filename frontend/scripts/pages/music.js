import { AudioEngine } from "../audio/engine.js";

const API_BASE = window.EJ_API_BASE || "http://127.0.0.1:8000";
const engine = new AudioEngine();

const LAYER_DEFS = [
  { id: "oceans", name: "Océanos", type: "noise", baseFreq: 400, volume: 0.4 },
  { id: "atmosphere", name: "Atmósfera", type: "sine", baseFreq: 110, volume: 0.3 },
  { id: "temperature", name: "Temperatura", type: "triangle", baseFreq: 440, volume: 0.3 },
  { id: "wind", name: "Viento", type: "noise", baseFreq: 1200, volume: 0.25 },
  { id: "geology", name: "Actividad geológica", type: "sawtooth", baseFreq: 80, volume: 0.3 },
  { id: "fauna", name: "Fauna", type: "square", baseFreq: 660, volume: 0.2 },
  { id: "synthetic", name: "Sonidos sintéticos", type: "sine", baseFreq: 880, volume: 0.25 },
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
    <label><input type="checkbox" data-layer="${d.id}" class="layer-toggle" /> Activar</label>
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
document.getElementById("save-comp").addEventListener("click", () => {
  const name = document.getElementById("comp-name").value.trim() || "Sin nombre";
  engine.saveComposition(name);
  alert("Composición guardada");
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
