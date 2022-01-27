import sys
input = sys.stdin.readline


def main():
    n = int(input())

    towers = list(map(int, input().split()))
    stack = []
    for i in range(n):
        while stack and stack[-1][0] < towers[i]:
            stack.pop()
        if not stack:
            print(0, end=" ")
        else:
            print(stack[-1][1], end=" ")
        stack.append([towers[i], i+1])


if __name__ == "__main__":
    main()
