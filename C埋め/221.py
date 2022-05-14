from itertools import product

n = input()

ans = 0

for pro in product((0, 1), repeat=len(n)):
    li1 = []
    li2 = []
    for i, b in enumerate(pro):
        if b == 1:
            li1.append(n[i])
        else:
            li2.append(n[i])

    if len(li1) == 0 or len(li2) == 0:
        continue

    li1.sort(reverse=True)
    li2.sort(reverse=True)
    a = int(''.join(li1))
    b = int(''.join(li2))
    ans = max(ans, a*b)

print(ans)