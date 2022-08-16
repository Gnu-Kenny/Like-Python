def solution(num: int):
    arr = [0 for _ in range(num + 1)]
    return fibo(num, arr)


def fibo(n: int, arr: list):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if arr[n] > 0:
        return arr[n]

    arr[n] = fibo(n-2, arr) + fibo(n-1, arr)

    return arr[n]


def main():
    num = 7
    print(solution(num))


if __name__ == "__main__":
    main()
