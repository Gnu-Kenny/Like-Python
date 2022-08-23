def solution(str: str):
    already_exist = list()
    arr = list(str)
    answer = ''

    for i in range(len(arr)):
        if arr[i] in already_exist:
            continue
        already_exist.append(arr[i])
        answer += arr[i]
    return answer


def main():
    str = "ksetkkset"
    print(solution(str))


if __name__ == "__main__":
    main()
