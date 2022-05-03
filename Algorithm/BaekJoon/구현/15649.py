import sys
input = sys.stdin.readline
n = 0
m = 0
arr = []

def dfs(i, level: int):
    global n,m, arr
    if level == m:
        print(*arr)
        return
    for e in range(1,n+1):
        if e in arr:
            continue
        arr.append(e)
        dfs(i+1, level + 1)
        arr.pop()

def main():
    global n, m, arr
    n, m = map(int,input().split())
    
    dfs(1,0)

if __name__ == "__main__":
    main()