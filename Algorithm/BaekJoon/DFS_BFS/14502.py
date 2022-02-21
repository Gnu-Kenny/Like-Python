# https://www.acmicpc.net/problem/14502
from collections import deque
import sys
input = sys.stdin.readline
from copy import deepcopy
n = 0
m = 0
board = []
board_copy = []
virus_points = []
max_secure_area = 0


class Virus:
    def __init__(self, y, x, level):
        self.y, self.x = y, x
        self.level = level


def select_wall(level: int):
    global n, m, board, virus_points, max_secure_area, board_copy
    # 종료 시점 -> 3개 벽을 모두 세웠을떄
    if level == 3:
        # 바이러스 퍼뜨리기
        board_copy = deepcopy(board)
        for virus in virus_points:
            bfs_spread_virus(virus)
        
        # 안전 영역 최대 크기
        secure_area = 0
        for i in range(n):
            for j in range(m):
                if board_copy[i][j] == 0:
                    secure_area += 1
        max_secure_area = max(max_secure_area, secure_area)

        return

    for y in range(n):
        for x in range(m):
            if board[y][x] > 0:
                continue

            board[y][x] = 1
            select_wall(level+1)
            board[y][x] = 0
    

def bfs_spread_virus(virus: Virus):
    global n, m, virus_points, board_copy
    dy = (0,0,-1,1)
    dx = (-1,1,0,0)
    q = deque()
    q.append(virus)
    while q:
        now = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if board_copy[ny][nx] >= 1:
                continue
            board_copy[ny][nx] = 2
            q.append(Virus(ny,nx,now.level + 1))


def main():
    global n, m, virus_points, board, max_secure_area
    n, m = map(int,input().split())
    for i in range(n):
        board_row = list(map(int,input().split()))
        board.append(board_row)
        for j in range(m):
            if board[i][j] == 2:
                virus_points.append(Virus(i,j,0))
    
    # 벽 쌓기
    select_wall(0)
    print(max_secure_area)


if __name__ == "__main__":
    main()
