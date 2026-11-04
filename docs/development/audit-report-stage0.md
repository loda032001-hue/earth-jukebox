# Informe de auditoría — Etapa 0 (Earth Jukebox)

## 1. Entorno de trabajo

- Directorio del proyecto: `C:\Users\LENIN\Documents\eart jukebox` (vacío al inicio).
- Sistema: Windows (win32).
- Python: 3.13.15.
- Node.js: v24.22.1.
- Git: 2.55.0.
- Docker: 29.8.0 (Compose v5.5.1).
- OpenCode: 2.2.0 (CLI en `AppData\Local\Programs\ai.opencode.desktop\resources\opencode-cli.exe`).
- Internet: disponible.
- npm: bloqueado por política de ejecución de PowerShell; usar `cmd /c npm` o ajustar política si se requiere.
- No se encontró `supabase` CLI ni `psql` ni `ffmpeg`. Supabase se puede usar vía cloud o Docker.

## 2. Dependencias Python disponibles

Instaladas: FastAPI 0.141.1, Uvicorn 0.53.0, Pydantic 2.13.5, httpx, requests, SQLAlchemy, asyncpg, psycopg2-binary, alembic, pytest, numpy, scipy, supabase/postgrest, python-dotenv, Jinja2.

No instaladas (requerirán justificación al instalar): Librosa, SoundFile, Shapely/GeoPandas, geopy, leaflet (frontend).

## 3. OpenCode — agentes

- Configuración global en `~/.config/opencode/opencode.jsonc` (mínima, solo schema).
- Agentes se definen como archivos Markdown en `.opencode/agents/` (o global). Frontmatter V2. No usar campos legacy (`temperature`, `top_p`, `prompt`, `permission`, `tools`, `disable`, `maxSteps`).
- Se crearon los siete agentes especializados en `.opencode/agents/`.

## 4. Arquitectura propuesta

Ver `docs/architecture/`. Resumen:

- Backend FastAPI (Python) con módulos: api, core, models, schemas, services, geographic, scientific, sonification.
- Frontend HTML/CSS/JS con scripts organizados (map, audio, api).
- Supabase (PostgreSQL + Auth + Storage). PostGIS a evaluar.
- Mapas: Leaflet + OpenStreetMap (raster) respetando política de tiles.
- Audio: Web Audio API.

## 5. Estructura de carpetas

Ver prompt maestro (sección 13). Se creó la estructura inicial en el repositorio.

## 6. Estrategia geográfica

- MVP: lat/lon con índices y Haversine para radio.
- Futuro: PostGIS (ST_DWithin, índices GiST).
- Identificar precisión: exact / approximate / region / unconfirmed.
- No inventar coordenadas. Regiones sin grabaciones muestran mensaje claro.

## 7. Fuentes científicas iniciales

- NASA POWER API (sin API key) como adaptador inicial. Datos meteorológicos/solares.
- NOAA CDO (requiere token).
- Otras a investigar: NOAA CO-OPS, instituciones oceanográficas, repositorios abiertos.

## 8. Fuentes de audio iniciales

- Freesound.org (API v2, CC, API key).
- Xeno-canto (aves, CC, API key).
- Internet Archive (PD/CC).
- NOAA Ocean Acoustics / PMEL (verificar).
- Wikimedia Commons (CC por archivo).

## 9. MVP (Etapa 1–3)

1. Proyecto arranca (backend + frontend estático).
2. Landing page con identidad visual.
3. Catálogo de sonidos con metadatos y reproductor (datos iniciales verificados).
4. Mapa Leaflet con marcadores reales (subset) y clustering.
5. Búsqueda por radio y filtros básicos.
6. Ficha de grabación y reproducción desde el mapa.

## 10. Riesgos técnicos

- Dependencia de fuentes externas y límites de uso.
- Precisión geográfica variable.
- Rendimiento del mapa con muchos marcadores.
- Licencias de audio/datos.
- Accesibilidad en mapas.
- Disponibilidad de tiles OSM (best-effort, sin SLA).

## 11. Decisiones pendientes de aprobación

- Versión de Leaflet (1.x estable vs 2.0 beta).
- Uso de PostGIS vs Haversine en MVP.
- Selección de proveedor de tiles alternativo si se requiere mayor capacidad.
- Prioridad de fuentes científicas (NASA POWER primero).

## 12. Próxima etapa

Etapa 1: Fundación (estructura ejecutable, FastAPI, frontend inicial, Supabase preparado, migraciones, pruebas básicas). Esperar revisión del propietario.
