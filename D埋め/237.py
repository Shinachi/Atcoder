N = int(input())
S = input()
L = []
R = []
for i in range(N):
    if S[i] == 'L':
        R.append(i)
    else:
        L.append(i)
        
ans = L + [N] + R[::-1]

print(*ans)