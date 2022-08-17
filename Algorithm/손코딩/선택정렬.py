def solution(arr: list):

    for i in range(len(arr)):
        min = int(1e9)
        min_idx = -1
        for j in range(i, len(arr)):
            if min > arr[j]:
                min = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(solution(arr))


if __name__ == "__main__":
    main()
