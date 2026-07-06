"""NL -> Cypher exact-match evaluation harness for the M11 Integration.

Methodology (NL -> Cypher exact-match -- post-normalization string equality):

Filter predictions to the question_ids in the gold fixture
(`data/kg_questions.json`). Normalize both predicted Cypher and gold Cypher
using `re.sub(r"\\s+", " ", s).strip()` (whitespace collapse + leading/trailing
strip), then uppercase the seven Cypher keywords MATCH, RETURN, WHERE,
OPTIONAL, WITH, LIMIT, ORDER BY in both strings using case-insensitive
substitution. Exact-match = the normalized predicted string equals the
normalized gold string. Aggregate as fraction of questions where exact-match
is True. Exclude from the denominator any question for which the `/kg/query`
endpoint returned HTTP 422 with `UnsupportedQueryError` (the W9B mapper's
documented "not supported by the bounded schema" response). Threshold floor:
exact-match >= 0.80. Tie-breaking: not applicable (the comparison is binary).

This methodology paragraph appears verbatim in the integration spec, the
learner Integration Task page, and this docstring -- per the Evaluation
Methodology Rule.
"""

import json
import os
from typing import Tuple

import httpx

from lib.cypher_normalizer import normalize_cypher


API_URL = os.environ.get("API_URL", "http://localhost:8000")
FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "data", "kg_questions.json")


def load_fixture():
    """Return the gold fixture as a list of {question_id, question, gold_cypher}."""
    with open(FIXTURE_PATH) as fh:
        return json.load(fh)


def run() -> Tuple[float, list]:
    """Run the harness end-to-end. Returns (exact_match_rate, per_question_results)."""
    fixture = load_fixture()
    results = []
    matched = 0
    excluded = 0

    for item in fixture:
        question_id = item["question_id"]
        question = item["question"]
        gold_cypher = item["gold_cypher"]

        resp = httpx.post(f"{API_URL}/kg/query", json={"question": question}, timeout=60.0)

        if resp.status_code == 422:
            excluded += 1
            results.append({
                "question_id": question_id,
                "question": question,
                "gold_cypher": gold_cypher,
                "predicted_cypher": None,
                "status": "excluded_unsupported",
                "passed": None,
            })
            continue

        if resp.status_code >= 500:
            results.append({
                "question_id": question_id,
                "question": question,
                "gold_cypher": gold_cypher,
                "predicted_cypher": None,
                "status": "server_error",
                "passed": False,
            })
            continue

        resp.raise_for_status()
        predicted_cypher = resp.json().get("cypher", "")

        norm_pred = normalize_cypher(predicted_cypher)
        norm_gold = normalize_cypher(gold_cypher)
        passed = norm_pred == norm_gold
        if passed:
            matched += 1

        results.append({
            "question_id": question_id,
            "question": question,
            "gold_cypher": gold_cypher,
            "predicted_cypher": predicted_cypher,
            "status": "scored",
            "passed": passed,
        })

    denominator = len(fixture) - excluded
    exact_match_rate = matched / denominator if denominator > 0 else 0.0

    return exact_match_rate, results


if __name__ == "__main__":
    rate, results = run()
    print(f"KG NL->Cypher exact-match: {rate:.4f}")