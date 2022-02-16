# https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline
def main():
    n, k = list(map(int,input().split()))

    money = []

    for _ in range(n):
        money_value = int(input())
        if money_value <= k:
            money.append(money_value)
    count = 0
    money.sort(reverse=True)
    for v in money:
        if k >= v:
            count += k//v
            k%=v
        if k == 0:
            break
    
    print(count)
if __name__ == '__main__':
    main()
    