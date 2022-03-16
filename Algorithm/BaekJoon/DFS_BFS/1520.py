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
        return 1
    # 이미 방문했었다면 그 위치에서 출발하는 경우의 수 리턴
    if dp[now.y][now.x] != -1:
        return dp[now.y][now.x]

    count = 0
    for i in range(4):
        ny = now.y + dy[i]
        nx = now.x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if board[now.y][now.x] <= board[ny][nx]:
            continue
        count += dfs(Node(ny, nx))

    dp[now.y][now.x] = count

    return dp[now.y][now.x]


def main():
    global n, m, board, dy, dx, dp
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    print(dfs(Node(0, 0)))


if __name__ == "__main__":
    main()
