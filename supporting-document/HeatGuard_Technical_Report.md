# HeatGuard AI – Technical Report (Supporting Document Draft)

## Project overview
HeatGuard AI is a prompt-based prototype for generating, adapting and reviewing heat-wave public-health advisories from forecast information supplied by a user. Its goal is to improve clarity and source-faithfulness while making missing information explicit. Outputs are drafts for human review, not official warnings or medical advice.

## Architecture and tools
The project has two distinct implementation tracks. The offline Python prototype (`backend.py`, `heatguard.py` and `static/index.html`) builds prompt templates, returns rule-based mock outputs and performs limited heuristic checks. It does not call Gemini or retrieve live weather. Separately, the prompt experiments were conducted in Google AI Studio using Gemini. The exact model identifier and settings must be confirmed from the user's AI Studio run history before final submission.

## Prompt design
Three prompt workflows were defined: P1 Advisory Generation, P2 Audience Adaptation and P3 Output Review. V1 established the core role and constraints. V2 strengthened factual preservation, missing-information handling and audience controls. V3 added explicit separation of forecast facts from general precautions, a structured review procedure and a final quality checklist. The full recovered prompts are stored in the repository's `prompts/` directory; V1 and V2 text should be verified against the original saved versions.

## Preliminary testing observations
Nine qualitative Google AI Studio runs are described in the experiment log: each of three workflow functions was tried with V1, V2 and V3. The review scenario intentionally contained unsupported claims (45°C, tomorrow, Hyderabad and an official red alert) while the source forecast contained only hot and dry afternoon conditions. The V2 and V3 reviews identified the invented details, omission of dry conditions, missing uncertainty and unsupported student audience assumption. The V3 advisory-generation and audience-adaptation runs preserved the supplied hot/dry forecast and identified missing temperature/date/location/warning information. These are qualitative observations; no numerical rubric scores were recorded. The 10-case test suite remains to be executed.

## Limitations and responsible use
The prototype has no live forecast integration. The local backend's outputs are mock outputs, not model-generated responses. The automatic checker uses simple heuristics and cannot replace semantic human review. Incomplete or contradictory forecast inputs require clarification. Before any public distribution, a human must verify the source forecast and direct readers to official local weather and public-health guidance.

## Next steps
Execute all 10 synthetic test cases (including edge/invalid cases), save actual Gemini outputs, complete the 1–5 evaluation rubric, add genuine run screenshots, verify the shared AI Studio prototype and repository links, and conduct human review.
