N = int(input())
z = int(N**0.5)

s = set()
for i in range(2, z+1):
    x = i* i
    while x <= N:
        s.add(x)
        x*=i
print(N-len(s))