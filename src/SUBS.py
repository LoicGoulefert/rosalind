def find_substring_positions(s, t):
    """Find every index in s where t occurs.

    Args:
        s: string input
        t: motif to search in s

    Returns:
        list of indexes of s where t occurs
    """

    len_t = len(t)
    indexes = []

    for i in range(len(s) - len_t):
        if s[i : i + len_t] == t:
            indexes.append(i + 1)

    return indexes


if __name__ == "__main__":
    path = "../data/SUBS.txt"
    with open(path) as f:
        s, t = [s.strip() for s in f.readlines()]

    indexes = find_substring_positions(s, t)

    print(" ".join(map(str, indexes)))
