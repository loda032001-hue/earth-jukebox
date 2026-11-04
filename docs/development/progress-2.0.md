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

### Verificación funcional (Etapa 5)

Verificaciones ejecutadas:
- Backend pytest: 18 passed, 2 skipped.
- Endpoint /api/geo/sounds: responde lista (vacía, sin coordenadas verificadas).
- Endpoint /api/scientific/sonify (local y desplegado): 200 OK, reglas T2M/PRECTOTCORR/WS10M y normalizados presentes.
- Audio URL (Wikimedia): HEAD devuelve 403 por falta de User-Agent en script; la reproducción en navegador usa GET con User-Agent del navegador (no probado en navegador real).
- Supabase: login, guardado y recuperación de composiciones verificados manualmente (OK).
- Mapa → laboratorio: lógica de sessionStorage implementada; no probado en navegador real.
- Accesibilidad/responsive: revisión de código; no probado con lector de pantalla.

Resultados:
- Backend funcional.
- Integración NASA POWER funcional.
- Supabase persistencia funcional.
- Mapa sin marcadores reales (estado vacío honesto).

Errores encontrados:
- Audio URL HEAD 403 (no bloqueante para reproducción en navegador).
- Sonify en frío puede tardar (cold start de Render).

Correcciones:
- Ninguna nueva en esta verificación.

### Tareas pendientes
- T3.3 aplicar componentes en todas las páginas.
- Prueba real en navegador (audio, mapa, responsive).
- Auditoría final documentada en `docs/development/final-audit-2.0.md`.

## Pre-producción (validación)

### Verificado
- Backend: 18 passed, 2 skipped.
- JS syntax: node --check sin errores.
- /api/scientific/sonify: 200 OK (local y desplegado).
- Supabase: login, favoritos, composiciones OK.
- 3 grabaciones geolocalizadas sembradas en Supabase.
- CI/CD añadido (.github/workflows/ci.yml).

### Pendiente
- Prueba real en navegador (audio, mapa, responsive, accesibilidad).
- Columna `source` en BD actual (ejecutar ALTER TABLE).

### Riesgos
- Sin rate limiting.
- Sin tests frontend.
- Sin métricas Lighthouse.

## Etapa 6 — Optimización (completada)

### Tareas completadas
- T5.1 Caché científica
- T5.2 Optimización de imágenes
- T5.3 Build de producción (decisión documentada)

### Archivos modificados
- `backend/app/core/cache.py` (nuevo)
- `backend/app/scientific/nasa_power.py` (caché)
- `netlify.toml` (nuevo)
- `docs/decisions/technical-decisions.md`

### Decisiones técnicas
- Caché en memoria TTL 1h para NASA POWER, con locks por clave.
- No se añade build step; assets estáticos pequeños.
- Cabeceras de caché en Netlify.

### Problemas encontrados
- Ninguno bloqueante.

### Pruebas ejecutadas
- Backend: 18 passed, 2 skipped.