N, K = map(int, input().split())
li = []
for i in range(N):
    p = list(map(int, input().split()))
    li.append(sum(p))
    
s = sorted(li, reverse=True)[K-1]

for i in range(N):
    if li[i]+300 >= s:
        print('Yes')
    else:
        print('No')