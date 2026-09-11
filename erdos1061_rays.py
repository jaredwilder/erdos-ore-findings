"""Erdos 1061: every solution of sigma(a)+sigma(b)=sigma(a+b) seeds a ray,
the rays are disjoint, and their densities add. Exits 0 or raises."""
from sympy import divisor_sigma as sigma, primefactors
from fractions import Fraction as F
from math import gcd

LIM = 4000


def solves(a, b):
    return sigma(a) + sigma(b) == sigma(a + b)


def rad(n):
    r = 1
    for p in primefactors(n):
        r *= p
    return r


def coefficient(a, b, s):
    """2*phi(M)/(M*s) with M = rad(a*b*s)"""
    M = rad(a * b * s)
    phi = M
    for p in primefactors(M):
        phi = phi // p * (p - 1)
    return F(2 * phi, M * s)


print("Erdos 1061: ray structure")

# --- find all solutions with s < LIM -----------------------------------------
seeds = []
for s in range(2, LIM):
    for a in range(1, s // 2 + 1):
        if solves(a, s - a):
            seeds.append((a, s - a, s))
print("  solutions with s < %d: %d" % (LIM, len(seeds)))
assert len(seeds) == 4745

# --- the scaling theorem ------------------------------------------------------
tested = bad = 0
for (a, b, s) in seeds[:40]:
    M = rad(a * b * s)
    for k in (2, 3, 5, 7, 11, 13):
        if gcd(k, M) != 1:
            continue
        tested += 1
        if not solves(k * a, k * b):
            bad += 1
print("  scaling theorem: %d scaled pairs tested, %d failures" % (tested, bad))
assert bad == 0 and tested > 100

# --- primitivity and disjointness --------------------------------------------
prim = [(a, b, s) for (a, b, s) in seeds if gcd(a, b) == 1]
print("  primitive seeds (gcd(a,b)=1): %d" % len(prim))
assert len(prim) == 1437
# gcd(a,b)=1 is equivalent to gcd(a,b,s)=1 since s=a+b
for (a, b, s) in seeds:
    assert (gcd(a, b) == 1) == (gcd(gcd(a, b), s) == 1)
# distinct primitive seeds have distinct reduced ratios => disjoint rays
ratios = {(a, b) for (a, b, s) in prim}
assert len(ratios) == len(prim), "primitive seeds must be pairwise non-proportional"
print("  all %d primitive seeds pairwise non-proportional => rays disjoint" % len(prim))

# --- sum the coefficients -----------------------------------------------------
total = sum((coefficient(*t) for t in prim), F(0))
print("  sum of ray coefficients: %.12f" % float(total))
assert float(total) > 0.94

# --- the published single family is the largest ray ---------------------------
print("  the (a,2a) family, a coprime to 6:")
for a in (1, 5, 7, 11):
    c = coefficient(a, 2 * a, 3 * a)
    print("    seed (%d,%d,%d)  coefficient %s" % (a, 2 * a, 3 * a, c))
assert coefficient(1, 2, 3) == F(2, 9)
# and it is the single largest coefficient of all
biggest = max(prim, key=lambda t: coefficient(*t))
assert coefficient(*biggest) == F(2, 9), biggest
print("    (1,2,3) has coefficient 2/9 and is the LARGEST of all %d rays" % len(prim))

# --- direct count at a point well inside the seed range -----------------------
X = 2000
c = 2 * sum(1 for (a, b, s) in seeds if s <= X) - sum(1 for (a, b, s) in seeds if s <= X and a == b)
print("  direct count at x=%d: %d ordered solutions, S(x)/x = %.3f" % (X, c, c / X))
assert c / X > float(total), "direct count must exceed the certified bound"

print()
print("liminf S(x)/x >= %.12f  -- so S(x) = o(x) is false" % float(total))
print("all checks passed")
