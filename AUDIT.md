# How an automated pipeline produced clean-looking proofs of nothing

An audit of a 30,438-object ore ledger and its 664 Lean declarations, with every arithmetic
claim re-derived independently. The mechanism that made failed proofs report perfect axiom
footprints is identified exactly. Seven claims marked `PROVED` are false. A further eight carry
flawless kernel receipts and prove nothing at all.

Author: Jared Wilder. 2026-09-11. Ranges audited: Erdős 1–300 and 301–700.

---

# Part 1 — the bug

## A doubled keyword

Several generated files contain a declaration of this shape:

```lean
theorem msl_fmz_erdos241_campaign_001_R004_L1 : theorem Erdos241Closer.counting_bound ...
```

`theorem X : theorem Y ...` does not parse. Lean reports
`unexpected token 'theorem'; expected term`, and the declaration never becomes a type.

**`#print axioms` on a declaration that never elaborated returns nothing.**

An empty axiom list is normally the strongest possible clean signal — it means the proof used
neither choice nor propositional extensionality nor anything else. Here it means the opposite.
The landing pass recorded `axioms: []` as a maximally clean footprint, and a summary table then
flattened `status: VERIFIED_PARTIAL` into `VERIFIED` and dropped the `errors` array.

> **`axioms: []` is only meaningful alongside `exitCode: 0`. On a theorem that imports Mathlib,
> an empty axiom list beside a non-zero exit code is a failure signature, not a clean
> footprint.**

## The extent, measured

- `grep -l ": *theorem "` over the kernel-verified corpus hits **exactly 12 files**.
- `grep -l "^axiom "` hits **exactly 5 files** — every one is a `lap_fmz_*` file, and **every
  one of those five also carries the doubled header.** The two defects travel together.
- `grep -l "sorry"` over the whole corpus returns **nothing**. Every `sorryAx` in every footprint
  is Lean's error-recovery marker for a broken proof, not a placeholder anybody typed.
- Across 664 declarations, **54 rows marked `VERIFIED` carry `exitCode` ≠ 0**.
- **Of 635 `attached` paths on `PROVED` objects in 301–700, zero resolve on disk.** They point at
  per-node files that were never written. The `attached` field is not evidence of anything.

One of the affected receipts carries its own warning in its header: *"Never cite this file as a
whole."*

## The worst single case: assuming the conclusion

A file on Erdős 101 contains, in full:

```lean
axiom MelchiorGreenTao_OrdinaryLineBounds :
  ∀ (C : PtConfig), C.n ≥ 3 → tK C 5 = 0 → tK C 4 ≤ tK C 2 ∧ C.n / 2 ≤ tK C 2

theorem msl_fmz_erdos101_campaign_001_R001_L1 : theorem t4_sublinear ...
  := exact MelchiorGreenTao_OrdinaryLineBounds C h3 h5
```

The theorem is a verbatim restatement of an axiom declared six lines above it. Separately, the
definition `tK` it depends on reports `[propext, sorryAx, Quot.sound]`.

The ore object built from this reads *"Melchior + Green–Tao … closing branch A."* **Eight other
`PROVED` objects on the same problem** each say the available bound contains no o(n²) mechanism
and cannot close branch A. The ledger contains both.

## The most instructive case: a headline clean over nine broken lemmas

On Erdős 218, the headline declaration reports `axioms: []`. In the same file,
`densityLE`, `densityGE`, `ratioLE`, `ratioGE`, `key`, `cntLE_eq`, `cntLE_succ`, `cntGE_eq` and
`cntGE_succ` **all carry `sorryAx`**, and the receipt lists all nine as unclean. `exitCode: 1`,
13 errors.

A `PROVED` object whose entire proof machinery is sorried, reporting a perfect footprint.

---

# Part 2 — eight perfect receipts that prove nothing

These carry `VERIFIED`, `exitCode: 0`, empty or standard axioms. **The receipts are honest. The
statements are empty.**

| problem | what the kernel actually verified |
|---|---|
| **218** | `L1Holds = true`, where the supplied fields are the literal strings `["none", "none", "per contract"]` and `IsPlaceholder s := s = "none" \|\| s = "per contract"`. **A kernel-clean theorem about three strings.** The file's own docstring says it: *"no verifiable mathematical claim is machine-extractable from the packet payload."* |
| **172** | `check_L1 = true`, which unfolds to `[] = [] && certifiable [] = false` |
| **234** | `checkL1 = true` with `pAt1 := -1` and `pAtM1 := 3` hardcoded — it proves −1 ≠ 0 and 3 ≠ 0. The polynomial the Rational Root Theorem is supposedly applied to **appears nowhere in the file** |
| **291** | `check = true` for `2*6 + 1*6 - 3*6 == 0`, i.e. 12 + 6 − 18 = 0 |
| **260** | the squares 0, 1, 4, …, 196 are strictly increasing and start at 0 |
| **91** | Gauss's formula Σk = n(n+1)/2, re-verified for n ≤ 40 |
| **101** | `n(n−1)/12 ≤ n²` for n < 100 |
| **1** | `∀ n : ℕ, (decide (n = n) : Bool) = true` |

**This is the load-bearing lesson of the whole audit.** The exit-0 tier splits in two. Some
`check = true` wrappers unfold to a real explicit mathematical object. Others unfold to a
tautology or a string comparison. **At the `VERIFIED` level the two are indistinguishable.** The
only way to tell them apart is to open the `.lean` and read what `check` is *defined to be*.

---

# Part 3 — seven `PROVED` claims that are false

Each was recomputed from scratch.

### 1. Three objects claim a hypothesis class is empty. It isn't.

Three `PROVED` lemmas on Erdős 124 assert that `Σ 1/(d_r − 1) ≥ 1` is unsatisfiable for strictly
increasing integers ≥ 3, making the statement vacuously true. A fourth `PROVED` object refutes
them with the triple **(3, 4, 5)**:

```
1/2 + 1/3 + 1/4 = 13/12 ≥ 1        strictly increasing, every d_r ≥ r+2
```

Confirmed exactly. **The fourth object is right and the other three are wrong.** The machine
caught itself; nothing retracted the three.

### 2. A fabricated factorization that refutes its own point

An object on Erdős 376, offered as evidence of coprimality with 105:

```
claimed:  C(20,10) = 184756 = 2^2 * 7 * 11 * 13 * 23
but:      2^2 * 7 * 11 * 13 * 23 = 92092        <- a different number
true:     C(20,10) = 2^2 * 11 * 13 * 17 * 19
```

The stated factorization **contains a factor of 7, and 7 divides 105.** It contradicts the exact
property it was cited to demonstrate. (The underlying biconditional is sound — checked to
n = 20,000.)

### 3. A closed form that fails at every even N

Erdős 486: *"exact closed form R(N) = (N+3)/(2N) … for all N ≥ 2"*.

| N | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| true | 1 | 1 | 3/4 | 4/5 | 2/3 | 5/7 | 5/8 |
| claimed | 5/4 | 1 | 7/8 | 4/5 | 3/4 | 5/7 | 11/16 |
| | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ |

Correct at odd N, wrong at every even N, where the true value is (N+2)/(2N). The limit 1/2
survives; the advertised exact closed form does not.

### 4. An extremizer set the machine itself refuted

Two Erdős 454 objects give different sets. Recomputing d(n) = f(n) − 2p_n over n = 2..20 settles
it: **d(7) = −2**, so 7 does not belong, and the maximum is attained exactly on
**{4, 8, 9, 14, 15}**. The later object says so explicitly and names d(7) = −2. The earlier one
is wrong and was never retracted. Both are `PROVED`.

Neither notices that the bound they share, −6 ≤ d ≤ +2, is **true but not tight** — the real
minimum is −4.

### 5. A vacuous survivor

An Erdős 383 declaration has two rows: one `VERIFIED, exit 0`, one `FAILED, exit 1` whose error
is *"Tactic `decide` proved that the proposition"* — Lean's message when `decide` proves the
**negation**. The falsified file is gone. The survivor reduces to asserting that p is the largest
prime factor of p², trivially true for every prime, and is presented as certifying the problem's
condition.

### 6. An overreaching pair claim

Erdős 288: one object says the only integral pair is **(1,1)**; another says **{(1,1), (2,2)}**.
Enumerated: the integral pairs are exactly **{(1,1), (2,2)}**. The first object overreaches past
its own hypothesis.

### 7. A witness that does not sum to 1

An Erdős 295 object claims `k₀(4) = 6` and then lists a **seven**-element witness
{4, 5, 6, 7, 8, 9, 230}, whose reciprocals sum to **57959/57960 ≠ 1**. A second object on the
same problem lists the pair products of {3,4,5,6,20} including **144**, which is not a product of
any two, and omitting **100 = 5·20**, which is.

### Four constants for one bound

Erdős 241 carries `(18N)^{1/3}`, `(6N)^{1/3}` and `(9N)^{1/3}` in three separate `PROVED`
objects, plus `A.card³ ≤ 27(3N+1)` in the Lean file — a fourth constant, and the weakest of the
four.

---

# Part 4 — what held up

Re-derived from scratch and correct.

**Erdős 295 — k(3) = 5, closed with both halves.** Upper by the explicit witness
`1/3 + 1/4 + 1/5 + 1/6 + 1/20 = 1`; lower because `1/3 + 1/4 + 1/5 + 1/6 = 19/20 < 1` bounds every
strictly increasing 4-tuple ≥ 3. Clean receipt, exit 0, and the statement *is* the mathematics
rather than a `check = true` wrapper. The strongest object in the corpus.

**Erdős 213 — an integral 4-point kite.** `{(0,0), (100,0), (72,96), (72,−96)}`. All six pairwise
distances integral: 100, 120, 120, 100, 100, 192. No three collinear, not concyclic. Checkable by
hand in thirty seconds, and it carries **no Lean at all**.

**Erdős 197 — W(2,3) > 8.** The 2-colouring `[1,4,5,8] | [2,3,6,7]`, both classes 3-AP-free,
union exactly [1,8]. Kernel-certified, clean.

**Erdős 3 — r₃(5) = 4** by exhaustive enumeration over all 32 subsets, witness {1,2,4,5}.

**Erdős 247 — √2 < 141/99** via the integer certificate 141² = 19881 > 19602 = 2·99².

**Erdős 383 — exactly {7, 41, 43, 47}** among primes p ≤ 47 with p²+1 p-smooth:
50 = 2·5², 1682 = 2·29², 1850 = 2·5²·37, 2210 = 2·5·13·17. Carries no Lean, while the file that
*is* Lean-verified for that problem proves something unrelated.

**Erdős 689** — 25 primes ≤ 100 and `Σ ⌈100/p⌉ = 194 < 200`, so the necessary condition **fails**
at n = 100.

**Erdős 700** — `gcd(pq, C(pq,q)) = p` with a matching lower bound, together pinning
f(pq) = min(p,q). A real Mathlib proof via Lucas.

Also confirmed: Erdős 394 (t₂(p) = p−1 for all odd p < 100), Erdős 535 (f₃ = 2,2,3,3,3,3,4),
Erdős 489 (period-6 gap cycle [4,2], density 10/3), Erdős 153 (Sidon Cauchy–Schwarz certificate,
Q = 30, 300 ≥ 196), Erdős 168 (a kernel-clean refutation of a monotonicity claim), Erdős 454
(f = 7,10,16,20,26,32,40,48,54,62,70).

---

# Part 5 — the shape of the corpus

30,438 objects: **27,847 STATED, 2,260 PROVED, 278 COMPUTED, 53 REFUTED.**

One problem, Erdős 170, owns **391 PROVED, all 278 COMPUTED and all 53 REFUTED.** Outside it,
across both audited ranges, there is **not a single COMPUTED or REFUTED object.** The corpus is
PROVED-or-nothing everywhere else — and several of its `PROVED` rows refute each other.

## How to read any object in this corpus

1. Ignore the summary `VERIFIED` column. Open the `.verify.json` and read `status`, `exitCode`
   and `errors`.
2. Treat `axioms: []` as meaningless unless `exitCode` is 0.
3. Ignore `attached`. It resolves nowhere.
4. **Even at exit 0, open the `.lean` and read what `check` is defined to be.** Eight perfect
   receipts in this corpus certify tautologies.
5. Treat every prose `PROVED` object as a lead and recompute it. Seven were false here, and
   three of those were contradicted by another object on the same problem.
