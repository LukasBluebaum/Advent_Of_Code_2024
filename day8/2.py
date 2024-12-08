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
      di = freqs[f][j][0] - freqs[f][i][0]
      dj = freqs[f][j][1] - freqs[f][i][1]

      ti, tj = freqs[f][j][0], freqs[f][j][1]
      while check(ti, tj, lines):
        locations.add((ti, tj))
        ti += di
        tj += dj

      ti, tj = freqs[f][i][0], freqs[f][i][1]
      while check(ti, tj, lines):
        locations.add((ti, tj))
        ti -= di
        tj -= dj

print(len(locations))

