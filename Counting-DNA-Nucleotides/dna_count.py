path = "rosalind_dna.txt"

with open(path) as f:
    dna = f.read()
    print(dna)

d = {"A": 0, "C": 0, "T": 0, "G": 0}

for nt in dna[:-1]:
    d[nt] += 1

# print(d)
print("{} {} {} {}".format(d["A"], d["C"], d["G"], d["T"]))
