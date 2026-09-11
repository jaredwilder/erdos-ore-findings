# erdos-ore-findings

**Results mined out of a 30,438-object ore ledger and independently re-checked from scratch:**
the longest composite run below 10^6, an infinite Pell family of square products, and explicit
counterexamples to a binomial largest-prime-factor bound.

One `PROVED` object in the same sample did not survive recomputation, and it is published here
beside the ones that did.

Author: Jared Wilder. First public timestamp: 2026-09-11.

An automated pass over this project's own output produced an ore ledger: 30,438 objects, each with
a canonical statement and a `claimed_status` recording what the *source* asserted. **A claimed
status is a lead, not a verdict.** Everything below was recomputed from scratch before it was
written down, and the one claim that failed that recomputation is published beside the ones that
passed.

---

## Release-day Pass-3 full-corpus extraction

`pass3-2026-09-02/` is a second, substantially larger extraction from the historical MSL corpus.
The source index records **2,612 latest route/lemma states**, including **617 latest states labelled
`PROVED` across 171 problem families**. Most importantly, the audit found **97 entire theorem-bearing
families absent from the earlier comparison theorem union**, containing **282 latest `PROVED`
states**.

This does **not** mean there are 617 independently certified new theorems. The folder deliberately
separates source labels from adjudicated mathematics. It currently publishes:

- all 29 curated Pass-3 gold results/reductions/repairs;
- all 28 cross-route/cross-problem fusion deductions;
- a 20-item adversarial close audit;
- six explicit proof repairs;
- the promotion/attack queue;
- an exact Erdős #1093 divisor-engine snapshot through `k<=45`.

The strongest newly exposed structural package in that index is the #1093 LCM divisor-window
reduction together with the #890↔#1093 large-prime binomial bridge. Historical novelty for those
formulations remains explicitly unresolved.

---

## Verified here, from scratch

### Erdős 238 — the longest composite run below 10⁶

> the maximum run of consecutive composite integers in [2, 10⁶] is **113**, between the primes
> **492113** and **492227**, gap 114

**Re-checked with an independent sieve. Exact match**: the run is 492114 through 492226, bracketed
by 492113 and 492227.

### Erdős 930 — an infinite Pell family of square products

> the product identity is algebraic: `1·2·a·(a+1)` with `a = (x−1)/2` equals `(x²−1)/2`, and Pell
> `x² − 2s² = 1` gives `x² − 1 = 2s²`, so the product is `s²` for **all** solutions

**Re-checked on five Pell solutions**, each an exact integer square:

| x | s | a | 1·2·a·(a+1) | |
|---|---|---|---|---|
| 3 | 2 | 1 | 4 | = 2² |
| 17 | 12 | 8 | 144 | = 12² |
| 99 | 70 | 49 | 4,900 | = 70² |
| 577 | 408 | 288 | 166,464 | = 408² |
| 3363 | 2378 | 1681 | 5,654,884 | = 2378² |

This is a genuine infinite family, not a finite sweep — the Pell equation has infinitely many
solutions and the identity is algebraic in each.

### Erdős 683 — explicit counterexamples, correctly scoped

> `C(9,2) = 36` has largest prime factor 3, and `C(10,3) = 120` has largest prime factor 5 —
> refuting `P(C(n,k)) ≥ min(n−k+1, k^(1+c))`

**Re-checked, and the scoping in the original object is exactly right**, which is worth saying
because it would have been easy to overclaim:

| witness | P | c = 1/2 | c = 3/4 | c = 1 |
|---|---|---|---|---|
| C(9,2) = 36 | 3 | **holds** (3 > 2.828) | refutes | refutes |
| C(10,3) = 120 | 5 | refutes | refutes | refutes |

The original object claimed (9,2) for c ∈ {3/4, 1} and (10,3) for c ∈ {1/2, 3/4, 1}. That is
precisely what the arithmetic gives. It did **not** claim (9,2) at c = 1/2, where the inequality
survives.

---

## One `PROVED` object that is FALSE

The same problem carries this, with `claimed_status: PROVED`:

> "c ≤ log₅(7/5) forced by (10,5); outward interval verifier gives log₅(7/5) ∈ [0.20905, 0.20906],
> so **c ≤ 0.20905**"

**It does not follow.** `C(10,5) = 252`, whose largest prime factor is **7**. The inequality asks
whether `P ≥ min(n−k+1, k^(1+c)) = min(6, 5^(1+c))`. Since `n−k+1 = 6`, the minimum can never
exceed 6, and `P = 7 > 6` **for every c**:

| c | min(6, 5^(1+c)) | P = 7 | inequality |
|---|---|---|---|
| 0 | 5.000 | 7 | holds |
| 0.20905 | 6.000 | 7 | holds |
| 0.5 | 6.000 | 7 | holds |
| 1.0 | 6.000 | 7 | **holds** |

The pair (10,5) forces nothing on `c`. The derived constant 0.20905 has no support from this
witness.

A second object on the same problem, `2c60fc4ea15ed5a6`, claims `P ≥ min(n−k+1, k^(3/2))` for
**all** 1 ≤ n ≤ 12 — which directly contradicts the (10,3) counterexample above, confirmed here.
**Both cannot be true. The counterexample is the one that survives recomputation.**

---

## What this says about the ore as a source

The automated pass that produced this ledger is a **lead generator, not an authority**. In this
sample it produced findings that recompute exactly, a counterexample that was scoped more carefully
than it needed to be, and a false `PROVED` object sitting next to a claim that contradicts it.

The audit that accompanied this mining pass found more of the same shape and is worth stating here
because it constrains how the rest of the ledger should be read:

- **54 of 362 rows** marked `VERIFIED` in the companion kernel-verdict table carry a non-zero exit
  code with a real error — unsolved goals, parse failures, type mismatches. Check `exit_code`
  before citing any row as verified.
- **Five `.lean` files** in a directory named `kernel-verified/` declare their own `axiom`.
- One declaration there, `tK` on Erdős 101, reports `depends on axioms: [propext, sorryAx,
  Quot.sound]` — so any claim resting on it is not kernel-clean.
- The 1,043 "multi-hop implication chains" in the same corpus are **lexical stitchings**, not
  derivations: in the length-2 chains both steps are the same sentence from two copies of one file.

None of that material is published anywhere, and no repository cites the 362 figure.

## Reproduce everything above

`verify.py` recomputes every claim on this page, including the false one, and prints the table. It
uses only the Python standard library.

## License

Apache-2.0.
