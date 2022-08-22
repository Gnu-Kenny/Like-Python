
# arr에서 value 찾기
answer = False


def is_target_exist(arr: list, target: int):
    global answer
    if len(arr) <= 1:
        return
    mid = arr[len(arr)//2]

    if target < mid:
        is_target_exist(arr[:len(arr)//2], target)
    elif target > mid:
        is_target_exist(arr[len(arr)//2:], target)
    else:
        answer = True
        return

    return


def main():
    global answer
    arr = [i for i in range(1, 1000 + 1)]
    target = 1000

    is_target_exist(arr, target)

    print(answer)


if __name__ == "__main__":
    main()
