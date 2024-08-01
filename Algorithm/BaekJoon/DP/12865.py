import sys
input = sys.stdin.readline

"""12865
4 7
6 13
4 8
3 6
5 12
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
      0     1   2   3   4   5   6   7
 0    0     0   0   0   0   0   0   0       
6 13  0     0   0   0   0   0   13  13
4 8   0     0   0   0   8   8   13  13
3 6   0     0   0   6   8   8   13  14
5 12  0     0   0   6   8   12  13  14  


"""

def main():
    n, k = map(int, input().split())  # 물품 수, 최대 무게 
    items = [list(map(int, input().split())) for _ in range(n)]
    
    dp_table = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        w, v = items[i-1][0], items[i-1][1]
        for j in range(1, k+1):
            if j >= w:
                #하나만 체크하면 될듯
                # 물건을 담을 수 있는 경우
                dp_table[i][j] = max(dp_table[i-1][j - w] + v, dp_table[i-1][j])
            else:
                # 물건을 담을 수 없는 경우
                dp_table[i][j] = dp_table[i-1][j] 
        
    print(dp_table[n][k])
    
if __name__ == '__main__':
    main()