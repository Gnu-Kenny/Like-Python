import sys
input = sys.stdin.readline

n = 0
nums = []
operators = []
sequence = [0 for _ in range(12)]
min_value = 21e8
max_value = -21e8


def backtracking(level: int):
    global n, nums, operators, sequence, min_value, max_value
    # 종료
    if level == n - 1:
        sum = nums[0]
        for i in range(level):
            if sequence[i] == 0:
                sum += nums[i+1]
            elif sequence[i] == 1:
                sum -= nums[i+1]
            elif sequence[i] == 2:
                sum *= nums[i+1]
            elif sequence[i] == 3:
                sum /= nums[i+1]
                sum = int(sum)

        max_value = max(max_value, sum)
        min_value = min(min_value, sum)
        return

        # 가지치기
    for i in range(4):
        if operators[i] > 0:
            sequence[level] = i
            operators[i] -= 1
            backtracking(level+1)
            operators[i] += 1


def main():
    global n, nums, operators, sequence, min_value, max_value

    n = int(input())
    nums = list(map(int, input().split()))
    operators = list(map(int, input().split()))  # [+,-,*,/]
    backtracking(0)

    print(max_value)
    print(min_value)


if __name__ == "__main__":
    main()
