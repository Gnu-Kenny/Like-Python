import sys
input = sys.stdin.readline
import heapq
n = 0
m = 0
x = 0
graph = []
graph_copy = []
distance_go = []
distance_back = []
go_to_x = []
INF = int(1e9)

class Node:
    def __init__(self, e, w):
        self.e = e
        self.w = w
    
    def __lt__(self, other):
        return self.w < other.w

def dijkstra_go(start: int):
    global n, m, x, graph_copy, distance_go, INF, go_to_x
    q = []
    distance_go  = [INF for _ in range(n + 1)]
    graph_copy = graph.copy()
    distance_go[start] = 0
    
    heapq.heappush(q, Node(start, distance_go[start]))
    while q:
        now = heapq.heappop(q)
        
        for next in graph_copy[now.e]:
            
            if distance_go[next.e] > now.w + next.w:
                distance_go[next.e] = now.w + next.w
                
                heapq.heappush(q, Node(next.e,distance_go[next.e]))
    
    go_to_x[start] = distance_go[x]


def dijkstra_back(start: int):
    global n, m, x, graph, distance_back, INF
    q = []
    distance_back[start] = 0
    heapq.heappush(q, Node(start, distance_back[start]))

    while q:
        now = heapq.heappop(q)
        
        for next in graph[now.e]:
            
            if distance_back[next.e] > now.w + next.w:
                distance_back[next.e] = now.w + next.w
                
                heapq.heappush(q, Node(next.e,distance_back[next.e]))

def main():
    global n, m, x, graph,graph_copy, distance_go, distance_back, INF, go_to_x

    n, m, x = list(map(int,input().split()))
    graph = [[] for _ in range(n + 1)] 
    distance_back = [INF for _ in range(n + 1)] 
    distance_go  = [INF for _ in range(n + 1)] 
    go_to_x = [0 for _ in range(n + 1)] 
    for _ in range(m):
        s, e, w = list(map(int,input().split()))

        graph[s].append(Node(e,w))

    graph_copy = graph.copy()
    
    for i in range(1,n+1):
        dijkstra_go(i)
    dijkstra_back(x) # 돌아오는데 걸리는 최단 경로
    answers = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        answers[i] = go_to_x[i] + distance_back[i]
    
    print(max(answers))

if __name__ == "__main__":
    main()