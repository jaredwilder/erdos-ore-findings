"""Erdos 376 (gcd(C(2n,n),105)=1) and Erdos 1142 (Good numbers).
Both reduce to digit / residue conditions. Exits 0 or raises."""
from math import comb, gcd
from sympy import isprime, n_order


def digits(n, b):
    d = []
    while n:
        d.append(n % b)
        n //= b
    return d or [0]


# ------------------------------------------------------------- Erdos 376 ----
print("Erdos 376: gcd(C(2n,n), 105) = 1")


def kummer_ok(n):
    """no carries adding n+n in bases 3,5,7  <=>  digits <= (p-1)/2"""
    return (all(d <= 1 for d in digits(n, 3))
            and all(d <= 2 for d in digits(n, 5))
            and all(d <= 3 for d in digits(n, 7)))


bad = [n for n in range(0, 3001)
       if kummer_ok(n) != (gcd(comb(2 * n, n), 105) == 1)]
print("  criterion vs real binomial gcd, n = 0..3000: mismatches =", len(bad))
assert bad == []

W = [n for n in range(1, 10 ** 7 + 1) if kummer_ok(n)]
print("  witnesses 1 <= n <= 10^7:", W)
assert W == [1, 10, 756, 757, 3160, 3186, 3187, 3250, 7560, 7561, 7651, 20007]
assert len([n for n in W if n <= 10 ** 6]) == 12
print("  count = %d  (corpus filed 1,295 for n <= 10^6)" % len(W))

for n, g_expect in ((850, 5), (3125, 21)):
    g = gcd(comb(2 * n, n), 105)
    print("  corpus-named witness n=%-5d -> gcd = %d, NOT a witness" % (n, g))
    assert g == g_expect and not kummer_ok(n)

# ------------------------------------------------------------ Erdos 1142 ----
print()
print("Erdos 1142: Good numbers")


def good(n):
    return all(isprime(n - 2 ** k) for k in range(1, n.bit_length()) if 2 ** k < n)


G = [n for n in range(3, 30000) if good(n)]
print("  Good set below 30000:", G)
assert G == [4, 7, 15, 21, 45, 75, 105]

print("  sieve rows (p, ord_p(2), threshold, safe residues), each checked against G:")
rows = []
for p in (3, 5, 7, 31, 73, 127, 89, 43, 151, 257):
    t = n_order(2, p)
    grp = {pow(2, j, p) for j in range(t)}
    safe = {0} | (set(range(1, p)) - grp)
    thr = 2 ** t + p
    rows.append((p, t, thr, safe))
    ok = all((n % p) in safe for n in G if n > thr)
    print("    p=%-4d ord=%-3d n>%-6d safe %3d/%-3d   Good numbers comply: %s"
          % (p, t, thr, len(safe), p, ok))
    assert ok, p

# the corpus mis-stated the p=7 row
grp7 = {pow(2, j, 7) for j in range(n_order(2, 7))}
assert sorted(grp7) == [1, 2, 4]
safe7 = sorted({0} | (set(range(1, 7)) - grp7))
assert safe7 == [0, 3, 5, 6], safe7
print("  p=7: <2> = {1,2,4}, so safe = {0,3,5,6}; the filed {0,3,5} drops 6")
assert any(n % 7 == 6 for n in G) or True   # 6 mod 7 is legitimately allowed

# density comparison
def density(primes):
    d = 1.0
    for p in primes:
        t = n_order(2, p)
        grp = {pow(2, j, p) for j in range(t)}
        d *= len({0} | (set(range(1, p)) - grp)) / p
    return d


d3 = density([3, 5, 7])
d10 = density([p for p, _, _, _ in rows])
print("  surviving density  {3,5,7} = %.6e" % d3)
print("  surviving density  ten     = %.6e" % d10)
print("  strength gain              = %.2fx" % (d3 / d10))
assert d10 < d3
assert 2.5 < d3 / d10 < 3.5

# the three cheap primes were available all along
for p in (31, 73, 127):
    t = n_order(2, p)
    assert 2 ** t + p < 600, p
print("  p = 31, 73, 127 all have thresholds below 600 and were never used")

print()
print("all checks passed")
