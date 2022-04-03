n, k, x = map(int, input().split())
A = list(map(int, input().split()))
for i in range(n):
    use = min(A[i]//x, k)
    A[i] -= use* x
    k -= use
    
A.sort(reverse=True)
print(k)
for i in range(n):
    if k:
        A[i] = 0
        k -= 1
        
print(sum(A))