# Semantic Court 13 — Erdős #653 regular-polygon argument is semantically invalid

Author: Jared Wilder  
Court date: 2026-09-11

## Verdict

A Pass-6 paragraph attached the regular-polygon chord count `floor(n/2)` to Erdős #653 and concluded that the regular `n`-gon forces

`g(n) <= floor(n/2)`.

That conclusion is **FALSE**.

## Canonical semantics

For a planar configuration `X={x_1,...,x_n}`, define

`R(x_i)=#{ |x_j-x_i| : j!=i }`.

Erdős #653 defines `g(n)` to be the **maximum, over all n-point configurations**, of the number of distinct values among

`R(x_1),...,R(x_n)`.

Thus `R(x_i)` is itself a count of distinct distances seen from one vertex, whereas `g(n)` counts how many different such counts occur across the vertices.

## What a regular polygon actually gives

In a regular `n`-gon, every vertex is symmetry-equivalent and has

`R(x_i)=floor(n/2)`.

Therefore the set of `R`-values is

`{floor(n/2)}`,

which has cardinality **1**.

So the regular polygon contributes a configuration with one distinct `R`-value. It does not show that `g(n)=floor(n/2)`, and it certainly cannot yield the upper bound

`g(n)<=floor(n/2)`

because `g(n)` is defined as a maximum over configurations.

## Two independent semantic errors

The Pass-6 inference contains both:

1. **quantity confusion:** `floor(n/2)` is the value of `R(x_i)` in the regular polygon, not the number of distinct `R`-values;
2. **extremum-direction reversal:** exhibiting one configuration can provide a lower bound on a maximum, not an upper bound.

## Cross-problem contamination

The regular-polygon chord count is load-bearing for the literal counterexample to Erdős #655, which asks about the total number of distinct distances under a centered-circle condition.

It was incorrectly transplanted into #653, a different problem about the diversity of the per-vertex counts `R(x_i)`.

## What survives

The separate Pass-6 claim `g(4)=3` is true and can be proved independently by an explicit four-point configuration. That result is routed separately with a self-contained exact witness.

The asymptotic Erdős #653 problem remains open.