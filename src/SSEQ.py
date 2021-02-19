from utils import parse_fasta


def find_spliced_motif(sequence, motif):
    """Find the indexes of a spliced motif inside a sequence.

    Args:
        sequence: string
        motif: string, spliced motif we're looking for in sequence

    Returns:
        a list of indexes of where the motif is within sequence
    """
    motif_index = 0
    indexes = []

    for i, aa in enumerate(sequence):
        if aa == motif[motif_index]:
            indexes.append(i + 1)
            motif_index += 1

            if motif_index == len(motif):
                break

    return indexes


if __name__ == "__main__":
    path = "../data/SSEQ.txt"
    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    fasta_seqs = parse_fasta(data)

    _, sequence = max(fasta_seqs.items(), key=lambda x: len(x[1]))
    _, motif = min(fasta_seqs.items(), key=lambda x: len(x[1]))

    indexes = find_spliced_motif(sequence, motif)

    print(" ".join(map(str, indexes)))
