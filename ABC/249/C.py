def bit(pro, li):
    x = []
    for i in range(N):
        if pro[i]:
            x += li[i]
        else:
            continue
    
    x = Counter(x)
    cnt = 0
    for i in x:
        if x[i] == K:
            cnt += 1
 
    return cnt

N, K = map(int, input().split())
from itertools import product
from collections import Counter

li = []
for i in range(N):
    s = list(input())
    li.append(s)
    
ans = 0
for pro in product((0, 1), repeat=N):
    ans = max(ans, bit(pro, li))
    
print(ans)