---
name: 09-performance
description: Directs actor behavior through objective, obstacle, tactic, beat, subtext, gaze, breath, posture, gesture, tempo, interpersonal distance, and emotional continuity.
version: 0.1.0
stage: production
---

# Performance Director

## Trigger
Use this skill whenever the request materially involves performance director in an AI film, commercial, trailer, music video, branded short, or narrative video workflow.

## Inputs
Accept any combination of brief, script, treatment, bibles, references, shotlist, generated clips, edit notes, audio, QC findings, and delivery requirements. If a missing input would change the result, flag it as a blocker rather than inventing canon.

## Outputs
Return a production artifact that can be consumed by the next stage. Use stable IDs, explicit assumptions, actionable decisions, state changes, and acceptance criteria.

## Performance model
For each beat specify: objective, obstacle, tactic, subtext, emotional value at start/end, gaze target, breath, posture, hand activity, micro-expression, tempo, interpersonal distance, and reaction behavior.

Avoid generic instructions such as “acts emotional.” Translate emotion into visible, playable behavior. Preserve performance continuity between adjacent shots.


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
