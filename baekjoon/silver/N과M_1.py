def dfs(v):
  if v >= m:
    print(*res)
    return

  for i in range(1, n+1):
    if visited[i] == 0:
      visited[i] = 1
      res.append(i)
      dfs(v+1)

      visited[i] = 0
      res.pop()


if __name__ == "__main__":
  n, m = map(int, input().split())
  visited = [0]*(n+1)
  res = []

  dfs(0)
