n = int(input())
a = list(set(list(map(int, input().split()))))
for i in range(a[-1]):
    if i not in a:
        print(i)
        exit()

print(a[-1]+1)