import sys
input = sys.stdin.readline
def main():
    pocketmon_dict = {}
    n, m = list(map(int,input().split()))
    for i in range(1,n+1):
        pocketmon = input()
        pocketmon_dict[i] = pocketmon[:-1]

    values = list(pocketmon_dict.values())
    for _ in range(m):

        quiz = input()[:-1]
        if quiz.isdigit():
            print(pocketmon_dict[int(quiz)])
        else:
            print(values.index(quiz)+1)
    

if __name__ == "__main__":
    main()