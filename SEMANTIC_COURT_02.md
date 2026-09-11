# Semantic Court 02 — five open-problem contamination corrections

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Source:** Day-One MSL / Erdős ore archive  
**Purpose:** prevent locally green or late-stage workflow claims from being mistaken for mathematical closes.

This packet records five claims that fail after canonical-statement reconciliation, elementary recomputation, or current-source comparison. These are not criticisms of the mine. They are exactly why the mine preserves chronology: a research corpus becomes more valuable when later users can distinguish a theorem from a locally green label.

No novelty claim is made here. The positive statements retained below are scoped exactly.

---

## 1. Erdős 385 — the `3 p*` closure mechanism has no valid witness

### Canonical problem

For

`F(n) = max_{m<n, m composite} (m + p(m))`,

where `p(m)` is the least prime divisor of `m`, ask whether `F(n)>n` eventually and whether `F(n)-n -> infinity`.

The Day-One chronology contains a route claiming that if `p*` is the largest prime below `n/2`, then

`F(n) >= 3 p*`,

which, combined with prime-gap information, would essentially close the problem.

### Why the mechanism fails

The natural candidate `m=2p*` does **not** contribute `3p*`: its least prime divisor is `2`, so it contributes

`m+p(m) = 2p*+2`.

Trying `m=3p*` does not repair the argument: when `p*` is near `n/2`, `3p*>n`, so this is not an admissible `m<n`.

The claimed lower bound is also directly false numerically. For example:

- `n=100`: exact evaluation gives `F(100)=102`, while `p*=47` and `3p*=141`;
- `n=1000`: `F(1000)=1012`, while `p*=499` and `3p*=1497`.

Thus the proposed `3p*` engine cannot be used.

### What survives

The elementary parity baseline in the same card is correct:

- for odd `n>=5`, take `m=n-1`; then `m` is even composite and `p(m)=2`, hence `F(n)>=n+1`;
- for even `n>=6`, take `m=n-2`; then `F(n)>=n`.

This reduces the first clause's difficulty to even `n`, but does not close either asymptotic question.

Current public status check: Erdős #385 remains open. Terence Tao's 2024 discussion of the problem explains the genuine sieve/parity obstruction around this question.

---

## 2. Erdős 1056 — singleton “closes” are semantic drift, not solutions

### Canonical problem

For every `k>=2`, ask whether there is a prime `p` and **consecutive intervals** `I_1,...,I_k` whose products are all `1 mod p`.

The Day-One registry repeatedly promotes constructions such as

- `p=2`, `I_i={2i-1}`;
- repeated `I_i={1}`;
- arbitrary separated singleton intervals,

as complete affirmative closes.

### Why those closes fail the intended semantics

The current Formal Conjectures encoding represents the intervals by one strictly increasing boundary map

`b_0 < b_1 < ... < b_k`

and uses

`I_i = [b_i,b_{i+1})`.

That is the ordinary adjacent/consecutive-block reading: the end of one interval is the beginning of the next. Separated odd singletons such as `{1},{3},{5},...` are not consecutive blocks under this definition, and repeating `{1}` is not possible under strict boundaries.

There is an even simpler obstruction to the proposed `p=2` family. Any nonempty interval with product `1 mod 2` must contain only odd integers. Two adjacent nonempty integer intervals cannot both contain only odd integers, because their common boundary forces the next block to begin at the following integer parity. The Day-One card itself eventually records this as a FALSE correction.

Known small examples fit the intended semantics: for `k=2`, boundaries `[3,5,8]` give blocks `{3,4}` and `{5,6,7}`, whose products are both `1 mod 11`.

Current public/open formal sources still classify the general problem as research-open. Therefore the singleton rows must not be used as closure evidence.

---

## 3. Erdős 40 — the alleged `sqrt(N)` infinite Sidon close crosses an open frontier

### Canonical problem

For what divergent functions `g(N)` does

`A(N) >> sqrt(N)/g(N)`

force the representation function `1_A * 1_A` to be unbounded?

A Day-One `PROVED` row states that “global Erdős–Turán Sidon sets” have

`A(N) >> sqrt(N)`

while the representation function stays bounded, and therefore the answer class is empty for every divergent `g`.

### Why that claim cannot stand

An infinite Sidon sequence with `A(N) >> sqrt(N)` uniformly would contradict the classical infinite-Sidon density obstruction: every infinite Sidon set has dips below the finite `sqrt(N)` scale. More concretely, the current best explicit exponent for an infinite Sidon sequence is the Ruzsa/Cilleruelo exponent `sqrt(2)-1`, not `1/2`.

The current Erdős #40 page explicitly remains open and notes that the question is stronger than the Erdős–Turán conjecture. A 2026 literature audit obtains rigorous counterexamples only in a polynomial-loss range of `g`, not for every arbitrarily slowly divergent `g`.

So the row conflates dense **finite** Sidon sets with a single infinite set having comparable density at all scales. That gluing step is exactly the missing mathematics.

### What survives

There are rigorous negative ranges for sufficiently rapidly growing `g`, using bounded-representation infinite sequences. Those are genuine partial results. The universal “answer class is empty” conclusion is not.

---

## 4. Erdős 325 — a `7/9` upper density does not refute an `Omega(x)` lower bound

For the `k=3` sum-of-three-cubes counting function, the archive correctly observes the familiar modulo-9 restriction: two residue classes are absent, giving an upper bound of shape

`f(x) <= (7/9)x + O(1)`.

A later locally green row says this **refutes** a strong lower bound `f(x) >> x`.

It does not. An upper bound `f(x) <= 0.778x + O(1)` is fully compatible with a lower bound such as

`f(x) >= 0.01x`

for all sufficiently large `x`. Big-Omega asks only for some positive constant.

The same problem card later catches this and marks the inference FALSE. The modulo-9 observation is useful local structure; it is not a negative solution of the linear-order counting question.

There is a second warning in the same card: counting parameter triples in a box does not by itself lower-bound the number of **distinct** represented integers, because collisions must be controlled.

---

## 5. Erdős 1049 — integer-base periodicity does not automatically transfer to rational bases

The Lambert-series identity

`sum_{n>=1} 1/(t^n-1) = sum_{m>=1} tau(m)/t^m`

for real `t>1` is valid by absolute convergence and divisor reindexing. Several Day-One rows correctly prove this identity.

A separate `PROVED` row claims irrationality for every rational `t>1` because unbounded `tau(m)` would force a non-eventually-periodic “base-t digit expansion.”

That step is not valid as stated. The familiar eventual-periodicity characterization is an integer-base digit theorem. For a nonintegral rational base, the coefficients `tau(m)` are not a canonical digit string in an ordinary positional expansion, and carrying/normalization changes the argument. The problem card later records exactly this domain-drift failure.

Therefore:

- **retain:** the Lambert-series identity;
- **do not promote:** the arbitrary-rational-`t` irrationality conclusion without a separate transfer theorem.

The general rational-`t` irrationality problem remains research-open in current public problem collections.

---

## Release rule extracted from these five cases

A locally green row is not publication authority when any of the following is still unresolved:

1. the proposed witness does not satisfy the frozen definition (#385);
2. ordinary-language semantics were weakened during formalization/search (#1056);
3. a finite extremal construction was silently promoted to one infinite object (#40);
4. asymptotic notation was used in a logically invalid direction (#325);
5. a theorem about one number-system representation was transferred to another domain without a bridge theorem (#1049).

These are reusable regression blades for the rest of the ore estate.

## External reconciliation pointers

- Erdős #385: `https://www.erdosproblems.com/385`; Tao, *The parity problem and Siegel zeroes* (2024 discussion containing this problem).
- Erdős #1056: `https://www.erdosproblems.com/1056`; Google DeepMind Formal Conjectures `ErdosProblems/1056.lean`, using strictly increasing interval boundaries.
- Erdős #40: `https://www.erdosproblems.com/40`; current status OPEN; compare the literature on infinite Sidon sequences by Ruzsa and Cilleruelo.
- Erdős #1049: `https://www.erdosproblems.com/1049`.

The correction ledger is append-only: false closes remain visible so that later mining cannot silently resurrect them.
