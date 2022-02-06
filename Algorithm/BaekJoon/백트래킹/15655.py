# https://www.acmicpc.net/problem/15655
import sys
input = sys.stdin.readline

n = 0
m = 0
sqnc = []
visit = []
answer = []
answers = []


def back(level: int):
    global n, m, sqnc, answer, visit, answers
    if level == m:
        if sorted(answer) not in answers:

            print(*answer)
            answers.append(sorted(answer))

        return

    for i in range(len(sqnc)):
        if visit[sqnc[i]]:
            continue
        visit[sqnc[i]] = 1
        answer.append(sqnc[i])
        back(level+1)
        visit[sqnc[i]] = 0
        answer.pop()


def main():
    global n, m, sqnc, answer, visit
    n, m = list(map(int, input().split()))
    visit = [0 for _ in range((10000 + 1))]
    sqnc = list(map(int, input().split()))
    sqnc.sort()

    back(0)


if __name__ == "__main__":
    main()
