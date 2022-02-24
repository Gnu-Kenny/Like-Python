import sys
input = sys.stdin.readline

def main():
    alphabets = [['A','B','C'], ['D','E','F'], ['G','H','I'] \
                ,['J','K','L'], ['M','N','O'], ['P','Q','R','S'] \
                ,['T','U','V'],['W','X','Y','Z']]
    word = input().strip()
    answer = 0
    for alpha in word:
        for i,alphas in enumerate(alphabets,3):
            if alpha in alphas:
                answer += i
    print(answer)
if __name__ == "__main__":
    main()