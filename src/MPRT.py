import requests
import regex as re

from utils import parse_fasta


def get_fasta_seqs(ids):
    """Get fasta sequences from protein IDs on uniprot.

    Args:
        ids: list of protein IDs

    Return:
        a dict of fasta sequences, with key: protein id and value: sequence
    """

    url_template = "http://www.uniprot.org/uniprot/{}.fasta"
    fasta_seqs = {}

    for id in ids:
        r = requests.get(url_template.format(id))
        data = r.text.split("\n")[:-1]
        fasta_sequence = parse_fasta(data)
        fasta_seqs[id] = next(iter(fasta_sequence.values()))

    return fasta_seqs


def search_motif(protein, motif):
    """Search for a motif in a protein.

    Args:
        protein: sequence of amino acids
        motif:

    Return:
        a list of indexes of the motif's locations within protein
    """
    motif_regex = motif.replace("{", "[^").replace("}", "]")
    indexes = re.finditer(motif_regex, protein, overlapped=True)

    return [i.start() + 1 for i in indexes]


if __name__ == "__main__":
    path = "../data/MPRT.txt"
    with open(path) as f:
        ids = [s.strip() for s in f.readlines()]

    fasta_seqs = get_fasta_seqs(ids)
    motif = "N{P}[ST]{P}"

    for name in fasta_seqs:
        indexes = search_motif(fasta_seqs[name], motif)
        if indexes != []:
            print(name)
            print(" ".join(map(str, indexes)))
