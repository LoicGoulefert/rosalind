path = "rosalind_rna.txt"

with open(path) as f:
    dna = f.read().strip()

rna = dna.replace("T", "U")
print(rna)
