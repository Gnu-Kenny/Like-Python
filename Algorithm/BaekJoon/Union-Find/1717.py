import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

table = []


def findBoss(a: int):
    global table
    if table[a] == a:
        return a
    table[a] = findBoss(table[a])
    return table[a]


def setUnion(a: int, b: int):
    global table

    aBoss = findBoss(a)
    bBoss = findBoss(b)
    if aBoss == bBoss:
        return
    if aBoss < bBoss:
        table[bBoss] = aBoss
    else:
        table[aBoss] = bBoss


def main():
    global table, dp
    n, m = map(int, input().split())
    table = [v for v in range(n+1)]
    dp = [-1 for _ in range(n+1)]
    for _ in range(m):
        operator, a, b = map(int, input().split())

        if operator == 0:
            setUnion(a, b)
        else:
            if findBoss(a) == findBoss(b):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    main()
