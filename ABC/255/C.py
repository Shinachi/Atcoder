import bisect

X, A, D, N = map(int, input().split())
if D < 0:
    A += D* (N-1)
    D = -D
    
li = []
li.append(A)

for i in range(1, N):
    li.append(li[i-1] + D)
    
x = bisect.bisect(li, X)

print(abs(X-li[x-1]))