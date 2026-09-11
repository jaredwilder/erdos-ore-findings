"""Cheap exact regression checks for SEMANTIC_COURT_02.md.

The script does not replace the semantic/literature arguments in the court record.
It pins the finite arithmetic that should never regress in later mining.
"""
from math import comb, isqrt


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


def least_prime_factor(n: int) -> int:
    assert n >= 2
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return n


def F385(n: int) -> int:
    vals = [m + least_prime_factor(m) for m in range(4, n) if not is_prime(m)]
    return max(vals)


def pstar(n: int) -> int:
    return max(p for p in range(2, n // 2) if is_prime(p))


# Erdős 385: explicit failures of the spurious F(n) >= 3 p* bound.
for n, expected in [(100, 102), (1000, 1012)]:
    f = F385(n)
    p = pstar(n)
    assert f == expected
    assert f < 3 * p

# The actual elementary parity baseline survives.
for n in range(5, 500):
    f = F385(n)
    if n % 2:
        assert f >= n + 1
    elif n >= 6:
        assert f >= n

# Erdős 1056: known intended-semantics k=2 example.
# Boundaries 3<5<8 give adjacent blocks [3,5) and [5,8).
p = 11
block1 = list(range(3, 5))
block2 = list(range(5, 8))
prod1 = 1
prod2 = 1
for x in block1:
    prod1 = prod1 * x % p
for x in block2:
    prod2 = prod2 * x % p
assert prod1 == prod2 == 1

# Separated odd singleton blocks are not adjacent consecutive blocks:
# [1,2) ends at 2, whereas [3,4) begins at 3.
assert 2 != 3

# Erdős 325: 4 mod 9 cannot be a sum of three cube residues.
cube_residues = {pow(x, 3, 9) for x in range(9)}
three_cube_residues = {(a + b + c) % 9 for a in cube_residues for b in cube_residues for c in cube_residues}
assert cube_residues == {0, 1, 8}
assert 4 not in three_cube_residues and 5 not in three_cube_residues
# But an upper constant 7/9 and a positive lower constant 1/100 are compatible.
assert 1 / 100 < 7 / 9

# Erdős 1049: the Lambert identity can be checked on finite truncations after
# expanding 1/(t^n-1) as a geometric series. Pin exact rational arithmetic.
from fractions import Fraction

def tau(n: int) -> int:
    return sum(1 for d in range(1, n + 1) if n % d == 0)

t = Fraction(2, 1)
# Compare coefficients through t^{-M}: each m receives one contribution per divisor.
M = 80
coeff = [0] * (M + 1)
for n in range(1, M + 1):
    for k in range(1, M // n + 1):
        coeff[n * k] += 1
for m in range(1, M + 1):
    assert coeff[m] == tau(m)

print("Semantic Court 02 regression checks: PASS")
