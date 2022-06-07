X = list(input())
N = int(input())
li = []

for i in range(N):
    S = input()
    x = []
    for j in S:
        x.append(X.index(j))
    li.append(x)
    
li.sort()

for i in li:
    ans = ''
    for j in i:
        ans += X[j]
    print(ans)