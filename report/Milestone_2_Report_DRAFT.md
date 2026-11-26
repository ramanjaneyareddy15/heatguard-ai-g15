# HEATGUARD AI – MILESTONE 2 REPORT (WORKING DRAFT)

> **Submission status: NOT READY.** Replace every [CONFIRM] field, execute pending tests, insert genuine evidence and confirm late-submission permission before uploading.

## 1. Cover page
- Team ID: [CONFIRM – use Milestone 1 Team ID]
- Team name: [CONFIRM]
- Project title: HeatGuard AI – Prompt-Based Heat-Wave Public-Health Advisory Generator
- Problem Pool: G15 – Heat-Wave Public-Health Advisory Generator
- Batch: [CONFIRM]
- Faculty guide: [CONFIRM]
- Members and enrollment numbers: [CONFIRM ALL]
- Prototype link: [ADD VERIFIED GOOGLE AI STUDIO SHARE LINK]
- Repository link: [ADD PUBLIC GITHUB OR ANYONE-WITH-LINK DRIVE LINK]
- Reel link: [ADD DRIVE/UNLISTED YOUTUBE LINK]

## 2. Prompt and solution design
### Problem, users, inputs and outputs
HeatGuard AI addresses the need for clear, responsible heat-safety communication based on forecast information supplied by a user. Intended users include the general public, students, campus administrators/staff and community communication teams. Inputs may include forecast text, location, date/forecast period, temperature, official warning level, audience, language and maximum length. Missing fields must remain missing; the system must not infer them. Outputs are concise draft advisories or reviews, with forecast facts separated from general precautions and uncertainty explicitly stated.

### Prompts and tool/model
The solution uses three distinct prompt workflows: P1 Advisory Generation, P2 Audience Adaptation and P3 Output Review. These separate generation, audience-specific rewriting and quality review into distinct tasks. The experiments were conducted in Google AI Studio using Gemini. **Exact model identifier and run settings: [CONFIRM FROM AI STUDIO HISTORY/RUN SETTINGS].**

### Changes since Milestone 1
The initial package contained an offline prompt-building prototype, baseline/structured prompt templates, five synthetic inputs, a rubric and a mock response generator. The subsequent work developed V1, V2 and V3 system-instruction iterations in Google AI Studio and tested the three workflow functions. The local Python backend remains a rule-based mock and is not connected to Gemini.

### Diagrams
Insert the four diagrams from `docs/diagrams/`: prompt workflow, task decomposition, input-output flow and no-code screen flow. These diagrams describe the intended Google AI Studio workflow and must be checked against the actual shared prototype before final submission.

### Prompt sheets
Insert the three prompt sheets from `prompts/final/`. Include the complete final V3 system prompt from `prompts/v3/system_instructions_v3.txt`. Add actual model settings and a real sample input/output for each prompt before submission.

## 3. Implementation
### What is built
- Google AI Studio prompt setup with HeatGuard system instructions (V1, V2, V3).
- Three tested prompt functions: advisory generation, audience adaptation and output review.
- Offline Python/HTML prototype that builds prompt text, produces clearly labelled mock output and runs limited rule-based checks.

### Module status
| Module | What it does | Status | Notes |
|---|---|---|---|
| P1 Advisory Generation (AI Studio) | Generates draft advisory | Working in observed AI Studio runs | Share link and evaluator access must be verified |
| P2 Audience Adaptation (AI Studio) | Adapts wording to audience | Working in observed AI Studio runs | Tested with student audience |
| P3 Output Review (AI Studio) | Finds fabricated/omitted details | Working in observed AI Studio runs | Tested with intentionally flawed advisory |
| Offline Python prompt builder | Builds prompt text | Working locally | Not Gemini-connected |
| Offline mock advisory | Demonstrates expected structure | Working locally | Mock only; not an AI response |
| Rule-based output checker | Checks simple conditions | Partly working | Limited heuristic checks; human review required |
| Live weather integration | Retrieves live forecasts | Not started | Outside current prototype scope |

### Prompt iteration log
| Version | Change | Why | Observed result |
|---|---|---|---|
| V1 | Basic role and rules: use supplied facts, identify missing information, calm language and safety precautions | Establish baseline behaviour | Observed generation/adaptation/review runs; numeric scoring not recorded |
| V2 | Added stricter fact preservation, explicit missing-field handling, audience controls and output review expectations | Address unsupported assumptions and omissions | Output review identified fabricated 45°C, tomorrow, Hyderabad, false red alert and unsupported student audience |
| V3 | Added explicit separation of forecast facts and precautions, structured review, final quality checklist | Improve consistency and transparency | Observed outputs clearly separated facts/precautions; review identified fabricated details, omitted dry conditions and hidden uncertainty |

**Full prompt texts:** attach V1, V2 and V3 files from `prompts/`. V1/V2 are reconstructed from the available screenshot/conversation and must be checked against original saved text.

## 4. Demonstration and testing
### Test dataset
A 10-case synthetic test plan is provided in `test-data/test_cases.csv`: six normal scenarios, three edge cases and one invalid/review scenario. These are test inputs, not live forecasts.

### Execution status
Nine qualitative Google AI Studio runs are documented in `tests/experiment_log.csv`: three workflow types were tried under each of V1, V2 and V3. The nine runs reuse three core scenarios and do **not** satisfy the requirement for at least 10 distinct executed test inputs. TC-01 to TC-10 remain pending execution and scoring. No numerical rubric scores have been invented.

| Test | Type | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| TC-01 to TC-10 | See `test-data/test_cases.csv` | See expected_result field | **PENDING – run in AI Studio and record exact output** | Pending |

### Screenshots
Insert 2–3 genuine screenshots of actual Gemini runs, each captioned with its test number. Existing setup screenshots are not substitutes for actual test-run evidence. Evidence currently available in the conversation includes a V3-style advisory output screenshot; collect and add at least two more distinct actual runs.

### Known limitations and next steps
1. The prototype does not fetch live weather data; next, evaluate a safe, sourced integration only if scope permits.
2. The local Python backend generates mock output rather than Gemini output; next, either keep it explicitly as an offline demonstrator or implement and test a secure Gemini integration.
3. The rule-based checker cannot reliably detect all semantic hallucinations or contradictions; next, combine automated checks with human rubric review.
4. Forecast inputs may be incomplete or contradictory; next, test clarification behaviour and require source verification before public use.

## 5. Repository
Insert one screenshot of the final public GitHub repository or shared project folder. The folder structure is prepared in this package. Add the verified repository URL here: [ADD LINK]. The changes since Milestone 1 include prompt iterations, three prompt sheets, synthetic test dataset, experiment observations, diagrams and this report draft.

## 6. Supporting document
Insert the 1–2 page Technical Report from `supporting-document/HeatGuard_Technical_Report.md`, export it to PDF, and include the same PDF in this section and as the separate supporting-document upload.

## 7. Team contribution
| Member | Enrollment number | Role | Tasks completed in Milestone 2 | Evidence | Contribution % |
|---|---|---|---|---|---:|
| [MEMBER 1] | [ID] | [ROLE] | [SPECIFIC TASK] | [FILE/COMMIT/PDF SECTION] | [ % ] |
| [MEMBER 2] | [ID] | [ROLE] | [SPECIFIC TASK] | [FILE/COMMIT/PDF SECTION] | [ % ] |
| [ADD ROWS AS NEEDED] | | | | | |

Percentages must total 100%. Every member must agree with the table. Do not submit placeholder names or invented contributions.
