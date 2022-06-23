N, K = map(int, input().split())
A = [int(i)-1 for i in input().split()]
XY = [list(map(int, input().split())) for i in range(N)]

ans = -1

for i in range(N):
    if i in A:
        continue
    min_dist = 1000000000000000000
    for j in A:
        x = ((XY[i][0]-XY[j][0])** 2 + (XY[i][1]-XY[j][1])** 2)** 0.5
        min_dist = min(min_dist, x)
    ans = max(ans, min_dist)
    
print(ans)