def main():
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    dp[1] = max(arr[0],arr[1]) # arr[0] 현재 위치의 식량을 털지 않고 앞 식량을 턴 량, arr[1] 현재 위치의 식량을 턴 양
    
    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
    print(dp[n-1])


if __name__ == '__main__':
    main()