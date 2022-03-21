import sys
input = sys.stdin.readline

table = []

class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __repr__(self):
        return f'Node({self.s}, {self.e})'


def findBoss(a: int):
    global table
    if table[a] == -1:
        return a
    table[a] = findBoss(table[a])

    return table[a]


def setUnion(a: int, b: int):
    global table
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
    global table
    n, m = map(int, input().split())

    table = [-1 for _ in range(n)]
    count = 0
    find_cycle = False
    for i in range(1, m + 1):
        s, e = map(int, input().split())
        if setUnion(s, e) is False and find_cycle is False:
            count = i
            find_cycle = True

    print(count)


if __name__ == "__main__":
    main()
