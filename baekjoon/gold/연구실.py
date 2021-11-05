import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
def input(): return sys.stdin.readline().split()

n, m = map(int, input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, graph, wall):
  for x, y in wall:
    graph[x][y] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < n) and (0 <= ny < m):
        if graph[nx][ny] == 0:
          graph[nx][ny] = 2
          queue.append([nx, ny])

  return graph


def cnt_safe(graph):
  cnt = 0
  for i in range(n):
    cnt += graph[i].count(0)
  return cnt


def main():
  graph = [list(map(int, input())) for _ in range(n)]
  res = 0

  queue = deque([])
  empty = deque([])

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        empty.append([i, j])
      elif graph[i][j] == 2:
        queue.append([i, j])

  for wall in list(combinations(empty, 3)):
    after_virus = bfs(deepcopy(queue), deepcopy(graph), wall)
    res = max(res, cnt_safe(after_virus))

  print(res)

main()
