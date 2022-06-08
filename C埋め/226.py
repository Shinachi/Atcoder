N = int(input())
T, K, A = [[0]], [[0]], [[0]]

for i in range(N):
    x = list(map(int, input().split()))
    T.append(x[0])
    K.append(x[1])
    A.append(x[2:])
    
need = [False]* (N+1)

need[N] = True
for i in range(N, 0, -1):
    if not need[i]:
        continue
    for v in A[i]:
        need[v] = True
        
ans = 0
for i in range(1, N+1):
    if need[i]:
        ans += T[i]
        
print(ans)