n = int(input())
a = list(map(str, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
import collections
li = []
for i in c:
    li.append(str(b[i-1]))
    
c = collections.Counter(li)

ans = 0
for i in a:
    ans += c[i]
    
print(ans)