from collections import Counter


my_str = 'dfdefdgf'
biggestValue = sorted(list(dict(Counter(my_str)).values()), reverse=True)[0]

# items => dictionary의 key-value pairs를 튜플로 반환
answer = [i for i, k in dict(Counter(my_str)).items() if k == biggestValue]
answer = ''.join(sorted(answer))
print(answer)
