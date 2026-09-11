# Erdős #1093 — independent exact frontier through `k <= 65`

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Artifact:** `verify_erdos1093_frontier65.py`

## Result

The public divisor-window engine previously recorded all deficiency `>1` examples through `k<=45`.
The engine has now been independently reconstructed from the mathematical statement and extended.

The reconstruction first reproduces **exactly** the maintained deficiency `>1` list through `k=45`:

```text
k=8:   (44,2)
k=10:  (46,3), (47,3), (74,2)
k=11:  (47,4)
k=12:  (174,2)
k=14:  (239,2)
k=16:  (241,3)
k=25:  (2105,3)
k=27:  (1119,3), (5179,2)
k=28:  (284,9), (8413,2), (8414,2)
k=33:  (6459,3)
k=42:  (96622,2)
```

with no additional `k<=45` examples.

It then finds

```text
NO deficiency > 1 examples for 46 <= k <= 65.
```

Thus the independently reproduced finite no-new-example frontier is extended from `k<=45` to

```text
k <= 65.
```

This is a finite exact computational result. It does **not** resolve either infinite question in Erdős #1093.

## Canonical semantics

For `n>=2k`, the deficiency of `C(n,k)` is undefined if some prime `p<=k` divides `C(n,k)`.
Otherwise the deficiency is the number of `0<=i<k` for which `n-i` is `k`-smooth.

For admissible `(n,k)`, the divisor-window theorem gives

```text
delta(n,k) = #{ d | L_k : n-k < d <= n },
L_k = lcm(1,...,k).
```

The verifier checks admissibility directly using Lucas' theorem: for every prime `p<=k`,
`C(n,k)` is nonzero modulo `p` iff every base-`p` digit of `k` is at most the corresponding digit of `n`.

## Candidate reduction

If `delta(n,k)>1`, the interval `(n-k,n]` contains at least two divisors of `L_k`.
Therefore some adjacent divisors `a<b` of `L_k` satisfy

```text
b-a < k.
```

Such a pair can occur together only for endpoints

```text
b <= n <= a+k-1.
```

The verifier merges these endpoint intervals, tests the canonical admissibility predicate, and counts divisors of `L_k` in the window exactly by binary search.

For scale, at `k=65`:

```text
tau(L_65) = 4,128,768
merged candidate endpoints checked = 773,053
```

so the structural reduction removes the overwhelming majority of possible endpoints before Lucas testing.

## Independent replay receipt

A fresh local execution of the same algorithm on release day returned:

```text
k<=45 replay_match = True
46<=k<=65 deficiency>1 hits = {}
```

The replay through `k<=45` took under one second in the release environment; the `46..65` extension took about 38 seconds. Timings are machine-dependent and are not part of the mathematical claim.

## Scope

- exact finite computation only;
- parent problem remains open;
- no claim that `65` is mathematically special;
- no historical novelty claim beyond the independently extended finite search frontier stated here.
