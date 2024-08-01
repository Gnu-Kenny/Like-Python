import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

def main():
    global n, m, arr
    """
4 2
9 8 7 1
    """
    arr.sort()
    
    back(0, 0)
    
    
def back(depth, idx):
    global n, m, arr, result
    
    if depth >= m:
        print(*result)
        return

    for i in range(idx, n):
        result.append(arr[i])
        back(depth+1, i)
        result.pop()


if __name__ == '__main__':
    main()