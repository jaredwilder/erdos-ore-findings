# Erdős 891: an explicit threshold, replicated six ways and attack-tested

The strongest positive result recovered from the Pass-6 delta. Unlike most of that corpus this is
a complete proof, it carries an explicit threshold rather than "sufficiently large", and it
survived the machine's own falsifier sweep.

---

## The statement

> For every `k ≥ 2` and every integer `n ≥ 2^k + 1`, the interval
> `[n, n + p₁p₂⋯p_k)` contains an integer `m` with `Ω(m) ≥ k + 1 > k`,
> where `Ω` counts prime factors with multiplicity.

`p₁p₂⋯p_k` is the k-th primorial, written `P_k` below.

## The proof, in full

Since `P_k ≥ 2^k`, every window of length `P_k` contains a multiple of `2^k`. Call it `m·2^k`.

If `n > 2^k`, that multiple cannot be `2^k` itself, so `m ≥ 2` and therefore

```
Ω(m · 2^k) = k + Ω(m) ≥ k + 1 > k
```

Two lines.

## Verified

`P_k ≥ 2^k` checked for k = 2..12:

| k | P_k | 2^k |
|---|---|---|
| 2 | 6 | 4 |
| 3 | 30 | 8 |
| 4 | 210 | 16 |
| 5 | 2,310 | 32 |
| 6 | 30,030 | 64 |
| 7 | 510,510 | 128 |
| 8 | 9,699,690 | 256 |

and the window argument spot-checked at `n = 2^k + 1` for each k: the multiple lands inside the
window every time, with `Ω` exceeding k every time.

## Why the threshold matters

The canonical question asks whether this holds for all *sufficiently large* n. This gives the
threshold explicitly:

```
n > P_k
```

That is strictly stronger than the statement being asked about, and it is checkable.

## What it does not settle, per the corpus itself

The argument is about **Ω**, which counts prime factors *with multiplicity*. The **ω** reading,
counting *distinct* primes, is untouched — `m·2^k` contributes only one distinct prime from the
`2^k` part.

The mining corpus keeps the two apart under an explicit contract trap flag, `OMEGA/OMEGA-CAPITAL`,
rather than letting the Ω result quietly stand in for the ω one. That discipline is why this find
is worth trusting: a system that conflated them would have reported a much bigger result and been
wrong.

## Replication, and an attack sweep

Independently restated in routes R004, R008, R010, R012, R013 and R014, plus a Lean fragment
certificate. `refs = 11–14, routes = 7–9, source kinds = 4`.

Route R012 ran the corpus's twelve-attack falsifier suite against it: *"all 12 attacks passed, no
circularity."*

**Replication alone would not persuade** — a companion finding in the same corpus documents a
constant replicated across nine routes and four source kinds that is simply false, and this
repository publishes that case alongside this one. What makes this result solid is that the proof
is two lines and re-derives from scratch, not that six routes agree about it.
