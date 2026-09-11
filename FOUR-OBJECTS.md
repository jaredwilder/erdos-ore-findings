# Four explicit objects, and one pattern that isn't one

Small, checkable, and each settles something. Every claim here was recomputed.

---

## Erdős 137 — three consecutive powerful numbers in arithmetic progression

A **powerful** number has `p | n ⟹ p² | n`. Consecutive here means consecutive *in the sequence of
powerful numbers* — nothing powerful lies between them.

```
1728 = 2⁶·3³
1764 = 2²·3²·7²
1800 = 2³·3²·5²
```

All three powerful. Differences **36 and 36** — an arithmetic progression. And exhaustively, there
is **no powerful number strictly between 1728 and 1764, nor between 1764 and 1800**. So these are
three consecutive terms of the powerful sequence that happen to form an AP.

### The related bound

Runs of consecutive *integers* all powerful are much shorter. Below `10⁶` the pairs start at

```
8, 288, 675, 9800, 12167, 235224, 332928, 465124
```

and the **longest run of consecutive integers all powerful is 2**. (A run of 3 would settle a
known open problem; none exists in this range.)

---

## Erdős 1107 — the gaps below 100, and why "≡ 7 mod 8" is not the obstruction

Which integers are **not** a sum of at most three powerful numbers? Below 100, exactly:

```
7,  15,  23,  87
```

All four are `≡ 7 (mod 8)`, which is what suggested the pattern. But the converse fails:

```
31 ≡ 7 (mod 8),   yet   31 = 4 + 27 = 2² + 3³
```

both summands powerful. So `n ≡ 7 (mod 8)` is **not** an obstruction class — the corpus records it
as one, which would make the exceptional set infinite. The four gaps satisfy the congruence; the
congruence does not produce gaps.

`87` is the interesting one: it needs the full powerful basis below it
`{1,4,8,9,16,25,27,32,36,49,64,72,81}` checked over all triples before it can be declared a gap,
which is why shorter searches stop at `{7,15,23}`.

---

## Erdős 949 — q ≤ 5 always works, and 5 is sharp

For a sum-free set `S`, one asks for a `q` with **both** `q ∉ S` and `2q ∉ S`.

**The bound `q ≤ 5` cannot be improved to `q ≤ 4`,** witnessed by `S = {1,4,6}`:

| q | q ∈ S? | 2q | 2q ∈ S? | |
|---|---|---|---|---|
| 1 | yes | 2 | no | blocked |
| 2 | no | 4 | **yes** | blocked |
| 3 | no | 6 | **yes** | blocked |
| 4 | **yes** | 8 | no | blocked |
| 5 | no | 10 | no | **free** |

`S` is sum-free — its pairwise sums are `{2,5,7,8,10,12}`, disjoint from `S`. Every `q ≤ 4` is
blocked, and `q = 5` is the first that works.

**And `q ≤ 5` is always enough:** over *every* sum-free subset of `[1,10]` — all of them, by
exhaustive search — there is no set for which all of `q = 1..5` are blocked.

---

## Erdős 913 — a distinct-exponent witness, and a Pell object that is something else

The question concerns `n` for which the exponents in the factorization of `n(n+1)` are pairwise
distinct.

**A clean witness well beyond hand search:**

```
57121 = 239²           exponents {2}
57122 = 2 · 13⁴        exponents {1, 4}
                       multiset {2, 1, 4} — pairwise distinct ✓
```

The smallest witnesses are `1, 3, 4, 7, 8, 16, 24, 27, 31, 48, 63, 71, 72, …`, and there are
**140 below 10⁵**.

### A correction worth stating

The corpus offers `n = 8119² = 65,918,161` as a witness here, noting the elegant negative-Pell
identity

```
8119² − 2·5741² = −1     so   65,918,161  and  65,918,162 = 2·5741²  are consecutive
```

**That identity is exactly right, but the number is not a distinct-exponent witness.** Its
factorizations are

```
65,918,161 = 23² · 353²        exponents {2, 2}
65,918,162 = 2 · 5741²         exponents {1, 2}
```

giving the multiset `{2,2,1,2}` — three exponents equal to 2. What the object *does* witness is a
different property: both `n` and `n+1` have two distinct prime factors while `n(n+1)` has
**exactly one** exponent equal to 1. That is a genuine and hard-to-reach example; it just answers
a different question than the one it is filed under.

---

## Reproduce

`four_objects.py` asserts all of it — powerfulness and the gap-free intervals for 137, the
exhaustive triple search for 1107 including the 31 counterexample, the full sum-free sweep of
`[1,10]` for 949, and both factorizations plus the Pell identity for 913. Exits 0.
