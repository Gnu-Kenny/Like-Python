# LIS응용 
# Longest Increasing Subsequence, 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [1 for _ in range(n)]

    for i in range(n):

        for j in range(i):
            if arr[j] >= arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(n-max(dp))

if __name__ == "__main__":
    main()