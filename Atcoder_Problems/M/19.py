S = input()
nom = []
for i in range(10):
    nom.append(str(i))

ans = ''   
for s in S:
    if s in nom:
        ans += s
        
print(ans)