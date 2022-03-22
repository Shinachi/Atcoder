n=int(input())
li = []
for i in range(n):
    ab = list(map(int, input().split()))
    
li.sort(key=lambda x:x[0], reverse=True)
