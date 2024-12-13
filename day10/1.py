with open("example2.txt") as f:
  lines = f.readlines()
  lines = [l.strip() for l in lines]
  lines = [[int(l) for l in line] for line in lines]


def dfs(i, j, visited):
  visited.add((i, j))
  if lines[i][j] == 9:
    return 1
  res = 0
  for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    ni = i + di
    nj = j + dj
    if ni < 0 or nj < 0 or ni >= len(lines) or nj >= len(lines[0]) or (ni, nj) in visited:
      continue
    if lines[i][j] + 1 == lines[ni][nj]:
      res += dfs(ni, nj, visited)
  return res

res = 0
for i in range(len(lines)):
  for j in range(len(lines[0])):
    if lines[i][j] == 0:
      a = dfs(i, j, set())
      res += a
print(res)
