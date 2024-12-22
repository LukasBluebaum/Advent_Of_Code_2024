import math
from collections import deque

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


prices = {}
res = 0
for num in lines:
  changes = deque()
  num = int(num.strip())
  prev = num % 10

  monkey_prices = {}
  for _ in range(2000):
    num = calc(num)
    d = num % 10
    changes.append(d - prev)
    if len(changes) == 4:
      key = tuple(changes)
      if key not in monkey_prices:
        monkey_prices[key] = d
      changes.popleft()
    prev = d

  for key in monkey_prices:
    if key not in prices:
      prices[key] = 0
    prices[key] += monkey_prices[key]

print(max(prices.values()))
