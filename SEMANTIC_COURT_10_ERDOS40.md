# Semantic Court 10 — Erdős #40: finite Sidon density does not glue to an infinite `sqrt(N)` sequence

Author: Jared Wilder  
Public release: 2026-09-11

Erdős #40 asks for which divergent functions `g(N)` the lower-density condition

`A(N) >> sqrt(N)/g(N)`

forces the additive representation function `1_A*1_A(n)` to be unbounded.

## False raw close

The Day-One chronology repeatedly claims that a globally dense infinite Sidon set satisfies

`A(N) >> sqrt(N)`

for all large `N` while its representation function remains bounded, and therefore that the implication fails for **every** divergent `g`.

That premise is false.

## Infinite Sidon sets are not as dense as optimal finite Sidon sets

Finite Sidon subsets of `[1,N]` can have size asymptotic to `sqrt(N)`. But those finite extremizers do not automatically glue into one infinite Sidon sequence retaining that density at every scale.

Erdős proved that every infinite Sidon set has density dips; in particular

`liminf A(N)/sqrt(N) = 0`,

and stronger logarithmic forms are known.

Ruzsa's landmark infinite construction has

`A(N)=N^(sqrt(2)-1+o(1))`,

where `sqrt(2)-1≈0.4142`, strictly below exponent `1/2`.

Thus the raw route silently replaced the difficult infinite-sequence problem by the finite extremal Sidon theorem.

## What is actually known toward #40

Bounded-representation `B_2[G]` constructions do give genuine counterexamples for substantial classes of `g`. In particular, modern work yields polynomial-loss ranges: for fixed `G`, one can obtain counting functions of exponent `G/(2G+1)=1/2-1/(4G+2)` while keeping the representation function uniformly bounded.

Therefore the implication fails for divergent `g` growing at least like a suitable positive power of `N`.

That does **not** settle slowly divergent functions such as powers of `log N`, `log log N`, or general `N^{o(1)}` functions. Those are exactly the scales the original problem is designed to probe.

## The finite-to-infinite trap

The false close used reasoning of the form:

1. for each finite `N`, there is a Sidon set in `[1,N]` of size about `sqrt(N)`;
2. therefore there is one infinite Sidon set having that density at every sufficiently large scale.

Step 2 does not follow. Compatibility across all scales is the entire obstruction in dense infinite Sidon theory.

## Verdict

**Reject the claim that Erdős #40 is false for every divergent `g`.**

The correct public status is a partial negative range, with the slowly-divergent/subpolynomial regime still nontrivial.

## Sources checked

- Erdős's density restriction for infinite Sidon sequences.
- I. Z. Ruzsa, *An Infinite Sidon Sequence*, J. Number Theory 68 (1998), giving exponent `sqrt(2)-1`.
- Modern audits of Erdős #40 separating polynomial-loss counterexamples from the unresolved logarithmic/subpolynomial regime.

## Operational lesson

**Finite extremal constructions do not glue automatically.** Whenever a route moves from “for every scale there exists a finite object” to “there exists one infinite object good at every scale,” an explicit compatibility/gluing theorem is load-bearing and must be proved.

## License

Apache-2.0.
