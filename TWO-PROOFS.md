# Two complete proofs, neither of which needs a search

Both of these were sitting in the ore as computation-backed claims with thousands of verified
instances attached. Neither needs one. Each is a few lines.

---

## Erdős 1052 — no odd unitary perfect number exists

A *unitary divisor* `d | n` satisfies `gcd(d, n/d) = 1`; equivalently, for every prime power
`p^a ‖ n`, either `p^a | d` or `p ∤ d`. So

```
σ*(n) = ∏_{p^a ‖ n} (1 + p^a)
```

`n` is **unitary perfect** when `σ*(n) = 2n`.

### Proof

Let `n` be odd and unitary perfect.

Every prime factor `p` of `n` is odd, so every `p^a` is odd, so every factor `1 + p^a` is **even**.
There are `ω(n)` such factors, hence

```
2^{ω(n)}  |  σ*(n)  =  2n
```

But `n` is odd, so `v₂(2n) = 1`. Therefore `ω(n) ≤ 1`.

- `ω(n) = 0` gives `n = 1`, and `σ*(1) = 1 ≠ 2`.
- `ω(n) = 1` gives `n = p^a`, and `σ*(p^a) = 1 + p^a = 2p^a` forces `p^a = 1` — contradiction.

**No odd unitary perfect number exists.** ∎

No bound, no search, no computation. The corpus carried this as a sweep to `10⁷` reporting "zero
odd hits"; the sweep was never the reason.

### Checks

Every odd `n < 200000` has `σ*(n) ≠ 2n` — vacuously consistent with the proof. The even unitary
perfects below `10⁶` are the known `{6, 60, 90, 87360}`. And the load-bearing divisibility:

| n | ω(n) | σ*(n) | v₂(σ*(n)) |
|---|---|---|---|
| 3 | 1 | 4 | 2 |
| 9 | 1 | 10 | 1 |
| 15 | 2 | 24 | 3 |
| 105 | 3 | 192 | 6 |
| 1155 | 4 | 2304 | 8 |
| 45045 | 5 | 80640 | 8 |

`v₂(σ*(n)) ≥ ω(n)` in every case, which is the whole argument.

---

## Erdős 891 — Ω > k in every primorial window

Write `P_k = p₁p₂⋯p_k` for the k-th primorial and `Ω` for the number of prime factors counted
with multiplicity.

> **For every `k ≥ 2` and every `n > 2^k`, the interval `[n, n + P_k)` contains an integer `m`
> with `Ω(m) ≥ k + 1 > k`.**

### Proof

`P_k = 2·3·5⋯p_k ≥ 2^k`, since each of the `k` factors is at least 2.

A window of length `P_k ≥ 2^k` therefore contains a multiple of `2^k`. Write it `m = t·2^k`.

Since `m ≥ n > 2^k`, we get `t ≥ 2`, so `Ω(t) ≥ 1`, and

```
Ω(m) = k + Ω(t) ≥ k + 1 > k     ∎
```

Two lines, with an **explicit threshold** `n > 2^k` rather than "sufficiently large."

### The threshold is not sharp

Direct computation gives the true exceptional sets:

| k | P_k | trivial threshold `2^k + 1` | actual exceptions |
|---|---|---|---|
| 2 | 6 | 5 | **{1, 2}** |
| 3 | 30 | 9 | **none** |
| 4 | 210 | 17 | **none** |

So for `k = 2` the statement holds from `n = 3` onward, and for `k ≥ 3` it holds for every `n ≥ 1`.

### Scope — this is the Ω reading, and it does not transfer to ω

`Ω` counts prime factors **with multiplicity**. The `ω` reading — *distinct* primes — does not
follow, and the proof shows exactly why: when `t` is itself a power of 2, `m = t·2^k` is a power
of 2 and `ω(m) = 1`.

This is not a technicality. For `k = 2`, the integers `n` below 200 for which **no** `m` in
`[n, n+6)` has `ω(m) ≥ 3` are

```
1–24, 31–36, 43–54, 71, 72, 91–96, 141–144, 157–159
```

The Ω statement holds from n = 3; the ω statement is still failing at n = 159. They are different
problems, and only the first is closed here.

---

## Reproduce

`two_proofs.py` asserts every claim above, including the exceptional sets and the ω failure list.
Exits 0.
