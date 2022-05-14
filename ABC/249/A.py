A,B,C,D,E,F,X = map(int, input().split())
t = (A + C) // X + (A+C)% X
a = (D + F) // X + (D+F)% X

t_kyori = B* t
a_kyori = E* a

if t_kyori > a_kyori:
    print('Takahashi')
elif a_kyori > t_kyori:
    print('Aoki')
else:
    print('Draw')