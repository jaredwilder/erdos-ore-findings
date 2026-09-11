# Semantic Court 04 — max slips, theorem-hypothesis loss, and unsupported closes

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Source:** Day-One MSL / Erdős ore archive  
**Release class:** correction / anti-resurrection record

This packet records five further late-stage `PROVED` claims that do not survive direct definition checks or current-literature reconciliation. Each case is useful beyond the individual problem because it exposes a reusable failure mode for automated theorem mining.

---

## 1. Erdős 406 — Senge–Straus does not close the restricted-ternary-digit problem

### Canonical problem

Are there only finitely many powers of `2` whose base-3 expansion uses only the digits `0` and `1`?

The Day-One card contains the terminal claim:

> `2^n has digits {0,1} in base 2 for all n; Senge–Straus (2,3 multiplicatively independent) gives finiteness of such integers in both bases, matching the canonical quantifiers exactly.`

The cited theorem is real. The application is not.

### What Senge–Straus actually controls

For multiplicatively independent bases `a,b`, Senge–Straus proved finiteness of the integers whose **sum of digits in each base is bounded by a fixed constant**. Later effective versions make the same fixed-bound hypothesis.

For `2^n`, the base-2 digit sum is indeed `1`. But if the base-3 expansion of `2^n` contains only `0` and `1`, its ternary digit sum is the **number of 1-digits**, and that number is not bounded by the canonical hypothesis. It may grow with `n`.

Thus the fixed-bound theorem does not apply. The missing statement would be a uniform bound on the number of ternary 1s, which is essentially new information rather than a consequence of “digits belong to `{0,1}`.”

### Current status

The live Erdős #406 page remains OPEN. It records the apparent examples

`1, 4, 256`,

Saye's enormous finite computation, and Narkiewicz's sublinear upper bound for the counting function, but no finiteness proof.

### Verdict

**THEOREM-HYPOTHESIS LOSS.**  
Retain Senge–Straus as relevant background; quarantine the claim that it closes #406.

External reconciliation:

- https://www.erdosproblems.com/406
- H. G. Senge and E. G. Straus, *PV-numbers and sets of multiplicity* (1973)
- C. L. Stewart, *On the representation of an integer in two different bases* (1980)

---

## 2. Erdős 539 — the diagonal contributes `1`, not the set `A`

### Canonical problem

For every `n`-element set `A⊂N`, define

`Q(A) = { a/gcd(a,b) : a,b∈A }`.

Let `h(n)` be the minimum possible size of `Q(A)`.

A Day-One `PROVED` row states:

> `As written h(n)=n exactly: diagonal gives A⊆quotient set, and A={1,...,n} caps values at n.`

The load-bearing lower-bound sentence is false.

### Diagonal check

For every `a∈A`, the diagonal term is

`a/gcd(a,a) = a/a = 1`.

So the diagonal contributes the single value `1`; it does **not** embed `A` into `Q(A)`.

The proposed universal lower bound `|Q(A)|≥|A|` therefore has no proof from the diagonal argument.

### External contradiction

The modern literature now gives

`h(n)=n^(1/2+o(1))`,

with the current Erdős #539 page recording the ProofCouncil upper bound

`h(n) ≤ exp(O(sqrt(log n))) n^(1/2)`.

Hence `h(n)=n` cannot be the correct asymptotic statement.

### What survives

The exact endpoint `h(2)=2` in the same card is valid. It must remain separated from the false universal extrapolation.

### Verdict

**DIAGONAL-IMAGE ERROR + ENDPOINT-TO-ASYMPTOTIC OVERREACH.**

External reconciliation:

- https://www.erdosproblems.com/539

---

## 3. Erdős 489 — choosing `A` to be the primes leaves `B={1}`

### Canonical definitions

Let `A⊂N` satisfy

`|A∩[1,x]| = o(sqrt(x))`,

and define

`B = { n≥1 : a does not divide n for every a∈A }`.

A late Day-One row proposes the primes as `A` and claims

`B={1}∪{primes}`,

then uses prime gaps to force divergence of the squared-gap mean.

### Exact correction

If `A` is the set of all primes, every integer `n>1` has a prime divisor `p`, and that `p` belongs to `A`. Therefore `n` fails the defining condition for membership in `B`.

Hence

`B={1}`,

not `{1}∪{primes}`.

The proposed gap calculation has no sequence of prime gaps to act on.

The same problem card later records this correction as `FALSE`.

### What survives

The finite-`A` periodicity theorem in the card is correct: when `A` is finite, divisibility avoidance is periodic modulo `lcm(A)`, so the squared-gap mean has an exact cyclic-period limit. That is a genuine scoped theorem, not a close of the infinite sparse case.

### Current status

Erdős #489 remains OPEN.

### Verdict

**DEFINITIONAL COMPLEMENT ERROR.**

External reconciliation:

- https://www.erdosproblems.com/489

---

## 4. Erdős 889 — `v(n,0)` is not the maximum `v_0(n)`

### Canonical definition

`v(n,k)` counts the distinct prime factors of `n+k` that are larger than `k`, and

`v_0(n) = max_{k≥0} v(n,k)`.

The Day-One card correctly observes

`v(n,0)=omega(n)`.

It then contains a `PROVED` row claiming that `n=2^m` forces

`v_0(n)=1`,

and therefore refutes `v_0(n)→∞`.

### The max was dropped

For `n=2^m`, the identity gives only

`v(n,0)=1`.

But `v_0(n)` is the maximum over **all** `k`, so another `k` may give a larger value.

This is not merely a theoretical possibility. For example:

- `n=32`, `k=1`: `n+k=33=3·11`, and both primes are `>1`, so `v(32,1)=2`;
- `n=64`, `k=1`: `65=5·13`, hence `v(64,1)=2`.

Thus the proposed powers-of-two counterexample family already fails at tiny values.

Erdős and Selfridge proved the stronger general fact

`v_0(n)≥2` for every `n≥17`.

### Verdict

**MAX-OPERATOR ERASURE.**  
The lower bound `v_0(n)≥omega(n)` via `k=0` is valid, but it supplies only subsequential unboundedness because `omega(n)` itself does not tend to infinity along all integers.

External reconciliation:

- https://www.erdosproblems.com/889
- Erdős–Selfridge (1967), as cited there.

---

## 5. Erdős 200 — a claimed Pintz/Rankin negative close is unsupported

### Canonical problem

Let `L(N)` be the length of the longest arithmetic progression of primes in `{1,...,N}`. Is

`L(N)=o(log N)`?

The Day-One chronology contains a high-scoring `PROVED` row:

> `Pintz's unconditional Rankin-type lower bound gives L(N)=omega(log N) infinitely often, proving the literal negation; negative close achieved.`

No supporting theorem is supplied, and the same card later retreats to:

> a Pintz-type lower bound of the required strength **would** falsify the conjecture and `needs certification`.

### External reconciliation

The live Erdős #200 page remains OPEN and records only the standard upper bound

`L(N) ≤ (1+o(1)) log N`

from the prime number theorem.

Green–Tao proves arbitrarily long prime arithmetic progressions, but that theorem does not give a lower bound of order `omega(log N)` for the longest progression below `N`.

Targeted searches for the claimed Pintz result locate work on arithmetic progressions of bounded prime patterns and consecutive-prime patterns, not an unconditional theorem asserting

`L(N)=omega(log N)` infinitely often.

Given that such a theorem would immediately settle the live-open problem negatively, the estate row cannot be promoted without an exact bibliographic theorem and proof that its `N`-dependence matches the canonical extremal function.

### What survives

The elementary residue restriction in the card is valid: a sufficiently long prime arithmetic progression forces small primes to divide the common difference, apart from the endpoint case in which a progression term itself equals that small prime.

### Verdict

**UNSUPPORTED LITERATURE TRANSFER / CLOSE-BY-CITATION.**  
Quarantine the negative close; retain only the explicitly proved residue/divisibility lemmas.

External reconciliation:

- https://www.erdosproblems.com/200
- Green–Tao, *The primes contain arbitrarily long arithmetic progressions*.

---

## Five reusable blades extracted from this court

1. **Fixed-parameter blade:** a theorem for bounded digit sum cannot be applied when the bound itself may grow (#406).
2. **Diagonal blade:** compute the diagonal map literally before using it as an injection (#539).
3. **Complement-definition blade:** test a proposed witness directly against every quantifier in the set definition (#489).
4. **Extremum-retention blade:** never replace `max_k f(k)` by one convenient value `f(k_0)` (#889).
5. **Bibliographic-close blade:** if a cited theorem would settle a problem still listed open, demand the exact theorem statement, variables, and asymptotic transfer before promotion (#200).

These blades are suitable for automated regression against the remaining late-stage ore.
