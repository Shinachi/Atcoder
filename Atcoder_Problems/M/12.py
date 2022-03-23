n=int(input())
li = []
for i in range(n):
    ab = list(map(int, input().split()))
    li.append(ab)
    
li.sort(key=lambda x:x[1], reverse=True)
print(li[-1][0]+li[-1][1])