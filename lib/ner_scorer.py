"""F1 scoring functions for the NER evaluation harness.

See eval_ner.py module docstring for the full methodology.
"""

from typing import Dict, List, Tuple


def score_document(pred: List[dict], gold: List[dict]) -> Tuple[int, int, int]:
    """Score a single document's predictions against gold entities.

    An entity is a true positive iff a gold entity with the same
    entity_text AND entity_label exists in the predicted set (string-equality,
    no whitespace normalization).

    Returns (tp, fp, fn).
    """
    pred_set = {(e["entity_text"], e["entity_label"]) for e in pred}
    gold_set = {(e["entity_text"], e["entity_label"]) for e in gold}

    tp = len(pred_set & gold_set)          
    fp = len(pred_set - gold_set)         
    fn = len(gold_set - pred_set)       

    return tp, fp, fn


def compute_micro_f1(
    predictions_by_doc: Dict[str, List[dict]],
    gold_by_doc: Dict[str, List[dict]],
) -> Tuple[float, float, float]:
    """Compute micro-averaged precision, recall, F1 across all documents.

    Sums TP/FP/FN across all documents in gold_by_doc, then computes once.
    Returns (precision, recall, f1). Never returns NaN -- 0.0 when the
    denominator is 0.
    """
    total_tp = 0
    total_fp = 0
    total_fn = 0

    for doc_id, gold_entities in gold_by_doc.items():
        pred_entities = predictions_by_doc.get(doc_id, [])
        tp, fp, fn = score_document(pred_entities, gold_entities)
        total_tp += tp
        total_fp += fp
        total_fn += fn

    precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
    recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0

    if precision + recall > 0:
        f1 = 2 * precision * recall / (precision + recall)
    else:
        f1 = 0.0

    return precision, recall, f1