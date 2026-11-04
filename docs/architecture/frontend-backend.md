# Arquitectura Frontend–Backend

## Principio

El frontend no duplica la lógica científica del backend. El backend procesa datos y entrega parámetros musicales listos para Web Audio API.

## Comunicación

- REST (JSON) sobre HTTP.
- El frontend usa `fetch` para consultar la API.
- Errores se devuelven con códigos HTTP y mensajes claros.

## Responsabilidades

### Frontend
- Estructura semántica (HTML5).
- Diseño visual y responsive (CSS3).
- Interactividad (JS).
- Mapa (Leaflet).
- Reproductor y laboratorio (Web Audio API).

### Backend
- Validación y lógica de negocio.
- Procesamiento científico y sonificación.
- Consultas geográficas.
- Gestión de usuarios y composiciones (vía Supabase).

## Seguridad

- No exponer claves privadas en frontend.
- CORS configurado.
- RLS en Supabase.
