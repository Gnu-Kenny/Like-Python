# https://www.acmicpc.net/problem/4485
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = 0
board = []
distance = []
dy = (0,0,-1,1)
dx = (-1,1,0,0)
INF = int(1e9)  


class Node:
    def __init__(self, y, x, w):
        self.y, self.x = y, x
        self.w = w
    
    def __lt__(self,other):
        return self.w < other.w


def dijkstra(node: Node):
    global n, board, distance, INF, dy, dx
    q = []
    distance[0][0] = 0
    heappush(q, node)
    while q:
        now = heappop(q)
        if now.y == n-1 and now.x == n-1:
            return distance[n-1][n-1]
        
        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            next = board[ny][nx]

            if distance[ny][nx] > now.w + next:
                distance[ny][nx] = now.w + next
                heappush(q, Node(ny,nx,distance[ny][nx]))

    return -1

def main():
    global n, board, distance, INF
    num = 1
    while (n:=int(input())) != 0:
        
        board = []
        distance = []
        distance = [[INF for _ in range(n)] for _ in range(n)]
        for _ in range(n): 
            board.append(list(map(int,input().split())))

        print(f'Problem {num}: {dijkstra(Node(0,0,board[0][0]))}')
        num += 1
if __name__ == '__main__':
    main()  