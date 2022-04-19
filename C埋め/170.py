X, N = map(int, input().split())
p = list(map(int, input().split()))

for i in range(0, 1000):
    if X - i not in p:
        print(X-i)
        exit()
    if X + i not in p:
        print(X+i)
        exit()