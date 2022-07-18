def main():
    N = int(input())
    H = list(map(int, input().split()))
    H.reverse()
    dp = [0]* (N)

    for i in range(1, N):
        if H[i] >= H[i-1]:
            dp[i] += dp[i-1]+1
        else:
            dp[i] = 0
            
    print(max(dp))
    
if __name__=='__main__':
    main()