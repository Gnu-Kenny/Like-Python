from collections import deque


def main():
    n, m = list(map(int, input().split()))
    alist = [[] for _ in range(n+1)]
    table = [0 for _ in range(n+1)]  # 해당 인덱스에 해당하는 값을 필요로 하는 다른 값들의 갯수

    for _ in range(0, m):
        s, e = list(map(int, input().split()))
        alist[s].append(e)
        table[e] += 1

    q = deque()
    # 선행이 필요하지 않은 값들을 큐에 추가
    for idx in range(1, n+1):
        if table[idx] == 0:
            q.append(idx)

    while len(q) != 0:
        now = q.popleft()

        print(now, end=" ")

        for e in alist[now]:
            table[e] -= 1

            if table[e] == 0:
                q.append(e)


if __name__ == "__main__":
    main()
