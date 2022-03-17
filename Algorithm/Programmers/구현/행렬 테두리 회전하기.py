import sys
input = sys.stdin.readline

board = []


def rotate(y1, x1, y2, x2):
    global board
    cached_num = 0
    prev_col = 0
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if i == y1:
                if j == x1:
                    prev_col = board[i][j]
                    board[i][j] = board[i+1][j]
                else:
                    cached_num = board[i][j]
                    board[i][j] = prev_col
                    prev_col = cached_num
            elif i == y2:
                if j < x2-1:
                    board[i][j] = board[i][j+1]
                elif j == x2-1:
                    board[i][j] = board[i][j+1]
                    board[i][j+1] = prev_col
            else:
                if j == x1:
                    if i < y2:
                        board[i][j] = board[i+1][j]
                elif j == x2:
                    cached_num = board[i][j]
                    board[i][j] = prev_col
                    prev_col = cached_num


def find_min_value(y1, x1, y2, x2):
    min_value = int(1e9)
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if i == y1 or i == y2 or j == x1 or j == x2:
                min_value = min(min_value, board[i][j])
    return min_value


def solution(rows, columns, queries):
    global board
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = num
            num += 1
    answer = []
    for y1, x1, y2, x2 in queries:

        rotate(y1-1, x1-1, y2-1, x2-1)
        answer.append(find_min_value(y1-1, x1-1, y2-1, x2-1))

    return answer


def main():
    rows = 6
    columns = 6
    queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
    rows = 3
    columns = 3
    queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
    # rows = 100
    # columns = 97
    # queries = [[1, 1, 100, 97]]
    print(solution(rows, columns, queries))


if __name__ == "__main__":
    main()
