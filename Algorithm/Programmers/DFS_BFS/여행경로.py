from collections import defaultdict
import sys
input = sys.stdin.readline

path = []
start_destinations = defaultdict(list)
tickets = []
answer = []

def solution(tickets):
    global path, start_destinations, answer
    for ticket in tickets:
        s, e = ticket
        start_destinations[s].append(e)

    for start in start_destinations:
        start_destinations[start].sort(reverse=True)
    
    stack = ['ICN']
    path = []

    while stack:
        top = stack[-1]

        if top not in start_destinations or len(start_destinations[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(start_destinations[top][-1])
            start_destinations[top] = start_destinations[top][:-1]
    
    return path[::-1]


def main():
    # tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets))

if __name__ == "__main__":
    main()