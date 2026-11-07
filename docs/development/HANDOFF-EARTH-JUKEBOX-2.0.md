# HANDOFF — Earth Jukebox 2.0

## Descripción general
Earth Jukebox es una plataforma web que conecta ciencia, naturaleza y música mediante experiencias sonoras interactivas. Permite explorar grabaciones reales de la Tierra, consultar su contexto científico y transformar datos científicos en composiciones musicales.

## Arquitectura y tecnologías
- Backend: Python + FastAPI (Render).
- Frontend: HTML5 + CSS3 + JavaScript (Netlify).
- Base de datos: Supabase (PostgreSQL + Auth + Storage + RLS).
- Mapas: Leaflet + OpenStreetMap.
- Audio: Web Audio API.
- Ciencia: NASA POWER API.
- Pruebas: Pytest.

## URLs
- Frontend: https://lovely-kringle-db5b09.netlify.app
- Backend: https://earth-jukebox.onrender.com
- Repositorio: https://github.com/loda032001-hue/earth-jukebox
- Pull Request: https://github.com/loda032001-hue/earth-jukebox/pull/1

## Ramas
- Desarrollo actual: `redesign/earth-jukebox-2.0`
- Rama estable: `main`

## Funcionalidades implementadas
- Landing inmersiva con Tierra protagonista.
- Biblioteca de sonidos con imágenes, filtros, búsqueda y paginación.
- Mapa interactivo con clustering, panel rico y lista accesible.
- Laboratorio musical con 7 capas, modulación real y guardado en Supabase.
- Comparación científica entre periodos/ubicaciones.
- Autenticación, favoritos y composiciones persistentes.
- Caché científica (TTL 1h).
- CI/CD con GitHub Actions.

## Pruebas realizadas
- Backend: 18 passed, 2 skipped (pytest).
- Sintaxis JS: node --check sin errores.
- Integración NASA POWER: 200 OK.
- Supabase: login, favoritos, composiciones verificados.

## Estado del despliegue
- Backend desplegado en Render (live).
- Frontend desplegado en Netlify (live).
- Base de datos Supabase configurada con RLS y datos seed.

## Variables de entorno necesarias (sin valores)
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`
- `NASA_POWER_BASE_URL`
- `CORS_ORIGINS`

## Problemas conocidos
- Mapa sin marcadores reales hasta verificar coordenadas (3 grabaciones geolocalizadas añadidas).
- Experiencia en navegador no probada manualmente.
- Sin rate limiting ni tests frontend.
- Columna `source` puede faltar en BD actual.

## Tareas pendientes
- T3.3 aplicar componentes en todas las páginas.
- Prueba real en navegador (audio, mapa, responsive, accesibilidad).
- Ejecutar `ALTER TABLE natural_sounds ADD COLUMN IF NOT EXISTS source text;` en Supabase.
- Revisar métricas Lighthouse.

## Riesgos antes de producción
- Falta de pruebas en navegador.
- Falta de contenido con coordenadas verificables.
- Sin CI/CD con pruebas de frontend.

## Próximos pasos recomendados
1. Probar en navegador (audio, mapa, responsive, accesibilidad).
2. Revisar y aprobar el Pull Request #1.
3. Hacer merge a `main` tras aprobación.
4. Desplegar backend y frontend.
5. Añadir más grabaciones con coordenadas verificables.

## Comandos para retomar el desarrollo

```bash
git clone https://github.com/loda032001-hue/earth-jukebox.git
cd earth-jukebox
git checkout redesign/earth-jukebox-2.0
cd backend
pip install -r requirements-dev.txt
pytest -q
cd ../frontend
# Servir estático, ej. python -m http.server 5500
```