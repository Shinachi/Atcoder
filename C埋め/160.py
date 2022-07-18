def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    x = -1
    for i in range(N):
        if i == N-1:
            x = max(x, A[0]+(K-A[-1]))
            break
        x = max(x, A[i+1]-A[i])
        
    print(K-x)
    
if __name__ == '__main__':
    main()