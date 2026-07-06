"""YOUR tests for the evaluation methodology helpers.

Per the integration guide, write at least 3 substantive tests against the
scorer helpers in `lib/`. At least 1 assertion per test. The autograder
enforces the structure via AST.
"""

import pytest

from lib import ner_scorer, cypher_normalizer, grounding_scorer


def test_ner_scorer_handles_perfect_match():
    """compute_micro_f1 returns (1.0, 1.0, 1.0) on identical predictions and gold."""
    gold_by_doc = {
        "doc-1": [
            {"entity_text": "Boston", "entity_label": "LOC"},
            {"entity_text": "Ali", "entity_label": "PER"},
        ],
        "doc-2": [
            {"entity_text": "Acme Corp", "entity_label": "ORG"},
        ],
        "doc-3": [
            {"entity_text": "Cambridge", "entity_label": "LOC"},
        ],
    }
    predictions_by_doc = {
        "doc-1": [
            {"entity_text": "Boston", "entity_label": "LOC"},
            {"entity_text": "Ali", "entity_label": "PER"},
        ],
        "doc-2": [
            {"entity_text": "Acme Corp", "entity_label": "ORG"},
        ],
        "doc-3": [
            {"entity_text": "Cambridge", "entity_label": "LOC"},
        ],
    }

    precision, recall, f1 = ner_scorer.compute_micro_f1(predictions_by_doc, gold_by_doc)

    assert precision == 1.0
    assert recall == 1.0
    assert f1 == 1.0


def test_ner_scorer_handles_disjoint_predictions():
    """compute_micro_f1 returns F1 ~= 0.0 when predictions are disjoint from gold."""
    gold_by_doc = {
        "doc-1": [{"entity_text": "Boston", "entity_label": "LOC"}],
        "doc-2": [{"entity_text": "Acme Corp", "entity_label": "ORG"}],
    }
    predictions_by_doc = {
        "doc-1": [{"entity_text": "New York", "entity_label": "LOC"}],
        "doc-2": [{"entity_text": "Globex", "entity_label": "ORG"}],
    }

    precision, recall, f1 = ner_scorer.compute_micro_f1(predictions_by_doc, gold_by_doc)

    assert f1 == pytest.approx(0.0)


def test_cypher_normalizer_collapses_whitespace():
    """normalize_cypher collapses runs of whitespace to a single space."""
    raw = "MATCH   (n)\n RETURN  n"
    normalized = cypher_normalizer.normalize_cypher(raw)

    assert "  " not in normalized
    assert "\n" not in normalized
    assert normalized == "MATCH (n) RETURN n"


def test_cypher_normalizer_uppercases_keywords():
    """normalize_cypher uppercases the seven Cypher keywords case-insensitively."""
    raw = "match (n) where n.name = 'x' return n order by n.name limit 5"
    normalized = cypher_normalizer.normalize_cypher(raw)

    assert "MATCH" in normalized
    assert "WHERE" in normalized
    assert "RETURN" in normalized
    assert "ORDER BY" in normalized
    assert "LIMIT" in normalized
    assert "match" not in normalized
    assert "where" not in normalized


def test_grounding_scorer_excludes_declines():
    """is_decline returns True for the canonical decline string only."""
    decline_response = {"answer": "I cannot answer this from the available sources."}
    normal_response = {"answer": "Hello"}

    assert grounding_scorer.is_decline(decline_response) is True
    assert grounding_scorer.is_decline(normal_response) is False


def test_grounding_scorer_denominator_excludes_declined():
    """Given 10 answered + 5 declined items, the denominator = 10."""
    responses = (
        [{"answer": f"Some answer {i}"} for i in range(10)]
        + [{"answer": "I cannot answer this from the available sources."} for _ in range(5)]
    )

    declined_count = sum(1 for r in responses if grounding_scorer.is_decline(r))
    answered_count = sum(1 for r in responses if not grounding_scorer.is_decline(r))

    assert declined_count == 5
    assert answered_count == 10


def test_grounding_scorer_membership():
    """is_grounded requires every cited chunk_id to be in the candidate set."""
    candidates = {"chunk-1", "chunk-2", "chunk-3"}

    grounded_response = {
        "answer": "ok",
        "citations": [{"chunk_id": "chunk-1"}, {"chunk_id": "chunk-2"}],
    }
    assert grounding_scorer.is_grounded(grounded_response, candidates) is True

    ungrounded_response = {
        "answer": "ok",
        "citations": [{"chunk_id": "chunk-1"}, {"chunk_id": "ghost-chunk"}],
    }
    assert grounding_scorer.is_grounded(ungrounded_response, candidates) is False

    no_citations = {"answer": "ok", "citations": []}
    assert grounding_scorer.is_grounded(no_citations, candidates) is False