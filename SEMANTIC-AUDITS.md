# Semantic audits of recovered mathematical claims

Author: Jared Wilder. Public release: 2026-09-11.

This page is the human-facing index for the numbered semantic audits in this repository. Historical filenames such as `SEMANTIC_COURT_02.md` are retained for provenance; they should be read simply as **audit 02**, **audit 03**, and so on.

Audits 02–08 now record **more than 30 concrete statement, scope, chronology, citation, or verification corrections** found while checking recovered claims against the mathematics itself.

The important point is symmetric: an old `PROVED` label can be wrong, but an old `FALSE` label can also be wrong. Chronology is evidence, not authority.

## What these audits test

The failures include:

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
- bounded computations or local formal checks promoted beyond their certified range;
- later `FALSE` labels based on incorrect counterexamples;
- endpoint exceptions omitted from otherwise correct theorems;
- mutually inconsistent finite values resolved by exact recomputation;
- interval-length / off-by-one mistakes used to manufacture counterexamples;
- citation-strength drift, where a real literature result is replaced by a quantitatively stronger statement it does not prove.

Where a correction can be checked cheaply, a regression script is stored beside the audit.

## Audit files

- [`SEMANTIC_COURT_02.md`](SEMANTIC_COURT_02.md) — open-problem / statement contamination audit.
- [`SEMANTIC_COURT_03.md`](SEMANTIC_COURT_03.md) — tail-contamination audit.
- [`SEMANTIC_COURT_04.md`](SEMANTIC_COURT_04.md) — maximum/citation/domain audit.
- [`SEMANTIC_COURT_05.md`](SEMANTIC_COURT_05.md) — low-score contamination audit.
- [`SEMANTIC_COURT_06.md`](SEMANTIC_COURT_06.md) — chronology repairs: false refutations, endpoint drift, and contradictory finite values.
- [`SEMANTIC_COURT_07.md`](SEMANTIC_COURT_07.md) — two false refutations in Erdős #394 caused by interval-length and endpoint mistakes.
- [`SEMANTIC_COURT_08_ERDOS829.md`](SEMANTIC_COURT_08_ERDOS829.md) — Erdős #829 citation audit: Mahler/Stewart lower bounds and additive-vs-Dirichlet convolution semantics.

The filenames are historical; the documents themselves are written as ordinary mathematical audits.

## Examples of repaired chronology

- **Erdős #602:** a claimed counterexample to the finite colouring theorem is itself invalid; the corrected theorem survives with the edge-size hypothesis.
- **Erdős #681:** `(n,k)=(250,3)` is a witness, not a counterexample, to the fourth-root necessary condition.
- **Erdős #456:** the prime-anchor theorem is correct for odd primes but has the endpoint exception `p=2`.
- **Erdős #390:** exact recomputation resolves contradictory historical values at `f(7)` in favor of `f(7)=20`.
- **Erdős #394:** `t_2(4)=3` and the endpoint `t_2(2)=1` both survive; the supposed refutations used the wrong interval length or misread the comparison value.
- **Erdős #829:** the recovered Mahler-based negative close is rejected; the actual recorded lower bounds remain fixed powers of `log n` and are compatible with the open polylogarithmic-upper-bound question.

## Relation to positive results

These audits are part of the integrity record. They do not define the value or status of unrelated mathematics in the same archive.

A failed claim should be corrected locally. A proved theorem elsewhere should continue to be described by its own statement and evidence. A false refutation should likewise be withdrawn when direct mathematics shows that the underlying theorem survives.
