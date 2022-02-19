# https://www.acmicpc.net/problem/1504
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

alist = []
distance = []
N = 0
E = 0
INF = int(1e9)
points = []


class Node:
    def __init__(self, e, w):
        self.e = e
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    
def dijkstra(start: int):
    global alist, distance, N, E, INF, points
    distance = [INF for _ in range(N+1)]
    q = []
    distance[start] = 0
    heappush(q, Node(start, distance[start]))

    while q:
        now = heappop(q)

        for next in alist[now.e]:
            
            if distance[next.e] > now.w + next.w:
                distance[next.e] = now.w + next.w
                heappush(q, Node(next.e,distance[next.e]))
    

def main():
    global alist, distance, N, E, INF, points

    N, E = list(map(int,input().split()))
    alist = [[] for _ in range(N+1)]
    # distance = [INF for _ in range(N+1)]
    for _ in range(E):
        s, e, w = list(map(int,input().split()))

        alist[s].append(Node(e,w))
        alist[e].append(Node(s,w))

    points = [0] + list(map(int,input().split()))
    # 1 -> p1 -> p2 -> n
    # 1 -> p2 -> p1 -> n
    dijkstra(1)
    s_to_p1 = distance[points[1]]
    s_to_p2 = distance[points[2]]
    dijkstra(points[1])
    p1_to_p2 = distance[points[2]]
    p1_to_n = distance[N]
    dijkstra(points[2])
    p2_to_p1 = distance[points[1]]
    p2_to_n = distance[N]

    path1 = s_to_p1 + p1_to_p2 + p2_to_n
    path2 = s_to_p2 + p2_to_p1 + p1_to_n

    result = min(path1,path2)
    print(result if result < INF else -1)

if __name__ == "__main__":
    main()