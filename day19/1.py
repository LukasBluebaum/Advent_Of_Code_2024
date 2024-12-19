with open("in.txt") as f:
  lines = ''.join(f.readlines())
  towels, patterns = lines.split("\n\n")
  towels = {t.strip() for t in towels.split(",")}
  patterns = patterns.split("\n")[:-1]

def find(i, word, dp, towels):
  if i == len(word):
    return True
  if i in dp:
    return dp[i]
  current = ''
  for j in range(i, len(word)):
    current += word[j]
    if current in towels and find(j+1, word, dp, towels):
      dp[i] = True
      return True
  dp[i] = False
  return False

res = 0
for p in patterns:
  if find(0, p, {}, towels):
    res += 1
print(res)
