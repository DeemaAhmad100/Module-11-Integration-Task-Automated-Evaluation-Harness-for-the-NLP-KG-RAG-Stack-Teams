"""RAG grounding-rate evaluation harness for the M11 Integration.

Methodology (RAG grounding rate -- citation-resolves-to-retrieved-chunk):

Filter to the question_ids in the gold fixture (`data/rag_questions.json`).
For each question: (i) call POST /rag/answer; (ii) read the candidate set
from the response's `retrieved` field (each entry carries a `chunk_id`).
A response is grounded iff (a) `response.citations` has length >= 1, AND
(b) every `chunk_id` in `response.citations` is in the candidate set for
the same question. Decline-exclusion: if
`response.answer` is exactly the canonical decline string (case-sensitive,
punctuation-sensitive, exact match against "I cannot answer this from the
available sources."), the question is excluded from the denominator (counted
as "declined", not "ungrounded"). Aggregate as grounding rate = grounded /
(total - declined). Threshold floor: grounding rate >= 0.85. Edge case: if
every question declines, the denominator is 0; the report writes `0.0 (all
declined)` rather than dividing by zero.

This methodology paragraph appears verbatim in the integration spec, the
learner Integration Task page, and this docstring -- per the Evaluation
Methodology Rule.
"""

import json
import os
from typing import Tuple

import httpx

from lib.grounding_scorer import is_decline, is_grounded


API_URL = os.environ.get("API_URL", "http://localhost:8000")
FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "data", "rag_questions.json")


def load_fixture():
    """Return the gold fixture as a list of {question_id, question, k, ...}."""
    with open(FIXTURE_PATH) as fh:
        return json.load(fh)


def run() -> Tuple[float, list]:
    """Run the harness end-to-end. Returns (grounding_rate, per_question_results)."""
    fixture = load_fixture()
    results = []
    grounded_count = 0
    declined = 0

    for item in fixture:
        question_id = item["question_id"]
        question = item["question"]
        k = item.get("k", 4)

        resp = httpx.post(
            f"{API_URL}/rag/answer", json={"question": question, "k": k}, timeout=60.0
        )
        resp.raise_for_status()
        response_json = resp.json()

        if is_decline(response_json):
            declined += 1
            results.append({
                "question_id": question_id,
                "question": question,
                "answer": response_json.get("answer"),
                "citations": response_json.get("citations", []),
                "status": "declined",
                "passed": None,
            })
            continue

        candidate_ids = [
            entry.get("chunk_id") for entry in response_json.get("retrieved", [])
        ]
        grounded = is_grounded(response_json, candidate_ids)
        if grounded:
            grounded_count += 1

        results.append({
            "question_id": question_id,
            "question": question,
            "answer": response_json.get("answer"),
            "citations": response_json.get("citations", []),
            "candidate_ids": candidate_ids,
            "status": "answered",
            "passed": grounded,
        })

    denominator = len(fixture) - declined
    grounding_rate = grounded_count / denominator if denominator > 0 else 0.0

    return grounding_rate, results


if __name__ == "__main__":
    rate, results = run()
    print(f"RAG grounding rate: {rate:.4f}")