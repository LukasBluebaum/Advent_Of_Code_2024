with open("in.txt") as f:
  lines = [l.strip() for l in f.readlines()]

def check(i, j, lines):
  return i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0])

freqs = {}
for i in range(len(lines)):
  for j in range(len(lines[0])):
    if lines[i][j] != '.':
      if lines[i][j] not in freqs:
        freqs[lines[i][j]] = []
      freqs[lines[i][j]].append((i, j))

locations = set()
for f in freqs:
  for i in range(len(freqs[f])):
    for j in range(i + 1, len(freqs[f])):
      x = freqs[f][j][0] - freqs[f][i][0]
      y = freqs[f][j][1] - freqs[f][i][1]
      if check(freqs[f][j][0]+x, freqs[f][j][1]+y, lines):
        locations.add((freqs[f][j][0]+x, freqs[f][j][1]+y))
      if check(freqs[f][i][0]-x, freqs[f][i][1]-y, lines):
        locations.add((freqs[f][i][0]-x, freqs[f][i][1]-y))
print(len(locations))

