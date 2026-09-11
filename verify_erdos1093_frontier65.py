#!/usr/bin/env python3
"""Independent finite verifier for the Erdős #1093 deficiency frontier through k=65.

Canonical semantics (n >= 2k): deficiency is defined only when no prime p <= k
divides C(n,k). If defined, it counts the k-smooth integers in (n-k,n].

For admissible (n,k), the divisor-window reduction gives
    delta(n,k) = #{d | L_k : n-k < d <= n},
where L_k = lcm(1,...,k).

A value delta>1 therefore forces two adjacent divisors of L_k to be less
than k apart. We enumerate only the resulting candidate endpoint intervals,
check admissibility by Lucas' theorem modulo every prime p<=k, and then count
divisors in the window exactly.

The script first reproduces the complete maintained list of known delta>1
examples through k=45, then verifies that there are no such examples for
46 <= k <= 65.
"""

from bisect import bisect_right
from math import isqrt


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def lcm_factorization(k: int) -> list[tuple[int, int]]:
    out = []
    for p in primes_upto(k):
        q = 1
        e = 0
        while q * p <= k:
            q *= p
            e += 1
        out.append((p, e))
    return out


def divisors_of_lcm(k: int) -> list[int]:
    divs = [1]
    for p, e in lcm_factorization(k):
        powers = [1]
        for _ in range(e):
            powers.append(powers[-1] * p)
        divs = [d * pe for d in divs for pe in powers]
    divs.sort()
    return divs


def lucas_nonzero_mod_p(n: int, k: int, p: int) -> bool:
    """Return C(n,k) != 0 (mod p) by Lucas digit comparison."""
    while k:
        if (k % p) > (n % p):
            return False
        n //= p
        k //= p
    return True


def admissible(n: int, k: int, primes: list[int]) -> bool:
    return all(lucas_nonzero_mod_p(n, k, p) for p in primes)


def candidate_ranges(divs: list[int], k: int) -> list[tuple[int, int]]:
    """Merged n-ranges whose window can contain >=2 divisors of L_k."""
    intervals = []
    for a, b in zip(divs, divs[1:]):
        if b - a >= k:
            continue
        lo = max(b, 2 * k)
        hi = a + k - 1
        if lo <= hi:
            intervals.append((lo, hi))

    if not intervals:
        return []

    intervals.sort()
    merged = [list(intervals[0])]
    for lo, hi in intervals[1:]:
        if lo <= merged[-1][1] + 1:
            if hi > merged[-1][1]:
                merged[-1][1] = hi
        else:
            merged.append([lo, hi])
    return [(lo, hi) for lo, hi in merged]


def deficiency_gt1(k: int) -> list[tuple[int, int]]:
    divs = divisors_of_lcm(k)
    ps = primes_upto(k)
    hits = []

    for lo, hi in candidate_ranges(divs, k):
        for n in range(lo, hi + 1):
            if not admissible(n, k, ps):
                continue
            left = bisect_right(divs, n - k)
            right = bisect_right(divs, n)
            delta = right - left
            if delta > 1:
                hits.append((n, delta))
    return hits


EXPECTED_THROUGH_45 = {
    8: [(44, 2)],
    10: [(46, 3), (47, 3), (74, 2)],
    11: [(47, 4)],
    12: [(174, 2)],
    14: [(239, 2)],
    16: [(241, 3)],
    25: [(2105, 3)],
    27: [(1119, 3), (5179, 2)],
    28: [(284, 9), (8413, 2), (8414, 2)],
    33: [(6459, 3)],
    42: [(96622, 2)],
}


def main() -> None:
    reproduced = {}
    for k in range(2, 46):
        hits = deficiency_gt1(k)
        if hits:
            reproduced[k] = hits

    assert reproduced == EXPECTED_THROUGH_45, (
        "k<=45 replay mismatch\n"
        f"expected={EXPECTED_THROUGH_45}\n"
        f"actual={reproduced}"
    )
    print("PASS: reproduced all maintained deficiency>1 examples through k=45")

    new_hits = {}
    for k in range(46, 66):
        hits = deficiency_gt1(k)
        if hits:
            new_hits[k] = hits
        print(f"k={k}: {hits}")

    assert not new_hits, f"unexpected deficiency>1 examples in 46<=k<=65: {new_hits}"
    print("PASS: no deficiency>1 examples for 46 <= k <= 65")
    print("ERDOS1093_FRONTIER_65: PASS")


if __name__ == "__main__":
    main()
