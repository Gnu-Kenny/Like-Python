import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())

    q = deque([e for e in range(1,n+1)])
    
    while q:
        if len(q) == 1:
            print(q[0])
            break
        q.popleft()
        q.append(q.popleft())

if __name__ == "__main__":
    main()