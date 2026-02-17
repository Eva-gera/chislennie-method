from math import *
def f(x):
    ans = acos(2**(x-1))
    return ans
x1 = 0
x2 = 0.6
c = 1
print(f'0 | {x2}')
eps = 10**(-3)
while abs(x2 - x1) > eps:
    x1 = x2
    x2 = round(f(x1), 4)
    print(f' {c} | {x2}')
    c += 1
print(f'Ответ: {round(x2, 3)}')
