def main():
    N = int(input())
    tmp = set()
    for i in range(N):
        s = input()
        if s not in tmp:
            tmp.add(s)
            print(i+1)
if __name__=='__main__':
    main()