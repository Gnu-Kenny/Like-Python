import sys
input = sys.stdin.readline


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def main():
    n, k = map(int, input().split())
    items = [[]]
    for i in range(n):
        w, v = map(int, input().split())
        items.append(Item(w, v))

    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            if j < items[i].weight:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(items[i].value + dp[i-1]
                               [j-items[i].weight], dp[i-1][j])

    print(dp[n][k])


if __name__ == "__main__":
    main()
