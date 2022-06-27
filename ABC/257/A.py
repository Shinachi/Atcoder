N, X = map(int, input().split())
x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
li = []
for i in x:
    for j in range(N):
        li.append(i)
    
print(li[X-1])