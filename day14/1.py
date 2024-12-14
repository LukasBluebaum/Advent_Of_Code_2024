import re

with open("in.txt") as f:
  lines = f.readlines()

robots = []
for l in lines:
  y, x, dy, dx = re.findall("-?\d+", l)
  robots.append([int(x), int(y), int(dx), int(dy)])

sx, sy = 103, 101
for _ in range(100):
  tmp = []
  for x, y, dx, dy in robots:
    x = (x + dx) % sx
    y = (y + dy) % sy
    tmp.append([x, y, dx, dy])
  robots = tmp


q1, q2, q3, q4 = 0, 0, 0, 0
hsx = sx // 2
hsy = sy // 2
for x, y, _, _ in robots:
  if x == hsx or y == hsy:
    continue
  elif x < hsx and y < hsy:
    q1 += 1
  elif x > hsx and y < hsy:
    q2 += 1
  elif x < hsx and y > hsy:
    q3 += 1
  elif x > hsx and y > hsy:
    q4 += 1
print(q1 * q2 * q3 * q4)



