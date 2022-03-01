import sys
input = sys.stdin.readline


visit = []
answer = 0

def dfs(begin:str, target:str, level:int, words:list, n:int):
    global visit, answer
    # 종료 시점
    if begin == target:
        answer = level
        return
    # 가지치기
    for i in range(n):
        if visit[i]:
            continue
        count_diff = 0
        for j,alpha in enumerate(words[i]):
            if begin[j] != alpha:
                if count_diff == 1:
                    count_diff += 1
                    break
                count_diff += 1
        if count_diff == 1:
            visit[i] = 1
            dfs(words[i], target, level + 1, words, n)
            visit[i] = 0


def solution(begin, target, words):
    global visit, answer
    n = len(words)
    visit = [0 for _ in range(len(words))]
    dfs(begin, target, 0, words, n)
    return answer

def main():
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    # return 4
    words = ["hot", "dot", "dog", "lot", "log"]
    # return 0
    print(solution(begin, target, words))

if __name__ == "__main__":
    main()
