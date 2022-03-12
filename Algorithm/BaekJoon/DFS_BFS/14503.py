import sys
input = sys.stdin.readline

m = 0 # 가로
r = 0 # 현재 로봇 y 좌표
c = 0 # 현재 로봇 x 좌표
d = 0 # 로봇이 바라보는 방향 0: 북, 1: 동, 2: 남, 3: 서
clean = 0
dy = (-1,0,1,0)
dx = (0,1,0,-1)
visit = []
board = []

def dfs(y:int, x:int, d: int):
    global clean, board, dy, dx
    
    if board[y][x] == 0:
        board[y][x] = 2
        clean += 1
    
    for _ in range(4):
        nd = (d+3) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]
        if board[ny][nx] == 0:
            dfs(ny,nx,nd)
            return
        d = nd
    nd = (d + 2) % 4
    ny = y + dy[nd]
    nx = x + dx[nd]
    if board[ny][nx] == 1:
        return 
    dfs(ny,nx,d)
def main():
    global n, m, r, c, d, clean, visit, board
    n, m = map(int,input().split())
    r, c, d = map(int,input().split())
    
    visit = [[0 for _ in range(m)] for _ in range(n)]
    board = [list(map(int,input().split())) for _ in range(n)]
    dfs(r,c,d)
    print(clean)
if __name__ == "__main__":
    main()