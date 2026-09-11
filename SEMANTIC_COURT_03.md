# Semantic Court 03 — literature, quantifier, and source-text contamination

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Source:** Day-One MSL / Erdős ore archive  
**Release class:** correction / anti-resurrection record

This packet records five high-risk failure modes discovered while mining the late `PROVED` tail. The common feature is not bad arithmetic. Each false promotion looks superficially authoritative because it carries one of: a real literature citation, a correct finite construction, a correct local theorem, or a formally frozen source string.

The purpose is to make these claims impossible to resurrect silently in later theorem extraction.

---

## 1. Erdős 749 — Ruzsa's `L²` theorem was silently upgraded to `L∞`

### Canonical problem

Given `ε>0`, does there exist `A⊆N` such that the **lower density** of `A+A` is at least `1-ε` while the representation function

`r_A(n) = 1_A * 1_A(n)`

is uniformly bounded by a constant depending only on `ε`?

### False Day-One promotion

A terminal row says:

> `L1 is Ruzsa's just-basis theorem (JLMS 1990): A+A contains all sufficiently large n with r(n)≤C ... implying the canonical affirmative.`

That is not what Ruzsa proved.

### What Ruzsa actually proved

Ruzsa's 1990 *A just basis* constructs an additive basis of order two for which the representation function is bounded **in square mean**:

`Σ_{n≤N} r_A(n)^2 = O(N)`.

This is an `L²` statement. It does **not** imply a uniform pointwise (`L∞`) bound on `r_A(n)`.

The distinction is load-bearing. A sequence may have bounded second-moment average while still possessing arbitrarily large exceptional values.

The current Erdős #749 page explicitly remains OPEN and its 2026 discussion calls out the Ruzsa result as nearby `L²` progress that does not directly answer the `L∞` question.

### Verdict

**QUARANTINE the `PROVED` close.**  
Retain Ruzsa 1990 as genuine nearby literature, at its actual norm.

External reconciliation:

- https://www.erdosproblems.com/749
- https://www.erdosproblems.com/forum/thread/749
- I. Z. Ruzsa, *A just basis* (1990)
- M. Tang, *A note on a result of Ruzsa, II* (2010), which again states the square-mean theorem explicitly.

---

## 2. Erdős 653 — a configuration witness cannot upper-bound a maximum over configurations

### Canonical quantifiers

For a configuration `X={x_1,...,x_n}⊂R²`, let `R_X(x_i)` be the number of distinct distances from `x_i` to the other points. Let

`g(n) = max_X #{ R_X(x_i) : 1≤i≤n }`.

The problem asks whether

`g(n) ≥ (1-o(1))n`.

### Repeated false Day-One route

Several rows observe that a regular `n`-gon has the same value `R_X(x_i)=floor(n/2)` at every vertex and then conclude one of:

- `g(n)=1`;
- `g(n)≤floor(n/2)`;
- the asymptotic conjecture is false.

All three deductions invert the outer quantifier.

A regular polygon proves only that **there exists a configuration** whose `R`-profile has one distinct value. But `g(n)` is the **maximum** number of distinct values over all configurations. A low-scoring competitor cannot upper-bound a maximum.

The same error appears in grid and generic-configuration variants: properties of one configuration are repeatedly promoted into universal bounds on the extremal function.

### External sanity check

The live Erdős #653 page states the same maximum definition and records published lower bounds, including Csizmadia's

`g(n) > 7n/10`.

That alone is incompatible with the archive's `g(n)=1` rows for large `n`.

### What survives

- the regular-polygon identity itself is true;
- the trivial upper bound `g(n)≤n-1` is true;
- collinear constructions can give genuine **lower bounds** on `g(n)` when they exhibit many distinct `R`-values;
- none of the low-profile configurations refutes the canonical maximum problem.

### Verdict

**QUANTIFIER-INVERSION CONTAMINATION.**  
Any future automated promotion involving an extremum must carry the direction of the outer `max`/`min` explicitly.

External reconciliation:

- https://www.erdosproblems.com/653
- Google DeepMind Formal Conjectures, `ErdosProblems/653.lean`.

---

## 3. Erdős 155 — `A ∪ 3A` is not Sidon in general

### Canonical problem

For `F(N)` the maximum size of a Sidon subset of `{1,...,N}`, ask whether for every fixed `k≥1`,

`F(N+k) ≤ F(N)+1`

for all sufficiently large `N`.

### False Day-One negative close

A `PROVED` row claims:

`A ∪ 3A` is Sidon whenever `A` is Sidon,

hence

`F(3N) ≥ 2F(N)`,

and from the square-root scale of `F(N)` concludes the canonical statement is false.

### One-line counterexample

Take the Sidon set

`A={1,2}`.

Then

`A ∪ 3A = {1,2,3,6}`,

but

`1+3 = 2+2 = 4`.

So the union is not Sidon. The route's load-bearing inequality and the claimed negative close both collapse.

The problem card later correctly records exactly this counterexample.

### What survives

The deletion lemma

`F(N+1)≤F(N)+1`

is elementary and valid for every `N`; it settles only the `k=1` slice. The live #155 problem remains open for the fixed-`k≥2` eventual statement.

External reconciliation:

- https://www.erdosproblems.com/155

---

## 4. Erdős 145 — squarefree gaps are not bounded by four

### Canonical problem

For consecutive squarefree numbers `s_n`, ask for which `α≥0` the limit

`(1/x) Σ_{s_n≤x} (s_{n+1}-s_n)^α`

exists.

### False Day-One universal close

A `PROVED` row asserts that squarefree gaps belong to

`{1,2,3,4}`,

turning the moment into a finite four-term density sum and claiming existence for every `α≥0`.

### Exact falsifier

`241` and `246` are squarefree, while

- `242 = 2·11²`,
- `243 = 3⁵`,
- `244 = 4·61`,
- `245 = 5·7²`

are not squarefree.

Thus there is already a gap of `5` from `241` to `246`.

More generally, CRT constructions force arbitrarily long runs of non-squarefree integers, so squarefree gaps are unbounded.

### What survives — and what the literature now says

The archive's `0≤α≤1` argument is a genuine scoped theorem route, but it is no longer the literature frontier. Current remarks for Erdős #145 cite Tsz Ho Chan (2023), who proves moment existence for all

`0≤α<3.75`,

with earlier work of Huxley reaching `α≤11/3`.

The universal all-`α` question remains beyond this finite-gap argument.

### Verdict

**KILL the bounded-gap close; retain only correctly scoped moment theorems.**

External reconciliation:

- https://www.erdosproblems.com/145
- T. H. Chan, *On moments of gaps between consecutive squarefree numbers* (2023).

---

## 5. Erdős 124 — a source-text typo created a vacuous 'proof'

### Frozen Day-One text

The frozen problem card contains the hypothesis

`Σ_{1≤i≤r} 1/(d_r-1) ≥ 1`.

Because the denominator is the same `d_r-1` in every term, this is just

`r/(d_r-1) ≥ 1`.

For strictly increasing integers `3≤d_1<...<d_r`, one has `d_r≥r+2`, so

`r/(d_r-1) ≤ r/(r+1) < 1`.

Therefore the literal frozen hypothesis is impossible. Several Day-One rows correctly notice this arithmetic and are then labelled `PROVED` because the implication becomes vacuous.

That is **not a mathematical solution of the intended problem**.

### The intended hypothesis

The modern Formal Conjectures source uses

`Σ_i 1/(d_i-1) ≥ 1`,

with the index `i` in the denominator. This is also the formulation used in the underlying complete-sequences literature.

The current formal source now separates the problem into:

- the `k=0` clause, marked solved in the formalization;
- the nonzero-`k` gcd-one clause, still marked research-open there.

The public Erdős Problems page still displays the `d_r` string, demonstrating exactly why scraped text cannot outrank source reconciliation.

### Verdict

The vacuity calculation is **correct about the corrupted string** and **irrelevant as a close of the intended mathematics**.

This is a source-ingestion regression case: when a hypothesis becomes unexpectedly empty, compare against primary/formal/literature sources before promoting vacuity as a theorem.

External reconciliation:

- https://www.erdosproblems.com/124
- Google DeepMind Formal Conjectures, `ErdosProblems/124.lean`
- S. A. Burr, P. Erdős, R. L. Graham, W. W.-C. Li, *Complete sequences of sets of integer powers* (1996).

---

## Five reusable blades extracted from this court

1. **Norm blade:** `L²` does not silently become `L∞` (#749).
2. **Extremum-direction blade:** one competitor cannot upper-bound a maximum (#653).
3. **Closure-under-operation blade:** prove that a construction preserves the defining property before using it asymptotically (#155).
4. **Finite-support blade:** never truncate an unbounded-support distribution without a tail theorem (#145).
5. **Source-fidelity blade:** vacuous truth caused by a transcription/index typo is a data-quality finding, not an open-problem solution (#124).

These five blades should be run automatically against the remaining ore tail before any `PROVED` row is promoted.
