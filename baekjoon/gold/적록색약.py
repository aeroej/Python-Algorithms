import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, color):
  if (0<=x<n) and (0<=y<n):
    if visited[x][y] == 0:
      if graph[x][y] == color:
        visited[x][y] = 1
        dfs(x-1, y, color)
        dfs(x+1, y, color)
        dfs(x, y-1, color)
        dfs(x, y+1, color)
        return True
  return False

def dfs_color(x, y, color):
  if (0<=x<n) and (0<=y<n):
    if visited[x][y] == 0:
      if (graph[x][y] == color) or (color == 'R' and graph[x][y] == 'G'):
        visited[x][y] = 1
        dfs_color(x-1, y, color)
        dfs_color(x+1, y, color)
        dfs_color(x, y-1, color)
        dfs_color(x, y+1, color)
        return True
  return False

if __name__ == '__main__':
  n = int(input())
  graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

  # 적록색약이 아닌 사람
  visited = [[0 for _ in range(n)] for _ in range(n)]
  result = 0

  for i in range(n):
    for j in range(n):
      if dfs(i, j, graph[i][j]) == True:
        result += 1

  print(result, end=' ')

  # 적록색약인 사람
  visited = [[0 for _ in range(n)] for _ in range(n)]
  result = 0

  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'G':
        graph[i][j] = 'R'
      if dfs_color(i, j, graph[i][j]) == True:
        result += 1

  print(result)