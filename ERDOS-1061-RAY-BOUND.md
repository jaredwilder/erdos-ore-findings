# Erdős 1061: a σ-ray theorem and a liminf bound eight times the previous one

Recovered 2026-09-11 from a mining transcript that had been sitting on disk truncated to a
quarter of its length. Two reported figures differed in their seventh decimal; that is resolved
below and they turn out to measure different things.

---

## The ray theorem

For `σ(a) + σ(b) = σ(a+b)`:

> If `(a,b)` is a coprime solution and `M = ab(a+b)`, then **every** `k` with `gcd(k,M) = 1`
> produces another solution `(ka, kb)`.

An exact infinite-ray theorem, straight from multiplicativity of σ. One solution is not one
solution — it is an arithmetic progression of them, thinned only by the coprimality condition.

Each seed therefore contributes to the counting function `S(x)` with density coefficient

```
2 φ(M) / ( M (a+b) )
```

## The bound

A certificate of all **152,803 seeds** was built, and a separate **integer-only verifier** —
recomputing every `gcd`, every `σ`, every `φ`, and a **downward-rounded** contribution — was run
over it:

```
PASS
rows=152803
floor_sum=2295492576177
rigorous_coefficient_lower_bound=2295492576177/1000000000000
```

giving

> **liminf S(x)/x ≥ 2.295492576177**

for the ordered-pair counting function. The previous two-seed bound was `38/135 ≈ 0.28148`. This
is **more than eight times larger**.

Growth of the coefficient as the seed search widened:

| seeds searched to | seeds found | coefficient |
|---|---|---|
| 100 | 12 | 0.3674 |
| 1,000 | 270 | 0.6745 |
| 5,000 | 1,870 | 1.0009 |
| 20,000 | 9,878 | 1.3864 |
| 50,000 | 29,596 | 1.7047 |
| 100,000 | 67,288 | 1.9811 |
| 150,000 | 108,660 | 2.1599 |
| 200,000 | **152,803** | **2.29549** |

## The two figures, reconciled

The recovered transcripts report two numbers, and both are labelled PASS-verified:

| figure | what it counts |
|---|---|
| **2.295492576177** | the **ray theorem alone**, over the 152,803 certified seeds |
| **2.295497372037** | the **combined** bound, over **both** seed populations |

They are not in conflict. The second transcript names the two populations explicitly — *"152,803
certified #1061 seeds, **43 generator seeds**"* — and describes rerunning *"**both** #1061 exact
verifiers: PASS / PASS"* before reporting *"the certified **combined** bound."*

The difference is `0.00000479586`: small, positive, and exactly the shape of a second disjoint
family of seeds adding its own density.

**Cite `2.295492576177` for the ray theorem; cite `2.295497372037` for the full estate.**

## A structural vein in the seeds

The seeds `(4,5,9)`, `(8,41,49)`, `(32,929,961)`, `(128,16001,16129)` come from

```
a = 2^m ,  a + b = (2^m − 1)^2
```

whenever `2^m − 1` and `(2^m − 1)^2 − 2^m` are **both prime**. The source states plainly that it
is *not* claiming that prime pattern is infinite.

## Scope

The bound is a **liminf**, established by a downward-rounded sum over a finite certified seed set.
It does not establish the asymptotic `S(x) ~ cx`, nor that the coefficient diverges — the source
says so in those words, and the divergent-family question stays open.

Both figures are the mining run's own verifier output, re-read here from the recovered transcript.
Neither is kernel-checked.
