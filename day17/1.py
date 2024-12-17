import re, math

def get_combo(val, a, b, c):
  if val <= 3:
    return val
  elif val == 4:
    return a
  elif val == 5:
    return b
  elif val == 6:
    return c

with open("example2.txt") as f:
  lines = ''.join(f.readlines())
  nums = re.findall("\d+", lines)

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
nums = nums[3:]
i = 0
outputs = []
while i < len(nums):
  ins, op = int(nums[i]), int(nums[i+1])
  if ins == 0:
    a = math.trunc(a / 2**get_combo(op, a, b, c))
  elif ins == 1:
    b = b ^ op
  elif ins == 2:
    b = get_combo(op, a, b, c) % 8
  elif ins == 3:
    i = i if a == 0 else op - 2
  elif ins == 4:
    b ^= c
  elif ins == 5:
    outputs.append(str(get_combo(op, a, b, c) % 8))
  elif ins == 6:
    b = math.trunc(a / 2**get_combo(op, a, b, c))
  elif ins == 7:
    c = math.trunc(a / 2**get_combo(op, a, b, c))
  i += 2

print(a, b, c)
print(','.join(outputs))
