N = int(input())
A = list(map(int, input().split()))
A.sort()
li = []
li.append(A[0])

for i in range(1, N):
    x = li[i-1]* A[i]
    if x > 10** 18:
        print(-1)
        exit()
    else:
        li.append(x)
        
print(li[-1])
