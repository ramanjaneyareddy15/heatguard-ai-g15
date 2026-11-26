# HeatGuard AI – Prompt-Based Heat-Wave Public-Health Advisory Generator

**Team:** NovaNex | **Team ID:** PE-B01-44 | **Batch:** B01-B12  
**Faculty:** Sonal Kukreja

## Project overview
HeatGuard AI is a browser-based prototype for drafting heat-wave public-health advisories from forecast information supplied by a user. It accepts a forecast, optional location/period/warning level, audience, language and word limit. It displays a filled prompt and a clearly labelled rule-based mock advisory.

## Actual implementation
- Python backend: `backend.py`; browser interface: `static/index.html`.
- `/api/generate` fills Baseline or Structured prompt templates and calls `heatguard.mock_output()`.
- The response marks the output as `is_mock: true`. It is not an LLM response.
- `/api/review` performs limited heuristic checks (numeric strings, section labels, word count, official-guidance mention and missing-input acknowledgement). It is not semantic hallucination detection.
- The current UI exposes Baseline and Structured prompt modes. V1/V2/V3 files are reference/design iterations, not runtime model calls.
- No Gemini/LLM API or live-weather API is integrated in this code.

## Version 2.0.0
- Added `GET /health` for Render health checks.
- Added `GET /api/version` to report app version and integration status.
- Updated Render build and health-check configuration.

## Run locally
```bash
python backend.py
```
Open `http://127.0.0.1:8000`. Render uses the `PORT` environment variable.

## Main files
- `backend.py` – HTTP server, JSON API, health and version endpoints.
- `heatguard.py` – sample-case loading, prompt filling and rule-based mock generation.
- `static/index.html` – browser interface.
- `prompts/` – runtime templates and prompt-design iterations.
- `test-data/`, `tests/` – synthetic cases, test tracker and rubric.
- `docs/diagrams/` – design diagrams.
- `report/`, `supporting-document/` – Milestone 2 draft documents.

## Verification
The local v2.0.0 server was checked for `/`, `/health`, `/api/version`, `/api/cases` and `/api/generate`; these returned HTTP 200 in the local smoke test. Generation returned `is_mock: true`. This does not establish model inference, factual accuracy, or semantic quality.

Repository: https://github.com/ramanjaneyareddy15/heatguard-ai-g15  
Render URL: https://heatguard-ai-g15.onrender.com

## Before submission
Confirm all report details and team contributions, add genuine screenshots, execute and score the required model tests if required, and verify Render's latest deployment and live health endpoint. Never claim LLM integration or completed tests without evidence.
