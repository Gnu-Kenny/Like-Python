def solution(arr: list):
    for i in range(1, len(arr)):
        idx = i - 1
        temp = i
        while idx >= 0:
            if arr[idx] > arr[temp]:
                arr[idx], arr[temp] = arr[temp], arr[idx]
                temp = idx
            idx -= 1

    return arr


def main():
    arr = [2, 4, 1, 9, 8, 7]

    print(solution(arr))


if __name__ == "__main__":
    main()
