import numpy as np

from utils import parse_fasta


def compute_profile(sequences):
    """Compute profile matrix of sequence list.

    Args:
        sequences: a list of DNA sequences

    Returns:
        profile of the sequence list
    """

    num_seqs = len(sequences)
    len_seq = len(sequences[0])
    joint_seqs = "".join(sequences)
    matrix_seqs = np.array(list(joint_seqs)).reshape((num_seqs, -1))
    profile = np.zeros((4, len_seq), dtype=np.uint)

    for i, base in enumerate(["A", "C", "G", "T"]):
        for j in range(len_seq):
            profile[i, j] = list(matrix_seqs[:, j]).count(base)

    return profile


def compute_consensus(profile):
    """Compute consensus from a profile matrix.

    Args:
        profile: 4 x len_sequence matrix

    Returns:
        string corresponding to the profile's consensus
    """

    profile_table = {0: "A", 1: "C", 2: "G", 3: "T"}
    consensus = ""

    for i in range(len(profile[0])):
        consensus += profile_table[np.argmax(profile[:, i])]

    return consensus


if __name__ == "__main__":
    path = "../data/CONS.txt"
    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    fasta_seqs = parse_fasta(data)
    sequences = list(fasta_seqs.values())

    profile = compute_profile(sequences)
    consensus = compute_consensus(profile)

    print(consensus)
    for base, line in zip(["A", "C", "G", "T"], profile):
        print(f"{base}: {' '.join(map(str, line))}")
