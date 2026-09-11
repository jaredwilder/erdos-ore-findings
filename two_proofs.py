"""Erdos 1052 (no odd unitary perfect number) and Erdos 891 (Omega > k in
primorial windows). Both are proofs; this script only checks the instances
quoted in the write-up. Exits 0 or raises."""
from math import gcd
from sympy import factorint, primerange


def Omega(n):
    return sum(factorint(n).values()) if n > 1 else 0


def omega(n):
    return len(factorint(n)) if n > 1 else 0


def sigma_star(n):
    s = 1
    for p, a in factorint(n).items():
        s *= 1 + p ** a
    return s


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


# ---- Erdos 1052 -------------------------------------------------------------
print("Erdos 1052: no odd unitary perfect number")
odd_hits = [n for n in range(1, 200000, 2) if sigma_star(n) == 2 * n]
print("  odd n < 200000 with sigma*(n) = 2n:", odd_hits)
assert odd_hits == []

even_hits = [n for n in range(1, 1000001) if sigma_star(n) == 2 * n]
print("  unitary perfect n <= 10^6:", even_hits)
assert even_hits == [6, 60, 90, 87360]

# the divisibility the proof turns on
print("  v2(sigma*(n)) >= omega(n) for odd n:")
for n in (3, 9, 15, 105, 1155, 45045):
    print("    n=%-6d omega=%d sigma*=%-8d v2=%d" %
          (n, omega(n), sigma_star(n), v2(sigma_star(n))))
    assert v2(sigma_star(n)) >= omega(n)
for n in range(1, 20000, 2):
    assert v2(sigma_star(n)) >= omega(n), n
print("  -> holds for every odd n < 20000, as the proof requires")

# unitary divisors of 6 sum to 12 = 2*6
ud = [d for d in range(1, 7) if 6 % d == 0 and gcd(d, 6 // d) == 1]
assert ud == [1, 2, 3, 6] and sum(ud) == 12 == sigma_star(6)

# ---- Erdos 891 --------------------------------------------------------------
print()
print("Erdos 891: Omega > k in every window of length P_k")

P = 1
prims = []
for k, p in enumerate(primerange(2, 60), 1):
    P *= p
    prims.append(P)
    if k > 12:
        break
for k in range(1, 13):
    assert prims[k - 1] >= 2 ** k, k
print("  P_k >= 2^k verified for k = 1..12")

Pk = {2: 6, 3: 30, 4: 210}
expected = {2: [1, 2], 3: [], 4: []}
for k in (2, 3, 4):
    bad = [n for n in range(1, 4000)
           if not any(Omega(m) >= k + 1 for m in range(n, n + Pk[k]))]
    print("  k=%d  exceptional set for n < 4000: %s" % (k, bad))
    assert bad == expected[k], (k, bad)

# the proof's own construction: the multiple of 2^k inside the window
for k in (2, 3, 4):
    for n in range(2 ** k + 1, 2 ** k + 500):
        m = ((n + 2 ** k - 1) // 2 ** k) * 2 ** k     # least multiple of 2^k >= n
        assert n <= m < n + Pk[k]
        assert m // 2 ** k >= 2
        assert Omega(m) >= k + 1
print("  -> the constructed witness t*2^k works for every n > 2^k tested")

# ---- the omega reading does NOT follow --------------------------------------
print()
print("  SCOPE: the omega (distinct primes) reading is a different statement.")
w = [n for n in range(1, 200) if not any(omega(m) >= 3 for m in range(n, n + 6))]
print("  k=2, n<200 with no m in [n,n+6) having omega(m)>=3:")
print("   ", w)
assert 157 in w and 159 in w and len(w) == 57
assert omega(2 ** 10) == 1 and Omega(2 ** 10) == 10
print("  -> Omega holds from n=3; omega still fails at n=159")

print()
print("all checks passed")
