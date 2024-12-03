
with open("in.txt") as f:
  lines = f.readlines()

diffs = []
res = 0
for l in lines:
  report = [int(a) for a in l.strip().split()]
  for i in range(len(report)):
    report2 = list(report)
    del report2[i]

    diffs = [report2[i] - report2[i-1] for i in range(1, len(report2))]
    sign = all((diffs[i] > 0) == (diffs[0] > 0) for i in range(len(diffs)))
    diff = all(abs(diffs[i]) >= 1 and abs(diffs[i]) <= 3  for i in range(len(diffs)))
    if sign and diff:
      res += 1
      break
print(res)






