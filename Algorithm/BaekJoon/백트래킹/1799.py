import sys
input = sys.stdin.readline

n = int(input())
board = []
count = 0
max_count = 0
points_black = []
points_white = []
black_chess_board = [[i,j] if i%2 == 0 else [i,j+1] for i in range(n) for j in range(0,n,2)]
white_chess_board = [[i,j] if i%2 == 1 else [i,j+1] for i in range(n) for j in range(0,n,2)]

class Node:
    def __init__(self, y, x):
        self.y, self.x = y, x


def put_or_pick_bishop(node: Node, board: list, put:bool):
    global n, points_black, points_white, black_chess_board, white_chess_board, max_count
    # 대각선 이동
    dy = (-1,1,1,-1)
    dx = (1,1,-1,-1)

    for i in range(4):
        ny = node.y
        nx = node.x
        
        while True:
            ny = ny + dy[i]
            nx = nx + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                break
            if put is True:
                board[ny][nx] += 1
            else:
                board[ny][nx] -= 1
    


def back(start:int, board: list, points: list, level:int):
    global n, points_black, points_white, black_chess_board, white_chess_board, max_count
    max_count = max(max_count, level)
    for i in range(start,len(points)):
        y, x = points[i]
        if board[y][x]:
            continue
        put_or_pick_bishop(Node(y,x), board, True)
        dfs(i+1, board, points, level + 1)
        put_or_pick_bishop(Node(y,x), board, False)

def main():
    global n, board, points_black, points_white, black_chess_board, white_chess_board, max_count

    for y in range(n):
        board_row = list(map(int,input().split()))
        for x,v in enumerate(board_row):
            if v == 1:
                if [y,x] in black_chess_board:
                    points_black.append((y,x))
                elif [y,x] in white_chess_board:
                    points_white.append((y,x))
        board.append(board_row)

    for y in range(n):
        for x in range(n):
            board[y][x] = 0 if board[y][x] else 1
            
    answer = 0
    back(0, board, points_black, 0)
    answer += max_count
    max_count = 0
    back(0, board, points_white, 0)
    answer += max_count
    print(answer)

if __name__ == "__main__":
    main()
