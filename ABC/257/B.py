N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
    
for i in range(Q):
    x = L[i] - 1
    if A[x] < N and A[x]+1 not in A:
        A[x] = A[x] + 1
    else:
        continue

print(*A)