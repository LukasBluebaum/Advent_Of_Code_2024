with open("in.txt") as f:
  nums = f.readlines()[0].strip().split(" ")
  nums = [int(n) for n in nums]

dp = {}
def dfs(i, n):
  key = (i, n)
  if i == 75:
    return 1
  if key in dp:
    return dp[key]

  s = str(n)
  res = 0
  if n == 0:
    res = dfs(i+1, 1)
  elif len(s) % 2 == 0:
    res += dfs(i+1, int(s[:len(s)//2])) + dfs(i+1, int(s[len(s)//2:]))
  else:
    res = dfs(i+1, n * 2024)
  dp[key] = res
  return res


res = 0
for n in nums:
  res += dfs(0, n)
print(res)

