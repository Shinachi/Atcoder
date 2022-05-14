X = list(input())
N = int(input())
li = [input() for i in range(N)]
li = sorted(li, key=X.index)
print(li)