
with open("in.txt") as f:
  lines = f.readlines()

diffs = []
res = 0
for l in lines:
  report = [int(a) for a in l.strip().split()]
  diffs = [report[i] - report[i-1] for i in range(1, len(report))]
  sign = all((diffs[i] > 0) == (diffs[0] > 0) for i in range(len(diffs)))
  diff = all(abs(diffs[i]) >= 1 and abs(diffs[i]) <= 3  for i in range(len(diffs)))
  res += (sign and diff)
print(res)






