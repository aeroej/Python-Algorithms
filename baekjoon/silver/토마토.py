# tistory
# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)

# def dfs(x, y):
#   if (0<=x<m) and (0<=y<n) and visited[y][x] == 0:
#     visited[y][x] = 1
#     if graph[y][x] == -1:
#       return 
#     if graph[y][x] == 1:
#       dfs(x, y-1)
#       dfs(x, y+1)
#       dfs(x-1, y)
#       dfs(x+1, y)
#     if graph[y][x] == 0:
#       graph[y][x] = 1
#       queue_x.append(x)
#       queue_y.append(y)
#     return True

# if __name__ == "__main__":
#   m, n = map(int, input().split())
#   graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
#   visited = [[0 for _ in range(m)] for _ in range(n)]

#   queue_x = deque([])
#   queue_y = deque([])
#   flag_0 = False 

#   for i in range(n):
#     if 1 in graph[i]:
#       for j in range(m):
#         if graph[i][j] == 1:
#           queue_x.append(j)
#           queue_y.append(i)
#     if 0 in graph[i]:
#       flag_0 = True

#   if flag_0 == False:  # 0이 하나도 없는 경우 (모두 익은 경우)
#     print(0)
#     sys.exit(0)

#   result = 0
#   while len(queue_x) != 0:
#     l = len(queue_x)
#     for _ in range(l):
#       x = queue_x.popleft()
#       y = queue_y.popleft()
#       visited[y][x] = 0
#       dfs(x, y)
#     result += 1

#   for i in graph:  # 0이 남아있는 경우 (모두 익지는 못할 때)
#     if 0 in i:
#       print(-1)
#       sys.exit(0)

#   print(result-1)



import sys
from collections import deque
def input(): return sys.stdin.readline().split()

m, n = map(int, input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
  day = 0
  queue = deque([])

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        queue.append([i, j])

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if (0 <= nx < n) and (0 <= ny < m):
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1
          queue.append([nx, ny])
          day = graph[x][y]
  
  return day


def haszero():
  for i in range(n):
    if 0 in graph[i]:
      return True
  return False


res = bfs()
print(res if not haszero() else -1)
