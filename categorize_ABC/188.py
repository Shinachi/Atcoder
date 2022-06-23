N = int(input())
A = list(map(int, input().split()))

L = max(A[:(2**N)// 2])
R = max(A[(2**N)// 2:])
print(A.index(min(L, R))+1)