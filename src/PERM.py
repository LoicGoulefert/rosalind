from itertools import permutations

if __name__ == "__main__":
    path = "../data/PERM.txt"
    with open(path) as f:
        n = int(f.read())

    perms = list(permutations(range(1, n + 1)))
    print(len(perms))
    for p in perms:
        print(" ".join(map(str, p)))
