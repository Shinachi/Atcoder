S = list(input())
li = []
for i in S:
    li.append(int(i))
    
li.sort()
for i in range(9):
    if i != li[i]:
        print(i)
        exit()
        
print(9)