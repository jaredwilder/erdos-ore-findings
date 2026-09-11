# Erdős 1061 — an infinite sigma solution family

Let `S(x)` count ordered pairs `(a,b)` with `a+b<=x` satisfying

`σ(a)+σ(b)=σ(a+b)`.

The historical corpus contains inconsistent small-value censuses. The theorem below is independent of those counts.

## Infinite family

For every positive integer `a` with `gcd(a,6)=1`,

`σ(a)+σ(2a)=σ(3a)`.

### Proof

Because `gcd(a,2)=gcd(a,3)=1`, multiplicativity gives

`σ(2a)=σ(2)σ(a)=3σ(a)`

and

`σ(3a)=σ(3)σ(a)=4σ(a)`.

Hence

`σ(a)+σ(2a)=4σ(a)=σ(3a)`.

Each such `a` therefore gives the ordered solutions `(a,2a)` and `(2a,a)`, both with sum `3a`.

## Counting consequence

Put `Y=floor(x/3)`. Then

`S(x) >= 2 * #{1<=a<=Y : gcd(a,6)=1}`.

Writing `Y=6q+r` with `0<=r<6`, the count of integers coprime to 6 is

`2q + 1_{r>=1} + 1_{r>=5}`.

In particular it is at least `Y/3 - 1/3`. Since `Y>=x/3-1`,

`S(x) >= 2x/9 - 4/3`.

Thus `S(x)` is bounded below by a positive linear function. In particular, `S(x)=o(x)` is impossible, and if an asymptotic `S(x)~cx` exists then necessarily `c>=2/9`.

The earlier release note used only complete six-term blocks and then attached an invalid numerical inequality to that coarser count. The exact residue count above fixes the arithmetic and gives the stronger constant term `-4/3`.

## A neighboring equation has no solutions

Write `a=2^k m` with `m` odd. Then

`σ(2a)-2σ(a)`

`=(2^(k+2)-1)σ(m)-2(2^(k+1)-1)σ(m)`

`=σ(m)>0`.

Therefore

`2σ(a)=σ(2a)`

has no positive-integer solution.

## Verification

The identity `σ(a)+σ(2a)=σ(3a)` was checked on all `a<4000` coprime to 6. The companion identity

`σ(2a)-2σ(a)=σ(odd part of a)`

was also checked on representative values; the proof above is exact and does not depend on those computations.

`sigma_family.py` contains the computational recheck.
