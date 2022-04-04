import sys
input = sys.stdin.readline

n = 0
m = 0
count = 0
board = []
dp = []
dy = (0, 0, 1, -1)
dx = (-1, 1, 0, 0)


class Node:
    def __init__(self, y, x):
        self.y, self.x = y, x


def dfs(now: Node):
    global n, m, board, dp, dy, dx

    if now.y == n-1 and now.x == m-1:
        dp[now.y][now.x] = 1
        return 1
    dp[now.y][now.x] = 0

    for i in range(4):
        ny = now.y + dy[i]
        nx = now.x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if board[now.y][now.x] <= board[ny][nx]:
            continue
        if dp[ny][nx] != -1:
            dp[now.y][now.x] += dp[ny][nx]
        else:
            dp[now.y][now.x] += dfs(Node(ny, nx))

    return dp[now.y][now.x]


def main():
    global n, m, board, dy, dx, dp
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    print(dfs(Node(0, 0)))


if __name__ == "__main__":
    main()
