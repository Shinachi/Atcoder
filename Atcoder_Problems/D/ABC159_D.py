n = int(input())
a = list(map(int, input().split()))

from collections import Counter

c = Counter(a)
ans = 0
for i in c.values():
    ans += i*(i-1)//2
    
for i in a:
    k = c[i]
    
    print(ans-(k*(k-1)//2)+((k-1)*(k-2)//2))