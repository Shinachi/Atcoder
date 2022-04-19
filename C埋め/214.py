N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
li = [0]* N
li[0] = T[0]
for i in range(1, N):
    li[i] = min(li[i-1]+S[i-1], T[i])

x = min(li[-1]+S[-1], T[0])

if x != li[0]:
    li[0]=x
    for i in range(1, N):
        li[i] = min(li[i-1]+S[i-1], T[i])

for i in li:
    print(i)
