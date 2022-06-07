N = int(input())

li = [[1]]
for i in range(1, N):
    li2 = []
    for j in range(i+1):
        if j == 0 or j == i:
            li2.append(1)
        else:
            x = li[i-1][j-1] + li[i-1][j]
            li2.append(x)
    li.append(li2)
            
for i in li:
    print(*i)