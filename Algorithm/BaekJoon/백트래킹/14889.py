import sys
input = sys.stdin.readline


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [0 for _ in range(n)]
min_ability_gap = int(1e9)


def dfs(start: int, level: int):
    global n, board, visit, min_ability_gap
    if level == n//2:
        sum_start_team = 0
        sum_link_team = 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    sum_start_team += board[i][j]
                elif visit[i] == 0 and visit[j] == 0:
                    sum_link_team += board[i][j]

        min_ability_gap = min(min_ability_gap, abs(
            sum_start_team - sum_link_team))

        return
    for i in range(start, n):
        if visit[i]:
            continue
        visit[i] = 1
        dfs(i+1, level + 1)
        visit[i] = 0


def main():
    global n, board, visit, min_ability_gap

    dfs(0, 0)

    print(min_ability_gap)


if __name__ == "__main__":
    main()
