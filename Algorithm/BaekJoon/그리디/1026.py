import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    sum_num = 0
    for i in range(n):
        sum_num += a[i] * b[i]

    print(sum_num)

if __name__ == "__main__":
    main()