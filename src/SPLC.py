from utils import build_codon_table, parse_fasta, transcribe, rna_to_protein


def extract_exons(sequence, introns):
    """Extract exons from a sequence.

    Args:
        sequence: the original dna sequence
        introns: the introns we're deleting from sequence

    Returns:
        the original sequence with its introns filtered out
    """

    res = sequence

    for intron in introns:
        res = res.replace(intron, "")

    return res


if __name__ == "__main__":
    path = "../data/SPLC.txt"
    with open(path) as f:
        data = [s.strip() for s in f.readlines()]

    fasta_seqs = parse_fasta(data)
    codon_table = build_codon_table("../data/RNA_codon_table.txt")

    #  find max length sequence
    _, sequence = max(fasta_seqs.items(), key=lambda x: len(x[1]))

    #  get introns
    introns = list(fasta_seqs.values())
    introns.remove(sequence)

    introns_seq = extract_exons(sequence, introns)
    rna = transcribe(introns_seq)
    protein = rna_to_protein(rna, codon_table)

    print(protein)
