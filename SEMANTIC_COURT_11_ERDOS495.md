# Semantic Court 11 — Erdős #495: the golden-ratio counterexample dies twice

Author: Jared Wilder  
Public release: 2026-09-11

Erdős #495 is Littlewood's conjecture:

`liminf_{n->infinity} n ||n alpha|| ||n beta|| = 0`.

## False raw counterexample

The chronology claims that taking

`alpha=beta=phi=(1+sqrt(5))/2`

refutes the conjecture because the golden ratio is badly approximable and therefore

`||n phi|| >= c/n`.

It then incorrectly concludes

`n ||n phi||^2 >= c^2 > 0`.

The algebra is wrong. Squaring the approximation bound gives

`n ||n phi||^2 >= c^2/n`,

and `c^2/n -> 0`. A lower bound tending to zero cannot produce a positive liminf.

The chronology notices and withdraws this error once, but a later row marked `PROVED` resurrects the same claim. That later label is also false.

## Exact golden-ratio subsequence

Let `F_k` be the Fibonacci numbers. The convergents of `phi` satisfy, for `k>=2`,

`|F_k phi - F_(k+1)| = phi^(-k)`.

Hence

`||F_k phi|| = phi^(-k)`

and therefore

`F_k ||F_k phi||^2 = F_k phi^(-2k) -> 0`.

So the proposed golden-ratio witness actually **satisfies** the Littlewood conclusion on an explicit subsequence.

## Stronger diagonal fact

More generally, for every real `alpha`,

`liminf_{n->infinity} n ||n alpha||^2 = 0`.

If `alpha` is rational, the expression is exactly zero on infinitely many multiples of its denominator. If `alpha` is irrational, Dirichlet/continued-fraction approximation gives infinitely many `n` with

`||n alpha|| < 1/n`,

so

`n ||n alpha||^2 < 1/n -> 0`.

Thus **no diagonal pair `(alpha,alpha)` can refute Littlewood's conjecture**.

## Verdict

Reject every raw #495 row claiming a positive Littlewood liminf from `alpha=beta=phi` or from bad approximability on the diagonal.

The canonical distinct-irrational problem remains the difficult content.

## Operational lesson

A Diophantine approximation lower bound of size `1/n` changes scale when inserted into a product. Every asymptotic substitution must carry its powers of `n` explicitly. A theorem can be correctly cited and still be used with the wrong homogeneity.

The second lesson is chronological: a later `PROVED` label may resurrect a claim that the same campaign already refuted. Terminal status must be recomputed from mathematics, not selected by latest timestamp alone.

## License

Apache-2.0.
