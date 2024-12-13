with open("in.txt") as f:
  grid = f.readlines()
  grid = [g.strip() for g in grid]


def dfs(i, j, visited, c):
  visited.add((i, j))
  area = 1
  perimeter = 0
  for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    ni = i + di
    nj = j + dj
    if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]) or grid[ni][nj] != c:
      perimeter += 1
      continue
    if (ni, nj) in visited:
      continue
    a, p = dfs(ni, nj, visited, c)
    area += a
    perimeter += p
  return area, perimeter

visited = set()
res = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if (i, j) not in visited:
      a, p = dfs(i, j, visited, grid[i][j])
      res += a*p
print(res)
