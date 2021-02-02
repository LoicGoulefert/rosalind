from utils import parse_fasta


def build_adjacency_list(sequences, k):
    """Build adjacency list from a list of sequences.

    Args:
        sequences: fasta dict of sequences
        k: size of suffix / prefix to look for

    Returns:
        Adjacency list
    """
    seq_len = len(next(iter(sequences.values())))
    if k > seq_len:
        raise ValueError(
            f"k must be smaller than the sequences length. Got k = {k}, len(sequence)={seq_len}."
        )

    adjacency_list = []

    for name in sequences:
        for other in sequences:
            if other != name:
                if sequences[name][-k:] == sequences[other][:k]:
                    adjacency_list.append((name, other))

    return adjacency_list


if __name__ == "__main__":
    path = "../data/GRPH.txt"
    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    sequences = parse_fasta(data)
    adj_list = build_adjacency_list(sequences, 3)

    for el in adj_list:
        print(" ".join(el))
