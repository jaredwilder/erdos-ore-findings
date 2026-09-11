# Semantic Court 12 — Erdős #68 factorial-minus-one coprimality claim is false

Author: Jared Wilder  
Court date: 2026-09-11

## Verdict

The Pass-6 statement

`gcd(n!-1,m!-1)=1 for every 2<=n<m`

is **FALSE**.

The smallest simple counterexample is

`n=4, m=8`.

Indeed,

`4!-1 = 23`,

while

`8!-1 = 40319 = 23*1753`.

Therefore

`gcd(4!-1,8!-1)=23`.

## Why the recorded proof fails

The source argument observes correctly that if a prime `p` divides `n!-1`, then `p>n`.

But this does **not** imply that `p` cannot also divide `m!-1` for some later `m>n`. A prime larger than `n` may also be larger than `m`, or may interact with the intervening factorial ratio so that `m!≡1 (mod p)` again.

The implication

`p|n!-1 and p>n  =>  p∤m!-1 for all m>n`

is simply invalid.

## Exact repair

For every `2<=n<m`, let

`P_(n,m)=prod_{j=n+1}^m j`.

Then

`m! = n! P_(n,m)`.

Modulo `n!-1` one has `n!≡1`, so

`m!-1 ≡ P_(n,m)-1 (mod n!-1)`.

Hence the exact identity

`gcd(n!-1,m!-1) = gcd(n!-1, P_(n,m)-1)`.

This is the correct reduction.

For `(n,m)=(4,8)`,

`P_(4,8)=5*6*7*8=1680`,

so

`P_(4,8)-1=1679=23*73`,

recovering the common factor 23.

## Additional small counterexamples

Exact computation also finds, among small pairs,

- `(4,11)` with common factor `23`;
- `(5,11)` with common factor `17`;
- `(5,15)` with common factor `17`;
- `(8,11)` with common factor `23`;
- `(11,15)` with common factor `17`.

These show the failure is structural rather than a one-off arithmetic accident.

## Release consequence

The geometric-series reformulation for Erdős #68 remains valid and is unaffected.

The factorial-minus-one pairwise-coprimality lemma must be removed from the survivor set and replaced by the exact gcd reduction above.

This is a status correction, not a claim about the unresolved parent irrationality problem.