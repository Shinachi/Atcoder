S = list(input())
from collections import Counter
S = Counter(S)
x = S.most_common()
if len(S) == 1:
    print(-1)
else:
    print(x[-1][0])