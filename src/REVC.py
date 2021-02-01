path = "data/REVC.txt"

with open(path) as f:
    dna = f.read().strip()

d = {"A": "T", "T": "A", "C": "G", "G": "C"}

dna_comp = ""

for nt in dna:
    dna_comp += d[nt]

print(dna_comp[::-1])
