import math

def main():
    ans = 0
    K = int(input())
    for i in range(1, K+1):
        for j in range(1, K+1):
            x = math.gcd(i, j)
            for k in range(1, K+1):
                ans+=math.gcd(x, k)
                
    print(ans)

if __name__ == '__main__':
    main()