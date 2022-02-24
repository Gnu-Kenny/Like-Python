import sys
input = sys.stdin.readline

def main():
    n = int(input())

    answer = 0
    for _ in range(n):
        
        word = input().strip()

        check = []
        flag = False
        if len(word) == 1:
            answer += 1
            continue
        for i,alpha in enumerate(word):
            if alpha not in check:
                check.append(alpha)

            elif alpha in check:
                if word[i-1] == alpha:
                    pass
                else:
                    flag = True
                    break
        if flag is not True:
            answer += 1
    
    print(answer)
if __name__ == "__main__":
    main()