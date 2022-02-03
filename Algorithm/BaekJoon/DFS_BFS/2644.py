from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
p1, p2 = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
answer = 0


class Node:
    def __init__(self, p, level):
        self.p = p
        self.level = level


def bfs(node: Node):
    global n, p1, p2, m, graph, visit, answer
    q = deque()

    q.append(node)
    visit[node.p] = 1
    while q:
        now = q.popleft()
        for v in graph[now.p]:
            if visit[v]:
                continue
            if v == p2:
                return now.level + 1
            visit[v] = 1
            q.append(Node(v, now.level+1))

    return -1


def main():
    global n, p1, p2, m, graph, visit, answer

    for _ in range(m):
        s, e = list(map(int, input().split()))
        graph[s].append(e)
        graph[e].append(s)

    print(bfs(Node(p1, 0)))


if __name__ == '__main__':
    main()
