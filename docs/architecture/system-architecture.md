# Arquitectura del sistema — Earth Jukebox

## Visión general

Earth Jukebox es una aplicación web con backend Python (FastAPI), frontend HTML/CSS/JS, base de datos Supabase (PostgreSQL) y motor de audio en el navegador (Web Audio API). El procesamiento científico se realiza en Python y se entrega al frontend como parámetros musicales.

## Componentes

- **Frontend (HTML5/CSS3/JS)**: estructura semántica, diseño visual, interactividad, mapas (Leaflet), reproductores, Web Audio API.
- **Backend (FastAPI)**: API, lógica de negocio, validación, procesamiento científico, sonificación, consultas geográficas, integraciones.
- **Base de datos (Supabase)**: PostgreSQL, Auth, Storage, RLS. PostGIS a evaluar.
- **Fuentes externas**: NASA POWER (datos científicos), OpenStreetMap (cartografía), Freesound/Xeno-canto/Archivo (audio, a verificar).

## Flujo principal

1. El usuario explora el catálogo o el mapa.
2. El frontend consulta la API FastAPI.
3. FastAPI consulta Supabase y/o fuentes científicas.
4. Los parámetros musicales se entregan al frontend.
5. Web Audio API reproduce y mezcla las capas.

## Módulos backend propuestos

- `app/api` — rutas y controladores.
- `app/core` — configuración, seguridad, logging.
- `app/models` — modelos ORM.
- `app/schemas` — esquemas Pydantic.
- `app/services` — lógica de negocio.
- `app/geographic` — consultas geográficas y búsqueda por radio.
- `app/scientific` — adaptadores de fuentes científicas.
- `app/sonification` — motor de sonificación.

## Riesgos iniciales

- Dependencia de fuentes externas y sus límites de uso.
- Precisión geográfica variable en grabaciones.
- Rendimiento del mapa con muchos marcadores (clustering).
- Licencias de audio y datos.
- Accesibilidad en mapas interactivos.

## Estado

Etapa 0: definición inicial. Pendiente de revisión del propietario.
