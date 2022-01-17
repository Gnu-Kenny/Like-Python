# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다.
# 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.


from collections import defaultdict
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, name, count):
        self.name = name
        self.count = count


table = defaultdict(Node)


def findBoss(a: str):
    global table
    if table[a].name == "":
        return a
    table[a].name = findBoss(table[a].name)

    return table[a].name


def setUnion(a: str, b: str):
    global table
    aBoss = findBoss(a)
    bBoss = findBoss(b)

    if aBoss != bBoss:
        table[bBoss].name = aBoss
        table[aBoss].count += table[bBoss].count

    return table[aBoss].count


def main():
    global table
    t = int(input())

    for _ in range(t):
        n = int(input())

        for _ in range(n):
            friend1, friend2 = input().split()
            # 등록이 안되어 있다면 등록
            if table.get(friend1) is None:
                table[friend1] = Node("", 1)  # Boss, 친구 수 (나포함)
            if table.get(friend2) is None:
                table[friend2] = Node("", 1)  # Boss, 친구 수 (나포함)

            print(setUnion(friend1, friend2))

        table.clear()


if __name__ == "__main__":
    main()
