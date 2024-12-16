from collections import deque

with open("in.txt") as f:
  grid = [g.strip() for g in f.readlines()]

queue = deque()
visited = set()
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == 'S':
      queue.append((i, j, 1, 0))
      visited.add((i, j, 1))

dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
while len(queue) > 0:
  i, j, d, s = queue.popleft()
  if grid[i][j] == 'E':
    print(s)
    break

  ni, nj = i + dirs[d][0], j + dirs[d][1]
  if ni >= 0 and nj >= 0 and ni < len(grid) and nj < len(grid[0]) \
      and (ni, nj, d) not in visited and grid[ni][nj] != '#':
    visited.add((ni, nj, d))
    queue.appendleft((ni, nj, d, s+1))

  if (i, j, (d-1) % 4) not in visited:
    visited.add((i, j, (d-1) % 4))
    queue.append((i, j, (d-1) % 4, s+1000))

  if (i, j, (d+1) % 4) not in visited:
    visited.add((i, j, (d+1) % 4))
    queue.append((i, j, (d+1) % 4, s+1000))


