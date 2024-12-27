
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


res = set()
for node in graph:
  if node[0] == 't':
    for n1 in graph[node]:
      for n2 in graph[node]:
        if n1 != n2:
          if n1 in graph[n2] and n2 in graph[n1]:
            res.add(''.join(sorted([node, n1, n2])))

print(len(res))

