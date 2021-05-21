from math import sqrt

multiplied = 1
for i in range(5):
    a = int(input())

    multiplied *= a

if sqrt(multiplied)**2 == multiplied:
    print("found")
else:
    print("not found")
