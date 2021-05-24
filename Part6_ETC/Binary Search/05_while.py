arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

# list를 넣고 숫자를 찾는다.


def binarySearch(arr, targetNum):
    # 유틸 변수(도우미 변수)
    start = 0
    end = len(arr) - 1
    while (start <= end):
        # 중간 인덱스
        midIndex = (start + end) // 2  # midIndex 값 변경

        # 중간 인덱스 값이 찾는 대상이면 중간 인덱스 리턴
        if arr[midIndex] == targetNum:
            return midIndex
        elif arr[midIndex] < targetNum:
            start = midIndex + 1
        elif arr[midIndex] > targetNum:
            end = midIndex - 1

        # print("start :", start, "end :", end)
    return -1


# 1------5--8---11
# 5-----8--11
print(binarySearch(arr, 8))
