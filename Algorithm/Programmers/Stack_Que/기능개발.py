from collections import deque
import math


def solution(progresses, speeds):
    rest_days = deque([])
    answer = []
    for progress, speed in zip(progresses, speeds):
        rest_progress = 100 - progress
        rest_day = math.ceil(rest_progress / speed)

        rest_days.append(rest_day)

    count = 1

    while len(rest_days) != 0:
        max = rest_days[0]
        count = 0
        while True:
            if len(rest_days) == 0:
                break
            if max < rest_days[0]:
                break
            count += 1
            rest_days.popleft()
        answer.append(count)

    return answer


def main():
    # progresses = [93, 30, 55]
    # speeds = [1, 30, 5]

    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))


if __name__ == "__main__":
    main()
