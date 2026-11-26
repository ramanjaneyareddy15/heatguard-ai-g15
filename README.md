# HeatGuard AI — Prompt-Based Heat-Wave Public-Health Advisory Generator

**Team:** NovaNex | **Team ID:** PE-B01-44 | **Batch:** B01-B12  
**Faculty:** Sonal Kukreja | **University:** Bennett University

## Project overview
HeatGuard AI is a browser-based prototype for drafting heat-wave public-health advisories from forecast information supplied by a user. It accepts forecast text, optional location/period/warning level, audience, language and a word limit. It displays the filled prompt and a clearly labelled rule-based mock advisory.

## Supported prompt options
The application provides exactly two selectable prompt options:
- **Baseline** — concise source-grounding instructions, missing-information handling and a four-section advisory structure.
- **Structured** — more explicit source-grounding, audience/tone guidance, metadata handling, fixed headings and a final claim check.

No third prompt option is part of the current application. P1 Advisory Generation, P2 Audience Adaptation and P3 Output Review are workflow tasks, not additional selector choices.

## Actual implementation
- `backend.py` serves the browser interface and JSON API.
- `heatguard.py` loads sample cases, fills prompt templates and generates rule-based mock output.
- `static/index.html` exposes the Baseline and Structured choices.
- `/api/generate` accepts only `baseline` and `structured`, builds the selected prompt and returns `is_mock: true`.
- `/api/review` performs limited heuristic checks. It is not semantic hallucination detection.
- No Gemini/LLM API or live-weather API is integrated into the deployed Python prototype.

## API routes
- `GET /health` — service health and application version.
- `GET /api/version` — version and integration-status information.
- `GET /api/cases` — synthetic sample cases and supported audiences.
- `POST /api/generate` — builds the selected prompt and returns a rule-based mock advisory and heuristic review.
- `POST /api/review` — checks pasted output using limited heuristic rules.

## Run locally
```bash
python backend.py
```
Open `http://127.0.0.1:8000`. Render supplies the `PORT` environment variable.

## Main files
- `backend.py` — HTTP server, API, health and version endpoints.
- `heatguard.py` — sample-case loading, prompt filling and mock generation.
- `static/index.html` — browser interface.
- `prompts/baseline_prompt.txt` and `prompts/structured_prompt.txt` — the two supported prompt templates.
- `prompts/final/` — P1/P2/P3 workflow prompt sheets.
- `test-data/`, `tests/` — synthetic cases, test tracker and rubric.
- `docs/diagrams/` — workflow and design diagrams.
- `report/`, `supporting-document/` — project documentation.

## Limitations and responsible use
The generator returns rule-based mock text, not an LLM response. It does not fetch live weather. Automatic review is heuristic and cannot guarantee factual correctness or reliably detect semantic hallucinations or contradictions. Sample cases are synthetic. Outputs are drafts, not official warnings or medical advice. A responsible person must verify every draft against the source forecast and official local guidance before distribution.

## Project links
- Repository: https://github.com/ramanjaneyareddy15/heatguard-ai-g15
- Live prototype: https://heatguard-ai-g15.onrender.com
- Demonstration reel (YouTube): https://youtu.be/j9HeEwSLZ34
- Reel duration: to be confirmed from the uploaded video.
