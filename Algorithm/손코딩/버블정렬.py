def solution(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

    return arr


def main():
    arr = [1, 4, 9, 2, 7, 8]
    print(solution(arr))


if __name__ == '__main__':
    main()
