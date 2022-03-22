S = input()
blue, red = 0, 0
for s in S:
    if s == '0':
        red+=1
    else:
        blue+=1
        
print(min(blue, red)* 2)