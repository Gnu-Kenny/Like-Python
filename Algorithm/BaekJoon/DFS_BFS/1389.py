from collections import deque
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
answers = []
answer = 999999


class Node:
    def __init__(self, v, level):
        self.v = v
        self.level = level


def bfs(node: Node):
    global n, m, graph, visit, answers, answer
    q = deque()
    visit[node.v] = 1
    cnt = 0
    q.append(node)

    while q:
        now = q.popleft()

        for v in graph[now.v]:
            if visit[v]:
                continue
            visit[v] = 1
            cnt += now.level + 1
            q.append(Node(v, now.level+1))

    return cnt


def main():
    global n, m, graph, visit, answers, answer

    for _ in range(m):
        s, e = list(map(int, input().split()))

        graph[s].append(e)
        graph[e].append(s)

    for i in range(1, n+1):
        visit = [0 for _ in range(n+1)]
        answers.append(bfs(Node(i, 0)))

    print(answers.index(min(answers))+1)


if __name__ == '__main__':
    main()
