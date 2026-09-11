# Semantic audit 07 — interval-length errors in Erdős #394

Author: Jared Wilder. Public release: 2026-09-11.

This audit corrects two historical `FALSE` labels in the Erdős #394 chronology. Both errors come from elementary interval bookkeeping.

Let `t_k(n)` be the least positive integer `m` such that

`n | m(m+1)...(m+k-1)`.

## 1. `t_2(4)=3`

One historical row rejects `t_2(4)=3` because `4|2*3*4=24`, treating that as evidence that `t_2(4)<=2`.

But `t_2` uses exactly **two** consecutive factors. At `m=2`, the relevant product is

`2*3=6`,

which is not divisible by 4. At `m=3`,

`3*4=12`,

which is divisible by 4. Therefore

`t_2(4)=3`.

The attempted refutation changed a length-2 product into a length-3 product.

## 2. `t_2(2)=1` agrees with the prime formula

Another historical `FALSE` row claims that

`t_2(p)=p-1`

fails at the prime `p=2` because `t_2(2)=1`.

But `p-1=1` at `p=2`. The endpoint agrees exactly with the formula.

## 3. General prime-window theorem

For every prime `p>k`,

`t_k(p)=p-k+1`.

Before `m=p-k+1`, the whole length-`k` interval lies in `{1,...,p-1}` and therefore contains no multiple of `p`. At `m=p-k+1`, the interval ends at `p`.

The theorem has its own writeup in `jaredwilder/erdos-proved-lemmas/erdos394-prime-window.md`.

## Correction principle

A concrete refutation is only as good as the definition it computes. Here, one row used the wrong interval length and another failed to evaluate its own comparison formula at the endpoint.

Direct recomputation restores the two finite facts and leaves the general prime-window theorem intact.

## License

Apache-2.0.
