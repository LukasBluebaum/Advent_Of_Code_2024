with open("in.txt") as f:
  line = f.readlines()[0].strip()
  line = [int(l) for l in line]

prefix = [0] * len(line)
for i in range(len(line)):
  prefix[i] += prefix[i-1] + line[i]

positions = {}
for r in range(len(line)-1, -1, -2):
  for l in range(1, r, 2):
    if line[l] >= line[r]:
      if l not in positions:
        positions[l] = []
      positions[l].append((r // 2, line[r]))
      line[l] -= line[r]
      line[r] = 0
      break

res = 0
for l in range(len(line)):
  pos = prefix[l-1] if l > 0 else 0
  if l % 2 == 0:
    for _ in range(line[l]):
      res += pos * (l // 2)
      pos += 1
  elif l in positions:
    for id_, count in positions[l]:
      for _ in range(count):
        res += id_ * pos
        pos += 1

print(res)
