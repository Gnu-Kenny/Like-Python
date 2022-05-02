import sys
input = sys.stdin.readline


def main():
    goal = int(input()) - 1
    if goal == 0:
        print(1)
        return
    i = 1
    while True:
        if goal <= i*6:
            print(i+1)
            break
        goal -= i*6
        i += 1


main()
