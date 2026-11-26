# Evaluation Rubric — HeatGuard AI

Score each criterion from 1 (poor) to 5 (strong). Run every prompt version on the same test cases. Fill in scores only after actually running tests.

| Criterion | 1 (poor) | 3 (acceptable) | 5 (strong) |
|---|---|---|---|
| Faithfulness to supplied forecast | Several invented or changed facts | Facts mostly preserved, minor drift | Every specific claim traceable to the input |
| Clarity and accessibility | Confusing or jargon-heavy | Understandable, some awkward parts | Clear, plain, easy to scan |
| Audience and tone appropriateness | Wrong tone or audience | Partly adapted | Wording clearly suited to the audience, calm tone |
| Completeness of required sections | Several sections missing | All present, some thin | All four sections present and useful |
| Length and format compliance | Well over limit or wrong format | Slightly over or minor format slips | Within limit, exact format |
| Handling of missing/uncertain information | Guesses missing details | Mentions some gaps | Lists every missing or uncertain item, guesses nothing |

## Also record (counts or notes)

- Invented values (temperatures, dates, locations, warning levels)
- Unsupported claims (causes, health statements not given in the input)
- Contradictory wording
- Missed caveats (for example, no pointer to official local guidance)

## Scoring tips

- Score each output independently, then compare versions.
- Use the same reviewer(s) for all versions where possible, and note who scored.
- Keep the failed outputs. They are the evidence for your prompt revisions.
