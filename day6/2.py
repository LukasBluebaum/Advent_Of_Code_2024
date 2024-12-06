import sys
sys.setrecursionlimit(15000)

with open("in.txt") as f:
  lines = f.readlines()
  lines = [list(l.strip()) for l in lines]

def check(i, j, lines):
  return i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0])


def dfs(i, j, d, visited, dirs, lines):
  if (i, j, d) in visited:
    return True
  visited.add((i, j, d))
  ni, nj = i + dirs[d][0], j + dirs[d][1]
  if not check(ni, nj, lines):
    return False
  if lines[ni][nj] != '#':
    return dfs(ni, nj, d, visited, dirs, lines)
  else:
    return dfs(i, j, (d + 1) % 4, visited, dirs, lines)


dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
pos = None
for i in range(len(lines)):
  for j in range(len(lines)):
    if lines[i][j] == "^":
      pos = (i, j)

res = 0
for i in range(len(lines)):
  for j in range(len(lines[0])):
    if lines[i][j] == ".":
      lines[i][j] = '#'
      res += dfs(pos[0], pos[1], 0, set(), dirs, lines)
      lines[i][j] = '.'
print(res)
