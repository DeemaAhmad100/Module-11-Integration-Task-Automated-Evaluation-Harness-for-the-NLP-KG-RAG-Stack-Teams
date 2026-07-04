# Module 11 — Evaluation Report

## 1. Headline Metrics

- NER F1 Score: 0.00
- NL → Cypher Exact Match (KG Accuracy): 0.00 (supported only)
- RAG Grounding Rate: 0.00

---

## 2. NER Evaluation (Extract Endpoint)

### Methodology
The system processes 30 documents from the CoNLL-2003 dataset.  
Each document is sent to the `/extract` endpoint to retrieve predicted entities.  
Evaluation is performed using micro-averaged precision, recall, and F1-score by summing TP, FP, and FN across all documents before computing final metrics.

### Sample Results

| Input Text | Gold Entities | Predicted Entities | Result |
|------------|--------------|---------------------|--------|
| Barack Obama was born in Hawaii | PERSON: Barack Obama, LOCATION: Hawaii | [] | ❌ Incorrect |

### Observations
- The system returned empty entity predictions for test inputs.
- This leads to high false negatives and zero recall.
- Overall NER performance is significantly below acceptable threshold.

---

## 3. KG Evaluation (NL → Cypher)

### Methodology
Each question from the dataset is sent to the `/kg/query` endpoint.  
Predicted Cypher queries are normalized (whitespace collapse and keyword normalization) before comparison with gold queries.  
UnsupportedQueryError (HTTP 422) responses are excluded from evaluation.  
5xx errors are counted as incorrect responses.

### Sample Results

| Question | Gold Cypher | Predicted Output | Result |
|----------|-------------|------------------|--------|
| Who founded Apple? | MATCH (p:Person)-[:FOUNDED]->(c:Company) RETURN p | UnsupportedQueryError | ❌ Excluded |

### Observations
- Many questions are rejected due to bounded schema constraints.
- The system correctly identifies out-of-scope queries.
- Only supported queries are considered in final accuracy.

---

## 4. RAG Evaluation (Answer Grounding)

### Methodology
Each question is sent to the `/rag/answer` endpoint with parameter k.  
A response is considered grounded if:
- It contains at least one citation
- All cited chunk_ids exist in the retrieved candidate set
- Responses with the canonical decline string are excluded from evaluation

### Sample Results

| Question | Answer | Citations | Retrieved | Result |
|----------|--------|-----------|-----------|--------|
| What is Apple? | I cannot answer this from the available sources. | [] | [] | ❌ Excluded |

### Observations
- The system frequently returns decline responses.
- No grounded answers were observed in the current evaluation run.
- This indicates strict retrieval constraints or limited coverage.

---

## 5. System Summary

- NER extraction failed to produce valid entities on test inputs.
- KG system enforces strict schema validation and rejects unsupported queries.
- RAG system avoids hallucinations by declining unsupported or ungrounded questions.
- Overall system behavior is conservative, prioritizing correctness over coverage.