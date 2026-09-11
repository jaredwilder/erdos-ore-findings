# Two witnesses the corpus never found, and two retractions that were themselves wrong

Four results, each recomputed from scratch. Two extend a published census past where the search
stopped; two restore correct entries that were withdrawn on bad arithmetic.

---

## 1. Erdős 386 — a sixth-order witness at n = 715

The question asks when `C(n,k)` is a product of consecutive primes. The corpus records the `k=2`
solution set as `{4, 15, 21}`, certified "for all prime blocks with product P ≤ 30020."

That bound is where the search stopped, not where the solutions stop.

```
C(715, 2) = 715 · 714 / 2 = 255255 = 3 · 5 · 7 · 11 · 13 · 17
```

Six consecutive primes, every exponent 1. **255255 > 30020**, so it lay outside the certified
block range and was never reachable.

The complete `k=2` solution set for `n < 20000`:

| n | C(n,2) | factorization | consecutive primes |
|---|---|---|---|
| 4 | 6 | 2 · 3 | 2 |
| 6 | 15 | 3 · 5 | 2 |
| 15 | 105 | 3 · 5 · 7 | 3 |
| 21 | 210 | 2 · 3 · 5 · 7 | 4 |
| **715** | **255255** | **3 · 5 · 7 · 11 · 13 · 17** | **6** |

So the filed set misses two: `n = 6` (inside the search range) and `n = 715` (outside it). No
`k=2` witness exists between 21 and 20000 other than 715.

## 2. Erdős 932 — r = 4 belongs in the census

The question concerns prime gaps `(p_r, p_{r+1})` containing at least two interior integers all of
whose prime factors are strictly below the gap length. The corpus certifies the qualifying `r ≤ 30`
as exactly `{9, 11, 15, 24, 30}`.

**r = 4 qualifies and is missing.** The gap is `(7, 11)`, length 4, interior `{8, 9, 10}`:

```
8  = 2³    largest prime factor 2 < 4   ✓
9  = 3²    largest prime factor 3 < 4   ✓
10 = 2·5   largest prime factor 5 ≥ 4   ✗
```

Two qualifying integers, which is what the condition asks for. The census should read
`{4, 9, 11, 15, 24, 30}`. (Outside their stated range, `r = 34` also qualifies: gap `(139,149)`
of length 10 holds 140 = 2²·5·7, 144 = 2⁴·3², 147 = 3·7².)

## 3. Erdős 383 — p = 47 was withdrawn on an arithmetic slip

A route filed the survivors of `P(p²+1) ≤ p` for `p ≤ 199`, including `p = 47` with the
factorization `47² + 1 = 2210 = 2 · 5 · 13 · 17`. A later route retracted that entry, stating

> 47² + 1 = 2222 = 2 · 11 · 101, so P = 101 > 47

**2222 is not 47² + 1.** 47² = 2209, so 47² + 1 = **2210**, and 2222 = 47² + 13. The original
entry was right:

```
47² + 1 = 2210 = 2 · 5 · 13 · 17     P(2210) = 17 ≤ 47   ✓
```

`p = 47` is a survivor. The retraction withdrew a correct result and narrowed the census from
eight entries to three.

**Corrected census, p ≤ 199:**

```
{7, 41, 43, 47, 73, 83, 157, 173, 191, 193}
```

Ten primes. The originally filed list had eight (missing 47 and 191); the retraction cut it to
three. This list is the exhaustive answer on that range.

## 4. Erdős 11 — the "depth 7" hard case does not exist

Every odd `n` is conjectured to be `k + 2^l` with `k` squarefree. A route records `n = 185` as a
depth-7 case (`185 = 57 + 128`) and `n = 137` as depth 6, treating them as the extremal
difficulties.

Neither is hard:

```
185 − 2¹ = 183 = 3 · 61     squarefree   →  l = 1
137 − 2² = 133 = 7 · 19     squarefree   →  l = 2
```

The genuine extremal case on odd `n ≤ 127` is `n = 29`:

```
29 − 2⁰ = 28 = 2²·7   not squarefree
29 − 2¹ = 27 = 3³     not squarefree
29 − 2² = 25 = 5²     not squarefree
29 − 2³ = 21 = 3 · 7  squarefree        →  l = 3
```

A later route in the same campaign gets this right and calls 29 the unique minimum-`l` extremizer
below 127. The depth-6 and depth-7 labels were never recomputed against it.

---

## Reproduce

`four_corrections.py`. Requires sympy. Exits 0, and asserts every claim above.
