import sys
input = sys.stdin.readline
import heapq

def main():
    n = int(input())
    q = []
    answer = 0
    for _ in range(n):
        heapq.heappush(q,int(input()))
    
    if n == 1:
        print(0)
    else:
        while len(q) > 1:
            now = heapq.heappop(q)
            next = heapq.heappop(q)
            answer += (now + next)
            heapq.heappush(q, now + next)

        print(answer)
if __name__ == "__main__":
    main()