import sys
input = sys.stdin.readline

def main():
    n = int(input())
    steps = [0 for _ in range(300 + 1)]
    dp = [0 for _ in range(300 + 1)]
    for i in range(1,n+1):
        step = int(input())
        steps[i] = step

    dp[1] = steps[1]
    dp[2] = steps[1] + steps[2]
    dp[3] = max(steps[1] + steps[3], steps[2] + steps[3])
    for i in range(4,n+1):
        dp[i] = max(steps[i] + dp[i-2],steps[i] + steps[i-1] + dp[i-3])
    
    print(dp[n])

if __name__ == "__main__":
    main()