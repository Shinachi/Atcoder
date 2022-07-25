def main():
    def f(pro):
        tmp = Counter(pro)
        if len(tmp) == 2 and tmp[0]==tmp[1]:
            return True


    from itertools import product
    from collections import Counter
    N = int(input())

    ans = []

    for pro in product((0, 1), repeat=N):
        if f(pro):
            x = ''
            l ,r = 0, 0
            for i in pro:
                if i:
                    x += '('
                    l += 1
                else:
                    if l > r:
                        x += ')'
                        r += 1
                    else:
                        break
            if len(list(x)) != N:
                continue
            ans.append(x)
            
    ans.sort()

    for i in ans:
        print(i)
        
if __name__=='__main__':
    main()