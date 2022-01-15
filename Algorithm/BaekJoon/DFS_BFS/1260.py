import sys
from collections import deque
# from queue import PriorityQueue
input = sys.stdin.readline

n = 0
m = 0
start = 0
alist = 0
visit = []


class Node:
    def __init__(self, point, level):
        self.point = point
        self.level = level

    def __lt__(self, other):
        return self.point < other.point


def dfs(node: Node):
    global n, m, start
    global alist, visit
    print(node.point, end=" ")
    visit[node.point] = True
    for v in alist[node.point]:
        if visit[v]:
            continue
        visit[v] = True
        dfs(Node(v, node.level+1))


def bfs():
    global n, m, start
    global alist, visit
    q = deque()

    q.append(Node(start, 0))
    # q = PriorityQueue()
    # q.put(Node(start, 0))

    visit[start] = True

    while q:
        now = q.popleft()

        print(now.point, end=" ")
        for v in alist[now.point]:
            if visit[v]:
                continue
            visit[v] = True
            q.append(Node(v, now.level+1))


def main():
    global n, m, start
    global alist, visit
    n, m, start = list(map(int, input().split()))
    alist = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    for _ in range(m):
        s, e = list(map(int, input().split()))

        alist[s].append(e)
        alist[e].append(s)

    for elements in alist:
        elements.sort()

    alist.sort(key=lambda x: alist[x])
    print(alist)
    dfs(Node(start, 0))
    print()
    visit = [0 for _ in range(n+1)]
    bfs()


if __name__ == "__main__":
    main()
