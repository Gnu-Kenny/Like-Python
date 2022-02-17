import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [0 for _ in range(n + 1)] # 연산 횟수 저장
    for i in range(2,n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i],dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i],dp[i//3] + 1)
        if i % 5 == 0:
            dp[i] = min(dp[i],dp[i//5] + 1)
    
    print(dp[n])

if __name__ == '__main__':
    main()