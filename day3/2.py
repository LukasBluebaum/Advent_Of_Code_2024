import re

with open("in.txt") as f:
  lines = f.readlines()

s = ""
for l in lines:
  s += l.strip()

res = 0
splits = re.split("(do\(\)|don't\(\))", s)
enabled = True
for i in range(len(splits)):
  if splits[i] == "do()":
    enabled = True
  elif splits[i] == "don't()":
    enabled = False
  elif enabled:
    muls = re.findall('mul\(\d+,\d+\)', splits[i])
    for m in muls:
      a, b = re.findall('\d+', m)
      res += int(a)*int(b)

print(res)
