from collections import deque
import re

with open("in.txt") as f:
  lines = ''.join(f.readlines())

nums = re.findall("\d+", lines)
visited = {(int(nums[i]), int(nums[i+1])) for i in range(0, 2048, 2)}
queue = deque()
queue.append((0, 0, 0))
visited.add((0, 0))
sx, sy = 70, 70
while len(queue) > 0:
  i, j, d = queue.popleft()
  if i == sx and j == sy:
    print(d)
    break
  for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    ni = i + di
    nj = j + dj
    if ni < 0 or nj < 0 or ni > sx or nj > sy or (ni, nj) in visited:
      continue
    visited.add((ni, nj))
    queue.append((ni, nj, d+1))

