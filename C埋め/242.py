N = int(input())
dp = [[0]* 9 for i in range(N)]

dp[0] = [1]* 9

MOD = 998244353
for i in range(N):
    for j in range(9):
        dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < 8:
            dp[i][j] += dp[i-1][j+1]
            
        dp[i][j] %= MOD
        
        
print(sum(dp[-1])%MOD)