sum = 0
answer = 0
arr = [1, -1]


def dfs(numbers, level, sum, target):
    global answer
    # 종료 시점
    if level == len(numbers):

        if sum == target:
            answer += 1
        return
    # 가지치기
    for idx in range(1 + 1):
        dfs(numbers, level + 1, sum + arr[idx] * numbers[level], target)


def solution(numbers, target):

    dfs(numbers, 0, 0, target)
    return answer


def main():
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))


if __name__ == "__main__":
    main()
