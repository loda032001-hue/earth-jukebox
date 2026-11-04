import { initCarousel } from "./components/carousel.js";

document.addEventListener("DOMContentLoaded", async () => {
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.getElementById("site-nav");
  toggle?.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(open));
  });

  initCarousel("#hero-carousel");

  try {
    const apiBase = window.EJ_API_BASE || "http://127.0.0.1:8000";
    const res = await fetch(`${apiBase}/api/health`);
    if (res.ok) {
      const data = await res.json();
      console.info("Earth Jukebox API:", data.status);
    }
  } catch (err) {
    console.warn("API no disponible aún:", err?.message || err);
  }
});
