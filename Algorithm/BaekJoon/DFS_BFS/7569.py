from collections import deque

n = 0  # box 세로
m = 0  # box 가로
h = 0  # box 높이
box = []
# box value
# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 비어있는 칸
visit = []
points = []  # [n,m,h]
answer = 0


class Node:
    def __init__(self, y, x, z, level):
        self.y, self.x, self.z = y, x, z
        self.level = level


def bfs():
    global box, visit
    global n, m, h
    global answer
    global points

    dy = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    q = deque()

    for idx in range(len(points)):
        y, x, z = points[idx]
        q.append(Node(y, x, z, 0))
        visit[z][y][x] = True

    while len(q) != 0:
        now = q.popleft()

        answer = now.level
        # 가지치기
        for idx in range(6):
            nz = now.z + dz[idx]
            ny = now.y + dy[idx]
            nx = now.x + dx[idx]

            if nz < 0 or ny < 0 or nx < 0 or nz >= h or ny >= n or nx >= m:
                continue
            if visit[nz][ny][nx]:
                continue
            # 토마토가 들어있지 않을때
            if box[nz][ny][nx] == -1:
                continue
            # 다음 토마토가 익지 않은 토마토일때
            elif box[nz][ny][nx] == 0:
                visit[nz][ny][nx] = True
                box[nz][ny][nx] = True
                q.append(Node(ny, nx, nz, now.level+1))
            # 다음 토마토가 익은 토마토일때
            elif box[nz][ny][nx] == 1:
                continue


def main():
    global box, visit
    global n, m, h
    global answer
    global points
    m, n, h = list(map(int, input().split()))

    for h_idx in range(h):
        box_layer = []
        for n_idx in range(n):
            box_layer_elements = list(map(int, input().split()))
            box_layer.append(box_layer_elements)
            for m_idx, m_value in enumerate(box_layer_elements):
                # 익은 토마토일때의 좌표를 저장
                if m_value == 1:
                    points.append([n_idx, m_idx, h_idx])

        box.append(box_layer)

    visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

    bfs()

    # 토마토가 모두 익지는 못하는 상황이면 -1
    for box_l in box:
        for m_values in box_l:
            for m_v in m_values:
                if m_v == 0:
                    answer = -1
                    break
    print(answer)


if __name__ == "__main__":
    main()
