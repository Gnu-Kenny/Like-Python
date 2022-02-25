import sys
input = sys.stdin.readline


def solution(numbers,k):
    stack = []

    for num in numbers:
        while stack:
            if stack[-1] < num:
                if k > 0:
                    stack.pop()
                    k-=1
                else:
                    break
            else:
                break

        stack.append(num)
    while k>0:
        stack.pop()
        k-=1
    return ''.join(stack)


def main():
    # number = "4177252841"
    # k = 4
    number = "1231234"
    k = 3
    # number = "1924"
    # k = 2
    # number = "1"
    # k = 1
    # number = "119"
    # k = 2
    # number = "10"
    # k=1
    print(solution(number, k))

if __name__ == "__main__":
    main()
