"""Six rows filed PROVED in the Erdos ore that recomputation refutes.
Exits 0 or raises."""
from itertools import combinations, product
from fractions import Fraction as F
from math import comb, log
from sympy import isprime, factorint, lcm

V = range(6)
E = list(combinations(V, 2))

# ------------------------------------------------- 1. ex(6, K_{2,2,2}) ------
print("1. ex(6, K_222)")


def is_matching(edges):
    seen = set()
    for a, b in edges:
        if a in seen or b in seen:
            return False
        seen.update((a, b))
    return True


best, ext = -1, []
for mask in range(1 << 15):
    comp = [e for i, e in enumerate(E) if not (mask >> i) & 1]
    if is_matching(comp):          # complement is a matching => contains K_222
        continue
    k = bin(mask).count("1")
    if k > best:
        best, ext = k, [mask]
    elif k == best:
        ext.append(mask)
print("   exhaustive over 2^15 graphs: ex =", best, " extremizers =", len(ext))
assert best == 13
assert len(ext) == 60 == 6 * comb(5, 2)
# every extremizer's complement is a 2-edge path
for mask in ext:
    comp = [e for i, e in enumerate(E) if not (mask >> i) & 1]
    assert len(comp) == 2 and not is_matching(comp)
print("   every extremizer is K_6 minus a P_3")


def alpha(edges):
    b = 0
    for r in range(7):
        for S in combinations(V, r):
            if all(not (a in S and c in S) for a, c in edges):
                b = max(b, r)
    return b


k6_minus_k3 = [e for e in E if e not in {(0, 1), (0, 2), (1, 2)}]
print("   alpha(K_6 - K_3) =", alpha(k6_minus_k3), "(corpus filed 2)")
assert alpha(k6_minus_k3) == 3

# ----------------------------------------------------- 2. Erdos 317 --------
print()
print("2. Erdos 317: m*(n)")
for n, want in ((7, 4), (8, 7)):
    L = int(lcm(list(range(1, n + 1))))
    best_s = None
    for d in product([-1, 0, 1], repeat=n):
        if not any(d):
            continue
        s = sum(d[k - 1] * L // k for k in range(1, n + 1))
        if s and (best_s is None or abs(s) < abs(best_s[0])):
            best_s = (s, d)
    s, d = best_s
    val = sum(F(d[k - 1], k) for k in range(1, n + 1))
    print("   n=%d  m*=%d  witness sums to %s" % (n, abs(s), val))
    assert abs(s) == want
    assert abs(val) == F(want, L)
print("   filed (.,.,.,.,.,.,10,15) -> true (.,.,.,.,.,.,4,7)")

# ----------------------------------------------------- 3. Erdos 295 --------
print()
print("3. Erdos 295: k(4)")
pre = sum(F(1, x) for x in (4, 5, 6, 7, 8, 9))
assert pre == F(2509, 2520) < 1
tot = sum(F(1, x) for x in (4, 5, 6, 7, 8, 9, 230, 57960))
assert tot == 1
print("   six-term prefix = %s < 1  => k(4) >= 7" % pre)
print("   eight-term set sums to exactly 1 => k(4) <= 8")
bad = sum(F(1, x) for x in (4, 5, 6, 7, 8, 9, 230))
assert bad == F(57959, 57960) != 1
print("   the filed k0(4)=6 witness has 7 terms and sums to %s" % bad)

# ----------------------------------------------------- 4. Erdos 479 --------
print()
print("4. Erdos 479: 2^n = 2 mod n")
psp = [n for n in range(3, 2001) if pow(2, n, n) == 2 and not isprime(n)]
print("   composite n <= 2000 satisfying it:", psp)
assert psp == [341, 561, 645, 1105, 1387, 1729, 1905]
assert 341 == 11 * 31
# the other half does hold
assert [n for n in range(2, 2001) if pow(2, n, n) == 0] == [2 ** m for m in range(1, 11)]
print("   the 2^n = 0 mod n  <=>  n = 2^m half holds")

# ----------------------------------------------------- 5. Erdos 156 --------
print()
print("5. Erdos 156: minimum maximal Sidon set in [1,8]")


def sidon(A):
    d = set()
    for a, b in combinations(sorted(A), 2):
        if b - a in d:
            return False
        d.add(b - a)
    return True


A = {1, 4, 5}
assert sidon(A)
ext8 = [x for x in range(1, 9) if x not in A and sidon(A | {x})]
print("   {1,4,5} is Sidon; extensions in [1,8]:", ext8)
assert ext8 == []
print("   maximal at size 3; corpus filed 4")

# ----------------------------------------------------- 6. Erdos 683 --------
print()
print("6. Erdos 683: which pairs actually constrain c")


def P(m):
    return max(factorint(m))


for (n, k) in ((10, 5), (14, 7)):
    c = comb(n, k)
    assert P(c) >= n - k + 1
    print("   filed (%d,%d): P=%d >= n-k+1=%d  -> not binding" % (n, k, P(c), n - k + 1))

best = None
for n in range(4, 161):
    for k in range(2, n // 2 + 1):
        c = comb(n, k)
        p = P(c)
        if p < n - k + 1 and p > k:
            v = log(p) / log(k) - 1
            if best is None or v < best[0]:
                best = (v, n, k, p)
v, n, k, p = best
print("   tightest binding pair (%d,%d): P=%d, c <= log_%d(%d) - 1 = %.7f" % (n, k, p, k, p, v))
assert (n, k, p) == (10, 3, 5)
assert abs(v - (log(5) / log(3) - 1)) < 1e-12

print()
print("all six refutations verified")
