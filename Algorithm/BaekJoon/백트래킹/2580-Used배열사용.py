import sys
input = sys.stdin.readline

table = [list(map(int, input().split())) for _ in range(9)]
points = [(i, j) for i in range(9) for j in range(9) if table[i][j] == 0]
row = [[0 for _ in range(9)] for _ in range(9)]
col = [[0 for _ in range(9)] for _ in range(9)]
mini_table = [[0 for _ in range(9)] for _ in range(9)]

flag = False
# level
# branch

for i in range(9):
    for j in range(9):
        if table[i][j]:
            # 각 배열의 인덱스는 스도쿠 값 - 1에 해당하고 i열에 존재하는 스도쿠 값을 저장한다.
            row[i][table[i][j] - 1] = 1
            # 각 배열의 인덱스는 스도쿠 값 - 1에 해당하고 j행에 존재하는 스도쿠 값을 저장한다. j번째 열이 col배열의 행으로 매핑된다.
            col[j][table[i][j] - 1] = 1
            #  좌측 상단부터 우측 하단 까지의 9개의 스도쿠 3x3 판을 mini_table 배열의 0 ~ 8행까지 차례대로 맵핑
            mini_table[(i//3)*3 + j//3][table[i][j]-1] = 1


def backtracking(level):
    global flag, row, col, mini_table
    if flag:
        return
    if level == len(points):
        for row in table:

            print(' '.join(map(str, row)))
        flag = True
        exit(0)

    y, x = points[level]
    # 0 ~ 8까지의 반복문과 비어있는 칸의 좌표 y,x를 통해
    # y번째 row에서 사용하지 않은 스도쿠 값,
    # x번째 col에서 사용하지 않은 스도쿠 값,
    #  y//3*3 + x//3 번째 minimap에서 사용하지 않은 스도쿠 값
    for i in range(0, 8+1):
        # 스도쿠 값 i를 사용했다면
        if row[y][i] or col[x][i] or mini_table[y//3*3 + x//3][i]:
            continue
        row[y][i] = 1
        col[x][i] = 1
        mini_table[y//3*3 + x//3][i] = 1
        table[y][x] = i+1
        backtracking(level + 1)
        row[y][i] = 0
        col[x][i] = 0
        mini_table[y//3*3 + x//3][i] = 0
        table[y][x] = 0


backtracking(0)
