# Guía de despliegue — Earth Jukebox

## 1. Preparar variables de entorno

Backend (en el proveedor o `.env` local):
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`
- `CORS_ORIGINS` = URL del frontend desplegado (ej. `https://earth-jukebox.netlify.app`)
- `NASA_POWER_BASE_URL=https://power.larc.nasa.gov/api`

Frontend: edita `frontend/config.js`:
```js
window.EJ_API_BASE = "https://tu-backend.onrender.com";
```

## 2. Backend (FastAPI) — Render (ejemplo)

1. Sube el repo a GitHub.
2. En Render → New → Web Service → conecta el repo.
3. Root directory: `backend`.
4. Build command: `pip install -r requirements.txt`.
5. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
6. Añade las variables de entorno en el panel.
7. Deploy.

Alternativa: Railway (similar).

## 3. Frontend (estático) — Netlify/Vercel

1. En Netlify → Add new site → Import from Git (o drag & drop la carpeta `frontend/`).
2. Publish directory: `frontend`.
3. Deploy.

## 4. Base de datos

Aplica `database/migrations/0001_initial_schema.sql` en Supabase (SQL Editor).

## 5. Verificación post-despliegue

- `https://tu-backend/health` o `/api/health` → `{"status":"ok"}`.
- Abrir frontend → probar login, catálogo, mapa, sonificación.
- Revisar CORS si hay errores de red.

## 6. Seguridad

- No subir `.env`.
- La `service_role` solo en el backend.
- Revisar RLS en Supabase.