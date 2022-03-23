s = input()
li = []
for i in s:
    li.append(int(i))
    
ans =0
for i in range(len(li)):
    if i% 2 != 0:
        ans -= li[i]
    else:
        ans += li[i]
        
print(ans)