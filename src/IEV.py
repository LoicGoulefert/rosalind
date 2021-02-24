def compute_dominant_offspring(couples, probs, n_offspring):
    """Compute the average dominant offspring count of a population.

    Args:
        couples: number of couples of each genotype combination
                 (AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa)
        probs: list of probability of having a dominant offspring
               for each genotype combination
        n_offspring: number of offspring each couple have

    Returns:
        the average dominant offspring count of the population
    """
    res = 0
    for c, p in zip(couples, probs):
        res += n_offspring * c * p

    return res


if __name__ == "__main__":
    path = "../data/IEV.txt"
    with open(path) as f:
        couples = list(map(int, f.read().split(" ")))

    genotypes_probs = [1, 1, 1, 0.75, 0.5, 0]
    print(compute_dominant_offspring(couples, genotypes_probs, 2))
