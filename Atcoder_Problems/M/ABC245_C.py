n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp_a = [False]* n
dp_b = [False]* n
dp_a[0], dp_b[0] = True, True

for i in range(n-1):
    if dp_a[i]:
        if abs(a[i+1]-a[i]) <= k:
            dp_a[i+1] = True
        if abs(b[i+1]-a[i]) <= k:
            dp_b[i+1] = True
    if dp_b[i]:
        if abs(a[i+1]-b[i]) <= k:
            dp_a[i+1] = True
        if abs(b[i+1]-b[i]) <= k:
            dp_b[i+1] = True
            
if dp_a[-1] or dp_b[-1]:
    print('Yes')
else:
    print('No')