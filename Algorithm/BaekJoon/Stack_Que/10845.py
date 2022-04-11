# https://www.acmicpc.net/problem/10845
import sys
input = sys.stdin.readline

def main():
    list = []
    for _ in range(int(input())):
        cmd = input().split()

        if "push" in cmd:
            list.append(int(cmd[1]))
        elif "front" in cmd:
            if list:
                print(int(list[0]))
            else:
                print(-1)
        elif "back" in cmd:
            if list:
                print(int(list[-1]))
            else:
                print(-1)
        elif "size" in cmd:
            if list:
                print(len(list))
            else:
                print(0)
        elif "pop" in cmd:
            if list:
                print(int(list.pop(0)))
            else:
                print(-1)
        elif "empty" in cmd:
            if list:
                print(0)
            else:
                print(1)
if __name__ == '__main__':
    main()
    