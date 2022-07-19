import math
def main():
    a,b,c,d = map(int, input().split())

    ans = 0
    ans += b//c - (a-1)//c
    ans += b//d - (a-1)//d
    x = (c* d)//math.gcd(c, d)
    ans -= b//x - (a-1)//x
    print((b-a)-ans+1)
    
if __name__=='__main__':
    main()