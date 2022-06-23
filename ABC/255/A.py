R, C = map(int, input().split())
li = [list(map(int, input().split())) for i in range(2)]

R -=1
C -=1

print(li[R][C])