A, B = map(float, input().split())
x = str(A* B)

ans = ''

for i in x:
    if i == '.':
        break
    else:
        ans += i
        
print(ans)

A, B = map(int, input().split())
print(A*B)