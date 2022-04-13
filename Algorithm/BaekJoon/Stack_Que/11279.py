import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def main():
    
    q = []
    for _ in range(int(input())):
        n = int(input())

        if n == 0:
            if q:
                print(-q[0])
                heappop(q)
            else:
                print(0)
        else:
            heappush(q,-n)
if __name__ == '__main__':
    main()
    