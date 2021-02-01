path = "data/RNA.txt"

with open(path) as f:
    dna = f.read().strip()

rna = dna.replace("T", "U")
print(rna)
