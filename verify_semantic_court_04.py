"""Exact regression checks for SEMANTIC_COURT_04.md.

The literature/domain findings in the court record are not replaced by these
finite checks. This file pins the direct definitional falsifiers.
"""
from math import gcd


def distinct_prime_factors(n: int) -> list[int]:
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


# Erdős 539: diagonal terms are all 1, not the elements of A.
for A in [{2, 3}, {6, 10, 15}, {7, 14, 21, 28}]:
    diagonal = {a // gcd(a, a) for a in A}
    assert diagonal == {1}

# Erdős 489: if A is the set of all primes, every n>1 is excluded from B.
# Verify the finite prefix directly.
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

primes = [p for p in range(2, 501) if is_prime(p)]
B = []
for n in range(1, 501):
    if all(n % p != 0 for p in primes):
        B.append(n)
assert B == [1]

# Erdős 889: powers of two do not force v_0=1.
def v(n: int, k: int) -> int:
    return sum(1 for p in distinct_prime_factors(n + k) if p > k)

assert v(32, 0) == 1
assert v(32, 1) == 2   # 33 = 3*11
assert v(64, 0) == 1
assert v(64, 1) == 2   # 65 = 5*13

# A few powers of two past the Erdős-Selfridge threshold already have max >=2.
for n in [32, 64, 128, 256]:
    assert max(v(n, k) for k in range(n + 1)) >= 2

# Erdős 406: "ternary digits in {0,1}" does not imply a fixed digit-sum
# bound. Exhibit numbers with arbitrarily many ternary 1s (not necessarily
# powers of two): 1+3+...+3^(r-1) has exactly r ternary 1-digits.
for r in range(1, 30):
    n = sum(3 ** j for j in range(r))
    x = n
    s = 0
    while x:
        digit = x % 3
        assert digit in (0, 1)
        s += digit
        x //= 3
    assert s == r

print("Semantic Court 04 regression checks: PASS")
