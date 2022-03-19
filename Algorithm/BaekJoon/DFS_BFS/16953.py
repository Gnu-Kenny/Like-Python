import sys
input = sys.stdin.readline
n = 0
answer = 0
def dfs(level:int, n:int):
    if n >= answer:
        if n == answer:
            print(level+1)
            exit(0)
        return
    
    dfs(level+1, n*2)
    dfs(level+1, n*10+1 )
def main():
    global n, answer
    n, answer = list(map(int,input().split()))

    dfs(0,n)

    print(-1)

if __name__ == "__main__":
    main()