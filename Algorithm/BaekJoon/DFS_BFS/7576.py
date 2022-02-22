from collections import deque
import sys
input = sys.stdin.readline

n = 0
m = 0
# 1: 익은 토마토 0: 익지 않은 토마토 -1: 토마토가 없음
board = [] 
visit = []
ripe_tomato_points = []

class Node:
    def __init__(self, y, x, level):
        self.y, self.x = y,x
        self.level = level

def bfs():
    global n, m, visit, board, ripe_tomato_points
    dy = (0,0,-1,1)
    dx = (-1,1,0,0)
    q = deque() 
    for point in ripe_tomato_points:
        q.append(point)

    while q:
        now = q.popleft()
        
        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if board[ny][nx] == -1 or board[ny][nx] == 1:
                continue
            if visit[ny][nx]:
                continue
            visit[ny][nx] = now.level+1
            q.append(Node(ny, nx, now.level + 1))
    

def main():
    global n, m, board, max_period, visit, ripe_tomato_points
    # 가로, 세로
    m, n = map(int,input().split()) 

    zero_flag = False
    for i in range(n):
        board_row = list(map(int,input().split()))
        board.append(board_row)
        for j,tomato in enumerate(board_row):
            if tomato == 1:
                ripe_tomato_points.append(Node(i,j,0))
            if tomato == 0:
                zero_flag = True
    
    if zero_flag is False:
        print(0)
        return

    # 토마토가 익었거나 토마토가 없으면 -1
    visit = [[-1 if board[i][j] else 0 for j in range(m)] for i in range(n)] 

    bfs()
        
    max_period = 0
    for periods in visit:
        for period in periods:
            if period == 0:
                print(-1)
                return
            max_period = max(max_period, period)
    print(max_period)
    
if __name__ == "__main__":
    main()
