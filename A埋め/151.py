import string

alp = [chr(ord("a")+i) for i in range(26)]

C = input()
print(alp[alp.index(C)+1])