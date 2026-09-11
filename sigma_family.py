"""Erdos 1061: sigma(a) + sigma(2a) = sigma(3a) for every a coprime to 6.

Proof is three lines (multiplicativity: sigma(2a)=3sigma(a), sigma(3a)=4sigma(a)).
This script is the check, not the proof.
"""
from sympy import divisor_sigma as S, gcd

fails = 0
n = 0
for a in range(1, 4000):
    if gcd(a, 6) != 1:
        continue
    n += 1
    if S(a) + S(2 * a) != S(3 * a):
        fails += 1
        print("  FAIL at a =", a)
print("identity sigma(a)+sigma(2a)=sigma(3a), gcd(a,6)=1:")
print("  checked %d values of a below 4000, %d failures" % (n, fails))
assert fails == 0

print()
print("the diagonal 2*sigma(a) = sigma(2a):")
sols = [a for a in range(1, 5000) if 2 * S(a) == S(2 * a)]
print("  solutions with a < 5000:", sols)
assert sols == []
print("  proof: a = 2^k m, m odd; sigma(2a)-2sigma(a) = sigma(m) >= 1")

print()
print("spot check of sigma(2a) - 2 sigma(a) = sigma(odd part of a):")
bad = 0
for a in [1, 2, 3, 4, 6, 8, 12, 24, 40]:
    m = a
    while m % 2 == 0:
        m //= 2
    lhs = S(2 * a) - 2 * S(a)
    ok = lhs == S(m)
    bad += 0 if ok else 1
    print("  a=%-3d odd part=%-3d  lhs=%-4d  sigma(m)=%-4d  %s"
          % (a, m, lhs, S(m), "OK" if ok else "FAIL"))
assert bad == 0
print()
print("all checks passed")
