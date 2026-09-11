#!/usr/bin/env python3
"""Exact finite extension for Erdős #1093, k=66..70.

This companion starts from divisors of L_65.  For k=66 the lcm is unchanged.
For k=67..70, L_k = 67*L_65, so the divisor set is the disjoint sorted union
D U 67D.  We stream adjacent gaps in that union instead of materializing all
8,257,536 divisors.

A deficiency >1 forces two adjacent divisors of L_k to lie less than k apart.
Those close gaps generate all possible endpoint intervals.  Canonical
admissibility is checked with Lucas' theorem for every prime p<=k.
"""

from bisect import bisect_right
from math import isqrt


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n+1:p] = b"\x00" * (((n-start)//p)+1)
    return [p for p in range(2, n + 1) if sieve[p]]


def divisors_of_lcm(k):
    divs = [1]
    for p in primes_upto(k):
        q = 1
        e = 0
        while q * p <= k:
            q *= p
            e += 1
        powers = [1]
        for _ in range(e):
            powers.append(powers[-1] * p)
        divs = [d * pe for d in divs for pe in powers]
    divs.sort()
    return divs


def lucas_nonzero(n, k, p):
    while k:
        if k % p > n % p:
            return False
        n //= p
        k //= p
    return True


def merged_endpoint_intervals(gaps, k):
    intervals = []
    for a, b in gaps:
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
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    return [tuple(x) for x in merged]


def direct_gaps(D, max_gap):
    return [(a, b) for a, b in zip(D, D[1:]) if b - a < max_gap]


def union_gaps(D, scale, max_gap):
    """Adjacent close gaps in sorted disjoint union D U scale*D."""
    i = j = 0
    N = len(D)
    previous = None
    out = []
    while i < N or j < N:
        x1 = D[i] if i < N else None
        x2 = scale * D[j] if j < N else None
        if x2 is None or (x1 is not None and x1 < x2):
            x = x1
            i += 1
        elif x1 is None or x2 < x1:
            x = x2
            j += 1
        else:
            raise AssertionError("D and scale*D unexpectedly intersect")
        if previous is not None and x - previous < max_gap:
            out.append((previous, x))
        previous = x
    return out


def admissible(n, k, primes):
    return all(lucas_nonzero(n, k, p) for p in primes)


def direct_count(D, x):
    return bisect_right(D, x)


def union_count(D, scale, x):
    if x < 0:
        return 0
    return bisect_right(D, x) + bisect_right(D, x // scale)


def scan(D, gaps, k, counter):
    primes = primes_upto(k)
    intervals = merged_endpoint_intervals(gaps, k)
    hits = []
    endpoints = 0
    for lo, hi in intervals:
        endpoints += hi - lo + 1
        for n in range(lo, hi + 1):
            if not admissible(n, k, primes):
                continue
            delta = counter(n) - counter(n-k)
            if delta > 1:
                hits.append((n, delta))
    return hits, endpoints, len(intervals)


def main():
    D = divisors_of_lcm(65)
    assert len(D) == 4_128_768

    gaps66 = direct_gaps(D, 67)
    hits66, endpoints66, intervals66 = scan(
        D, gaps66, 66, lambda x: direct_count(D, x)
    )
    assert hits66 == []
    assert endpoints66 == 792_148

    gaps67 = union_gaps(D, 67, 71)
    assert len(gaps67) == 45_313

    expected_endpoints = {
        67: 1_053_772,
        68: 1_079_415,
        69: 1_105_259,
        70: 1_131_243,
    }

    print(f"k=66 hits={hits66} endpoints={endpoints66} intervals={intervals66}")
    for k in range(67, 71):
        hits, endpoints, intervals = scan(
            D, gaps67, k, lambda x, D=D: union_count(D, 67, x)
        )
        assert hits == []
        assert endpoints == expected_endpoints[k]
        print(f"k={k} hits={hits} endpoints={endpoints} intervals={intervals}")

    print("ERDOS1093_FRONTIER_70_INCREMENT: PASS")


if __name__ == "__main__":
    main()
