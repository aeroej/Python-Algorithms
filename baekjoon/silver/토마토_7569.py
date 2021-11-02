from collections import deque
import sys
input = lambda: sys.stdin.readline().split()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs() -> int:
  day = 0
  queue = deque([])

  for i in range(h):
    for j in range(n):
      for k in range(m):
        if tomato[i][j][k] == 1:
          queue.append([i, j, k])

  while queue:
    x, y, z = queue.popleft()
    
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if (0 <= nx < h) and (0 <= ny < n) and (0 <= nz < m):
        if tomato[nx][ny][nz] == 0:
          tomato[nx][ny][nz] = tomato[x][y][z] + 1
          queue.append([nx, ny, nz])
          day = tomato[x][y][z]

  return day


def haszero() -> bool:
  for i in range(h):
    for j in range(n):
      if 0 in tomato[i][j]:
        return True
  return False


if __name__ == '__main__':
  m, n, h = map(int, input())
  tomato = [[list(map(int, input())) for _ in range(n)] for _ in range(h)]
  
  res = bfs()
  print(res if not haszero() else -1)

