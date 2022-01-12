from collections import deque

w = 0
h = 0
ground = []
visit = []
answer = 0


class Node:
    def __init__(self, y, x, level):
        self.y = y
        self.x = x
        self.level = level


def bfs(start: Node):
    global w, h
    global ground
    global visit

    dy = [-1, 1, 0, 0, 1, -1, -1, 1]
    dx = [0, 0, -1, 1, 1, -1, 1, -1]

    q = deque([])
    q.append(start)
    while len(q) != 0:
        now = q.popleft()
        for idx in range(8):
            ny = now.y + dy[idx]
            nx = now.x + dx[idx]
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            if visit[ny][nx]:
                continue
            if ground[ny][nx] == 0:
                continue

            visit[ny][nx] = True

            q.append(Node(ny, nx, now.level + 1))


def main():
    global w, h
    global ground
    global visit
    global answer
    # input init
    while True:
        w, h = list(map(int, input().split()))
        ground = []
        if w == 0 and h == 0:
            break

        for _ in range(h):
            ground_row = list(map(int, input().split()))
            ground.append(ground_row)

        visit = [[0 for _ in range(w)] for _ in range(h)]

        for y in range(h):
            for x in range(w):
                if visit[y][x] == False and ground[y][x] == True:
                    answer += 1
                    bfs(Node(y, x, 0))

        print(answer)
        answer = 0


if __name__ == "__main__":
    main()
