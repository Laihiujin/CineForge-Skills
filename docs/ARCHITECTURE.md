# Architecture

CineForge separates **creative canon**, **shot state**, **generation payload**, and **evaluation**. This prevents prompt edits from accidentally rewriting story facts.

## Data layers
1. Canon: stable facts.
2. Asset registry: references that instantiate canon.
3. Scene state: state at scene boundaries.
4. Shot state: inherited state + delta + protected invariants.
5. Prompt payload: model-facing instructions.
6. Acceptance criteria: observable pass/fail conditions.
7. QC evidence: failure and fix history.

The director orchestrator may route among specialists, but only canon-producing skills can propose canonical changes. Continuity validates those changes before downstream use.
