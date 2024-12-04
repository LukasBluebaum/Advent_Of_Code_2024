
with open("in.txt") as f:
  lines = f.readlines()

def check(i, j, l, word, di, dj):
  while i >= 0 and j >= 0 and i < len(lines) and j < len(lines) and l < len(word) \
        and lines[i][j] == word[l]:
    i += di
    j += dj
    l += 1
  return l == len(word)


res = 0
for i in range(len(lines)):
  for j in range(len(lines[0])):
    for di, dj in [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
      res += check(i, j, 0, "XMAS", di, dj)

print(res)



