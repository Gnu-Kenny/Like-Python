import sys
input = sys.stdin.readline


def main():
    n, m = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # dp 초기화
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = board[i][j]
            elif i == 0:
                dp[0][j] = dp[0][j-1] + board[0][j]
            elif j == 0:
                dp[i][0] = dp[i-1][0] + board[i][0]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i][j]
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 1 and y1 == 1:
            print(dp[x2-1][y2-1])
        elif x1 == 1:
            print(dp[x2-1][y2-1] - dp[x2-1][y1-2])
        elif y1 == 1:
            print(dp[x2-1][y2-1] - dp[x1-2][y2-1])
        else:

            print(dp[x2-1][y2-1] - (dp[x1-2][y2-1] +
                  dp[x2-1][y1-2] - dp[x1-2][y1-2]))


if __name__ == "__main__":
    main()
