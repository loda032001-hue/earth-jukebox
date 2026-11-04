import { } from "../api/client.js";

const API_BASE = window.EJ_API_BASE || "http://127.0.0.1:8000";
const listEl = document.getElementById("sounds-list");
const emptyEl = document.getElementById("sounds-empty");
const catSelect = document.getElementById("category-filter");
const searchInput = document.getElementById("search-input");
const applyBtn = document.getElementById("apply-filters");
const player = document.getElementById("audio-player");
const detailEl = document.getElementById("sound-detail");

async function fetchJSON(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

function renderCategories(cats) {
  cats.forEach((c) => {
    const opt = document.createElement("option");
    opt.value = c.slug;
    opt.textContent = c.name;
    catSelect.appendChild(opt);
  });
}

function renderSounds(items) {
  listEl.innerHTML = "";
  if (!items.length) {
    emptyEl.hidden = false;
    return;
  }
  emptyEl.hidden = true;
  items.forEach((s) => {
    const card = document.createElement("article");
    card.className = "card";
    const img = s.image_url ? `<img src="${escapeHtml(s.image_url)}" alt="${escapeHtml(s.name)}" class="sound-image" loading="lazy" />` : "";
    card.innerHTML = `
      ${img}
      <h3>${escapeHtml(s.name)}</h3>
      <p>${escapeHtml(s.description || "")}</p>
      <p class="muted">Categoría: ${escapeHtml(s.category)} · Autor: ${escapeHtml(s.author || "—")} · Licencia: ${escapeHtml(s.license || "—")}</p>
      <button class="btn btn-secondary play-btn" data-id="${s.id}">Reproducir</button>
    `;
    card.querySelector(".play-btn").addEventListener("click", () => playSound(s));
    listEl.appendChild(card);
  });
}

function playSound(s) {
  if (!s.audio_url) {
    detailEl.innerHTML = "<p>Esta grabación no tiene audio disponible.</p>";
    return;
  }
  player.src = s.audio_url;
  player.play().catch(() => {});
  detailEl.innerHTML = `
    <h3>${escapeHtml(s.name)}</h3>
    <p>${escapeHtml(s.description || "")}</p>
    <ul>
      <li><strong>Ubicación:</strong> ${escapeHtml(s.region || s.country || "No confirmada")}</li>
      <li><strong>Precisión:</strong> ${escapeHtml(s.location_precision || "—")}</li>
      <li><strong>Fuente:</strong> ${escapeHtml(s.source || "—")}</li>
      <li><strong>Licencia:</strong> ${escapeHtml(s.license || "—")}</li>
      <li><strong>Duración:</strong> ${s.duration_seconds ? s.duration_seconds + " s" : "—"}</li>
    </ul>
  `;
}

function escapeHtml(str) {
  return String(str).replace(/[&<>"']/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[m]));
}

async function load() {
  try {
    const cats = await fetchJSON("/api/sounds/categories");
    renderCategories(cats);
    const data = await fetchJSON("/api/sounds");
    renderSounds(data.items);
  } catch (e) {
    listEl.innerHTML = `<p class="muted">No se pudo cargar el catálogo: ${escapeHtml(e.message)}</p>`;
  }
}

applyBtn.addEventListener("click", async () => {
  const cat = catSelect.value;
  const q = searchInput.value.trim();
  const params = new URLSearchParams();
  if (cat) params.set("category", cat);
  if (q) params.set("q", q);
  try {
    const data = await fetchJSON(`/api/sounds?${params.toString()}`);
    renderSounds(data.items);
  } catch (e) {
    listEl.innerHTML = `<p class="muted">Error: ${escapeHtml(e.message)}</p>`;
  }
});

load();
