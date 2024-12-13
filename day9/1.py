with open("in.txt") as f:
  line = f.readlines()[0].strip()
  line = [int(l) for l in line]

l = 0
l_id = 0
r = len(line) - 1
r_id = len(line) // 2
pos = 0
res = 0
test = ''
while l < r:
  if l % 2 == 0:
    for i in range(line[l]):
      res += pos * l_id
      pos += 1
    l += 1
    l_id += 1
  else:
    while line[r] > 0 and line[l] > 0:
      res += pos * r_id
      pos += 1
      line[r] -= 1
      line[l] -= 1
    if line[r] == 0:
      r -= 2
      r_id -= 1
    if line[l] == 0:
      l += 1

if l == r and line[r] > 0:
  while line[r] > 0:
    res += r_id * pos
    pos += 1
    line[r] -= 1
print(res)
