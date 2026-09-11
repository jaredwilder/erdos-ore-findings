"""Six exact values from the Erdos ore, recomputed. Exits 0 or raises."""
from collections import defaultdict
from math import factorial, gcd, isqrt, pi
from sympy import primerange, mobius, totient, divisor_count, factorint
from mpmath import mp, mpf

# ---------------------------------------------------------------- E979 ------
print("E979: sums of two prime squares")
LIM = 200000
pr = [p for p in primerange(2, isqrt(LIM) + 2)]
reps = defaultdict(list)
for i, a in enumerate(pr):
    for b in pr[i:]:
        s = a * a + b * b
        if s <= LIM:
            reps[s].append((a, b))
mx = max(len(v) for v in reps.values())
tops = sorted(n for n in reps if len(reps[n]) == mx)
print("  max multiplicity below %d: %d, attained at %s" % (LIM, mx, tops))
assert mx == 8 and tops == [81770]
for a, b in sorted(reps[81770]):
    assert a * a + b * b == 81770
    print("    %3d^2 + %3d^2" % (a, b))
assert len(reps[81770]) == 8

# ---------------------------------------------------------------- E145 ------
print()
print("E145: squarefree count")
X = 10 ** 7
N = sum(mobius(d) * (X // (d * d)) for d in range(1, isqrt(X) + 1))
est = int(6 / pi ** 2 * X)
print("  N(10^7) = %d" % N)
print("  floor((6/pi^2)*10^7) = %d   (the value the ore filed)" % est)
assert N == 6079291
assert est == 6079271
assert N - est == 20

# ---------------------------------------------------------------- E68 -------
print()
print("E68: the constant, and pairwise coprimality")
mp.dps = 60
S = sum((mpf(1) / (mpf(factorial(n)) - 1) for n in range(2, 60)), mpf(0))
s49 = mp.nstr(S, 49)
print("  S =", s49)
assert s49.startswith("1.2534987556999534716433609379")

bad = [(n, m, gcd(factorial(n) - 1, factorial(m) - 1))
       for n in range(2, 25) for m in range(n + 1, 25)
       if gcd(factorial(n) - 1, factorial(m) - 1) > 1]
print("  pairs 2<=n<m<=24 with gcd(n!-1, m!-1) > 1:", len(bad))
assert len(bad) == 9
assert (4, 8, 23) in bad
assert factorial(4) - 1 == 23
assert factorial(8) - 1 == 40319 == 23 * 1753
assert set(g for _, _, g in bad) == {17, 23}
print("    gcd(4!-1, 8!-1) = gcd(23, 40319) = 23")

# ---------------------------------------------------------------- E51 -------
print()
print("E51: extremal totient preimage ratio")
LIM2 = 20000
least = {}
for m in range(1, 400000):
    t = int(totient(m))
    if t <= LIM2 and t not in least:
        least[t] = m
best = max(least, key=lambda a: least[a] / a)
print("  max n_a/a = %d/%d = %.6f at a=%d" % (least[best], best, least[best] / best, best))
assert best == 5888 and least[5888] == 11985
assert factorint(5888) == {2: 8, 23: 1}
assert factorint(11985) == {3: 1, 5: 1, 17: 1, 47: 1}
over = [(a, least[a]) for a in sorted(least) if least[a] / a > 2]
print("  totient values with ratio > 2:", over)
assert over == [(5888, 11985), (10496, 21165), (17408, 34935)]

# ---------------------------------------------------------------- E826 ------
print()
print("E826: tau(n+k) <= 2k for every k")


def holds(n):
    for k in range(1, 300):
        if divisor_count(n + k) > 2 * k:
            return False
        if 2 * isqrt(n + k) <= 2 * k:      # tau(m) <= 2*sqrt(m) settles the tail
            return True
    return True


good = [n for n in range(1, 3001) if holds(n)]
print("  complete list n <= 3000:", good)
assert good == [1, 2, 4, 6, 12, 36, 60, 72, 420]

# ---------------------------------------------------------------- E829 ------
print()
print("E829: two representations as a sum of two positive cubes")
cubes = defaultdict(list)
R = int(200000 ** (1 / 3)) + 2
for a in range(1, R):
    for b in range(a, R):
        s = a ** 3 + b ** 3
        if s < 200000:
            cubes[s].append((a, b))
two = sorted(n for n in cubes if len(cubes[n]) >= 2)
print("  count below 200000:", len(two))
print(" ", two)
assert len(two) == 17
assert two[0] == 1729 and 20683 in two
assert max(len(v) for v in cubes.values()) == 2
assert cubes[1729] == [(1, 12), (9, 10)]

print()
print("all six verified")
