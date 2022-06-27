N = input()
li = []

for i in N:
    li.append(int(i))
    
li.sort(reverse=True)

left, right = '', ''

x = ''
for i in range(len(N)):
    if len(li) % 2 != 0 and i == len(N)-1:
        x += str(li[i])
    else:
        if i %2 == 0:
            left += str(li[i])
        else:
            right += str(li[i])
          
print(max((int(left+x)* int(right)), (int(left)* int(right+x))))
