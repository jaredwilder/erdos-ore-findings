# Gold Rush 03 — five survivors from the Day-One archive

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Release class:** independently rechecked ore promotion  
**Historical novelty:** not claimed unless separately established.

This tranche was mined from the uploaded Day-One archive and rechecked against the full problem-card chronology rather than trusting `PROVED`, audit rank, or kernel labels. One important example (#700) was first promoted by the audit, then falsely killed by a later chronology entry, then restored by direct arithmetic and an independent proof. That is exactly the adjudication model used here: **truth outranks labels and chronology**.

---

## 1. Erdős 400 — universal factorial witness

For fixed `k >= 2`, let `g_k(n)` be the maximum of

`(a_1 + ... + a_k) - n`

over integer tuples satisfying

`a_1! ... a_k! | n!`.

### Theorem

For every `m,k >= 2`,

`g_k(m!) >= m+k-3`.

### Proof

Set `n=m!` and choose

`(a_1,...,a_k) = (m!-1, m, 1, ..., 1)`.

Then

`a_1! ... a_k! = (m!-1)! m! = (m!)! = n!`,

so the divisibility condition holds with equality. The objective is

`(m!-1)+m+(k-2)-m! = m+k-3`.

Therefore `g_k(m!) >= m+k-3` for every `m,k>=2`.

This is an infinite universal family. The archived Lean artifact checked only a single numerical instance; the mathematics is much stronger than that receipt.

---

## 2. Erdős 289 — Kürschák 2-adic obstruction, with a multi-interval parity corollary

Let

`H([a,b]) = sum_{n=a}^b 1/n`

for a finite interval of consecutive positive integers of length at least two.

### Theorem A

`H([a,b])` is never an integer.

### Proof

Among any finite set of consecutive integers there is a **unique** integer with maximal `v_2`.

Indeed, if two distinct integers `x<y` both had the same maximal exact valuation `v_2=e`, then `x/2^e` and `y/2^e` would both be odd, so `(y-x)/2^e` would be even. Hence `2^(e+1) | y-x`, and between `x` and `y` lies a multiple of `2^(e+1)`, contradicting maximality of `e`.

Let `L=lcm(a,...,b)` and let `n_*` be that unique maximal-`v_2` denominator. In

`L H([a,b]) = sum_{n=a}^b L/n`,

the term `L/n_*` is odd and every other term is even. Thus `L H([a,b])` is odd. But `L` is even because the interval has length at least two. If `H([a,b])` were an integer, `L H([a,b])` would be divisible by the even integer `L`, contradiction.

### Theorem B

Suppose a finite multiset of length-at-least-two intervals has total reciprocal sum in `Z`. For each interval let `e_i` be the maximum `v_2` among its denominators, and put `E=max e_i`. Then the number of intervals with `e_i=E` is even.

### Proof

Take `L` to be the lcm of all denominators. Modulo two, an interval contributes `1` to `L` times the total sum exactly when its own maximum equals `E`; otherwise it contributes `0`. Since the total sum is integral and `L` is even, the total parity is zero. Hence the number of intervals attaining `E` is even.

This is the universal theorem hiding behind the archive's bounded finite verifiers.

---

## 3. Erdős 247 — sparse binary support forces irrationality

Let

`1 <= a_1 < a_2 < ...`

be integers with

`limsup a_n/n = infinity`,

and define

`x = sum_{n>=1} 2^(-a_n)`.

### Theorem

`x` is irrational.

### Proof

The binary expansion of `x` has digit `1` exactly in positions `a_n` and `0` elsewhere. The hypothesis `limsup a_n/n=infinity` implies that this digit sequence cannot eventually have positive density; in particular it is not eventually all `1`s, so there is no binary-expansion ambiguity from a terminal tail of ones.

If `x` were rational, its binary expansion would be eventually periodic. Because it contains infinitely many `1`s, some period block would contain at least one `1`. If the eventual period has length `p`, the number of `1`s among the first `N` tail digits would then be at least `N/p-O(1)`. Equivalently,

`a_n <= p n + O(1)`,

which makes `limsup a_n/n` finite. Contradiction.

Thus `x` is irrational.

This is a genuine theorem but only a partial result toward the canonical transcendence question.

---

## 4. Erdős 313 — the fixed head `(2,3,p)` has exactly one prime continuation

Consider solutions of

`1/p_1 + ... + 1/p_k = 1 - 1/m`

with `m>=2` and distinct increasing primes.

### Theorem

If the first three primes are `(2,3,p)`, then necessarily `p=7` and `m=42`.

### Proof

The equation becomes

`1/2 + 1/3 + 1/p = 1 - 1/m`,

hence

`1/m = 1/6 - 1/p = (p-6)/(6p)`

and therefore

`m = 6p/(p-6) = 6 + 36/(p-6)`.

Since `m` is an integer and `p>6`, the positive integer `p-6` divides `36`. Checking the positive divisors of `36`, the only value for which `p=6+(p-6)` is prime is `p=7`. Then `m=42`.

So the familiar head `(2,3,7)` is forced; there is no infinite family with the fixed head `(2,3,p)`.

---

## 5. Erdős 700 — semiprime formula, rescued from a false internal refutation

Define

`f(n) = min_{1<k<=n/2} gcd(n, C(n,k))`.

### Theorem

If `n=pq` with primes `p<=q` (allowing `p=q`), then

`f(pq)=p=min(p,q)=n/P(n)`.

This is a known public baseline for Erdős #700. It is included here because the Day-One archive later falsely claimed that `n=21` refutes it.

### Proof for distinct primes `p<q`

Use

`k C(n,k) = n C(n-1,k-1)`.

Write `d=gcd(n,C(n,k))`, `n=d n'`, and `C(n,k)=d c'` with `gcd(n',c')=1`. The identity implies

`n' | k`,

so

`n / gcd(n,C(n,k)) | k`.

For `n=pq` and `1<k<=pq/2`, `gcd(n,C(n,k))` cannot be `1`, because that would force `pq|k`. Therefore every admissible gcd is at least `p`.

Now take `k=q`, which is admissible because `q<=pq/2`. Lucas' theorem modulo `q` gives

`C(pq,q) ≡ C(p,1) C(0,0) ≡ p (mod q)`.

Thus `q` does not divide `C(pq,q)`, while the divisibility identity above forces the gcd to be at least `p`. Hence

`gcd(pq,C(pq,q))=p`,

so `f(pq)=p`.

### Prime-square case

For `n=p^2`, the same lower-divisibility identity forces every admissible gcd to be divisible by `p`. Taking `k=p`, Kummer's theorem gives

`v_p(C(p^2,p))=1`,

so `gcd(p^2,C(p^2,p))=p`. Therefore `f(p^2)=p`.

### The archive's false kill

The problem card later asserted that `n=21` is a counterexample and claimed `gcd(21,C(21,7))=9`. Direct arithmetic gives

`C(21,7)=116280`,

`gcd(21,116280)=3`.

So `f(21)=3`, exactly as the theorem predicts. The later `FALSE` row is false; the theorem survives.

---

## Release doctrine

These five items were promoted only after reading the full chronology and independently rebuilding the proofs. No `PROVED`, `KERNEL_CHECKED`, audit score, or late registry state was treated as authoritative by itself.

`verify_gold_rush_03.py` supplies finite regression checks for the arithmetic portions. The proofs above, not the finite tests, carry the universal statements.
