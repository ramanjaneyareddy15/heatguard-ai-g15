# HEATGUARD AI — MILESTONE 2 REPORT (TWO-OPTION PROJECT DOCUMENTATION)

> Working report draft. Complete the evidence and submission checks in `SUBMISSION_BLOCKERS.md` before formal submission.

## 1. Project overview
HeatGuard AI is a prompt-based prototype for drafting heat-wave public-health advisories from forecast information supplied by a user. Intended audiences include the general public, students, campus staff and community communication teams. The project emphasizes preserving supplied facts, identifying missing or uncertain information, calm communication and human review.

## 2. Prompt and solution design
### Inputs and outputs
Inputs include forecast text, optional location, forecast period and warning level, audience, language and maximum word count. The output is a four-section advisory draft plus limited automatic review messages.

### Two supported prompt options
The deployed interface offers exactly two prompt choices:
- **Baseline:** concise source-grounding instructions, missing-information handling and a four-section advisory.
- **Structured:** explicit source-grounding rules, audience/tone guidance, metadata handling, fixed headings and a final claim check.

P1 Advisory Generation, P2 Audience Adaptation and P3 Output Review are workflow tasks documented separately; they are not additional choices in the prompt selector.

### Actual implementation and tool choice
The deployed Python prototype builds the selected prompt but returns rule-based mock advisory output (`is_mock: true`). It does not call Gemini or another LLM, and it does not retrieve live weather. The automatic reviewer uses limited heuristics and is not semantic hallucination detection. Any external AI Studio experiments must be reported separately from the deployed prototype and supported by genuine run evidence.

## 3. Implementation
- `backend.py`: Python HTTP server and API request handling.
- `heatguard.py`: sample-case loading, prompt filling and rule-based mock generation.
- `static/index.html`: browser interface with Baseline and Structured radio options.
- `prompts/baseline_prompt.txt`, `prompts/structured_prompt.txt`: two runtime prompt templates.
- `prompts/final/`: P1/P2/P3 workflow prompt sheets.
- `test-data/`, `tests/`: synthetic cases, execution matrix, rubric and experiment notes.

## 4. Workflow
1. User enters forecast text and optional metadata.
2. User chooses Baseline or Structured.
3. Backend validates input and prepares the selected prompt.
4. Prototype returns a rule-based mock advisory.
5. Heuristic checks report limited findings.
6. A human verifies the source forecast and official local guidance before any public use.

## 5. Testing and limitations
Synthetic test cases and the execution matrix are stored in `test-data/`. The experiment log contains qualitative observations; numerical rubric scores must only be entered after actual scoring. Do not represent local mock tests as Gemini runs. Limitations include no live LLM integration, no live weather integration, heuristic-only review, possible word-limit overruns and the need for human verification.

## 6. Repository and deployment
Repository: https://github.com/ramanjaneyareddy15/heatguard-ai-g15  
Live prototype: https://heatguard-ai-g15.onrender.com

The Render service previously ran application version 2.0.0. The documentation-alignment commit is being deployed separately; confirm its final Render status before claiming the live site contains the latest documentation.

## 7. Team and submission evidence
Confirm team details, contribution percentages and member approval against the team's actual records. Add genuine screenshots and completed test evidence. Do not invent results, scores, model settings or approvals.
