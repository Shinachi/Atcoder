alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s = list(input())
oomoji = False
komoji = False
x = set(s)
if len(s) == len(x):
    for i in s:
        if i in alp:
            komoji = True
        else:
            oomoji = True
            
    if oomoji and komoji:
        print('Yes')
        exit()
            
print('No')