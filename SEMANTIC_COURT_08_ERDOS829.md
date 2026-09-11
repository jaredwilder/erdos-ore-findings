# Semantic audit 08 — Erdős #829 and the Mahler citation

Author: Jared Wilder. Public release: 2026-09-11.

## The problem

Let `A` be the set of nonnegative perfect cubes and let

`r(n)=#{(a,b)∈A^2 : a+b=n}`.

Erdős #829 asks whether there is a fixed constant `C` such that

`r(n)=O((log n)^C)`.

The problem is currently recorded as open.

## Historical citation error

One recovered research row attributes to Mahler a lower bound of the form

`r(n) >= exp(c (log n)^(1/3))`

along an infinite sequence and uses that to reject every polylogarithmic upper bound.

That is not the cited theorem.

The current Erdős #829 literature summary records Mahler's lower bound as

`r(n) >> (log n)^(1/4)`

for infinitely many `n`. Stewart later improved the exponent to

`11/13`.

Both are fixed powers of `log n`, so neither contradicts the possibility that `r(n)=O((log n)^C)` for some larger fixed `C`.

## Additive and Dirichlet convolution are different problems

Historical notes around this problem also drift between two operations:

- additive convolution counts representations `x^3+y^3=n`;
- Dirichlet convolution counts multiplicative factorizations `de=n` with cube constraints.

The formal Erdős #829 statement uses the additive representation function. Divisor-count arguments about multiplicative factorizations therefore do not resolve the stated problem.

## A coarse surviving bound

The elementary estimate

`r(n) <= 2 tau(n)`

is a legitimate coarse upper bound. It is not strong enough to prove a universal polylogarithmic estimate because the maximal order of `tau(n)` is itself larger than every fixed power of `log n` along suitable integers. Conversely, that divisor growth does not create sums-of-two-cubes representations and therefore does not disprove the conjecture.

## Current status

The recovered Mahler-based negative conclusion is rejected. Erdős #829 remains open in the current problem database and formal-conjecture record.

## Sources checked

- K. Mahler, *On the Lattice Points on Curves of Genus 1*, Proc. London Math. Soc. (1935), 431–466.
- C. L. Stewart, *Cubic Thue Equations with Many Solutions*, IMRN (2008), rnn040.
- the current Erdős Problems #829 record;
- Google DeepMind `formal-conjectures`, Erdős 829.

## Correction principle

A citation can name the right author and still be mathematically misused if its quantitative strength is changed. Here, replacing a fixed polylogarithmic lower bound by a super-polylogarithmic one turns compatible evidence into a false disproof.

The exponent and the operation being discussed must both be checked before a literature result is used to change problem status.

## License

Apache-2.0.
