import sys
input = sys.stdin.readline

def main():
    meetings = []
    for _ in range(int(input())):
        s,e = list(map(int,input().split()))
        meetings.append([s,e])
    
    meetings.sort(key=lambda x: (x[1],x[0]))
    answer = 0
    count = 0
    for meeting in meetings:
        if answer <= meeting[0]:
            answer = meeting[1]
            count += 1
    
    print(count)
if __name__ == '__main__':
    main()