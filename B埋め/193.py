N = int(input())
ans = 100000000000000000
k = False
for i in range(1, N+1):
    a,p,x=map(int, input().split())
    if a < x:
        ans = min(ans, p)
        k = True
        
print(ans if k else -1)