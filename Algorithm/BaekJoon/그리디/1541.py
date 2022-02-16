import sys
input = sys.stdin.readline

def main():
    equation = input().rstrip().split('-')

    for i,v in enumerate(equation):
        if i == 0:
            sum_equation = sum(list(map(int,equation[0].split('+'))))
            continue
        v = list(map(int,v.split('+')))
        sum_v = sum(v)
        
        sum_equation -= sum_v
        
    print(sum_equation)


if __name__ == "__main__":
    main()