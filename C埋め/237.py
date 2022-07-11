from collections import deque

N = list(input())
x = set(N)
if len(x) == 1 and 'a' in x:
    print('Yes')
    exit()
n = deque(N)
left, right = 0, 0
l, r = True, True
while l or r:
    if n[0] == 'a':
        n.popleft()
        left += 1
    else:
        l = False
    if n[-1] == 'a':
        n.pop()
        right += 1
    else:
        r = False

n = list(n)
left_N, right_N = n, n[::-1]

if left <= right and left_N==right_N:
    print('Yes')
else:
    print('No')