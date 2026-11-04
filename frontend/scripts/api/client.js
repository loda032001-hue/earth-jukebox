// Cliente mínimo para la API de Earth Jukebox.
const API_BASE = window.EJ_API_BASE || "http://127.0.0.1:8000";

export async function healthCheck() {
  const res = await fetch(`${API_BASE}/api/health`);
  if (!res.ok) throw new Error("API no disponible");
  return res.json();
}
