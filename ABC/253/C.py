Q = int(input())

dict = {}

for i in range(Q):
    li = list(map(int, input().split()))
    if li[0] == 1:
        if li[1] not in dict:
            dict[li[1]] = 1
        else:
            dict[li[1]] += 1
    elif li[0] == 2:
        if li[1] not in dict:
            continue
        x = min(li[2], dict[li[1]])
        dict[li[1]] -= x
        if dict[li[1]] == 0:
            del dict[li[1]]
    else:
        dict_sort = sorted(dict.items(), reverse=True)
        print(dict_sort[0][0]-dict_sort[-1][0])