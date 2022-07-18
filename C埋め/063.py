def main():
    N = int(input())
    S = [int(input()) for i in range(N)]
    dp = [[0]* 10001 for i in range(N+1)]

    dp[0][0] = 1

    for i in range(N):
        for j in range(10001):
            if dp[i][j]:
                dp[i+1][j] = 1
                dp[i+1][j+S[i]] = 1

    ans = 0
    for i in range(10001):
        if dp[N][i] and i% 10!=0:
            ans = max(ans, i)
            
    print(ans)

if __name__ == '__main__':
    main()