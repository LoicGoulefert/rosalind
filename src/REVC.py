from utils import reverse_complement


if __name__ == "__main__":
    path = "../data/REVC.txt"
    with open(path) as f:
        dna = f.read().strip()

    print(reverse_complement(dna))
