import sys
input = sys.stdin.readline
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0


# branch : 보드판 열
# level : 보드판 행


def put_or_pick(y, x, put_or_pick: bool):

    global n, board, cnt
    dy = [1, 1, 1]  # 인덱스 1부터 유의미한 이동의 의미를 가짐
    dx = [-1, 0, 1]
    # 행, 열, 대각선 검사
    for i in range(0, 3):
        for j in range(1, n):
            ny = y + dy[i]*j
            nx = x + dx[i]*j
            if ny > n-1 or ny < 0 or nx > n-1 or nx < 0:
                break

            if put_or_pick == True:
                board[ny][nx] += 1
            else:
                board[ny][nx] -= 1


def back(level: int):
    global n, board, cnt
    # 종료 시점
    # board에 0이 없을 때
    if level == n:
        cnt += 1
        return

    # 가지치기
    # 보드 판의 열
    for i in range(n):
        # 유효성 검사를 만족한다면
        y, x = level, i
        if board[y][x] != 0:
            continue

        put_or_pick(y, x, 1)
        back(level + 1)
        put_or_pick(y, x, 0)


back(0)
print(cnt)
