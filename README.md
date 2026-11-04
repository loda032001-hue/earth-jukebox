# Earth Jukebox

**Listen to the Planet. Discover the Science. Create with Nature.**

Earth Jukebox es una plataforma web que conecta ciencia, naturaleza y música mediante experiencias sonoras interactivas. Permite explorar grabaciones reales de la Tierra, consultar su contexto científico y transformar datos científicos en composiciones musicales.

## Estado del proyecto

Etapa actual: **Etapa 8 — Validación final completada** (prototipo funcional).

Todas las etapas del plan inicial han sido ejecutadas. El proyecto está listo para configurar credenciales (Supabase) y desplegar.

## Stack tecnológico

- Backend: Python + FastAPI
- Frontend: HTML5 + CSS3 + JavaScript (módulos ES)
- Audio: Web Audio API
- Base de datos: Supabase (PostgreSQL) + RLS + Storage
- Procesamiento científico: NumPy, SciPy (preparado)
- Mapas: Leaflet + OpenStreetMap
- Pruebas: Pytest

## Estructura del proyecto

```text
earth-jukebox/
├── backend/          # FastAPI, servicios, pruebas
├── frontend/         # HTML/CSS/JS, páginas, scripts
├── database/         # Migraciones SQL
├── docs/             # Documentación técnica
├── .env.example      # Variables de entorno (sin valores reales)
├── .gitignore
├── AGENTS.md
└── README.md
```

## Cómo ejecutar

### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### Frontend
Servir la carpeta `frontend/` como sitio estático (por ejemplo con `python -m http.server 5500` dentro de `frontend/`).

### Pruebas
```bash
cd backend
pytest -q
```

## Variables de entorno
Ver `.env.example`. Copiar a `.env` y rellenar:
- Supabase: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`.
- Fuentes científicas: `NASA_POWER_BASE_URL`.
- Fuentes de audio: `FREESOUND_API_KEY`, `XENO_CANTO_API_KEY` (opcional).

## Base de datos
Aplicar `database/migrations/0001_initial_schema.sql` en Supabase.

## Documentación
- `docs/development/project-status.md` — estado actual.
- `docs/development/audit-report-stage0.md` — auditoría inicial.
- `docs/testing/testing-report.md` — pruebas.
- `docs/decisions/technical-decisions.md` — decisiones.
- `docs/scientific-sources/` — fuentes y licencias.

## Agentes especializados
Ver `AGENTS.md` y `.opencode/agents/`.

## Licencias y fuentes
Ver `docs/scientific-sources/licenses.md`. Los datos y audios provienen de fuentes verificables (NASA POWER, Wikimedia Commons, etc.).
