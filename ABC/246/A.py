import collections

xy = [list(map(int, input().split())) for i in range(3)]
x, y = [], []
for i in xy:
    x.append(i[0])
    y.append(i[1])
    
cx = collections.Counter(x)
cy = collections.Counter(y)

print(str(cx.most_common()[1][0])+' '+str(cy.most_common()[1][0]))