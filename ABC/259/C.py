from itertools import groupby

def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

S = input()
T = input()

S_li, T_li = runLengthEncode(S), runLengthEncode(T)

ans = True
if len(S_li) != len(T_li):
    print('No')
    exit()
    
for i in range(len(S_li)):
    if S_li[i][0] != T_li[i][0]:
        ans = False
        break
    if S_li[i][1] == T_li[i][1] or (S_li[i][1] < T_li[i][1] and S_li[i][1] >= 2):
        continue
    else:
        ans = False
        break
    
print('Yes' if ans else 'No')