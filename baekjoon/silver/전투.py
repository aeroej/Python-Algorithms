import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [input() for _ in range(m)]
visited = [[0]*n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
  power = 1
  queue = deque([[x, y]])

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if (0 <= nx < m) and (0 <= ny < n):
        if graph[nx][ny] == color and visited[nx][ny] == 0:
          visited[nx][ny] = 1
          queue.append([nx, ny])
          power += 1

  return power


res = [0, 0]

for i in range(m):
  for j in range(n):
    if visited[i][j] == 0:
      visited[i][j] = 1

      if graph[i][j] == 'W':
        res[0] += bfs(i, j, 'W') ** 2
      else:
        res[1] += bfs(i, j, 'B') ** 2

print(*res)