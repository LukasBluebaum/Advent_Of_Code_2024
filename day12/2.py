
with open("in.txt") as f:
  grid = f.readlines()
  grid = [g.strip() for g in grid]

def check(i, j, c):
  return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != c

def dfs(i, j, visited, c):
  visited.add((i, j))
  area = 1
  sides = 0

  if check(i+1, j, c) and check(i, j+1, c):
    sides += 1
  if check(i-1, j, c) and check(i, j-1, c):
    sides += 1
  if check(i-1, j, c) and check(i, j+1, c):
    sides += 1
  if check(i, j-1, c) and check(i+1, j, c):
    sides += 1

  if check(i+1, j+1, c) and not check(i+1, j, c) and not check(i, j+1, c):
    sides += 1
  if check(i-1, j-1, c) and not check(i-1, j, c) and not check(i, j-1, c):
    sides += 1
  if check(i-1, j+1, c) and not check(i-1, j, c) and not check(i, j+1, c):
    sides += 1
  if check(i+1, j-1, c) and not check(i, j-1, c) and not check(i+1, j, c):
    sides += 1

  for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
    ni = i + di
    nj = j + dj
    if check(ni, nj, c):
      continue
    if (ni, nj) in visited:
      continue
    a, s = dfs(ni, nj, visited, c)
    area += a
    sides += s
  return area, sides


visited = set()
res = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if (i, j) not in visited:
      points = []
      a, sides = dfs(i, j, visited, grid[i][j])
      res += a * sides
print(res)


