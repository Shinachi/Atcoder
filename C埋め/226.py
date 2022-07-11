N = int(input())
T, K, A = [[0]], [[0]], [[0]]

for i in range(N):
    S = list(map(int, input().split()))
    T.append(S[0])
    K.append(S[1])
    A.append(S[2:])

need = [False]* (N+1)
need[N] = True

for i in range(N, 0, -1):
    if not need[i]:
        continue
    for j in A[i]:
        need[j] = True

ans = 0
for i in range(N+1):
    if need[i]:
        ans += T[i]
        
print(ans)