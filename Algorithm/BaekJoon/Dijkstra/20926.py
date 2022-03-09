# https://www.acmicpc.net/problem/20926
# 얼음 미로
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

w = 0
h = 0
board = []
distance = []
INF = int(1e9)
obj = ('T', 'R', 'H', 'E') # T : 테라, R : 바위, H : 구멍, E : 출구
class Node:
    def __init__(self,y,x,w):
        self.y, self.x = y, x
        self.w = w

    def __lt__(self,other):
        return self.w < other.w


def dijkstra(node:Node):
    global w, h, board, distance, obj, INF
    dy = (1,0,-1,0)
    dx = (0,1,0,-1)

    q = []
    distance[node.y][node.x] = 0

    heappush(q, node)

    while q:
        now = heappop(q)
        if board[now.y][now.x] == 'E':
            return now.w
        for i in range(4):
            
            ny = now.y + dy[i]
            nx = now.x + dx[i]
            dist = now.w
            while True:
                if ny < 0 or nx < 0 or ny >= h or nx >= w:
                    break
                next = board[ny][nx]
                if next == 'H':
                    break
                elif next == 'E':
                    if distance[ny][nx] > dist:
                        distance[ny][nx] = dist
                        heappush(q, Node(ny, nx, distance[ny][nx]))
                    break
                elif next == 'R':
                    ny = ny - dy[i]
                    nx = nx - dx[i]
                    if distance[ny][nx] > dist:
                        distance[ny][nx] = dist
                        heappush(q, Node(ny, nx, distance[ny][nx]))
                    break
                else:
                    dist += board[ny][nx]
                    ny = ny + dy[i]
                    nx = nx + dx[i]
                        

    return -1
    
def main():
    global w, h, board, distance, obj, INF
    
    w, h = list(map(int,input().split()))
    for y in range(h):
        board_row = list(input()[:-1])
        for x,v in enumerate(board_row):
            if v not in obj:
                board_row[x] = int(board_row[x])
            elif v == 'T':
                start = Node(y,x,0)
        board.append(board_row)
    board[start.y][start.x] = 0
    distance = [[INF for _ in range(w)] for _ in range(h)]
    print(dijkstra(start))


if __name__ == "__main__":
    main()