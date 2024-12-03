import re

with open("in.txt") as f:
  lines = f.readlines()

res = 0
for l in lines:
  muls = re.findall('mul\(\d+,\d+\)', l)
  for m in muls:
    a, b = re.findall('\d+', m)
    res += int(a)*int(b)
print(res)
