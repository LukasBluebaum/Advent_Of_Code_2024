with open("in.txt") as f:
  lines = ''.join(f.readlines())
  towels, patterns = lines.split("\n\n")
  towels = {t.strip() for t in towels.split(",")}
  patterns = patterns.split("\n")[:-1]

def find(i, word, dp, towels):
  if i == len(word):
    return 1
  if i in dp:
    return dp[i]
  current = ''
  res = 0
  for j in range(i, len(word)):
    current += word[j]
    if current in towels:
      res += find(j+1, word, dp, towels)
  dp[i] = res
  return res

res = 0
for p in patterns:
  res += find(0, p, {}, towels)
print(res)
