arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

# list를 넣고 숫자를 찾는다.


def binarySearch(arr, targetNum):
    # 유틸 변수(도우미 변수)
    start = 0
    end = len(arr) - 1
    # 중간 인덱스
    midIndex = len(arr) // 2  # 5

    # 중간 인덱스 값 저장
    indexValue = arr[midIndex]

    # 중간 인덱스 값이 찾는 대상이면 중간 인덱스 리턴
    if indexValue == targetNum:
        return midIndex
    elif indexValue < targetNum:
        start = midIndex + 1
    elif indexValue > targetNum:
        end = midIndex - 1

    print("start :", start, "end :", end)
    return -1


# 1------5--8---11
# 5-----8--11
print(binarySearch(arr, 8))
