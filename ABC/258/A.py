K = int(input())
x = K// 60
y = K % 60
x = str(21+x)
if y < 10:
    y = '0'+str(y)
else:
    y = str(y)

print(x+':'+y)