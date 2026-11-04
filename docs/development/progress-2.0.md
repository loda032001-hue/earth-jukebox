# Progreso — Earth Jukebox 2.0

Rama: `redesign/earth-jukebox-2.0`

## Etapa 3 — Rediseño de interfaz y navegación (en progreso)

### Tareas completadas
- T3.1 Sistema de diseño
- T3.2 Landing inmersiva
- T1.1 Script de ingesta
- T1.2 Validación de metadatos
- T1.3 Paginación catálogo
- T2.1 Clustering en el mapa
- T2.2 Panel de resultados rico
- T2.3 Alternativa accesible (lista)
- T2.4 Integración mapa → laboratorio
- T4.1 Modulación en tiempo real
- T4.2 Guardado de composiciones
- T4.3 Guía de uso del laboratorio

### Archivos modificados
- `frontend/styles/tokens.css` (nuevo)
- `frontend/styles/main.css`
- `frontend/index.html`
- `frontend/components/layout.js`
- `frontend/scripts/pages/sounds.js`
- `frontend/pages/sounds.html`
- `backend/scripts/import_sounds.py` (nuevo)
- `backend/app/services/ingest.py` (nuevo)
- `backend/data/sounds.example.json` (nuevo)
- `backend/app/api/sounds.py`
- `backend/app/services/sound_catalog.py`
- `backend/tests/test_ingest.py`, `backend/tests/test_pagination.py`
- `frontend/pages/explorer.html`
- `frontend/scripts/pages/explorer.js`
- `frontend/scripts/audio/engine.js`
- `frontend/scripts/pages/music.js`
- `frontend/pages/music.html`

### Decisiones técnicas
- Ingesta vía script + validación centralizada.
- Paginación con limit/offset.
- Mapa con Leaflet.markercluster y lista accesible por teclado.
- Modulación real de capas con datos NASA POWER.
- Guardado de composiciones en Supabase cuando hay sesión.

### Problemas encontrados
- Sin marcadores reales (no hay coordenadas verificadas en seed). Estado vacío honesto.

### Pruebas ejecutadas
- Backend: 18 passed, 2 skipped.

### Tareas pendientes
- T3.3 aplicar componentes en todas las páginas.
- Etapa 6: optimización y pruebas.