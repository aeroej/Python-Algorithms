import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def bfs_color(x, y, color):
  queue = deque([[x, y]])
  while queue:
    x, y = queue.popleft()
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
      nx, ny = x + dx, y + dy
      if (0 <= nx < n) and (0 <= ny < n) and not visited_color[nx][ny]:
        if graph[nx][ny] == color:
          visited_color[nx][ny] = 1
          queue.append([nx, ny])


def bfs_blind(x, y, color):
  queue = deque([[x, y]])
  while queue:
    x, y = queue.popleft()
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
      nx, ny = x + dx, y + dy
      if (0 <= nx < n) and (0 <= ny < n) and not visited_blind[nx][ny]:
        if color == 'B' == graph[nx][ny]:  # (b, b)
          visited_blind[nx][ny] = 1
          queue.append([nx, ny])
        elif color != 'B' and graph[nx][ny] != 'B':  # (c, g) -> (r, r) (g, g) (r, g) (g, r)
          visited_blind[nx][ny] = 1
          queue.append([nx, ny])


n = int(input())
graph = [input() for _ in range(n)]
visited_color = [[0]*n for _ in range(n)]
visited_blind = [[0]*n for _ in range(n)]

cnt = [0, 0]
for i in range(n):
  for j in range(n):
    if not visited_color[i][j]:
      visited_color[i][j] = 1
      cnt[0] += 1
      bfs_color(i, j, graph[i][j])

    if not visited_blind[i][j]:
      visited_blind[i][j] = 1
      cnt[1] += 1
      bfs_blind(i, j, graph[i][j])

print(*cnt)
