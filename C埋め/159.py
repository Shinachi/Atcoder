N , Q= map(int, input().split())
S = list(input())
for i in range(Q):
    q, a = map(int, input().split())
    if q == 1:
        li = S[a-1:]
        li.reverse()
        del S[a-1:]
        S = li + S[:a-1]
    else:
        print(S[a-1])