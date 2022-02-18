from collections import deque
import sys
input = sys.stdin.readline

n = 0
board = []
start = 0
end = 0


class Node:
    def __init__(self, y, x, level):
        self.y, self.x = y, x
        self.level = level


def bfs(node: Node):
    global n, board, start, end
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]

    q = deque()

    q.append(node)

    while q:
        now = q.popleft()
        # 종료 시점
        y, x = now.y, now.x
        if y == end.y and x == end.x:
            return now.level

        # 가지치기
        for i in range(8):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx]:
                continue

            board[ny][nx] = 1
            q.append(Node(ny, nx, now.level+1))

    return -1


def main():
    global board, n, start, end
    for _ in range(int(input())):  # 테스트케이스
        n = int(input())  # N x N

        board = [[0 for _ in range(n)] for _ in range(n)]

        y, x = list(map(int, input().split()))
        start = Node(y, x, 0)
        y, x = list(map(int, input().split()))
        end = Node(y, x, 0)
        print(bfs(start))


if __name__ == '__main__':
    main()
