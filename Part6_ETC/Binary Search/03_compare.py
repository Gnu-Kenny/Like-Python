arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]

# list를 넣고 숫자를 찾는다.


def binarySearch(arr, targetNum):
    # 중간 인덱스
    midIndex = len(arr) // 2  # 5
    # 중간 인덱스 값 저장
    indexValue = arr[midIndex]
    # 중간 인덱스 값이 찾는 대상이면 중간 인덱스 리턴
    if indexValue == targetNum:
        return midIndex
    print(midIndex, indexValue)
    return -1


print(binarySearch(arr, 8))
