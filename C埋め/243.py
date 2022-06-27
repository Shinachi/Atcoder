N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]
S = input()
di = {}

for i in range(N):
    x, y = XY[i][0], XY[i][1]
    s = S[i]
    if y in di:
        di[y].append([x, s])
    else:
        di[y] = [[x, s]]

for i in di:
    temp = sorted(di[i], key=lambda x: x[0])
    ans = temp[0][1]
    for i in range(1, len(temp)):
        if ans == 'R' and temp[i][1] == 'L':
            print('Yes')
            exit()
        else:
            ans = temp[i][1]
            
print('No')