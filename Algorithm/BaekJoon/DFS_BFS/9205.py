from collections import deque
import sys
input = sys.stdin.readline


n = 0
h = 0
c = []
d = 0
visit = []
class Node:
    def __init__(self, y, x):
        self.y, self.x = y,x

def bfs():
    global n, h, c, d, visit
    q = deque()
    q.append(h)
    
    while q:
        now = q.popleft()

        if abs(now.y-d.y) + abs(now.x-d.x) <= 1000:
            print("happy")
            return
        
        for i in range(n):
            if visit[i]:
                continue
            
            ny, nx = c[i].y, c[i].x

            if abs(ny-now.y) + abs(nx-now.x) <= 1000:
                q.append(Node(ny,nx))
                visit[i] = 1
    
    print("sad")
    return
def main():
    global n, h, c, d, visit
    for _ in range(int(input())):
        n = int(input())
        x, y = map(int,input().split())
        h = Node(y,x)
        c = []
        for _ in range(n):
            x, y = map(int,input().split())
            c.append(Node(y,x))
        x, y = map(int,input().split())
        d = Node(y,x)
        visit = [0 for _ in range(n+1)]
        bfs()
if __name__ == "__main__":
    main()