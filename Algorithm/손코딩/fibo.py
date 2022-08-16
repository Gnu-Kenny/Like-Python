# 재귀를 이용한 피보나치

def fibo(n: int, fibo_arr: list):
    # 메모이제이션
    if n != 0 and fibo_arr[n] > 0:
        return fibo_arr[n]
    if n == 1:
        fibo_arr[n] = 1
        return 1
    if n == 0:
        fibo_arr[n] = 0
        return 0
    fibo_arr[n] = fibo(n-2, fibo_arr) + fibo(n-1, fibo_arr)
    return fibo_arr[n]


def main():
    n = 20
    fibo_arr = [0 for _ in range(n + 1)]
    print(fibo(n, fibo_arr))


if __name__ == "__main__":
    main()
