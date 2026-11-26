# HeatGuard AI — Technical Report (Supporting Document)

## 1. Project overview
HeatGuard AI is a prototype for drafting heat-wave public-information advisories from forecast text supplied by a user. It aims to preserve supplied facts, identify missing or uncertain information, use calm language and direct readers to official local guidance. Outputs are drafts for human review, not official warnings or medical advice.

## 2. Architecture and implementation
The deployed offline prototype consists of `backend.py`, `heatguard.py` and `static/index.html`. It prepares prompt templates, returns rule-based mock outputs and performs limited heuristic checks. It does not call Gemini or another live LLM and does not retrieve live weather. The browser interface provides exactly two prompt options: Baseline and Structured.

## 3. Prompt design
The Baseline prompt gives concise instructions to preserve facts, avoid invented details, mention missing information and produce four sections. The Structured prompt adds explicit source-grounding rules, audience/tone guidance, metadata fields, fixed headings and a final claim check. P1 Advisory Generation, P2 Audience Adaptation and P3 Output Review are described as workflow tasks, not as extra selector options.

## 4. Testing and observed results
The repository includes synthetic test cases, an execution matrix, an evaluation rubric and a qualitative experiment log. The local prototype's smoke tests demonstrate application and API behavior only; mock output is not model performance. Numerical rubric scores and claims about external model experiments must be supported by saved actual outputs and genuine run evidence.

## 5. Limitations and responsible use
There is no live weather feed or integrated LLM call in the deployed prototype. The automatic checker uses simple heuristics and cannot guarantee factual correctness or reliably detect semantic hallucinations or contradictions. Sample cases are synthetic. A human must verify every draft against the source forecast and official local guidance before distribution.

## 6. Next steps
Potential future work includes secure model integration if approved, verified weather-data integration, stronger contradiction and unsupported-claim detection, improved word-limit enforcement, expanded testing and documented human review.
