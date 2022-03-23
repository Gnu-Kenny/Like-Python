from collections import deque
import sys
input = sys.stdin.readline


def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    while q:
        if len(q) >= 2:
            now = q.pop()
            lmt = limit-now
            for _ in range(len(q)):
                if q[0] <= lmt:
                    lmt-=q[0]
                    q.popleft()
                else:
                    answer += 1
                    break
                if len(q) == 0:
                    answer += 1
                    break
        elif len(q) == 1: # 0, 1
            answer += 1
            q.popleft()
        else:
            answer 
    return answer
    
def main():
    people = [70, 50, 80, 50]
    # people = [30,50, 50, 70, 100]
    # people = [50, 70, 80]
    limit = 100
    print(solution(people, limit)  )

if __name__ == "__main__":
    main()