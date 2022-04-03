c = list(map(str, input().split()))
li = []
for i in c:
    li.append(i)
    li.append(',')
    
li.pop()
print(''.join(li))