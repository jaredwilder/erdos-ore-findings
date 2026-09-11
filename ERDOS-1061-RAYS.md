# Erdős 1061: every solution generates a ray, and the rays add

Erdős 1061 counts the pairs `(a,b)` with `a + b ≤ x` satisfying `σ(a) + σ(b) = σ(a+b)`, and asks
whether that count is `~ cx`.

A companion note in this repository proves one infinite family by multiplicativity and gets
`S(x) ≥ 2x/9`. This is the same mechanism run to its conclusion: **every** solution generates a
family, not just that one, and the families are disjoint so their densities add.

---

## The scaling theorem

Let `(a,b)` be any solution, `s = a + b`, and let `M = rad(abs)`. For every `k` with
`gcd(k, M) = 1`, multiplicativity applies to each of `ka`, `kb`, `ks` separately:

```
σ(ka) + σ(kb) = σ(k)·(σ(a) + σ(b)) = σ(k)·σ(s) = σ(ks)
```

So **`(ka, kb)` is again a solution.** Each solution is the seed of an infinite ray.

*Verified:* 120 scaled pairs drawn from 40 distinct seeds, zero failures.

## The rays are disjoint

Call a seed **primitive** when `gcd(a,b) = 1`. (Since `s = a+b`, this is the same as
`gcd(a,b,s) = 1`.) If two primitive seeds produced a common pair, `ka = k'a'` and `kb = k'b'`,
then `a/b = a'/b'`, and primitivity forces `a = a'`, `b = b'` — the same seed.

**Distinct primitive seeds give disjoint rays, so their contributions add.**

## The density each ray contributes

The `k ≤ x/s` coprime to `M` number `(x/s)·φ(M)/M + O(1)`. Counting ordered pairs doubles it. So
a seed `(a,b,s)` contributes

```
  2·φ(M)
  ───────  ·  x        solutions below x
   M·s
```

Summing over finitely many primitive seeds gives a valid `liminf` bound — each error term is
`O(1)` and there are finitely many of them.

---

## The result

Exhaustive search for solutions with `s < 4000` finds **4,745 solutions, of which 1,437 are
primitive**. Summing their coefficients:

```
liminf  S(x)/x  ≥  0.948192477686...
```

from those seeds alone. Every larger seed adds a further positive term, so the true constant — if
the limit exists at all — is larger still.

### The single-family bound is the lowest ray

The family proved separately in this repository, `(a, 2a)` for `a` coprime to 6, is exactly the
sub-collection of seeds `(a, 2a, 3a)`:

| seed | coefficient |
|---|---|
| (1, 2, 3) | **2/9** |
| (5, 10, 15) | 8/225 |
| (7, 14, 21) | 4/147 |
| (11, 22, 33) | 20/1089 |

The first row alone is `2/9 = 0.2222`, which is precisely the bound that family gives. So the
earlier result is not a different argument — it is **the single largest ray**, and the other 1,436
primitive seeds below 4000 supply the remaining `0.726`.

### Direct count, as a sanity check

Counting actual solutions rather than ray coefficients:

```
x = 2000     ordered solutions ≤ x : 3806     S(x)/x = 1.903
```

comfortably above the certified `0.948` — as it must be, since the certificate uses only seeds
below 4000 and counts only their coprime multiples.

*(Counts past `x = 4000` from this run are meaningless: the seed search itself stopped at 4000, so
no new solutions enter and the ratio decays as an artifact of the cap. Only the `x = 2000` row is
a real measurement.)*

## What this does and does not settle

It settles that **`S(x) = o(x)` is false**, unconditionally and with an explicit constant. It does
not settle whether `S(x) ~ cx`: that needs the ray coefficients to converge, and the partial sums
are still rising. A diverging sum would mean `S(x)/x → ∞` and no such `c` exists — which the
direct counts, climbing through 1.9 at x = 2000, are consistent with but do not prove.

## Reproduce

`erdos1061_rays.py` finds the seeds, verifies the scaling theorem on them, checks primitivity and
disjointness, and sums the coefficients in exact rational arithmetic. Exits 0.
