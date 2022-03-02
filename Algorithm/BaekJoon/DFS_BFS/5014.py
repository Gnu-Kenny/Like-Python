from collections import deque
import sys
input = sys.stdin.readline
f = 0 # 건물 층
s = 0 # 강호가 위치한 층
g = 0 # 스타트링크가 위치한 층
u = 0 # 위로 U층
d = 0 # 아래로 D층
visit = []
class Node:
    def __init__(self,f,level):
        self.f = f
        self.level = level

def bfs():
    global f, s, g, u, d, visit

    q = deque()
    q.append(Node(s,0))
    visit[s] = 1

    while q:
        now = q.popleft()
        if now.f == g:
            return now.level

        if now.f + u <= f and visit[now.f + u] == 0:
            visit[now.f + u] = 1
            q.append(Node(now.f + u, now.level + 1))
        if now.f - d >= 1 and visit[now.f - d] == 0:
            visit[now.f - d] = 1
            q.append(Node(now.f - d, now.level + 1))

    return 'use the stairs'
def main():
    global f, s, g, u, d, visit
    f, s, g, u, d = map(int,input().split())

    visit = [0 for _ in range(f+1)]

    print(bfs())

if __name__ == "__main__":
    main()