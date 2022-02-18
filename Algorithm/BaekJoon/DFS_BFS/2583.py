
from collections import deque
import sys
input = sys.stdin.readline

m = 0
n = 0
ground = []
visit = []
cnts = []


class Node:
    global ground, visit, cnts

    def __init__(self, y, x):
        self.y, self.x = y, x


def bfs(node: Node):
    global m, n, ground, visit, cnts
    cnt = 1
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    q = deque()
    q.append(node)
    while q:
        now = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= m or nx >= n:
                continue
            if ground[ny][nx] == 0:
                continue
            if visit[ny][nx] == 1:
                continue

            visit[ny][nx] = 1
            cnt += 1
            q.append(Node(ny, nx))

    if cnt > 1:
        cnt -= 1

    cnts.append(cnt)


def main():
    global m, n, ground, visit, cnts
    answer = 0
    m, n, k = list(map(int, input().split()))
    ground = [[1 for _ in range(n)] for _ in range(m)]
    visit = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x1, y1, x2, y2 = list(map(int, input().split()))

        for y in range(y1, y2):
            for x in range(x1, x2):
                # if ground[y][x] == 0:
                #     continue
                ground[y][x] = 0

    for y in range(m):
        for x in range(n):
            if visit[y][x] == 0 and ground[y][x] == 1:
                answer += 1
                bfs(Node(y, x))

    print(answer)
    cnts.sort()
    print(*cnts)


if __name__ == '__main__':
    main()
