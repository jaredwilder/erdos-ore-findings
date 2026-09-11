# Semantic Court 07 — interval-length mistakes can generate false refutations

Author: Jared Wilder  
Public release: 2026-09-11

This packet records two false `FALSE` events found in the Erdős #394 chronology. Both arise from elementary interval-length bookkeeping.

Let `t_k(n)` be the least positive `m` such that

`n | m(m+1)...(m+k-1)`.

## 1. `t_2(4)=3` is correct

A later raw row claims `t_2(4)=3` is false because `4 | 2*3*4=24`, allegedly showing `t_2(4)<=2`.

But `t_2` uses exactly **two** consecutive factors. At `m=2` the relevant product is

`2*3=6`,

which is not divisible by 4.

At `m=3`,

`3*4=12`,

which is divisible by 4. Therefore

` t_2(4)=3 `.

The supposed refutation silently changed a length-2 product into a length-3 product.

## 2. `t_2(2)=1` supports, rather than refutes, the prime formula

Another raw `FALSE` row says the identity

`t_2(p)=p-1`

cannot hold for all primes because `t_2(2)=1`.

But for `p=2`,

`p-1=1`.

So `t_2(2)=1` is exact agreement with the formula, not a counterexample.

## 3. Surviving general theorem

The chronology's prime mechanism actually extends cleanly: for every prime `p>k`,

` t_k(p)=p-k+1 `.

Before `m=p-k+1`, the length-`k` interval lies entirely below `p`; at `m=p-k+1` it ends at `p`.

That theorem is released separately in the canonical proved-lemmas bank.

## Operational lesson

Small-index semantics need the same court treatment as sophisticated asymptotics. A single off-by-one change in the number of factors can create a perfectly explicit but completely false refutation; a numerically correct endpoint can be mislabelled as a counterexample simply because the comparison value was not evaluated.

Direct recomputation outranks the chronology label.

## License

Apache-2.0.
