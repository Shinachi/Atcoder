def f(pro):
    x = Counter(list(pro))
    res = False
    if len(x) == 2:
        if x[1] == x[0]:
            return True
        
    return res

N = int(input())
from itertools import product
from collections import Counter
from termios import N_PPP

li = []
for pro in product((0, 1), repeat=N):
    if f(pro):
        temp = ''
        left, right = 0, 0
        for i in range(N):
            if pro[i]:
                temp += '('
                left += 1
            else:
                if left > right:
                    right += 1
                    temp += ')'
                else:
                    break
        if len(list(temp))!=N:
            continue
        li.append(temp)

li.sort()

for i in li:
    print(i)