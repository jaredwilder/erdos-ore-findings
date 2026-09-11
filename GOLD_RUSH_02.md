# Gold Rush 02 — five independently verified ore promotions

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Release class:** mathematically rechecked ore promotion  
**Historical novelty:** **not claimed**. Truth, provenance, and novelty are separate questions.

This tranche was mined from `jaredwilder/msl-ore-estate`, especially the promoted catalog. Each result below was re-derived independently before promotion. The accompanying `verify_gold_rush_02.py` is a regression/recomputation layer; the universal claims are proved here rather than inferred from finite tests.

---

## 1. Erdős 949 — a sharp five-point forcing lemma for sum-free sets

### Theorem

Let `S ⊂ R` be sum-free: there are no `x,y,z ∈ S` with `x+y=z` (allowing `x=y`). Then there exists

`q ∈ {1,2,3,4,5}`

such that both `q ∉ S` and `2q ∉ S`.

Moreover **5 is sharp** for this finite forcing statement: the sum-free set `{1,4,6}` meets at least one of `{q,2q}` for every `q=1,2,3,4`.

### Proof

Assume for contradiction that for every `q=1,...,5`, at least one of `q,2q` lies in `S`.

**Case 1: `1 ∈ S`.** Then `2 ∉ S`, since `1+1=2`. The `q=2` pair forces `4 ∈ S`. For `q=3`, we cannot have `3 ∈ S`, because `1+3=4`; hence `6 ∈ S`. For `q=5`, we cannot have `5 ∈ S`, because `1+5=6`; hence `10 ∈ S`. But now `4+6=10`, contradiction.

**Case 2: `1 ∉ S`.** The `q=1` pair forces `2 ∈ S`, hence `4 ∉ S` because `2+2=4`. The `q=4` pair therefore forces `8 ∈ S`. For `q=3`, `6 ∈ S` is impossible because `2+6=8`; hence `3 ∈ S`. Then `5 ∉ S` because `2+3=5`, so the `q=5` pair forces `10 ∈ S`. But `2+8=10`, contradiction.

Thus some `q≤5` has `q,2q∉S`.

For sharpness, `{1,4,6}` is sum-free and hits the pairs `{1,2}`, `{2,4}`, `{3,6}`, `{4,8}`. Therefore no universal bound `q≤4` is possible.

**Ore source:** promoted catalog, Erdős 949. The source recorded the `q≤5` theorem and sharpness as a discovery-gold item. This release supplies a complete independent proof.

---

## 2. Erdős 479 — an infinite congruence family

### Theorem

Let `j≥0`, let `p` be any odd prime, and set

`e = 2^j`, `n = ep`.

Then

`n | (2^n - 2^e)`.

Equivalently, for every `j≥0`, the fixed value `k=2^(2^j)` has infinitely many witnesses `n=2^j p` to

`2^n ≡ k (mod n)`.

### Proof

Factor

`2^n - 2^e = 2^e (2^(e(p-1)) - 1)`.

Since `p` is odd, Fermat's little theorem gives `2^(p-1) ≡ 1 (mod p)`, so

`p | 2^(e(p-1)) - 1`.

Also `e=2^j` divides `2^e`, because `e=2^j≥j` and therefore `2^j | 2^(2^j)`.

Finally `gcd(e,p)=1`, so the two divisibilities combine to give

`ep | 2^e (2^(e(p-1))-1)`.

Hence `n | 2^n-2^e`.

**Ore source:** promoted catalog, Erdős 479. The ore already marked this as an infinite family; this release re-derives it from Fermat plus the coprime factor split.

---

## 3. Erdős 727 — an infinite factorial-divisibility obstruction

### Theorem

For every prime `p≥7`, put `n=2p-2`. Then

`((n+2)!)^2 ∤ (2n)!`.

### Proof

Here `n+2=2p`. For `p≥7`,

`v_p((2p)!) = 2`,

because the multiples of `p` up to `2p` are exactly `p,2p`, and `p^2>2p`. Therefore

`v_p(((n+2)!)^2)=4`.

On the other hand `2n=4p-4`. The multiples of `p` up to `4p-4` are exactly `p,2p,3p`, while `p^2>4p-4`. Hence

`v_p((2n)!) = 3`.

The right-hand factorial has only three factors of `p`, while the proposed divisor requires four. Divisibility is impossible.

**Ore source:** promoted catalog, Erdős 727. A targeted literature/web collision check found the same valuation observation in older public discussion, so **no novelty claim is made here**. Its value in this release is as a clean, independently verified infinite obstruction family with preserved provenance.

---

## 4. Erdős 887 — an explicit two-divisor cluster at the fourth-root scale

### Theorem

For every integer `m≥2`, define

`N = m(m-1)(m+1)(m+2)`,

`d1 = m(m+1)`, `d2 = m(m+2)`.

Then `d1` and `d2` are divisors of `N` and both lie in

`(sqrt(N), sqrt(N) + 2 N^(1/4))`.

### Proof

Both divisibilities are immediate:

`N/d1 = (m-1)(m+2)`,

`N/d2 = (m-1)(m+1)`.

Let `A=m(m+1)=d1`. Then

`N = A(A-2)`.

Therefore

`d1^2-N = A^2-A(A-2)=2A>0`,

so `d1>sqrt(N)`, and hence also `d2>d1>sqrt(N)`.

For the upper bound, since `A≥6`,

`N-(A-2)^2 = 2A-4>0`,

so `sqrt(N)>A-2`. Thus

`d2-sqrt(N) < (A+m)-(A-2)=m+2`.

It remains to show `m+2≤2N^(1/4)`. Raising to the fourth power, this is implied by

`(m+2)^4 ≤ 16N`.

The difference factors as

`16m(m-1)(m+1)(m+2) - (m+2)^4`

`= (m+2)(15m^3 - 6m^2 - 28m - 8)`.

The cubic equals `32` at `m=2` and is strictly increasing for `m≥2`, because its derivative `45m^2-12m-28` is positive there. Hence the difference is positive for every `m≥2`.

Therefore

`d2 < sqrt(N)+m+2 ≤ sqrt(N)+2N^(1/4)`,

and the same upper bound holds for `d1<d2`.

**Ore source:** promoted catalog, Erdős 887. The source contained both a sufficiently-large-`m` version and a sharpened `m≥2` version; this release verifies the all-`m≥2` statement directly.

---

## 5. Erdős 1061 — an infinite sigma-identity family

### Theorem

If `gcd(a,6)=1`, then

`sigma(a) + sigma(2a) = sigma(3a)`.

Consequently `(a,2a)` and `(2a,a)` give infinitely many ordered solutions of

`sigma(x)+sigma(y)=sigma(x+y)`.

### Proof

Because `gcd(a,6)=1`, both `gcd(a,2)=1` and `gcd(a,3)=1`. Multiplicativity of the divisor-sum function gives

`sigma(2a)=sigma(2)sigma(a)=3sigma(a)`,

`sigma(3a)=sigma(3)sigma(a)=4sigma(a)`.

Hence

`sigma(a)+sigma(2a)=sigma(a)+3sigma(a)=4sigma(a)=sigma(3a)`.

There are infinitely many positive integers coprime to `6`, so this yields an infinite family.

**Ore source:** promoted catalog, Erdős 1061. This is released as verified structure, not as a historical novelty claim.

---

## Reproducibility

Run:

```bash
python verify_gold_rush_02.py
```

The script:

- exhausts all subsets of `{1,...,10}` for the Erdős 949 forcing lemma and verifies the sharpness witness;
- checks the Erdős 479 congruence family across a grid of primes and exponents;
- checks the exact `p`-adic valuation mismatch for Erdős 727;
- checks the exact algebraic inequalities behind the Erdős 887 divisor family over a large finite regression range;
- checks the Erdős 1061 sigma identity over a large finite regression range.

The finite checks are regression evidence. The proofs above carry the universal statements.
