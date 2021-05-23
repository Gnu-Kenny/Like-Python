# 숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
# 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력

from math import sqrt

multiplied = 1
for i in range(5):
    a = int(input())

    multiplied *= a

    if multiplied == int(sqrt(multiplied))**2:
        print("found")
        break
else:
    print("not found")
