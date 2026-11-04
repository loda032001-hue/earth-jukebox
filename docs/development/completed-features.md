# Funcionalidades terminadas

Etapa 0 completada: planificación y documentación inicial.

Etapa 1 (fundación) completada:
- Backend FastAPI funcional con endpoint /health.
- Frontend inicial con identidad visual básica.
- Migración SQL inicial con esquema geográfico.
- Pruebas básicas (2 pasadas).

Etapa 2 (interfaz principal) completada:
- Landing inmersiva con hero, carrusel accesible y secciones.
- Navegación consistente entre páginas placeholder.
- Responsive y preferencia de movimiento reducido.
- Accesibilidad inicial (skip link, nav, aria).

Etapa 3 (sonidos y explorador) completada:
- Catálogo de sonidos con metadatos, filtros y reproductor.
- API de sonidos y categorías.
- Explorador geográfico con Leaflet, búsqueda por radio y panel de resultados.
- Registros iniciales verificados (Wikimedia Commons), sin coordenadas inventadas.

Etapa 4 (motor científico) completada:
- Adaptador NASA POWER (daily, point) con validación y limpieza de fill values.
- Motor de sonificación con normalización y reglas de mapeo documentadas.
- Endpoint /api/scientific/sonify con trazabilidad.
- UI básica para sonificar datos.

Etapa 5 (Música de la Tierra) completada:
- Laboratorio musical con Web Audio API.
- Capas activables con volumen individual.
- Controles de reproducción, pausa, detención.
- Visualización de frecuencias.
- Guardar/recuperar composiciones en localStorage.

Etapa 6 (usuarios y proyectos) completada:
- Endpoints de autenticación (signup/login/me) con Supabase.
- Favoritos y composiciones persistentes (Supabase).
- RLS en migración SQL.
- Páginas de cuenta, favoritos y composiciones.

Etapa 7 (comparación y accesibilidad) completada:
- Endpoint de comparación científica entre periodos/ubicaciones.
- Página de comparación.
- Mejoras de accesibilidad (foco visible, skip links, aria-live).

Etapa 8 (validación final) completada:
- 15 tests pasando.
- Revisión de seguridad (sin credenciales).
- Documentación final actualizada.
- Preparación para despliegue documentada.
