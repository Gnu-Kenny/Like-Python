import sys
input = sys.stdin.readline

limit_number = 15000
sys.setrecursionlimit(limit_number)

t = int(input())
m, n, k = 0,0,0
board = []
visited = []

dy = [0,0,-1,1]
dx = [-1,1,0,0]


class Node():
    def __init__(self,y,x):
        self.y = y
        self.x = x


def main():
    global t, m, n, k, board, visited
    
    for _ in range(t):
        # init
        m, n, k = map(int, input().split())
        board = [[0 for _ in range(m)]for _ in range(n)]
        visited = [[0 for _ in range(m)]for _ in range(n)]
        
        for _ in range(k):
            x, y = map(int, input().split())

            board[y][x] = 1
        
        # 탐색 구간 선정
        ans = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1 and visited[i][j] == 0:
                    
                    dfs(Node(i,j))
                    
                    ans += 1
        
        print(ans)


def dfs(now: Node):
    global m, n, board, visited, dy, dx
    
    visited[now.y][now.x] = 1
    
    for i in range(4):
        ny = now.y + dy[i]
        nx = now.x + dx[i]
        
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        
        if board[ny][nx] == 0:
            continue
        
        if visited[ny][nx] == 1:
            continue
        
        dfs(Node(ny, nx))

if __name__ == '__main__':
    main()