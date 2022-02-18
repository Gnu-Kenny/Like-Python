from collections import deque

n = 0
m = 0
ground = []
visit = []
answer = 0


class Node:
    def __init__(self, y, x, level):
        self.y, self.x = y, x
        self.level = level


def bfs(node: Node):
    global n, m
    global ground, visit
    global answer
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    q.append(node)
    while len(q) != 0:
        now = q.popleft()
        # 종료 조건
        if now.y == n - 1 and now.x == m - 1:
            return now.level + 1

        visit[node.y][node.x] = True

        for idx in range(4):
            ny = now.y + dy[idx]
            nx = now.x + dx[idx]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if visit[ny][nx]:
                continue
            if ground[ny][nx] == 0:
                continue

            visit[ny][nx] = True
            q.append(Node(ny, nx, now.level + 1))


def main():
    global n, m
    global ground, visit
    global answer

    n, m = list(map(int, input().split()))
    for _ in range(n):
        ground.append(list(map(int, list(input()))))

    visit = [[0 for _ in range(m)] for _ in range(n)]

    print(bfs(Node(0, 0, 0)))


if __name__ == "__main__":
    main()
