# Semantic audits of recovered mathematical claims

Author: Jared Wilder. Public release: 2026-09-11.

This page is the human-facing index for the numbered semantic audits in this repository. Historical filenames such as `SEMANTIC_COURT_02.md` are retained for provenance; they should be read simply as **audit 02**, **audit 03**, and so on.

Across audits 02–05, the release records **25 distinct contamination / misstatement cases** found while checking recovered claims against their actual mathematics.

## What these audits test

The failures are not one generic category. They include:

- max/min or quantifier inversion;
- existential statements accidentally promoted to universal ones;
- additive convolution confused with multiplicative convolution;
- finite constructions treated as infinite without a gluing theorem;
- an `L^2` statement used as if it were `L^∞`;
- a fixed-bound hypothesis dropped from a literature theorem;
- reciprocal or asymptotic inequalities reversed;
- source-text corruption that changes the intended problem;
- endpoint facts extrapolated into asymptotic laws;
- interval membership confused with divisibility;
- results over integer bases transferred to rational bases without proof;
- bounded computations or local formal checks promoted beyond their certified range.

Where a correction can be checked cheaply, a regression script is stored beside the audit.

## Audit files

- [`SEMANTIC_COURT_02.md`](SEMANTIC_COURT_02.md) — open-problem / statement contamination audit.
- [`SEMANTIC_COURT_03.md`](SEMANTIC_COURT_03.md) — tail-contamination audit.
- [`SEMANTIC_COURT_04.md`](SEMANTIC_COURT_04.md) — maximum/citation/domain audit.
- [`SEMANTIC_COURT_05.md`](SEMANTIC_COURT_05.md) — low-score contamination audit.

The filenames are historical. The mathematical purpose is ordinary: identify which statement was wrong, explain why, give the corrected statement where one survives, and add an executable regression check when practical.

## Relation to positive results

These audits are part of the integrity record. They do not define the value or status of unrelated mathematics in the same archive.

A failed claim should be corrected locally. A proved theorem elsewhere should continue to be described by its own statement and evidence.
