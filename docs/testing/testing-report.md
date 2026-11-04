# Informe de pruebas — Earth Jukebox

## Ejecución final (Etapa 8)

- Backend: `pytest` → **15 passed**, 2 warnings (deprecaciones de librerías, no bloqueantes).
- Prueba de integración real: endpoint `/api/scientific/sonify` respondió correctamente contra NASA POWER.
- Prueba de servidor: Uvicorn arrancó y `/api/health` respondió `ok`.

## Cobertura por área

- Salud del servicio: 2 tests.
- Catálogo de sonidos: 4 tests.
- Geografía: 2 tests.
- Sonificación: 3 tests.
- Autenticación (sin Supabase): 2 tests.
- Comparación: 2 tests.

## Seguridad
- No se encontraron credenciales en el repositorio.
- `.env` ignorado por `.gitignore`.
- RLS definido en la migración SQL.

## Accesibilidad
- Skip links, nav semántica, foco visible, `aria-live`, `prefers-reduced-motion`.

## Responsive
- Layouts con CSS Grid/Flexbox y media queries (menú colapsable en móvil).

## Problemas conocidos
- Mapa sin marcadores reales por falta de coordenadas verificadas en los registros iniciales (estado vacío honesto).
- Leaflet 1.9.4 vía CDN (evaluar 2.0 en el futuro).

## Integración Supabase (verificada)
- Login, perfil, favoritos y composiciones funcionan contra Supabase real.
- RLS activo y migración aplicada.
