// Carrusel accesible para la landing page.
export function initCarousel(rootSelector) {
  const root = document.querySelector(rootSelector);
  if (!root) return;

  const slides = Array.from(root.querySelectorAll(".carousel-slide"));
  const dots = Array.from(root.querySelectorAll(".carousel-dot"));
  const prev = root.querySelector(".carousel-prev");
  const next = root.querySelector(".carousel-next");
  const live = root.querySelector(".carousel-live");

  let index = 0;
  let timer = null;
  const INTERVAL = 5000;

  function show(i) {
    index = (i + slides.length) % slides.length;
    slides.forEach((s, n) => {
      s.classList.toggle("is-active", n === index);
      s.setAttribute("aria-hidden", n === index ? "false" : "true");
    });
    dots.forEach((d, n) => {
      d.classList.toggle("is-active", n === index);
      d.setAttribute("aria-current", n === index ? "true" : "false");
    });
    if (live) live.textContent = `Diapositiva ${index + 1} de ${slides.length}`;
  }

  function start() {
    stop();
    timer = setInterval(() => show(index + 1), INTERVAL);
  }
  function stop() {
    if (timer) clearInterval(timer);
    timer = null;
  }

  prev?.addEventListener("click", () => { show(index - 1); start(); });
  next?.addEventListener("click", () => { show(index + 1); start(); });
  dots.forEach((d, n) => d.addEventListener("click", () => { show(n); start(); }));

  root.addEventListener("mouseenter", stop);
  root.addEventListener("mouseleave", start);
  root.addEventListener("focusin", stop);
  root.addEventListener("focusout", start);

  root.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") { show(index - 1); start(); }
    if (e.key === "ArrowRight") { show(index + 1); start(); }
  });

  show(0);
  start();
}
