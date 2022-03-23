n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i==0:
        x = a[i]+max(a)
        a.append(x)
        print(x)
    else:
        x = a[i] + a[-1]
        a.append(x)
        print(x)

print(a)