N, Q = map(int, input().split())
S = input()

P = 0
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        P += x
    else:
        y = P% N
        print(S[x-y-1])