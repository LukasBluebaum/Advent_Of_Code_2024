import re, math

with open("in.txt") as f:
  lines = ''.join(f.readlines())
  machines = lines.split("\n\n")

res = 0
for machine in machines:
  lines = machine.split("\n")
  ax, ay = re.findall("\d+", lines[0])
  bx, by = re.findall("\d+", lines[1])
  x, y = re.findall("\d+", lines[2])
  ax, ay, bx, by, x, y = int(ax), int(ay), int(bx), int(by), int(x), int(y)

  b = (-(ay * x / ax) + y) / (by - (ay * bx / ax))
  a = (x - bx*b) / ax
  if math.isclose(a, round(a)) and math.isclose(b, round(b)):
    res += 3*a + b
print(int(res))


