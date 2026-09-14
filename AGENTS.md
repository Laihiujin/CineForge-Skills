# Agent Entry Point

Use `skills/00-film-director/SKILL.md` as the default router for any film, commercial, music-video, cinematic social, trailer, branded short, or narrative-video request.

Operating rules:
- Never generate shots before required canon and continuity artifacts exist.
- Prefer stable IDs: `CHAR-*`, `LOC-*`, `PROP-*`, `SC-*`, `SH-*`, `AST-*`.
- Every shot must declare purpose, duration, inherited state, state delta, references, prompt payload, and acceptance criteria.
- Specialists may propose changes to canon but may not silently mutate canon.
- Record unresolved contradictions as blockers.
- Keep the system vendor-neutral unless the user explicitly requests a model-specific adapter.
- Use `schemas/` and `templates/` as the contract for artifacts.
