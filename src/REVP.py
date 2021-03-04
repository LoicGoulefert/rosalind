from utils import parse_fasta, reverse_complement


def find_reverse_palindromes(sequence):
    """Find every reverse palindromes of size >= 4, <= 12 and
    return their indices and associated length within a sequence.

    Args:
        sequence: string, dna sequence

    Returns:
        list of starting indices and length of each reverse palindrome
        found
    """
    output = []

    for i in range(len(sequence)):
        for j in range(4, 13):
            if i + j > len(sequence):
                continue

            subseq = sequence[i : i + j]
            rc = reverse_complement(subseq)

            if subseq == rc:
                output.append((i + 1, j))

    return output


if __name__ == "__main__":
    path = "../data/REVP.txt"
    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    fasta_seqs = parse_fasta(data)
    sequence = list(fasta_seqs.values())[0]

    output = find_reverse_palindromes(sequence)

    for o in output:
        print(f"{o[0]} {o[1]}")
