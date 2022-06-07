H, W = map(int, input().split())
li = [input() for i in range(H)]

x = []
y = []

for i in range(H):
    for j in range(W):
        if li[i][j] == 'o':
            x.append(i)
            y.append(j)
            
print(abs(x[0]-x[1]) + abs(y[0]-y[1]))
