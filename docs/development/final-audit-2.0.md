# Auditoría final — Earth Jukebox 2.0

## 1. Alcance

Auditoría técnica, visual, funcional y de rendimiento del estado actual del proyecto en la rama `redesign/earth-jukebox-2.0`.

## 2. Estado de etapas

| Etapa | Estado |
|---|---|
| Etapa 3 — Diseño y landing | Parcial (T3.1, T3.2 completas; T3.3 pendiente) |
| Etapa 4 — Biblioteca sonora | Completada |
| Etapa 5 — Mapa y laboratorio | Completada (verificación de navegador pendiente) |
| Etapa 6 — Optimización | Completada |

## 3. Verificaciones ejecutadas

- Backend pytest: **18 passed, 2 skipped**.
- Importación de módulos JS: `node --check` sin errores.
- Endpoint `/api/scientific/sonify` (local y desplegado): 200 OK.
- Supabase: login, favoritos y composiciones verificados manualmente (OK).
- Caché científica: implementada en código; no se midió hit rate en producción.

## 4. Funcionalidades verificadas

- API de salud, sonidos, categorías, geografía, ciencia, comparación, auth, favoritos, composiciones.
- Paginación del catálogo.
- Validación de ingesta.
- Caché de NASA POWER.
- Guardado/recuperación de composiciones con sesión.

## 5. Funcionalidades no verificadas (sin navegador real)

- Reproducción de audio en el navegador.
- Mapa interactivo (zoom, marcadores, clustering).
- Flujo mapa → laboratorio.
- Responsive y accesibilidad con lector de pantalla.
- Carrusel automático.

## 6. Problemas encontrados

1. **Mapa sin marcadores reales**: no hay grabaciones con coordenadas verificables. Estado vacío honesto.
2. **Audio URL HEAD 403**: Wikimedia bloquea HEAD sin User-Agent; la reproducción en navegador usa GET (no probado).
3. **Columna `source` en BD**: la migración se actualizó, pero la BD actual puede no tenerla. Ejecutar `ALTER TABLE natural_sounds ADD COLUMN IF NOT EXISTS source text;`.
4. **Sin rate limiting**: endpoints de auth sin protección contra fuerza bruta.
5. **Sin tests frontend**: no hay pruebas automatizadas de UI.
6. **Canvas visualization** corre con `requestAnimationFrame` siempre (menor impacto).

## 7. Correcciones realizadas en esta auditoría

- Ajustado `netlify.toml` para no cachear `config.js` por 1 año (TTL 5 min).

## 8. Rendimiento

- Caché de NASA POWER: TTL 1 hora.
- Imágenes con `loading="lazy"`.
- Cabeceras de caché en Netlify para JS/CSS.
- No se midieron métricas Lighthouse (pendiente).

## 9. Seguridad

- Sin credenciales en el repo.
- RLS implementado.
- CORS restringido al frontend desplegado.
- Service role solo en backend.

## 10. Riesgos pendientes

- Falta de contenido real con coordenadas verificables.
- Falta de pruebas en navegador.
- Falta de CI/CD con pruebas automáticas.
- Rate limiting no implementado.

## 11. Conclusión

El proyecto está en buen estado técnico para una versión 2.0 beta. Las funcionalidades backend están verificadas. La experiencia de usuario en navegador requiere pruebas manuales antes de declarar la versión lista para producción.

**Recomendación**: ejecutar pruebas manuales en navegador (audio, mapa, responsive) y añadir al menos 3 grabaciones con coordenadas verificables para demostrar el mapa.