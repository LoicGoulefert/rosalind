def hamming_distance(s, t):
    """Compute the hamming distance between 2 strings.

    Args:
        s, t: strings

    Returns:
        difference count between s and t
    """
    if len(s) != len(t):
        raise ValueError(
            f"s and t must be of equal length. Got lengths {len(s)} and {len(t)}"
        )

    count = 0
    for a, b in zip(s, t):
        if a != b:
            count += 1

    return count


if __name__ == "__main__":
    path = "../data/HAMM.txt"
    with open(path) as f:
        s, t = [s.strip() for s in f.readlines()]

    print(hamming_distance(s, t))
