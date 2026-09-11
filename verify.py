"""Independently check the ore findings that are cheap to check.

Every claim here came out of a prose ore object with claimed_status PROVED. A claimed
status is a lead, not a verdict. These are recomputed from scratch.
"""
from math import comb, isqrt


def largest_prime_factor(n):
    lp, d = 1, 2
    while d * d <= n:
        while n % d == 0:
            lp, n = d, n // d
        d += 1
    return max(lp, n) if n > 1 else lp


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


print("=" * 66)
print("ERDOS 683 -- counterexamples to P(C(n,k)) >= min(n-k+1, k^(1+c))")
for (n, k) in [(9, 2), (10, 3)]:
    C = comb(n, k)
    P = largest_prime_factor(C)
    print("  C(%d,%d) = %-6d  largest prime factor = %d" % (n, k, C, P))
    for c in (0.5, 0.75, 1.0):
        bound = min(n - k + 1, k ** (1 + c))
        verdict = "REFUTES" if P < bound else "holds"
        print("      c=%-5s  min(%d, %.4f) = %.4f   P=%d  -> %s"
              % (c, n - k + 1, k ** (1 + c), bound, P, verdict))

print()
print("=" * 66)
print("ERDOS 683 -- the c <= 0.20905 claim from (10,5), which the miner could NOT reproduce")
n, k = 10, 5
C = comb(n, k)
P = largest_prime_factor(C)
print("  C(10,5) = %d, largest prime factor = %d" % (C, P))
for c in (0.0, 0.20905, 0.5, 1.0):
    bound = min(n - k + 1, k ** (1 + c))
    print("      c=%-8s min(%d, %.4f) = %.4f  P=%d  inequality holds? %s"
          % (c, n - k + 1, k ** (1 + c), bound, P, P >= bound))

print()
print("=" * 66)
print("ERDOS 238 -- maximum run of consecutive composites in [2, 10^6]")
LIM = 1000000
sieve = bytearray([1]) * (LIM + 1)
sieve[0] = sieve[1] = 0
for i in range(2, isqrt(LIM) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
best, run, start, bstart = 0, 0, 0, 0
for i in range(2, LIM + 1):
    if not sieve[i]:
        if run == 0:
            start = i
        run += 1
        if run > best:
            best, bstart = run, start
    else:
        run = 0
print("  longest composite run = %d, from %d to %d" % (best, bstart, bstart + best - 1))
print("  bracketing primes: %d and %d, gap %d"
      % (bstart - 1, bstart + best, best + 1))
print("  claim was: run 113 between primes 492113 and 492227, gap 114")
print("  MATCHES:", best == 113 and bstart - 1 == 492113 and bstart + best == 492227)

print()
print("=" * 66)
print("ERDOS 930 -- Pell family: x^2-2s^2=1 gives 1*2*a*(a+1) = s^2 with a=(x-1)/2")
for (x, s) in [(3, 2), (17, 12), (99, 70), (577, 408), (3363, 2378)]:
    if (x * x - 2 * s * s) != 1:
        print("  (x=%d,s=%d) NOT a Pell solution" % (x, s))
        continue
    a = (x - 1) // 2
    prod = 1 * 2 * a * (a + 1)
    r = isqrt(prod)
    print("  x=%-6d s=%-5d a=%-4d  1*2*a*(a+1) = %-10d  = %d^2 ? %s"
          % (x, s, a, prod, r, r * r == prod))
