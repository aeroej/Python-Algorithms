import sys
sys.setrecursionlimit(10 ** 6)
si = sys.stdin.readline

move = [
  (-1, 0), (1, 0), (0, -1), (0, 1),
  (-1, -1), (-1, 1), (1, -1), (1, 1)
]

def dfs(x, y):
  for dx, dy in move:
    nx, ny = x + dx, y + dy
    if (0 <= nx < h) and (0 <= ny < w):
      if not visited[nx][ny] and graph[nx][ny]:
        visited[nx][ny] = 1
        dfs(nx, ny)
  return

while True:
  w, h = map(int, si().split())
  if w == h == 0:
    break

  graph = [list(map(int, si().split())) for _ in range(h)]
  visited = [[0]*w for _ in range(h)]

  cnt = 0
  for i in range(h):
    for j in range(w):
      if not visited[i][j] and graph[i][j]:
        visited[i][j] = 1
        cnt += 1
        dfs(i, j)

  print(cnt)
