N, Q = map(int, input().split())
A = list(map(int, input().split()))
di = {}
for i, a  in enumerate(A):
    if a not in di:
        di[a] = [i+1]
    else:
        di[a].append(i+1)
    
for i in range(Q):
    x, k = map(int, input().split())
    if x not in di:
        print(-1)
        continue
    if k <= len(di[x]):
        print(di[x][k-1])
    else:
        print(-1)