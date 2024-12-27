with open("in.txt") as f:
  grids = ''.join(f.readlines()).split("\n\n")


def count(grid):
  grid = [g.strip() for g in grid if len(g) > 0]
  cols = [-1] * len(grid[0])
  for j in range(len(grid[0])):
    for i in range(len(grid)):
      cols[j] += grid[i][j] == '#'
  return cols

keys = []
locks = []
for grid in grids:
  grid = grid.split("\n")
  if grid[0][0] == '#':
    locks.append(count(grid))
  else:
    keys.append(count(grid))

res = 0
for l in locks:
  for k in keys:
    if all(k[i] + l[i] <= 5 for i in range(len(l))):
      res += 1
print(res)

