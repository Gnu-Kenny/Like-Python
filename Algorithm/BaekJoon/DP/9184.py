import sys
input = sys.stdin.readline

dp = [[[0]*(20 + 1) for _ in range(20 + 1)] for _ in range(20 + 1)]
def w(a : int, b : int, c : int):
    global dp
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]
    

def main():
    global dp
    while True:
        a,b,c = map(int,input().split())
        if a == -1 and b == -1 and c == -1:
            return

        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

if __name__ == "__main__":
    main()