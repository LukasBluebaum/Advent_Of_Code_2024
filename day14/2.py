import re
from PIL import Image
import numpy as np

with open("in.txt") as f:
  lines = f.readlines()

robots = []
for l in lines:
  y, x, dy, dx = re.findall("-?\d+", l)
  robots.append([int(x), int(y), int(dx), int(dy)])

sx, sy = 103, 101
for i in range(10000):
  tmp = []
  rows = set()
  cols = set()
  for x, y, dx, dy in robots:
    x = (x + dx) % sx
    y = (y + dy) % sy
    tmp.append([x, y, dx, dy])
    rows.add(x)
    cols.add(y)
  robots = tmp
  if sx - len(rows) > 10 and sy - len(cols) > 10:
    grid = [[0 for _ in range(sy)] for _ in range(sx)]
    for x, y, _, _ in robots:
      grid[x][y] = 255
    im = Image.fromarray(np.array(grid,dtype=np.uint8))
    im.save(f'{i+1}.png')

