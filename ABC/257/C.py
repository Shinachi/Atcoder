N = int(input())
S = input()
W = list(map(int, input().split()))
kodomo = []
otona = []
for i in range(N):
    if S[i] == '1':
        otona.append(W[i])
    else:
        kodomo.append(W[i])

if len(kodomo)==0 or len(otona)==0:
    print(N)
    exit()

kodomo.sort(reverse=True)
otona.sort

cnt = 0

if len(kodomo) >= len(otona):
    for i in otona:
        if i <= kodomo[-1]:
            cnt += 1
        else:
            continue
else:
    for i in kodomo:
        if i <= otona[-1]:
            cnt += 1
        else:
            continue

print(N-cnt)