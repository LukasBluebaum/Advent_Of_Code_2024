import re

l1, l2 = [], []
with open("in.txt") as f:
  lines = f.readlines()
  for l in lines:
    a, b = re.findall('\d+', l)
    l1.append(int(a))
    l2.append(int(b))

l1 = sorted(l1)
l2 = sorted(l2)
print(sum(abs(a-b) for a, b in zip(l1, l2)))

