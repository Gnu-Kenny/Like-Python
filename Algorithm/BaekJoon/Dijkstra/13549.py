from queue import PriorityQueue

n = 0
k = 0
visit = []  # value : Node의 level
answer = [0, 0]


class Node:
    def __init__(self, x, level):
        self.x, self.level = x, level

    # 연산자 재정의
    def __lt__(self, other):
        return self.level < other.level  # 객체의 level을 비교


def bfs():
    global n, k
    global visit
    global answer
    dx = (-1, 1, 0)
    da = (1, 1, 2)

    q = PriorityQueue()
    q.put(Node(n, 0))
    visit[n] = 0
    while not q.empty():
        now = q.get()
        if visit[now.x] < now.level:
            continue
        if now.x == k:
            return now.level

        # +1
        if now.x + 1 <= 100000 and now.x < k:
            if visit[now.x + 1] == -1 or visit[now.x + 1] > now.level + 1:
                visit[now.x + 1] = now.level + 1
                q.put(Node(now.x+1, now.level + 1))

        # -1
        if now.x - 1 >= 0:
            if visit[now.x - 1] == -1 or visit[now.x - 1] > now.level + 1:
                visit[now.x - 1] = now.level + 1
                q.put(Node(now.x-1, now.level + 1))

        # *2
        if now.x * 2 <= 100000 and now.x < k:
            if visit[now.x * 2] == -1 or visit[now.x * 2] > now.level:
                visit[now.x * 2] = now.level
                q.put(Node(now.x*2, now.level))


def main():
    global n, k
    global visit
    global answer

    n, k = list(map(int, input().split()))

    visit = [-1 for _ in range(100000 + 1)]

    print(bfs())


if __name__ == "__main__":
    main()
