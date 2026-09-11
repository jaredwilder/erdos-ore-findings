# Erdős 1061: an infinite solution family, proved in three lines

Erdős 1061 asks how many pairs `(a,b)` with `a+b ≤ x` satisfy

```
σ(a) + σ(b) = σ(a+b)
```

The corpus's census of small solutions is inconsistent across routes — S(40) appears as 22, 24
and 26 in four different places. That disagreement is real and it is resolved elsewhere. What
survives all of it, because it never depended on the census, is this:

## The identity

**For every `a` with `gcd(a,6) = 1`:**

```
σ(a) + σ(2a) = σ(3a)
```

**Proof.** σ is multiplicative. `gcd(a,2) = 1` gives `σ(2a) = σ(2)σ(a) = 3σ(a)`.
`gcd(a,3) = 1` gives `σ(3a) = σ(3)σ(a) = 4σ(a)`. Then

```
σ(a) + σ(2a) = σ(a) + 3σ(a) = 4σ(a) = σ(3a).
```

Three lines, no computation, no hypothesis beyond coprimality to 6.

**Checked:** all 1,333 values of `a < 4000` with `gcd(a,6) = 1`. Zero failures.

| a | σ(a) + σ(2a) | σ(3a) |
|---|---|---|
| 1 | 1 + 3 = 4 | σ(3) = 4 |
| 5 | 6 + 18 = 24 | σ(15) = 24 |
| 7 | 8 + 24 = 32 | σ(21) = 32 |
| 11 | 12 + 36 = 48 | σ(33) = 48 |
| 13 | 14 + 42 = 56 | σ(39) = 56 |
| 25 | 31 + 93 = 124 | σ(75) = 124 |
| 29 | 30 + 90 = 120 | σ(87) = 120 |

## What it gives

Every such `a` yields the ordered pairs `(a, 2a)` and `(2a, a)`, both summing to `3a`. Counting
the `a` coprime to 6 with `3a ≤ x` — exactly two per block of six — gives an unconditional
lower bound

```
S(x) ≥ 4⌊⌊x/3⌋/6⌋ ≥ 2x/9 − 10/3   for all real x
```

So **S(x) = o(x) is false**, and any limit `S(x) ~ cx` must have `c ≥ 2/9`. This does not depend
on any census, any search bound, or any of the contested counts.

## The companion: a diagonal that is provably empty

The same multiplicativity settles a neighbouring question negatively. Write `a = 2^k·m` with `m`
odd. Then

```
σ(2a) − 2σ(a) = (2^{k+2} − 1)σ(m) − 2(2^{k+1} − 1)σ(m) = σ(m) ≥ 1
```

so **`2σ(a) = σ(2a)` has no solution at all** — not "no solution below some bound," none.

Verified: the identity `σ(2a) − 2σ(a) = σ(odd part of a)` holds exactly at a = 1, 2, 3, 4, 6, 8,
12, 24, 40; and no `a < 5000` satisfies `2σ(a) = σ(2a)`.

## Scope

This is a family of solutions and a lower bound on their count. Erdős 1061 asks for the exact
asymptotic order, which this does not give. What it does give is a floor no search can move and
a neighbouring case closed outright.

## Reproduce

`sigma_family.py`. Requires sympy for `divisor_sigma`. Exits 0.
