# https://www.acmicpc.net/problem/1904
import sys
input = sys.stdin.readline

def main():
    dp = [0 for _ in range(1000000 + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3,1000000 + 1):
        dp[i] = (dp[i-2] + dp[i-1] ) % 15746
    
    n = int(input())

    print(dp[n])
if __name__ == "__main__":
    main()