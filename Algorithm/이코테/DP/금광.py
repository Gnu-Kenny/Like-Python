def main():
    # 오른쪽 위 / 중간 / 아래
    dy = (1, 0, -1) 
    for _ in range(int(input())):
        n, m = list(map(int,input().split()))
        gold_nums = list(map(int,input().split()))
        s, e = 0, 0
        gold = []
        for i in range(n):
            s = e
            e = m * (i + 1)
            gold.append(gold_nums[s:e])

        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(len(gold)):
            dp[i][0] = gold[i][0]

        
        for x in range(1, m):
            for y in range(n):
                for i in range(3):
                    py = y + dy[i]
                    px = x - 1
                    if py < 0 or py>=n:
                        continue

                    dp[y][x] = max(dp[y][x], dp[py][px] + gold[y][x])

        answer = 0
        for i in range(n):
            if answer < dp[i][m-1]:
                answer = dp[i][m-1]
                
        print(answer)
            

if __name__ == '__main__':
    main()
