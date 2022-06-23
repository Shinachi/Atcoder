li = list(map(int, input().split()))

ans = 0 
for a in range(1, 31):
    for b in range(1, 31):
        for d in range(1, 31):
            for e in range(1, 31):
                c=li[0]-a-b
                f=li[1]-d-e
                g=li[3]-a-d
                h=li[4]-b-e
                wi=li[2]-g-h
                hi=li[5]-c-f
                if min(c,f,g,h)>0 and wi==hi:
                    ans+=1
                    
print(ans)