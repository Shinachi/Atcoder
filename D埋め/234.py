import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))
que = P[0:K]
print(min(que))
heapq.heapify(que)
for i in range(K, N):
    minia = heapq.heappop(que)
    minia = max(minia, P[i])
    heapq.heappush(que, minia)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)