# A constant replicated nine ways, and wrong

The Pass-6 delta of this mining corpus carries a file named `PASS6_REPLICATED_EXACT_CONSTANTS.csv`.
The premise is sound: a value independently reproduced by several routes should be more trustworthy
than one produced once.

This is the counterexample to that premise, found by re-deriving the constants instead of counting
the routes.

---

## The constant

Erdős 68 asks whether `Σ_{n≥2} 1/(n!−1)` is irrational. Two routes in the corpus certify an
enclosure of the sum. Both are marked replicated; the cluster carries
**occurrence 20, refs 18, routes 9, source kinds 4.**

```
route A :  S ∈ (1.25349875606,       1.25349875607)
route B :  S ∈ (1.253498755679455,   1.253498755679566)
```

Computed exactly, as a rational sum over n = 2..29 and then converted:

```
S = 1.2534987556999534716433609379057...
```

| | contains S | error |
|---|---|---|
| route A | **no** | S sits **3.60 × 10⁻¹⁰ below** its lower endpoint |
| route B | **no** | S sits **2.04 × 10⁻¹¹ above** its upper endpoint |

**The two intervals do not overlap each other, and neither contains the true value.**

## The corpus refutes itself, and says nothing

The same cluster separately certifies two pieces that are both correct:

- the exact partial sum through n = 12: `1.2534987555270768002034937366…`
- a tail bound: `3/13! = 4.8177 × 10⁻¹⁰`

Add them. They give

```
S < 1.253498756008848
```

which is **below route A's stated lower endpoint of 1.25349875606.**

So the corpus contains, at the same time: a certified enclosure, a second certified enclosure
disjoint from the first, and two certified components whose sum contradicts the first. Nothing in
the file flags any of it. The replication counter reads 9.

## What replication actually measured

Nine routes agreeing means nine routes derived from shared upstream text. It is a **popularity
count, not an independence count.** The file's own structure shows why:

- **41% of rows have `distinct_source_kind_count` = 1** — a single source kind, in a file named
  REPLICATED.
- **19% come from a single route.**
- Only **7%** reach three distinct routes *and* three distinct source kinds.
- The same paragraph is re-filed once per number it contains. One Erdős 1055 paragraph appears
  under atoms 13, 17, 37, 73 and 1021 — five "replications" of one sentence.

## The contrast case, in the same corpus

Erdős 1055 produced **three mutually inconsistent answer sequences** across routes:

```
2, 13, 37, 73, 1021, 8167
2, 13, 37, 313, 79709
2, 5, 13, 37, 73, 1021
```

Instead of averaging them or picking the most-replicated, the machine found the root cause — the
predicate *"class-r prime"* is absent from the contract and is satisfiable by at least three
different readings — and **refused to certify anything.** It then separately checked the one
claim it could: 1021 is prime, 1020 = 2²·3·5·17 with Ω = 5 and ω = 4, so the asserted "1021
breaks the pattern" is false under either reading.

That is the correct behaviour, produced by the same system in the same pass. The Erdős 68 cluster
is what happens when it does not fire.

## The rule this yields

> **Replication count is not a truth signal. Re-derive the constant.**

It is cheap. Computing `Σ 1/(n!−1)` to forty digits takes one line and settled a value that nine
routes and four source kinds had agreed on incorrectly.

## Two more uncaught disagreements in the same pass

Reported for completeness; neither is adjudicated by the file.

- **Erdős 1** — four routes give `N(0..5) = 1,1,2,4,7,13`; a fifth files `1,1,3,4,7,13,24,44,84`,
  with a 3 where the others have 2. OEIS A276661 has 2.
- **Erdős 701** — one route writes the Dedekind anchor as `2,5,20,168,7581`; the correct sequence is
  `2,3,6,20,168,7581`, and a sibling route **in the same problem** independently enumerates 6
  downsets on a 2-element ground set, contradicting the 5.

## One that looks like a contradiction and is not

Worth stating because it cuts the other way. Three routes on Erdős 689 report different constants:

```
route 1:  Σ⌈n/p⌉ ≈ 195
route 2:  Σ⌈100/p⌉ = 194
route 3:  Σ(⌊n/p⌋+1) = 196
```

Recomputed: `Σ_{p≤100} ⌈100/p⌉ = 194` and `Σ_{p≤100} (⌊100/p⌋+1) = 196`. **Both are correct.** They
differ by exactly 2 because `⌈n/p⌉ = ⌊n/p⌋+1` unless `p | n`, and only p = 2 and p = 5 divide 100.
A real definitional split, faithfully preserved by the file. Only the hand-waved `≈ 195` is junk.

Re-deriving separates these cases. Counting routes does not.
