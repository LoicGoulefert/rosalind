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


def transcribe(dna):
    """Transcribe a DNA sequence into its corresponding RNA.

    Args:
        dna: a sequence of amino acids

    Returns:
        a sequence of amino acids corresponding to the RNA of the input sequence
    """

    rna = dna.replace("T", "U")

    return rna


def reverse_complement(dna):
    """Return the reverse complement of a DNA strand.

    Args:
        dna: string

    Returns:
        the reverse complement of input DNA
    """

    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    dna_comp = ""

    for nt in dna:
        dna_comp += d[nt]

    return dna_comp[::-1]


def rna_to_protein(rna, codon_table):
    """Translate a RNA strand into a protein.

    Args:
        rna: sequence of amino acids
        codon_table: dict of codon to protein amino acid

    Returns:
        an amino acid chain corresponding to the protein translated from rna
    """

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
