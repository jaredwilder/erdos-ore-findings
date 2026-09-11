# MSL Pass 3 — Full-Corpus Pure-Math Mining Release

**Author:** Jared Wilder  
**Source snapshot:** `MSL_PASS3_INDEX_FINAL_2026-09-02.xlsx`  
**Public release extraction:** 2026-09-11

This directory publishes the pure-mathematics payload of the Pass-3 corpus-mining index without
promoting source labels beyond their evidence.

## Scale

The source workbook records:

- **2,612** latest route/lemma states;
- **617** latest states labelled `PROVED`;
- **171** problem families containing at least one latest `PROVED` state;
- **97** entire problem families omitted from the earlier comparison theorem union;
- **282** latest `PROVED` states inside those 97 omitted families;
- **1,238** raw historical `PROVED` events;
- **1,428** contradictory status histories requiring adjudication;
- **29** curated Pass-3 gold items;
- **28** fusion rows;
- **20** close-shaped claims audited;
- **6** explicit proof repairs;
- an exact Erdős #1093 divisor engine through `k <= 45`.

That is the important release-day finding: the public theorem estate was not merely missing a few
notes. A comparison union previously treated as broad had omitted **97 theorem-bearing families**.

## Authority classes

This release preserves several distinct things:

1. `LATEST-PROVED.csv` is a **source-state ledger**, not independent certification. `PROVED` means
   the campaign registry's latest state says proved.
2. `OMITTED97.csv` is the subset proving the coverage hole: 282 latest `PROVED` states from 97
   families absent from the earlier theorem union.
3. `PASS3-GOLD.md` is the curated mathematical review. Each row states its own proof and novelty
   status.
4. `FUSIONS.md` contains cross-route/cross-problem deductions and repairs.
5. `CLOSE-AUDIT.md` is deliberately adversarial: false closes, semantic mismatches, stale proof
   labels, and known/special-case closes are kept rather than erased.
6. `PROOF-REPAIRS.md` records conclusions whose original proof was defective, together with the
   repaired argument where one was found.
7. `ERDOS1093-ENGINE.csv` is an exact finite computation snapshot, not a global theorem.

No row becomes historically novel because it is public here. No open Erdős problem is declared
closed unless the exact claim and proof independently earn that status.

## IP boundary

Only pure mathematics from the Erdős/MSL corpus is included. Biomedical, clinical, patent,
commercial, and proprietary-system material is intentionally excluded.

## Highest-priority mathematics

The source audit singled out two linked results as its highest-value Pass-3 discovery:

- **Erdős #1093 — LCM divisor-window reduction.** For an admissible `(n,k)`, the deficiency is
  exactly the number of divisors of `L_k = lcm(1,...,k)` in `(n-k,n]`.
- **Erdős #890 ↔ #1093 — large-prime binomial bridge.**
  `sum_(i<k) omega_k(n+i) = omega_{>k}(C(n+k-1,k))`, with the deficiency/excess identity
  `S_k = k - d + E`.

Those are published here as theorem/reduction candidates at the exact authority recorded in the
source review, not as claims of literature priority.

## Files

- `PASS3-GOLD.md` — 29 curated results/reductions/repairs.
- `FUSIONS.md` — 28 synthesis rows.
- `CLOSE-AUDIT.md` — 20 close-shaped claims and their adjudication.
- `PROOF-REPAIRS.md` — 6 explicit proof corrections.
- `ACTIONS.md` — promotion/formalization queue.
- `PROBLEM-ATLAS.csv` — per-problem coverage summary.
- `OMITTED97.csv` — 282 latest `PROVED` states from the 97 omitted families.
- `LATEST-PROVED.csv` — all 617 latest `PROVED` states.
- `ERDOS1093-ENGINE.csv` — exact divisor-engine output through `k <= 45`.

## License

Apache-2.0 for repository-authored material unless otherwise stated.
