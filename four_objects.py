"""Four explicit objects from the Erdos ore. Exits 0 or raises."""
from itertools import combinations
from sympy import factorint


def powerful(n):
    return n > 0 and all(e >= 2 for e in factorint(n).values())


def exps(n):
    return list(factorint(n).values())


# ------------------------------------------------------------ Erdos 137 ----
print("Erdos 137: three consecutive powerful numbers in AP")
T = (1728, 1764, 1800)
for t in T:
    assert powerful(t), t
    print("   %-5d = %-22s powerful" % (t, factorint(t)))
assert T[1] - T[0] == T[2] - T[1] == 36
assert [m for m in range(T[0] + 1, T[1]) if powerful(m)] == []
assert [m for m in range(T[1] + 1, T[2]) if powerful(m)] == []
print("   common difference 36, and nothing powerful lies between them")

starts, cur, best = [], 0, 0
for n in range(1, 10 ** 6):
    if powerful(n):
        cur += 1
        best = max(best, cur)
    else:
        if cur >= 2:
            starts.append(n - cur)
        cur = 0
assert best == 2
assert starts[:4] == [8, 288, 675, 9800]
print("   longest run of consecutive INTEGERS all powerful, below 10^6:", best)

# ----------------------------------------------------------- Erdos 1107 ----
print()
print("Erdos 1107: integers not a sum of at most 3 powerful numbers")
P = [n for n in range(1, 200) if powerful(n)]


def rep3(n):
    for a in P:
        if a > n:
            break
        if a == n:
            return (a,)
        for b in P:
            if a + b > n:
                break
            if a + b == n:
                return (a, b)
            for c in P:
                if a + b + c > n:
                    break
                if a + b + c == n:
                    return (a, b, c)
    return None


gaps = [n for n in range(1, 100) if rep3(n) is None]
print("   gaps below 100:", gaps)
assert gaps == [7, 15, 23, 87]
assert all(g % 8 == 7 for g in gaps)
# but the congruence is NOT an obstruction class
r31 = rep3(31)
assert 31 % 8 == 7 and r31 is not None
assert sorted(r31) == [4, 27] and powerful(4) and powerful(27)
print("   31 = 4 + 27 is 7 mod 8 yet representable => the congruence is not an obstruction")

# ------------------------------------------------------------ Erdos 949 ----
print()
print("Erdos 949: q <= 5 always works, and 5 is sharp")


def sumfree(S):
    return all(a + b not in S for a in S for b in S)


S = {1, 4, 6}
assert sumfree(S)
assert sorted({a + b for a in S for b in S}) == [2, 5, 7, 8, 10, 12]
for q in range(1, 5):
    assert (q in S) or (2 * q in S), q
assert 5 not in S and 10 not in S
print("   S={1,4,6} is sum-free; q=1..4 all blocked, q=5 free => 5 is sharp")

bad = []
for r in range(0, 11):
    for T2 in combinations(range(1, 11), r):
        Ts = set(T2)
        if sumfree(Ts) and not any(q not in Ts and 2 * q not in Ts for q in range(1, 6)):
            bad.append(Ts)
assert bad == []
print("   no sum-free subset of [1,10] blocks all of q=1..5")

# ------------------------------------------------------------ Erdos 913 ----
print()
print("Erdos 913: distinct exponents in n(n+1)")


def distinct_exponents(n):
    e = exps(n) + exps(n + 1)
    return len(set(e)) == len(e)


assert factorint(57121) == {239: 2}
assert factorint(57122) == {2: 1, 13: 4}
assert distinct_exponents(57121)
print("   57121 = 239^2, 57122 = 2*13^4, exponent multiset {2,1,4} distinct")

W = [n for n in range(1, 100000) if distinct_exponents(n)]
assert len(W) == 140
assert W[:9] == [1, 3, 4, 7, 8, 16, 24, 27, 31]
print("   witnesses below 10^5:", len(W))

# the Pell object is NOT a distinct-exponent witness
assert 8119 ** 2 - 2 * 5741 ** 2 == -1
assert 8119 ** 2 == 65918161 and 8119 == 23 * 353
assert factorint(65918161) == {23: 2, 353: 2}
assert factorint(65918162) == {2: 1, 5741: 2}
assert not distinct_exponents(65918161)
allexp = exps(65918161) + exps(65918162)
assert sorted(allexp) == [1, 2, 2, 2]
assert sum(1 for e in allexp if e == 1) == 1
print("   8119^2 - 2*5741^2 = -1 holds, but 65918161 has exponents {2,2,1,2}")
print("   -> not a distinct-exponent witness; it has exactly ONE unit exponent")

print()
print("all four verified")
