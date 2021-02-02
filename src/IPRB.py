import operator as op
from functools import reduce


def ncr(n, r):
    """N choose R.
    Args:
        n: total to choose from
        r: amount to choose from n

    Returns:
        n! / (k! * (n - k)!)
    """
    r = min(r, n - r)

    if r < 0:
        raise ValueError("r must be smaller or equal to n")

    num = reduce(op.mul, range(n, n - r, -1), 1)
    denum = reduce(op.mul, range(1, r + 1), 1)

    return num // denum


if __name__ == "__main__":
    path = "../data/IPRB.txt"

    with open(path) as f:
        k, m, n = map(int, f.read().split(" "))

    children_count = ncr(k + m + n, 2)
    rec_children_count = ncr(n, 2) + 0.5 * m * n + 0.25 * ncr(m, 2)
    p_dominant = 1 - rec_children_count / children_count

    print(round(p_dominant, 5))
    print(ncr(2, 3))