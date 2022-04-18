N = int(input())
li = []
for i in range(1, N+1):
    li = li + [i] + li
    
print(*li)