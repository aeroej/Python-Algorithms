import sys
si = sys.stdin.readline

n = int(si())

x, y = 0, 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for move in si().split():
  if move == 'L':
    i = 0
  elif move == 'R':
    i = 1
  elif move == 'U':
    i = 2
  elif move == 'D':
    i = 3
  
  nx, ny = x + dx[i], y + dy[i]
  if (0 <= nx < n) and (0 <= ny < n):
    x, y = nx, ny

print(x + 1, y + 1)
