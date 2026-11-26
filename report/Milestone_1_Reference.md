# BENNETT UNIVERSITY
## B.Tech — 5th Semester
### Prompt Engineering Mini-Project — Milestone 1

**Project title:** HeatGuard AI — Prompt-Based Heat-Wave Public-Health Advisory Generator  
**Problem Pool ID:** G15 — Heat-Wave Public-Health Advisory Generators  
**Team name:** [Enter team name]  
**Team members:** [Enter names and student IDs]  
**Faculty guide:** [Enter name]  
**Submission date:** [Confirm on LMS / with faculty]

---

## 1. Introduction
Heat waves can create public-health risks, and people may need clear, audience-appropriate information about forecast conditions and general precautions. HeatGuard AI is proposed as a prompt-engineering system that takes supplied heat-forecast information and an audience type, then produces a concise public-health advisory message.

The main assessed work is prompt design, iteration, evaluation, and responsible handling of uncertain or missing information—not merely building a chatbot.

## 2. Problem statement and user context
**Problem statement:** Design and evaluate a prompt workflow that converts supplied heat-forecast data and audience information into a clear, appropriately toned public-health advisory.

**Target users:** General public, students, campus administrators, and community communication teams preparing informational messages.

**Inputs:** Supplied heat forecast or warning text, forecast period/location if provided, audience type, preferred language, and message length. The prototype must not infer missing forecast details.

**Expected outputs:** A concise advisory, a short explanation based on the supplied forecast, general heat-safety messaging appropriate to the audience, and explicit notes about missing or uncertain information.

## 3. Reason for selecting the project
This project is directly aligned with Problem G15 in Appendix A of the supplied Bennett University guidelines. It is feasible as a small prompt-engineering prototype using sample forecast text and an available language model. It can demonstrate context injection, audience/tone constraints, length constraints, few-shot examples, prompt comparison, and rubric-based evaluation.

## 4. Existing solutions and proposed gap
Weather services and public-health agencies publish forecasts and heat-safety advice. This project does not claim that existing services lack these capabilities.

**Proposed evaluation question:** Does a structured prompt that specifies audience, tone, length, source-grounding, and missing-information handling produce more consistent and useful advisory drafts than a basic prompt on the team's test set? This is a question to test, not a completed finding.

## 5. Objectives
1. Create a baseline prompt that drafts an advisory from supplied heat-forecast text.
2. Create improved prompt variants with audience, tone, length, and grounding constraints.
3. Test prompt versions on the same representative inputs.
4. Evaluate clarity, relevance, completeness, format compliance, and handling of uncertainty.
5. Record errors and refine prompts based on actual test evidence.
6. Document limitations and responsible AI safeguards.

## 6. Prompt-engineering task definition
- **Task A — Advisory generation:** forecast text + audience type → short public-health advisory.
- **Task B — Audience adaptation:** same forecast + different audience → appropriately adapted wording without changing the underlying facts.
- **Task C — Output review:** forecast + generated message → flag unsupported claims, omitted caveats, or missing forecast details.

The prototype provides general informational messaging only. It does not diagnose illness, replace official warnings, or invent forecast values.

## 7. Initial baseline prompt
> You are a public-information writing assistant. Using only the heat-forecast information supplied below, draft a clear and concise public-health advisory for the specified audience. Preserve the supplied facts. Do not invent temperatures, dates, locations, warning levels, or causes. If important information is missing, say so. Keep the wording calm, accessible, and suitable for public communication. Include general heat-safety information only where appropriate, and state that people should follow relevant official local guidance.
>
> Forecast information: [insert supplied forecast text]  
> Audience: [general public / students / campus staff]  
> Preferred language: [insert language]  
> Maximum length: [insert word limit]  
> Output sections: (1) Advisory headline, (2) Main message, (3) Practical general precautions, (4) Missing/uncertain information.

This prompt is proposed and has not been claimed to have passed testing.

## 8. Proposed workflow
1. Prepare a small test set of supplied or clearly labelled synthetic forecast examples.
2. Run the baseline prompt and save outputs.
3. Run a structured prompt with explicit audience, tone, length, and source-grounding rules.
4. Compare outputs against the same rubric.
5. Record failures, revise the prompt, and repeat the same test cases.
6. Have a person review the draft before treating it as public-facing guidance.

## 9. Technology and tools
- Language model: an available model selected by the team based on access, cost, and course requirements.
- Prototype: Python; the starter version works offline and prints prompt templates plus a transparent mock output.
- Test inputs: synthetic examples in `data/sample_inputs.json`; these are not real forecasts.
- Evaluation: rubric and experiment log in `tests/`.
- Version control: Git/GitHub if used by the team.

This starter package does not connect to live weather feeds or an external AI model.

## 10. Research and evidence plan
Use and verify suitable official public-health and weather guidance before final submission. Suggested starting sources:
- World Health Organization, *Heat and health*: https://www.who.int/news-room/fact-sheets/detail/climate-change-heat-and-health
- World Meteorological Organization, *Heat-health*: https://public.wmo.int/
- Bennett University, *Prompt Engineering Mini-Project Guidelines, Milestones & Assessment* (2026), Appendix A, G15.

The team should verify the exact pages and guidance it uses, add access dates, and cite sources consistently. These are starting points, not evidence of completed experiments.

## 11. Proposed evaluation plan
Run every prompt version on the same test inputs. Score each criterion from 1 (poor) to 5 (strong) using a written rubric:
- Faithfulness to supplied forecast information
- Clarity and accessibility
- Audience and tone appropriateness
- Completeness of required output sections
- Compliance with the length and format constraints
- Appropriate handling of missing or uncertain information

Also record invented values, unsupported claims, contradictory wording, and missed caveats. Fill in scores only after actually running tests.

## 12. Responsible AI and limitations
- Clearly label synthetic test cases; do not present them as live forecasts.
- Use only supplied forecast information for claims about specific conditions.
- Do not invent temperatures, warning levels, locations, or dates.
- State uncertainty and missing data.
- Treat outputs as draft informational messages, not medical advice or official warnings.
- Require human review and use relevant official local guidance before public distribution.
- Acknowledge all sources, models, and tools.

Limitations include incomplete input, model-generated inaccuracies, lack of live forecast integration in this starter version, and the need for local authorities' official guidance.

## 13. Expected deliverables
1. Baseline and improved prompt versions.
2. Test inputs and saved outputs.
3. Evaluation rubric and completed experiment log.
4. Working demonstration of the prompt workflow.
5. Error analysis and responsible-use notes.
6. Later milestone report, presentation, and demonstration materials.

## 14. Faculty/senior feedback
**Status: Not yet obtained.** Complete this section only after an actual discussion.

- Person consulted and role: [fill in]
- Date: [fill in]
- Feedback received: [record actual feedback]
- Changes made: [record actual changes]

No faculty feedback or approval is claimed in this draft.

## 15. Conclusion
HeatGuard AI is proposed as a prompt-engineering implementation of Problem G15: Heat-Wave Public-Health Advisory Generators. It will explore how audience-aware, constrained, source-grounded prompts can produce clear advisory drafts from supplied heat-forecast information. The team will compare prompt versions on a defined test set and report only observed results.

## References
1. World Health Organization. *Heat and health*. https://www.who.int/news-room/fact-sheets/detail/climate-change-heat-and-health
2. World Meteorological Organization. Public heat-health information. https://public.wmo.int/
3. Bennett University. (2026). *Prompt Engineering Mini-Project Guidelines, Milestones & Assessment*. Appendix A, Problem G15.
