import sys
si = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(v, h):
  global cnt

  if v != 1 and len(graph[v]) == 1:  # leaf node
    cnt += h
    return

  for node in graph[v]:
    if not visited[node]:
      visited[node] = 1
      dfs(node, h + 1)


n = int(si())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int, si().split())
  graph[a].append(b)
  graph[b].append(a)

cnt = 0
visited = [0 for _ in range(n+1)]

visited[1] = 1
dfs(1, 0)
print("Yes" if cnt % 2 else "No")
