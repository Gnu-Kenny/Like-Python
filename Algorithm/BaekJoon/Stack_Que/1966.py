# https://www.acmicpc.net/problem/1966
import sys
input = sys.stdin.readline
from collections import deque


def main():
    t = int(input())

    for _ in range(t):

        doc_num, doc_index = list(map(int,input().split()))
        docs_priority = list(map(int,input().split()))
        
        q = deque()
        for i, v in enumerate(docs_priority):
            q.append((i,v))
        docs_priority.sort()

        num = 1

        while q:
            now = q.popleft()
            
            if now[1] < docs_priority[len(docs_priority)-1]:
                q.append(now)
            else:
                if now[0] == doc_index:
                    print(num)
                    break
                docs_priority.pop()
                num += 1
        

if __name__ == "__main__":
    main()