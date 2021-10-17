# 'X': 방문여부 flag
import sys
from collections import deque

n, m = map(int, input().split())
campus = []
for i in range(n):
  inpuT = [_ for _ in sys.stdin.readline().rstrip()]
  if 'I' in inpuT:
    start = (i, inpuT.index('I'))  # (x, y)
  campus.append(inpuT)

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = start
campus[x][y] = 'X'
queue = deque([start]) 

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < n) and (0 <= ny < m):
      if campus[nx][ny] != 'X':  # 'P' or 'O'
        if campus[nx][ny] == 'P':
          cnt += 1
        campus[nx][ny] = 'X'
        queue.append((nx, ny))

print(cnt if cnt > 0 else 'TT')


# # visited 배열 사용
# import sys
# from collections import deque

# n, m = map(int, input().split())
# campus = []
# for i in range(n):
#   inpuT = list(map(str, sys.stdin.readline().rstrip()))
#   if 'I' in inpuT:
#     start = (i, inpuT.index('I'))
#   campus.append(inpuT)

# cnt = 0
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# visited = [[0 for _ in range(m)] for _ in range(n)]
# x, y = start
# visited[x][y] = 1
# queue = deque([start])

# while queue:
#   x, y = queue.popleft()
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if (0 <= nx < n) and (0 <= ny < m):
#       if visited[nx][ny] == 0:
#         visited[nx][ny] = 1
#         if campus[nx][ny] == 'X':
#           continue
#         elif campus[nx][ny] == 'P':
#           cnt += 1
#         queue.append((nx, ny))  # 'P' or 'O'

# print(cnt if cnt > 0 else 'TT')
