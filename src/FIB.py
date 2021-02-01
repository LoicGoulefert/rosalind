def fibonacci_rabbits(n, k):
    if n == 1 or n == 2:
        return 1

    return fibonacci_rabbits(n - 1, k) + k * fibonacci_rabbits(n - 2, k)


if __name__ == "__main__":
    path = "data/FIB.txt"

    with open(path) as f:
        data = f.read().strip().split(" ")
        n, k = int(data[0]), int(data[1])

    print(fibonacci_rabbits(n, k))
