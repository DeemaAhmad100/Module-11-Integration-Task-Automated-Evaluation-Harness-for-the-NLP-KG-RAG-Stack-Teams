"""Cypher normalization for the NL -> Cypher exact-match harness.

Per the integration spec methodology paragraph (NL -> Cypher exact-match):
collapse whitespace, strip leading/trailing whitespace, then case-insensitively
uppercase the seven Cypher keywords (MATCH, RETURN, WHERE, OPTIONAL, WITH,
LIMIT, ORDER BY). After normalization, two strings are exact-match iff they
are byte-equal.

The split between this module and eval_kg.py exists so the normalization logic
is unit-testable without a live backend.
"""

import re


KEYWORDS = (
    "MATCH",
    "RETURN",
    "WHERE",
    "OPTIONAL",
    "WITH",
    "LIMIT",
    "ORDER BY",
)


def normalize_cypher(s: str) -> str:
    """Return `s` normalized per the integration spec methodology: whitespace
    collapse and keyword uppercasing. See the module docstring for the full
    methodology paragraph.
    """
    normalized = re.sub(r"\s+", " ", s).strip()

    for keyword in KEYWORDS:
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        normalized = pattern.sub(keyword, normalized)

    return normalized