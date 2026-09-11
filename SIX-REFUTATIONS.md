# Six results filed as PROVED that recomputation refutes

These come from the registry rows that carry `status = PROVED`. Every one was recomputed from
scratch. In four of the six the corpus's *conclusion* is wrong; in two the conclusion survives but
the stated certificate does not.

---

## 1. ex(6, K₂,₂,₂) = 13, not 12

`K₂,₂,₂` is the octahedron: three pairs, each vertex adjacent to everything but its partner.
Equivalently **`K₆` minus a perfect matching**.

### The reduction, stated correctly

```
G ⊇ K₂,₂,₂  ⟺  G ⊇ (K₆ − M) for some perfect matching M
            ⟺  complement(G) ⊆ M for some perfect matching M
            ⟺  complement(G) is a matching
```

So `G` is `K₂,₂,₂`-free exactly when **complement(G) is *not* a matching** — that is, when the
complement has two edges sharing a vertex. The cheapest such complement is a path `P₃`, which has
**2** edges. Therefore

```
ex(6, K₂,₂,₂) = 15 − 2 = 13
```

with extremizers exactly `K₆` minus a `P₃`. Counting them: 6 choices of centre × `C(5,2)` = **60**.

**Exhaustive confirmation** over all `2¹⁵` labelled graphs on 6 vertices: maximum 13, extremizer
count 60.

### Where the filed version went wrong

The corpus states the reduction as *"G contains K₂,₂,₂ iff the complement **contains** a perfect
matching."* It is *is a subgraph of*, not *contains*. That one inversion costs an edge.

The same row reports **α(K₆ − K₃) = 2**. Deleting the triangle on `{0,1,2}` leaves those three
vertices pairwise non-adjacent, so **α = 3**. The graph with α = 2 is `K₆ − P₃` — the actual
extremizer.

## 2. Erdős 317 — m\*(7) and m\*(8) are 4 and 7, not 10 and 15

`m*(n) = min |Σ δ_k · L_n/k|` over nonzero `δ ∈ {−1,0,1}ⁿ`, where `L_n = lcm(1..n)`.

Filed: `(1,1,1,1,2,2,10,15)`, "by exact 3ⁿ enumeration." True values, by actual exhaustive search
over all `3ⁿ` sign vectors:

```
n = 7   m* = 4    witness   −1/1 + 1/2 + 1/5 + 1/6 + 1/7  =  1/105
n = 8   m* = 7    witness   −1/1 + 1/2 + 1/5 + 1/6 + 1/8  = −1/120
```

The filed numbers 10 and 15 are exactly `L/(n−1) − L/n`. Only adjacent pairs were searched. The
claimed `3ⁿ` enumeration did not happen.

## 3. Erdős 295 — k(4) is 7 or 8, and both filed bounds are wrong

The corpus files `k₀(4) = 6` with a witness, and elsewhere `k(4) ≥ 9`.

Its own six-term prefix settles the lower end against it:

```
1/4 + 1/5 + 1/6 + 1/7 + 1/8 + 1/9  =  2509/2520  <  1     ⟹  k(4) ≥ 7
```

And the eight-term set reaches 1 exactly:

```
1/4 + 1/5 + 1/6 + 1/7 + 1/8 + 1/9 + 1/230 + 1/57960  =  1
```

So **7 ≤ k(4) ≤ 8**. The filed witness for `k₀(4)=6` has *seven* elements and sums to
`57959/57960 ≠ 1`.

## 4. Erdős 479 — the criterion fails inside its own certified range

Filed as PROVED: *"for all n ≤ 2000, 2ⁿ ≡ 2 (mod n) iff n is an odd prime."*

The composite counterexamples below 2000:

```
341, 561, 645, 1105, 1387, 1729, 1905
```

These are the base-2 Fermat pseudoprimes — 341 = 11·31 is the smallest and has been known since
1819. The companion half (`2ⁿ ≡ 0 mod n ⟺ n = 2^m`) does hold.

## 5. Erdős 156 — the minimum at N = 8 is 3, not 4

The quantity is the smallest size of a **maximal** Sidon set in `[1,N]`. Two separate rows file 4
at `N = 8`.

`{1, 4, 5}` has differences `{1, 3, 4}`, all distinct, so it is Sidon. And no element of `[1,8]`
can be added:

```
2 → repeats difference 1     3 → repeats 1     6 → repeats 1
7 → repeats 3                8 → repeats 4
```

It is **maximal at size 3**.

## 6. Erdős 683 — the two filed witnesses constrain nothing

The min-form `P(C(n,k)) ≥ min(n−k+1, k^{1+c})` is only constrained by pairs where the **first**
argument is not already the minimum — that is, where `P(C(n,k)) < n−k+1`.

| filed witness | C(n,k) | P | n−k+1 | binding? |
|---|---|---|---|---|
| (10,5) → "c ≤ 0.20905" | 252 | 7 | 6 | **no** — 7 ≥ 6 |
| (14,7) → "c ≤ 0.1938" | 3432 | 13 | 8 | **no** — 13 ≥ 8 |

In both the min-arm is already satisfied, so neither pair says anything about `c`.

Exhaustive search over `2 ≤ k ≤ n/2`, `n ≤ 160` for genuinely binding pairs gives

```
(n,k) = (10,3):   C = 120,  P = 5    ⟹   c ≤ log₃5 − 1 = 0.4649735
```

as the tightest finite-range cap — roughly **twice** the value the non-binding witnesses
suggested.

---

## Reproduce

`six_refutations.py` asserts all six, including the exhaustive `2¹⁵` graph sweep, the `3ⁿ` sign
search, and the exact Egyptian-fraction sums. Exits 0.
