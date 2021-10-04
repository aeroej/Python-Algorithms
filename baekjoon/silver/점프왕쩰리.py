import sys
from collections import deque

n = int(input())
visited = [[0]*n for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
  visited[x][y] = 1
  queue = deque([(x, y)])

  while queue:
    x, y = queue.popleft()

    if graph[x][y] == -1:
      print('HaruHaru') 
      sys.exit(0)
    
    for i in range(4):
      nx, ny = x + dx[i]*graph[x][y], y + dy[i]*graph[x][y]
      if 0 <= nx < n and 0 <= ny < n:  # 경계값확인
        if not visited[nx][ny]:
          visited[nx][ny] = 1
          queue.append([nx, ny])


BFS(0, 0)
print('Hing')

