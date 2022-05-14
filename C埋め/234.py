K = int(input())

bina = format(K, 'b')

ans = ''
for i in bina:
    if i == '1':
        ans += '2'
    else:
        ans += '0'
        
print(ans)