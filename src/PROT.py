from utils import build_codon_table, rna_to_protein


if __name__ == "__main__":
    codon_table_path = "../data/RNA_codon_table.txt"
    input_path = "../data/PROT.txt"

    codon_table = build_codon_table(codon_table_path)

    with open(input_path) as f:
        rna = f.read()

    print(rna_to_protein(rna, codon_table))
