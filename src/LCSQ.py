import numpy as np

from utils import parse_fasta


def find_lcs(sequences):
    """Find the longest common subsequence from a list of sequences.
    Using dynamic programming algo : https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

    Args:
        sequences: list of 2 sequences

    Returns:
        the longest common subsequence found
    """
    X, Y = sequences

    #  Build C array
    C = np.zeros(shape=(len(X) + 1, len(Y) + 1), dtype=int)
    for i in range(1, len(C)):
        for j in range(1, len(C[0])):
            if X[i - 1] == Y[j - 1]:
                C[i, j] = C[i - 1, j - 1] + 1
            else:
                C[i, j] = max(C[i, j - 1], C[i - 1, j])

    # Backtrack on C to extract LCS
    lcs = ""
    i, j = len(X), len(Y)
    while i != 0 and j != 0:
        if X[i - 1] == Y[j - 1]:
            lcs += X[i - 1]
            i -= 1
            j -= 1
        else:
            if C[i, j - 1] == C[i - 1, j]:
                if i > 0:
                    i -= 1
                else:
                    j -= 1
            elif C[i, j - 1] > C[i - 1, j]:
                j -= 1
            elif C[i, j - 1] < C[i - 1, j]:
                i -= 1

    return lcs[::-1]


if __name__ == "__main__":
    path = "../data/LCSQ.txt"
    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    fasta_seqs = parse_fasta(data)
    sequences = list(fasta_seqs.values())

    lcs = find_lcs(sequences)
    print(lcs)
