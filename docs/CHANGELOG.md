# CHANGELOG

## [Unreleased]

### Etapa 0 — Auditoría y planificación
- Estructura de carpetas inicial.
- Documentación inicial.
- Definición de agentes especializados.
- Investigación preliminar de fuentes científicas y de audio.
- Definición de MVP y riesgos.

### Etapa 1 — Fundación (completada)
- Backend FastAPI con configuración tipada, CORS y endpoint /health.
- Cliente Supabase preparado (sin credenciales).
- Frontend inicial (landing) con identidad visual.
- Migración SQL inicial con esquema geográfico.
- Servicios placeholder (geografía, NASA POWER, sonificación).
- Pruebas básicas (2 pasadas).

### Etapa 2 — Interfaz principal (completada)
- Landing inmersiva con hero y carrusel accesible.
- Navegación consistente y páginas placeholder.
- Responsive y accesibilidad inicial.

### Etapa 3 — Sonidos y Explorador (completada)
- Catálogo de sonidos con filtros, metadatos y reproductor.
- API de sonidos, categorías y geografía.
- Mapa Leaflet con búsqueda por radio y panel de resultados.
- Registros iniciales verificados (Wikimedia Commons).

### Etapa 4 — Motor científico (completada)
- Adaptador NASA POWER con validación y limpieza.
- Motor de sonificación con normalización y reglas.
- Endpoint /api/scientific/sonify.
- UI básica de sonificación.

### Etapa 5 — Música de la Tierra (completada)
- Laboratorio musical con Web Audio API.
- Capas activables y mezclador.
- Controles de reproducción.
- Visualización de frecuencias.
- Persistencia local de composiciones.

### Etapa 6 — Usuarios y proyectos (completada)
- Endpoints de autenticación Supabase.
- Favoritos y composiciones persistentes.
- RLS en migración SQL.
- Páginas de cuenta, favoritos y composiciones.

### Etapa 7 — Comparación y accesibilidad (completada)
- Endpoint de comparación científica.
- Página de comparación.
- Mejoras de accesibilidad (foco visible, aria-live).

### Etapa 8 — Validación final (completada)
- 15 tests pasando.
- Revisión de seguridad y dependencias.
- Documentación final.
- Preparación para despliegue.
