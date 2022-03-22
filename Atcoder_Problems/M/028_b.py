S = list(input())
a, b, c, d, e, f = 0,0,0,0,0,0

for s in S:
    if s == 'A':
        a += 1
    elif s == 'B':
        b += 1
    elif s=='C':
        c+=1
    elif s=='D':
        d+=1
    elif s=='E':
        e+=1
    else:
        f+=1
        
li = [a,b,c,d,e,f]
    
ans = ''
for i in li:
    ans += str(i)
    
print(' '.join(ans))