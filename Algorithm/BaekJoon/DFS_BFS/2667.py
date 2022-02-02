from collections import deque
# import sys
# input = sys.stdin.readline

n = int(input())
ground = [list(map(int, list(input()))) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
cnts = []
group_cnt = 0


class Node:
    def __init__(self, y, x):
        self.y, self.x = y, x


def bfs(node: Node):
    global ground, visit, n, group_cnt, cnts
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    cnt = 1
    q = deque()
    q.append(node)
    while q:
        now = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if ground[ny][nx] == 0:
                continue
            if visit[ny][nx] == 1:
                continue
            visit[ny][nx] = 1
            cnt += 1
            q.append(Node(ny, nx))
    # 인접한 좌표가 2개 이상일때는
    # 그래프 탐색 중 시작 좌표를 탐색하게 되어 카운트가 증가하지만
    # 좌표가 하나일 경우는 시작 좌표를 탐색할 수 없다.
    # 따라서 첫 카운트는 값은 1로 하되 좌표가 2개 이상일 경우에는 카운트 값을 하나 빼준다.
    if cnt > 1:
        cnt -= 1
    cnts.append(cnt)


def main():
    global ground, visit, n, cnts, group_cnt

    for y in range(n):
        for x in range(n):
            if visit[y][x] == 0 and ground[y][x] == 1:
                group_cnt += 1
                bfs(Node(y, x))

    print(group_cnt)
    cnts.sort()
    for cnt in cnts:
        print(cnt)


if __name__ == "__main__":
    main()
