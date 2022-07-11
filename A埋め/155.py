from collections import Counter
A = list(map(int, input().split()))
A = Counter(A)

if len(A) == 2:
    print('Yes')
else:
    print('No')