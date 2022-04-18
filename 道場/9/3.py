N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [float('INF')]*N
dp[0], dp[1] = 0, abs(h[0]-h[1])
for i in range(2, N):
    for j in range(1, K+1):
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j]+abs(h[i-j]-h[i]))
            
print(dp[-1])