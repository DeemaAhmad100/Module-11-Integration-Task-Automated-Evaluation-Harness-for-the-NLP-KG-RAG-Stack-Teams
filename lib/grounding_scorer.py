"""RAG grounding-rate scoring functions -- testable in isolation.

Per the integration spec methodology paragraph (RAG grounding rate):

  - Decline detection. A response whose `answer` field equals the canonical
    decline string is excluded from the denominator.
  - Grounded detection. A non-decline response is grounded iff (a) at least
    one citation is present AND (b) every cited chunk_id is in the candidate
    set read from the response's `retrieved` field for the same question.

The split between this module and eval_rag.py exists so the scoring logic is
unit-testable.
"""
from typing import Iterable


DECLINE_STRING = "I cannot answer this from the available sources."


def is_decline(response: dict) -> bool:
    """Return True iff `response.answer` is exactly the canonical decline string.

    Case-sensitive, punctuation-sensitive, exact-match.
    """
    return response.get("answer") == DECLINE_STRING


def is_grounded(response: dict, candidate_ids: Iterable[str]) -> bool:
    """Return True iff the response satisfies the two grounding conditions.

    (a) response.citations has length >= 1.
    (b) every chunk_id in response.citations is in candidate_ids.
    """
    citations = response.get("citations", [])
    if len(citations) < 1:
        return False

    candidate_set = set(candidate_ids)
    for citation in citations:
        # citation ممكن يكون string مباشر أو dict فيه chunk_id
        chunk_id = citation if isinstance(citation, str) else citation.get("chunk_id")
        if chunk_id not in candidate_set:
            return False

    return True