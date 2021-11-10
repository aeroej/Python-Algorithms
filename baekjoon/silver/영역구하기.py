import sys
def input(): return sys.stdin.readline().split()
sys.setrecursionlimit(10**6)

m, n, k = map(int, input())
graph = [[0]*m for _ in range(n)]


for _ in range(k):
  xl, yl, xr, yr = map(int, input())

  for i in range(xl, xr):
    for j in range(yl, yr):
      graph[i][j] = -1


def dfs(x, y):
  if (0 <= x < n) and (0 <= y < m):
    if graph[x][y] == 0:
      graph[x][y] = 1
      res[-1] += 1
      dfs(x - 1, y)
      dfs(x + 1, y)
      dfs(x, y - 1)
      dfs(x, y + 1)
  return


res = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      res.append(0)
      dfs(i, j)


print(len(res))
print(*sorted(res))
