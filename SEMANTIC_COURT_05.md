# Semantic Court 05 — five low-score rows that could poison a mass release

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Source:** Day-One MSL / Erdős ore archive  
**Release class:** correction / anti-resurrection record

This court was mined deliberately from lower-ranked rows rather than the headline queue. That matters: several of the most dangerous claims in a large research corpus are short, elementary-looking “negative closes” that are easy to propagate because they appear too simple to question.

The five cases below were checked against the frozen archive, direct arithmetic, and current public problem statements.

---

## 1. Erdős 396 — the claimed `k=2` impossibility is refuted by `n=2480`

### Canonical problem

For every `k`, does there exist `n` such that

`∏_{0≤i≤k}(n-i) | C(2n,n)`?

A Day-One `PROVED` row claims that `k=2` admits no `n`, using a prime `p` from a Bertrand-type interval and asserting that it divides

`n(n-1)(n-2)`

exactly once while not appearing in the central binomial coefficient.

### The elementary gap in the proof

A prime lying in an interval such as `(n/2,n-2]` does **not** thereby divide any of the three integers `n,n-1,n-2`. Interval membership is not divisibility.

The later attempted repair using a prime in `(2n/3,n]` also fails: for primes not lying in the last three positions, the valuation of the factorial quotient picks up contribution from `(n-3)!`, so the advertised uniform valuation `-1` does not hold.

### Exact refutation

The smallest known witness for `k=2` is

`n=2480`.

Direct exact arithmetic gives

`2480·2479·2478 | C(4960,2480)`.

OEIS A375077, which records the least witness for each `k`, begins

`2, 2480, 8178, 45153, ...`

for `k=1,2,3,4,...` under the corresponding indexing convention.

Thus the Day-One “negative close via k=2” is not merely unproved; it is false.

### Current status

Erdős #396 remains open in the universal `∀k∃n` form.

External reconciliation:

- https://www.erdosproblems.com/396
- https://oeis.org/A375077

---

## 2. Erdős 943 — the mine solved multiplicative convolution, not the stated additive problem

### Canonical problem

Let `A` be the set of powerful numbers. Is the additive representation function

`(1_A * 1_A)(n)`

subpolynomial, i.e. `n^{o(1)}`?

Here the convolution is **additive**:

`(1_A * 1_A)(n) = #{(a,b)∈A² : a+b=n}`

(up to the standard ordered/unordered convention).

### Day-One semantic drift

Several rows replace this with multiplicative factorisation counting. They enumerate divisors `a|n`, inspect prime exponents of `n`, and count pairs with

`ab=n`.

That is Dirichlet/multiplicative convolution, a different function.

The archive then derives exact product formulas in the prime exponents of `n` and promotes them as a proof of the canonical statement. Those formulas may be correct for the multiplicative problem and are irrelevant to the additive one.

### External confirmation

Thomas Bloom explicitly clarified this exact ambiguity in a public discussion of Erdős #943: `1_A*1_A(n)` here denotes **additive convolution**, counting powerful `a,b` with `a+b=n`, not factor pairs. The original question remains open.

The modern Formal Conjectures encoding also uses an additive representation-count function.

### Verdict

**OPERATION SEMANTICS FAILURE.**

Any theorem miner must type the ambient semigroup/group operation before manipulating a convolution symbol. A proof about divisor pairs cannot be promoted into a theorem about additive representations merely because both are written with `*` in different contexts.

External reconciliation:

- https://www.erdosproblems.com/943
- https://math.stackexchange.com/questions/5113585/erdos-problem-943-and-its-lean-formalisation
- Google DeepMind Formal Conjectures, `ErdosProblems/943.lean`

---

## 3. Erdős 317 — the LCM granularity bound points in the wrong direction for clause 1

### Canonical first clause

Does there exist a constant `c>0` such that for every `n` there is a nonzero signed reciprocal sum

`S = Σ_{k≤n} δ_k/k`,  `δ_k∈{-1,0,1}`

with

`0<|S|<c/2^n`?

### Correct granularity fact

If `L_n=lcm(1,...,n)`, every such signed sum is an integer multiple of `1/L_n`. Hence every nonzero sum satisfies

`|S| ≥ 1/L_n`.

The Day-One card correctly proves this, then incorrectly says it **refutes clause 1** because

`L_n/2^n -> ∞`.

### Direction check

`L_n` grows roughly like `e^n`, faster than `2^n`. Therefore

`1/L_n`

is **much smaller** than

`1/2^n`.

A lower bound by a much smaller quantity does not prevent a signed sum from lying below `c/2^n`.

Already at `n=10`,

`L_10=2520`,

so

`1/L_10 = 1/2520 < 1/1024 = 2^{-10}`.

Thus the granularity theorem is compatible with the desired first-clause upper scale; it does not negate it.

### Second clause

The same granularity identity explains why the **nonstrict** inequality

`|S| ≥ 1/L_n`

is automatic. The actual question asks for eventual **strict** inequality. Equality occurs at small `n`, e.g.

`1/2 - 1/3 - 1/4 = -1/12 = -1/L_4`.

The current #317 page remains open and explicitly distinguishes these two issues.

### Verdict

**RECIPROCAL/ASYMPTOTIC DIRECTION ERROR.**

External reconciliation:

- https://www.erdosproblems.com/317

---

## 4. Erdős 881 — one bad deletion does not refute an existential deletion theorem

### Canonical quantifiers

Let `A` be a minimal asymptotic basis of order `k`, in the strong sense that deleting any infinite subset destroys order `k`.

Must there **exist** an infinite `B⊂A` such that `A\B` is a basis of order `k+1`?

### False Day-One counterexample pattern

A row takes the endpoint `k=1`, `A=N`, chooses one specific infinite `B`, shows that this particular `A\B` is not an order-2 basis, and declares the canonical existential statement false.

That is a quantifier error.

To refute

`∃ infinite B : A\B is an order-(k+1) basis`,

one must prove failure for **every** infinite `B⊂A`, not exhibit one inconvenient deletion.

### The same card contains an affirmative endpoint construction

For `k=1`, take `A=N` and

`B={n : n≡2 (mod 4)}`.

Then `A` is strongly minimal as an order-1 asymptotic basis: deleting any infinite subset leaves infinitely many omitted integers, so the remainder is not eventually all integers.

But `A\B` contains precisely the positive integers in residue classes `0,1,3 mod 4`. Pairwise sums of these residue classes cover all four residues modulo 4:

- `0=0+0`,
- `1=0+1`,
- `2=1+1`,
- `3=0+3`.

Choosing sufficiently large summands gives an order-2 asymptotic basis.

So the endpoint `k=1` is positive, and the naive negative row is false for purely logical reasons.

### Current status

The general problem is still listed open. A 2026 public discussion contains a proposed complete answer, but the site owner notes that a standard check found major gaps in the writeup; it is not incorporated as a verified solution.

### Verdict

**EXISTS/FORALL DELETION SLIP.**

External reconciliation:

- https://www.erdosproblems.com/881
- https://www.erdosproblems.com/forum/thread/881

---

## 5. Erdős 1203 — maximal-order bounds do not make `F(n)` bounded

### Canonical problem

Let

`F(n)=max_k ω(n+k) · loglog(k)/log(k)`

(with the natural domain restriction on `k`). Prove that

`F(n)->∞`.

Several late Day-One rows claim a negative close of the form

`F(n)=O(1)`

by combining the maximal-order estimate

`ω(m) ≲ log m / loglog m`

with heuristic comparisons between `m=n+k` and `k`.

### Exact obstruction to any uniform boundedness claim

Fix `k=3`. Then the positive constant

`c_3 = loglog(3)/log(3)`

is fixed.

For any `r`, let

`M_r = p_1 p_2 ... p_r`

be the product of the first `r` primes and choose

`n_r = M_r - 3`.

Then

`ω(n_r+3)=ω(M_r)=r`.

Therefore

`F(n_r) ≥ c_3 r`,

which tends to infinity with `r`.

Hence `F(n)` is unbounded on a subsequence. In particular, all Day-One rows claiming a global `F(n)=O(1)` theorem are false.

### What this does NOT prove

Unboundedness on a subsequence is far weaker than the canonical statement

`F(n)->∞` for every sufficiently large n.

So this correction kills the negative boundedness route without solving the open problem positively.

The current #1203 page remains OPEN and records only the easy baseline

`F(n)≥1-o(1)`.

### Verdict

**MAXIMAL-ORDER VARIABLE-MISMATCH / SUBSEQUENCE DISTINCTION.**

External reconciliation:

- https://www.erdosproblems.com/1203

---

## Five reusable blades extracted from this court

1. **Interval-is-not-divisibility blade:** membership of a prime in a numerical interval never implies it divides a nearby product (#396).
2. **Operation-typing blade:** type every convolution as additive, multiplicative, or another operation before using it (#943).
3. **Reciprocal-direction blade:** when inverting asymptotic scales, reverse inequalities carefully (#317).
4. **Quantifier-blade for witnesses:** one failed existential witness cannot refute an existential conclusion (#881).
5. **Fixed-parameter subsequence blade:** a fixed `k` can destroy a claimed uniform upper bound without proving a full-limit lower bound (#1203).

These blades should be applied automatically to the remaining low-score ore, where short false closes are otherwise easy to mistake for finished mathematics.
