from itertools import combinations

from utils import parse_fasta


def find_lcs(fasta_seqs):
    """Find the longest common substring.

    Args:
        fasta_seqs: a dict of sequences

    Returns:
        The longest common substring among the given sequences
    """
    #  find min length sequence and it's name
    min_name, min_seq = min(fasta_seqs.items(), key=lambda x: len(x[1]))

    # Build every substring from the shortest sequence (length 2 minimum)
    # Sort them by length and remove duplicates
    substrings = sorted(
        list(
            set(
                [
                    min_seq[x:y]
                    for x, y in combinations(range(len(min_seq) + 1), r=2)
                    if len(min_seq[x:y]) > 1
                ]
            )
        ),
        key=len,
    )

    sequence_list = list(fasta_seqs.values())
    sequence_list.remove(min_seq)

    #  Search for the LCS
    LCS = ""
    for substring in substrings:
        is_common = all(substring in seq for seq in sequence_list)
        if is_common and len(substring) > len(LCS):
            LCS = substring

    return LCS


if __name__ == "__main__":
    path = "../data/LCSM.txt"
    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    fasta_seqs = parse_fasta(data)
    print(find_lcs(fasta_seqs))
