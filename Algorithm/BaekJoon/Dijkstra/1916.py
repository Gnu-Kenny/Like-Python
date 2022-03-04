import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF for _ in range(n+1)]
start = 0
end = 0


class Node:
    def __init__(self, e, w):
        self.e = e
        self.w = w

    def __lt__(self,other):
        return self.w < other.w


def dijkstra():
    global n, m, graph, distance, start, end
    q = []
    distance[start] = 0
    heapq.heappush(q, Node(start, distance[start]))

    while q:
        now = heapq.heappop(q)
        if now.e == end:
            break
        for next in graph[now.e]:

            if distance[next.e] > now.w + next.w:
                distance[next.e] = now.w + next.w

                heapq.heappush(q, Node(next.e, distance[next.e]))
            
            

def main():
    global n, m, graph, distance, start, end

    for _ in range(m):
        s, e, w = list(map(int,input().split()))
        graph[s].append(Node(e,w))

    start, end = list(map(int,input().split()))

    dijkstra()  
    print(distance[end])
if __name__ == "__main__":
    main()
