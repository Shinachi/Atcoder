n, k = map(int, input().split())
for i in range(n):
    a = int(input())
    k -= a
    if k <= 0:
        print(i+1)
        exit()
