# https://www.acmicpc.net/problem/11054
from copy import deepcopy
import sys
input = sys.stdin.readline

class Max_Num:
    def __init__(self,i,v):
        self.i = i
        self.v = v

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    reversed_arr = deepcopy(arr)
    for i in range(n//2):
        reversed_arr[i], reversed_arr[n-i-1] = reversed_arr[n-i-1], reversed_arr[i]
    dp = [1 for _ in range(n)]
    increased_dp = deepcopy(dp)
    decreased_dp = deepcopy(dp)
    increased_dp[0] = 1 
    decreased_dp[0] = 1
    for i in range(1, n):
        
        for j in range(i):
            if arr[j] < arr[i]:
                increased_dp[i] = max(increased_dp[i], increased_dp[j]+1)
            if reversed_arr[j] < reversed_arr[i]:
                decreased_dp[i] = max(decreased_dp[i], decreased_dp[j]+1)

    for i in range(n//2):
        decreased_dp[i], decreased_dp[n-i-1] = decreased_dp[n-i-1], decreased_dp[i]

    for i in range(n):
        dp[i] = increased_dp[i] + decreased_dp[i]
    print(max(dp)-1)
if __name__ == '__main__':
    main()
