import math

N = int(input())
li = []
time = 0
for i in range(N):
    a, b = map(int, input().split())
    li.append([a, b])
    time += a/ b
    
time /= 2

ans = 0
for a, b in li:
    if time >= a/ b:
        ans += a
        time -= a/ b
    else:
        ans += b* time
        break
    
print(ans)