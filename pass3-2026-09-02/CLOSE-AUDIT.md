# Pass-3 Close Audit — 20 close-shaped claims adjudicated

This is the anti-hype ledger. A close-shaped source label is not a close until the exact statement,
semantics, proof, and scope survive review.

| id | problem | close-shaped claim | verdict | decisive reason | current interpretation | severity |
| --- | --- | --- | --- | --- | --- | --- |
| C001 | 539 | `h(n)=n` for every n, via diagonal `a/gcd(a,a)=a` | FALSE_CLOSE | `a/gcd(a,a)=1`, not `a`; the claimed lower bound dies immediately. | Corpus close rejected. Canonical #539 is separately externally reported solved with `h(n)=n^(1/2+o(1))`; do not inherit the corpus claim. | HIGH |
| C002 | 943 | Earlier branch/canonical `PROVED` row | STALE_PROVED_NOT_CLOSE | Later target ledger keeps Branch A active; derivation status unknown and a related divisor-count route is internally refuted. | No close established. | HIGH |
| C003 | 1203 | `F(n)<=2` / `O(1)` negative close | RETRACTED/FALSE_CLOSE | Later campaign state refutes the uniform bound; surviving witness has `F(510495)>2.575`. | Target remains active. | HIGH |
| C004 | 1210 | Uniform constant `C=1` because shifted numbers remain pairwise coprime | FALSE_PROOF | Counterexample `n=5, A={1,3}`: original gcd is 1 but shifted values 4 and 2 have gcd 2. | `C>=1` survives; `C=1` upper theorem is unproved. | HIGH |
| C005 | 317 | Small signed harmonic sums impossible because `1/lcm(1..n) >> c/2^n` | FALSE_ASYMPTOTIC_DIRECTION | `1/lcm(1..n)` is about `e^{-n}`, asymptotically *smaller* than `2^{-n}`; ratio `(2/e)^n -> 0`. | Grid lower bound does not kill the uniform-c question. | HIGH |
| C006 | 200 | Erdős–Rankin prime gaps give a negative close | WRONG_QUANTITY | Canonical problem concerns long arithmetic progressions of primes, not composite intervals / prime gaps. | No implication to target. | HIGH |
| C007 | 1056 | Singleton intervals trivially close the problem | SEMANTIC_TARGET_MISMATCH | Target requires a structured sequence of consecutive intervals; arbitrary separated singletons do not instantiate it. | No close established. | HIGH |
| C008 | 1073 | Wilson yields odd prime powers and infinitely many relevant divisors | FALSE_WILSON_EXTENSION | Wilson is modulo `p`; for `p^2`, `(p^2-1)!` is generally divisible by `p^2`, so `+1` is not 0 mod `p^2`. | Canonical problem open; only the prime-factor restriction survives. | HIGH |
| C009 | 891 | Kernel theorem on `>k` prime factors closes canonical target | SEMANTIC_MISMATCH | Formal theorem counts prime factors with multiplicity (`Omega`); target needs distinct factors (`omega`). | Correct formal theorem, wrong target. | HIGH |
| C010 | 655 | Regular polygons refute the literal universal lower bound | REAL_LITERAL_NEGATIVE_CLOSE / KNOWN | Regular n-gons satisfy the frozen premise and have exactly `floor(n/2)` distances. | Real literal close, but known; intended formulation may carry extra general-position intent. | MEDIUM |
| C011 | 683 | Branch marked closed | FINITE_CONTRACT_ONLY | Closure applies to a bounded verified exponent family; global `c*` extrapolation is still open debt. | Useful finite certificate, not canonical close. | HIGH |
| C012 | 145 | `alpha=0,1` closed | KNOWN_SMALL_PARAMETER_SLICE | Current public results extend beyond these values. | True slice, low novelty. | LOW |
| C013 | 193 | dimension `<=1` / dimension 2 closure | KNOWN_DIMENSIONAL_SLICE | Public literature already handles low-dimensional cases. | True infrastructure, not new close. | LOW |
| C014 | 241 | lower asymptotic half closed | KNOWN_CLASSICAL_HALF | Bose–Chowla-type lower construction is known; upper side contains the hard residual. | True but not new. | LOW |
| C015 | 383 | `k=0` branch | TRIVIAL_PARAMETER_CASE | Only a trivial/special parameter slice is closed. | No general close. | LOW |
| C016 | 479 | `k=0,2,-1` slices | KNOWN_PARAMETER_SLICES | Current public record contains these and stronger families. | True but not new. | LOW |
| C017 | 156 | Raw maximal-Sidon proof | CONCLUSION_SURVIVES_AFTER_REPAIR | Raw inclusion omitted `2x=a+b`; corrected blocker dichotomy restores the `N^(1/3)` bound. | Theorem retained, proof replaced. | HIGH |
| C018 | 501 | Raw finite independent-triple count | CONCLUSION_SURVIVES_AFTER_REPAIR | Raw `2*bad_pairs<=mN` need not hold; `bad_pairs<=mN` suffices under `6m<N-1`. | Finite theorem retained, proof replaced. | HIGH |
| C019 | 247 | Later `FALSE` registry label on density equivalence | FALSE_REFUTATION_LABEL | Direct inverse-counting proof establishes the equivalence. | The theorem is true despite workflow label history. | HIGH |
| C020 | C(13,6,3) | 21-block witnesses imply optimality | NOT_A_CLOSE | Witnesses prove only `C<=21`; public lower bound 20 leaves one-block gap. | Extremely actionable near-close, not closed. | HIGH |

The purpose of publishing this beside the positive ledger is simple: the corpus contains both real
mathematics and persuasive-looking failure modes. Release means preserving both.
