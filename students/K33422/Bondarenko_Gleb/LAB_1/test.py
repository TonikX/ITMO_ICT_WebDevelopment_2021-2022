import re

data = input("введи числа: ")
helping = (re.findall(r'\d+', data))
res = list(map(int, helping))
print(res)
a, b, h = res
s = 0.5 * (a + b) * h
print(s)