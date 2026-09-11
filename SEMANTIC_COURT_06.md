# Semantic Court 06 — false refutations, endpoint drift, and contradictory finite values

Author: Jared Wilder  
Public release: 2026-09-11

This packet records four Day-One chronology failures found while attacking the theorem vault. The common theme is important: a later `FALSE` or `PROVED` label can itself be wrong. Chronology is evidence, not authority.

## 1. Erdős #602 — the `K_4^3` refutation is false

A raw row says the complete 3-uniform hypergraph on four vertices, `K_4^3`, is not 2-colourable and claims all 16 colourings fail.

That is false. Colour two vertices red and two blue. Every 3-subset then contains vertices of both colours. Hence `K_4^3` is 2-colourable.

This matters because the false row was used to kill a finite hypergraph route. The independently reconstructed finite theorem survives after the correct edge-size hypothesis is stated: every finite hypergraph with all edges of size at least two and with no two distinct edges meeting in exactly one vertex is 2-colourable.

The directly relevant countable-index stratum of the canonical set-colouring problem also survives and is now released separately.

## 2. Erdős #681 — `n=250,k=3` is a witness, not a counterexample

A raw `FALSE` row claims `n=250,k=3` refutes the necessary fourth-root window.

In fact

`n+k = 253 = 11*23`,

so the least prime factor is `11`, and

`11 > 3^2 = 9`.

Thus `k=3` is a valid witness for the canonical condition. Moreover

`3^4 = 81 < 253 = n+k`,

exactly as the fourth-root necessity theorem predicts.

The row introduced the irrelevant comparison `11^4>253`. The theorem compares `k^4` with `n+k`, not the fourth power of the least prime factor.

## 3. Erdős #456 — the prime anchor has an endpoint exception

The theorem vault states

`m_(p-1)=p_(p-1)=p`

for every prime `p`.

The proof is correct for every **odd** prime. At `p=2`, however, the target index is `n=1`. Under the standard convention `phi(1)=1`, the least positive `m` satisfying `1 | phi(m)` is

`m_1=1`,

while the least prime congruent to `1 mod 1` is `p_1=2`.

So `p=2` is a genuine endpoint exception. The corrected odd-prime theorem has been released in the proved-lemmas bank.

## 4. Erdős #390 — contradictory exact values; `f(7)=20`

The raw chronology contains three incompatible values for the same extremal function:

- one row gives `f(7)=20`;
- a later row gives `f(7)=24`;
- another later row gives `f(7)=21`.

Exact recomputation settles the conflict:

`7! = 14*18*20`,

so `f(7)<=20`, and exhaustive search through all distinct divisors of `7!` greater than `7` shows that no factorization has largest factor below `20`.

Therefore

`f(7)=20`.

The same independent exhaustive search gives

`f(3..10) = 6,24,12,10,20,16,28,25`,

matching OEIS A193429 exactly. The rows claiming `24` and `21` are chronology corruption and must not be propagated.

## Operational rule extracted

Release adjudication must allow all four transitions:

- `PROVED -> false` when recomputation kills a claim;
- `FALSE -> true` when a purported refutation is itself wrong;
- `PROVED -> repaired theorem` when an endpoint or quantifier was dropped;
- conflicting finite values -> exact recomputation plus an external independent sequence/certificate check.

No terminal workflow label is allowed to outrank direct mathematics.

## License

Apache-2.0.
