
with open("in.txt") as f:
  lines = f.readlines()

def check(i, j, a, b, c, d):
  return lines[i-1][j-1] == a and lines[i+1][j-1] == b and \
         lines[i-1][j+1] == c and lines[i+1][j+1] == d

res = 0
for i in range(1, len(lines)-1):
  for j in range(1, len(lines[0])-1):
    if lines[i][j] == 'A':
      res += (check(i, j, 'M', 'M', 'S', 'S') or check(i, j, 'S', 'S', 'M', 'M') or
              check(i, j, 'M', 'S', 'M', 'S') or check(i, j, 'S', 'M', 'S', 'M'))

print(res)



