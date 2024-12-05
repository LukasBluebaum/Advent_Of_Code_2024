from collections import defaultdict

with open("in.txt") as f:
  lines = f.readlines()
  order, updates = ''.join(lines).split("\n\n")
  order = order.split("\n")
  updates = updates.split("\n")

after = defaultdict(set)
for o in order:
  a, b = o.split("|")
  after[int(a)].add(int(b))

res = 0
for u in updates[:-1]:
  nums = u.split(",")
  seen = set()
  for n in nums:
    if len(after[int(n)] & seen) != 0:
      break
    seen.add(int(n))
  else:
    res += int(nums[len(nums)//2])

print(res)

