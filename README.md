# CineForge Skills

[中文](README_CN.md) · English

[![Validate](https://github.com/Laihiujin/CineForge-Skills/actions/workflows/validate.yml/badge.svg)](https://github.com/Laihiujin/CineForge-Skills/actions/workflows/validate.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**A vendor-neutral, production-grade skill library for AI filmmaking.**

CineForge treats AI video as filmmaking, not prompt roulette. The library turns a creative brief into a controlled production system with canon, state, shot logic, continuity, generation instructions, editorial intent, sound, finishing, and QC.

The core design principle is simple: **a model should never be asked to remember what the production system can explicitly track.** Identity, wardrobe, geography, light, props, performance state, screen direction, temporal state, and visual language are all written down and carried forward as production data.

## Pipeline

`Brief → Story → Script → Canon → Characters → World → Visual Language → Shotlist → References → Generation → Continuity → Edit → Sound → Color → QC → Master`

The `00-film-director` skill is the front door. Give it a concept, brief, script, treatment, reference set, or partially completed project. It decides which specialist to call, what artifact must exist before generation, and what must be approved before moving forward.

## What makes this different

CineForge is built around five production laws:

1. **Canon before generation.** Stable facts live in bibles, not in memory.
2. **State before prompts.** Every shot declares what changed and what must persist.
3. **Purpose before beauty.** Every shot has a dramatic or informational job.
4. **Continuity is a graph.** Shots depend on previous states, assets, eyelines, screen direction, and time.
5. **Generation is replaceable.** The creative system is model-agnostic so the same project can move between image/video models without rebuilding the film.

## Skill map

| Stage | Skills |
|---|---|
| Direction | `00-film-director` |
| Development | `01-creative-brief` · `02-story-development` · `03-screenplay` |
| Canon & pre-production | `04-story-bible` · `05-character-bible` · `06-world-bible` · `07-visual-language` |
| Production design & directing | `08-cinematography` · `09-performance` · `10-shotlist` · `11-continuity` · `12-reference-strategy` |
| Generation | `13-image-generation` · `14-video-generation` · `15-dialogue-lipsync` |
| Post | `16-vfx` · `17-sound-design` · `18-music` · `19-editorial` · `20-color-finishing` |
| Quality & delivery | `21-qc` · `22-delivery` |

## Project structure

```text
project/
├── 00-brief/
├── 01-story/
├── 02-script/
├── 03-canon/
│   ├── story-bible.md
│   ├── characters/
│   ├── locations/
│   └── visual-language.md
├── 04-assets/
│   ├── characters/
│   ├── locations/
│   ├── props/
│   └── style/
├── 05-shotlist/
├── 06-prompts/
├── 07-generations/
├── 08-audio/
├── 09-edit/
├── 10-qc/
└── 11-delivery/
```

## Installation

The repository uses the common `SKILL.md` convention. Copy individual skill folders into the skills directory supported by your agent, or keep this repository at project level and point your agent to `AGENTS.md` / `CLAUDE.md`.

```bash
git clone <your-repo-url>
cd CineForge-Skills
python3 scripts/validate_skills.py
python3 scripts/new_project.py my-film
```

## Start a film

Ask the orchestrator:

> Build a 60-second cinematic short from this concept. Start in director mode, establish canon before prompting, and do not allow generation until the shotlist and continuity gates pass.

Or enter at any specialist layer:

> Turn this scene into a shotlist with continuity dependencies and generation acceptance criteria.

> Lock this character from my references and create an identity/wardrobe consistency packet.

> Audit these clips for face drift, screen-direction errors, prop state, and bad first/last-frame transitions.

## Output philosophy

Skills should produce production artifacts, not inspirational prose. Tables, IDs, state deltas, acceptance criteria, reference maps, prompt payloads, and QC verdicts are preferred whenever they make the work more reproducible.

## Continuous development

CineForge Skills is continuously iterated and optimized. Production rules, schemas, templates, and model-adaptation guidance evolve with real-world filmmaking practice and generation technology.

## License

MIT. See `LICENSE`.
