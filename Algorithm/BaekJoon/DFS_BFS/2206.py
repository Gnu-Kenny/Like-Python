from collections import deque
import sys
input = sys.stdin.readline

n = 0
m = 0
board = [] # 0: 이동할 수 있는 곳, 1: 이동할 수 없는 벽
visit = [] # [y좌표][x좌표][index: 0 -> 방문 유무, index: 1 -> 벽을 부수고 이동했는지 판별]

class Node:
    def __init__(self, y, x, level):
        self.y, self.x = y, x
        self.level = level

def bfs():
    global n, m, board, visit

    dy = (0,0,-1,1)
    dx = (-1,1,0,0) 
    q = deque()

    visit[0][0][0] = 1
    q.append([0,0,0])

    while q:
        y, x, wall_count = q.popleft()
        if y == n-1 and x == m-1:
            return visit[y][x][wall_count]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and visit[ny][nx][wall_count] == 0:
                if board[ny][nx] == 0:
                    visit[ny][nx][wall_count] = visit[y][x][wall_count] + 1
                    q.append([ny, nx, wall_count])
                
                if wall_count == 0 and board[ny][nx] == 1:
                    visit[ny][nx][1] = visit[y][x][wall_count] + 1
                    q.append([ny,nx,1])
            
    return -1

def main():
    global n, m, board, visit
    n, m = map(int,input().split())
    visit = [[[0,0] for _ in range(m)] for _ in range(n)]
    for _ in range(n):

        board.append(list(map(int,list(input().strip()))))
    
    print(bfs())
if __name__ == "__main__":
    main()

# 6 4
# 0000
# 1110
# 1000
# 1011
# 1111
# 0000
