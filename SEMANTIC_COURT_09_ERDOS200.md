# Semantic Court 09 — Erdős #200: a prime-gap lower bound is not a prime-AP lower bound

Author: Jared Wilder  
Public release: 2026-09-11

Let `L(N)` denote the maximum length of an arithmetic progression consisting of primes at most `N`. Erdős #200 asks whether

`L(N)=o(log N)`.

## False raw close

The Day-One chronology contains `PROVED` rows asserting that a Pintz / Rankin-type lower bound gives

`L(N) = omega(log N)`

along an infinite sequence and therefore disproves the conjecture.

One row even records a Rankin-shaped factor of the form

`log N * log log N * log log log log N / (log log log N)^2`.

That is not a theorem about the length of prime arithmetic progressions inside `[1,N]`.

## Current mathematical status

The maintained Erdős Problems entry for #200 still lists the problem as open. Its recorded unconditional general bound is the prime-number-theorem upper bound

`L(N) <= (1+o(1)) log N`.

No lower bound of order `omega(log N)` is recorded there; such a result would directly settle the problem negatively.

## What Pintz's AP work actually proves

Pintz proved strong qualitative pattern results combining Green–Tao with bounded-prime-gap technology: for each fixed finite pattern size, certain bounded configurations of consecutive primes occur along arbitrarily long finite arithmetic progressions of translations.

That is a different quantifier structure from a lower bound saying that, among primes `<=N`, the **single longest prime arithmetic progression** has length larger than every constant multiple of `log N` along some sequence of `N`.

Arbitrarily long finite progressions as the ambient scale is allowed to grow do not by themselves give a quantitative relation between progression length and `log N`.

## Where the Rankin-shaped expression belongs

The iterated-log factor copied into the raw chronology is characteristic of lower bounds for **large gaps between consecutive primes**. Large prime gaps and long arithmetic progressions of primes are different extremal objects. A theorem making a gap unusually large does not manufacture many equally spaced primes.

Thus the raw close conflates:

- large gaps between consecutive primes;
- arithmetic progressions consisting of primes;
- arithmetic progressions in sets of prime patterns.

None may be substituted for another without a proved transfer theorem.

## Surviving local mathematics

The elementary residue restriction on a `k`-term prime arithmetic progression remains valid: apart from the endpoint possibility where a term itself equals a small prime `q`, sufficiently long progressions force small primes `q` to divide the common difference. That is structural infrastructure, not a lower bound of size `omega(log N)`.

## Verdict

**Reject the Pintz/Rankin negative close. Erdős #200 remains open at the canonical asymptotic scale.**

## Sources checked

- T. F. Bloom, maintained Erdős Problem #200 page: open; PNT gives the `(1+o(1))log N` upper bound.
- J. Pintz, *Patterns of primes in arithmetic progressions* (2015/2017): qualitative arbitrarily-long finite AP results for bounded prime patterns, not an `omega(log N)` lower bound for `L(N)`.
- Modern surveys of large prime gaps, where the Rankin-type iterated-log factor actually occurs.

## Operational lesson

Citation drift can preserve the correct mathematician, the correct subject (primes), and even the correct phrase (“arithmetic progressions”) while still changing the load-bearing quantitative object. Every citation-based close must be checked at the level of **exact dependent variable and quantifiers**, not topical similarity.

## License

Apache-2.0.
