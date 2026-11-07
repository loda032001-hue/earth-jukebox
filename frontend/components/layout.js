// Componentes reutilizables de layout (Etapa 3).
export function renderHeader(container, activePage = "index.html") {
  const links = [
    ["index.html", "Inicio"],
    ["pages/sounds.html", "Sonidos de la Tierra"],
    ["pages/explorer.html", "Explorador del Planeta"],
    ["pages/music.html", "Música de la Tierra"],
    ["pages/account.html", "Cuenta"],
  ];
  const nav = links.map(([href, label]) => {
    const current = href === activePage ? ' aria-current="page"' : "";
    return `<a href="${href}"${current}>${label}</a>`;
  }).join("");
  container.innerHTML = `
    <div class="brand"><span class="brand-mark" aria-hidden="true">◉</span><span class="brand-name">Earth Jukebox</span></div>
    <nav class="site-nav" aria-label="Principal">${nav}</nav>
  `;
}

export function renderFooter(container) {
  container.innerHTML = `
    <p>© Earth Jukebox. Datos y audio con fuentes verificables y licencias documentadas.</p>
    <p class="muted">Imágenes: Wikimedia Commons (CC). Mapas: © OpenStreetMap contributors.</p>
  `;
}
