# https://www.acmicpc.net/problem/9461
import sys
input = sys.stdin.readline

def main():
    dp = [0 for _ in range(100+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    for i in range(5, 100 + 1):
        dp[i] = dp[i-1] + dp[i-5]
    for _ in range(int(input())):
        print(dp[int(input())])

if __name__ == "__main__":
    main()