"""
Utils functions reused in Rosalind problems.
"""


def parse_fasta(data):
    """
    Args:
        data: fasta input as a list of lines

    Returns:
        a dict with key = sequence name and value = sequence
    """
    res = {}

    for i, line in enumerate(data):
        if line[0] == ">":
            key = line[1:]
            value = ""
            for sub_seq in data[i + 1 :]:
                if sub_seq[0] == ">":
                    break
                value += sub_seq
            res[key] = value

    return res


def build_codon_table(path):
    """Build the codon table as a dict.

    Args:
        path: the path to the codon table file

    Returns:
        a dict with key: codon and value: corresponding protein amino acid
    """

    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    table = {}

    for line in data:
        key, value = line.split(" ")
        table[key] = value

    return table


def build_inverse_codon_table(path):
    """Build the inverse codon table as a dict.

    Args:
        path: the path to the codon table file

    Returns:
        a dict with key: protein amino acid and value: list of corresponding codons
    """

    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    table = {}

    for line in data:
        value, key = line.split(" ")
        if key in table:
            table[key] += [value]
        else:
            table[key] = [value]

    return table
