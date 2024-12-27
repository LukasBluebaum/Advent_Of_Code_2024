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
highest_z = "z00"
for op in ops[:-1]:
  wires = op.strip().split(" ")
  queue.append(wires)
  if wires[-1][0] == "z" and int(wires[-1][1:]) > int(highest_z[1:]):
    highest_z = wires[-1]

wrong = set()
for op1, op, op2, _, res in queue:
    if res[0] == "z" and op != "XOR" and res != highest_z:
        wrong.add(res)
    if (
        op == "XOR"
        and res[0] not in ["x", "y", "z"]
        and op1[0] not in ["x", "y", "z"]
        and op2[0] not in ["x", "y", "z"]
    ):
        wrong.add(res)
    if op == "AND" and "x00" not in [op1, op2]:
        for subop1, subop, subop2, _, subres in queue:
            if (res == subop1 or res == subop2) and subop != "OR":
                wrong.add(res)
    if op == "XOR":
        for subop1, subop, subop2, _, subres in queue:
            if (res == subop1 or res == subop2) and subop == "OR":
                wrong.add(res)

print(','.join(sorted(wrong)))
