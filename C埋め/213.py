H, W, N = map(int, input().split())
A, B = [], []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
A_set, B_set = set(A), set(B)

Adi, Bdi = {}, {}
for i, x in enumerate(sorted(list(A_set))):
    Adi[x] = i+1
for i, x in enumerate(sorted(list(B_set))):
    Bdi[x] = i+1
    
for i in range(N):
    print(Adi[A[i]], Bdi[B[i]])