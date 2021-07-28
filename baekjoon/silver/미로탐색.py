import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  queue = deque([(x, y)])
  visited[x][y] = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (-1<nx<N) and (-1<ny<M) and graph[nx][ny] and not visited[nx][ny]:
        queue.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
  return visited[N-1][M-1]

print(bfs(0, 0))