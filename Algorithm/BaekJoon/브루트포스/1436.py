# https://www.acmicpc.net/problem/1436
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    num_the_end = 0
    count = 0
    while True:
        num_the_end += 1
        if str(num_the_end).find("666") != -1:
            count+=1
        if count == n:
            break
    print(num_the_end)
                

if __name__ == "__main__":
    main()