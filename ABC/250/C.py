N,Q=map(int,input().split())
A=[i for i in range(N+1)]
A_INV=[i for i in range(N+1)]

for i in range(Q):
    x=int(input())

    k=A_INV[x]

    if k==N:
        k=N-1

    A[k],A[k+1]=A[k+1],A[k]
    A_INV[A[k]]=k
    A_INV[A[k+1]]=k+1

print(A_INV)
print(*A[1:])
