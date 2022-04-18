N = int(input())
A, B, C = [0]*N, [0]*N, [0]*N
for i in range(N):
    A[i], B[i], C[i] = map(int, input().split())
    
dp = [[0]* 3 for i in range(N)]

dp[0] = [A[0], B[0], C[0]]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1]+A[i], dp[i-1][2]+A[i])
    dp[i][1] = max(dp[i-1][0]+B[i], dp[i-1][2]+B[i])
    dp[i][2] = max(dp[i-1][0]+C[i], dp[i-1][1]+C[i])
    
print(max(dp[-1]))