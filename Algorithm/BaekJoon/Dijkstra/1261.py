# https://www.acmicpc.net/problem/1261
import sys
input = sys.stdin.readline
import heapq


n = 0 # 세로
m = 0 # 가로
board = []
distance = []
INF = int(1e9)
class Node:
    def __init__(self, y, x, w):
        self.y, self.x = y, x
        self.w = w
    
    def __lt__(self, other):
        return self.w < other.w


def dijkstra(node: Node):
    global n,m, board, distance, INF
    q = []
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    distance[0][0] = 0
    heapq.heappush(q, node)
    while q:
        now = heapq.heappop(q)
        if now.y == n and now.x == m:
            break
        for i in range(4):
            
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if distance[ny][nx] > now.w + board[ny][nx]:
                distance[ny][nx] = now.w + board[ny][nx]
                heapq.heappush(q, Node(ny,nx, distance[ny][nx]))




def main():
    global n,m, board, distance, INF
    m,n = list(map(int,input().split()))
    board = [list(map(int,(list(input())[:-1]))) for _ in range(n)]
    distance = [[INF for _ in range(m)] for _ in range(n)]
    dijkstra(Node(0,0,0))
    print(distance[n-1][m-1])
if __name__ == "__main__":
    main()