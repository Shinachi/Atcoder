n = int(input())
di = {}
cnt = 0
score = -1
for i in range(n):
    s, t = input().split()
    t = int(t)
    if s not in di:
        di[s] = t
        if t > score:
            cnt = i +1
            score = t
            
print(cnt)