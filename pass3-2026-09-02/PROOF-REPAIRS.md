# Pass-3 Proof Repairs

Six places where the mathematics and the workflow disagreed. The rejected derivation is kept next
to the repaired status so later readers can audit the transition.

| problem | raw issue | repair | result | status |
| --- | --- | --- | --- | --- |
| 156 | Claim `[N] ⊆ A ∪ ((A+A)-A)` for maximal Sidon `A` omits the collision `2x=a+b`. | Every excluded `x` is blocked either by `x+a=b+c` or by `2x=a+b`. Count at most `m^3+m^2` blockers plus `A`. | `N<=m+m^3+m^2<=m+2m^3`; `m=Omega(N^(1/3))` survives. | REPAIRED_TRUE |
| 501 | Directed-row count incorrectly used `2*bad_pairs<=mN`. | Use `bad_pairs<=mN`; each bad pair contaminates at most `N-2` triples. | Under `6m<N-1`, `mN(N-2)<C(N,3)`; an independent triple exists. | REPAIRED_TRUE |
| 247 | A later route labelled a correct density equivalence false. | If `a_n/n` is unbounded, `A(a_n)/a_n=n/a_n ->0` along a subsequence. Conversely if `A(N_j)/N_j->0`, set `n_j=A(N_j)+1`; then `a_{n_j}>N_j` and `a_{n_j}/n_j->infty`. | Equivalence restored; registry `FALSE` is rejected. | TRUTH_OVERRIDES_LABEL |
| 1210 | Shifted-coprimality step is false. | No repair found in Pass 3. Counterexample: `n=5,A={1,3}`. | `C=1` upper claim remains unproved; only `C>=1` lower constraint survives. | UNREPAIRED |
| 317 | Asymptotic comparison `e^{-n} >> 2^{-n}` was reversed. | Correct comparison: `e^{-n}/2^{-n}=(2/e)^n->0`. | Purported negative close disappears; clause remains live. | FALSE_CLOSE_REMOVED |
| 539 | Diagonal term simplified as `a/gcd(a,a)=a`. | Correct simplification is `1`. | Corpus claim `h(n)=n` rejected; canonical problem is separately externally reported solved at a different asymptotic. | FALSE_CLOSE_REMOVED |

These are not housekeeping trivia. They are proof objects about the reliability boundary of the
estate itself: a source status may be stale or wrong, and a valid conclusion may survive a broken
proof only after a new proof is supplied.
