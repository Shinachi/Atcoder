n = int(input())

li = []

for i in range(n):
    li.append(input())
    
for i in zip(*li):
    print(''.join(reversed(list(i))))