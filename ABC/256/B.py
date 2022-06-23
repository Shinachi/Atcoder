N = int(input())
A = list(map(int, input().split()))

ans = 0
a = [0]* N
for i in range(N):
    a[i] += A[i]
    for j in range(0, i):
        a[j] += A[i]
        
for i in a:
    if i >= 4:
        ans += 1
        
print(ans)