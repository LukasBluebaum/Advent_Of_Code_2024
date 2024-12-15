with open("in.txt") as f:
  lines = ''.join(f.readlines())
  grid, moves = lines.split("\n\n")
  grid = [list(g.strip()) for g in grid.split("\n")]
  moves = ''.join(moves.split("\n"))


def move(i, j, di, dj, grid):
  count = 0
  grid[i][j] = '.'
  i += di
  j += dj

  while grid[i][j] == 'O':
    count += 1
    grid[i][j] = '.'
    i += di
    j += dj

  if grid[i][j] == '#':
    i -= di
    j -= dj
  while count > 0:
    grid[i][j] = 'O'
    count -= 1
    i -= di
    j -= dj
  grid[i][j] = '@'
  return i, j


x, y = 0, 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == '@':
      x = i
      y = j

dirs = {'v': (1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, 1)}
for m in moves:
  x, y = move(x, y, *dirs[m], grid)

res = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == 'O':
      res += i*100 + j
print(res)

