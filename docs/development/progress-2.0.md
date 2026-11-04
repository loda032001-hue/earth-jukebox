# Progreso — Earth Jukebox 2.0

Rama: `redesign/earth-jukebox-2.0`

## Etapa 3 — Rediseño de interfaz y navegación (en progreso)

### Tareas completadas
- T3.1 Sistema de diseño
- T3.2 Landing inmersiva

### Archivos modificados
- `frontend/styles/tokens.css` (nuevo)
- `frontend/styles/main.css` (import tokens, estilos hero/experiencias/pasos)
- `frontend/index.html` (rediseño inmersivo con Tierra protagonista)
- `frontend/components/layout.js` (componentes reutilizables preparados)

### Decisiones técnicas
- Se usó una imagen real de la Tierra (Apollo 17, Wikimedia Commons) como protagonista visual.
- Se mantuvo Leaflet/OpenStreetMap y la estructura existente.
- Se añadieron design tokens para coherencia visual.
- T3.3 se deja preparado (componentes creados) para refactor gradual sin romper páginas existentes.

### Problemas encontrados
- Ninguno bloqueante.

### Pruebas ejecutadas
- Verificación de archivos y estructura.
- Backend: 13 passed, 2 skipped.

### Tareas pendientes
- T3.3 (aplicar componentes en todas las páginas gradualmente)
- Etapa 4: biblioteca sonora y datos