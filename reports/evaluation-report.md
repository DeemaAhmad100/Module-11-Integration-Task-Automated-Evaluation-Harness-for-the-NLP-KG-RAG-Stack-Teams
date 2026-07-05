# M11 Integration -- Evaluation Report

## Headline

- **NER Precision**: 1.0000
- **NER Recall**: 1.0000
- **NER F1**: 1.0000
- **NL->Cypher Exact-Match**: 1.0000
- **RAG Grounding Rate**: 1.0000

## Per-Endpoint Detail

### NER (`/extract`) -- Per-Document Results

| document_id | predicted_entities | gold_entities | tp | fp | fn |
|---|---|---|---|---|---|
| doc-001 | [{'entity_text': 'Acme Corp', 'entity_label': 'ORG'}, {'entity_text': 'Globex', 'entity_label': 'ORG'}, {'entity_text': 'Boston', 'entity_label': 'LOC'}] | [{'entity_text': 'Acme Corp', 'entity_label': 'ORG'}, {'entity_text': 'Globex', 'entity_label': 'ORG'}, {'entity_text': 'Boston', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-002 | [{'entity_text': 'Jane Smith', 'entity_label': 'PER'}, {'entity_text': 'OpenAI', 'entity_label': 'ORG'}, {'entity_text': 'San Francisco', 'entity_label': 'LOC'}] | [{'entity_text': 'Jane Smith', 'entity_label': 'PER'}, {'entity_text': 'OpenAI', 'entity_label': 'ORG'}, {'entity_text': 'San Francisco', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-003 | [{'entity_text': 'Berlin', 'entity_label': 'LOC'}] | [{'entity_text': 'Berlin', 'entity_label': 'LOC'}] | 1 | 0 | 0 |
| doc-004 | [{'entity_text': 'Microsoft', 'entity_label': 'ORG'}, {'entity_text': 'Apple', 'entity_label': 'ORG'}] | [{'entity_text': 'Microsoft', 'entity_label': 'ORG'}, {'entity_text': 'Apple', 'entity_label': 'ORG'}] | 2 | 0 | 0 |
| doc-005 | [{'entity_text': 'Maria Garcia', 'entity_label': 'PER'}, {'entity_text': 'Paris', 'entity_label': 'LOC'}] | [{'entity_text': 'Maria Garcia', 'entity_label': 'PER'}, {'entity_text': 'Paris', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-006 | [{'entity_text': 'Google', 'entity_label': 'ORG'}, {'entity_text': 'Tokyo', 'entity_label': 'LOC'}] | [{'entity_text': 'Google', 'entity_label': 'ORG'}, {'entity_text': 'Tokyo', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-007 | [{'entity_text': 'Amazon Web Services', 'entity_label': 'ORG'}, {'entity_text': 'Seattle', 'entity_label': 'LOC'}] | [{'entity_text': 'Amazon Web Services', 'entity_label': 'ORG'}, {'entity_text': 'Seattle', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-008 | [{'entity_text': 'Elena Rossi', 'entity_label': 'PER'}, {'entity_text': 'MIT', 'entity_label': 'ORG'}] | [{'entity_text': 'Elena Rossi', 'entity_label': 'PER'}, {'entity_text': 'MIT', 'entity_label': 'ORG'}] | 2 | 0 | 0 |
| doc-009 | [{'entity_text': 'Tesla', 'entity_label': 'ORG'}, {'entity_text': 'Shanghai', 'entity_label': 'LOC'}] | [{'entity_text': 'Tesla', 'entity_label': 'ORG'}, {'entity_text': 'Shanghai', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-010 | [{'entity_text': 'Russia', 'entity_label': 'LOC'}, {'entity_text': 'India', 'entity_label': 'LOC'}, {'entity_text': 'Delhi', 'entity_label': 'LOC'}] | [{'entity_text': 'Russia', 'entity_label': 'LOC'}, {'entity_text': 'India', 'entity_label': 'LOC'}, {'entity_text': 'Delhi', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-011 | [{'entity_text': 'Bank of America', 'entity_label': 'ORG'}, {'entity_text': 'New York', 'entity_label': 'LOC'}] | [{'entity_text': 'Bank of America', 'entity_label': 'ORG'}, {'entity_text': 'New York', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-012 | [{'entity_text': 'Nvidia', 'entity_label': 'ORG'}, {'entity_text': 'Intel', 'entity_label': 'ORG'}] | [{'entity_text': 'Nvidia', 'entity_label': 'ORG'}, {'entity_text': 'Intel', 'entity_label': 'ORG'}] | 2 | 0 | 0 |
| doc-013 | [{'entity_text': 'Pedro Alvarez', 'entity_label': 'PER'}, {'entity_text': 'IBM', 'entity_label': 'ORG'}, {'entity_text': 'Madrid', 'entity_label': 'LOC'}] | [{'entity_text': 'Pedro Alvarez', 'entity_label': 'PER'}, {'entity_text': 'IBM', 'entity_label': 'ORG'}, {'entity_text': 'Madrid', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-014 | [{'entity_text': 'World Bank', 'entity_label': 'ORG'}, {'entity_text': 'Africa', 'entity_label': 'LOC'}] | [{'entity_text': 'World Bank', 'entity_label': 'ORG'}, {'entity_text': 'Africa', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-015 | [{'entity_text': 'Sarah Johnson', 'entity_label': 'PER'}, {'entity_text': 'London', 'entity_label': 'LOC'}, {'entity_text': 'Sydney', 'entity_label': 'LOC'}] | [{'entity_text': 'Sarah Johnson', 'entity_label': 'PER'}, {'entity_text': 'London', 'entity_label': 'LOC'}, {'entity_text': 'Sydney', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-016 | [{'entity_text': 'Reuters', 'entity_label': 'ORG'}, {'entity_text': 'BP', 'entity_label': 'ORG'}, {'entity_text': 'Shell', 'entity_label': 'ORG'}] | [{'entity_text': 'Reuters', 'entity_label': 'ORG'}, {'entity_text': 'BP', 'entity_label': 'ORG'}, {'entity_text': 'Shell', 'entity_label': 'ORG'}] | 3 | 0 | 0 |
| doc-017 | [{'entity_text': 'Carlos Mendes', 'entity_label': 'PER'}, {'entity_text': 'Petrobras', 'entity_label': 'ORG'}] | [{'entity_text': 'Carlos Mendes', 'entity_label': 'PER'}, {'entity_text': 'Petrobras', 'entity_label': 'ORG'}] | 2 | 0 | 0 |
| doc-018 | [{'entity_text': 'Toyota', 'entity_label': 'ORG'}, {'entity_text': 'Aichi', 'entity_label': 'LOC'}] | [{'entity_text': 'Toyota', 'entity_label': 'ORG'}, {'entity_text': 'Aichi', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-019 | [{'entity_text': 'Federal Reserve', 'entity_label': 'ORG'}, {'entity_text': 'Washington', 'entity_label': 'LOC'}] | [{'entity_text': 'Federal Reserve', 'entity_label': 'ORG'}, {'entity_text': 'Washington', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-020 | [{'entity_text': 'Linda Park', 'entity_label': 'PER'}, {'entity_text': 'Samsung', 'entity_label': 'ORG'}, {'entity_text': 'Seoul', 'entity_label': 'LOC'}] | [{'entity_text': 'Linda Park', 'entity_label': 'PER'}, {'entity_text': 'Samsung', 'entity_label': 'ORG'}, {'entity_text': 'Seoul', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-021 | [{'entity_text': 'Volkswagen', 'entity_label': 'ORG'}, {'entity_text': 'Germany', 'entity_label': 'LOC'}, {'entity_text': 'Mexico', 'entity_label': 'LOC'}] | [{'entity_text': 'Volkswagen', 'entity_label': 'ORG'}, {'entity_text': 'Germany', 'entity_label': 'LOC'}, {'entity_text': 'Mexico', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-022 | [{'entity_text': 'Ahmed Hassan', 'entity_label': 'PER'}, {'entity_text': 'Cairo University', 'entity_label': 'ORG'}] | [{'entity_text': 'Ahmed Hassan', 'entity_label': 'PER'}, {'entity_text': 'Cairo University', 'entity_label': 'ORG'}] | 2 | 0 | 0 |
| doc-023 | [{'entity_text': 'Goldman Sachs', 'entity_label': 'ORG'}, {'entity_text': 'JP Morgan', 'entity_label': 'ORG'}, {'entity_text': 'Wall Street', 'entity_label': 'LOC'}] | [{'entity_text': 'Goldman Sachs', 'entity_label': 'ORG'}, {'entity_text': 'JP Morgan', 'entity_label': 'ORG'}, {'entity_text': 'Wall Street', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-024 | [{'entity_text': 'Olivia Brown', 'entity_label': 'PER'}, {'entity_text': 'Pfizer', 'entity_label': 'ORG'}, {'entity_text': 'Moderna', 'entity_label': 'ORG'}] | [{'entity_text': 'Olivia Brown', 'entity_label': 'PER'}, {'entity_text': 'Pfizer', 'entity_label': 'ORG'}, {'entity_text': 'Moderna', 'entity_label': 'ORG'}] | 3 | 0 | 0 |
| doc-025 | [{'entity_text': 'Florida', 'entity_label': 'LOC'}, {'entity_text': 'Cuba', 'entity_label': 'LOC'}] | [{'entity_text': 'Florida', 'entity_label': 'LOC'}, {'entity_text': 'Cuba', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-026 | [{'entity_text': 'Spotify', 'entity_label': 'ORG'}, {'entity_text': 'Stockholm', 'entity_label': 'LOC'}] | [{'entity_text': 'Spotify', 'entity_label': 'ORG'}, {'entity_text': 'Stockholm', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-027 | [{'entity_text': 'Hiroshi Tanaka', 'entity_label': 'PER'}, {'entity_text': 'Sony', 'entity_label': 'ORG'}, {'entity_text': 'Osaka', 'entity_label': 'LOC'}] | [{'entity_text': 'Hiroshi Tanaka', 'entity_label': 'PER'}, {'entity_text': 'Sony', 'entity_label': 'ORG'}, {'entity_text': 'Osaka', 'entity_label': 'LOC'}] | 3 | 0 | 0 |
| doc-028 | [{'entity_text': 'Walmart', 'entity_label': 'ORG'}, {'entity_text': 'Canada', 'entity_label': 'LOC'}] | [{'entity_text': 'Walmart', 'entity_label': 'ORG'}, {'entity_text': 'Canada', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-029 | [{'entity_text': 'Disney', 'entity_label': 'ORG'}, {'entity_text': 'Orlando', 'entity_label': 'LOC'}] | [{'entity_text': 'Disney', 'entity_label': 'ORG'}, {'entity_text': 'Orlando', 'entity_label': 'LOC'}] | 2 | 0 | 0 |
| doc-030 | [{'entity_text': 'Naomi Foster', 'entity_label': 'PER'}, {'entity_text': 'Stanford', 'entity_label': 'ORG'}, {'entity_text': 'Berkeley', 'entity_label': 'ORG'}] | [{'entity_text': 'Naomi Foster', 'entity_label': 'PER'}, {'entity_text': 'Stanford', 'entity_label': 'ORG'}, {'entity_text': 'Berkeley', 'entity_label': 'ORG'}] | 3 | 0 | 0 |

**Sample NER Failures:**

- {'document_id': 'doc-001', 'predicted_entities': [{'entity_text': 'Acme Corp', 'entity_label': 'ORG'}, {'entity_text': 'Globex', 'entity_label': 'ORG'}, {'entity_text': 'Boston', 'entity_label': 'LOC'}], 'gold_entities': [{'entity_text': 'Acme Corp', 'entity_label': 'ORG'}, {'entity_text': 'Globex', 'entity_label': 'ORG'}, {'entity_text': 'Boston', 'entity_label': 'LOC'}], 'tp': 3, 'fp': 0, 'fn': 0}
- {'document_id': 'doc-002', 'predicted_entities': [{'entity_text': 'Jane Smith', 'entity_label': 'PER'}, {'entity_text': 'OpenAI', 'entity_label': 'ORG'}, {'entity_text': 'San Francisco', 'entity_label': 'LOC'}], 'gold_entities': [{'entity_text': 'Jane Smith', 'entity_label': 'PER'}, {'entity_text': 'OpenAI', 'entity_label': 'ORG'}, {'entity_text': 'San Francisco', 'entity_label': 'LOC'}], 'tp': 3, 'fp': 0, 'fn': 0}
- {'document_id': 'doc-003', 'predicted_entities': [{'entity_text': 'Berlin', 'entity_label': 'LOC'}], 'gold_entities': [{'entity_text': 'Berlin', 'entity_label': 'LOC'}], 'tp': 1, 'fp': 0, 'fn': 0}

### NL->Cypher (`/kg/query`) -- Per-Question Results

| question_id | question | gold_cypher | predicted_cypher | status | passed |
|---|---|---|---|---|---|
| kg-001 | List all Italian restaurants in the North End. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Italian'}) WHERE r.neighborhood = 'North End' RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Italian'}) WHERE r.neighborhood = 'North End' RETURN r.name | scored | True |
| kg-002 | Which restaurants serve seafood? | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Seafood'}) RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Seafood'}) RETURN r.name | scored | True |
| kg-003 | Show neighborhoods that have a Thai restaurant. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Thai'}) RETURN DISTINCT r.neighborhood | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Thai'}) RETURN DISTINCT r.neighborhood | scored | True |
| kg-004 | Find all restaurants with a rating above 4.5. | MATCH (r:Restaurant) WHERE r.rating > 4.5 RETURN r.name ORDER BY r.rating DESC | MATCH (r:Restaurant) WHERE r.rating > 4.5 RETURN r.name ORDER BY r.rating DESC | scored | True |
| kg-005 | Which cuisines does Acme Bistro serve? | MATCH (r:Restaurant {name: 'Acme Bistro'})-[:SERVES]->(c:Cuisine) RETURN c.name | MATCH (r:Restaurant {name: 'Acme Bistro'})-[:SERVES]->(c:Cuisine) RETURN c.name | scored | True |
| kg-006 | List restaurants in Back Bay. | MATCH (r:Restaurant) WHERE r.neighborhood = 'Back Bay' RETURN r.name | MATCH (r:Restaurant) WHERE r.neighborhood = 'Back Bay' RETURN r.name | scored | True |
| kg-007 | Show all Mexican restaurants. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Mexican'}) RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Mexican'}) RETURN r.name | scored | True |
| kg-008 | Which restaurants have a price tier of $$? | MATCH (r:Restaurant) WHERE r.price_tier = '$$' RETURN r.name | MATCH (r:Restaurant) WHERE r.price_tier = '$$' RETURN r.name | scored | True |
| kg-009 | List the top 10 highest-rated restaurants. | MATCH (r:Restaurant) RETURN r.name ORDER BY r.rating DESC LIMIT 10 | MATCH (r:Restaurant) RETURN r.name ORDER BY r.rating DESC LIMIT 10 | scored | True |
| kg-010 | Find Chinese restaurants in Chinatown. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Chinese'}) WHERE r.neighborhood = 'Chinatown' RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Chinese'}) WHERE r.neighborhood = 'Chinatown' RETURN r.name | scored | True |
| kg-011 | What restaurants are open late? | MATCH (r:Restaurant) WHERE r.open_late = true RETURN r.name | MATCH (r:Restaurant) WHERE r.open_late = true RETURN r.name | scored | True |
| kg-012 | Show vegetarian options in Cambridge. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Vegetarian'}) WHERE r.neighborhood = 'Cambridge' RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Vegetarian'}) WHERE r.neighborhood = 'Cambridge' RETURN r.name | scored | True |
| kg-013 | Which neighborhoods have the most restaurants? | MATCH (r:Restaurant) WITH r.neighborhood AS hood, count(*) AS n RETURN hood ORDER BY n DESC LIMIT 5 | MATCH (r:Restaurant) WITH r.neighborhood AS hood, count(*) AS n RETURN hood ORDER BY n DESC LIMIT 5 | scored | True |
| kg-014 | List Japanese restaurants with rating above 4.0. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Japanese'}) WHERE r.rating > 4.0 RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Japanese'}) WHERE r.rating > 4.0 RETURN r.name | scored | True |
| kg-015 | Find pizza places in Beacon Hill. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Pizza'}) WHERE r.neighborhood = 'Beacon Hill' RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Pizza'}) WHERE r.neighborhood = 'Beacon Hill' RETURN r.name | scored | True |
| kg-016 | Show French restaurants. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'French'}) RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'French'}) RETURN r.name | scored | True |
| kg-017 | What is the average rating across all restaurants? | MATCH (r:Restaurant) RETURN avg(r.rating) | MATCH (r:Restaurant) RETURN avg(r.rating) | scored | True |
| kg-018 | Find Indian restaurants near MIT. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Indian'}) WHERE r.neighborhood = 'Cambridge' RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Indian'}) WHERE r.neighborhood = 'Cambridge' RETURN r.name | scored | True |
| kg-019 | List restaurants that serve both Italian and Mediterranean. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Italian'}) MATCH (r)-[:SERVES]->(:Cuisine {name: 'Mediterranean'}) RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Italian'}) MATCH (r)-[:SERVES]->(:Cuisine {name: 'Mediterranean'}) RETURN r.name | scored | True |
| kg-020 | Which neighborhoods have BBQ restaurants? | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'BBQ'}) RETURN DISTINCT r.neighborhood | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'BBQ'}) RETURN DISTINCT r.neighborhood | scored | True |
| kg-021 | Show Korean restaurants in Allston. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Korean'}) WHERE r.neighborhood = 'Allston' RETURN r.name | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Korean'}) WHERE r.neighborhood = 'Allston' RETURN r.name | scored | True |
| kg-022 | Which restaurants have outdoor seating? | MATCH (r:Restaurant) WHERE r.outdoor_seating = true RETURN r.name | MATCH (r:Restaurant) WHERE r.outdoor_seating = true RETURN r.name | scored | True |
| kg-023 | Compute the average price of an entree in the Italian cuisine category. | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Italian'}) RETURN avg(r.avg_entree_price) | MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Italian'}) RETURN avg(r.avg_entree_price) | scored | True |
| kg-024 | List restaurants by chef Maria Garcia. | MATCH (c:Chef {name: 'Maria Garcia'})-[:CHEF_AT]->(r:Restaurant) RETURN r.name | MATCH (c:Chef {name: 'Maria Garcia'})-[:CHEF_AT]->(r:Restaurant) RETURN r.name | scored | True |
| kg-025 | Find restaurants that only opened in the last year. | MATCH (r:Restaurant) WHERE r.opened_year >= 2025 RETURN r.name | None | excluded_unsupported | None |

**Sample KG Failures:**

- {'question_id': 'kg-001', 'question': 'List all Italian restaurants in the North End.', 'gold_cypher': "MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Italian'}) WHERE r.neighborhood = 'North End' RETURN r.name", 'predicted_cypher': "MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Italian'}) WHERE r.neighborhood = 'North End' RETURN r.name", 'status': 'scored', 'passed': True}
- {'question_id': 'kg-002', 'question': 'Which restaurants serve seafood?', 'gold_cypher': "MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Seafood'}) RETURN r.name", 'predicted_cypher': "MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Seafood'}) RETURN r.name", 'status': 'scored', 'passed': True}
- {'question_id': 'kg-003', 'question': 'Show neighborhoods that have a Thai restaurant.', 'gold_cypher': "MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Thai'}) RETURN DISTINCT r.neighborhood", 'predicted_cypher': "MATCH (r:Restaurant)-[:SERVES]->(:Cuisine {name: 'Thai'}) RETURN DISTINCT r.neighborhood", 'status': 'scored', 'passed': True}

### RAG (`/rag/answer`) -- Per-Question Results

| question_id | question | answer | citations | candidate_ids | status | passed |
|---|---|---|---|---|---|---|
| rag-001 | Which restaurants in the North End are known for Italian food? | Match for question_id=rag-001. | [{'chunk_id': 'chunk-italian-northend-1'}, {'chunk_id': 'chunk-italian-northend-2'}] | ['chunk-italian-northend-1', 'chunk-italian-northend-2'] | answered | True |
| rag-002 | What seafood restaurants are near the Boston waterfront? | Match for question_id=rag-002. | [{'chunk_id': 'chunk-seafood-1'}, {'chunk_id': 'chunk-waterfront-1'}] | ['chunk-seafood-1', 'chunk-waterfront-1'] | answered | True |
| rag-003 | Recommend Thai food in Allston. | Match for question_id=rag-003. | [{'chunk_id': 'chunk-thai-allston-1'}] | ['chunk-thai-allston-1'] | answered | True |
| rag-004 | Best brunch spots in Cambridge? | Match for question_id=rag-004. | [{'chunk_id': 'chunk-brunch-cambridge-1'}, {'chunk_id': 'chunk-brunch-cambridge-2'}] | ['chunk-brunch-cambridge-1', 'chunk-brunch-cambridge-2'] | answered | True |
| rag-005 | Where can I find good pizza in Beacon Hill? | Match for question_id=rag-005. | [{'chunk_id': 'chunk-pizza-bh-1'}] | ['chunk-pizza-bh-1'] | answered | True |
| rag-006 | Vegetarian-friendly restaurants near MIT? | Match for question_id=rag-006. | [{'chunk_id': 'chunk-veg-mit-1'}] | ['chunk-veg-mit-1'] | answered | True |
| rag-007 | Where to eat tapas in Boston? | Match for question_id=rag-007. | [{'chunk_id': 'chunk-tapas-1'}] | ['chunk-tapas-1'] | answered | True |
| rag-008 | Ramen in Back Bay? | Match for question_id=rag-008. | [{'chunk_id': 'chunk-ramen-bb-1'}] | ['chunk-ramen-bb-1'] | answered | True |
| rag-009 | Mexican restaurants in Jamaica Plain? | Match for question_id=rag-009. | [{'chunk_id': 'chunk-mexican-jp-1'}] | ['chunk-mexican-jp-1'] | answered | True |
| rag-010 | Where to find Ethiopian food? | Match for question_id=rag-010. | [{'chunk_id': 'chunk-ethiopian-1'}] | ['chunk-ethiopian-1'] | answered | True |
| rag-011 | Korean BBQ in Allston? | Match for question_id=rag-011. | [{'chunk_id': 'chunk-kbbq-allston-1'}] | ['chunk-kbbq-allston-1'] | answered | True |
| rag-012 | Late-night dining in Chinatown? | Match for question_id=rag-012. | [{'chunk_id': 'chunk-late-chinatown-1'}] | ['chunk-late-chinatown-1'] | answered | True |
| rag-013 | Best Sunday brunch downtown? | Match for question_id=rag-013. | [{'chunk_id': 'chunk-brunch-downtown-1'}] | ['chunk-brunch-downtown-1'] | answered | True |
| rag-014 | Greek restaurants in Brookline? | Match for question_id=rag-014. | [{'chunk_id': 'chunk-greek-brookline-1'}] | ['chunk-greek-brookline-1'] | answered | True |
| rag-015 | Where can I find good ice cream? | Match for question_id=rag-015. | [{'chunk_id': 'chunk-icecream-1'}] | ['chunk-icecream-1'] | answered | True |
| rag-016 | Fine dining for an anniversary? | Match for question_id=rag-016. | [{'chunk_id': 'chunk-finedining-1'}, {'chunk_id': 'chunk-finedining-2'}] | ['chunk-finedining-1', 'chunk-finedining-2'] | answered | True |
| rag-017 | Vegan options in Cambridge? | Match for question_id=rag-017. | [{'chunk_id': 'chunk-vegan-cam-1'}] | ['chunk-vegan-cam-1'] | answered | True |
| rag-018 | Best burgers in Somerville? | Match for question_id=rag-018. | [{'chunk_id': 'chunk-burgers-som-1'}] | ['chunk-burgers-som-1'] | answered | True |
| rag-019 | Where to get dim sum on a Sunday? | Match for question_id=rag-019. | [{'chunk_id': 'chunk-dimsum-1'}] | ['chunk-dimsum-1'] | answered | True |
| rag-020 | Family-friendly restaurants near Fenway? | Match for question_id=rag-020. | [{'chunk_id': 'chunk-fenway-family-1'}] | ['chunk-fenway-family-1'] | answered | True |

**Sample RAG Failures:**

- {'question_id': 'rag-001', 'question': 'Which restaurants in the North End are known for Italian food?', 'answer': 'Match for question_id=rag-001.', 'citations': [{'chunk_id': 'chunk-italian-northend-1'}, {'chunk_id': 'chunk-italian-northend-2'}], 'candidate_ids': ['chunk-italian-northend-1', 'chunk-italian-northend-2'], 'status': 'answered', 'passed': True}
- {'question_id': 'rag-002', 'question': 'What seafood restaurants are near the Boston waterfront?', 'answer': 'Match for question_id=rag-002.', 'citations': [{'chunk_id': 'chunk-seafood-1'}, {'chunk_id': 'chunk-waterfront-1'}], 'candidate_ids': ['chunk-seafood-1', 'chunk-waterfront-1'], 'status': 'answered', 'passed': True}
- {'question_id': 'rag-003', 'question': 'Recommend Thai food in Allston.', 'answer': 'Match for question_id=rag-003.', 'citations': [{'chunk_id': 'chunk-thai-allston-1'}], 'candidate_ids': ['chunk-thai-allston-1'], 'status': 'answered', 'passed': True}

## Methodologies

### NER F1

```
NER F1 evaluation harness for the M11 Integration.

Methodology (NER F1 -- token-level entity exact-match):

Filter the predictions to the document_ids present in the gold fixture
(`data/ner_conll30.json`); discard predictions for any other document_id. An
entity is a true positive (TP) iff a gold entity with the same `entity_text`
AND the same `entity_label` exists in the same `document_id` (string-equality
on `entity_text`; string-equality on `entity_label`; whitespace is not
normalized -- the M6 NER pipeline already returns trimmed entity text). An
entity in predictions with no matching gold entity is a false positive (FP).
A gold entity with no matching prediction is a false negative (FN). Compute
precision = TP / (TP + FP), recall = TP / (TP + FN), F1 = 2*P*R / (P + R).
Aggregate micro-averaged across documents -- sum TPs / FPs / FNs across all 30
documents, then compute. Threshold floor: F1 >= 0.65. NaN handling: if
TP + FP = 0, precision is 0; if TP + FN = 0, recall is 0; if both are 0, F1
is 0 (not NaN -- the report writes `0.0`, not `nan`).

This methodology paragraph appears verbatim in the integration spec, the
learner Integration Task page, and this docstring -- per the Evaluation
Methodology Rule.
```

### NL->Cypher Exact-Match

```
NL -> Cypher exact-match evaluation harness for the M11 Integration.

Methodology (NL -> Cypher exact-match -- post-normalization string equality):

Filter predictions to the question_ids in the gold fixture
(`data/kg_questions.json`). Normalize both predicted Cypher and gold Cypher
using `re.sub(r"\s+", " ", s).strip()` (whitespace collapse + leading/trailing
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
```

### RAG Grounding Rate

```
RAG grounding-rate evaluation harness for the M11 Integration.

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
```

## Derived /metrics Signals

| Endpoint | p95 Latency (s) | Error Rate | Request Count |
|---|---|---|---|
| /extract | 0.0049 | 0.0000 | 90.0 |
| /kg/query | 0.0047 | 0.0400 | 75.0 |
| /rag/answer | 0.0048 | 0.0000 | 60.0 |
