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


def compute_GC(sequences):
    """
    Args:
        sequences: dict of sequences

    Returns:
        a dict with key: sequence name and value: GC content
    """
    res = {}

    for name in sequences:
        sequence = sequences[name]
        gc_content = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
        res[name] = round(gc_content, 4)

    return res


if __name__ == "__main__":
    path = "../data/GC.txt"

    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    sequences = parse_fasta(data)
    gc_contents = compute_GC(sequences)

    max_key = max(gc_contents, key=gc_contents.get)
    print(max_key)
    print(gc_contents[max_key])
