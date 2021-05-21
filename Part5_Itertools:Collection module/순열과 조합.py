from itertools import permutations

mylist = [1, 2]


def solution(mylist):
    return list(map(list, permutations(sorted(mylist), len(mylist))))


print(solution(mylist))
