# Progreso — Earth Jukebox 2.0

Rama: `redesign/earth-jukebox-2.0`

## Etapa 3 — Rediseño de interfaz y navegación (en progreso)

### Tareas completadas
- T3.1 Sistema de diseño
- T3.2 Landing inmersiva
- T1.1 Script de ingesta
- T1.2 Validación de metadatos
- T1.3 Paginación catálogo
- T5 (parcial) integración frontend (imágenes, paginación)

### Archivos modificados
- `frontend/styles/tokens.css` (nuevo)
- `frontend/styles/main.css`
- `frontend/index.html`
- `frontend/components/layout.js`
- `frontend/scripts/pages/sounds.js` (paginación)
- `frontend/pages/sounds.html` (botón cargar más)
- `backend/scripts/import_sounds.py` (nuevo)
- `backend/app/services/ingest.py` (nuevo)
- `backend/data/sounds.example.json` (nuevo)
- `backend/app/api/sounds.py` (paginación)
- `backend/app/services/sound_catalog.py` (paginación)
- `backend/tests/test_ingest.py`, `backend/tests/test_pagination.py` (nuevos)

### Decisiones técnicas
- Ingesta vía script + validación centralizada en `app/services/ingest.py`.
- Paginación con limit/offset en API y frontend.
- No se inventaron coordenadas; precisión documentada.

### Problemas encontrados
- Ninguno bloqueante.

### Pruebas ejecutadas
- Backend: 18 passed, 2 skipped.

### Tareas pendientes
- T3.3 aplicar componentes en todas las páginas.
- Etapa 5: mapa y audio (T2.x, T4.x).