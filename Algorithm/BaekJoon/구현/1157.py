from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    word = list(input().strip().lower())
    alphabets = defaultdict(int)
    max_num = 0
    for alpha in word:
        alphabets[alpha] += 1
        max_num = max(max_num,alphabets[alpha])

    answer = []
    for alphabet,count in alphabets.items():
        if count == max_num:
            answer.append([count, alphabet])

    if len(answer) > 1:
        print('?')
        return
    print(answer[0][1].capitalize())
    
    
if __name__ == "__main__":
    main()