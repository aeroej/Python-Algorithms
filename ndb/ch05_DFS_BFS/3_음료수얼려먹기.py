import sys
si = sys.stdin.readline

def dfs(x, y):
  for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
    nx, ny = x + dx, y + dy
    if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
      graph[nx][ny] = 1
      dfs(nx, ny)
  return


n, m = map(int, si().split())
graph = [list(map(int, si().rstrip())) for _ in range(n)]
cnt = 0

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      graph[i][j] = 1
      dfs(i, j)
      cnt += 1
      
print(cnt)
