from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while scoville[0] < K:
        first_food = heappop(scoville)
        if len(scoville) == 0:
            if first_food < K:
                return -1
            else:
                answer += 1
                break
        elif len(scoville) == 1:
            if first_food + scoville[0] * 2 < K:
                return -1
            else:
                answer += 1
                break
        else:
            new_food = first_food + heappop(scoville) * 2
            heappush(scoville, new_food)
            answer += 1
        
    return answer


def main():
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))

if __name__ == "__main__":
    main()