N, A, B = map(int, input().split())
li = [['.']* (N* B) for i in range(A)]

li[0][0] = True

for i in range(N* A):
    for j in range(N* B):
        if i == 0 and j == 0:
            continue
        