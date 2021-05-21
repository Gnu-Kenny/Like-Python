import itertools
from functools import reduce
mylist = [['A', 'B'], ['X', 'Y'], ['1']]
#[[1], [2]]


def solution(mylist):
    #answer = [element for array in mylist for element in array]
    #answer = list(reduce(lambda x, y: x + y, mylist))
    answer = list(itertools.chain(*mylist))
    return answer


print(solution(mylist))
