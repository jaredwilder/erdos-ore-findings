# Day-One forensic corrections — false late claims that must not re-enter the live mathematics

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Purpose:** truth-over-label quarantine for the uploaded Day-One archive.

The archive contains excellent mathematics, but it also contains statements labelled `PROVED` late in problem chronologies that fail direct arithmetic or elementary checking. This file records several high-risk cases so they cannot silently return as live claims.

---

## 1. Erdős 885 — the claimed explicit canonical close is false

A late chronology row claims:

> `N_i = i*lcm(1..2k)` gives `{0,...,k-1} subset intersection D(N_i)`.

This already fails at `k=2`.

Here

`L=lcm(1,2,3,4)=12`,

so the proposed numbers are `N_1=12`, `N_2=24`.

By definition

`D(n)={|a-b|:ab=n}`.

The factor pairs of `12` give

`D(12)={11,4,1}`.

The factor pairs of `24` give

`D(24)={23,10,5,2}`.

Hence

`D(12) intersect D(24)=empty`.

So the proposed family does not merely fail to prove the general statement; it fails at the first nontrivial test case. The late `PROVED` close is quarantined.

---

## 2. Erdős 1073 — the prime-power Wilson close is false

A chronology row claims that a Wilson-type argument for odd prime powers yields enough counted values to force

`A(x) >= pi(sqrt(x))`,

thereby refuting the proposed `x^{o(1)}` upper bound.

The claimed automatic prime-power family is false.

Take `p=3`, `u=9`. If `9 | n!+1`, every prime divisor of `9` must exceed `n`, so necessarily `n<3`. But

`1!+1=2`,

`2!+1=3`,

and neither is divisible by `9`.

Thus `9` is not counted. Equivalently, the naive extension of Wilson's theorem from primes to all odd prime powers is invalid here. In fact, divisibility such as `p^2 | (p-1)!+1` is exceptional rather than automatic.

The same problem card later returns to the correct position: the known elementary constraint gives roughly an `x^{1/2+o(1)}`-type upper regime, not a branch-B close. The prime-power close is quarantined.

---

## 3. Erdős 243 — the advertised `+2` recurrence counterexample does not have sum 1

A chronology row claims that

`a_1=2`,

`a_{n+1}=a_n^2-a_n+2`

has reciprocal sum exactly `1`, thereby refuting the canonical statement.

The first terms are

`2, 4, 14, 184, 33674, 1133904604, ...`.

The first four reciprocals sum exactly to

`1/2+1/4+1/14+1/184 = 1065/1288`.

From `x>=2`, the recurrence satisfies

`x^2-x+2 >= 2x`,

so starting at `33674` the remaining denominators at least double each step. Therefore the entire tail from `33674` onward is less than

`2/33674 = 1/16837`.

Hence the total reciprocal sum is strictly less than

`1065/1288 + 1/16837 < 1`.

So this sequence is **not** the claimed rational-sum-1 counterexample. The `FALSE` canonical conclusion derived from it is unsupported.

---

## 4. Erdős 400 — the `a_i=n` universal extremizer claim is false

A late chronology row asserts that for every `k>=2` and every `n`, taking

`a_1=...=a_k=n`

is admissible because `(n!)^k | n!`, and concludes `g_k(n)=(k-1)n`.

The divisibility assertion is false as soon as `n!>1` and `k>1`. For example,

`n=2`, `k=2` gives

`(2!)^2=4`,

which does not divide `2!=2`.

Therefore the claimed exact linear formula and the derived asymptotic refutation do not follow.

By contrast, the distinct factorial witness promoted in `GOLD_RUSH_03.md`,

`(m!-1,m,1,...,1)` at `n=m!`,

is valid because `(m!-1)! m! = (m!)!` exactly.

---

## 5. Erdős 700 — a false refutation of a true known semiprime theorem

The archive later claims that `n=21` refutes the semiprime formula by asserting an incorrect gcd at `k=7`.

In fact

`C(21,7)=116280`

and

`gcd(21,116280)=3`.

Thus the proposed counterexample fails. The semiprime formula is a known public baseline and is re-proved in `GOLD_RUSH_03.md`.

This is an especially useful regression case because the correct theorem appears earlier in the same chronology and is then falsely marked dead later. A latest-label policy would get the mathematics wrong.

---

## Operational rule extracted from Day One

Never promote by any of the following alone:

- latest registry status;
- `PROVED` label;
- audit rank;
- `KERNEL_CHECKED` wrapper status;
- a later chronology entry overriding an earlier one.

Promotion requires literal statement reconstruction plus independent mathematical replay. When chronology conflicts, arithmetic and proof win.
