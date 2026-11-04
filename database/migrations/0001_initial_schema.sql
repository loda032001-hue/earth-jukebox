-- Earth Jukebox - migración inicial
-- Ejecutar en Supabase (PostgreSQL). PostGIS es opcional y se evalúa en etapas posteriores.

-- Extensiones
create extension if not exists "pgcrypto";

-- Perfiles de usuario
create table if not exists profiles (
  id uuid primary key default gen_random_uuid(),
  user_id uuid unique,
  display_name text,
  preferences jsonb default '{}'::jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Categorías de sonidos
create table if not exists sound_categories (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  name text not null,
  description text,
  created_at timestamptz default now()
);

-- Fuentes de audio
create table if not exists sound_sources (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  url text,
  license text,
  source_type text,
  created_at timestamptz default now()
);

-- Grabaciones naturales
create table if not exists natural_sounds (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  category_id uuid references sound_categories(id) on delete set null,
  source_id uuid references sound_sources(id) on delete set null,
  description text,
  image_url text,
  audio_url text,
  duration_seconds integer,
  -- Información geográfica obligatoria
  latitude double precision,
  longitude double precision,
  country text,
  region text,
  continent text,
  ecosystem text,
  location_precision text check (location_precision in ('exact','approximate','region','unconfirmed')),
  coordinate_source text,
  recorded_at date,
  author text,
  source text,
  license text,
  scientific_info text,
  tags text[] default '{}',
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create index if not exists idx_natural_sounds_category on natural_sounds(category_id);
create index if not exists idx_natural_sounds_location on natural_sounds(latitude, longitude);
create index if not exists idx_natural_sounds_country on natural_sounds(country);

-- Conjuntos de datos científicos
create table if not exists scientific_datasets (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  provider text,
  url text,
  description text,
  license text,
  created_at timestamptz default now()
);

create table if not exists dataset_variables (
  id uuid primary key default gen_random_uuid(),
  dataset_id uuid references scientific_datasets(id) on delete cascade,
  name text not null,
  unit text,
  description text,
  created_at timestamptz default now()
);

-- Reglas de sonificación
create table if not exists sonification_rules (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  variable_id uuid references dataset_variables(id) on delete set null,
  musical_parameter text not null,
  rule_description text,
  created_at timestamptz default now()
);

-- Sesiones de sonificación
create table if not exists sonification_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid,
  dataset_id uuid references scientific_datasets(id) on delete set null,
  parameters jsonb default '{}'::jsonb,
  created_at timestamptz default now()
);

-- Composiciones
create table if not exists compositions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid,
  name text not null,
  description text,
  data jsonb default '{}'::jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create table if not exists composition_layers (
  id uuid primary key default gen_random_uuid(),
  composition_id uuid references compositions(id) on delete cascade,
  layer_type text not null,
  parameters jsonb default '{}'::jsonb,
  volume double precision default 1.0,
  enabled boolean default true,
  created_at timestamptz default now()
);

-- Favoritos
create table if not exists favorites (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null,
  sound_id uuid references natural_sounds(id) on delete cascade,
  created_at timestamptz default now(),
  unique (user_id, sound_id)
);

-- Proyectos de usuario
create table if not exists user_projects (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null,
  name text not null,
  data jsonb default '{}'::jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Row Level Security (RLS)
alter table profiles enable row level security;
alter table favorites enable row level security;
alter table compositions enable row level security;
alter table composition_layers enable row level security;
alter table user_projects enable row level security;
alter table sonification_sessions enable row level security;

-- Políticas básicas: el usuario solo accede a sus propios datos
create policy "profiles_own" on profiles for all using (auth.uid() = user_id);
create policy "favorites_own" on favorites for all using (auth.uid() = user_id);
create policy "compositions_own" on compositions for all using (auth.uid() = user_id);
create policy "composition_layers_own" on composition_layers for all using (
  exists (select 1 from compositions c where c.id = composition_id and c.user_id = auth.uid())
);
create policy "user_projects_own" on user_projects for all using (auth.uid() = user_id);
create policy "sonification_sessions_own" on sonification_sessions for all using (auth.uid() = user_id);

-- Lectura pública de catálogos
alter table sound_categories enable row level security;
alter table natural_sounds enable row level security;
alter table sound_sources enable row level security;
alter table scientific_datasets enable row level security;
alter table dataset_variables enable row level security;
alter table sonification_rules enable row level security;

create policy "sound_categories_read" on sound_categories for select using (true);
create policy "natural_sounds_read" on natural_sounds for select using (true);
create policy "sound_sources_read" on sound_sources for select using (true);
create policy "scientific_datasets_read" on scientific_datasets for select using (true);
create policy "dataset_variables_read" on dataset_variables for select using (true);
create policy "sonification_rules_read" on sonification_rules for select using (true);
