# Mathematical results recovered from the MSL ore archive

A re-examination of a **30,438-object historical research ledger**, with selected results independently recomputed from scratch and a larger second extraction used to recover mathematics that earlier indexes had missed.

The first recomputed results include the longest composite run below `10^6`, an infinite Pell family of square products, and explicit counterexamples to a binomial largest-prime-factor bound. The larger extraction also identified **97 mathematical families absent from the earlier theorem index**, containing **282 historical records labelled `PROVED`** that required statement-by-statement review rather than automatic promotion.

Author: Jared Wilder. First public timestamp: 2026-09-11.

The historical ledger records what the original research workflow said at the time. This repository separates those old status labels from present mathematical verification.

## Larger corpus extraction

Historical directory: `pass3-2026-09-02/`.

The source archive contains **2,612 latest route/lemma records**, including **617 latest records labelled `PROVED` across 171 problem families**. The second extraction found **97 entire mathematical families missing from the earlier comparison index**, accounting for **282** of those historical `PROVED` labels.

Rather than treating those labels as a theorem count, the public extraction organizes the mathematics into reviewed objects:

- **29** curated results, reductions, or repairs;
- **28** deductions combining information from different routes or problems;
- **20** audits of claimed problem closures;
- **6** explicit proof repairs;
- a queue of statements still requiring mathematical review;
- an exact Erdős #1093 divisor-engine snapshot through `k<=45`.

The strongest structural package recovered here is the **Erdős #1093 LCM divisor-window reduction together with the #890↔#1093 large-prime binomial bridge**. Historical novelty of those formulations remains a literature question.

## Independently recomputed results

### Erdős 238 — longest composite run below `10^6`

The maximum run of consecutive composite integers in `[2,10^6]` has length **113**:

```text
492114, ..., 492226
```

bracketed by the primes **492113** and **492227**, a prime gap of 114.

An independent sieve reproduces the result exactly.

### Erdős 930 — infinite Pell family of square products

Let `a=(x−1)/2`. Then

```text
1·2·a·(a+1) = (x²−1)/2.
```

If `x²−2s²=1`, then `x²−1=2s²`, so the product equals `s²`. Because the Pell equation has infinitely many solutions, this gives an infinite family.

Five exact examples were recomputed:

| x | s | a | `1·2·a·(a+1)` |
|---:|---:|---:|---:|
| 3 | 2 | 1 | 4 = 2² |
| 17 | 12 | 8 | 144 = 12² |
| 99 | 70 | 49 | 4,900 = 70² |
| 577 | 408 | 288 | 166,464 = 408² |
| 3363 | 2378 | 1681 | 5,654,884 = 2378² |

### Erdős 683 — explicit counterexamples

`C(9,2)=36` has largest prime factor 3, while `C(10,3)=120` has largest prime factor 5. For the tested lower-bound family:

| witness | P | `c=1/2` | `c=3/4` | `c=1` |
|---|---:|---|---|---|
| `C(9,2)=36` | 3 | holds | refutes | refutes |
| `C(10,3)=120` | 5 | refutes | refutes | refutes |

The historical record stated exactly those parameter ranges, and the recomputation agrees.

## A historical `PROVED` label that fails recomputation

The same problem family contains an old record labelled `PROVED` claiming that `(10,5)` forces `c <= 0.20905`.

It does not. `C(10,5)=252`, whose largest prime factor is 7. The tested lower bound is `min(6,5^(1+c))`, which never exceeds 6, so `P=7` satisfies the inequality for every `c`. The pair `(10,5)` therefore forces no such upper bound.

A second old record claims the `c=1/2` form for all `1<=n<=12`; the independently recomputed `(10,3)` counterexample above disproves that universal statement.

This is why the repository distinguishes historical workflow labels from mathematical verification.

## What the source audit found

Several additional checks show why raw archive labels must be read cautiously:

- **54 of 362** rows marked `VERIFIED` in a companion kernel table have non-zero exit codes with actual errors;
- **five Lean files** stored under a historical `kernel-verified/` directory declare their own axioms;
- one declaration reports `sorryAx` in its axiom footprint;
- 1,043 historical “multi-hop implication chains” are lexical links between repeated text, not mathematical derivations.

These findings concern the old archive's metadata. They do not change the independently recomputed results or the separately reviewed mathematical extractions.

## Reproduce the arithmetic

`verify.py` recomputes the arithmetic claims on this page—including the failed historical claim—using only the Python standard library.

## License

Apache-2.0.