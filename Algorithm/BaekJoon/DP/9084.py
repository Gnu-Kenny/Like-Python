import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        coins = [0] + list(map(int, input().split()))
        m = int(input())
        dp = [0 for _ in range(m+1)]
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(coins[i], m+1):
                dp[j] += dp[j-coins[i]]

        print(dp[m])


if __name__ == "__main__":
    main()

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2]]
