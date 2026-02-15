from math import *
def f(x):
  ans = 2**x - 2 * cos(x)
  return ans
eps = 1
a = 0.5
b = 1
while eps > 0.001:
  c = (a+b)/2
  if f(a) * f(c) < 0:
    b = c
  else:
    a = c
  eps = (b - a)/2
  # print(f'a = {a}')
  # print(f'b = {b}')
  # print(f'eps = {eps}')
solution = (a+b)/2
print(solution)
