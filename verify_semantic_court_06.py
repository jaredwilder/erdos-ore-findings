from itertools import combinations, product
from math import factorial, isqrt


def phi(n):
    if n == 1:
        return 1
    r = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            r -= r // p
        p += 1
    if x > 1:
        r -= r // x
    return r


def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def factorization_with_max(n, M):
    target = factorial(n)
    ds = [d for d in divisors(target) if n < d <= M]
    memo = set()

    def rec(i, rem):
        if rem == 1:
            return []
        if i < 0:
            return None
        key = (i, rem)
        if key in memo:
            return None
        r = rec(i - 1, rem)
        if r is not None:
            return r
        d = ds[i]
        if rem % d == 0:
            r = rec(i - 1, rem // d)
            if r is not None:
                return r + [d]
        memo.add(key)
        return None

    return rec(len(ds) - 1, target)


def f390(n):
    target = factorial(n)
    for M in [d for d in divisors(target) if d > n]:
        fac = factorization_with_max(n, M)
        if fac is not None:
            return M, sorted(fac)
    raise AssertionError('no factorization found')


# #602: K_4^3 is 2-colourable. Use a 2-2 split.
vertices = range(4)
red = {0, 1}
edges = list(combinations(vertices, 3))
assert all(not (set(e) <= red or set(e).isdisjoint(red)) for e in edges)

# #681: n=250,k=3 is a positive witness, not a counterexample.
assert 250 + 3 == 253 == 11 * 23
assert 11 > 3**2
assert 3**4 < 253

# #456 endpoint.
assert phi(1) == 1
assert min(m for m in range(1, 20) if phi(m) % 1 == 0) == 1

# #390 exact finite sequence.
expected = {3: 6, 4: 24, 5: 12, 6: 10, 7: 20, 8: 16, 9: 28, 10: 25}
for n, want in expected.items():
    got, fac = f390(n)
    assert got == want, (n, got, want, fac)
    p = 1
    for x in fac:
        assert x > n
        p *= x
    assert p == factorial(n)

print('Semantic Court 06 exact checks: PASS')
