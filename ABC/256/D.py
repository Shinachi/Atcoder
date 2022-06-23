import bisect

N = int(input())
X, Y = [], []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

for i in range(N):
    z = bisect.bisect(X, Y[i])
    print(z)
    
    