# Six exact values, measured

Each of these is a finite, checkable quantity. Four are recomputations that disagree with what the
ore recorded; two are just the answers.

---

## Erdős 979 — the integer 81770 has eight representations

`n = 81770` is the **unique** integer below 200,000 expressible as `p² + q²` with both `p` and `q`
prime in **eight** ways:

```
 41² + 283²  =   1681 +  80089
 53² + 281²  =   2809 +  78961
 71² + 277²  =   5041 +  76729
 97² + 269²  =   9409 +  72361
137² + 251²  =  18769 +  63001
157² + 239²  =  24649 +  57121
179² + 223²  =  32041 +  49729
193² + 211²  =  37249 +  44521
```

Eight is the maximum on that range, and 81770 is the only place it occurs.

*(The ore records `max f₂ = 5 on n ≤ 10⁶` and separately `f₂(n) ≤ 1 for all tested ranges`. Both
are refuted at 81770, which is well inside both.)*

---

## Erdős 145 — an asymptotic estimate filed as an exact count

The number of squarefree integers up to `10⁷`, by the Möbius identity
`N(x) = Σ_{d ≤ √x} μ(d)⌊x/d²⌋`:

```
N(10⁷) = 6,079,291
```

The ore files **6,079,271**, described as *"cross-checked against an independent d²-sieve"*.

```
⌊(6/π²) · 10⁷⌋ = 6,079,271
```

The filed number is exactly the **asymptotic estimate** `6x/π²`, not the count — off by 20, and
"cross-checked" twice without the discrepancy surfacing. The density `6/π²` is right; it is not
what the problem asks for.

---

## Erdős 68 — the constant, and a coprimality claim that fails

```
S = Σ_{n≥2} 1/(n!−1)
  = 1.253498755699953471643360937905798940369232208332…
```

(49 digits, computed at 60-digit working precision.)

The ore also files, as PROVED, that `{n! − 1}` is **pairwise coprime**. It is not:

```
4! − 1 = 23
8! − 1 = 40319 = 23 · 1753
gcd = 23
```

Nine such pairs occur with `2 ≤ n < m ≤ 24`, at gcds 23 and 17:

```
(4,8) (4,11) (4,21) (8,11) (8,21)  → 23
(5,11) (5,15) (11,15)              → 17
```

The usual argument — *"p | n!−1 forces p > n"* — bounds `p` below by `n`, but says nothing about
`m`, and every failure above has `p` between `n` and `m`.

---

## Erdős 51 — the extremal totient preimage ratio

For a totient value `a`, let `n_a` be the least `m` with `φ(m) = a`. Over all totient values
`a ≤ 20000`:

```
max n_a / a  =  11985 / 5888  =  2.035496…      at  a = 5888
```

with `5888 = 2⁸ · 23` and `11985 = 3 · 5 · 17 · 47`.

Only **three** totient values below 20000 have ratio exceeding 2:

| a | n_a | ratio |
|---|---|---|
| 5888 | 11985 | 2.0355 |
| 10496 | 21165 | 2.0165 |
| 17408 | 34935 | 2.0068 |

*(The ore files `n_a/a ≤ 2 for every a ≤ 10⁶, max 2 at a = 2^{k−1}`. The ratio 2 is not attained at
any power of two in range, and 5888 exceeds it.)*

---

## Erdős 826 — the complete list

The integers `n` with `τ(n+k) ≤ 2k` for **every** `k ≥ 1` — the tail is finite because
`τ(m) ≤ 2√m` — are exactly, for `n ≤ 3000`:

```
{ 1, 2, 4, 6, 12, 36, 60, 72, 420 }
```

Nine values. The ore's list stops at seven, omitting **72** and **420**.

---

## Erdős 829 — seventeen, not four

The integers below 200,000 expressible as a sum of two positive cubes in two ways:

```
1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232,
65728, 110656, 110808, 134379, 149389, 165464, 171288, 195841
```

**Seventeen.** Maximum multiplicity on the range is 2. Samples:

```
1729  =  1³ + 12³  =  9³ + 10³
4104  =  2³ + 16³  =  9³ + 15³
20683 = 10³ + 27³  = 19³ + 24³
```

The ore reports the maximizers as `{1729, 4104, 13832, 40033}` — omitting thirteen, including
**20683**, which is smaller than one of the four it does list.

---

## Reproduce

`measured_values.py` computes all six from scratch — the prime-square representation table, the
Möbius squarefree count, the constant at 60-digit precision, the totient preimage sweep, the
divisor condition with its `τ(m) ≤ 2√m` cutoff, and the cube-sum enumeration. Exits 0.
