from utils import parse_fasta


def transition_transversion_ratio(sequences):
    """Compute the transition / transversion ratio between 2 sequences.

    Args:
        sequences: list of 2 sequences

    Returns:
        the transition / transversion ratio
    """
    transitions, transversions = 0, 0

    for a1, a2 in zip(*sequences):
        if a1 != a2:
            #  Transition
            if a1 in "AG" and a2 in "AG" or a1 in "CT" and a2 in "CT":
                transitions += 1
            # Transversion
            else:
                transversions += 1

    return transitions / transversions


if __name__ == "__main__":
    path = "../data/TRAN.txt"

    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    fasta_seqs = parse_fasta(data)
    sequences = list(fasta_seqs.values())

    print(transition_transversion_ratio(sequences))
