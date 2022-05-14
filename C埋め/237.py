S = list(input())
S.reverse()

cnt = 0
for i in S:
    if i != 'a':
        break
    cnt += 1
    
S += ['a']* cnt
usi = S[:len(S)//2]
mae = S[len(S)//2+1:len(S)]
mae.reverse()
if mae == usi:
    print('Yes')
else:
    print('No')