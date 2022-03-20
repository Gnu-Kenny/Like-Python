import sys
input = sys.stdin.readline


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


if __name__ == "__main__":
    main()
