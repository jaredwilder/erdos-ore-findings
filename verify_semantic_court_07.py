def t_k(n, k):
    m = 1
    while True:
        prod = 1
        for j in range(k):
            prod *= m + j
        if prod % n == 0:
            return m
        m += 1

# The two false refutations.
assert t_k(4, 2) == 3
assert t_k(2, 2) == 1 == 2 - 1

# Regression for the general prime-window theorem.
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for k in range(1, 8):
    for p in primes:
        if p > k:
            assert t_k(p, k) == p - k + 1, (p, k, t_k(p, k))

print('Semantic Court 07 checks: PASS')
