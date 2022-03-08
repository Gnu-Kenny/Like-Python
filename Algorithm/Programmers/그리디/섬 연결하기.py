# 크루스칼 알고리즘 (최소의 비용으로 모든 노드를 연결하는 알고리즘)
# 1. 간선 정보를 오름차순으로 정렬
# 2. 정렬된 순서에 맞게 그래프에 포함
# 3-1. Union-find -> 사이클 여부 확인
# 3-2. 사이클을 형성하는 경우 포함하지 않음
from heapq import heappop as hpop
from heapq import heappush as hpush
import sys
input = sys.stdin.readline

INF = int(1e9)
distance = []
table = []
alist = []


class Node:
    def __init__(self, s, e, w):
        self.s, self.e = s, e
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def __repr__(self):
        return f'Node({self.s},{self.e},{self.w})'


def findBoss(a: int):
    global table

    if table[a] == -1:
        return a
    table[a] = findBoss(table[a])

    return table[a]


def setUnion(a: int, b: int):
    aBoss = findBoss(a)
    bBoss = findBoss(b)

    # 숫자가 더 작은 부모로 병합
    if aBoss < bBoss:
        table[bBoss] = aBoss
    elif aBoss > bBoss:
        table[aBoss] = bBoss
    else:
        return False

    return True


def solution(n, costs):
    global alist, distance, table
    v = []
    for cost in costs:
        if cost[0] not in v:
            v.append(cost[0])
        if cost[1] not in v:
            v.append(cost[1])
        alist.append(Node(cost[0], cost[1], cost[2]))
    # 간선 정보를 오름차순 정렬
    alist.sort()
    print(alist)
    table = [-1 for _ in range(len(v))]

    answer = 0
    for i in range(len(alist)):
        now = alist[i]
        if setUnion(now.s, now.e):

            answer += now.w

    return answer


def main():
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    print(solution(n, costs))


if __name__ == "__main__":
    main()
