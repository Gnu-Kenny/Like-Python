import sys
input = sys.stdin.readline
INF = int(1e9)
def main():
    global INF
    n, m = list(map(int, input().split()))
    nums = []
    dp = [INF for _ in range(m+1)]
    
    for _ in range(n):
        num = int(input())
        if num <= m:
            nums.append(num)
            dp[num] = 1

    for i in range(1,m+1):
        for num in nums:
            if i - num >= 0:
                dp[i] = min(dp[i],dp[i-num] + 1)
    if dp[m] != INF:
        print(dp[m])
    else:
        print(-1)

    
if __name__ == "__main__":
    main()