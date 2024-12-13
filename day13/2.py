import re, math
from decimal import *

getcontext().prec = 20

with open("in.txt") as f:
  lines = ''.join(f.readlines())
  machines = lines.split("\n\n")

res = 0
for machine in machines:
  lines = machine.split("\n")
  ax, ay = re.findall("\d+", lines[0])
  bx, by = re.findall("\d+", lines[1])
  x, y = re.findall("\d+", lines[2])
  ax, ay, bx, by, x, y = Decimal(ax), Decimal(ay), Decimal(bx), Decimal(by), Decimal(x), Decimal(y)
  x += 10000000000000
  y += 10000000000000

  b = (-(ay * x / ax) + y) / (by - (ay * bx / ax))
  a = (x - bx*b) / ax
  if math.isclose(a, round(a), rel_tol=0) and math.isclose(b, round(b), rel_tol=0):
    res += 3*a + b
print(int(res))


