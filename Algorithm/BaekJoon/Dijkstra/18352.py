# https://www.acmicpc.net/problem/18352
import sys
input = sys.stdin.readline
import heapq

n = 0 # 노드 개수
m = 0 # 간선 개수
k = 0 # 거리
x = 0 # 시작 노드
INF = int(1e9)
graph = []
distance = []


class Node:
    def __init__(self,e, w):
        self.e = e
        self.w = w
    
    def __lt__(self, other):
        return self.w < other.w


def dijkstra(start: int):
    global n,m,k,x, graph, distance, INF
    q = []
    distance[start] = 0
    heapq.heappush(q,Node(start, distance[start]))

    while q:
        now = heapq.heappop(q)

        for next in graph[now.e]:

            if distance[next.e] > now.w + next.w:
                distance[next.e] = now.w + next.w
                heapq.heappush(q,Node(next.e, distance[next.e]))
        
def main():
    global n,m,k,x, graph, distance, INF
    n,m,k,x = list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]
    for _ in range(m):
        s, e = list(map(int,input().split()))
        graph[s].append(Node(e, 1))
    
    dijkstra(x)

    if k not in distance:
        print(-1)
    else:
        for idx,value in enumerate(distance):
            if value == k:
                print(idx)


if __name__ == "__main__":
    main()