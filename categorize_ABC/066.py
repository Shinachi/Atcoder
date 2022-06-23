from collections import deque

n = int(input())
a = list(map(int, input().split()))
li = deque()
for i in range(n):
    if i% 2 == 0:
        li.append(a[i])
    else:
        li.appendleft(a[i])
        
if n%2 == 0:
    print(*li)
else:
    print(*deque(reversed))