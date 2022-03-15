from collections import deque
import sys
input = sys.stdin.readline

board = []
n = 0
m = 0
s = 0  # start
e = 0  # end
ponds = []  # pond


class Node:
    def __init__(self, y, x, level, is_pond):
        self.y, self.x = y, x
        self.level = level
        self.is_pond = is_pond


def bfs(node: Node):
    global n, m, board, s, e, ponds
    dy = (0, 0, -1, 1)
    dx = (-1, 1, 0, 0)

    q = deque()
    # 물이 찰 예정인 칸은 이동 불가 이므로 고슴도치가 이동하기 전에 먼저 물을 채운다.

    for p in ponds:
        q.append(p)

    q.append(node)

    while q:
        now = q.popleft()
        if (now.y == e.y and now.x == e.x) and (now.is_pond is False):
            return now.level
        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if board[ny][nx] == 0 or board[ny][nx] == 1:
                continue
            if board[ny][nx] == 2:
                if now.is_pond is True:
                    board[ny][nx] = 0
                    q.append(Node(ny, nx, 0, True))
                else:
                    pass
                continue
            if board[ny][nx] == 400:
                if now.is_pond is True:
                    pass
                else:
                    q.append(Node(ny, nx, now.level + 1, False))
                continue

            if now.is_pond is True:
                board[ny][nx] = 0
                q.append(Node(ny, nx, 0, True))
            else:
                board[ny][nx] = 2
                q.append(Node(ny, nx, now.level + 1, False))

    return "KAKTUS"


def main():
    global n, m, board, s, e, ponds
    n, m = map(int, input().split())

    for i in range(n):
        board_row = list(input().strip())
        for j in range(len(board_row)):
            if board_row[j] == 'S':
                board_row[j] = 2
                s = Node(i, j, 0, False)
            elif board_row[j] == 'D':
                board_row[j] = 400
                e = Node(i, j, 0, False)
            elif board_row[j] == '.':
                board_row[j] = -1
            elif board_row[j] == '*':
                board_row[j] = 0
                ponds.append(Node(i, j, 0, True))
            elif board_row[j] == 'X':
                board_row[j] = 1

        board.append(board_row)
    print(bfs(s))


if __name__ == "__main__":
    main()
