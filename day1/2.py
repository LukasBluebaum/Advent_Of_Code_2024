import re
from collections import Counter

l1, l2 = [], []
with open("in.txt") as f:
  lines = f.readlines()
  for l in lines:
    a, b = re.findall('\d+', l)
    l1.append(int(a))
    l2.append(int(b))

l1 = set(l1)
l2 = Counter(l2)
print(sum(a*l2[a] for a in l1))


