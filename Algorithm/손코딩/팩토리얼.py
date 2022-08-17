def factorial(n: int, fact: list):
    if n == 1:
        return 1
    return n * factorial(n-1, fact)


def main():
    n = 5
    fact = [0 for _ in range(n + 1)]
    print(factorial(n, fact))


if __name__ == "__main__":
    main()
