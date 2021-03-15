from operator import gt, lt


def LIS(seq, op=lt):
    """Find the Longest Increasing (or Decreasing) Subsequence.

    Args:
        seq: list of integers
        op: function, operation to perform. lt (lower than, default) yields
        the LIS, and gt (greater than) yields the LDS.

    Returns:
        the LIS (or LDS) found, as a list
    """
    L = [1] * len(seq)
    prev = [-1] * len(seq)

    #  Find LIS indices
    for i in range(len(L)):
        for j in range(i):
            if op(seq[j], seq[i]) and L[i] < L[j] + 1:
                L[i] = L[j] + 1
                prev[i] = j

    len_lis = max(L)
    pos = L.index(len_lis)

    # Restoring LIS
    lis_seq = []
    while pos != -1:
        lis_seq.append(seq[pos])
        pos = prev[pos]

    return lis_seq[::-1]


if __name__ == "__main__":
    path = "../data/LGIS.txt"
    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    n = int(data[0])
    seq = list(map(int, data[1].split(" ")))

    lis = LIS(seq)
    lds = LIS(seq, op=gt)

    print(" ".join(map(str, lis)))
    print()
    print(" ".join(map(str, lds)))
