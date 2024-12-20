from collections import deque, defaultdict

with open("in.txt") as f:
  grid = [list(l.strip()) for l in f.readlines()]


def bfs(i, j, grid):
  queue = deque()
  queue.append((i, j, 0))
  dists = {}
  while len(queue) > 0:
    i, j, d = queue.popleft()
    if (i, j) in dists:
      continue
    dists[(i, j)] = d

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      ni = i + di
      nj = j + dj
      if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]):
        continue
      if grid[ni][nj] != '#':
        queue.append((ni, nj, d+1))
  return dists

def offsets(c):
  return [(i, j) for i in range(-c, c+1) for j in range(-c, c+1)
          if abs(i) + abs(j) <= c and not (i == 0 and j == 0)]

i, j = 0, 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == 'E':
      si, sj = i, j

dists = bfs(si, sj, grid)
offs = offsets(20)

res = 0
for i, j in dists:
  for di, dj in offs:
    ni = i + di
    nj = j + dj
    if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]) or grid[ni][nj] == '#':
      continue
    if dists[(i, j)] - (abs(di) + abs(dj)) - dists[(ni, nj)] >= 100:
      res += 1
print(res)




