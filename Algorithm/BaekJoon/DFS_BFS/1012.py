from collections import deque
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, y, x):
        self.y, self.x = y, x


w = 0
h = 0
v_num = 0
ground = []
visit = []


def bfs(node: Node):
    global w, h, v_num
    global ground
    global visit

    dy = [-1, 1, 0, 0]  # 위, 아래, 좌, 우
    dx = [0, 0, -1, 1]

    q = deque()

    q.append(node)
    while q:
        now = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            if visit[ny][nx]:
                continue
            if ground[ny][nx] == 0:
                continue
            visit[ny][nx] = 1
            q.append(Node(ny, nx))


def main():
    global w, h, v_num
    global ground
    global visit

    t = int(input())

    for _ in range(t):
        answer = 0
        ground = []
        visit = []
        w, h, v_num = list(map(int, input().split()))
        ground = [[0 for _ in range(w)] for _ in range(h)]
        visit = [[0 for _ in range(w)] for _ in range(h)]
        for _ in range(v_num):
            x, y = list(map(int, input().split()))  # w, h 순으로 입력
            ground[y][x] = 1
        for y in range(h):
            for x in range(w):
                if visit[y][x] == 0 and ground[y][x] == 1:
                    answer += 1
                    bfs(Node(y, x))

        print(answer)


if __name__ == "__main__":
    main()
