# Semantic Court 08 — Erdős #829: the Mahler citation does not refute the conjecture

Author: Jared Wilder  
Public release: 2026-09-11

## Canonical mathematical object

Let `A` be the set of nonnegative perfect cubes and let the convolution be the **additive representation function**

`r(n) = #{(a,b) in A^2 : a+b=n}`.

Erdős #829 asks whether there is some fixed `C` with

`r(n) = O((log n)^C)`.

## False raw close

The Day-One chronology contains a `PROVED` row asserting that Mahler gives

`r(n) >= exp(c (log n)^(1/3))`

along an infinite sequence, and therefore that `r(n)` exceeds every fixed power of `log n`.

That citation claim is false.

## What Mahler actually proved

Mahler's 1935 theorem gives infinitely many positive integers `n` for which the number of positive representations as a sum of two cubes exceeds

`(log n)^(1/4)`.

This is a fixed power of `log n`, not a super-polylogarithmic function.

The modern Formal Conjectures record for Erdős #829 states the same bound and also records Stewart's later improvement to

`(log n)^(11/13)`

for infinitely many `n`.

Again, `11/13` is a fixed exponent. This is fully compatible with the existence of some larger exponent `C` giving a universal polylogarithmic upper bound.

Thus neither Mahler's theorem nor Stewart's improvement refutes Erdős #829.

## Semantic fork: additive versus Dirichlet convolution

Some historical machine text around this problem also drifted between two meanings of `*`:

- additive convolution counts `x^3+y^3=n`;
- Dirichlet convolution counts multiplicative factorizations `de=n` with both factors cubes.

These are different problems.

The current Formal Conjectures theorem uses its `sumRep` additive representation function, matching the intended sums-of-two-cubes problem. Any primorial/cube argument based on divisor counts belongs to the Dirichlet-convolution fork and cannot close the additive problem.

## Surviving mathematics

The elementary divisor reduction

`r(n) <= 2 tau(n)`

may be useful as a coarse bound, but maximal divisor growth is itself super-polylogarithmic, so this estimate does not prove the desired conjecture. Conversely, the large maximal order of `tau(n)` does not manufacture sums-of-two-cubes representations and therefore does not disprove it.

The raw chronology eventually recognizes exactly this gap. The correct terminal status is:

**Erdős #829 remains open; the Mahler/CRT negative close is rejected.**

## Sources checked

- K. Mahler, *On the lattice points on curves of genus 1*, Proc. London Math. Soc. (1935), especially the theorem giving more than the fourth root of `log n` representations along an infinite sequence.
- C. L. Stewart, *Cubic Thue equations with many solutions*, IMRN (2008), recorded in the modern Erdős #829 formalization with exponent `11/13`.
- Google DeepMind `formal-conjectures`, Erdős 829, which classifies the polylogarithmic upper-bound question as research-open and records both lower bounds above.

## Operational lesson

A real theorem attached to the correct author is not enough. The **quantitative strength** of the cited theorem must be checked. Replacing `(log n)^(1/4)` by `exp(c(log n)^(1/3))` changes a compatible lower bound into a purported disproof of an open problem.

Citation-strength drift is therefore a first-class Semantic Court failure mode.

## License

Apache-2.0.
