N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = 3002
mod = 998244353
dp = [[0]*m for i in range(N)]

for i in range(a[0], b[0]+1):
    dp[0][i] = 1 
for j in range(1, m):
    dp[0][j] += dp[0][j-1]
    
for i in range(1, N-1):
    for j in range(a[i], b[i]+1):
        dp[i][j] += dp[i-1][j]
        dp[i][j] %= mod
    for j in range(1, m):
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= mod
        
i = N-1
for j in range(a[i], b[i] + 1):
    dp[i][j] += dp[i - 1][j]
    dp[i][j] %= mod

print(sum(dp[-1])% mod)