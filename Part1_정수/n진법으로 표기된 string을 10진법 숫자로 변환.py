# base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.
# int(str, base)
num, base = 12, 3
num = str(num)

#print(int(num, base))

answer = 0
for i, number in enumerate(num[::-1]):
    answer += int(number) * (base ** i)

print(answer)
