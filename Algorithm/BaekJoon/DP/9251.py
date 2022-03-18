# https://www.acmicpc.net/problem/9251
# LCS(Longest Common Subsequence)
import sys
input = sys.stdin.readline


def main():
    a = [0] + list(input().strip())
    b = [0] + list(input().strip())
    max_subseq_len = 0
    lcs = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

    for i in range(1, len(b)):
        for j in range(1, len(a)):
            if b[i] == a[j]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

            if max_subseq_len < lcs[i][j]:
                max_subseq_len = lcs[i][j]

    print(max_subseq_len)


if __name__ == "__main__":
    main()
