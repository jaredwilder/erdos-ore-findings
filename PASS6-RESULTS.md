# Results recovered from the Pass-6 delta

Every statement below was recomputed from scratch before it was written down.

---

## Erdős 653 — g(4) = 3, exactly

An explicit 4-point configuration with coordinates in **Q(√3)**, squared distances in Q(√3),
attaining exactly **3** distinct values of the map `x_i → R(x_i)`.

Since `R(x_i) ≤ n − 1 = 3` for four points, the witness meets the ceiling. **g(4) = 3.**

An exact determination with a matching upper bound — the rarest object in this corpus.

### And the regular n-gon count

For every `n` in [3, 64], the number of distinct chord lengths from a fixed vertex of a regular
n-gon is exactly **⌊n/2⌋**, from

```
d(k)² = 4 sin²(πk/n) = 4 sin²(π(n−k)/n)
```

Recomputed for all 62 values. Consequence: the n-gon family forces `g(n) ≤ ⌊n/2⌋` on an unbounded
set, so the literal statement fails with **ε = 1/2**.

---

## Erdős 936 — the powerful-number question is Brocard's problem

For `n ≤ 12`, exhaustive and fail-closed in exact integer arithmetic:

| family | powerful values |
|---|---|
| `2ⁿ + 1` | only **n = 3** (9 = 3²) |
| `2ⁿ − 1` | only n = 1 (vacuous) |
| `n! + 1` | exactly **n ∈ {4, 5, 7}** — 25 = 5², 121 = 11², 5041 = 71² |

And the identification the corpus makes explicitly:

> `n! + 1 = m²` for `n ≥ 4` **is** Brocard's problem — the model reproduces (4,5), (5,11), (7,71)
> exactly.

That names the exact open problem the branch reduces to. Verified: 4!+1 = 25, 5!+1 = 121,
7!+1 = 5041, and 2³+1 = 9 is the only powerful 2ⁿ+1 for n ≤ 12.

### Plus an exact periodicity, kernel-checked

```
9 | 2ⁿ + 1   ⟺   n ≡ 3 (mod 6)
```

Verified for all n ≤ 30; it follows from ord₉(2) = 6. Carries a `covers=full` kernel certificate.

---

## Erdős 479 — four proved infinite families

For `{n : 2ⁿ ≡ k (mod n)}`:

| k | family | verified |
|---|---|---|
| 0 | `n = 2^a` | yes |
| −1 | `n = 3^a` | 9 \| 2³+1, 27 \| 2⁹+1, 81 \| 2²⁷+1 |
| 2 | odd primes, plus n = 341 | yes |
| `2^(2^j)` | `n = ap`, primes `p ≡ 1 mod ord(2)/gcd`, by CRT + Dirichlet | 2²⁵ ≡ 32 (mod 25), 2⁶⁵ ≡ 32 (mod 65) |

**The Novák closure lemma**: if `n ∈ W(−1)` and `p` is an odd prime with `p | 2ⁿ+1`, then
`np ∈ W(−1)`. Gives witnesses 1, 3, 9, 171 — and correctly excludes 57. All five confirmed.

**A refutation in the same cluster:** the naive lift to all `k ≠ 1` is killed by `k = 4, n = 140`.
Verified — 2¹⁴⁰ ≡ 116 (mod 140), not 4.

---

## Erdős 701 — Chvátal's conjecture, exhausted to n = 4

> exhaustive over all **65,812** hereditary families with |X| ∈ {1,2,3,4}
> (4 + 16 + 256 + 65,536), every intersecting subfamily checked exactly, **zero violations**

and for the n = 4 case specifically: all **M(4) = 168** downsets of B₄, brute-forcing every one of
up to 2¹⁶ subfamilies each, exact integer arithmetic, fail-closed. Three Lean kernel fragments for
n = 2, 3, 4.

The line that makes it trustworthy is in the corpus itself: **"supersedes 5000-sample evidence."**
The machine replaced sampling with exhaustion and said so.

---

## Erdős 11 — exhaustive to 4096, and a correction that is right

Every odd `n` in [3, 4096] is `k + 2ˡ` with `k` squarefree. Verified by full sweep.

The extremizer is **29 = 21 + 2³** — unique minimum-l on odd n ≤ 127.

And a later route **falsified its own earlier labels**. The claim that 53, 89, 95, 97 were hard
cases needing l = 3..4 is wrong:

```
53 = 51 + 2¹   (51 = 3·17)
89 = 87 + 2¹
95 = 94 + 2⁰
97 = 95 + 2¹
```

All use `l ≤ 1`. Confirmed. The corpus kept both the error and its correction.

### The counting obstruction, and where it fails

A genuine attempted obstruction: any branch-B witness has least instance `n₀ > 63` with
`p_l² | n₀ − 2^l` for every `l < L`, forcing `Σ_p ⌈L / ord_{p²}(2)⌉ ≥ L`.

The order table, hand-checked and every value correct:

| p | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 |
|---|---|---|---|---|---|---|---|---|---|
| ord_{p²}(2) | 6 | 20 | 21 | 110 | 156 | 136 | 342 | 253 | 812 |

At L = 12 the lane-cover sum is **10 < 12**. **The obstruction fails**, and the corpus says so,
naming the wall as the unbounded tail lanes `l ≥ 12`. A stated failure with the exact point of
failure is a better starting position than most successes.

---

## Erdős 890 — the primorial witness

`ω(30030) = 6` (2·3·5·7·11·13) and `ω(30031) = 2` (59 · 509) — the classic first
primorial-plus-one composite. Both verified. An outward-rational interval check with strict tail
bounds gives `R(30030) > 3/2` with wide margin.

The corpus also records a **retraction**: an earlier `R = 1.8056` claim was killed by re-factoring
510510, and the file keeps the retraction rather than the number.

---

## Erdős 456 — an exact exceptional set

`n | p_n − 1` holds for exactly **n ∈ {1, 2, 5, 6, 12, 14}** in n ≤ 20, with the universal clause
failing explicitly at n = 3 (3 ∤ 4).

A determinate finite statement where a vague "mostly holds" would have been easier to write.

---

## Erdős 985 — least prime primitive roots

Nine exact pairs `(p, q)` for primes 3 ≤ p ≤ 29, with the maximum least-root being **7, attained
at p = 41 and p = 71**. Recomputed the full table.

Produced independently by a computational route, a falsifier route, and a Lean formalization — all
three agreeing.

---

## Erdős 821 — an infinite branch closed in one line

`φ(m)` is even for every `m ≥ 3`. Therefore **`g(n) = 0` for every odd `n > 1`.**

Case analysis given: `m = 2^a` with `a ≥ 2` gives `φ = 2^(a−1)`; an odd prime power `p^a ‖ m`
contributes `p^(a−1)(p−1)`. Both even.

Elementary, unconditional, universal — and it disposes of an entire infinite branch.

---

## Erdős 170 — nonexistence by parity

Ten distinct differences in [1,10] must sum to **55, odd**. But any 5-mark ruler's gap-weighted
sum is

```
4d₁ + 6d₂ + 6d₃ + 4d₄  =  40 + 2(d₂ + d₃)
```

which is **even**. Contradiction. **N = 10 nonexistence, with no enumeration at all.**

---

## Erdős 17 — non-monotonicity

With `C(p)` := every even `n ≤ p−3` is a difference of two primes `≤ p`:

**`C(97)` is FALSE** — blocked at n = 88 by 91 = 7·13, 93 = 3·31, 95 = 5·19, all composite.
**`C(101)` is TRUE** by full enumeration.

Verified. The property is **not monotone**, which kills the obvious inductive approach.

---

## Erdős 513 — an exact algebraic constant and a structural exclusion

```
M(1)² = (191 + 49√33) / 128        exactly, in Q(√33)
g(u*) − (2−c)² = (5c−1)² / (4c)    an exact identity
```

And a real exclusion: **Hadamard-lacunary functions cannot be extremizers**, because
`Q(Σ z^{2^k}) ≤ 2/7 < 1/2`.

The corpus also catches that its own `ρ*` formula is inconsistent with its own `M(1)`, deriving
the absurdity `16√33 = 16` and flagging it unresolved.

---

## Erdős 68 — the coprimality lemma

`gcd(n! − 1, m! − 1) = 1` for `2 ≤ n < m`, since `p | n!−1` forces `p > n`.

Exact partial sums confirmed: 1, 6/5, 143/115, 17132/13685, **12331593/9839515**.

*(A separate finding in this repository documents an enclosure of the full sum that nine routes
agreed on and that is wrong. The pieces above are the parts that hold.)*
