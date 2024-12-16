from collections import deque, defaultdict

def find_path(i, j, d, si, sj, parents, path, spots):
  if i == si and j == sj:
    spots.update(path)
  else:
    for ni, nj, nd in parents[(i, j, d)]:
      path.append((ni, nj))
      find_path(ni, nj, nd, si, sj, parents, path, spots)
      path.pop()

with open("in.txt") as f:
  grid = [g.strip() for g in f.readlines()]

queue = deque()
dists = defaultdict(lambda: float('inf'))
parents = defaultdict(list)
si, sj = None, None
ei, ej = None, None
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == 'S':
      queue.append((i, j, 1))
      dists[(i, j, 1)] = 0
      si, sj = i, j
    if grid[i][j] == 'E':
      ei, ej = i, j

dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
while len(queue) > 0:
  i, j, d = queue.popleft()

  for ni, nj, nd, s in [(i+dirs[d][0], j+dirs[d][1], d, 1), (i, j, (d-1) % 4, 1000),
                     (i, j, (d+1) % 4, 1000)]:
    if ni >= 0 and nj >= 0 and ni < len(grid) and nj < len(grid[0]) and grid[ni][nj] != '#':
      if dists[(ni, nj, nd)] > (dists[(i, j, d)] + s):
        dists[(ni, nj, nd)] = dists[(i, j, d)] + s
        if s == 1:
          queue.appendleft((ni, nj, nd))
        else:
          queue.append((ni, nj, nd))
        parents[(ni, nj, nd)] = [(i, j, d)]
      elif dists[(ni, nj, d)] == (dists[(i, j, d)] + s):
        parents[(ni, nj, nd)].append((i, j, d))

spots = set()
for i in range(4):
  find_path(ei, ej, i, si, sj, parents, [], spots)
print(len(spots))
