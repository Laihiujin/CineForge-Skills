---
name: 14-video-generation
description: Builds model-agnostic video prompts for single shots and timed multi-shot sequences, with motion, camera, performance, continuity, first/last frame, audio intent, and failure-avoidance constraints.
version: 0.1.0
stage: generation
---

# Video Generation Director

## Trigger
Use this skill whenever the request materially involves video generation director in an AI film, commercial, trailer, music video, branded short, or narrative video workflow.

## Inputs
Accept any combination of brief, script, treatment, bibles, references, shotlist, generated clips, edit notes, audio, QC findings, and delivery requirements. If a missing input would change the result, flag it as a blocker rather than inventing canon.

## Outputs
Return a production artifact that can be consumed by the next stage. Use stable IDs, explicit assumptions, actionable decisions, state changes, and acceptance criteria.

## Prompt architecture
Use this order when useful: scene/mood → subjects → spatial map → continuity locks → action/performance → camera → temporal beats/cuts → end-frame requirement → environment → diegetic sound → realism/failure constraints.

For multi-shot generation, timestamp cuts and keep each sub-shot simple. For continuity-sensitive shots, explicitly define first-frame inheritance and last-frame handoff. Never overload a shot with independent actions that compete for model attention.


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
