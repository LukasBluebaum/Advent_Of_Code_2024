
with open("in.txt") as f:
  lines = f.readlines()

graph = {}
for l in lines:
  a, b = l.strip().split("-")
  if a not in graph:
    graph[a] = set()
  if b not in graph:
    graph[b] = set()
  graph[a].add(b)
  graph[b].add(a)


dp = {}
def dfs(node, current):
  key = (node, tuple(current))
  if key in dp:
    return dp[key]

  s = ','.join(sorted(current))
  for nb in graph[node]:
    if nb not in current and sum(nb2 in current for nb2 in graph[nb]) == len(current):
      current.add(nb)
      ss = dfs(nb, current)
      if len(s) < len(ss):
        s = ss
      current.remove(nb)
  dp[key] = s
  return s

res = 0
for node in graph:
  s = dfs(node, set([node]))
  if len(s) > res:
    res = len(s)
    print(s)

