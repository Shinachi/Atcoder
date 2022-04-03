import math

a, b = map(int, input().split())
x = math.sqrt(a**2+b**2)
ansx = a/x
ansy = b/x
print(str(ansx)+' '+str(ansy))