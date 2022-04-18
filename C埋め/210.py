from collections import Counter


N, K = map(int, input().split())
c = list(map(int, input().split()))
counter = Counter(c[:K])
ans = len(counter)
for i in range(K, N):
    left = c[i-K]
    right = c[i]
    counter[left] -= 1
    counter[right] += 1
    if counter[left] == 0:
        del counter[left]
    ans = max(ans, len(counter))
    
print(ans)