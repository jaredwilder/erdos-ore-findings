"""Two new census entries and two restored retractions. Exits 0 or raises."""
from sympy import factorint, primerange, prime
from math import comb


def P(m):
    return max(factorint(m))


def squarefree(m):
    return all(e == 1 for e in factorint(m).values()) if m > 1 else m == 1


# ---- 1. Erdos 386: C(n,2) a product of consecutive primes -------------------
primes = list(primerange(2, 40))
blocks = set()
for i in range(len(primes)):
    p = 1
    for j in range(i, len(primes)):
        p *= primes[j]
        if p > 10 ** 9:
            break
        if j > i:                      # at least two consecutive primes
            blocks.add(p)

hits = [n for n in range(3, 20000) if comb(n, 2) in blocks]
print("Erdos 386, C(n,2) a product of >=2 consecutive primes, n < 20000:")
for n in hits:
    f = sorted(factorint(comb(n, 2)))
    print("  n=%-5d C=%-8d = %s" % (n, comb(n, 2), " * ".join(map(str, f))))
assert hits == [4, 6, 15, 21, 715], hits
assert comb(715, 2) == 255255
assert sorted(factorint(255255)) == [3, 5, 7, 11, 13, 17]
assert all(e == 1 for e in factorint(255255).values())
assert 255255 > 30020, "witness must lie outside the certified block bound"
print("  -> n=715 confirmed; 255255 > 30020, outside the corpus search bound")

# ---- 2. Erdos 932: gaps with >=2 smooth interior integers -------------------
print()
print("Erdos 932, qualifying r with >= 2 interior integers, all prime factors < gap:")
qual = []
for r in range(2, 31):
    a, b = prime(r), prime(r + 1)
    g = b - a
    S = [m for m in range(a + 1, b) if P(m) < g]
    if len(S) >= 2:
        qual.append(r)
        print("  r=%-3d (%d,%d) gap=%-3d witnesses %s" % (r, a, b, g, S))
assert qual == [4, 9, 11, 15, 24, 30], qual
assert P(8) < 4 and P(9) < 4 and P(10) >= 4
print("  -> census is {4,9,11,15,24,30}; the filed {9,11,15,24,30} omits r=4")

# ---- 3. Erdos 383: p=47 restored -------------------------------------------
print()
print("Erdos 383, survivors of P(p^2+1) <= p for p <= 199:")
surv = [p for p in primerange(2, 200) if P(p * p + 1) <= p]
print(" ", surv)
assert 47 * 47 + 1 == 2210
assert sorted(factorint(2210)) == [2, 5, 13, 17]
assert P(2210) == 17 <= 47
assert 2222 != 47 * 47 + 1          # the retraction's number
assert 2222 - 47 * 47 == 13
assert 47 in surv and 191 in surv
assert surv == [7, 41, 43, 47, 73, 83, 157, 173, 191, 193], surv
print("  -> 47^2+1 = 2210 = 2*5*13*17, P = 17 <= 47; the retraction used 2222 = 47^2+13")

# ---- 4. Erdos 11: the depth-7 claim ----------------------------------------
print()
print("Erdos 11, least l with n - 2^l squarefree:")


def least_l(n):
    l = 0
    while 2 ** l < n:
        if squarefree(n - 2 ** l):
            return l
        l += 1
    raise AssertionError("no l for n=%d" % n)


for n in (29, 137, 185):
    l = least_l(n)
    print("  n=%-4d least l = %d  (n - 2^%d = %d)" % (n, l, l, n - 2 ** l))
assert least_l(185) == 1 and squarefree(183) and 183 == 3 * 61
assert least_l(137) == 2 and squarefree(133) and 133 == 7 * 19
assert least_l(29) == 3
assert max(least_l(n) for n in range(3, 128, 2)) == 3
assert [n for n in range(3, 128, 2) if least_l(n) == 3] == [29]
print("  -> 185 and 137 are depth 1 and 2; 29 is the unique depth-3 case below 127")

print()
print("all four verified")
