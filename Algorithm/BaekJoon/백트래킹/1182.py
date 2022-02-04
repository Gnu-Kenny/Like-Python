# https://www.acmicpc.net/problem/1182
import sys
input = sys.stdin.readline

n = 0  # 수열 내부 정수의 개수
s = 0  # 부분 수열의 합
sqnc = []
candi = 0  # s가 목표가 되어지는 부분 수열의 합
answer = 0  # 조건을 만족하는 부분 수열의 갯수


def back(index: int):
    global n, s, sqnc, candi, answer

    if index != 0 and candi == s:
        answer += 1

    for i in range(index, len(sqnc)):
        candi += sqnc[i]
        back(i+1)
        candi -= sqnc[i]


def main():
    global n, s, sqnc, candi, answer

    n, s = list(map(int, input().split()))
    sqnc = list(map(int, input().split()))

    back(0)

    print(answer)


if __name__ == '__main__':
    main()
