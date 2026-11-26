# HeatGuard AI – Milestone 2 Working Package (G15)

**Status: WORKING DRAFT – NOT READY TO SUBMIT.** This package consolidates the supplied offline prototype, prompt versions, prompt sheets, synthetic test plan, experiment observations and draft documentation.

## Project scope
HeatGuard AI drafts heat-wave public-health advisories from forecast information supplied by a user. It has three prompt workflows: (1) advisory generation, (2) audience adaptation, and (3) output review. It must not invent forecast facts, conceal uncertainty, present drafts as official warnings, or replace official local guidance.

## Important prototype distinction
The included `backend.py`, `heatguard.py` and `static/index.html` are an offline prototype. Their generated advisory is rule-based mock output, not Gemini output. The Gemini experiments were run separately in Google AI Studio. Do not describe the local backend as Gemini-integrated.

## Run the local prototype
From this folder: `python backend.py`, then open `http://127.0.0.1:8000`. This demonstrates the offline prompt-building/mock-review interface only.

## Folder structure
- `prompts/v1`, `prompts/v2`, `prompts/v3`: recovered prompt versions (V1/V2 reconstructed from screenshots/conversation; verify against originals).
- `prompts/final`: three prompt sheets/templates.
- `test-data`: 10 synthetic cases and execution tracker.
- `tests`: rubric and nine qualitative run notes.
- `docs/diagrams`: four Mermaid diagrams.
- `report`: seven-section Milestone 2 report draft.
- `supporting-document`: technical report draft.

## Before submission
1. Confirm team name, Team ID, batch, faculty guide, members/enrollment numbers and contribution percentages.
2. Confirm exact Gemini model name and settings from AI Studio.
3. Execute at least 10 test inputs (including at least 3 edge/invalid cases), save actual outputs, complete expected/actual/pass-fail table and numeric rubric scores.
4. Add 2–3 genuine AI Studio run screenshots with test numbers.
5. Verify V1/V2 exact text and add the full V1/V2/V3 iteration log.
6. Add real prototype/repository/reel links and test them in incognito.
7. Record 90–150 second reel.
8. Obtain team agreement and confirm faculty late-submission permission.

No test outputs, scores, team details, links, faculty approval or video have been fabricated in this package.
