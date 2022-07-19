n = int(input())
h = list(map(int,input().split()))
 
cnt = 0
for i in range(n):
    if h[i] == 0:
        continue
    
    while h[i]>0:
        cnt += 1
        for j in range(i, n):
            if h[j]==0:
                break
            h[j] -=1
            
print(cnt)