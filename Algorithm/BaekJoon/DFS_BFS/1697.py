from collections import deque

n = 0
k = 0
visit = []


class Node:
    def __init__(self, x, level):
        self.x, self.level = x, level


def bfs():
    global n, k
    global visit
    dx = (-1, 1, 0)
    da = (1, 1, 2)

    q = deque()
    q.append(Node(n, 0))
    visit[n] = 1

    while len(q) != 0:
        now = q.popleft()

        if now.x == k:
            return now.level
        for idx in range(3):
            nx = now.x*da[idx] + dx[idx]

            if nx < 0 or nx > 200000:
                continue
            if visit[nx]:
                continue

            visit[nx] = 1
            q.append(Node(nx, now.level+1))

    return -1


def main():
    global n, k
    global visit
    n, k = list(map(int, input().split()))
    visit = [0 for _ in range(200001)]
    print(bfs())


if __name__ == "__main__":
    main()
