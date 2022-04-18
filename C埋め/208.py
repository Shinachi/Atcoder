N, K = map(int, input().split())
a = list(map(int, input().split()))

a_sort = sorted(a)
di = {}
x = K//N
y = K%N
for i in a_sort:
    di[str(i)] = x
    if y != 0:
        di[str(i)] = x + 1
        y -=1
        
for i in a:
    print(di[str(i)])
