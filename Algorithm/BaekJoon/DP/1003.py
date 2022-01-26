import sys
input = sys.stdin.readline


class Node:
    def __init__(self, zero, one):
        self.zero, self.one = zero, one


def main():
    # 피보나치 수열에서 0은 0을 1번 호출, 1은 0번 호출하고 1은 0을 0번 호출, 1을 한번 호출한다.
    dp = [Node(1, 0), Node(0, 1)]

    for i in range(2, 41):
        dp_zero = dp[i-1].zero + dp[i-2].zero
        dp_one = dp[i-1].one + dp[i-2].one
        dp.append(Node(dp_zero, dp_one))

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dp[n].zero, dp[n].one)


if __name__ == "__main__":
    main()
