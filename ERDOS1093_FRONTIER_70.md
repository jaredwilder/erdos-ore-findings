# Erdős #1093 — exact finite frontier extended through `k <= 70`

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Base verifier:** `verify_erdos1093_frontier65.py`  
**Increment verifier:** `verify_erdos1093_frontier66_70.py`

## Result

The independently reconstructed divisor-window engine reproduces the complete maintained deficiency `>1` list through `k<=45`, finds no additional examples for `46<=k<=65`, and now also finds

```text
NO deficiency > 1 examples for 66 <= k <= 70.
```

Therefore the exact independently checked no-new-example frontier represented by this release is

```text
k <= 70.
```

This remains a finite computation. Erdős #1093 itself is not claimed solved.

## Increment details

For `k=66`,

```text
L_66 = L_65,
tau(L_66) = 4,128,768,
merged candidate endpoints = 792,148,
deficiency>1 hits = none.
```

At `k=67`, the lcm acquires the new prime factor 67:

```text
L_k = 67 L_65   for 67 <= k <= 70.
```

Hence the divisor set is the disjoint union

```text
D(L_k) = D(L_65) union 67 D(L_65).
```

Rather than materializing all

```text
8,257,536
```

divisors, the verifier merges the two sorted streams once and keeps only adjacent divisor gaps shorter than 71. Exactly

```text
45,313
```

such close gaps occur.

Those gaps generate all possible endpoint intervals for deficiency `>1`. The exact candidate counts are

```text
k=67: 1,053,772 endpoints
k=68: 1,079,415 endpoints
k=69: 1,105,259 endpoints
k=70: 1,131,243 endpoints
```

Every candidate is then checked against the canonical admissibility predicate using Lucas' theorem for each prime `p<=k`, and its divisor-window deficiency is counted exactly by binary search in the two divisor streams.

The result is empty in all four cases.

## Why the reduction is exhaustive

For admissible `(n,k)`, with

```text
L_k = lcm(1,...,k),
```

the deficiency is

```text
delta(n,k) = #{d | L_k : n-k < d <= n}.
```

If `delta(n,k)>1`, then at least two divisors of `L_k` lie in an interval of length `k`. Therefore some adjacent divisors `a<b` satisfy

```text
b-a < k.
```

Both divisors can occur in `(n-k,n]` only when

```text
b <= n <= a+k-1.
```

Thus every possible positive hit is contained in one of the generated endpoint intervals. No ungenerated endpoint can have deficiency greater than one.

## Authority boundary

- `k<=45`: independent replay exactly matches the maintained public deficiency `>1` list before extension.
- `46<=k<=70`: exact finite no-hit computation.
- no asymptotic inference is made from the finite frontier;
- no claim is made that `70` is intrinsically special;
- historical novelty is limited to the explicitly stated independently extended finite frontier.
