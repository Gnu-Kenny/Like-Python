# https://www.acmicpc.net/problem/1339

from collections import defaultdict
import string
import sys
input = sys.stdin.readline

def main():
    # dictionary 초기화
    d = defaultdict(int)
    for alpha, _ in zip(string.ascii_uppercase, [_ for _ in range(10)]):
        d[alpha] # ex {A: 0, B: 1 ..}
    # 입력값들 저장
    words = []
    for _ in range(int(input())):
        word = input().strip()
        words.append(word)
        
    # 알파벳의 종류는 중요하지 않다.
    # 알파벳의 자리에 따라 자리수 값을 더한다.
    for word in words:
        for i, alpha in enumerate(word):
            num = 10 ** (len(word) - i - 1)
            d[alpha] += num
    
    answer = 0
    d_values = list(filter(lambda x: x>0, d.values()))
    sorted_d_values = sorted(d_values, reverse=True)
    for i,v in enumerate(sorted_d_values):
        answer += v * (9-i)
    
    print(answer)
    
if __name__ == "__main__":
    main()