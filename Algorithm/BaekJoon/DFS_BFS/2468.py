from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]


class Node:
    def __init__(self, y, x):
        self.y, self.x = y, x


def bfs(node: Node):
    global n, ground, visit
    dy = (0, 0, -1, 1)
    dx = (-1, 1, 0, 0)

    q = deque()
    q.append(node)
    while q:
        now = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if ground[ny][nx] < 1:
                continue
            if visit[ny][nx]:
                continue

            visit[ny][nx] = 1
            q.append(Node(ny, nx))


def main():
    global n, ground, visit
    answer = 0
    max_area = 0
    # 1 <= h <= 100지만,
    # 비가 전혀 오지 않는 경우를 고려하여
    # 높이는 0 <= h <= 100가 된다.
    for _ in range(0, 100+1):
        answer = 0
        visit = [[0 for _ in range(n)] for _ in range(n)]

        for y in range(n):
            for x in range(n):
                if visit[y][x] == 0 and ground[y][x] >= 1:
                    answer += 1
                    bfs(Node(y, x))

        for y in range(n):
            for x in range(n):
                ground[y][x] -= 1

        max_area = max(max_area, answer)

    print(max_area)


if __name__ == '__main__':
    main()
