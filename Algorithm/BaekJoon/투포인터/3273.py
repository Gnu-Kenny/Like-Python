import sys
input = sys.stdin.readline


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    arr.sort()
    answer = 0
    for i in range(n):
        s = arr[i]
        for j in range(i+1, n):
            if s + arr[j] == x:
                answer += 1
            elif s + arr[j] > x:
                break

    # for i in range(n):
    #     for j in range(i+1, n):
    #         if arr[i] + arr[j] == x:
    #             answer += 1

    print(answer)


if __name__ == "__main__":
    main()
