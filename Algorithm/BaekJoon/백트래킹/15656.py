import sys
input = sys.stdin.readline


n = 0
m = 0
sqnc = []
answer = []


def back(level: int):
    global n, m, sqnc, answer
    if level == m:
        print(*answer)
        return

    for i in range(n):
        answer.append(sqnc[i])
        back(level+1)
        answer.pop()


def main():
    global n, m, sqnc, answer

    n, m = list(map(int, input().split()))
    sqnc = list(map(int, input().split()))
    sqnc.sort()

    back(0)


if __name__ == "__main__":
    main()
