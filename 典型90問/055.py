N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
import math
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                for m in range(l+1, N):
                    if A[i]%P*A[j]%P*A[k]%P*A[l]%P*A[m]%P == Q:
                        cnt += 1
                        
print(cnt)
