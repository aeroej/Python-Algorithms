import sys
si = sys.stdin.readline


def pawn():
  for i in range(0, num_p * 2, 2):
    x, y = p[i], p[i+1]
    graph[x][y] = 0  # 장애물


def knight():
  dx = [-2, -2, 2, 2, -1, -1, 1, 1]
  dy = [-1, 1, -1, 1, -2, 2, -2, 2]

  for i in range(0, num_k * 2, 2):
    x, y = k[i], k[i+1]
    graph[x][y] = 0  # 장애물

    for j in range(8):
      nx, ny = x + dx[j], y + dy[j]
      if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == -1:
        graph[nx][ny] = 1  # 안전 X


def queen():
  for i in range(0, num_q * 2, 2):
    x, y = q[i], q[i+1]
    graph[x][y] = 0  # 장애물
  
  dx = [-1, 1, 0, 0, -1, -1, 1, 1]
  dy = [0, 0, -1, 1, -1, 1, -1, 1]
  
  for i in range(0, num_q * 2, 2):
    x, y = q[i], q[i+1]

    for j in range(8):  # index of dx, dy
      for k in range(1, max(m, n)):
        nx, ny = x + dx[j]*k, y + dy[j]*k
        
        if (0 <= nx < n) and (0 <= ny < m):
          if graph[nx][ny] == -1:
            graph[nx][ny] = 1  # 안전 X
          elif graph[nx][ny] == 0: 
            break


n, m = map(int, si().split())
num_q, *q = map(int, si().split())
num_k, *k = map(int, si().split())
num_p, *p = map(int, si().split())

n += 1
m += 1
graph = [[-1 for _ in range(m)] for _ in range(n)]  # -1: 안전, 1: 안전 X, 0: 장애물

pawn()
knight()
queen()

cnt = 0
for i in range(1, n):
  for j in range(1, m):
    if graph[i][j] == -1:
      cnt += 1

print(cnt)
