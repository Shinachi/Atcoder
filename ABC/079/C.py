from itertools import product

def f(li, pro):
    cnt = 0
    ans = str(li[0])
    for i in range(3):
        if pro[i] == 0:
            ans += '-'
            ans += str(li[i+1])
            cnt -= li[i+1]
        else:
            ans += '+'
            ans += str(li[i+1])
            cnt += li[i+1]
            
    if cnt + li[0] == 7:
        return ans
    else:
        return False
        

ABCD = list(input())
li = []
for i in ABCD:
    li.append(int(i))

for pro in product((0, 1), repeat=3):
    x = f(li, pro)
    if x is False:
        continue
    else:
        print(x+'=7')
        exit()