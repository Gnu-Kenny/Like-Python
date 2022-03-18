import sys
input = sys.stdin.readline


def main():
    a_string = [0] + list(input().strip())
    b_string = [0] + list(input().strip())
    n = len(b_string)
    m = len(a_string)
    lcs = [[0 for _ in range(m)] for _ in range(n)]
    max_length = 0
    for i in range(1, n):
        for j in range(1, m):
            if b_string[i] == a_string[j]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    max_length = lcs[n-1][m-1]

    y, x = n - 1, m - 1
    answer = []
    while y >= 0 and x >= 0:
        if lcs[y-1][x] == lcs[y][x]:
            y -= 1
            continue
        if lcs[y][x-1] == lcs[y][x]:
            x -= 1
            continue
        answer.append(a_string[x])
        y -= 1
        x -= 1

    print(max_length)
    answer = answer[::-1]
    if len(answer) != 0:
        print(''.join(answer))


if __name__ == "__main__":
    main()
