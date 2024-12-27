from collections import deque

with open("in.txt") as f:
  lines, ops = ''.join(f.readlines()).split("\n\n")
  lines = lines.split("\n")
  ops = ops.split("\n")

start = {}
for l in lines:
  wire, val = l.strip().split(": ")
  start[wire] = int(val)

queue = deque()
for op in ops[:-1]:
  wires = op.strip().split(" ")
  queue.append(wires)

res = 0
while len(queue) > 0:
  wires = queue.popleft()
  if wires[0] not in start or wires[2] not in start:
    queue.append(wires)
    continue
  if wires[1] == 'AND':
    val = start[wires[0]] & start[wires[2]]
  elif wires[1] == 'OR':
    val = start[wires[0]] | start[wires[2]]
  if wires[1] == 'XOR':
    val = start[wires[0]] ^ start[wires[2]]
  start[wires[-1]] = val
  if wires[-1][0] == 'z':
    res += 2**int(wires[-1][1:]) * val
print(res)
