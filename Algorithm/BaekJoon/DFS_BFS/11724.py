import sys
input = sys.stdin.readline

alist = []
visit = []


def dfs(start: int):
    global alist, visit

    for element in alist[start]:
        if visit[element]:
            continue
        visit[element] = 1
        dfs(element)


def main():
    global alist, visit
    answer = 0
    n, m = list(map(int, input().split()))

    alist = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    for _ in range(m):
        s, e = list(map(int, input().split()))

        alist[s].append(e)
        alist[e].append(s)  # 방향성이 없으므로

    for i in range(1, n+1):
        if visit[i] == 0:
            answer += 1
            dfs(i)

    print(answer)


if __name__ == "__main__":
    main()

