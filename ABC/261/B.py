N = int(input())
A = [list(input()) for i in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] == 'W' and A[j][i] != 'L':
            print('incorrect')
            exit()
        if A[i][j] == 'L' and A[j][i] != 'W':
            print('incorrect')
            exit()
        if A[i][j] == 'D' and A[j][i] != 'D':
            print('incorrect')
            exit()
            
print('correct')