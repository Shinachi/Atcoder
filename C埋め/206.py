from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt_A = Counter(A)
cnt = cnt_A.most_common()

y = (N*(N-1))// 2

x = 0
for i in range(len(cnt_A)):
    if cnt[i][1] <= 1:
        continue
    x += (cnt[i][1]* (cnt[i][1]-1))// 2

print(y-x)