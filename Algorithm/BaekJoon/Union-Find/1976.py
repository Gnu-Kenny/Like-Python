import sys
input = sys.stdin.readline

table = []


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
    n = int(input())
    m = int(input())
    table = [-1 for _ in range(n)]
    for i in range(n):
        cities_connect = list(map(int, input().split()))
        for j, v in enumerate(cities_connect):
            if v == 1:
                setUnion(i, j)
    destinations = list(map(lambda x: x-1, list(map(int, input().split()))))

    for i in range(1, m):
        if setUnion(destinations[i-1], destinations[i]):
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()
