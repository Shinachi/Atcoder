H, W, N = map(int, input().split())

A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
A_set, B_set = set(A), set(B)
Adict, Bdict = {}, {}
for i, x in enumerate(sorted(list(A_set))):
    Adict[x] = i+1
    
for i, y in enumerate(sorted(list(B_set))):
    Bdict[y] = i+1
    

for i in range(N):
    print(Adict[A[i]], Bdict[B[i]])