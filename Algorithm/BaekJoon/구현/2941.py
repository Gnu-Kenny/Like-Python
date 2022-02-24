import sys
input = sys.stdin.readline

def main():
    croatias = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    word = input().strip()
    answer = 0

    for i,alpha in enumerate(word):
        if len(word) >= 3 and word[0:3] in croatias:
            word = word[3:]
            answer +=1
            continue
        if len(word) >= 2 and word[0:2] in croatias:
            word = word[2:]
            answer +=1
            continue
        if len(word) >= 1:
            word = word[1:]
            answer +=1
    print(answer)
if __name__ == "__main__":
    main()