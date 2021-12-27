import sys
si = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def get_cntW(x, y):
  cntW = 0
  for i in range(8):  # direction
    cnt = 0
    for j in range(1, 8):  # 이동하는 칸수
      nx, ny = x + dx[i]*j, y + dy[i]*j
      if (0 <= nx < 8) and (0 <= ny < 8):
        if graph[nx][ny] == '.':
          break
        elif graph[nx][ny] == 'W':
          cnt += 1
        elif graph[nx][ny] == 'B':
          cntW += cnt
          break

  return cntW
  

graph = [si().rstrip() for _ in range(8)]
max_cntW = 0

for x in range(8):
  for y in range(8):
    if graph[x][y] == '.':
      max_cntW = max(max_cntW, get_cntW(x, y))

print(max_cntW)
