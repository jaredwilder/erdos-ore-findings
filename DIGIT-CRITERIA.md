# Two problems that reduce to digit conditions, and what the reduction settles

Both of these collapse an apparently infinite search into a finite digit predicate. In one case
that turns a filed count of 1,295 into a complete list of 12. In the other it produces a sieve
2.9x stronger than the one on record.

---

## Erdős 376 — the complete witness list is twelve integers

The question: is `gcd(C(2n,n), 105) = 1` infinitely often?

### The reduction

By **Kummer's theorem**, `v_p(C(2n,n))` equals the number of carries when adding `n + n` in base
`p`. Adding `n` to itself carries at digit position `i` exactly when `2d_i ≥ p`. So

```
p ∤ C(2n,n)   ⟺   every base-p digit of n is ≤ (p−1)/2
```

Since `105 = 3·5·7`:

```
gcd(C(2n,n), 105) = 1   ⟺   base-3 digits of n all ≤ 1
                            base-5 digits all ≤ 2
                            base-7 digits all ≤ 3
```

Verified against actual binomial gcds for every `n ≤ 3000`: **zero mismatches**.

### The answer

Sweeping the digit predicate to `10⁷`:

```
n ∈ {1, 10, 756, 757, 3160, 3186, 3187, 3250, 7560, 7561, 7651, 20007}
```

**Twelve integers. Nothing above 20007 up to ten million.**

| n | base 3 | base 5 | base 7 |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| 10 | 101 | 20 | 13 |
| 756 | 1001000 | 11011 | 2130 |
| 20007 | 1000110020 | 1120012 | 112230 |

### What the corpus filed

> "Count of n ≤ 10⁶ with gcd(C(2n,n),105)=1: **1,295** … two independent exact methods … zero
> discrepancies."

The true count on that range is **12**. A hundredfold error, stated with a claim of independent
confirmation.

Two integers it names as witnesses are not witnesses:

```
n = 850   base-5 digits 1,1,4,0,0 — the 4 exceeds 2   →  gcd = 5
n = 3125  base-3 digits contain 2                     →  gcd = 21
```

The problem asks whether such `n` are infinite. Nothing here settles that — the digit set is a
Cantor-type set and the question is whether it is infinite, which the sweep cannot decide. What
the reduction *does* give is the exact answer on `[1, 10⁷]`, against a filed figure that was wrong
by two orders of magnitude.

---

## Erdős 1142 — a sieve 2.9x stronger, and sound

`n` is **Good** when `n − 2^k` is prime for every `2^k < n` (`k ≥ 1`). The known Good set is

```
{4, 7, 15, 21, 45, 75, 105}
```

and no further member exists below 30,000 (recomputed).

### The sieve rule

Let `p` be an odd prime and `t = ord_p(2)`. If `p ∤ n` and `n mod p` lies in the cyclic group
`⟨2⟩ mod p`, then `p | n − 2^j` for some `j`; once `n − 2^j > p`, that value is composite and `n`
is not Good. So for every `n > 2^t + p`:

```
n mod p  must be 0, or OUTSIDE ⟨2⟩ mod p
```

### The corpus used three primes and mis-stated one

It applies `p = 3, 5, 7` only, and for `p = 7` it records the safe residues as `{0,3,5}`. But
`⟨2⟩ mod 7 = {1,2,4}`, so the safe set is

```
{0, 3, 5, 6}
```

Dropping 6 wrongly excludes every `n ≡ 6 (mod 7)`.

### The corrected and extended sieve

Seven further primes, each with its threshold, every row checked against all seven known Good
numbers:

| p | ord_p(2) | threshold n > | safe residues |
|---|---|---|---|
| 3 | 2 | 7 | 1 / 3 |
| 5 | 4 | 21 | 1 / 5 |
| 7 | 3 | 15 | **4 / 7** |
| 31 | 5 | 63 | 26 / 31 |
| 73 | 9 | 585 | 64 / 73 |
| 127 | 7 | 255 | 120 / 127 |
| 89 | 11 | 2137 | 78 / 89 |
| 43 | 14 | 16427 | 29 / 43 |
| 151 | 15 | 32919 | 136 / 151 |
| 257 | 16 | 65793 | 241 / 257 |

Every Good number above each threshold satisfies that row. Surviving density:

```
p ∈ {3,5,7}      3.809524 × 10⁻²
all ten primes   1.321287 × 10⁻²      →  2.88x stronger
```

Note that `p = 31, 73, 127` all have thresholds **below 600** — far under the corpus's own working
cutoff — so they were available the whole time and simply never used.

---

## Reproduce

`digit_criteria.py` asserts the Kummer criterion against real binomial gcds, produces the twelve
witnesses, recomputes the Good set, and checks every sieve row against it. Exits 0.
