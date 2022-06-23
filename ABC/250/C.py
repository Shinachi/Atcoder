N,Q=map(int,input().split())
A=[i for i in range(N+1)]
A_sub=[i for i in range(N+1)]
 
for i in range(Q):
    x=int(input())
 
    k = A_sub[x]
    
    if k == N:
        k = N-1
    A[k], A[k+1] = A[k+1], A[k]
    A_sub[A[k]] = k
    A_sub[A[k+1]] = k+1
    print(k+1)