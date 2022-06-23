S = input()
li = []
ans = 0
for i in range(len(S)):
    if len(li) != 0:
        x = li.pop()
        if x != S[i]:
            ans += 2
        else:
            li.append(x)
            li.append(S[i])
    else:
        li.append(S[i])

print(ans)