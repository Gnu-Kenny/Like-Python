# https://www.acmicpc.net/problem/11727
# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

def main():
    n = int(input())

    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    if n == 1:
        print(dp[1])
        return
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
    
    print(dp[n] % 10007)
if __name__ == "__main__":
    main()