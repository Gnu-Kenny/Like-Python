import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())

    a = 1
    for _ in range(m):
        a *= n
        n -= 1
    b = 1
    for i in range(1,m+1):
        b *= i
    
    print(a//b)
    

if __name__ == "__main__":
    main()