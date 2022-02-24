import sys
input = sys.stdin.readline

def main():
    n = int(input())

    array = list(map(int,list(input().strip())))
    print(sum(array))

if __name__ == "__main__":
    main()