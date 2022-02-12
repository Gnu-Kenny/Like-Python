from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
alist = []
visit = []
answer = [0 for _ in range(n+1)]


def bfs(start: int):
    global alist, visit, n, answer
    q = deque()

    q.append(start)
    visit[start] = 1
    while q:
        now = q.popleft()
        for element in alist[now]:
            if visit[element]:
                continue
            visit[element] = 1
            answer[element] = now

            q.append(element)


def main():
    global alist, visit, n, answer

    alist = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    for _ in range(1, n):
        s, e = list(map(int, input().split()))

        alist[s].append(e)
        alist[e].append(s)

    bfs(1)

    for i in range(2, n+1):
        print(answer[i])


if __name__ == "__main__":
    main()
