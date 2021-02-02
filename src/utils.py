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
