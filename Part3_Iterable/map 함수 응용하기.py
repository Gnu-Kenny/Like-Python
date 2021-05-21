# 정수를 담은 이차원 리스트 mylist의 각 원소의 길이를 담은 리스트를 리턴
# map
mylist = [[1, 2], [3, 4], [5]]


def solution(mylist):
    answer = list(map(len, mylist))
    return answer


print(solution(mylist))
