from itertools import permutations

S, K = input().split()
K = int(K)

li = set(permutations(S))
li = sorted(li)

print(''.join(li[K-1]))