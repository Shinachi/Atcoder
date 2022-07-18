L, R = map(int, input().split())
MOD = 10**9+7
x = 1
y = 1
ans = 0
for i in range(L, R+1):
    if i // y == 0:
        x += 1
        y *= 10
    ans += (i* x% MOD)
    
print(ans% MOD)