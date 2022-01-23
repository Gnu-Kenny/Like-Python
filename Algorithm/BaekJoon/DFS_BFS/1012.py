from collections import deque


class Node:
    def __init__(self, y, x, level):
        self.y, self.x = y, x
        self.level = level


width = 0
height = 0
veg_num = 0
ground = []
visit = []
min_path = 99999999
dy = [-1, 1, 0, 0]  # 위, 아래, 좌, 우
dx = [0, 0, -1, 1]
answer = 0


def bfs():
    global width, height, veg_num
    global ground
    global visit
    global dy, dx
    global answer
    q = deque()

    q.append(Node(0, 0, 0))
    while len(q) != 0:
        now = q.popleft()

        # 종료 조건(도착)
        # if now.y == height - 1 and now.x == width - 1:
        #     return now.level + 1

        for idx in range(4):
            ny = now.y + dy[idx]
            nx = now.x + dx[idx]

            if ny < 0 or nx < 0 or ny >= height or nx >= width:
                continue
            if visit[ny][nx]:
                continue
            if ground[ny][nx] == 0:
                continue
            visit[ny][nx] = True
            q.append(Node(ny, nx, now.level + 1))

    if visit.count(True) == veg_num:
        answer += 1
    else:
        answer += 1
        bfs()

    return answer


def main():
    global width, height, veg_num
    global ground
    global visit

    t = int(input())

    for _ in range(t):
        width, height, veg_num = list(map(int, input().split()))
        ground = [[0 for _ in range(width)] for _ in range(height)]
        visit = [[False for _ in range(width)] for _ in range(height)]
        for _ in range(veg_num):
            pos = list(map(int, input().split()))  # w, h 순으로 입력
            ground[pos[1]][pos[0]] = 1

        bfs()
        print(answer)


if __name__ == "__main__":
    main()
