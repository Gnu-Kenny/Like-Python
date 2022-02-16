# https://www.acmicpc.net/submit/11399
import sys
input = sys.stdin.readline


def main():
    n = int(input())

    p_list = list(map(int,input().split()))
    answer = [0 for _ in range(n)]
    p_list.sort()
    sum_p = 0
    for i in range(len(p_list)):
        sum_p += p_list[i]
        answer[i] += sum_p
    print(sum(answer))

if __name__ == "__main__":
    main()