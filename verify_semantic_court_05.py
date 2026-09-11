"""Exact regression checks for SEMANTIC_COURT_05.md.

These checks pin the arithmetic/logic witnesses. They do not replace the
literature reconciliation in the court record.
"""
from math import comb, gcd, log

# Erdős 396: k=2 has the exact witness n=2480.
n = 2480
block = n * (n - 1) * (n - 2)
assert comb(2 * n, n) % block == 0

# Erdős 943: powerful-number convolution is additive, so a simple value can
# be checked by enumerating powerful a+b=n rather than divisors ab=n.
def prime_factors(n: int):
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            yield p, e
        p += 1
    if n > 1:
        yield n, 1

def powerful(n: int) -> bool:
    if n == 1:
        return True
    return all(e >= 2 for _, e in prime_factors(n))

# 10 = 1+9 = 9+1 are additive powerful representations.
reps10 = [(a, 10-a) for a in range(1, 10) if powerful(a) and powerful(10-a)]
assert reps10 == [(1, 9), (9, 1)]

# Erdős 317: the LCM granularity scale is smaller than 2^-n at n=10.
def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b
L = 1
for k in range(1, 11):
    L = lcm(L, k)
assert L == 2520
assert 1 / L < 1 / (2 ** 10)
# Exact equality witness for the strict second clause at n=4.
from fractions import Fraction
s = Fraction(1, 2) - Fraction(1, 3) - Fraction(1, 4)
assert s == Fraction(-1, 12)

# Erdős 881: allowed residues of N\{2 mod 4} add to all residue classes.
allowed = {0, 1, 3}
sum_residues = {(a + b) % 4 for a in allowed for b in allowed}
assert sum_residues == {0, 1, 2, 3}

# Erdős 1203: fixed k=3 gives an unbounded subsequence using primorials.
def first_primes(r: int):
    out = []
    x = 2
    while len(out) < r:
        is_p = all(x % p for p in out if p * p <= x)
        if is_p:
            out.append(x)
        x += 1
    return out

c3 = log(log(3)) / log(3)
assert c3 > 0
previous = 0.0
for r in range(2, 10):
    M = 1
    for p in first_primes(r):
        M *= p
    n = M - 3
    omega = len(list(prime_factors(n + 3)))
    lower = omega * c3
    assert omega == r
    assert lower > previous
    previous = lower

print("Semantic Court 05 regression checks: PASS")
