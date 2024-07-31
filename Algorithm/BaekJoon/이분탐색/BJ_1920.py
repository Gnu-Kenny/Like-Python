import sys
input = sys.stdin.readline

def main():
    """
    0 10 20 30 40 50 60 70 
    s       m           e
            s     m     e
    target 50
    
    # s_idx 0
    # e_idx 7
    # mid_idx = 0 + 7 // 2 = 3
    
    list[mid_idx] < m
        s = m
        m = (m + e) // 2   3 + 7 // 2 = 5
    """
    # init
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))
    
    n_list.sort()
    
    for tgt in m_list:
    
        s_idx = 0
        e_idx = n-1
        mid_idx = (s_idx + e_idx) // 2
        
        result = 0
        while s_idx <= e_idx:
            if n_list[mid_idx] < tgt:
                s_idx = mid_idx + 1
            elif n_list[mid_idx] > tgt:
                e_idx = mid_idx - 1        
            else:
                result = 1
                break
            
            mid_idx = (s_idx + e_idx) // 2

        print(result)
    

if __name__ == '__main__':
    main()