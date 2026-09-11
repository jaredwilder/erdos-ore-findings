from math import factorial, gcd, prod


def tail_product(n: int, m: int) -> int:
    return prod(range(n + 1, m + 1))


def main() -> None:
    # Small explicit counterexample.
    assert factorial(4) - 1 == 23
    assert factorial(8) - 1 == 40319
    assert 40319 == 23 * 1753
    assert gcd(factorial(4) - 1, factorial(8) - 1) == 23

    # Exact repaired identity on a broad finite regression window.
    for n in range(2, 13):
        for m in range(n + 1, 18):
            lhs = gcd(factorial(n) - 1, factorial(m) - 1)
            rhs = gcd(factorial(n) - 1, tail_product(n, m) - 1)
            assert lhs == rhs, (n, m, lhs, rhs)

    expected = {
        (4, 8, 23),
        (4, 11, 23),
        (5, 11, 17),
        (5, 15, 17),
        (8, 11, 23),
        (11, 15, 17),
    }
    found = set()
    for n in range(2, 15):
        for m in range(n + 1, 20):
            g = gcd(factorial(n) - 1, factorial(m) - 1)
            if g > 1:
                found.add((n, m, g))
    assert expected <= found

    print("Semantic Court 12: PASS")


if __name__ == "__main__":
    main()
