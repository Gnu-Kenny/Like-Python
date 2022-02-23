# https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    roads = list(map(int,input().split())) + [0]
    prices = list(map(int,input().split())) 
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            prices[i] = prices[i-1]
    dp = [0 for _ in range(100000+1)] # 도시별 주유 누적합

    dp[0] = prices[0] * roads[0]
    
    for i in range(1,n):
        dp[i] = dp[i-1] + roads[i] * prices[i]
    print(dp[n-1])


if __name__ == "__main__":
    main()