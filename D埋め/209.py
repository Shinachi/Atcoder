def main():
    import sys
    sys.setrecursionlimit(120000)

    def dfs(pos, G, visited, li):
        visited[pos] = True
        for i in G[pos]:
            if visited[i] == False:
                li[i] += li[pos] + 1
                dfs(i, G, visited, li)


    N, Q = map(int, input().split())

    G = [[] for i in range(N+1)]

    li = [0]* (N+1)
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        
    visited = [False]* (N+1)
    li[1]=1
    dfs(1, G, visited, li)

    for i in range(Q):
        c, d = map(int, input().split())
        if abs(li[c]-li[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')
            
if __name__=='__main__':
    main()