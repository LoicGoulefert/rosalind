def build_mass_table(path):
    """Build a dict amino acid: mass.

    Args:
        path: path to amino acid mass table

    Returns:
        dict with key: amino acid and value: mass
    """

    with open(path) as f:
        data = [s.strip().split("   ") for s in f.readlines()]

    table = {key: float(value) for key, value in data}

    return table


def protein_mass(protein, mass_table):
    """Compute the mass of a protein.

    Args:
        protein: chain of amino acids
        mass_table: dict containing the mass of each amino acid

    Returns:
        total mass of the protein
    """

    total_mass = 0

    for aa in protein:
        total_mass += mass_table[aa]

    return round(total_mass, 3)


if __name__ == "__main__":
    mass_table = build_mass_table("../data/monoisotopic-mass-table.txt")
    path = "../data/PRTM.txt"
    with open(path) as f:
        protein = f.read()

    print(protein_mass(protein, mass_table))
