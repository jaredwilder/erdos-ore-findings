# How an automated pipeline produced clean-looking proofs of nothing

An audit of 6,824 ore objects on Erdős problems 301–700, with every arithmetic claim
re-derived independently. Four claims marked `PROVED` are false, and the mechanism that
made them look verified is identified and named.

Author: Jared Wilder. 2026-09-11.

---

## The mechanism

Of 86 Lean verification receipts in this range, 81 report `status: VERIFIED, exitCode: 0,
errors: []`. Five report **`status: VERIFIED_PARTIAL, exitCode: 1`**.

In **every one of those five**, the headline declaration appears in the receipt's own
`verified_clean_declarations` list, marked `"clean": true, "axioms": []`.

It is listed as clean **because it never elaborated.**

`#print axioms` returns nothing for a declaration that failed to parse. The landing pass read
that silence as an empty axiom footprint, which is the signature of a maximally clean proof. A
summary table then flattened `VERIFIED_PARTIAL` into `VERIFIED` and dropped the `errors` array
entirely.

> **`axioms: []` is only meaningful alongside `exitCode: 0`. On a theorem that imports Mathlib,
> an empty axiom list next to a non-zero exit code is a failure signature, not a clean
> footprint.**

The failures underneath are ordinary. Several are a doubled keyword — `theorem X : theorem
L1_baseline ...` — emitted by a wrapper generator, producing `unexpected token 'theorem'`. Two
files additionally declare a published result as an `axiom`
(`PublishedTheorem_Rodl1985`, `PublishedTheorem_SengeStraus1971`), and one of them has its
central definition depending on `sorryAx`.

One of the five carries its own warning in its header: *"Never cite this file as a whole."*

## A second structural finding

**Of 635 `attached` paths on `PROVED` objects in this range, 0 resolve on disk.** They point at
per-node files that were never written. The sibling `sources` field resolves 636 of 636 — but
those point to the prose the statement was scraped from, not to a verifier.

**The `attached` field is not evidence of anything.**

---

## Four `PROVED` claims that are false

### 1. A fabricated factorization that refutes its own point

An object on Erdős 376 offers, as evidence that a binomial coefficient is coprime to 105:

> "incl. **C(20,10) = 184756 = 2²·7·11·13·23** coprime to 105"

Recomputed:

```
C(20,10)            = 184756
2^2 * 7 * 11 * 13 * 23 = 92092          <- not the same number
true factorization  = 2^2 * 11 * 13 * 17 * 19
```

The stated factorization is of a different integer. Worse, **it contains a factor of 7, and
7 divides 105** — so the number as factorized would not be coprime to 105 at all. The claim
contradicts the property it was offered to demonstrate.

The underlying biconditional on that problem is fine; it was checked to n = 20,000 with zero
mismatches. The fabrication is in the illustrative example.

### 2. A closed form that fails at every even N

> "exact closed form **R(N) = (N+3)/(2N)** for B = {1,2} ∪ odds, **N ≥ 2**"

| N | true R(N) | claimed | |
|---|---|---|---|
| 2 | 1 | 5/4 | ✗ |
| 3 | 1 | 1 | ✓ |
| 4 | 3/4 | 7/8 | ✗ |
| 5 | 4/5 | 4/5 | ✓ |
| 6 | 2/3 | 3/4 | ✗ |
| 7 | 5/7 | 5/7 | ✓ |
| 8 | 5/8 | 11/16 | ✗ |

The formula is correct for odd N and wrong for every even N, where the true value is
(N+2)/(2N). The limit 1/2 survives. The advertised **exact closed form for all N ≥ 2 does not.**

### 3. An extremizer set the machine itself refuted

Two objects on Erdős 454 give different answers for the same set. Recomputing
d(n) = f(n) − 2p_n over n = 2..20 settles it: **d(7) = −2**, so 7 does not belong, and the
maximum d = +2 is attained exactly on **{4, 8, 9, 14, 15}**.

The later object is right and says so explicitly, naming d(7) = −2 as the refutation. The
earlier one is wrong and was never retracted. Both are marked `PROVED`.

A detail neither states: the bound both assert, −6 ≤ d ≤ +2, is **true but not tight** — the
actual minimum over the range is −4.

### 4. A surviving declaration that is vacuous

A declaration on Erdős 383 has two rows: one `VERIFIED, exit 0`, one `FAILED, exit 1` whose
error is *"Tactic `decide` proved that the proposition"* — the message Lean emits when `decide`
proves the **negation**. The falsified file is no longer on disk.

The surviving version reduces to asserting that p is the largest prime factor of p², which is
trivially true for every prime. It is presented as certifying the problem's condition.

---

## What held up

Everything below was re-derived from scratch and is correct.

**Erdős 383** — among the 15 primes p ≤ 47, exactly **{7, 41, 43, 47}** have p²+1 that is
p-smooth, with factorizations 50 = 2·5², 1682 = 2·29², 1850 = 2·5²·37, 2210 = 2·5·13·17.
Confirmed exhaustively. This is the strongest unreceipted result in the range and carries no
Lean at all — while the file that *is* Lean-verified for that problem proves something
unrelated.

**Erdős 689** — there are 25 primes p ≤ 100 and `Σ ⌈100/p⌉ = 194 < 200`, confirming the
necessary condition **fails** at n = 100.

**Erdős 394** — for every odd prime p < 100, the least m ≥ 1 with p | m(m+1) is exactly p−1.
All 24 checked, zero counterexamples.

**Erdős 535** — f₃(2..8) = 2, 2, 3, 3, 3, 3, 4, consistent across three independent objects.

**Erdős 489** — the period-6 gap cycle [4,2] for A = {2,3}, per-period squared-gap sum 20,
density 20/6 = 10/3.

**Erdős 454** — f(n) = 7, 10, 16, 20, 26, 32, 40, 48, 54, 62, 70 for n = 2..12, exact match.

**Erdős 700** — `gcd(pq, C(pq,q)) = p` and the matching lower bound, together pinning
f(pq) = min(p,q). Genuine Mathlib proof via Lucas, clean receipt, exit 0.

---

## The shape of the range

6,824 objects name a problem in 301–700: **6,189 STATED, 635 PROVED, 0 COMPUTED, 0 REFUTED.**
Not one COMPUTED or REFUTED object exists anywhere in this range — all 278 and all 53
respectively live outside it.

## How to read any object in this corpus

1. Ignore the summary `VERIFIED` column. Open the `.verify.json` and read `status`,
   `exitCode` and `errors`.
2. Treat `axioms: []` as meaningless unless `exitCode` is 0.
3. Ignore `attached`. It resolves nowhere.
4. Treat every prose `PROVED` object as a lead and recompute it. Four in this sample were
   false, and two of those were contradicted by another object on the same problem.
