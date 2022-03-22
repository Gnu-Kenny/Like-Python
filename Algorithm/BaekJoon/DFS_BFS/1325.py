from collections import deque
import sys
input = sys.stdin.readline

alist = []
visit = []
path = []
cnt = 0


def bfs(v: int):
    global alist, visit, path, cnt

    q = deque()

    q.append(v)
    visit[v] = 1
    while q:
        now = q.popleft()
        cnt += 1
        for i in alist[now]:
            if visit[i]:
                continue
            visit[i] = 1
            q.append(i)


def main():
    global alist, visit, path, cnt
    n, m = map(int, input().split())
    alist = [[] for _ in range(n + 1)]

    path = [0 for _ in range(n + 1)]
    for _ in range(m):
        s, e = map(int, input().split())
        alist[e].append(s)

    for i in range(1, n+1):
        visit = [0 for _ in range(n + 1)]
        cnt = 0
        bfs(i)
        path[i] = cnt

    answer = []
    max_computer_nums_in_path = max(path)
    for i, com in enumerate(path):
        if com == max_computer_nums_in_path:
            answer.append(i)

    print(*answer)


if __name__ == "__main__":
    main()
