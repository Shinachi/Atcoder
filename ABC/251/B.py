n, w = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = set()

if n == 1:
    for i in a:
        if a[i] <=w:
            ans.add(a[i])
            
elif n == 2:
    for i in range(n):
        if a[i] <= w:
            ans.add(a[i])
        for j in range(i+1, n):
                if a[i] + a[j] <= w:
                    ans.add(a[i] + a[j])

else:
    for i in range(n):
        if a[i] <= w:
            ans.add(a[i])
        for j in range(i+1, n):
            if a[i] + a[j] <= w:
                ans.add(a[i] + a[j])
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] <= w:
                    ans.add(a[i] + a[j] + a[k])

print(len(ans))