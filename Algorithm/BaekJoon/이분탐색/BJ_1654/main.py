import sys
input = sys.stdin.readline


def main():
    k, n = map(int, input().split())
    lans = [int(input()) for _ in range(k)]
    max_l = 0
    
    lans.sort()
    
    s = 1
    e = lans[-1]
    m = (s + e) // 2 
    
    while s <= e:
        cnt = 0 
        
        for l in lans:
            cnt += (l // m)
        
        if cnt < n:
            e = m - 1
        elif cnt >= n:
            s = m + 1
            max_l = max(max_l, m)
        
        m = (s + e) // 2 

    print(max_l)


if __name__ == '__main__':
    main()