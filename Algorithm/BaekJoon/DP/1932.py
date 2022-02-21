# https://www.acmicpc.net/problem/1932
import sys
input = sys.stdin.readline

def main():
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    dp = [[0 for _ in range(len(arr_row))] for arr_row in arr]
    dp[0][0] = arr[0][0]
    
    for i in range(1, len(arr)):
        for j in range(i + 1):
            if i == 1 and j == 0:
                dp[i][j] = arr[i-1][j] + arr[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            elif j == len(arr[i])-1:
                dp[i][j] = dp[i-1][j-1] + arr[i][j]
            else:
                dp[i][j] = max(dp[i][j], arr[i][j] + dp[i-1][j-1], arr[i][j] + dp[i-1][j])
    
    print(max(dp[len(dp)-1]))
if __name__ == "__main__":
    main()