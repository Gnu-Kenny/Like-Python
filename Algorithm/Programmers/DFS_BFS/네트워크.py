import sys
input = sys.stdin.readline

visit = []
alist = []
def dfs(network:list):
    global visit, alist
    for computer in network:
        if visit[computer]:
            continue
        visit[computer] = 1
        dfs(alist[computer])
def solution(n, computers):
    global visit, alist
    visit = [0 for _ in range(n)]
    alist = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                alist[i].append(j)
    answer = 0
    for i in range(n):
        if visit[i] == 0:
            answer += 1
            dfs(alist[i])
    
    return answer

def main():
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	
    print(solution(n, computers))

if __name__ == "__main__":
    main()