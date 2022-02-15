import sys
input = sys.stdin.readline

def main():
    n = int(input())
    sqnc = []
    stack = []
    count = 1
    flag = True
    for _ in range(n):
        e = int(input())
        if e in stack:
            if stack[-1] == e:
                sqnc.append('-')
                stack.pop()
            else:
                flag = False
                
        elif e not in stack:
            for i in range(count, e+1):
                sqnc.append('+')
                stack.append(i)
                count+=1
            sqnc.append('-')
            stack.pop()
    if flag is not False:
        for e in sqnc:
            print(e)
    else:
        print("NO")
    
if __name__ == "__main__":
    main()