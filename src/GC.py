from utils import parse_fasta


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
