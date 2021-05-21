# i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트
# zip
mylist = [83, 48, 13, 4, 71, 11]

# def solution(mylist):
#     answer = []
#     for i in range(len(mylist)-1):
#         answer.append(abs(mylist[i]-mylist[i+1]))
#     return answer


def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number2-number1))

    return answer


print(solution(mylist))
