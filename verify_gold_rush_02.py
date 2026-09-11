from math import gcd, isqrt

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def sigma(n):
    total = 0
    r = isqrt(n)
    for d in range(1, r+1):
        if n % d == 0:
            total += d
            q = n//d
            if q != d: total += q
    return total

def vp_factorial(n,p):
    s = 0
    while n:
        n //= p
        s += n
    return s

# 949

def sum_free(S):
    return all(x+y not in S for x in S for y in S)
assert not any(sum_free({i+1 for i in range(10) if mask>>i & 1}) and all((q in {i+1 for i in range(10) if mask>>i & 1} or 2*q in {i+1 for i in range(10) if mask>>i & 1}) for q in range(1,6)) for mask in range(1<<10))
assert sum_free({1,4,6})
assert all((q in {1,4,6} or 2*q in {1,4,6}) for q in range(1,5))

# 479
primes = [p for p in range(3,200) if is_prime(p)]
for j in range(8):
    e=2**j
    for p in primes:
        n=e*p
        assert (pow(2,n,n)-pow(2,e,n)) % n == 0

# 727
for p in primes:
    if p >= 7:
        n=2*p-2
        assert 2*vp_factorial(n+2,p) == 4
        assert vp_factorial(2*n,p) == 3

# 887
for m in range(2,10001):
    N=m*(m-1)*(m+1)*(m+2)
    d1=m*(m+1); d2=m*(m+2)
    assert N % d1 == 0 and N % d2 == 0
    assert d1*d1 > N and d2*d2 > N
    assert (m+2)**4 <= 16*N

# 1061
for a in range(1,5001):
    if gcd(a,6)==1:
        assert sigma(a)+sigma(2*a)==sigma(3*a)

print('Gold Rush 02 regression checks: PASS')
