# https://www.acmicpc.net/problem/15658
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
operators = list(map(int,input().split())) # [+,-,x,//] 각 연산자들의 갯수
min_v = int(1e9)
max_v = int(-1e9)

def back(level:int, answer:int):
    global n, nums, operators, min_v, max_v
    if level == len(nums)-1:
        if min_v > answer:
            min_v = answer
        if max_v < answer:
            max_v = answer
        return
    
    for i in range(4):
        if operators[i] < 1:
            continue    
        # +
        if i == 0:
            operators[i] -= 1
            back(level + 1, answer + nums[level+1])
            operators[i] += 1
        # -
        elif i == 1:
            operators[i] -= 1
            back(level + 1, answer - nums[level+1])
            operators[i] += 1
        # *
        elif i == 2:
            operators[i] -= 1
            back(level + 1, answer * nums[level+1])
            operators[i] += 1
        # //
        elif i == 3:
            operators[i] -= 1
            back(level + 1, int(answer / nums[level+1]))
            operators[i] += 1

def main():
    global n, nums, operators, min_v, max_v

    back(0,nums[0])
    
    print(max_v)
    print(min_v)
    

if __name__ == "__main__":
    main()
