import sys
sys.setrecursionlimit(15000)

with open("in.txt") as f:
  lines = f.readlines()
  lines = [l.strip() for l in lines]

def check(i, j, lines):
  return i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0])


def dfs(i, j, d, visited, dirs, lines):
  visited.add((i, j))
  ni, nj = i + dirs[d][0], j + dirs[d][1]
  if not check(ni, nj, lines):
    return
  if lines[ni][nj] != '#':
    dfs(ni, nj, d, visited, dirs, lines)
  else:
    dfs(i, j, (d + 1) % 4, visited, dirs, lines)


dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
visited = set()
for i in range(len(lines)):
  for j in range(len(lines)):
    if lines[i][j] == "^":
      dfs(i, j, 0, visited, dirs, lines)
print(len(visited))
