A, B, C = map(int, input().split())
X = max(A, B, C)

if X >= (X-C)+(X-B)+(X-A):
    print(X)
else:
    print(-1)