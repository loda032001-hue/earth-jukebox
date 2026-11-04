# Decisiones técnicas

## Stack definido (prompt maestro)

- Backend: Python + FastAPI.
- Frontend: HTML5 + CSS3 + JavaScript.
- Audio: Web Audio API.
- BD: Supabase (PostgreSQL + Auth + Storage).
- Procesamiento científico: NumPy, SciPy, Librosa, SoundFile.
- Mapas: Leaflet + OpenStreetMap.

## Dependencias y despliegue

### Conflicto de dependencias (Render)
- Problema: `pytest==9.2.0` era incompatible con `pytest-asyncio==0.24.0`, que requiere `pytest>=8.2,<9`.
- Solución: separar dependencias de runtime y desarrollo.
  - `backend/requirements.txt`: solo dependencias de producción (sin pytest).
  - `backend/requirements-dev.txt`: dependencias de desarrollo (`pytest==8.4.2`, `pytest-asyncio==0.24.0`).
- Verificación: instalación limpia en entorno virtual y `pytest` ejecutado correctamente (13 passed, 2 skipped).
- Motivo: Render solo necesita dependencias de runtime; las de prueba no deben bloquear el despliegue.

## Decisiones iniciales (Etapa 0)

1. **Leaflet 2.0 beta** disponible; usar versión estable 1.x si se detectan incompatibilidades. Decidir en Etapa 3.
2. **OpenStreetMap raster** como fuente inicial, respetando política de tiles (atribución, User-Agent, sin bulk download). Proveedor alternativo a evaluar si se requiere offline.
3. **NASA POWER API** como primera fuente científica (sin API key, datos meteorológicos/solares). Verificar límites y formato.
4. **Geografía MVP**: lat/lon + Haversine; PostGIS en etapa posterior.
5. **Audio**: Freesound/Xeno-canto/Archivo como candidatos; requieren API keys y verificación de licencias.
6. **Agentes OpenCode**: archivos Markdown en `.opencode/agents/` (formato V2).
