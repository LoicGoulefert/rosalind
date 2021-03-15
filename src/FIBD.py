def fibd(n, m):
    """Compute number of rabbit pairs alive after n months,
    if a rabbit pair lives for m months.

    Args:
        n: int, total number of months
        m: int, lifespan of a rabbit

    Returns:
        number of rabbit pairs alive after n months
    """

    rabbits = [0] * m
    rabbits[-1] = 1

    for _ in range(1, n):
        offsprings = sum(rabbits[:-1])
        rabbits[:-1] = rabbits[1:]
        rabbits[-1] = offsprings

    return sum(rabbits)


if __name__ == "__main__":
    path = "../data/FIBD.txt"
    with open(path) as f:
        n, m = map(int, f.read().split(" "))

    print(fibd(n, m))
