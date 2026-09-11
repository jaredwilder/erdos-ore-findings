from math import comb, gcd, factorial, isqrt
from fractions import Fraction


def is_prime(n):
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


def v2(n):
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def vp_factorial(n, p):
    s = 0
    while n:
        n //= p
        s += n
    return s


# Erdős 400: exact factorial witness for a finite regression grid.
for m in range(2, 8):
    M = factorial(m)
    for k in range(2, 7):
        prod = factorial(M - 1) * factorial(m)
        assert prod == factorial(M)
        gain = (M - 1) + m + (k - 2) - M
        assert gain == m + k - 3


# Erdős 289: finite regression for interval nonintegrality and unique max v2.
for a in range(1, 80):
    for b in range(a + 1, min(a + 20, 100)):
        vals = [v2(n) for n in range(a, b + 1)]
        assert vals.count(max(vals)) == 1
        s = sum((Fraction(1, n) for n in range(a, b + 1)), Fraction(0, 1))
        assert s.denominator != 1


# Erdős 313: fixed head (2,3,p).
solutions = []
for p in range(7, 500):
    if not is_prime(p):
        continue
    num = 6 * p
    den = p - 6
    if num % den == 0:
        solutions.append((p, num // den))
assert solutions == [(7, 42)]


# Erdős 700: semiprime formula for a broad finite grid.
def f700(n):
    return min(gcd(n, comb(n, k)) for k in range(2, n // 2 + 1))

primes = [p for p in range(2, 80) if is_prime(p)]
for i, p in enumerate(primes):
    for q in primes[i:]:
        n = p * q
        assert f700(n) == p

assert comb(21, 7) == 116280
assert gcd(21, comb(21, 7)) == 3
assert f700(21) == 3


# Prime-square Kummer valuation spot-check used in Erdős 700.
for p in primes:
    # v_p(C(p^2,p)) = v_p((p^2)!)-v_p(p!)-v_p((p^2-p)!) = 1
    val = vp_factorial(p * p, p) - vp_factorial(p, p) - vp_factorial(p * p - p, p)
    assert val == 1

print('Gold Rush 03 regression checks: PASS')
