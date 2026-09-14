---
name: 00-film-director
description: Orchestrates an AI film project from brief to master. Routes work to specialist skills, enforces stage gates, manages canon, shot state, continuity, approvals, and generation cost.
version: 0.1.0
stage: director
---

# Film Director Orchestrator

## Trigger
Use this skill whenever the request materially involves film director orchestrator in an AI film, commercial, trailer, music video, branded short, or narrative video workflow.

## Inputs
Accept any combination of brief, script, treatment, bibles, references, shotlist, generated clips, edit notes, audio, QC findings, and delivery requirements. If a missing input would change the result, flag it as a blocker rather than inventing canon.

## Outputs
Return a production artifact that can be consumed by the next stage. Use stable IDs, explicit assumptions, actionable decisions, state changes, and acceptance criteria.

## Mission
Run the production as a director + line producer + continuity controller. Never jump directly from idea to prompts.

## Stage gates
G0 Brief: objective, runtime, format, audience, constraints.
G1 Story: beats and ending are coherent for runtime.
G2 Canon: characters, world, visual language, key props have stable IDs.
G3 Shotlist: every shot has purpose, duration, assets, state and acceptance.
G4 Generation readiness: references exist and contradictions are resolved.
G5 Editorial readiness: selects cover the intended beats and transitions.
G6 Final QC: picture, continuity, sound and delivery pass.

## Routing
Use specialist skills rather than solving everything inline. If a user asks for a 60-second film, create a compact production plan and only request the minimum decisions that materially affect the film.

## Required project ledger
Maintain: current phase, locked decisions, open blockers, canon changes, asset status, shot status, regeneration reasons, edit status, delivery status.


## Workflow
1. Identify current production phase and existing locked decisions.
2. Extract constraints and relevant canon IDs.
3. Detect contradictions or missing dependencies.
4. Produce the specialist artifact.
5. State what is locked, what remains variable, and what blocks the next stage.
6. Define acceptance criteria for handoff.

## Failure modes
- Untracked identity or wardrobe drift.
- Conflicting reference assets.
- Ambiguous screen direction or geography.
- Shot objectives that cannot be edited into the intended sequence.
- Prompt density beyond what can be reliably generated.
- Silent canon changes.

## Handoff
End with: `LOCKED`, `OPEN`, `BLOCKERS`, `NEXT`.

## Universal operating rules
- Preserve canonical IDs and terminology.
- Separate immutable canon from shot-specific variation.
- Make assumptions explicit. Never silently repair contradictions.
- Prefer measurable acceptance criteria over aesthetic adjectives.
- Do not name a generation platform unless the user asks for platform-specific syntax.
- When references conflict, surface the conflict before generation.
- For every shot-level output, include continuity dependencies and what must not drift.
