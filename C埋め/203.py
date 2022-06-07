N, K = map(int, input().split())
dict = {}
for i in range(N):
    A, B = map(int, input().split())
    if A in dict:
        dict[A] += B
    else:
        dict[A] = B
        
sort_d = sorted(dict.items())


for i in range(len(sort_d)):
    if sort_d[i][0] <= K:
        K += sort_d[i][1]
    else:
        break
    
print(K)