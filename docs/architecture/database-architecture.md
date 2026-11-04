# Arquitectura de base de datos

## Tecnología

Supabase: PostgreSQL + Auth + Storage. Evaluar PostGIS para geografía.

## Entidades iniciales

- `profiles`
- `sound_categories`
- `natural_sounds`
- `sound_sources`
- `scientific_datasets`
- `dataset_variables`
- `sonification_rules`
- `sonification_sessions`
- `compositions`
- `composition_layers`
- `favorites`
- `user_projects`

## Campos geográficos obligatorios en `natural_sounds`

- `latitude`
- `longitude`
- `country`
- `region`
- `continent`
- `ecosystem`
- `location_precision` (exact / approximate / region / unconfirmed)
- `coordinate_source`

## Estrategia geográfica

- MVP: lat/lon con índices y cálculo Haversine para radio.
- Futuro: PostGIS (ST_DWithin, índices GiST) para búsquedas por proximidad.

## Seguridad

- RLS por usuario.
- Migraciones versionadas en `database/migrations/`.
- `.env` para credenciales; `.env.example` sin valores reales.
