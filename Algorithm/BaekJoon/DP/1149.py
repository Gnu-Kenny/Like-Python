import sys
input = sys.stdin.readline


class Node:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b


def main():
    n = int(input())
    houses = []
    for _ in range(n):
        r, g, b = list(map(int, input().split(" ")))
        houses.append(Node(r, g, b))

    for i in range(1, n):
        houses[i].r = min(houses[i-1].g, houses[i-1].b) + houses[i].r
        houses[i].g = min(houses[i-1].r, houses[i-1].b) + houses[i].g
        houses[i].b = min(houses[i-1].r, houses[i-1].g) + houses[i].b

    print(min(min(houses[n-1].r, houses[n-1].g), houses[n-1].b))


if __name__ == "__main__":
    main()
