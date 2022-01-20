from queue import PriorityQueue
import sys
input = sys.stdin.readline
INF = 1000000000


class Node:
    def __init__(self, point, weight):
        self.point = point  # 시점
        self.weight = weight  # 가중치

    def __lt__(self, other):
        return self.weight < other.weight  # 객체의 level을 비교 Max Heap


def main():
    V, E = list(map(int, input().split()))

    start = int(input())

    alist = [[] for _ in range(V+1)]
    DP = [INF for _ in range(V+1)]
    for _ in range(E):
        s, e, w = list(map(int, input().split()))

        alist[s].append(Node(e, w))

    q = PriorityQueue()

    q.put(Node(start, 0))
    DP[start] = 0

    while q.qsize():
        now = q.get()
        # print(now)
        for idx in range(len(alist[now.point])):
            next = alist[now.point][idx]

            if DP[next.point] > now.weight + next.weight:
                DP[next.point] = now.weight + next.weight
                q.put(Node(next.point, DP[next.point]))

    for idx in range(1, V+1):
        if DP[idx] == INF:
            print("INF")
        else:
            print(DP[idx])


if __name__ == "__main__":
    main()
