# 문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수
# map

mylist = ['1', '100', '33']


def solution(mylist):
    return list(map(int, mylist))


solution(mylist)
