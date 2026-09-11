# Two constructions: one refutes a conjecture outright, one kills a machine's overreach

Neither needs a search. The first is a single family of point sets. The second is five integers.

---

## Erdős 655 — the regular n-gon refutes the statement for every n

The question: if a finite planar set has the property that **no circle centred at one of its
points contains three others**, must it determine at least `(1+c)n/2` distinct distances for some
`c > 0`?

**No. The regular n-gon satisfies the hypothesis and determines exactly `⌊n/2⌋` distances.**

### The whole argument

Put the vertices at `v_k = (cos(2πk/n), sin(2πk/n))`, `k = 0,…,n−1`. Then

```
|v_0 − v_k|² = 2 − 2cos(2πk/n)
```

so

```
d(k) = d(j)   ⟺   cos(2πk/n) = cos(2πj/n)   ⟺   k ≡ ±j  (mod n)
```

Two consequences, and they are the whole result:

**The hypothesis holds.** From a fixed vertex, the distance classes are exactly the pairs
`{k, n−k}`. Every class has **two** members — one, when `n` is even and `k = n/2`. So a circle
centred at a vertex passes through at most 2 other vertices, never 3. By vertex-transitivity this
holds at every vertex.

**The conclusion fails.** The number of distinct distances is exactly the number of classes,
`⌊n/2⌋`. And

```
⌊n/2⌋  ≤  n/2  <  (1+c)·n/2      for every c > 0
```

So the bound fails for every `c > 0` and every `n ≥ 3`, on an unbounded family. ∎

### Verified

Exact symbolic check in ℚ(ζ_n) — no floating point — for `n = 3..16`: distinct-distance count
equals `⌊n/2⌋` and maximum vertices on a vertex-centred circle equals 2, in every case. The
integer criterion `k ≡ ±j (mod n)` swept for `n = 3..512`: zero failures.

| n | distinct distances | ⌊n/2⌋ | max on one circle |
|---|---|---|---|
| 3 | 1 | 1 | 2 |
| 5 | 2 | 2 | 2 |
| 8 | 4 | 4 | 2 |
| 13 | 6 | 6 | 2 |
| 16 | 8 | 8 | 2 |

---

## Erdős 477 — the k² case is proved, and the machine's general claim is false

The question: for a polynomial `f`, is there a set `A` with `A ⊕ f(ℤ) = ℤ` — every integer having
**exactly one** representation `a + f(k)`?

### The directness constraint

If `a, a′ ∈ A` are distinct and `a − a′ = s′ − s` for some `s, s′ ∈ S = f(ℤ)`, then
`a + s = a′ + s′` — two representations of one integer. So an exact complement forces

```
(A − A) \ {0}    disjoint from    (S − S) \ {0}
```

### f(k) = k² : no exact complement exists

An integer `d` is a difference of two squares exactly when `d ≢ 2 (mod 4)` — write
`d = (j−k)(j+k)`, whose two factors share a parity, so `d` is odd or divisible by 4. *(Verified
constructively for all `|d| ≤ 3000`: the achieved set matches `{d : d ≢ 2 mod 4}` exactly.)*

Therefore `(A − A) \ {0} ⊆ {d : d ≡ 2 (mod 4)}`.

Now take any three distinct `a₁ < a₂ < a₃` in `A`:

```
a₂ − a₁ ≡ 2   (mod 4)
a₃ − a₂ ≡ 2   (mod 4)
a₃ − a₁ = (a₃−a₂) + (a₂−a₁) ≡ 4 ≡ 0   (mod 4)
```

But `a₃ − a₁` is a nonzero element of `A − A`, so it must be `≡ 2 (mod 4)`. Contradiction.

**`|A| ≤ 2`.** And since `|S ∩ [1,N]| ~ √N`, a two-element `A` reaches at most `2(√N + 1)`
integers of `[1,N]` — for `N = 10⁸` that is 20,002 out of 100,000,000. **No exact complement
exists.** ∎

### The general-quadratic claim is false

The corpus files this, as PROVED:

> for every quadratic `ak² + bk + c` (`a ≠ 0`), `Δf` covers all integers outside **one** residue
> class mod `4|a|`

**Counterexample: `f(k) = 2k² + k`,** where `4|a| = 8`. Its difference set hits **every** residue
class mod 8, with witnesses of absolute value at most 8:

| class mod 8 | d | as f(j) − f(k) |
|---|---|---|
| 0 | −8 | f(−4) − f(4) = 28 − 36 |
| 1 | 1 | f(−1) − f(0) = 1 − 0 |
| 2 | 2 | f(1) − f(−1) = 3 − 1 |
| 3 | 3 | f(−2) − f(1) = 6 − 3 |
| 4 | −4 | f(−2) − f(2) = 6 − 10 |
| 5 | −3 | f(0) − f(1) = 0 − 3 |
| 6 | −2 | f(−1) − f(1) = 1 − 3 |
| 7 | −1 | f(0) − f(−1) = 0 − 1 |

Five values of `f` — 0, 1, 3, 6, 10 — are enough. Zero classes are missed, not one.

Nor is the count stable across the family:

```
k²          mod 4    misses  1 class    {2}
k² + k      mod 4    misses  2 classes  {1,3}
2k² + k     mod 8    misses  0 classes  { }
2k²         mod 8    misses  5 classes  {1,3,4,5,7}
3k² + k     mod 12   misses  6 classes  {1,3,5,7,9,11}
4k²         mod 16   misses 13 classes
5k² + 2k    mod 20   misses  5 classes  {2,6,10,14,18}
```

### And at least two different mechanisms are being conflated

`f(k) = k² + k = k(k+1)` is **always even** — values 0, 2, 6, 12, 20, 30, … Its difference set
misses both odd classes, so `A − A` is even and `A` sits inside one class mod 2. But `S` is
*also* entirely even, so `A ⊕ S` lies in a single class mod 2 and cannot be ℤ.

That kill comes from the parity of `S` itself, **not** from the three-term difference argument
that settles `k²`. The corpus merged two distinct mechanisms into one general statement, and the
merged statement is false.

**What stands:** `k²` is closed, completely, by four lines. The general quadratic is open by this
route, and the route the corpus recorded for it does not exist.

---

## Reproduce

`two_constructions.py` asserts every claim above — the n-gon distance counts symbolically, the
difference-of-squares criterion constructively, the three-term kill, and the mod-8 counterexample
with its witnesses. Exits 0.
