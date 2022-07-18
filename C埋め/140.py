def main():
    N = int(input())
    B = list(map(int, input().split()))
    ans = []
    x = B[-1]
    B.reverse()
    for i in range(N-1):
        z = min(B[i], x)
        ans.append(z)
        x = B[i]
        
    ans.append(B[-1])

    print(sum(ans))
    
if __name__=='__main__':
    main()