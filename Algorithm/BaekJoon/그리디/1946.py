from heapq import heappush as hpush
from heapq import heappop as hpop
import sys
input = sys.stdin.readline


class Applicant:
    def __init__(self, doc, interv):
        self.doc = doc
        self.interv = interv

    def __lt__(self, other):
        return self.doc < other.doc

    def __repr__(self):
        return f'Aplication({self.doc}, {self.interv})'


def main():

    for _ in range(int(input())):
        n = int(input())
        applicants = []
        for _ in range(n):
            d, i = map(int, input().split())  # document, interview scores
            hpush(applicants, Applicant(d, i))

        candidate_rank = 0
        answer = 0
        while applicants:
            first = hpop(applicants)
            if candidate_rank == 0 or candidate_rank > first.interv:
                candidate_rank = first.interv
                answer += 1
        print(answer)


if __name__ == "__main__":
    main()
