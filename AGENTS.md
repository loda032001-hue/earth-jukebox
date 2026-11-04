# Earth Jukebox — Agentes especializados (OpenCode)

OpenCode v2.2.0. Los agentes se definen como archivos Markdown en `.opencode/agents/` (o globalmente en `~/.config/opencode/agents/`). Cada archivo usa frontmatter compatible con V2 (sin campos legacy como `temperature`, `top_p`, `prompt`, `permission`, `tools`, `disable`, `maxSteps`).

## Los siete agentes

1. `software-architect.md` — Arquitecto de software.
2. `backend-python.md` — Desarrollador backend Python.
3. `supabase-specialist.md` — Especialista Supabase.
4. `nasa-data-specialist.md` — Especialista en NASA y datos científicos.
5. `audio-sonification-engineer.md` — Ingeniero de audio y sonificación.
6. `qa-testing.md` — QA y pruebas.
7. `technical-tutor.md` — Tutor técnico.

## Uso

- Los agentes `subagent` se lanzan mediante la herramienta `subagent` de OpenCode.
- El agente `technical-tutor` puede ejecutarse como `primary` para explicar el proyecto.
- Permisos por agente se definen en el frontmatter.

## Nota

Los agentes se crean en Etapa 0 como definición inicial. Pueden ajustarse tras la revisión del propietario.
