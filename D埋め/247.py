from collections import deque

N = int(input())
Q = deque()

for i in range(N):
    q = list(map(int, input().split()))
    if q[0] == 1:
        Q.append([q[1], q[2]])
    else:
        ans = 0
        while q[1] > 0:
            x = Q.popleft()
            if q[1] < x[1]:
                ans += q[1]* x[0]
                q[1] -= x[1]
                Q.appendleft([x[0], abs(q[1])])
            else:
                ans += x[1]* x[0]
                q[1] -= x[1]
        print(ans)
