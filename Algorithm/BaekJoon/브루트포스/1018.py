# https://www.acmicpc.net/problem/1018 

import sys
input =  sys.stdin.readline

chess_w = [['W',"B"] * 4 if i % 2 == 0 else ['B',"W"] * 4 for i in range(8)]
chess_b = [['B',"W"] * 4 if i % 2 == 0 else ['W',"B"] * 4 for i in range(8)]
def painting(chess_board: list):
    global chess_w, chess_b

    count_on_chess_w = 0
    count_on_chess_b = 0
    for y in range(8):
        for x in range(8):
            if chess_board[y][x] != chess_w[y][x]:
                count_on_chess_w += 1
            if chess_board[y][x] != chess_b[y][x]:
                count_on_chess_b += 1

    return min(count_on_chess_w,count_on_chess_b)


def main():
    INF = int(1e9)
    min_painting_count = INF
    n, m = list(map(int,input().split())) # N : 세로, M : 가로
    board = []

    for _ in range(n):
        board.append(list(input()[:-1]))
    
    for i in range(n-8 + 1):
        for j in range(m-8 + 1):
            # 체스판 자르기 # chess_board = board[i:i+8][j:j+8] 가 잘 동작하지 않음.
            chess_board = []
            for k in range(i,8+i):
                chess_board.append(board[k][j:j+8])
            
            min_painting_count = min(min_painting_count, painting(chess_board))
    
    print(min_painting_count)

if __name__ == "__main__":
    main()