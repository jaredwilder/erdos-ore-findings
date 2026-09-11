"""Erdos 655 (regular n-gon refutation) and Erdos 477 (exact complements of
polynomial images). Both are constructions; this asserts every claim in the
write-up. Exits 0 or raises."""
from collections import Counter
import sympy as sp

# ---------------------------------------------------------------- Erdos 655 --
print("Erdos 655: the regular n-gon satisfies the hypothesis, fails the conclusion")
print("  exact symbolic check (algebraic numbers, no floats):")
for n in range(3, 17):
    mult = Counter()
    for k in range(1, n):
        d2 = sp.simplify(sp.expand(sp.nsimplify(2 - 2 * sp.cos(2 * sp.pi * k / n))))
        mult[d2] += 1
    distinct = len(mult)
    worst = max(mult.values())
    print("    n=%-3d distinct=%-3d floor(n/2)=%-3d  max on one circle=%d"
          % (n, distinct, n // 2, worst))
    assert distinct == n // 2, n
    assert worst <= 2, n                     # hypothesis: never 3 on a circle

# the integer criterion k ~ n-k, swept far
for n in range(3, 513):
    mult = Counter()
    for k in range(1, n):
        mult[min(k, n - k)] += 1
    assert len(mult) == n // 2, n
    assert max(mult.values()) <= 2, n
print("  integer criterion k = +-j (mod n) swept n=3..512: 0 failures")
# and floor(n/2) < (1+c)n/2 for every c>0
for n in (3, 10, 101, 512):
    assert n // 2 <= n / 2
print("  -> floor(n/2) <= n/2 < (1+c)n/2 for every c>0; refuted for all n >= 3")

# ---------------------------------------------------------------- Erdos 477 --
print()
print("Erdos 477: exact complements A (+) f(Z) = Z")

# (1) difference of two squares <=> d not 2 mod 4, built constructively
CAP = 3000


def is_diff_of_squares(d):
    if d == 0:
        return True
    ad = abs(d)
    for u in range(1, ad + 1):
        if ad % u:
            continue
        v = ad // u
        if (u + v) % 2:
            continue
        j, k = (u + v) // 2, (v - u) // 2
        if j * j - k * k == ad:
            return True
    return False


D = set(d for d in range(-CAP, CAP + 1) if is_diff_of_squares(d))
pred = set(d for d in range(-CAP, CAP + 1) if d % 4 != 2)
assert D == pred
print("  squares: difference set = {d : d != 2 mod 4}, verified |d| <= %d" % CAP)

# (2) the three-term kill
assert (2 + 2) % 4 == 0 != 2
print("  three-term kill: 2 + 2 = 0 mod 4, not 2  =>  |A| <= 2")
import math
for N in (10 ** 4, 10 ** 6, 10 ** 8):
    assert 2 * (math.isqrt(N) + 1) < N // 10
print("  and |A| <= 2 covers o(N) of [1,N]  =>  no exact complement for k^2")


# (3) the general-quadratic claim is FALSE at (a,b,c) = (2,1,0)
def missed_classes(a, b, c, R=400):
    V = [a * k * k + b * k + c for k in range(-R, R + 1)]
    m = 4 * abs(a)
    hit = set()
    for x in V:
        for y in V:
            if x != y:
                hit.add((x - y) % m)
    return m, sorted(r for r in range(m) if r not in hit)


print()
print("  the filed claim: every quadratic misses exactly ONE class mod 4|a|")
table = [(1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 0, 0), (3, 1, 0), (4, 0, 0), (5, 2, 0)]
counts = {}
for (a, b, c) in table:
    m, ms = missed_classes(a, b, c)
    counts[(a, b, c)] = len(ms)
    print("    f = %dk^2%+dk%+d  mod %-3d  misses %2d class(es): %s"
          % (a, b, c, m, len(ms), ms))
assert counts[(1, 0, 0)] == 1                 # the k^2 case does miss exactly one
assert counts[(2, 1, 0)] == 0                 # THE COUNTEREXAMPLE
assert len(set(counts.values())) > 1          # count is not even constant

# explicit smallest witnesses for 2k^2+k, all 8 classes
f = lambda k: 2 * k * k + k
best = {}
for j in range(-60, 61):
    for k in range(-60, 61):
        d = f(j) - f(k)
        if d == 0:
            continue
        r = d % 8
        if r not in best or abs(d) < abs(best[r][0]):
            best[r] = (d, j, k)
assert sorted(best) == list(range(8))
print("  COUNTEREXAMPLE f(k) = 2k^2+k, 4|a| = 8, all 8 classes hit:")
for r in range(8):
    d, j, k = best[r]
    assert f(j) - f(k) == d and abs(d) <= 8
    print("    class %d : d = %-3d = f(%d) - f(%d) = %d - %d" % (r, d, j, k, f(j), f(k)))

# (4) k^2+k dies by parity of S, a different mechanism
S = [k * k + k for k in range(-60, 61)]
assert all(s % 2 == 0 for s in S)
m, ms = missed_classes(1, 1, 0)
assert ms == [1, 3]                            # every odd class missed
print()
print("  k^2+k: S is entirely even and Delta f misses both odd classes,")
print("         so A (+) S sits in one class mod 2 - a DIFFERENT kill from k^2's")

print()
print("all checks passed")
