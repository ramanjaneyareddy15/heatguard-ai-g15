# Code version audit — 26 November 2026

## Current implementation
1. The repository contains the Python backend, rule-based generator, browser UI, prompt templates, synthetic data, tests, diagrams and project documentation.
2. The browser interface exposes exactly two prompt-selector options: Baseline and Structured.
3. The backend accepts only `baseline` and `structured` in `POST /api/generate`.
4. The generator returns rule-based mock output and marks it `is_mock: true`; no live LLM call is made.
5. The reviewer uses limited heuristics and is not semantic hallucination detection.
6. No live-weather API is integrated.
7. P1 Advisory Generation, P2 Audience Adaptation and P3 Output Review are documented as workflow tasks, not as three prompt-selector options.

## Version 2.0.1 documentation alignment
- Removed the obsolete third prompt-version artifact.
- Removed the third-version experiment-log rows.
- Aligned project documentation, prompt sheets, diagrams, rubric and submission checklist with the two-option interface.

## Version 2.0.0 runtime
- Added `/health` for service health reporting.
- Added `/api/version` for application version and integration-status reporting.
- Updated Render deployment configuration.

## Verification scope
The previous local smoke test checked the homepage, health, version, sample cases and generation endpoint. It returned HTTP 200 and `is_mock: true`. This does not establish model inference, factual correctness, advisory quality or completion of every required model experiment.

## Deployment
Render previously reported the v2.0.0 deployment as Live from commit `eb989214`. The documentation-alignment commit must complete a new Render deployment before the live site can be called updated.
