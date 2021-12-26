import sys
from collections import deque
si = sys.stdin.readline


def bfs(x, y):
  queue = deque([[x, y]])
  graph[x][y] = -1
  cnt = 1

  while queue:
    x, y = queue.popleft()
    
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
      nx, ny = x + dx, y + dy
      if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
        graph[nx][ny] = -1
        queue.append([nx, ny])
        cnt += 1

  return cnt


n, m = map(int, si().split())
x, y, d = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]

print(bfs(x, y))
