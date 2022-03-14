import sys
input = sys.stdin.readline


def main():
    n = int(input())

    areas = [0] * 1001
    for _ in range(n):
        w, h = map(int, input().split())
        areas[w] = h

    left_max_values = [0] * 1001

    for i in range(1, 1000+1):
        left_max_values[i] = max(left_max_values[i-1], areas[i])
    right_max_values = [0] * 1002
    for i in range(1000, -1, -1):
        right_max_values[i] = max(right_max_values[i+1], areas[i])
    sum = 0
    for i in range(1000+1):
        sum += min(left_max_values[i], right_max_values[i])

    print(sum)


if __name__ == "__main__":
    main()
