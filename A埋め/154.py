S, T = input().split()
AB = list(map(int, input().split()))
U = input()
if U == S:
    AB[0] -=1
else:
    AB[1] -=1
    
ans = ''
for i in AB:
    ans += str(i)
    
print(' '.join(ans))