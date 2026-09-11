# Semantic Court 14 — Erdős #701 hereditary-family count was mislabeled

Author: Jared Wilder  
Court date: 2026-09-11

## Verdict

A Pass-6 summary says that the finite Chvátal-star audit exhausted

`65,812 hereditary families with |X| in {1,2,3,4}`

and explains the number as

`4 + 16 + 256 + 65,536`.

That description is **incorrect**.

For a ground set of size `n`, the number

`2^(2^n)`

counts **all families of subsets** of the ground set. It does not count hereditary families/downsets.

The numbers of hereditary families are the Dedekind numbers

- `M(1)=3`,
- `M(2)=6`,
- `M(3)=20`,
- `M(4)=168`.

Thus there are exactly

`3+6+20+168 = 197`

hereditary families across ground-set sizes 1 through 4.

## Independent recomputation

The finite theorem itself survives.

A fresh exact enumeration generated every downset for `n=1,2,3,4`, computed

- the largest pairwise-intersecting subfamily, and
- the largest star,

for each downset, and found **zero violations** of the Chvátal-star inequality.

The recovered counts were exactly

`3, 6, 20, 168`.

## Correct finite theorem

Every hereditary family on a ground set of size at most 4 has a largest intersecting subfamily no larger than a largest star.

This is a finite exhaustive result, not a proof of the general Chvátal conjecture.

## Failure class

This is a **universe-count / label mismatch**:

- `65,812` is the number of all set-families across `n=1..4`;
- `197` is the number of hereditary families actually relevant to the theorem.

The mathematical finite conclusion survives after the counting description is repaired.