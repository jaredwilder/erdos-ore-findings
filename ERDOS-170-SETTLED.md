# Erdős 170: the constant is 1.5603, not √2

Erdős 170 asks for the asymptotics of `F(N)` — the least number of marks on `[0, N]` whose
pairwise differences cover every distance `1..N` (a sparse ruler, or difference basis). The
question the campaign actually froze is the **value of `lim F(N)/√N`**, and the frozen definition
of the governing constant reads

```
c₀ = √( sup { 2(1 − sin θ / θ) : θ ∈ ℝ, θ ≠ 0 } )
```

Three separate objects in the corpus evaluate that supremum as **2**, giving `c₀ = √2 ≈ 1.414214`.

**That is wrong, and the error is a one-liner.** `sin θ / θ` goes negative. Taking `θ → ∞` gives
the limit 2, not the supremum. The supremum is attained where `sin θ / θ` is *minimized*, at the
first positive root of `tan θ = θ`:

```
θ*            = 4.493409457909064175307880927...
sin θ* / θ*   = −0.217233628211221657408279326...
sup           = 2(1 + 0.2172336282...) = 2.434467256422443314816558651...
c₀            = √2.4344672564...        = 1.560277942041879702102077382...
```

A scan of `sin θ / θ` over `θ ∈ (0, 60)` at step `10⁻³` confirms `θ*` is the global minimum.

**`c₀ = 1.5603`, not `1.4142`.** The difference is 0.1461 — about 10%. This is the
Rédei–Rényi / Leech constant, and it is strictly stronger than the trivial pair-counting bound
√2 that the corpus collapsed it onto. Since the campaign's whole target is the value of
`lim F(N)/√N`, this is the single consequential correction in the seam, and it takes one line to
make.

---

## The small-value table, computed exhaustively

Complete enumeration over all mark sets containing 0 and N, smallest size first.

| N | F(N) | witnesses of that size | lexicographically first |
|---|---|---|---|
| 1 | 2 | 1 | `{0,1}` |
| 2 | 3 | 1 | `{0,1,2}` |
| 3 | 3 | 2 | `{0,1,3}` |
| 4 | 4 | 3 | `{0,1,2,4}` |
| 5 | 4 | 4 | `{0,1,2,5}` |
| 6 | 4 | 2 | `{0,1,4,6}` |
| 7 | 5 | 12 | `{0,1,2,3,7}` |
| 8 | 5 | 8 | `{0,1,2,5,8}` |
| 9 | 5 | 4 | `{0,1,2,6,9}` |
| 10 | **6** | 38 | `{0,1,2,3,6,10}` |
| 11 | 6 | 30 | `{0,1,2,3,7,11}` |
| 12 | 6 | 14 | `{0,1,2,3,8,12}` |
| 13 | 6 | 6 | `{0,1,2,6,10,13}` |
| 14 | 7 | 130 | `{0,1,2,3,4,9,14}` |
| 15 | 7 | 80 | `{0,1,2,3,4,10,15}` |
| 16 | 7 | 32 | `{0,1,2,3,8,12,16}` |
| 17 | 7 | 12 | `{0,1,2,3,8,13,17}` |
| 18 | 8 | 500 | `{0,1,2,3,4,5,12,18}` |
| 19 | 8 | 326 | `{0,1,2,3,4,9,14,19}` |
| 20 | 8 | 150 | `{0,1,2,3,4,10,15,20}` |

```
F(1..20) = 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8
```

Extended by the same exhaustive method to N = 48:

```
F(1..48) = 2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,
           10,10,10,10,10,10,10,11,11,11,11,11,11,11,12,12,12,12,12
```

with `F(N) <= F(N+1) <= F(N)+1` throughout the range. Witnesses at the top:
`F(43)=11` via `{0,1,3,6,13,20,27,34,38,42,43}` and `F(48)=12` via
`{0,1,2,3,13,26,29,33,39,43,47,48}` — both checked to cover every distance.

The value runs come in equal-length pairs:

```
F =  4  5  |  6  7  |  8  9  | 10 11
run  3  3  |  4  4  |  6  6  |  7  7
```

Agrees with the known sparse-ruler sequence. The value here is adjudication, not novelty —
everything below is a corpus claim this table settles.

## Two shipped witnesses do not work

The corpus ships eight witnesses. Six are correct. Two are not:

| N | shipped witness | result |
|---|---|---|
| 7 | `{0,1,3,4,7}` | **fails — distance 5 is not covered** |
| 8 | `{0,1,3,6,8}` | **fails — distance 4 is not covered** |

Check by hand. `{0,1,3,4,7}` gives differences `{1,2,3,4,6,7}`. No 5. `{0,1,3,6,8}` gives
`{1,2,3,5,6,7,8}`. No 4.

The **values** F(7)=5 and F(8)=5 are right; only the exhibited sets are wrong. Correct witnesses
of the same size:

```
N = 7 :  {0, 1, 2, 3, 7}
N = 8 :  {0, 1, 2, 5, 8}
```

The bad N=7 set is the most-repeated error in the corpus. A later route caught it and filed the
replacement `{0,1,3,5,7}` — also valid — but the fix was never propagated back.

## F(10) = 6

The corpus carries both F(10)=5 and F(10)=6 in different routes. **It is 6**, with 38 distinct
6-mark witnesses. No 5-mark ruler of length 10 exists.

## Where the counting bound is actually tight

`F(N) ≥ ⌈(1 + √(1+8N))/2⌉` comes from needing `C(m,2) ≥ N` distinct positive differences. Routes
disagree about where it binds, because **three different formulas circulate in the corpus under
the one name "the counting bound"** — the one above, `min k with k(k+1)/2 ≥ N+1` (an off-by-one
that lets the free difference 0 pay for one of the N required values), and `⌈√N⌉+1`.

For the real bound, exhaustively:

| | N |
|---|---|
| **tight** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 16, 17, 22, 23, 29 |
| **not tight** | everything else through N = 48 |

(seventeen tight values over the full computed range N <= 48, and none above N = 29)

So the corpus claims that the bound fails at N = 4 and N = 7 are **both wrong** — it is tight at
both. The correct statement of where pair-counting gives out:

```
tight through N = 9
first short by 1 at N = 10   (bound 5, truth 6)
first short by 2 at N = 44   (bound 10, truth 12)
```

This matters beyond bookkeeping: the campaign's route-selection narrative records that the
pair-count bound "is provably not the answer (F(4)=4, F(7)=5, F(10)=6 all exceed it)," and routes
were opened and killed on that basis. Two of those three data points are false — the instinct was
right and the evidence was wrong.

**And the two halves of this document are the same fact.** The counting bound is asymptotically
`√(2N)`, i.e. constant `√2 = 1.4142`. The true constant is `c₀ = 1.5603`. Since `1.5603 > 1.4142`,
the deficit `F(N) − ⌈(1+√(1+8N))/2⌉` has to grow without limit — and N = 44 is simply the first
place it reaches 2. A corpus that had evaluated `c₀` correctly would have predicted that widening
instead of being surprised by it.

## The "non-monotone" claim is mislabelled

One object reads *"Counterexample to F(N) nondecreasing: F(9)=5 < F(10)=6."*

`5 < 6` is F **increasing**, which is exactly what nondecreasing permits. The computation is
right and the label on it is wrong. F is nondecreasing with unit steps throughout the computed
range.

## The parity obstruction, and the generalization nobody took

The one genuinely elegant object in the seam, correct as filed:

> Ten distinct differences in `[1,10]` must sum to `1+2+…+10 = 55`, which is **odd**. Any 5-mark
> ruler's gap-weighted sum is `4d₁ + 6d₂ + 6d₃ + 4d₄ = 40 + 2(d₂+d₃)`, which is **even**.
> So no *perfect* 5-mark ruler of length 10 exists.

The general identity is

```
Σ_{i<j} (a_j − a_i)  =  Σ_i (2i − k + 1) a_i
```

which is **even whenever k is odd**, while a perfect k-mark ruler needs the differences to be
exactly `1 .. C(k,2)`, summing to `C(k,2)(C(k,2)+1)/2`. The obstruction therefore fires for every
odd k where that sum is odd — **k = 5, 7, 13, …**, not only k = 5. The corpus states the k=5 case
and stops.

## The definition is load-bearing from N = 18

The corpus flags, but never resolves, that *restricted* differences (marks confined to `[0,N]`)
and *unrestricted* differences (marks anywhere in ℤ, diameter free) are distinct variants. They
agree for all N ≤ 17 and first diverge at **N = 18**: the 7-mark set

```
{0, 2, 7, 14, 15, 18, 24}
```

has diameter 24 and covers `1..18`, while no 7-mark subset of `{0,…,18}` does. So restricted
F(18) = 8 and unrestricted = 7.

Every F-value stated in the corpus is therefore definition-independent — but only because none of
them goes past N = 17. Any extension of the table has to name its variant.

## Reproduce

`ruler.py` recomputes the table, counts every witness, checks the eight shipped witnesses, and
prints the tightness column. `c0.py` computes the constant. Standard library plus mpmath.
