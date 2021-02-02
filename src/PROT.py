from utils import build_codon_table


def rna_to_protein(rna, codon_table):
    """Translate RNA strand into a chain of amino acids."""

    if rna[:3] != "AUG":
        raise ValueError(f"rna must start with 'AUG', got {rna[:3]}.")

    if rna[-3:] not in ["UAA", "UAG", "UGA"]:
        raise ValueError(f"rna must end with 'UAA', 'UAG' or 'UGA'. Got {rna[-3:]}.")

    if len(rna) % 3 != 0:
        raise ValueError(f"rna size must be a multiple of 3. Got size {len(rna)}.")

    protein = ""

    for i in range(0, len(rna), 3):
        codon = rna[i : i + 3]
        if codon_table[codon] == "Stop":
            break
        protein += codon_table[codon]

    return protein


if __name__ == "__main__":
    codon_table_path = "../data/RNA_codon_table.txt"
    input_path = "../data/PROT.txt"

    codon_table = build_codon_table(codon_table_path)

    with open(input_path) as f:
        rna = f.read()

    print(rna_to_protein(rna, codon_table))
