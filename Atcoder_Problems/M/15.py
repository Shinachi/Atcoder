A=int(input())
B=int(input())
C=int(input())
li = [A, B, C]
li.sort(reverse=True)
print(li.index(A)+1)
print(li.index(B)+1)
print(li.index(C)+1)