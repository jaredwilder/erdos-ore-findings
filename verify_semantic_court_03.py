"""Exact regression checks for the finite arithmetic in SEMANTIC_COURT_03.md.

Semantic/literature corrections (#749, #653, #124 source reconciliation) are
not reducible to these checks. This file pins the cheap arithmetic falsifiers.
"""
from math import isqrt


def is_squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


# Erdős 155: A={1,2} is Sidon, but A union 3A is not.
A = {1, 2}
B = A | {3 * a for a in A}
assert B == {1, 2, 3, 6}
assert 1 + 3 == 2 + 2 == 4

# Erdős 145: exact squarefree gap 241 -> 246 has length 5.
assert is_squarefree(241)
assert is_squarefree(246)
for n in range(242, 246):
    assert not is_squarefree(n), n
assert 246 - 241 == 5

# Erdős 124: the corrupted frozen hypothesis is impossible under
# 3 <= d1 < ... < dr, since dr >= r+2.
for r in range(1, 1000):
    dr_min = r + 2
    assert r / (dr_min - 1) < 1

# Erdős 653: a regular polygon can have a one-valued R-profile, but this
# is only a value for one configuration. The following tiny extremum toy
# is a generic regression against the logical mistake:
# max{1,3} is not <= 1 merely because one competitor has value 1.
assert max(1, 3) == 3
assert not (max(1, 3) <= 1)

# Erdős 749: bounded L2 average does not imply a uniform L-infinity bound.
# This finite family has mean square < 2 while its max grows arbitrarily.
for M in [10, 100, 1000]:
    x = [0] * (M * M) + [M]
    mean_square = sum(v * v for v in x) / len(x)
    assert mean_square < 1.0
    assert max(x) == M

print("Semantic Court 03 regression checks: PASS")
