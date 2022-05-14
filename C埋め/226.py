N = int(input())
T = [0]* (N+1)
K = [0]* (N+1)
A = [0]* (N+1)

for i in range(1, N+1):
    li = list(map(int, input().split()))
    T[i] = li[0]
    K[i] = li[1]
    A[i] = li[2:]

need = [False]* (N+1)

need[N] = True

for i in range(N, 0, -1):
    if not need[i]:
        continue
    for v in A[i]:
        need[v] = True
        
ans = sum(T[i] for i in range(1, N+1) if need[i])

print(ans)