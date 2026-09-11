# erdos-ore-findings

**Results mined from a 30,438-object ore ledger and independently re-checked from scratch**, together with a substantially larger Pass-3 extraction from the historical MSL corpus.

The first independently recomputed results include the longest composite run below `10^6`, an infinite Pell family of square products, and explicit counterexamples to a binomial largest-prime-factor bound. Pass 3 then exposes **97 theorem-bearing families absent from the earlier comparison union**, containing **282 latest source states labelled `PROVED`**, plus curated gold results, cross-route deductions, proof repairs, and an exact Erdős #1093 divisor-engine snapshot.

Author: Jared Wilder. First public timestamp: 2026-09-11.

The source ledger records what the historical pipeline asserted; this repository separates that source status from recomputation and adjudication. A source label is therefore provenance, while the sections below state which objects were independently rechecked, which were promoted, and which failed.

---

## Release-day Pass-3 full-corpus extraction

`pass3-2026-09-02/` is a second, substantially larger extraction from the historical MSL corpus. The source index records **2,612 latest route/lemma states**, including **617 latest states labelled `PROVED` across 171 problem families**. The audit found **97 entire theorem-bearing families absent from the earlier comparison theorem union**, containing **282 latest `PROVED` states**.

Those workflow labels are not collapsed into a theorem count. The folder instead publishes status-bearing mathematical objects:

- all **29 curated Pass-3 gold results / reductions / repairs**;
- all **28 cross-route and cross-problem fusion deductions**;
- a **20-item adversarial close audit**;
- **six explicit proof repairs**;
- the promotion / attack queue;
- an exact Erdős #1093 divisor-engine snapshot through `k<=45`.

The strongest newly exposed structural package in that index is the **#1093 LCM divisor-window reduction together with the #890↔#1093 large-prime binomial bridge**. Historical novelty for those formulations remains a separate literature question.

---

## Verified here, from scratch

### Erdős 238 — the longest composite run below `10^6`

> the maximum run of consecutive composite integers in `[2,10^6]` is **113**, between the primes **492113** and **492227**, gap 114

**Re-checked with an independent sieve. Exact match:** the run is 492114 through 492226, bracketed by 492113 and 492227.

### Erdős 930 — an infinite Pell family of square products

The product identity is algebraic: `1·2·a·(a+1)` with `a=(x−1)/2` equals `(x²−1)/2`; Pell `x²−2s²=1` gives `x²−1=2s²`, so the product is `s²` for every Pell solution.

**Re-checked on five Pell solutions**, each an exact integer square:

| x | s | a | `1·2·a·(a+1)` |
|---:|---:|---:|---:|
| 3 | 2 | 1 | 4 = 2² |
| 17 | 12 | 8 | 144 = 12² |
| 99 | 70 | 49 | 4,900 = 70² |
| 577 | 408 | 288 | 166,464 = 408² |
| 3363 | 2378 | 1681 | 5,654,884 = 2378² |

This is an infinite family: the Pell equation has infinitely many solutions and the product identity is algebraic in each.

### Erdős 683 — explicit counterexamples with exact parameter scope

`C(9,2)=36` has largest prime factor 3, while `C(10,3)=120` has largest prime factor 5. These give explicit counterexamples to the stated lower-bound family at the parameter values below:

| witness | P | `c=1/2` | `c=3/4` | `c=1` |
|---|---:|---|---|---|
| `C(9,2)=36` | 3 | holds | refutes | refutes |
| `C(10,3)=120` | 5 | refutes | refutes | refutes |

The original object scoped the witnesses exactly this way, and the recomputation matches it.

---

## Audit finding: a source object labelled `PROVED` that fails recomputation

The same problem family contains a historical source object labelled `PROVED` asserting that `(10,5)` forces `c <= 0.20905`.

It does not. `C(10,5)=252`, whose largest prime factor is 7. The tested lower bound is `min(6,5^(1+c))`; that minimum never exceeds 6, so `P=7` satisfies the inequality for every `c`. The pair `(10,5)` therefore forces no such upper bound on `c`.

A second source object claims the `c=1/2` form for all `1 <= n <= 12`, which is directly contradicted by the independently recomputed `(10,3)` witness above. The counterexample survives; the universal source claim does not.

This failure is preserved because it changes how raw workflow labels in the ledger must be interpreted. It is **an audit result about the source status system**, not the headline for the mathematics that survived recomputation.

## What the larger audit establishes about source authority

The mining pass found several reasons to keep source labels separate from final mathematical authority:

- **54 of 362 rows** marked `VERIFIED` in a companion kernel-verdict table carry a non-zero exit code with a real error;
- **five `.lean` files** in a directory named `kernel-verified/` declare their own `axiom`;
- one declaration there reports `sorryAx` in its footprint;
- the 1,043 historical “multi-hop implication chains” are lexical stitchings rather than mathematical derivations.

These observations constrain how the raw ledger is read. They do not erase the independently recomputed results or the separately curated Pass-3 mathematical objects.

## Reproduce the independently checked results

`verify.py` recomputes every arithmetic claim on this page, including the failed source object, using only the Python standard library.

## License

Apache-2.0.
