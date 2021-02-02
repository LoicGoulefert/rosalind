from utils import build_inverse_codon_table


def mRNA_count(protein, table):
    """Count the number of possible mRNA chains that could translate
    into the input protein.

    Args:
        protein: amino acid chain
        table: inverse codon table

    Returns:
        count of mRNA chains that could translate into protein
    """
    count = len(table[protein[0]])

    for acid in protein[1:]:
        count *= len(table[acid])

    # Taking into account the different codons that can be used to stop
    count *= len(table["Stop"])

    return count


if __name__ == "__main__":
    path = "../data/MRNA.txt"
    with open(path) as f:
        protein = f.read().strip()

    table = build_inverse_codon_table("../data/RNA_codon_table.txt")
    count = mRNA_count(protein, table)

    # Python3.7 automatically handles big int (>32bits) conversion
    print(count % 1000000)
