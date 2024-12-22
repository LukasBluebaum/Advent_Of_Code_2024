import math

with open("in.txt") as f:
  lines = f.readlines()

def calc(n):
  t1 = n * 64
  t2 = n ^ t1
  t2 = t2 % 16777216

  t3 = math.floor(t2 / 32)
  t4 = t2 ^ t3
  t4 = t4 % 16777216

  t5 = t4 * 2048
  t6 = t5 ^ t4
  t6 = t6 % 16777216
  return t6

res = 0
for num in lines:
  num = int(num.strip())
  for _ in range(2000):
    num = calc(num)
  res += num
print(res)
