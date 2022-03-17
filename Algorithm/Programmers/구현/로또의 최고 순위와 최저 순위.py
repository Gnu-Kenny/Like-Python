import sys
input = sys.stdin.readline


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = lottos.count(0)
    answer = 0
    for lotto in lottos:
        if lotto in win_nums:
            answer += 1

    return [rank[answer + zero_count], rank[answer]]


def main():
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    lottos = [0, 0, 0, 0, 0, 0]
    win_nums = [38, 19, 20, 40, 15, 25]
    lottos = [45, 4, 35, 20, 3, 9]
    win_nums = [20, 9, 3, 45, 4, 35]
    print(solution(lottos, win_nums))


if __name__ == "__main__":
    main()
