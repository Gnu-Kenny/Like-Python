import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)
ans = ""
cnt = 0
answers = []


class Node:
    def __init__(self, y, x, level):
        self.y, self.x = y, x
        self.level = level


def back(node: Node):
    global board, dy, dx, ans, cnt, answers
    if node.level == 6:
        if ans not in answers:
            answers.append(ans)
            cnt += 1
        return
    for i in range(4):
        ny = node.y + dy[i]
        nx = node.x + dx[i]

        if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
            continue
        ans += str(board[ny][nx])
        back(Node(ny, nx, node.level+1))
        ans = ans[:-1]


def main():
    global board, ans, cnt, answers

    for y in range(5):
        for x in range(5):
            back(Node(y, x, 0))

    print(cnt)


if __name__ == "__main__":
    main()
