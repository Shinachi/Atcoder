def main():
    n = int(input())
    di = {}
    for i in range(n):
        s = input()
        if s not in di:
            print(s)
            di[s] = 1
        else:
            print(s + '(' + str(di[s]) + ')')
            di[s] += 1

if __name__=='__main__':
    main()