"""Orchestrator -- runs the three eval harnesses, reads /metrics, writes report.

Usage:
    python eval_runner.py --output reports/evaluation-report.md
"""

import argparse
import os
import sys

import eval_ner
import eval_kg
import eval_rag
from lib import metrics_reader


ENDPOINTS = ["/extract", "/kg/query", "/rag/answer"]


def _render_table(rows: list) -> list:
    """Render a list of dicts as a generic Markdown table (safe on any keys)."""
    if not rows:
        return ["_(no rows)_", ""]
    columns = []
    for row in rows:
        for k in row.keys():
            if k not in columns:
                columns.append(k)
    lines = []
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("|" + "|".join(["---"] * len(columns)) + "|")
    for row in rows:
        cells = [str(row.get(c, "")) for c in columns]
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def _sample_failures(rows: list, n: int = 3) -> list:
    """Pick up to n rows to show as sample failures (prefer passed == False)."""
    failures = [r for r in rows if r.get("passed") is False]
    if len(failures) >= n:
        return failures[:n]
    # pad with any other rows so we always show something
    extra = [r for r in rows if r not in failures]
    return (failures + extra)[:n]


def assemble_report(ner_result, kg_result, rag_result, metrics_signals) -> str:
    """Return the Markdown report body."""
    ner_precision, ner_recall, ner_f1, ner_details = ner_result
    kg_rate, kg_details = kg_result
    rag_rate, rag_details = rag_result

    lines = []

    # ---- Headline ----
    lines.append("# M11 Integration -- Evaluation Report\n")
    lines.append("## Headline\n")
    lines.append(f"- **NER Precision**: {ner_precision:.4f}")
    lines.append(f"- **NER Recall**: {ner_recall:.4f}")
    lines.append(f"- **NER F1**: {ner_f1:.4f}")
    lines.append(f"- **NL->Cypher Exact-Match**: {kg_rate:.4f}")
    lines.append(f"- **RAG Grounding Rate**: {rag_rate:.4f}\n")

    # ---- Per-Endpoint Detail ----
    lines.append("## Per-Endpoint Detail\n")

    # NER -- endpoint /extract
    lines.append("### NER (`/extract`) -- Per-Document Results\n")
    lines.extend(_render_table(ner_details))
    lines.append("")
    lines.append("**Sample NER Failures:**\n")
    for d in _sample_failures(ner_details):
        lines.append(f"- {d}")
    lines.append("")

    # KG -- endpoint /kg/query
    lines.append("### NL->Cypher (`/kg/query`) -- Per-Question Results\n")
    lines.extend(_render_table(kg_details))
    lines.append("")
    lines.append("**Sample KG Failures:**\n")
    for d in _sample_failures(kg_details):
        lines.append(f"- {d}")
    lines.append("")

    # RAG -- endpoint /rag/answer
    lines.append("### RAG (`/rag/answer`) -- Per-Question Results\n")
    lines.extend(_render_table(rag_details))
    lines.append("")
    lines.append("**Sample RAG Failures:**\n")
    for d in _sample_failures(rag_details):
        lines.append(f"- {d}")
    lines.append("")

    # ---- Methodologies (copied verbatim from docstrings) ----
    lines.append("## Methodologies\n")
    lines.append("### NER F1\n")
    lines.append(f"```\n{eval_ner.__doc__.strip()}\n```\n")
    lines.append("### NL->Cypher Exact-Match\n")
    lines.append(f"```\n{eval_kg.__doc__.strip()}\n```\n")
    lines.append("### RAG Grounding Rate\n")
    lines.append(f"```\n{eval_rag.__doc__.strip()}\n```\n")

    # ---- Derived /metrics Signals ----
    lines.append("## Derived /metrics Signals\n")
    lines.append("| Endpoint | p95 Latency (s) | Error Rate | Request Count |")
    lines.append("|---|---|---|---|")
    for endpoint, signals in metrics_signals.items():
        lines.append(
            f"| {endpoint} | {signals['p95']:.4f} | {signals['error_rate']:.4f} | {signals['count']} |"
        )
    lines.append("")

    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="reports/evaluation-report.md",
        help="Where to write the Markdown report.",
    )
    args = parser.parse_args(argv)

    ner_result = eval_ner.run()
    kg_result = eval_kg.run()
    rag_result = eval_rag.run()

    metrics_signals = {}
    for endpoint in ENDPOINTS:
        metrics_signals[endpoint] = {
            "p95": metrics_reader.get_p95_latency(endpoint),
            "error_rate": metrics_reader.get_error_rate(endpoint),
            "count": metrics_reader.get_request_count(endpoint),
        }

    report = assemble_report(ner_result, kg_result, rag_result, metrics_signals)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as fh:
        fh.write(report)

    print(f"Report written to {args.output}")
    print(f"NER F1={ner_result[2]:.4f}  KG EM={kg_result[0]:.4f}  RAG Grounding={rag_result[0]:.4f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())