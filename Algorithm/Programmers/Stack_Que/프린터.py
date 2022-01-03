from collections import deque


def solution(priorities, location):
    answer = []
    queue = deque([[priority, idx] for idx, priority in enumerate(priorities)])

    while len(queue) != 0:
        if len(queue) == 0:
            break
        max_value = max(queue)
        max_value = max_value[0]
        if queue[0][0] == max_value:

            answer.append(queue.popleft())
            continue
        queue.append(queue.popleft())
    answer_prev_index = [e[1] for e in answer]
    return answer_prev_index.index(location) + 1


def main():
    priorities = [2, 1, 3, 2]
    location = 2

    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))


if __name__ == "__main__":
    main()
