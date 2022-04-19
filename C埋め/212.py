def nibun(A, b):
    left = 0
    right = N
    while abs(left-right) > 1:
        mid = (left+right)// 2
        if b > A[mid]:
            left = mid
        else:
            right = mid
            
    return min(abs(b-A[left]), abs(b-A[min(N-1, left+1)]), abs(b-A[max(0, left-1)]))

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

ans = float('INF')
for b in B:
    ans = min(ans, nibun(A, b))
    
print(ans)