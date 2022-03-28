n = int(input())
A = list(map(int, input().split()))
cnt = [0 for i in range(200)]
ans = 0
for a in A:
    r = a%200
    ans += cnt[r]
    cnt[r] += 1
    
print(ans)