import sys
input = sys.stdin.readline


V = int(input())
E = int(input())
table = []
graph = []


class Node:
    def __init__(self, s, e, w):
        self.s = s
        self.e = e
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def __repr__(self):
        return f'Node({self.s},{self.e},{self.w}'


def findBoss(a: int):
    if table[a] == -1:
        return a

    table[a] = findBoss(table[a])
    return table[a]


def setUnion(a: int, b: int):
    aBoss = findBoss(a)
    bBoss = findBoss(b)

    if aBoss < bBoss:
        table[bBoss] = aBoss
    elif aBoss > bBoss:
        table[aBoss] = bBoss
    else:
        return False

    return True


def main():
    global V, E, graph, table

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph.append(Node(s, e, w))
    graph.sort()

    table = [-1 for _ in range(V+1)]

    answer = 0
    for i in range(len(graph)):
        now = graph[i]

        if setUnion(now.s, now.e):
            answer += now.w

    print(answer)


if __name__ == "__main__":
    main()
