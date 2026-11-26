#!/usr/bin/env python3
"""HeatGuard AI - offline starter prototype (Milestone 1).

Prints the filled prompt template and a transparent, rule-based MOCK output
for a synthetic test case. It does NOT call any AI model or weather service.
The mock output only repeats supplied fields and lists missing ones; it is
not a model result and must not be reported as one.
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOT_PROVIDED = "Not provided"

PRECAUTIONS = {
    "general public": [
        "Drink water regularly, even if you do not feel thirsty.",
        "Avoid strenuous outdoor activity during the hottest part of the day.",
        "Wear light, loose clothing and stay in shade or cool places when possible.",
        "Check on older neighbours, young children and people who live alone.",
    ],
    "students": [
        "Carry a water bottle and refill it often between classes.",
        "Plan outdoor sports and events for cooler hours, if you can.",
        "Take breaks in shaded or cool indoor areas.",
        "Look out for friends who seem unwell and tell staff if someone needs help.",
    ],
    "campus staff": [
        "Consider scheduling outdoor work and events outside the hottest hours.",
        "Make drinking water and shaded rest areas easy to reach.",
        "Remind staff and students to take regular breaks.",
        "Share information through your usual campus channels.",
    ],
    "community communication team": [
        "Share the message through the channels your community already uses.",
        "Use plain language and keep the supplied facts unchanged.",
        "Include a pointer to official local guidance in every post.",
        "Have the draft reviewed by a responsible person before publishing.",
    ],
}
DEFAULT_PRECAUTIONS = PRECAUTIONS["general public"]


def load_cases():
    path = ROOT / "data" / "sample_inputs.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)["cases"]


def load_template(name):
    path = ROOT / "prompts" / f"{name}_prompt.txt"
    return path.read_text(encoding="utf-8")


def fill_prompt(template, case):
    values = {
        "forecast": case["forecast_text"],
        "audience": case["audience"],
        "language": case["language"],
        "max_words": case["max_words"],
        "location": case.get("location") or NOT_PROVIDED,
        "period": case.get("period") or NOT_PROVIDED,
        "warning_level": case.get("warning_level") or NOT_PROVIDED,
    }
    return template.format(**values)


def mock_output(case):
    """Rule-based placeholder. Repeats supplied facts only; never infers."""
    location = case.get("location")
    period = case.get("period")
    level = case.get("warning_level")

    where = f" for {location}" if location else ""
    headline = f"Heat advisory{where} (draft)"

    main = f"Based on the supplied forecast: {case['forecast_text']}"
    if level:
        main += f" Warning level given: {level}."
    if period:
        main += f" Period given: {period}."

    precautions = PRECAUTIONS.get(case["audience"].lower(), DEFAULT_PRECAUTIONS)

    missing = []
    if not location:
        missing.append("Location was not provided.")
    if not period:
        missing.append("Forecast period was not provided.")
    if not level:
        missing.append("Warning level was not provided.")
    if not missing:
        missing.append("No fields missing. Confirm details against the official source.")
    missing.append("This is a draft, not an official warning. Follow official local guidance.")

    lines = [
        "1. Advisory headline",
        headline,
        "",
        "2. Main message",
        main,
        "",
        "3. Practical general precautions",
        *[f"- {p}" for p in precautions],
        "",
        "4. Missing/uncertain information",
        *[f"- {m}" for m in missing],
    ]
    text = "\n".join(lines)
    words = len(text.split())
    note = f"[mock word count: {words} / limit {case['max_words']}]"
    if words > case["max_words"]:
        note += " - over limit, tighten the prompt or the template"
    return text + "\n\n" + note


def main():
    parser = argparse.ArgumentParser(description="HeatGuard AI offline starter")
    parser.add_argument("--list", action="store_true", help="list test cases")
    parser.add_argument("--case", default="case_01", help="case id")
    parser.add_argument("--prompt", choices=["baseline", "structured"], default="baseline")
    parser.add_argument("--prompt-only", action="store_true", help="print only the filled prompt")
    parser.add_argument("--mock-only", action="store_true", help="print only the mock output")
    args = parser.parse_args()

    cases = load_cases()
    if args.list:
        for c in cases:
            print(f"{c['id']}: {c['label']}")
        return

    case = next((c for c in cases if c["id"] == args.case), None)
    if case is None:
        raise SystemExit(f"Unknown case '{args.case}'. Use --list to see cases.")

    if not args.mock_only:
        print(f"=== FILLED PROMPT ({args.prompt}) | {case['label']} ===\n")
        print(fill_prompt(load_template(args.prompt), case))
        print()
    if not args.prompt_only:
        print("=== MOCK OUTPUT (rule-based, NOT a model result) ===\n")
        print(mock_output(case))


if __name__ == "__main__":
    main()
