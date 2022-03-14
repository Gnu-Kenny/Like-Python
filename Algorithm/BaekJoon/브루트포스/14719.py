import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    arr = [0] + list(map(int, input().split())) + [0]

    left_max_values = [0] * (m+1)
    right_max_values = [0] * (m+2)
    
    for i in range(1, m+1):
        left_max_values[i] = max(left_max_values[i-1], arr[i])
    for i in range(m, -1, -1):
        right_max_values[i] = max(right_max_values[i+1], arr[i])

    sum = 0
    for i in range(1, m+1):
        sum += min(left_max_values[i], right_max_values[i]) - arr[i]

    print(sum)


if __name__ == "__main__":
    main()
