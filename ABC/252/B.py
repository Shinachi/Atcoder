N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sort = sorted(A, reverse=True)
max_A = A_sort[0]
li = []
for i in range(N):
    if A[i] == max_A:
        li.append(i+1)
        
ans = False
for b in B:
    if b in li:
        ans = True
        break
    
if ans:
    print('Yes')
else:
    print('No')