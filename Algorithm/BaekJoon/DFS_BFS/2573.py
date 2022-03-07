from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

board = []
visit = []
n = 0
m = 0
dy = (0,0,-1,1)
dx = (-1,1,0,0)
answer = 1


class Node:
    def __init__(self,y,x):
        self.y, self.x = y,x


def check_iceberg_connected(board):
    global n, m, dy, dx, answer
    visit = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    flag = False
    for y in range(1,n-1):
        for x in range(1,m-1):
            if board[y][x]:
                flag = True
                q.append(Node(y,x))
                break
        if flag is True:
            break
    
    while q:
        now = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if board[ny][nx] == 0:
                continue
            
            if visit[ny][nx]:
                continue

            visit[ny][nx] = 1
            q.append(Node(ny,nx))

    is_all_iceberg_melt = True
    for y in range(1,n-1):
        for x in range(1,m-1):
            if board[y][x]:
                is_all_iceberg_melt = False
            if board[y][x] and visit[y][x] == 0:
                return False
    if is_all_iceberg_melt is True:
        print(0)
        exit(0)
    return True 
def bfs(level: int):
    global n, m, board, answer
    
    new_board = deepcopy(board)
    for y in range(1,n-1):
        for x in range(1,m-1):
            if new_board[y][x] == 0:
                continue
            else:
                count = 0
                for i in range(4):
                    ny = dy[i] + y
                    nx = dx[i] + x
                    if board[ny][nx] == 0:
                        count += 1
                
                new_board[y][x] -= count
                if new_board[y][x] < 0:
                    new_board[y][x] = 0
    
    board = deepcopy(new_board)
    
    # 빙산이 연결되어 있는지 검사
    if check_iceberg_connected(board) is True:

        answer += 1
        bfs(level + 1)
    else:
        print(answer)
    exit(0)
   
def main():
    global n, m, board, visit
    n, m = map(int,input().split())

    for _ in range(n):
        board.append(list(map(int,input().split())))
    
    visit = [[0 for _ in range(m)] for _ in range(n)]

    bfs(0)

if __name__ == '__main__':
    main()

