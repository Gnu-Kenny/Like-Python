# https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    n_list = list(map(int,input().split()))
    m = int(input())
    m_list = list(map(int,input().split()))

    for e in m_list:
        if e not in n_list:
            print(0)
        else:
            print(1)

    print()
if __name__ == "__main__":
    main()