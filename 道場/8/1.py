s = input()
li = []
for i in s:
    if i == '0':
        li.append(i)
    elif i == '1':
        li.append(i)
    else:
        if len(li) == 0:
            continue
        li.pop()
        
print(''.join(li))