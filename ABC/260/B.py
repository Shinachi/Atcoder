N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_di, B_di, sum_AB= {}, {}, {}
for i in range(N):
    A_di[i+1] = A[i]
    B_di[i+1] = B[i]
    sum_AB[i+1] = A[i]+B[i]

A_sort = sorted(A_di.items(), key=lambda x:x[1], reverse=True)
B_sort = sorted(B_di.items(), key=lambda x:x[1], reverse=True)
AB_sort = sorted(sum_AB.items(), key=lambda x:x[1], reverse=True)

ans_li = []
for i in range(N):
    if i+1 > X:
        break
    else:
        ans_li.append(A_sort[i][0])

cnt_B = 0
for i in range(N):
    if cnt_B >= Y:
        break
    if B_sort[i][0] in ans_li:
        continue
    cnt_B += 1
    ans_li.append(B_sort[i][0])

cnt_AB = 0
for i in range(N):
    if cnt_AB >= Z:
        break
    if AB_sort[i][0] in ans_li:
        continue
    cnt_AB += 1
    ans_li.append(AB_sort[i][0])
    
ans_li.sort()

for i in ans_li:
    print(i)