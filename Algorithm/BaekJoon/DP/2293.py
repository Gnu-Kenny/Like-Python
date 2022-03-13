def main():
    n, k = map(int, input().split())
    money_values = []
    dp = [0 for _ in range(k+1)]
    for _ in range(n):
        money_values.append(int(input()))
    dp[0] = 1
    for money_value in money_values:
        for i in range(money_value, k + 1):
            dp[i] += dp[i-money_value]

    print(dp[k])


if __name__ == "__main__":
    main()
