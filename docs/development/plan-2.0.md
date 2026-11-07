# Plan de implementación — Earth Jukebox 2.0

Referencia: `docs/development/audit-2.0.md`.

Regla: no se modifica código hasta aprobar este plan. No se eliminan funcionalidades existentes. No se inventan datos.

---

## 1. Biblioteca sonora — estructura de datos

### Objetivo
Registrar grabaciones reales con procedencia verificable y permitir ampliar el catálogo sin tocar código.

### Estructura de datos (Supabase / JSON de ingesta)
Entidad `natural_sounds` (ya existe) con campos:
- `id` (uuid)
- `name`
- `category_id` (FK a `sound_categories`)
- `description`
- `image_url`
- `audio_url`
- `duration_seconds`
- `country`, `region`, `continent`, `ecosystem`
- `location_precision` (`exact` | `approximate` | `region` | `unconfirmed`)
- `coordinate_source` (obligatorio si hay coordenadas)
- `latitude`, `longitude` (solo si verificables)
- `recorded_at`
- `author`
- `source` (fuente original)
- `license`
- `scientific_info`
- `tags`

### Ingesta sin modificar código
- Crear una tabla de staging `sound_ingest` (CSV/JSON) o un endpoint de importación protegido por service role.
- Script `backend/scripts/import_sounds.py` que valide y upsert en `natural_sounds`.
- Validaciones: campos obligatorios, licencia no vacía, coordenadas solo si `location_precision` != `unconfirmed`, `coordinate_source` documentado.
- Fuentes candidatas (a verificar licencias): Freesound (API), Xeno-canto (aves), Wikimedia Commons, Internet Archive.
- Nunca se insertan grabaciones sin fuente y licencia.

### Tareas
1. **T1.1 — Script de ingesta**  
   - Qué: crear `backend/scripts/import_sounds.py` que lea JSON/CSV y upsert en Supabase.  
   - Por qué: ampliar catálogo sin tocar código.  
   - Archivos: `backend/scripts/import_sounds.py`, `docs/tutorials/data-ingestion-guide.md`.  
   - Dependencias: Supabase service role.  
   - Verificación: importar 1 grabación de prueba y consultar `/api/sounds`.

2. **T1.2 — Validación de metadatos**  
   - Qué: validaciones en el script (campos obligatorios, precisión geográfica).  
   - Por qué: evitar datos incompletos.  
   - Archivos: `backend/scripts/import_sounds.py`.  
   - Verificación: intentar importar registro inválido y confirmar rechazo.

3. **T1.3 — Paginación del catálogo**  
   - Qué: añadir `limit`/`offset` a `/api/sounds`.  
   - Por qué: rendimiento con catálogos grandes.  
   - Archivos: `backend/app/api/sounds.py`, `backend/app/schemas/sound.py`.  
   - Verificación: pruebas con `limit` y `offset`.

---

## 2. Mapa mundial — representación y accesibilidad

### Objetivo
Mapa interactivo real con marcadores solo para grabaciones con coordenadas verificables, más alternativa accesible.

### Diseño
- **Tecnología**: Leaflet 1.9.4 + OpenStreetMap raster (mantener). Evaluar vector tiles en el futuro.
- **Capas**: continentes (polígonos opcionales), países (GeoJSON simplificado), marcadores de grabaciones.
- **Clustering**: Leaflet.markercluster cuando haya > 50 marcadores.
- **Selección de región**: clic en mapa → consulta `/api/geo/search` con radio configurable.
- **Panel lateral**: nombre, descripción, metadatos, reproductor, precisión geográfica.
- **Precisión**: marcadores diferenciados por icono/color según `location_precision`. Si `unconfirmed`, no se muestra marcador.
- **Sin resultados**: mensaje "No tenemos grabaciones verificadas disponibles para esta región todavía".
- **Accesibilidad**: 
  - Lista alternativa de ubicaciones (tabla) navegable por teclado.
  - Atributos ARIA en el mapa y controles.
  - Atajos de teclado (flechas para mover, Enter para seleccionar).
  - `role="application"` con instrucciones de uso.

### Tareas
4. **T2.1 — Clustering en el mapa**  
   - Qué: integrar `leaflet.markercluster` vía CDN.  
   - Por qué: evitar saturación con muchos marcadores.  
   - Archivos: `frontend/pages/explorer.html`, `frontend/scripts/pages/explorer.js`.  
   - Verificación: probar con > 50 marcadores simulados (solo en tests, no en producción).

5. **T2.2 — Panel de resultados rico**  
   - Qué: mostrar ficha completa con imagen, metadatos, reproductor.  
   - Por qué: experiencia informativa.  
   - Archivos: `frontend/scripts/pages/explorer.js`, `frontend/styles/main.css`.  
   - Verificación: clic en marcador muestra panel.

6. **T2.3 — Alternativa accesible (lista)**  
   - Qué: tabla/lista de grabaciones geolocalizadas navegable por teclado.  
   - Por qué: accesibilidad para lectores de pantalla.  
   - Archivos: `frontend/pages/explorer.html`, `frontend/scripts/pages/explorer.js`.  
   - Verificación: navegación completa sin mouse.

7. **T2.4 — Integración mapa → laboratorio**  
   - Qué: botón "Sonificar esta región" que pasa coordenadas al laboratorio.  
   - Por qué: conectar experiencias.  
   - Archivos: `frontend/scripts/pages/explorer.js`, `frontend/scripts/pages/music.js`.  
   - Verificación: seleccionar región y sonificar.

---

## 3. Identidad visual — estructura de la landing

### Objetivo
Landing inmersiva con la Tierra como protagonista, sin imágenes inventadas.

### Estructura propuesta
1. **Hero**: Tierra (imagen real o visualización Canvas/SVG) + mensaje principal "La Tierra tiene una banda sonora" + CTA "Comenzar a explorar".
2. **Carrusel de destacados**: grabaciones reales con imagen, nombre, ubicación, botón de reproducción.
3. **Dos experiencias**: tarjetas grandes para "Sonidos de la Tierra" y "Música de la Tierra".
4. **Cómo funciona**: 3 pasos (Explora → Escucha → Crea).
5. **Footer**: créditos, fuentes, licencias.

### Recursos gráficos
- Imágenes reales de Wikimedia Commons (Tierra, océanos, tormentas, etc.) con atribución.
- Iconografía SVG propia (ondas, frecuencias).
- Gradientes oscuros como fondo.
- Tipografía: sistema (Inter o similar) con jerarquía clara.

### Tareas
8. **T3.1 — Sistema de diseño**  
   - Qué: definir variables CSS (colores, tipografía, espaciado, sombras).  
   - Por qué: coherencia visual.  
   - Archivos: `frontend/styles/tokens.css`, `frontend/styles/main.css`.  
   - Verificación: aplicar tokens en todas las páginas.

9. **T3.2 — Landing inmersiva**  
   - Qué: rediseñar `index.html` con hero, carrusel de destacados, secciones.  
   - Por qué: primera impresión profesional.  
   - Archivos: `frontend/index.html`, `frontend/styles/main.css`, `frontend/scripts/main.js`.  
   - Verificación: carga correcta en desktop y móvil.

10. **T3.3 — Componentes reutilizables**  
    - Qué: extraer header, footer, card, player a `frontend/components/`.  
    - Por qué: evitar duplicación.  
    - Archivos: `frontend/components/*.js`, páginas HTML.  
    - Verificación: todas las páginas usan los mismos componentes.

---

## 4. Laboratorio musical — integración real

### Objetivo
Permitir sonificar datos ambientales reales y experimentar con capas, sin confundir datos científicos con decoración.

### Diseño
- **Fuentes de datos**: NASA POWER (temperatura, precipitación, viento) y futuras fuentes (NOAA, oceanográficas).
- **Flujo**:
  1. Seleccionar ubicación y periodo.
  2. Obtener datos (backend).
  3. Normalizar variables (backend).
  4. Aplicar reglas de mapeo (documentadas).
  5. Entregar parámetros al frontend.
  6. Web Audio API reproduce capas con esos parámetros.
- **Parámetros modificables**: volumen por capa, activación/desactivación, tempo general, selección de variable.
- **Visualización**: ondas y frecuencias reflejan el audio real, no datos inventados.
- **Transparencia**: mostrar qué variable se escucha y cómo se mapeó.

### Tareas
11. **T4.1 — Modulación en tiempo real**  
    - Qué: usar parámetros normalizados para modular frecuencia/amplitud de osciladores.  
    - Por qué: sonificación real.  
    - Archivos: `frontend/scripts/audio/engine.js`, `frontend/scripts/pages/music.js`.  
    - Verificación: cambiar datos y observar cambio en audio.

12. **T4.2 — Guardado de composiciones en Supabase**  
    - Qué: conectar el botón "Guardar" al endpoint `/api/compositions`.  
    - Por qué: persistencia real.  
    - Archivos: `frontend/scripts/pages/music.js`.  
    - Verificación: guardar y recuperar composición tras recargar.

13. **T4.3 — Guía de uso del laboratorio**  
    - Qué: añadir instrucciones y descripción de cada capa.  
    - Por qué: usabilidad.  
    - Archivos: `frontend/pages/music.html`.  
    - Verificación: revisión manual.

---

## 5. Rendimiento y arquitectura

### Objetivo
Optimizar carga, imágenes y consultas sin eliminar funcionalidades.

### Cambios propuestos
- **Imágenes**: servir desde Supabase Storage o CDN; usar `srcset` y `loading="lazy"`.
- **Caché**: cachear respuestas de NASA POWER en backend (TTL 1h) por coordenadas+periodo.
- **Minificación**: añadir build step (Vite o esbuild) para CSS/JS.
- **Lazy loading**: cargar Leaflet y Web Audio solo cuando se necesiten.
- **Service worker**: caché offline de assets estáticos (opcional, Etapa 6).
- **Monitoreo**: logs en Render, métricas básicas.

### Tareas
14. **T5.1 — Caché de datos científicos**  
    - Qué: cachear respuestas de NASA POWER en memoria o Supabase.  
    - Por qué: reducir latencia y llamadas externas.  
    - Archivos: `backend/app/scientific/nasa_power.py`, `backend/app/core/cache.py`.  
    - Verificación: segunda consulta más rápida.

15. **T5.2 — Optimización de imágenes**  
    - Qué: subir imágenes a Supabase Storage y usar URLs optimizadas.  
    - Por qué: rendimiento y control de assets.  
    - Archivos: `backend/scripts/upload_assets.py`, `frontend/scripts/pages/sounds.js`.  
    - Verificación: Lighthouse / inspección de red.

16. **T5.3 — Build step (opcional)**  
    - Qué: añadir Vite para minificar y bundlear.  
    - Por qué: rendimiento de producción.  
    - Archivos: `frontend/vite.config.js`, `package.json`.  
    - Verificación: build sin errores, assets minificados.

---

## 6. Plan de ejecución (tareas ordenadas)

| # | Tarea | Etapa | Prioridad |
|---|---|---|---|
| 1 | T1.1 Script de ingesta | 4 | Alta |
| 2 | T1.2 Validación de metadatos | 4 | Alta |
| 3 | T1.3 Paginación catálogo | 4 | Media |
| 4 | T2.1 Clustering mapa | 5 | Media |
| 5 | T2.2 Panel de resultados rico | 5 | Alta |
| 6 | T2.3 Alternativa accesible (lista) | 6 | Alta |
| 7 | T2.4 Integración mapa → laboratorio | 5 | Media |
| 8 | T3.1 Sistema de diseño | 3 | Alta |
| 9 | T3.2 Landing inmersiva | 3 | Alta |
| 10 | T3.3 Componentes reutilizables | 3 | Media |
| 11 | T4.1 Modulación en tiempo real | 5 | Alta |
| 12 | T4.2 Guardado de composiciones | 6 | Media |
| 13 | T4.3 Guía de uso del laboratorio | 5 | Baja |
| 14 | T5.1 Caché de datos científicos | 6 | Media |
| 15 | T5.2 Optimización de imágenes | 6 | Media |
| 16 | T5.3 Build step (opcional) | 6 | Baja |

### Orden sugerido de implementación
1. Etapa 3 (diseño y landing) — impacto visual inmediato.
2. Etapa 4 (biblioteca y datos) — contenido real.
3. Etapa 5 (mapa y audio) — funcionalidades centrales.
4. Etapa 6 (optimización y pruebas) — calidad y rendimiento.

### Verificación por etapa
- Cada etapa termina con pruebas (pytest + revisión manual).
- Actualización de `docs/CHANGELOG.md`, `docs/development/project-status.md`, `docs/development/completed-features.md`.
- No se declara terminado sin pruebas.

---

## 7. Reglas de implementación

1. No inventar datos, coordenadas, fuentes ni licencias.
2. No reemplazar funcionalidades reales por demostraciones visuales.
3. No eliminar código funcional sin justificarlo.
4. Conservar integraciones con Render, Netlify y Supabase.
5. No exponer credenciales.
6. Actualizar documentación después de cada etapa.
7. Informar qué se hizo, archivos modificados, qué funciona, qué queda pendiente y pruebas realizadas.

---

**Plan completo preparado.** Esperando aprobación para iniciar la Etapa 3 (rediseño de interfaz y navegación).