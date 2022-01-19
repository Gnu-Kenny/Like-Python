
import sys
input = sys.stdin.readline

alist = []
table = []


class Node:
    def __init__(self, s, e, w):
        self.s = s
        self.e = e
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


def findBoss(a: int):
    global alist, table
    if table[a] == -1:
        return a
    table[a] = findBoss(table[a])  # a의 보스를 찾아야됨
    return table[a]


def setUnion(a: int, b: int):
    global alist, table

    aBoss = findBoss(a)
    bBoss = findBoss(b)

    if aBoss != bBoss:
        table[bBoss] = aBoss

        return True

    return False


def main():
    global alist, table
    answer = 0
    V, E = list(map(int, input().split()))
    table = [-1 for _ in range(V+1)]
    for _ in range(E):
        s, e, w = list(map(int, input().split()))

        alist.append(Node(s, e, w))

    alist.sort()

    for idx in range(len(alist)):

        now: Node = alist[idx]

        if setUnion(now.s, now.e):
            answer += now.w

    print(answer)


if __name__ == "__main__":
    main()
