# https://www.acmicpc.net/problem/10164
import sys
input = sys.stdin.readline

n = 0
m = 0
p = 0
dy = (0,0,-1,1)
dx = (-1,1,0,0)
visit = []
point = 0
start_to_point = 0
point_to_end = 0
class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x

def dfs_start_to_point(node:Node):
    global n,m,p, point, start_to_point, point_to_end, dy, dx, visit
    dy = (0,1)
    dx = (1,0)
    y, x = node.y, node.x
    if y == point.y and x == point.x:
        start_to_point += 1
        return
        
    for i in range(2):
        ny = node.y + dy[i]
        nx = node.x + dx[i]

        if ny < 0 or nx < 0 or ny > point.y or nx > point.x:
            continue
        
            
        if visit[ny][nx]:
            continue
            
        visit[ny][nx] = 1

        dfs_start_to_point(Node(ny,nx))

        visit[ny][nx] = 0

def dfs_point_to_end(node:Node):
    global n,m,p, point, start_to_point, point_to_end, dy, dx, visit
    dy = (0,1)
    dx = (1,0)
    y, x = node.y, node.x
    if y == n-1 and x == m-1:
        point_to_end += 1
        return
        
    for i in range(2):
        ny = node.y + dy[i]
        nx = node.x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
            
        if visit[ny][nx]:
            continue
            
        visit[ny][nx] = 1

        dfs_point_to_end(Node(ny,nx))

        visit[ny][nx] = 0

def main(): 
    global n,m,p, point, start_to_point, point_to_end, visit
    n,m,p = map(int,input().split())

    point = Node((p-1) // m, (p-1) % m)

    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1
    if p != 0:
        dfs_start_to_point(Node(0,0))
        dfs_point_to_end(Node(point.y,point.x))
        print(start_to_point * point_to_end)
    else:
        dfs_point_to_end(Node(0,0))
        print(point_to_end)

if __name__ == "__main__":
    main()