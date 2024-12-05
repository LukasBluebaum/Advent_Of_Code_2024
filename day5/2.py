from collections import defaultdict
from functools import cmp_to_key

with open("in.txt") as f:
  lines = f.readlines()
  order, updates = ''.join(lines).split("\n\n")
  order = order.split("\n")
  updates = updates.split("\n")

after = defaultdict(set)
for o in order:
  a, b = o.split("|")
  after[int(a)].add(int(b))

def compare(a, b):
  if a not in after[b] and b not in after[a]:
    return 0
  return 1 if a in after[b] else -1

res = 0
for u in updates[:-1]:
  nums = u.split(",")
  seen = set()
  order = True
  for n in nums:
    if len(after[int(n)] & seen) != 0:
      order = False
      break
    seen.add(int(n))
  if not order:
    nums = [int(n) for n in nums]
    nums = sorted(nums, key=cmp_to_key(compare))
    res += nums[len(nums)//2]

print(res)

